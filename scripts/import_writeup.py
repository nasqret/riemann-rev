#!/usr/bin/env python3
"""Import the write-up of the condensed proof (lsernau/grh-lean, edition grh-compact) into writeup/ for publication.

    python3 -B scripts/import_writeup.py                                  # the workspace's place: private/config.json
    python3 -B scripts/import_writeup.py --public-clone DIR --edition "29: what changed"

The write-up is made in a Readback workspace (structured proofs checked by program against the pinned Lean source,
notes written from them, an independent second reading, referee reports). This script copies what a reader or an
agent needs, and nothing else:

* handout.pdf (overview, the notes in the order of the argument, the condensed catalogue, the record of checks),
  catalogue-full.pdf, and overview.tex;
* chapters/: the handout cut at the top level of its outline into the front matter (title page, summary, contents,
  overview), one PDF per chapter (chapter-1.pdf ... chapter-8.pdf) and the back matter (the catalogue and the record
  of checks). Every link survives: a link to a page of the same part is kept, a link into another part becomes a link
  to that page of that part on the site; the links of every page are counted against the handout's (pdfinfo -url);
* the sources of every note whose last build reported no problem other than overfull lines:
  notes/<slug>/{<slug>.tex, data.tex, spec.json, concordance.json, reader.json} and the macro files the manuscript
  loads from its folder (so that each source builds alone);
* the structured proofs of every unit: structured-proofs/<id>/{unit.json, check.json, README.md, CORRECTIONS.md,
  proofs/*.json} (the merged units, not their chunks; not the generators);
* catalogue/catalogue.json (every background declaration the argument uses, classified) and
  catalogue/second-reading-verdicts.json (the second reader's comparison of each named theorem with its published
  statement: the verdict, the comparison, the sources, the place in the Lean source);
* reading/, when the workspace has built it (book/reading/reading-handout.pdf): the reading edition, the same text
  without the links to the Lean source, cut into chapters like the handout (or, if its outline has no chapters,
  with the chapter PDFs of book/reading/chapters/);
* browse/, when the workspace has built it as a static site of at most 100 MiB (site/index.html): the annotated
  version for the browser, copied whole;
* editions.json: every published edition, derived from the history of a clone of the public repository (an edition
  is a commit "feat(writeup): edition N: ..."; edition 1 is the commit that added the handout): its number, date,
  description, commit and the SHA-256 of its handout; and the current edition. The clone is given by --public-clone,
  the environment variable PUBLIC_CLONE or "public_clone" in private/config.json; without one the archive of the
  previous import is kept as it was;
* MANIFEST.json: the pin, the edition, counts, the chapters, and the SHA-256 of every file.

Texts are rewritten by the private patterns of private/writeup-scrub.json (how the second reader and its messages
are named); a text that still matches its forbidden patterns or private/leak-patterns.txt stops the import, and so
does a PDF whose text or metadata does. Hand-written files of writeup/ (README.md, AGENTS.md) are kept.
"""
import argparse
import bisect
import collections
import datetime
import gzip
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.parse
from pathlib import Path

try:
    from pypdf import PdfReader, PdfWriter
    from pypdf.generic import (ArrayObject, ByteStringObject, DictionaryObject, IndirectObject, NameObject,
                               NumberObject, TextStringObject)
except ImportError:
    sys.exit("import_writeup: needs pypdf to cut the handout into chapters (python3 -m pip install pypdf)")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from build_readme import REPO, SITE  # noqa: E402

OUT = ROOT / "writeup"
KEEP = {"README.md", "AGENTS.md"}
# The patterns of what is rewritten or refused are private (they name what must not appear in public files):
# private/writeup-scrub.json, {"scrub": [[regex, replacement], ...], "forbidden": regex}, and the patterns of the
# export's leak scan, private/leak-patterns.txt (one case-insensitive regex per line).
_PRIV = json.loads((ROOT / "private" / "writeup-scrub.json").read_text(encoding="utf-8"))
SCRUB = [(re.compile(a), b) for a, b in _PRIV["scrub"]]
FORBIDDEN = re.compile(_PRIV["forbidden"])
LEAKS = [re.compile(line.strip(), re.I)
         for line in (ROOT / "private" / "leak-patterns.txt").read_text(encoding="utf-8").splitlines()
         if line.strip() and not line.startswith("#")]
ARTIFACT = "https://github.com/lsernau/grh-lean"
BROWSE_MAX = 100 * 2**20            # the workspace's site/ is the static edition only when it is at most this large
# Strings of third-party code (files under a folder vendor/ of the site) that match a forbidden pattern without naming
# anything private: the default home directory of the Emscripten runtime in PDF.js's image decoders.
THIRD_PARTY = ('"/home/web_user"', '"PT Astra Serif"')   # a PDF.js path string; a font name in PDF.js's substitution table
EDITION = re.compile(r"feat\(writeup\): edition (\d+): (.+)")
ROMAN = re.compile(r"(?P<numeral>[IVXLCDM]+)\.\s+(?P<title>\S.*)")      # a chapter of the outline: "V. Theorem A: ..."
NUMBERED = re.compile(r"^\d+(?:\.\d+)*\s+")                              # "0.8 The seesaw identity" -> its title


