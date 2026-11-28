#!/usr/bin/env python3
"""Assemble the web site (GitHub Pages) in _site/.

    python3 -B scripts/build_site.py                  # the book is included if it has been built
    python3 -B scripts/build_site.py --require-book   # fail if book/_build/html is missing (used in CI)

    _site/index.html                    the home page, generated here from data/model.json
    _site/writeup/index.html            the write-up: the current edition (the handout, its chapters, the reading
                                        edition, the annotated version in the browser, the catalogue), then every
                                        edition, from writeup/MANIFEST.json and writeup/editions.json
    _site/writeup/                      the files of the current edition (scripts/import_writeup.py)
    _site/atlas/index.html              the atlas (a copy; links that leave the site go to the repository)
    _site/guide/proof-guide.{pdf,gif}   the guide
    _site/digests/<slug>.pdf            the deformalization notes (tower-bound, local-nilpotence, layer-descent)
    _site/digests/<slug>.json           their reader indexes (declaration, place in the note, page, PDF destination)
    _site/digests/editions/             every published edition of a note, named by its SHA-256
    _site/blueprint/atlas-blueprint.pdf the illustrated blueprint
    _site/book/                         the Jupyter Book (book/_build/html)

Nothing is typed by hand: counts, the status line and its time come from the model. The script
fails if a relative link of the home page or of the atlas does not resolve inside the site, or if a
computation of the book printed a warning into its page.
"""
from __future__ import annotations

import argparse
import datetime
import html
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_guide import GUIDE_PAGES  # noqa: E402
from build_readme import REPO, SITE, load, utc  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "_site"
BLOB = f"https://github.com/{REPO}/blob/main/"
esc = html.escape

CSS = """
:root { --night:#0b1020; --bg:#fafbfc; --surface:#fff; --text:#1e293b; --muted:#64748b; --heading:#0f172a;
  --border:#e2e8f0; --accent:#4f46e5; --arith:#c2410c; --est:#7c3aed; --ana:#0891b2; --dest:#e11d48; --ok:#047857;
  --sans:'Inter','Helvetica Neue',Helvetica,Arial,system-ui,-apple-system,'Segoe UI',sans-serif; }
*,*::before,*::after { box-sizing:border-box; }
body { margin:0; font-family:var(--sans); color:var(--text); background:var(--bg); line-height:1.6;
  -webkit-font-smoothing:antialiased; }
a { color:var(--accent); text-decoration:none; } a:hover { text-decoration:underline; }
.wrap { max-width:1120px; margin:0 auto; padding:0 28px; }
.hero { position:relative; overflow:hidden; background:var(--night); color:#e2e8f0; }
.hero-bg { position:absolute; inset:0; opacity:.3; }
.hero-bg svg { width:100%; height:100%; display:block; }
.hero-grid { position:relative; z-index:2; display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1.08fr); gap:48px;
  align-items:center; padding-top:64px; padding-bottom:64px; }
.hero h1 { font-size:clamp(1.9rem,3.3vw,2.7rem); }
.shot { margin:0; }
.shot > a { display:block; border-radius:12px; overflow:hidden; border:1px solid rgba(255,255,255,.22); background:#fff;
  box-shadow:0 18px 50px rgba(0,0,0,.45); }
.shot img { display:block; width:100%; height:auto; }
.shot figcaption { margin-top:10px; font-size:.82rem; color:#94a3b8; line-height:1.45; }
.shot figcaption a { color:#c7d2fe; }
.label { font-size:.72rem; font-weight:700; letter-spacing:.14em; text-transform:uppercase; color:#a5b4fc;
  margin-bottom:18px; }
h1 { color:#fff; font-size:clamp(2rem,4.2vw,3.1rem); font-weight:800; letter-spacing:-.02em; line-height:1.15;
  margin:0 0 18px; }
h1 em { font-style:normal; background:linear-gradient(90deg,#fde68a,#fbbf24 55%,#f59e0b);
  -webkit-background-clip:text; background-clip:text; color:transparent; }
.lead { font-size:1.12rem; color:#cbd5e1; margin:0 0 22px; }
.status { display:inline-block; padding:10px 14px; border-radius:12px; background:rgba(255,255,255,.06);
  border:1px solid rgba(255,255,255,.14); font-size:.9rem; color:#e2e8f0; margin:0 0 26px; }
.status b { color:#6ee7b7; font-weight:600; } .status span { color:#94a3b8; }
.cta { display:flex; flex-wrap:wrap; gap:10px; }
.btn { display:inline-block; padding:10px 16px; border-radius:10px; font-weight:600; font-size:.92rem;
  background:var(--accent); color:#fff; border:1px solid transparent; }
.btn.ghost { background:rgba(255,255,255,.06); border-color:rgba(255,255,255,.18); color:#e2e8f0; }
.btn:hover { text-decoration:none; filter:brightness(1.1); }
.note { margin:34px 0 8px; padding:16px 20px; border-left:4px solid var(--est); background:#f5f3ff;
  border-radius:0 12px 12px 0; color:#2e1065; font-size:.96rem; }
h2 { color:var(--heading); font-size:1.35rem; margin:44px 0 8px; letter-spacing:-.01em; }
.stampline { margin:0 0 16px; color:var(--muted); font-size:.84rem; }
.stampline code, .stamp code { color:inherit; }
.grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(320px,1fr)); gap:18px; }
.card { display:flex; flex-direction:column; background:var(--surface); border:1px solid var(--border);
  border-top:4px solid var(--c); border-radius:14px; padding:20px 22px 16px; color:var(--text);
  box-shadow:0 1px 3px rgba(15,23,42,.06); }
.card h3 { margin:0 0 6px; color:var(--heading); font-size:1.08rem; }
.card h3 a { color:inherit; }
.card p { margin:0 0 12px; font-size:.93rem; color:#475569; }
.card .go { margin-top:auto; font-weight:600; font-size:.88rem; display:flex; flex-wrap:wrap; gap:4px 16px; }
.card .go a { color:var(--c); }
.card .stamp { margin:12px 0 0; padding-top:9px; border-top:1px solid var(--border); font-size:.78rem; color:var(--muted); }
.list { margin:0; padding:0; list-style:none; }
.list li { padding:11px 0; border-bottom:1px solid var(--border); }
.list li:last-child { border-bottom:none; }
.list b { color:var(--heading); }
.list .stamp { display:block; color:var(--muted); font-size:.8rem; }
.earlier { margin-top:56px; padding:6px 24px 8px; border-radius:14px; background:#f1f5f9; color:#64748b; }
.earlier h2 { color:#475569; font-size:1.1rem; }
.earlier a { color:#475569; text-decoration:underline; text-decoration-color:#cbd5e1; }
.earlier p { font-size:.9rem; }
.earlier .list li { padding:8px 0; }
.earlier .list b a { font-weight:600; }
footer { margin-top:44px; padding:26px 0 54px; border-top:1px solid var(--border); color:var(--muted);
  font-size:.86rem; }
footer p { margin:0 0 6px; }
footer code { color:inherit; }
@media (max-width:900px) { .hero-grid { grid-template-columns:minmax(0,1fr); gap:30px; padding-top:44px; padding-bottom:44px; } }
@media (max-width:760px) { .wrap { padding:0 20px; } .grid { grid-template-columns:minmax(0,1fr); } }
"""

