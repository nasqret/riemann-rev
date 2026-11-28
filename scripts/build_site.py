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
import os
import re
import shutil
import sys
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_guide import GUIDE_PAGES  # noqa: E402
from build_readme import REPO, SITE, STEPS, load, utc  # noqa: E402

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
.hero-bg { position:absolute; inset:0 0 0 auto; width:70%; height:100%; opacity:.9; }
.hero-bg svg { width:100%; height:100%; display:block; }
.hero-content { position:relative; z-index:2; max-width:720px; padding:76px 28px 72px 48px; }
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
h2 { color:var(--heading); font-size:1.35rem; margin:38px 0 16px; letter-spacing:-.01em; }
.grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(310px,1fr)); gap:18px; }
.card { display:block; background:var(--surface); border:1px solid var(--border); border-top:4px solid var(--c);
  border-radius:14px; padding:20px 22px 18px; color:var(--text);
  box-shadow:0 1px 3px rgba(15,23,42,.06),0 6px 16px rgba(15,23,42,.06); transition:transform .15s,box-shadow .15s; }
.card:hover { text-decoration:none; transform:translateY(-2px);
  box-shadow:0 4px 12px rgba(15,23,42,.08),0 14px 32px rgba(15,23,42,.12); }
.card h3 { margin:0 0 6px; color:var(--heading); font-size:1.08rem; }
.card p { margin:0 0 12px; font-size:.93rem; color:#475569; }
.card .go { font-weight:600; font-size:.88rem; color:var(--c); }
footer { margin-top:44px; padding:26px 0 54px; border-top:1px solid var(--border); color:var(--muted);
  font-size:.86rem; }
footer p { margin:0 0 6px; }
@media (max-width:760px) { .hero-bg { width:100%; opacity:.4; } .hero-content { padding:48px 20px 52px; } }
@media (prefers-reduced-motion:reduce) { .card { transition:none; } }
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

    cards = [("accent", "The handout", "The whole reading in one PDF: the summary, the overview of the argument, "
                                       "Chapters I–VIII, the catalogue of quoted results and the record of checks. "
                                       "Every statement and every step links to the Lean lines it renders. "
                                       f"{h['pages']:,} pages, {mb(h['bytes'])}.", "handout.pdf", "Read the handout (PDF)")]
    if parts:
        cards.append(("arith", "Chapter by chapter", f"The same pages in {len(parts)} PDFs: the front matter, one PDF "
                                                     "per chapter, and the catalogue with the record of checks. A link "
                                                     "into another part opens that part at the right page.",
                      "#chapters", "Choose a chapter"))
    if reading:
        cards.append(("est", "The reading edition", "The same text without the links to the Lean source, for reading "
                                                    f"from beginning to end. {reading['pages']:,} pages, "
                                                    f"{mb(reading['bytes'])}.", reading["file"],
                      "Read the reading edition (PDF)"))
    if browse:
        cards.append(("ana", "The annotated version, in the browser", "Each note in the browser, beside the structured "
                                                                      "proofs and the Lean lines of its statements.",
                      "browse/", "Open the annotated version"))
    cards += [("dest", "The catalogue of quoted results", "Every background result that the argument uses, classified as "
                                                         "a definition, an elementary lemma, a named theorem or a "
                                                         "substantial result, with references; for a named theorem, how "
                                                         "the formal statement compares with the published one. "
                                                         f"{cat['pages']:,} pages.", "catalogue-full.pdf",
               "Read the catalogue (PDF)"),
              ("ok", "For AI agents, and for checking", "The structured proofs (every proof a tree of small steps, each "
                                                        "quoting the Lean lines it renders), the LaTeX source of every "
                                                        "note, the catalogue as data, and a guide for AI agents.",
               f"{repo}/tree/main/writeup", "Open the folder")]
    card_html = "\n".join(
        f'<a class="card" style="--c:var(--{c})" href="{esc(href)}"><h3>{esc(title)}</h3><p>{esc(text)}</p>'
        f'<span class="go">{esc(go)} →</span></a>' for c, title, text, href, go in cards)

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
  <p class="what">The pages of the handout cut at its chapters; the pages keep the handout's numbers, and every link is
  kept: a link into another part opens that part at the right page{', and the reading edition is cut the same way' if by_name else ''}.</p>
  <div class="scroll"><table>
   <thead><tr><th>part</th><th>contents</th><th>handout pages</th><th>annotated</th>{'<th>reading edition</th>' if by_name else ''}</tr></thead>
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
    buttons += ['<a class="btn ghost" href="browse/">The annotated version</a>'] if browse else []
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
  {f'<p class="what">What changed: {esc(cur["description"])}.</p>' if cur.get('description') else ''}
  <div class="grid">
{card_html}
  </div>
{chapters_html}
  <h2 id="editions">Every edition <span class="sub">{len(ed_rows)} editions since {day(first)}</span></h2>
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


def hero_svg() -> str:
    svg = (ROOT / "assets" / "figures" / "hero.svg").read_text(encoding="utf-8")
    svg = re.sub(r"^<\?xml[^>]*\?>\s*", "", svg)
    return svg.replace('width="', 'data-w="', 1).replace('height="', 'data-h="', 1).replace(
        "<svg ", '<svg preserveAspectRatio="xMidYMid slice" ', 1)


def home(has_book: bool) -> str:
    model = load("data/model.json")
    st = model["status"]
    comps = model["components"]
    n_decl = sum(1 for n in model["nodes"] if n["kind"] != "motivation")
    chapters = len(re.findall(r"^\s*-?\s*(?:file|root):", (ROOT / "book" / "_toc.yml").read_text(encoding="utf-8"), flags=re.M))
    repo = f"https://github.com/{REPO}"
    wm = load("writeup/MANIFEST.json")              # scripts/import_writeup.py: the edition of the write-up
    cur = load("writeup/editions.json")["current"]
    extra = "".join(s for s, on in ((", a reading edition without the Lean links", wm.get("reading")),
                                    (", the annotated version in the browser", wm.get("browse"))) if on)
    cards = [
        ("ok", "The write-up (working draft)", f"A complete reading of the condensed proof as mathematics: "
                                               f"{len(wm['notes'])} notes on all {len(wm['units'])} units, from the five "
                                               "theorems down, each statement linked to its Lean lines: the handout whole "
                                               f"and chapter by chapter{extra}, and every edition. Read by AI agents and "
                                               "checked by programs; not yet refereed by a human.",
         "writeup/", "Open the write-up"),
        ("ok", "The condensed proof", "25 November 2026: the same five theorems in 112,827 lines instead of 17.4 million, "
                                      "24,850 of them for the argument itself. What happened, how the argument goes, "
                                      "and what has been checked, with links into the Lean source.",
         "summary/grh-condensed-summary.pdf", "Read the note (PDF)"),
        ("arith", "The atlas", f"An interactive map: the {len(comps)} components, a guided tour, the graph of "
                               f"{n_decl} declarations with links to their Lean source, illustrated ideas and the "
                               "verification ledger.", "atlas/", "Open the atlas"),
        ("est", "The guide", f"The whole argument in standard mathematical terminology, {GUIDE_PAGES} pages: the "
                             "theorem, the steps, and why each idea calls for the next. Every symbol is defined.",
         "guide/proof-guide.pdf", "Read the guide (PDF)"),
    ]
    # The three deformalization notes of the original long proof (tower-bound, local-nilpotence, layer-descent) are no
    # longer shown on the site's pages (owner, 27 Nov 2026); their PDFs and reader indexes are still copied below, so
    # that their URLs, which the embedding atlas uses, keep working.
    if has_book:
        cards.append(("ana", "The book", f"{chapters} chapters with formulas, figures and computations that are "
                                         "executed every time the site is built.", "book/", "Open the book"))
    cards += [
        ("dest", "The illustrated blueprint", "The map as a document: every declaration with its statement in words "
                                              "and a link to its source line.", "blueprint/atlas-blueprint.pdf",
         "Read the blueprint (PDF)"),
        ("ok", "The status dashboard", f"Who has checked what, with sources; the theorem in full; the route of the "
                                       f"proof in {len(STEPS)} steps with links to the formal proofs.",
         f"{repo}#readme", "Open the dashboard"),
        ("accent", "The sources", "The Lean skeleton of the argument, the data with their provenance, the logs, and "
                                  "the scripts that generate every page of this site.", repo, "Open the repository"),
    ]
    card_html = "\n".join(
        f'<a class="card" style="--c:var(--{c})" href="{esc(href)}"><h3>{esc(title)}</h3><p>{esc(text)}</p>'
        f'<span class="go">{esc(go)} →</span></a>' for c, title, text, href, go in cards)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The announced proof of the Riemann hypothesis: map, guide and record of checks</title>
<meta name="description" content="A map, a guide and a verification dashboard for the formal proof of the Riemann hypothesis announced by Levent Alpöge on 20 November 2026. An independent reading aid.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<header class="hero">
  <div class="hero-bg" aria-hidden="true">{hero_svg()}</div>
  <div class="hero-content">
    <div class="label">A map · a guide · a record of checks</div>
    <h1>The announced proof of the <em>Riemann hypothesis</em></h1>
    <p class="lead">On 20&nbsp;November&nbsp;2026 Levent Alpöge announced a proof of the Riemann hypothesis and of its
    analogue for Dirichlet L-functions, published as a formal proof in Lean. These pages map the argument, explain it
    in standard mathematical language, and record who has checked what.</p>
    <p class="status"><b>{esc(st["headline"])}</b><br><span>Record of {esc(utc(st["as_of"]))}; the mathematics has not
    yet been refereed.</span></p>
    <div class="cta"><a class="btn" href="writeup/">The write-up</a><a class="btn ghost" href="summary/grh-condensed-summary.pdf">The condensed proof (note)</a><a class="btn ghost" href="atlas/">Open the atlas</a><a class="btn ghost" href="guide/proof-guide.pdf">Read the guide</a>
    <a class="btn ghost" href="{repo}#readme">Status dashboard</a></div>
  </div>
</header>
<main class="wrap">
  <p class="note"><b>What this site is.</b> A map of an announced proof and a record of who has checked what. It is not
  a proof, not a referee report and not an endorsement, and it is not an official companion to the announcement.</p>
  <p class="note"><b>Since 26&nbsp;November&nbsp;2026: the write-up, a working draft</b> (now
  <a href="writeup/#editions">edition {cur['edition']}</a>). The condensed proof read as mathematics, unit by unit:
  <a href="writeup/handout.pdf">the handout (PDF)</a>, in which every statement links to the Lean lines it renders, also
  <a href="writeup/#chapters">chapter by chapter</a>{'; <a href="writeup/' + esc(wm['reading']['file']) + '">a reading edition</a> without the Lean links' if wm.get('reading') else ''}{'; <a href="writeup/browse/">the annotated version in the browser</a>' if wm.get('browse') else ''};
  <a href="writeup/catalogue-full.pdf">the catalogue of quoted results</a>; <a href="writeup/#editions">every edition</a>; and,
  for AI agents, <a href="{repo}/tree/main/writeup">the structured proofs, the LaTeX sources and a guide</a>. Read by AI
  agents and checked by programs; not yet refereed by a human. It does not say that RH is proved.</p>
  <p class="note"><b>25&nbsp;November&nbsp;2026: a condensed proof.</b> A rewriting of the proof by Luke Sernau,
  colleagues at Anthropic and Claude states the same five theorems in 112,827 lines of Lean instead of 17.4 million;
  the argument itself takes 24,850 lines of code, the background is separated and referenced. Machines have checked it;
  no mathematician has read it yet. <a href="summary/grh-condensed-summary.pdf">Read our note</a> ·
  <a href="https://github.com/lsernau/grh-lean">the repository</a> ·
  <a href="https://nasqret.github.io/riemann-proof-atlas/">the proof atlas</a></p>
  <h2>Where to go</h2>
  <div class="grid">
{card_html}
  </div>
</main>
<footer><div class="wrap">
  <p>Built from <a href="{repo}">{esc(REPO)}</a>; the record shown is as of {esc(utc(st["as_of"]))}. The curve above is
  computed: the centred prime sum, normalized, for arguments up to ten million.</p>
  <p>The announcement and the Lean archive belong to their author. Everything original on this site may be used for
  any purpose (<a href="{repo}/blob/main/LICENSE">licence</a>).</p>
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