def scrub_text(s: str) -> str:
    for pat, rep in SCRUB:
        s = pat.sub(rep, s)
    for _, rep in SCRUB:            # a name that stood alone in a formula ($...$) is words now, not mathematics
        s = s.replace(f"${rep}$", rep)
    return s


def leak(s: str) -> str | None:
    """What in s must not be published (the forbidden patterns and the leak patterns), or None."""
    m = FORBIDDEN.search(s)
    if m:
        return m.group(0)
    for pat in LEAKS:
        m = pat.search(s)
        if m:
            return m.group(0)
    return None


def check_text(s: str, where) -> None:
    hit = leak(s)
    if hit:
        sys.exit(f"import_writeup: {where} contains a private name or path ({hit!r}); not imported")


def copy_text(src: Path, dst: Path) -> None:
    s = scrub_text(src.read_text(encoding="utf-8"))
    check_text(s, src)
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(s, encoding="utf-8")


def check_pdf(path: Path, where) -> None:
    """A PDF is checked through its metadata and its text (as the export's leak scan reads it)."""
    with open(path, "rb") as fh:
        if fh.read(5) != b"%PDF-":
            sys.exit(f"import_writeup: {where} is not a PDF; not imported")
    info = subprocess.run(["pdfinfo", str(path)], capture_output=True, text=True, check=True).stdout
    text = subprocess.run(["pdftotext", str(path), "-"], capture_output=True, text=True, check=True).stdout
    check_text(info + text, where)