# the write-up page: a band instead of the hero, and tables for the chapters and the editions
WRITEUP_CSS = """
.band { background:var(--night); color:#e2e8f0; }
.band .wrap { padding:34px 28px 38px; }
.crumb { display:inline-block; color:#a5b4fc; font-size:.86rem; margin-bottom:22px; }
.band h1 { font-size:clamp(1.8rem,3.6vw,2.6rem); margin:0 0 14px; }
.band .lead { max-width:860px; }
.band .status { margin-bottom:22px; }
h2 .sub { font-weight:500; color:var(--muted); font-size:1rem; }
.what { max-width:900px; margin:-6px 0 18px; color:#334155; }
.scroll { overflow-x:auto; border:1px solid var(--border); border-radius:12px; background:var(--surface);
  box-shadow:0 1px 3px rgba(15,23,42,.05); }
table { width:100%; border-collapse:collapse; font-size:.92rem; }
th, td { text-align:left; vertical-align:top; padding:11px 14px; border-bottom:1px solid var(--border); }
th { background:#f1f5f9; color:var(--heading); font-weight:600; font-size:.8rem; letter-spacing:.03em; }
tbody tr:last-child td { border-bottom:none; }
tbody tr:hover td { background:#fafaff; }
td.part { white-space:nowrap; font-weight:600; color:var(--heading); }
td.num { white-space:nowrap; text-align:right; font-variant-numeric:tabular-nums; }
td.links { white-space:nowrap; }
td.date { white-space:nowrap; color:#475569; }
.notes { display:block; margin-top:4px; color:var(--muted); font-size:.84rem; line-height:1.5; }
code { font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace; font-size:.84em; color:#334155; }
a code { color:inherit; }
.tag { display:inline-block; margin-left:6px; padding:1px 8px; border-radius:999px; background:#dcfce7; color:#166534;
  font-size:.7rem; font-weight:700; letter-spacing:.06em; text-transform:uppercase; vertical-align:2px; }
.dim { color:var(--muted); }
.chap td.part { width:1%; }
@media (max-width:760px) {
  .chap thead { display:none; }
  .chap, .chap tbody, .chap tr, .chap td { display:block; width:auto; }
  .chap tr { padding:12px 14px; border-bottom:1px solid var(--border); }
  .chap td { border:none; padding:2px 0; text-align:left; }
  .chap td.num { text-align:left; }
  .chap td.part::before { content:'Chapter '; }
  .chap td.num::after { content:' pages'; color:var(--muted); }
  .chap tbody tr:hover td { background:none; }
}
.fine { margin:14px 0 0; color:var(--muted); font-size:.88rem; max-width:900px; }
"""


def mb(n: int) -> str:
    return f"{n / 1e6:.1f} MB" if n >= 1e5 else f"{n / 1e3:.0f} kB"


def when(stamp: str) -> str:
    """'2026-11-28T05:21Z' -> '28 Nov 2026, 05:21'."""
    d = datetime.datetime.strptime(stamp, "%Y-%m-%dT%H:%MZ")
    return f"{d.day}&nbsp;{d:%b}&nbsp;{d:%Y}, {d:%H:%M}"


def day(stamp: str) -> str:
    d = datetime.datetime.strptime(stamp, "%Y-%m-%dT%H:%MZ")
    return f"{d.day}&nbsp;{d:%B}&nbsp;{d:%Y}"


REPO_URL = f"https://github.com/{REPO}"
# Hashes of the private working copy do not exist publicly: a commit is linked only when the site is built in the
# public repository (on GitHub's runner); a local build shows the date and "local build".
PUBLIC = os.environ.get("GITHUB_REPOSITORY") == REPO


