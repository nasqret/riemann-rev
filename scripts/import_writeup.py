#!/usr/bin/env python3
"""Import the write-up of the condensed proof (lsernau/grh-lean, edition grh-compact) into writeup/ for publication.

    python3 -B scripts/import_writeup.py      # the workspace's place is read from private/config.json, writeup_workspace

The write-up is made in a Readback workspace (structured proofs checked by program against the pinned Lean source,
notes written from them, an independent second reading, referee reports). This script copies what a reader or an
agent needs, and nothing else:

* handout.pdf (overview, the notes in the order of the argument, the condensed catalogue, the record of checks),
  catalogue-full.pdf, and overview.tex;
* the sources of every note whose last build reported no problem other than overfull lines:
  notes/<slug>/{<slug>.tex, data.tex, spec.json, concordance.json, reader.json};
* the structured proofs of every unit: structured-proofs/<id>/{unit.json, check.json, README.md, CORRECTIONS.md,
  proofs/*.json} (the merged units, not their chunks; not the generators);
* catalogue/catalogue.json (every background declaration the argument uses, classified) and
  catalogue/second-reading-verdicts.json (the second reader's comparison of each named theorem with its published
  statement: the verdict, the comparison, the sources, the place in the Lean source);
* MANIFEST.json: the pin, the edition, counts, and the SHA-256 of every file.

Texts are rewritten by the private patterns of private/writeup-scrub.json (how the second reader and its messages
are named), and a file that still matches its forbidden patterns stops the import. Hand-written files of writeup/ (README.md, AGENTS.md) are kept.
"""
import datetime
import gzip
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "writeup"
KEEP = {"README.md", "AGENTS.md"}
# The patterns of what is rewritten or refused are private (they name what must not appear in public files):
# private/writeup-scrub.json, {"scrub": [[regex, replacement], ...], "forbidden": regex}.
_PRIV = json.loads((ROOT / "private" / "writeup-scrub.json").read_text(encoding="utf-8"))
SCRUB = [(re.compile(a), b) for a, b in _PRIV["scrub"]]
FORBIDDEN = re.compile(_PRIV["forbidden"])


def scrub_text(s: str) -> str:
    for pat, rep in SCRUB:
        s = pat.sub(rep, s)
    return s


def copy_text(src: Path, dst: Path) -> None:
    s = scrub_text(src.read_text(encoding="utf-8"))
    m = FORBIDDEN.search(s)
    if m:
        sys.exit(f"import_writeup: {src} contains a private path ({m.group(0)!r}); not imported")
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(s, encoding="utf-8")


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


def main() -> int:
    cfg = json.loads((ROOT / "private" / "config.json").read_text(encoding="utf-8"))
    WS = Path(cfg["writeup_workspace"])
    rb = json.loads((WS / "readback.json").read_text(encoding="utf-8"))
    pin = rb["artifact"]["commit"]
    if OUT.exists():
        for p in OUT.iterdir():
            if p.name in KEEP:
                continue
            shutil.rmtree(p) if p.is_dir() else p.unlink()
    OUT.mkdir(exist_ok=True)

    # the handout
    for f in ("handout.pdf", "catalogue-full.pdf"):
        shutil.copy2(WS / "book" / "handout" / f, OUT / f)
    copy_text(WS / "book" / "handout" / "overview.tex", OUT / "overview.tex")

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

    # the manifest
    files = sorted(p for p in OUT.rglob("*") if p.is_file() and p.name != "MANIFEST.json")
    man = {"schema": "riemann-rev/writeup-manifest/1",
           "edition": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%MZ"),
           "artifact": {"repository": "https://github.com/lsernau/grh-lean", "edition": "grh-compact", "commit": pin},
           "notes": notes, "units": units, "catalogue_entries": sum(len(e.get("declarations") or []) for e in cat),
           "second_reading_verdicts": len(verdicts),
           "files": {str(p.relative_to(OUT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in files}}
    (OUT / "MANIFEST.json").write_text(json.dumps(man, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    size = sum(p.stat().st_size for p in OUT.rglob("*") if p.is_file())
    print(f"writeup: {len(notes)} notes, {len(units)} units, {man['catalogue_entries']} catalogue entries, "
          f"{len(verdicts)} verdicts, {len(files) + 1} files, {size / 1e6:.1f} MB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