def copy_pdf(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    check_pdf(dst, src)


def pdf_facts(path: Path) -> dict:
    return {"pages": len(PdfReader(path).pages), "bytes": path.stat().st_size}


def urls_by_page(pdf: Path) -> dict[int, list[str]]:
    """The targets of the external links of a PDF, by page (counted from 1), as pdfinfo -url lists them."""
    out = collections.defaultdict(list)
    listing = subprocess.run(["pdfinfo", "-url", str(pdf)], capture_output=True, text=True, check=True).stdout
    for line in listing.splitlines()[1:]:
        fields = line.split(None, 2)
        if len(fields) == 3 and fields[0].isdigit():
            out[int(fields[0])].append(fields[2].strip())
    return out


# ---------------------------------------------------------------------------------------------- the chapter PDFs
def outline_top(reader: PdfReader) -> list[tuple[str, int | None, list[tuple[str, int | None]]]]:
    """The top level of the outline: (title, page index, [(title, page index) of its children])."""
    def page(item):
        try:
            return reader.get_destination_page_number(item)
        except Exception:      # an entry whose destination does not resolve has no page
            return None
    top = []
    for item in reader.outline:
        if isinstance(item, list):
            if top:
                top[-1][2].extend((c.title, page(c)) for c in item if not isinstance(c, list))
            continue
        top.append((item.title, page(item), []))
    return top


def annotations(page) -> list:
    annots = page.get("/Annots")
    return [a.get_object() for a in annots.get_object()] if annots is not None else []


def link_target(reader: PdfReader, annot, pages_by_id: dict, named: dict) -> tuple[bool, int | None]:
    """(is it a link inside the document, the page index it leads to or None)."""
    if annot.get("/Subtype") != "/Link":
        return False, None
    action = annot.get("/A")
    if action is not None:
        action = action.get_object()
        if action.get("/S") != "/GoTo":
            return False, None
        dest = action.get("/D")
    else:
        dest = annot.get("/Dest")
    if dest is None:
        return False, None
    dest = dest.get_object() if isinstance(dest, IndirectObject) else dest
    if isinstance(dest, ArrayObject):
        ref = dest[0] if len(dest) else None
        return True, pages_by_id.get(ref.idnum) if isinstance(ref, IndirectObject) else None
    name = dest.decode("latin-1") if isinstance(dest, ByteStringObject) else str(dest)
    target = named.get(name)
    return True, (reader.get_destination_page_number(target) if target is not None else None)


def label_tree(labels: list[str]) -> DictionaryObject:
    """/PageLabels for pages labelled as in the source (runs of decimal labels; any other label as a prefix)."""
    nums, prev = ArrayObject(), None
    for i, label in enumerate(labels):
        decimal = label.isdigit() and int(label) >= 1
        if decimal and prev is not None and prev.isdigit() and int(label) == int(prev) + 1:
            prev = label
            continue
        style = ({NameObject("/S"): NameObject("/D"), NameObject("/St"): NumberObject(int(label))} if decimal
                 else {NameObject("/P"): TextStringObject(label)})
        nums += [NumberObject(i), DictionaryObject(style)]
        prev = label
    return DictionaryObject({NameObject("/Nums"): nums})


def contents_page(pdf: Path, last: int) -> int | None:
    """The page index of the table of contents among the pages 0..last, found by its heading."""
    text = subprocess.run(["pdftotext", "-f", "1", "-l", str(last + 1), str(pdf), "-"],
                          capture_output=True, text=True, check=True).stdout
    for i, page in enumerate(text.split("\f")):
        lines = [line.strip() for line in page.splitlines() if line.strip()]
        if lines and lines[0] == "Contents":
            return i
    return None


def split_pdf(src: Path, dest: Path, url: str, strict: bool = True) -> tuple[list[dict], dict] | None:
    """Cut a PDF at the top level of its outline: the front matter (the pages before the first chapter, an entry
    "I. Title"), one PDF per chapter, and the back matter (from the first entry after the last chapter). The parts
    are written to dest as front-matter.pdf, chapter-<k>.pdf, back-matter.pdf; `url` is their folder on the site.
    Kept in every part: its outline, its named destinations, the page labels of the source, the language. Returns
    (the parts, counts of the links), or None if the outline has no chapter. A link of the source that leads nowhere
    stops the import if `strict`, and is otherwise left out of the parts and counted."""
    reader = PdfReader(src)
    n = len(reader.pages)
    top = outline_top(reader)
    chapters = [(k, entry) for k, entry in enumerate(top) if ROMAN.fullmatch(entry[0]) and entry[1] is not None]
    if not chapters:
        return None
    labels = reader.page_labels
    named = reader.named_destinations
    note_at = {}                         # the first page of each note of the handout: its destination note:<slug>.1
    for name, d in named.items():
        m = re.fullmatch(r"note:(.+)\.1", name)
        if m:
            note_at[reader.get_destination_page_number(d)] = m.group(1)

    first = chapters[0][1][1]
    after = [entry for entry in top[chapters[-1][0] + 1:] if entry[1] is not None]
    back = after[0][1] if after else n
    parts = []
    if first > 0:
        heads = [(p, t) for t, p, _ in top[:chapters[0][0]] if p is not None and p < first]
        c = contents_page(src, first - 1)
        if c is not None:
            heads.append((c, "Contents"))
        if not any(p == 0 for p, _ in heads):
            heads.append((0, "Title page"))
        parts.append({"file": "front-matter.pdf", "part": "Front matter",
                      "title": " · ".join(t for _, t in sorted(heads, key=lambda h: h[0])),
                      "start": 0, "end": first - 1, "sections": []})
    for j, (_, (title, p, kids)) in enumerate(chapters):
        end = (chapters[j + 1][1][1] if j + 1 < len(chapters) else back) - 1
        m = ROMAN.fullmatch(title)
        sections = [{"title": NUMBERED.sub("", t, count=1), "page": labels[q], **({"note": note_at[q]} if q in note_at else {})}
                    for t, q in kids if q is not None]
        parts.append({"file": f"chapter-{j + 1}.pdf", "part": f"Chapter {m['numeral']}", "numeral": m["numeral"],
                      "title": m["title"], "start": p, "end": end, "sections": sections})
    if back < n:
        parts.append({"file": "back-matter.pdf", "part": "Back matter", "title": " · ".join(t for t, _, _ in after),
                      "start": back, "end": n - 1, "sections": []})
    if [p["start"] for p in parts] != sorted({p["start"] for p in parts}) or any(p["end"] < p["start"] for p in parts):
        sys.exit(f"import_writeup: the outline of {src.name} does not cut it into consecutive parts")

    # A link into another part leads to that page of that part on the site (the reader's objects are changed in
    # memory before any part is written, so every part sees the change).
    starts = [p["start"] for p in parts]
    part_of = lambda i: bisect.bisect_right(starts, i) - 1                # noqa: E731
    pages_by_id = {pg.indirect_reference.idnum: i for i, pg in enumerate(reader.pages)}
    moved = collections.defaultdict(list)        # page index -> the new targets of its links into other parts
    internal = dangling = 0
    for i, page in enumerate(reader.pages):
        for annot in annotations(page):
            inside, target = link_target(reader, annot, pages_by_id, named)
            if not inside:
                continue
            if target is None:
                if strict:
                    sys.exit(f"import_writeup: a link on page {i + 1} of {src.name} leads nowhere")
                dangling += 1                    # the parts leave it out (pypdf drops a link to nowhere)
                continue
            internal += 1
            q = part_of(target)
            if q == part_of(i):
                continue
            to = f"{url}{parts[q]['file']}#page={target - parts[q]['start'] + 1}"
            annot[NameObject("/A")] = DictionaryObject({NameObject("/S"): NameObject("/URI"),
                                                        NameObject("/URI"): TextStringObject(to)})
            if "/Dest" in annot:
                del annot["/Dest"]
            moved[i].append(to)

    dest.mkdir(parents=True, exist_ok=True)
    doc = str((reader.metadata or {}).get("/Title") or src.stem)
    lang = reader.root_object.get("/Lang")
    for p in parts:
        w = PdfWriter()
        w.append(reader, pages=(p["start"], p["end"] + 1), import_outline=True)
        name = f"Chapter {p['numeral']}. {p['title']}" if "numeral" in p else (
            p["part"] if p["file"] == "front-matter.pdf" else p["title"])
        w.add_metadata({"/Title": f"{name} — {doc}",
                        "/Subject": f"Pages {labels[p['start']]}–{labels[p['end']]} of {doc}"})
        w.root_object[NameObject("/PageLabels")] = label_tree(labels[p["start"]:p["end"] + 1])
        if lang is not None:
            w.root_object[NameObject("/Lang")] = TextStringObject(str(lang))
        if len(w.outline):
            w.page_mode = "/UseOutlines"
        with open(dest / p["file"], "wb") as fh:
            w.write(fh)

    # The check: every external link of every page is in its part, and every link inside a part resolves there.
    want = urls_by_page(src)
    kept = 0
    for k, p in enumerate(parts):
        f = dest / p["file"]
        have = urls_by_page(f)
        for local in range(1, p["end"] - p["start"] + 2):
            i = p["start"] + local - 1
            if collections.Counter(have.get(local, [])) != collections.Counter(want.get(i + 1, []) + moved.get(i, [])):
                sys.exit(f"import_writeup: the links of page {i + 1} of {src.name} did not survive in {f.name}")
        part = PdfReader(f)
        if len(part.pages) != p["end"] - p["start"] + 1:
            sys.exit(f"import_writeup: {f.name} has {len(part.pages)} pages, not {p['end'] - p['start'] + 1}")
        ids = {pg.indirect_reference.idnum: i for i, pg in enumerate(part.pages)}
        dests = part.named_destinations
        for i, page in enumerate(part.pages):
            for annot in annotations(page):
                inside, target = link_target(part, annot, ids, dests)
                if inside and target is None:
                    sys.exit(f"import_writeup: a link on page {i + 1} of {f.name} leads nowhere")
                kept += inside
        check_pdf(f, f)
        p.update({"first_page": labels[p["start"]], "last_page": labels[p["end"]], "pages": len(part.pages),
                  "bytes": f.stat().st_size, "links": sum(len(v) for v in have.values()),
                  "links_to_other_parts": sum(len(moved.get(i, [])) for i in range(p["start"], p["end"] + 1))})
    n_moved = sum(len(v) for v in moved.values())
    if kept != internal - n_moved:
        sys.exit(f"import_writeup: {internal - n_moved - kept} internal links of {src.name} were lost in the parts")
    counts = {"external": sum(len(v) for v in want.values()), "internal": internal, "to_other_parts": n_moved,
              **({"leading_nowhere": dangling} if dangling else {})}
    for p in parts:
        del p["start"], p["end"]
    return parts, counts


# ------------------------------------------------------------------------------------- the reading edition, browse
def import_reading(ws: Path) -> dict | None:
    src = ws / "book" / "reading"
    pdf = src / "reading-handout.pdf"
    if not pdf.is_file():
        print("reading edition: not built in the workspace yet (book/reading/reading-handout.pdf); not imported")
        return None
    dst = OUT / "reading"
    copy_pdf(pdf, dst / "reading-handout.pdf")
    info = {"file": "reading/reading-handout.pdf", **pdf_facts(dst / "reading-handout.pdf"),
            "links_to_lean": sum(u.startswith(ARTIFACT) for v in urls_by_page(dst / "reading-handout.pdf").values()
                                 for u in v)}
    cut = split_pdf(dst / "reading-handout.pdf", dst / "chapters", f"{SITE}/writeup/reading/chapters/", strict=False)
    if cut is not None:
        info["chapters"], info["chapter_links"] = [{**p, "file": f"reading/chapters/{p['file']}"} for p in cut[0]], cut[1]
        if cut[1].get("leading_nowhere"):
            print(f"WARNING: {cut[1]['leading_nowhere']} links of the reading edition lead nowhere; its chapters leave "
                  "them out")
    else:                    # an outline without chapters: the chapter PDFs that the workspace made, if any
        info["chapters"] = []
        given = sorted((src / "chapters").glob("*.pdf"), key=lambda f: (f.stem != "front-matter", f.stem == "back-matter",
                                                                       roman(f.stem) or 0, f.stem))
        for f in given:      # I.pdf, II.pdf, ... are named as the handout's parts: chapter-1.pdf, chapter-2.pdf, ...
            name = f"chapter-{roman(f.stem)}.pdf" if roman(f.stem) else f.name
            copy_pdf(f, dst / "chapters" / name)
            title = str((PdfReader(f).metadata or {}).get("/Title") or f.stem)
            info["chapters"].append({"file": f"reading/chapters/{name}", "part": f.stem, "title": title,
                                     **pdf_facts(dst / "chapters" / name)})
    if info["links_to_lean"]:
        print(f"WARNING: the reading edition has {info['links_to_lean']} links to the Lean source; it should have none")
    return info


def roman(s: str) -> int | None:
    """The value of an upper-case Roman numeral (I, II, ..., VIII, ...), or None."""
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if not s or any(c not in values for c in s):
        return None
    total = sum(-values[a] if values[a] < values[b] else values[a] for a, b in zip(s, s[1:])) + values[s[-1]]
    return total if total > 0 else None


def printable(data: bytes) -> str:
    """The runs of printable characters of a binary file, as `strings` gives them."""
    return "\n".join(m.decode("ascii") for m in re.findall(rb"[\x20-\x7e]{4,}", data))


def import_browse(ws: Path) -> dict | None:
    """The workspace's static site (site/) into writeup/browse/: every text file scrubbed and checked, every PDF
    checked through its text, every other file through its printable strings. Links that do not resolve inside
    writeup/ are reported."""
    site = ws / "site"
    if not (site / "index.html").is_file():
        print("browse: the workspace has no static site yet (site/index.html); not imported")
        return None
    root = site.resolve()
    files = [p for p in sorted(site.rglob("*")) if (p.is_file() or p.is_symlink())
             and not any(x.startswith(".") or x == "__pycache__" for x in p.relative_to(site).parts)]
    for p in files:
        if p.is_symlink() and (root not in p.resolve().parents or not p.resolve().is_file()):
            sys.exit(f"import_writeup: {p} is a link that leaves the site or leads nowhere; not imported")
    size = sum(p.stat().st_size for p in files)
    if size > BROWSE_MAX:
        print(f"browse: the workspace's site/ has {size / 2**20:.1f} MiB, more than {BROWSE_MAX / 2**20:.0f} MiB, so "
              "it is not the static edition; not imported")
        return None
    dst = OUT / "browse"
    for p in files:
        rel = p.relative_to(site)
        check_text(rel.as_posix(), f"the file name site/{rel}")
        out = dst / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        data = p.read_bytes()
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError:
            text = None
        if text is not None:
            if "vendor" in rel.parts:              # third-party code is copied as it is, and checked without its known strings
                vendored = text
                for s in THIRD_PARTY:
                    vendored = vendored.replace(s, "")
                check_text(vendored, p)
            else:
                text = scrub_text(text)
                check_text(text, p)
            out.write_bytes(text.encode("utf-8"))
        elif p.suffix.lower() == ".pdf":
            out.write_bytes(data)
            check_pdf(out, p)
        else:
            if p.suffix.lower() == ".gz":     # compressed text is checked, not rewritten
                inner = gzip.decompress(data).decode("utf-8", "replace")
                if scrub_text(inner) != inner:
                    sys.exit(f"import_writeup: {p} names what the scrub rewrites; compressed files are not rewritten")
                check_text(inner, p)
            check_text(printable(data), p)
            out.write_bytes(data)
    broken, pages = [], sorted(dst.rglob("*.html"))
    for page in pages:
        text = re.sub(r"<script\b.*?</script>", "", page.read_text(encoding="utf-8"), flags=re.S)
        for target in sorted(set(re.findall(r'(?:href|src)="([^"#][^"]*)"', text))):
            if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:|//", target):
                continue
            path = Path(urllib.parse.unquote(target.split("#")[0].split("?")[0]))
            path = (page.parent / path).resolve() if not path.is_absolute() else path
            if path.is_dir():
                path = path / "index.html"
            if not path.exists() or OUT.resolve() not in path.parents:
                broken.append(f"{page.relative_to(dst)}: {target}")
    if broken:
        print(f"WARNING: browse: {len(broken)} links do not resolve inside writeup/, e.g. " + "; ".join(broken[:5]))
    copied = sorted(p for p in dst.rglob("*") if p.is_file())
    tree = hashlib.sha256("".join(f"{p.relative_to(dst).as_posix()} {hashlib.sha256(p.read_bytes()).hexdigest()}\n"
                                  for p in copied).encode("utf-8")).hexdigest()
    return {"index": "browse/index.html", "files": len(copied), "pages": len(pages),
            "bytes": sum(p.stat().st_size for p in copied), "unresolved_links": len(broken), "tree_sha256": tree}


# ------------------------------------------------------------------------------------------------- the editions
def git(clone: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(clone), *args], capture_output=True, text=True, check=True).stdout