def last_commit(*paths: str) -> tuple[str | None, str | None]:
    """(sha, date) of the last commit that touched the paths: git log -1 --format=%H%x09%cs -- <paths>."""
    try:
        out = subprocess.run(["git", "log", "-1", "--format=%H%x09%cs", "--", *paths], cwd=ROOT, capture_output=True,
                             text=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return None, None
    if "\t" not in out:
        return None, None
    sha, date = out.split("\t")
    return sha, date


def short_date(iso: str) -> str:
    """'2026-11-28' or '2026-11-28T11:30Z' -> '28 Nov 2026'."""
    d = datetime.date.fromisoformat(iso[:10])
    return f"{d.day}&nbsp;{d:%b}&nbsp;{d:%Y}"


def commit_ref(sha: str | None) -> str:
    """A linked short hash in the public build; 'local build' otherwise."""
    if PUBLIC and sha:
        return f'commit <a href="{REPO_URL}/commit/{sha}"><code>{sha[:7]}</code></a>'
    return "" if PUBLIC else "local build"


def stamp(*paths: str, edition: int | None = None, date: str | None = None, prefix: str = "") -> str:
    """The stamp of a section: [edition N ·] date · commit (the last commit touching the paths). For a section of the
    write-up the edition and its date are those of writeup/editions.json; otherwise the date is the commit's."""
    sha, cdate = last_commit(*paths)
    parts = [prefix] if prefix else []
    if edition is not None:
        parts.append(f"edition {edition}")
    if date or cdate:
        parts.append(short_date(date or cdate))
    ref = commit_ref(sha)
    if ref:
        parts.append(ref)
    return " · ".join(parts)


def card(colour: str, title: str, text: str, links: list[tuple[str, str]], stamp_html: str) -> str:
    """A card: the title links to the first link; the others stand in the bottom row; the stamp closes the card."""
    first = esc(links[0][0])
    go = "".join(f'<a href="{esc(h)}">{esc(t)} →</a>' for h, t in links)
    return (f'<div class="card" style="--c:var(--{colour})"><h3><a href="{first}">{esc(title)}</a></h3><p>{esc(text)}</p>'
            f'<div class="go">{go}</div><p class="stamp">{stamp_html}</p></div>')


def writeup_page() -> str:
    """The write-up: the current edition first (the handout, its chapters, the reading edition, the annotated version
    in the browser, the catalogue), then every published edition with links pinned to its commit."""
    man = load("writeup/MANIFEST.json")                      # scripts/import_writeup.py
    eds = load("writeup/editions.json")
    cur, docs, parts = eds["current"], man["documents"], man.get("chapters") or []
    reading, browse = man.get("reading"), man.get("browse")
    repo = f"https://github.com/{REPO}"
    pinned = lambda commit, path: f"https://raw.githubusercontent.com/{REPO}/{commit}/writeup/{path}"   # noqa: E731
    viewed = lambda commit, path: f"{repo}/blob/{commit}/writeup/{path}"                                  # noqa: E731
    # The commit of the current edition is known once it is in the public history; until then the site that is built
    # from it on GitHub's runner knows its own commit, which holds the same files.
    built = os.environ.get("GITHUB_SHA", "") if os.environ.get("GITHUB_REPOSITORY") == REPO else ""
    pin = cur.get("commit") or (built if re.fullmatch(r"[0-9a-f]{40}", built) else None)
    h, cat = docs["handout.pdf"], docs["catalogue-full.pdf"]

    ed, eday = cur["edition"], cur["date"]
    st = lambda *paths, **kw: stamp(*paths, edition=ed, date=eday, **kw)                                   # noqa: E731
    cards = [("accent", "The handout", "The whole reading in one PDF: the summary, the overview of the argument, "
                                       "Chapters I–VIII, the catalogue of quoted results and the record of checks. "
                                       "Every statement and every step links to the Lean lines it renders. "
                                       f"{h['pages']:,} pages, {mb(h['bytes'])}.",
              [("handout.pdf", "Read the handout (PDF)")], st("writeup/handout.pdf"))]
    if parts:
        cards.append(("arith", "Chapter by chapter", f"The same pages in {len(parts)} PDFs: the front matter, one PDF "
                                                     "per chapter, and the catalogue with the record of checks. A link "
                                                     "into another part opens that part at the right page.",
                      [("#chapters", "Choose a chapter")], st("writeup/chapters")))
    if reading:
        cards.append(("est", "The reading edition", "The same text without the links to the Lean source, for reading "
                                                    f"from beginning to end. {reading['pages']:,} pages, "
                                                    f"{mb(reading['bytes'])}.",
                      [(reading["file"], "Read the reading edition (PDF)")], st("writeup/reading")))
    if browse:
        cards.append(("ana", "The browsable proof", "Each note in the browser, beside the structured proofs and the "
                                                    "Lean lines of its statements, with a page for every chapter.",
                      [("browse/", "Open the browsable proof")], st("writeup/browse")))
    cards += [("dest", "The catalogue of quoted results", "Every background result that the argument uses, classified as "
                                                         "a definition, an elementary lemma, a named theorem or a "
                                                         "substantial result, with references; for a named theorem, how "
                                                         "the formal statement compares with the published one. "
                                                         f"{cat['pages']:,} pages.",
               [("catalogue-full.pdf", "Read the catalogue (PDF)")], st("writeup/catalogue-full.pdf")),
              ("ok", "For AI agents, and for checking", "The structured proofs (every proof a tree of small steps, each "
                                                        "quoting the Lean lines it renders), the LaTeX source of every "
                                                        "note, the catalogue as data, and a guide for AI agents.",
               [(f"{repo}/tree/main/writeup", "Open the folder")], st("writeup"))]
    card_html = "\n".join(card(*c) for c in cards)

    by_name = {Path(p["file"]).name: p for p in (reading or {}).get("chapters") or []}
    rows = []
    for p in parts:
        name = Path(p["file"]).name
        notes = " · ".join(esc(s["title"]) for s in p.get("sections") or [] if s["title"] != p["title"])
        title = esc(p["title"]) + (f'<span class="notes">{notes}</span>' if notes else "")
        light = by_name.get(name)
        cells = [f'<td class="part">{esc(p["part"])}</td>', f"<td>{title}</td>",
                 f'<td class="num">{p["first_page"]}–{p["last_page"]}</td>',
                 f'<td class="links"><a href="{esc(p["file"])}">PDF</a> <span class="dim">{mb(p["bytes"])}</span></td>']
        if by_name:
            cells.append(f'<td class="links"><a href="{esc(light["file"])}">PDF</a> <span class="dim">{mb(light["bytes"])}'
                         "</span></td>" if light else '<td class="dim">–</td>')
        rows.append("<tr>" + "".join(cells) + "</tr>")
    chapters_html = ""
    if parts:
        chapters_html = f"""
  <h2 id="chapters">Chapter by chapter</h2>
  <p class="stampline">{st("writeup/chapters")}</p>
  <p class="what">The pages of the handout cut at its chapters; the pages keep the handout's numbers, and every link is
  kept: a link into another part opens that part at the right page{', and the reading edition is cut the same way' if by_name else ''}.</p>
  <div class="scroll"><table>
   <thead><tr><th>part</th><th>contents</th><th>handout pages</th><th>handout, with Lean links</th>{'<th>reading edition</th>' if by_name else ''}</tr></thead>
   <tbody>
{chr(10).join(rows)}
   </tbody>
  </table></div>"""

    def edition_row(e: dict, commit: str | None, current: bool) -> str:
        sha = e["handout_sha256"]
        if commit:
            ref = f'<a href="{repo}/commit/{commit}"><code>{commit[:7]}</code></a>'
            get = (f'<a href="{viewed(commit, "handout.pdf")}">view</a> · <a href="{pinned(commit, "handout.pdf")}">PDF</a>'
                   + (f' · <a href="{repo}/tree/{commit}/writeup/chapters">chapters</a>' if e.get("chapters") else ""))
        else:
            ref, get = '<span class="dim">this site</span>', '<a href="handout.pdf">PDF</a>'
        tag = ' <span class="tag">current</span>' if current else ""
        return (f'<tr><td class="part">{e["edition"]}{tag}</td><td class="date">{when(e["date"])}</td>'
                f'<td>{esc(e.get("description") or "")}</td><td>{ref}</td>'
                f'<td><code title="{sha}">{sha[:16]}</code></td><td class="links">{get}</td></tr>')

    history = list(reversed(eds["editions"]))
    ed_rows = [] if cur.get("commit") else [edition_row(cur, pin, True)]
    ed_rows += [edition_row(e, e["commit"], e["edition"] == cur["edition"]) for e in history]
    first = eds["editions"][0]["date"] if eds["editions"] else cur["date"]
    status = (f'<b>Edition {cur["edition"]}</b>, {when(cur["date"])} UTC<br><span>Handout SHA-256 '
              f'<code style="color:inherit">{cur["handout_sha256"][:16]}</code>…'
              + (f' · commit <a href="{repo}/commit/{pin}" style="color:#a5b4fc"><code style="color:inherit">{pin[:7]}</code></a>'
                 if pin else "") + "</span>")
    buttons = ['<a class="btn" href="handout.pdf">The handout (PDF)</a>']
    buttons += ['<a class="btn ghost" href="#chapters">Chapter by chapter</a>'] if parts else []
    buttons += ['<a class="btn ghost" href="' + esc(reading["file"]) + '">The reading edition</a>'] if reading else []
    buttons += ['<a class="btn ghost" href="browse/">The browsable proof</a>'] if browse else []
    buttons += ['<a class="btn ghost" href="#editions">Every edition</a>']
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The write-up of the condensed proof of RH and GRH: every edition</title>
<meta name="description" content="A reading of the condensed Lean proof of the Riemann hypothesis and its generalization to Dirichlet L-functions, as mathematics: the handout, its chapters and every edition. A working draft, not yet refereed by a human.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>{CSS}{WRITEUP_CSS}</style>
</head>
<body>
<header class="band"><div class="wrap">
  <a class="crumb" href="../index.html">← The announced proof of the Riemann hypothesis</a>
  <div class="label">The write-up · a working draft</div>
  <h1>The condensed proof, read as mathematics</h1>
  <p class="lead">The Lean proof of the Riemann hypothesis and of its generalization to Dirichlet L-functions in
  <a href="https://github.com/lsernau/grh-lean" style="color:#c7d2fe">lsernau/grh-lean</a> (edition grh-compact), read
  unit by unit: {len(man['notes'])} notes on all {len(man['units'])} units of the argument, from the five final theorems
  down, in the order of the argument, with classical results quoted from the literature.</p>
  <p class="status">{status}</p>
  <div class="cta">{''.join(buttons)}</div>
</div></header>
<main class="wrap">
  <p class="note"><b>What this is.</b> A working draft, read by AI agents and checked by programs; it has not been
  refereed by a human. The formal proof it reads is a claim: its authors report that Lean's kernel accepts the five
  final theorems with the three standard axioms. Nothing here says that the Riemann hypothesis is proved.</p>
  <h2 id="current">The current edition <span class="sub">edition {cur['edition']} of {day(cur['date'])}</span></h2>
  <p class="stampline">{st("writeup")}</p>
  {f'<p class="what">What changed: {esc(cur["description"])}.</p>' if cur.get('description') else ''}
  <div class="grid">
{card_html}
  </div>
{chapters_html}
  <h2 id="editions">Every edition <span class="sub">{len(ed_rows)} editions since {day(first)}</span></h2>
  <p class="stampline">{st("writeup/editions.json")}</p>
  <p class="what">Each edition is a commit of the public repository, and its handout stays at that commit: the links
  below are pinned to it (<em>view</em> shows the PDF on GitHub, <em>PDF</em> downloads it). The SHA-256 identifies the
  file: compare it with <code>shasum -a 256 handout.pdf</code>. Times are UTC.</p>
  <div class="scroll"><table>
   <thead><tr><th>edition</th><th>published</th><th>what changed</th><th>commit</th><th>handout SHA-256</th><th>handout</th></tr></thead>
   <tbody>
{chr(10).join(ed_rows)}
   </tbody>
  </table></div>
  <p class="fine">The list is derived from the history of the repository by
  <a href="{BLOB}scripts/import_writeup.py">scripts/import_writeup.py</a>: an edition is a commit whose message begins
  with “feat(writeup): edition N:”, and edition 1 is the commit that added the handout. Nothing in it is typed by hand.</p>
</main>
<footer><div class="wrap">
  <p>Built from <a href="{repo}">{esc(REPO)}</a>. The Lean quotations are from
  <a href="https://github.com/lsernau/grh-lean">lsernau/grh-lean</a> (Apache License 2.0); the proof is Levent
  Alpöge's, with Claude, and the condensed edition is by Luke Sernau, colleagues at Anthropic, and Claude.
  Corrections are welcome as <a href="{repo}/issues">issues</a>: cite the note and the Lean lines.</p>
  <p>Everything original on this site may be used for any purpose (<a href="{repo}/blob/main/LICENSE">licence</a>).</p>
</div></footer>
</body>
</html>
"""


SCREEN = ROOT / "assets" / "screens" / "reading-mode.webp"      # taken by a script outside the build (Chrome, DevTools)
SCREEN_JSON = ROOT / "assets" / "screens" / "reading-mode.json"


def hero_curve() -> tuple[str, str]:
    """(inline SVG, caption) of the hero's background. The computed curve of the zeta function when the figures have
    it (assets/figures/hero-zeta.svg with the key "hero_zeta" in facts.json); the older figure and caption otherwise."""
    facts = load("assets/figures/facts.json")
    zeta = facts.get("hero_zeta")
    if zeta and (ROOT / "assets" / "figures" / "hero-zeta.svg").is_file():
        name = "hero-zeta.svg"
        cap = (f"The curve behind the title is computed: t ↦ ζ(½ + it) in the complex plane for 0 ≤ t ≤ "
               f"{zeta['t_max']:g}, from {zeta['samples']:,} samples; it passes through the origin at each of the "
               f"{zeta['n_zeros']} zeros on the critical line in that range.")
    else:
        name = "hero.svg"
        h = facts["hero"]
        cap = (f"The curve behind the title is computed: the centred prime sum, normalized, for arguments up to "
               f"{h['y_max']:,}.")
    svg = (ROOT / "assets" / "figures" / name).read_text(encoding="utf-8")
    svg = re.sub(r"^<\?xml[^>]*\?>\s*", "", svg)
    svg = svg.replace('width="', 'data-w="', 1).replace('height="', 'data-h="', 1).replace(
        "<svg ", '<svg preserveAspectRatio="xMidYMid slice" ', 1)
    return svg, cap


def roman_pages(manifest: dict) -> list[tuple[int, dict]]:
    """The chapters proper (those with a numeral), numbered 1, 2, ... as the pages chapter-N.html of the browsable proof."""
    return list(enumerate([c for c in manifest.get("chapters") or [] if c.get("numeral")], start=1))


def stamp_json(man: dict, eds: dict) -> dict:
    """What the browsable pages display: the edition, its date and the commit of the browsable proof."""
    cur = eds["current"]
    sha, _ = last_commit("writeup/browse")
    sha = sha if PUBLIC else None
    return {"edition": cur["edition"], "date": cur["date"][:10], "commit": sha,
            "commit_url": f"{REPO_URL}/commit/{sha}" if sha else None, "editions_url": "../index.html#editions"}


def home(has_book: bool) -> str:
    model = load("data/model.json")
    ms = model["status"]
    man = load("writeup/MANIFEST.json")                 # scripts/import_writeup.py: the edition of the write-up
    eds = load("writeup/editions.json")
    cur, docs = eds["current"], man["documents"]
    reading, browse = man.get("reading"), man.get("browse")
    ed, eday = cur["edition"], cur["date"]
    st = lambda *paths: stamp(*paths, edition=ed, date=eday)                                               # noqa: E731
    curve, curve_caption = hero_curve()
    n_eds = len(eds["editions"]) + (0 if cur.get("commit") else 1)
    first = eds["editions"][0]["date"] if eds["editions"] else eday
    parts = roman_pages(man)
    front = next(c for c in man["chapters"] if c["part"] == "Front matter")
    lfront = next((c for c in (reading or {}).get("chapters") or [] if c["part"] == "Front matter"), None)
    by_light = {Path(c["file"]).name: c for c in (reading or {}).get("chapters") or []}

    # ---------------------------------------------------------------- the screenshot of the browsable proof
    shot = ""
    if SCREEN.is_file() and SCREEN_JSON.is_file():
        sj = json.loads(SCREEN_JSON.read_text(encoding="utf-8"))
        shot = (f'<figure class="shot"><a href="writeup/browse/{esc(sj["page"])}"><img src="assets/screens/{esc(SCREEN.name)}" '
                f'width="{sj["width"]}" height="{sj["height"]}" alt="A note of the browsable proof in reading mode: its '
                f'PDF pages on the left, the structured proof and the Lean text of the chosen statement on the right"></a>'
                f'<figcaption>The browsable proof in reading mode: {esc(sj["page_title"])}. Edition {sj["edition"]}, '
                f'{short_date(sj["date"])}. <a href="writeup/browse/{esc(sj["page"])}">Open this page →</a></figcaption></figure>')

    # ---------------------------------------------------------------- read the proof
    cards = []
    if browse:
        cards.append(("ana", "The browsable proof", f"All {len(man['notes'])} notes in the browser, each beside its "
                      "structured proofs and the Lean lines of its statements, with a page for every chapter.",
                      [("writeup/browse/", "Browse the proof")], st("writeup/browse")))
    cards.append(("accent", "The handout", f"The whole reading in one PDF: {docs['handout.pdf']['pages']:,} pages, "
                  f"{mb(docs['handout.pdf']['bytes'])}. Every statement links to the Lean lines it renders.",
                  [("writeup/handout.pdf", "Read the handout (PDF)"), ("#chapters", "Chapter by chapter")],
                  st("writeup/handout.pdf")))
    if reading:
        cards.append(("est", "The reading edition", f"The same text, light: no links to the Lean source, "
                      f"{reading['pages']:,} pages, {mb(reading['bytes'])}. For reading from beginning to end.",
                      [("writeup/" + reading["file"], "Read the reading edition (PDF)")], st("writeup/reading")))
    cards.append(("ok", "The summary and the overview", f"The handout's front matter, {front['pages']} pages: the title "
                  "page, the summary, the contents and the overview of the argument. Read it before a chapter. "
                  "It replaces the condensed-proof note of 25 November.",
                  [("writeup/" + front["file"], "Summary and overview (PDF)")]
                  + ([("writeup/" + lfront["file"], "Light version (PDF)")] if lfront else []),
                  st("writeup/chapters/front-matter.pdf")))
    cards.append(("dest", "The catalogue of quoted results", f"{man['catalogue_entries']:,} background results that the "
                  f"argument uses, classified and referenced; {docs['catalogue-full.pdf']['pages']} pages.",
                  [("writeup/catalogue-full.pdf", "Read the catalogue (PDF)")], st("writeup/catalogue-full.pdf")))
    cards.append(("arith", "Every edition", f"{n_eds} editions since {short_date(first).replace('&nbsp;', ' ')}. Each handout stays at its "
                  "commit, with its SHA-256, so that a change can be traced.",
                  [("writeup/#editions", "See the editions")], st("writeup/editions.json")))
    card_html = "\n".join(card(*c) for c in cards)

    # ---------------------------------------------------------------- the eight chapters
    rows = []
    for n, c in parts:
        notes = [s for s in c.get("sections") or [] if s.get("note")]
        lst = "".join(f'<li><a href="writeup/browse/note-{esc(s["note"])}.html">{esc(s["title"])}</a></li>' for s in notes)
        det = (f'<details><summary>{len(notes)} note{"s" if len(notes) != 1 else ""}</summary><ul>{lst}</ul></details>'
               if notes else "")
        light = by_light.get(Path(c["file"]).name)
        rows.append(
            f'<tr><td class="part">{esc(c["numeral"])}</td>'
            f'<td><a href="writeup/browse/chapter-{n}.html"><b>{esc(c["title"])}</b></a>{det}</td>'
            f'<td class="num">{c["pages"]}' + (f' <span class="dim">/ {light["pages"]}</span>' if light else "") + "</td>"
            f'<td class="links"><a href="writeup/browse/chapter-{n}.html">Browse</a> · '
            f'<a href="writeup/{esc(c["file"])}">PDF</a>'
            + (f' · <a href="writeup/{esc(light["file"])}">Light PDF</a>' if light else "") + "</td></tr>")
    chapters_html = f"""
  <h2 id="chapters">The argument in eight chapters</h2>
  <p class="stampline">{st("writeup/chapters", "writeup/browse")}</p>
  <div class="scroll"><table class="chap">
   <thead><tr><th>chapter</th><th>title and notes</th><th>pages (handout / reading edition)</th><th>read</th></tr></thead>
   <tbody>
{chr(10).join(rows)}
   </tbody>
  </table></div>"""

    # ---------------------------------------------------------------- sources
    art = man["artifact"]
    art_ref = (f'edition {esc(art["edition"])}, <a href="{esc(art["repository"])}/commit/{esc(art["commit"])}">commit '
               f'<code>{esc(art["commit"][:7])}</code></a> (the commit that the notes were read from)')
    head_sha, _ = last_commit()
    sources = [
        (f"{REPO_URL}#readme", "The status dashboard", "Who has checked what, with sources, and the theorem in full.",
         stamp("README.md")),
        (REPO_URL, "The repository", "The scripts that generate every page of this site, the data, and the Lean skeleton.",
         stamp(prefix="latest change")),
        (f"{REPO_URL}/tree/main/writeup", "The write-up on GitHub, for agents", "The structured proofs, the LaTeX sources "
         "of every note, the catalogue as data, and a guide.", st("writeup")),
        ("https://github.com/lsernau/grh-lean", "The condensed Lean proof", "The Lean repository that the write-up reads.",
         art_ref),
        ("https://nasqret.github.io/riemann-proof-atlas/", "The proof atlas", "The declarations of the Lean archive placed "
         "on a map of the literature; kept at its own address and versioned there.", ""),
    ]
    src_html = "\n".join(
        f'<li><b><a href="{esc(h)}">{esc(t)}</a></b> · {esc(d)}' + (f'<span class="stamp">{s}</span>' if s else "") + "</li>"
        for h, t, d, s in sources)

    # ---------------------------------------------------------------- earlier materials
    def last_changed(*paths: str) -> str:
        sha, date = last_commit(*paths)
        ref = commit_ref(sha)
        return "last changed " + (short_date(date) if date else "date unknown") + (f" · {ref}" if ref else "")

    earlier = [("atlas/", "The atlas", "an interactive map of the argument of the original announcement",
                last_changed("atlas/index.html")),
               ("guide/proof-guide.pdf", "The guide (PDF)", "the argument in standard terminology, "
                f"{GUIDE_PAGES} pages; also <a href=\"guide/proof-guide.gif\">as an animated GIF</a>",
                last_changed("guide/proof-guide.pdf", "guide/proof-guide.gif")),
               ("summary/grh-condensed-summary.pdf", "The condensed-proof note of 25 November (PDF)",
                "our first note on the condensed proof", last_changed("summary/grh-condensed-summary.pdf")),
               ("blueprint/atlas-blueprint.pdf", "The illustrated blueprint (PDF)",
                "the map as a document, with a link to the source line of every declaration",
                last_changed("blueprint/atlas-blueprint.pdf"))]
    if has_book:
        earlier.append(("book/", "The book", "chapters with formulas, figures and computations", last_changed("book")))
    earlier_html = "\n".join(
        f'<li><b><a href="{esc(h)}">{esc(t)}</a></b> · {d}<span class="stamp">{s}</span></li>'
        for h, t, d, s in earlier)

    sha = os.environ.get("GITHUB_SHA", "") if PUBLIC else ""
    sha = sha if re.fullmatch(r"[0-9a-f]{40}", sha) else (head_sha if PUBLIC else None)
    _, head_date = last_commit()
    built = (f'Built from commit <a href="{REPO_URL}/commit/{sha}"><code>{sha[:7]}</code></a>' if sha
             else "Local build of the working copy" + (f", last commit of {short_date(head_date)}" if head_date else ""))
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The announced proof of the Riemann hypothesis, read as mathematics</title>
<meta name="description" content="A reading of the condensed Lean proof announced as a proof of the Riemann hypothesis, written as mathematics: the browsable proof, the handout and every edition. A working draft, not refereed by a human; it does not settle correctness.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>{CSS}{WRITEUP_CSS}</style>
</head>
<body>
<header class="hero">
  <div class="hero-bg" aria-hidden="true">{curve}</div>
  <div class="wrap hero-grid">
    <div>
      <div class="label">A reading of an announced proof · a working draft</div>
      <h1>The announced proof of the <em>Riemann hypothesis</em>, read as mathematics</h1>
      <p class="lead">A proof was announced on 20&nbsp;November&nbsp;2026, as a formal proof in Lean; a condensed
      version appeared on 25&nbsp;November. This site reads the condensed proof into mathematics, note by note, and
      records who has checked what. It does not settle whether the proof is correct.</p>
      <p class="status"><b>{esc(ms["headline"])}</b><br><span>Record of {esc(utc(ms["as_of"]))}; the mathematics has not
      yet been refereed.</span></p>
      <div class="cta"><a class="btn" href="writeup/browse/">Browse the proof</a>
      <a class="btn ghost" href="writeup/handout.pdf">The handout (PDF)</a>
      {'<a class="btn ghost" href="writeup/' + esc(reading["file"]) + '">The reading edition (PDF)</a>' if reading else ''}
      <a class="btn ghost" href="writeup/#editions">Every edition</a></div>
    </div>
    {shot}
  </div>
</header>
<main class="wrap">
  <p class="note"><b>What this is.</b> A working draft, read by AI agents and checked by programs; no mathematician has
  refereed it. The formal proof it reads is a claim: its authors report that Lean's kernel accepts the five final
  theorems with the three standard axioms. Nothing here says that the Riemann hypothesis is proved, and this is not an
  official companion to the announcement.</p>
  <h2 id="read">Read the proof</h2>
  <p class="stampline">{st("writeup")}</p>
  <div class="grid">
{card_html}
  </div>
{chapters_html}
  <h2 id="sources">Sources</h2>
  <ul class="list">
{src_html}
  </ul>
  <section class="earlier">
    <h2 id="earlier">Earlier materials</h2>
    <p>These were made for the original announcement. They are kept at their addresses and are superseded by the
    write-up above.</p>
    <ul class="list">
{earlier_html}
    </ul>
  </section>
</main>
<footer><div class="wrap">
  <p>{built}. {esc(curve_caption)}</p>
  <p>The announcement and the Lean archive belong to their author. Everything original on this site may be used for
  any purpose (<a href="{REPO_URL}/blob/main/LICENSE">licence</a>).</p>
</div></footer>
</body>
</html>
"""


def site_atlas() -> str:
    """The atlas as it is served: links that leave the site point to the repository."""
    text = (ROOT / "atlas" / "index.html").read_text(encoding="utf-8")
    marker = "<!--site-links-->"
    if text.count(marker) != 1:
        raise SystemExit("site: the atlas has no place for the links of the site (marker missing)")
    banner = ('<div style="background:#fef3c7;color:#78350f;padding:10px 20px;font:500 14px/1.5 Inter,Helvetica,Arial,sans-serif;'
              'text-align:center">An earlier map, made for the original archive and kept at this address. The current '
              'material is the write-up of the condensed proof: <a href="../index.html" style="color:#78350f">the home '
              'page</a> · <a href="../writeup/index.html" style="color:#78350f">the write-up</a>.</div>')
    if text.count("<body>") != 1:
        raise SystemExit("site: the atlas has no single <body> tag for its banner")
    text = text.replace("<body>", "<body>\n" + banner, 1)
    text = text.replace(marker, '<a href="../index.html">Home of this site</a><br><a href="../book/index.html">The book</a><br>')
    text = text.replace('href="../README.md"', f'href="https://github.com/{REPO}#readme"')
    return re.sub(r'href="\.\./((?:lean|lean-mathlib|scripts|data|verification|references)/[^"#]+)',
                  lambda m: f'href="{BLOB}{m.group(1)}', text)


def relative_links(page: Path) -> list[str]:
    text = page.read_text(encoding="utf-8")
    text = re.sub(r"<script\b.*?</script>", "", text, flags=re.S)      # data and code are not links
    out = []
    for target in set(re.findall(r'(?:href|src)="([^"#][^"]*)"', text)):
        if re.match(r"[a-z][a-z0-9+.-]*:|//", target):
            continue
        path = (page.parent / target.split("#")[0].split("?")[0]).resolve()
        if path.is_dir():
            path = path / "index.html"
        if not path.exists():
            out.append(f"{page.relative_to(OUT)}: {target}")
    return sorted(out)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--require-book", action="store_true")
    args = ap.parse_args()
    book = ROOT / "book" / "_build" / "html"
    has_book = (book / "index.html").is_file()
    if args.require_book and not has_book:
        print("site: the book has not been built (book/_build/html/index.html is missing)")
        return 1
    if not ((ROOT / "writeup" / "editions.json").is_file() and (ROOT / "writeup" / "chapters").is_dir()):
        print("site: writeup/editions.json or writeup/chapters/ is missing; run scripts/import_writeup.py")
        return 1
    if OUT.exists():
        shutil.rmtree(OUT)
    for sub in ("atlas", "guide", "blueprint", "digests", "summary", "writeup"):
        (OUT / sub).mkdir(parents=True)
    (OUT / ".nojekyll").write_text("", encoding="utf-8")                 # the book has folders that begin with "_"
    (OUT / "atlas" / "index.html").write_text(site_atlas(), encoding="utf-8")
    for rel in ("guide/proof-guide.pdf", "guide/proof-guide.gif", "blueprint/atlas-blueprint.pdf",
                "summary/grh-condensed-summary.pdf", "writeup/handout.pdf", "writeup/catalogue-full.pdf",
                "writeup/MANIFEST.json", "writeup/editions.json", "writeup/AGENTS.md", "writeup/README.md"):
        shutil.copy2(ROOT / rel, OUT / rel)
    # the current edition of the write-up: its chapters, and the reading edition and the annotated version in the
    # browser when the import has brought them (scripts/import_writeup.py); earlier editions stay at their commits
    shutil.copytree(ROOT / "writeup" / "chapters", OUT / "writeup" / "chapters")
    for sub in ("reading", "browse"):
        if (ROOT / "writeup" / sub).is_dir():
            shutil.copytree(ROOT / "writeup" / sub, OUT / "writeup" / sub)
    (OUT / "writeup" / "index.html").write_text(writeup_page(), encoding="utf-8")
    if (OUT / "writeup" / "browse").is_dir():           # read by the pages of the browsable proof
        (OUT / "writeup" / "browse" / "stamp.json").write_text(
            json.dumps(stamp_json(load("writeup/MANIFEST.json"), load("writeup/editions.json")), indent=1) + "\n",
            encoding="utf-8")
    if SCREEN.is_file():
        (OUT / "assets" / "screens").mkdir(parents=True)
        shutil.copy2(SCREEN, OUT / "assets" / "screens" / SCREEN.name)
    (OUT / "digests" / "editions").mkdir(exist_ok=True)
    for slug in ("tower-bound", "local-nilpotence", "layer-descent"):
        shutil.copy2(ROOT / f"digests/{slug}/{slug}.pdf", OUT / "digests" / f"{slug}.pdf")
        # for readers that show the note beside the Lean text: every cited declaration with its place in the PDF
        shutil.copy2(ROOT / f"digests/{slug}/reader.json", OUT / "digests" / f"{slug}.json")
        # every published edition of a note stays at a permanent address, named by its SHA-256
        for f in sorted((ROOT / f"digests/{slug}/editions").glob("*.pdf")):
            shutil.copy2(f, OUT / "digests" / "editions" / f.name)
    if has_book:
        shutil.copytree(book, OUT / "book", ignore=shutil.ignore_patterns(".doctrees", ".buildinfo"))
    (OUT / "index.html").write_text(home(has_book), encoding="utf-8")

    noisy = []              # pages of the book into which a computation printed a warning
    if has_book:
        noisy = sorted(p.name for p in (OUT / "book").glob("*.html")
                       if 'class="output stderr' in p.read_text(encoding="utf-8"))
    broken = (relative_links(OUT / "index.html") + relative_links(OUT / "atlas" / "index.html")
              + relative_links(OUT / "writeup" / "index.html"))
    if not has_book:        # the link to the book is expected to be open until the book is built
        broken = [b for b in broken if "book/" not in b]
    files = [p for p in OUT.rglob("*") if p.is_file()]
    size = sum(p.stat().st_size for p in files) / 2**20
    print(f"site: _site/, {len(files)} files, {size:.1f} MiB, book {'included' if has_book else 'not built'}; "
          f"served at {SITE}/" + ("" if not broken else " -- BROKEN LINKS: " + "; ".join(broken))
          + ("" if not noisy else " -- WARNINGS PRINTED INTO THE BOOK: " + ", ".join(noisy)))
    return 1 if broken or noisy else 0


if __name__ == "__main__":
    sys.exit(main())