def blob_digest(clone: Path, commit: str, path: str) -> tuple[str, int]:
    proc = subprocess.Popen(["git", "-C", str(clone), "cat-file", "blob", f"{commit}:{path}"],
                            stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    h, n = hashlib.sha256(), 0
    for chunk in iter(lambda: proc.stdout.read(1 << 20), b""):
        h.update(chunk)
        n += len(chunk)
    if proc.wait() != 0:
        sys.exit(f"import_writeup: {path} is missing at commit {commit[:7]} of the public clone")
    return h.hexdigest(), n


def utc_minute(stamp: str) -> str:
    return datetime.datetime.fromisoformat(stamp).astimezone(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%MZ")


def published_editions(clone: Path) -> list[dict]:
    """Every edition in the history of a clone of the public repository, oldest first."""
    if git(clone, "rev-parse", "--is-shallow-repository").strip() != "false":
        sys.exit(f"import_writeup: {clone} is a shallow clone; the editions need the whole history")
    origin = git(clone, "remote", "get-url", "origin").strip()
    if not re.search(rf"github\.com[:/]{re.escape(REPO)}(?:\.git)?/?$", origin):
        sys.exit(f"import_writeup: {clone} is not a clone of the public repository {REPO}")
    added = git(clone, "log", "--diff-filter=A", "--format=%H", "--", "writeup/handout.pdf").split()
    first = added[-1] if added else None
    editions = []
    for line in git(clone, "log", "--first-parent", "--reverse", "--format=%H%x1f%cI%x1f%s").splitlines():
        commit, when, subject = line.split("\x1f", 2)
        m = EDITION.fullmatch(subject)
        if m:
            number, what = int(m.group(1)), m.group(2)
        elif commit == first:
            number, what = 1, re.sub(r"^feat\(writeup\):\s*", "", subject)
        else:
            continue
        sha, size = blob_digest(clone, commit, "writeup/handout.pdf")
        tree = set(git(clone, "ls-tree", "--name-only", commit, "--", "writeup/").split())
        editions.append({"edition": number, "date": utc_minute(when), "description": what, "commit": commit,
                         "handout_sha256": sha, "handout_bytes": size,
                         **{k: True for k in ("chapters", "reading", "browse") if f"writeup/{k}" in tree}})
    numbers = [e["edition"] for e in editions]
    if numbers != list(range(1, len(numbers) + 1)):
        sys.exit(f"import_writeup: the editions in the public history are not numbered 1, 2, ... in order: {numbers}")
    return editions


def parse_edition(text: str) -> tuple[int, str | None]:
    m = re.fullmatch(r"(?:edition\s+)?(\d+)(?:\s*:\s*(.+))?", text.strip(), flags=re.S | re.I)
    if not m:
        sys.exit('import_writeup: --edition takes "N: what changed", as in the commit message "edition N: ..."')
    return int(m.group(1)), (m.group(2) or "").strip() or None


def editions_record(clone: Path | None, previous: dict | None, edition: str | None, when: str) -> dict:
    if clone is not None:
        published = published_editions(clone)
    else:
        published = (previous or {}).get("editions", [])
        print("editions: no clone of the public repository (--public-clone, PUBLIC_CLONE); "
              + ("the archive of the previous import is kept" if previous else "the archive is empty"))
    sha = hashlib.sha256((OUT / "handout.pdf").read_bytes()).hexdigest()
    size = (OUT / "handout.pdf").stat().st_size
    last = published[-1] if published else None
    new = {"date": when, "description": None, "commit": None, "handout_sha256": sha, "handout_bytes": size}
    if edition is not None:
        number, what = parse_edition(edition)
        if last and number == last["edition"]:
            if last["handout_sha256"] != sha:
                sys.exit(f"import_writeup: edition {number} is published with another handout; the next is {number + 1}")
            current = dict(last)
        elif number == (last["edition"] + 1 if last else 1):
            current = {"edition": number, **new, "description": what}
        else:
            sys.exit(f"import_writeup: --edition {number}, but the public history ends at edition "
                     f"{last['edition'] if last else 0} (is the public clone up to date?)")
    elif last and last["handout_sha256"] == sha:
        current = dict(last)
    else:
        current = {"edition": last["edition"] + 1 if last else 1, **new}
    return {"schema": "riemann-rev/writeup-editions/1",
            "about": "Every published edition of the write-up: a commit of the public repository whose message begins "
                     "with 'feat(writeup): edition N:' (edition 1: the commit that added the handout), derived from the "
                     "git history by scripts/import_writeup.py. The handout of an edition stays at its commit. "
                     "'current' is the edition in this folder; its commit is null until it is published.",
            "repository": REPO,
            "handout_at_commit": f"https://raw.githubusercontent.com/{REPO}/{{commit}}/writeup/handout.pdf",
            "current": current, "editions": published}


# ----------------------------------------------------------------------------------------------- the structured proofs
def check_public_dossiers(ws: Path, config: dict, units: list[dict]) -> None:
    """Run Readback on the exported bytes with the same Lean source and unit membership."""
    with tempfile.TemporaryDirectory() as tmp:
        workspace = Path(tmp)
        reading = workspace / "reading"
        reading.mkdir()
        source = (ws / Path(config["artifact"]["path"]).expanduser()).resolve()
        settings = {**config, "artifact": {**config["artifact"], "path": str(source)}}
        (workspace / "readback.json").write_text(json.dumps(settings), encoding="utf-8")
        for rel in ("census.json", "units.proposal.json", "ledger/units.json", "statement-ranges.json"):
            original = ws / "reading" / rel
            if original.is_file():
                (reading / rel).parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(original, reading / rel)
        exported = OUT / "structured-proofs"
        (reading / "units").symlink_to(exported.resolve(), target_is_directory=True)
        for unit in units:
            uid = unit["unit"]
            subprocess.run([sys.executable, "-B", str((ws / "tools/rb.py").resolve()), "check", uid],
                           cwd=workspace, check=True)
            check = json.loads((exported / uid / "check.json").read_text(encoding="utf-8"))
            unit["check_problems"] = len(check["problems"])


def local_inputs(folder: Path, manuscript: Path) -> list[str]:
    """The files that a note's manuscript loads with \\input or \\include from its own folder (comments stripped),
    other than data.tex, which is copied anyway. A name that leaves the folder is refused."""
    if not manuscript.is_file():
        return []
    text = "\n".join(re.sub(r"(?<!\\)%.*", "", line) for line in manuscript.read_text(encoding="utf-8").splitlines())
    found = []
    for name in re.findall(r"\\(?:input|include)\s*\{([^}]+)\}", text):
        name = name.strip()
        rel = name if name.endswith(".tex") else name + ".tex"
        target = (folder / rel).resolve()
        if folder.resolve() not in target.parents:
            sys.exit(f"import_writeup: {manuscript} loads {name!r}, outside its folder; not imported")
        if rel != "data.tex" and target.is_file() and rel not in found:
            found.append(rel)
    return found


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--public-clone", type=Path, help="a full clone of the public repository (for the editions)")
    ap.add_argument("--edition", help='the edition being imported, "N: what changed" (as in its commit message)')
    ap.add_argument("--no-reading", action="store_true", help="leave out the reading edition")
    ap.add_argument("--no-browse", action="store_true", help="leave out the browsable annotated version")
    args = ap.parse_args()
    cfg = json.loads((ROOT / "private" / "config.json").read_text(encoding="utf-8"))
    WS = Path(cfg["writeup_workspace"])
    clone = args.public_clone or (Path(os.environ["PUBLIC_CLONE"]) if os.environ.get("PUBLIC_CLONE") else None) or (
        Path(cfg["public_clone"]).expanduser() if cfg.get("public_clone") else None)
    rb = json.loads((WS / "readback.json").read_text(encoding="utf-8"))
    pin = rb["artifact"]["commit"]
    previous = None
    if (OUT / "editions.json").is_file():
        previous = json.loads((OUT / "editions.json").read_text(encoding="utf-8"))
    # Everything is built in a folder outside the repository and replaces writeup/ only when the whole import has
    # passed: a refusal (a private path, a lost link) leaves writeup/ as it was.
    return staged(lambda: run(args, WS, rb, pin, clone, previous))


def staged(job) -> int:
    global OUT
    final, OUT = OUT, Path(tempfile.mkdtemp(prefix="writeup-import-"))
    try:
        for name in sorted(KEEP):                    # the hand-written files are kept
            if (final / name).is_file():
                shutil.copy2(final / name, OUT / name)
        job()
        final.mkdir(exist_ok=True)
        for p in final.iterdir():
            shutil.rmtree(p) if p.is_dir() else p.unlink()
        for p in OUT.iterdir():
            shutil.move(str(p), str(final / p.name))
    finally:
        shutil.rmtree(OUT, ignore_errors=True)
        OUT = final
    return 0


def run(args, WS: Path, rb: dict, pin: str, clone: Path | None, previous: dict | None) -> None:
    when = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%MZ")

    # the handout, and the handout cut into its chapters
    for f in ("handout.pdf", "catalogue-full.pdf"):
        copy_pdf(WS / "book" / "handout" / f, OUT / f)
    copy_text(WS / "book" / "handout" / "overview.tex", OUT / "overview.tex")
    cut = split_pdf(OUT / "handout.pdf", OUT / "chapters", f"{SITE}/writeup/chapters/")
    if cut is None:
        sys.exit("import_writeup: the outline of the handout has no chapters (entries 'I. ...'); not imported")
    chapters = [{**p, "file": f"chapters/{p['file']}"} for p in cut[0]]

    # the notes: sources of every note built with layout problems at most
    notes = []
    for spec in sorted((WS / "notes").glob("*/spec.json")):
        N = spec.parent
        pr = json.loads((N / "problems.json").read_text(encoding="utf-8")) if (N / "problems.json").exists() else None
        if not (isinstance(pr, dict) and all("overfull line" in str(x) for x in pr.get("problems") or [])
                and (N / f"{N.name}.pdf").exists()):
            continue
        s = json.loads(spec.read_text(encoding="utf-8"))
        for f in (f"{N.name}.tex", "data.tex", "spec.json", "concordance.json", "reader.json"):
            if (N / f).exists():
                copy_text(N / f, OUT / "notes" / N.name / f)
        for f in local_inputs(N, N / f"{N.name}.tex"):   # the note's own macro files, so that the source builds alone
            copy_text(N / f, OUT / "notes" / N.name / f)
        notes.append({"slug": N.name, "unit": str(s.get("unit")), "title": s.get("title")})

    # the structured proofs of every unit (merged units only)
    units = []
    for U in sorted((WS / "reading" / "units").iterdir()):
        if not U.is_dir() or not re.fullmatch(r"\d+", U.name) or not (U / "unit.json").exists():
            continue
        dst = OUT / "structured-proofs" / U.name
        for f in ("unit.json", "README.md", "CORRECTIONS.md"):
            if (U / f).exists():
                copy_text(U / f, dst / f)
        for p in sorted((U / "proofs").glob("*.json")):
            copy_text(p, dst / "proofs" / p.name)
        D = json.loads((U / "unit.json").read_text(encoding="utf-8"))
        units.append({"unit": U.name, "title": D.get("title"), "members": len(D.get("members") or []),
                      "structured_proofs": len(list((U / "proofs").glob("*.json")))})
    check_public_dossiers(WS, rb, units)

    # the catalogue and the second reader's verdicts
    cat = []
    for p in sorted((WS / "book" / "plan" / "catalogue").glob("part-*.json")):
        cat += json.loads(p.read_text(encoding="utf-8"))
    (OUT / "catalogue").mkdir(exist_ok=True)
    (OUT / "catalogue" / "catalogue.json").write_text(
        scrub_text(json.dumps({"pin": pin, "about": "every declaration of the background library (Lib) that the argument "
                               "(New) uses by name, classified as definition / elementary / named / substantial",
                               "entries": cat}, ensure_ascii=False, indent=1)) + "\n", encoding="utf-8")
    verdicts = {}
    for sj in sorted(list((WS / "exchange").glob("to-claude/*/*.json")) + list((WS / "exchange").glob("archive/**/*.json"))):
        try:
            data = json.loads(sj.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue
        recs = data.get("by_name") if isinstance(data, dict) else None
        if not isinstance(recs, dict):
            continue
        for name, v in recs.items():
            if isinstance(v, dict) and v.get("verdict"):
                verdicts[name] = {k: v.get(k) for k in ("verdict", "comparison", "sources", "file", "source_range", "lean_url")
                                  if v.get(k) is not None}
    (OUT / "catalogue" / "second-reading-verdicts.json").write_text(
        scrub_text(json.dumps({"pin": pin, "about": "the second reader's comparison of named theorems of the background "
                               "with their published statements (verdict, comparison, sources with places)",
                               "by_name": dict(sorted(verdicts.items()))}, ensure_ascii=False, indent=1)) + "\n",
        encoding="utf-8")
    for p in (OUT / "catalogue").glob("*.json"):
        check_text(p.read_text(encoding="utf-8"), p)

    # the reading edition and the browsable annotated version, when the workspace has built them
    reading = None if args.no_reading else import_reading(WS)
    browse = None if args.no_browse else import_browse(WS)

    # the editions
    record = editions_record(clone, previous, args.edition, when)
    text = scrub_text(json.dumps(record, ensure_ascii=False, indent=1)) + "\n"
    check_text(text, OUT / "editions.json")
    (OUT / "editions.json").write_text(text, encoding="utf-8")

    # the manifest
    files = sorted(p for p in OUT.rglob("*") if p.is_file() and p.name != "MANIFEST.json")
    man = {"schema": "riemann-rev/writeup-manifest/1", "edition": when,
           "edition_number": record["current"]["edition"],
           "artifact": {"repository": ARTIFACT, "edition": "grh-compact", "commit": pin},
           "notes": notes, "units": units, "catalogue_entries": sum(len(e.get("declarations") or []) for e in cat),
           "second_reading_verdicts": len(verdicts),
           "documents": {f: pdf_facts(OUT / f) for f in ("handout.pdf", "catalogue-full.pdf")},
           "chapters": chapters, "chapter_links": cut[1], "reading": reading, "browse": browse,
           "files": {str(p.relative_to(OUT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in files}}
    (OUT / "MANIFEST.json").write_text(json.dumps(man, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    size = sum(p.stat().st_size for p in OUT.rglob("*") if p.is_file())
    cur = record["current"]
    print(f"writeup: {len(notes)} notes, {len(units)} units, {man['catalogue_entries']} catalogue entries, "
          f"{len(verdicts)} verdicts, {len(files) + 1} files, {size / 1e6:.1f} MB")
    print(f"chapters: {len(chapters)} PDFs, {sum(p['bytes'] for p in chapters) / 1e6:.1f} MB; links kept: "
          f"{cut[1]['external']} external, {cut[1]['internal'] - cut[1]['to_other_parts']} internal, "
          f"{cut[1]['to_other_parts']} now lead to another part on the site")
    print("reading edition: " + (f"{reading['pages']} pages, {len(reading['chapters'])} chapter PDFs" if reading else "none"))
    print("browse: " + (f"{browse['files']} files, {browse['bytes'] / 1e6:.1f} MB" if browse else "none"))
    print(f"editions: {len(record['editions'])} published; current: edition {cur['edition']}"
          + (f" (commit {cur['commit'][:7]})" if cur.get("commit") else " (not yet published)"))


if __name__ == "__main__":
    raise SystemExit(main())
