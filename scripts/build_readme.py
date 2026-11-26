#!/usr/bin/env python3
"""Generate README.md, the public dashboard of the repository.

    python3 -B scripts/build_readme.py            # write README.md
    python3 -B scripts/build_readme.py --check    # fail if README.md is not what would be written

Everything that is a status, a count, a time or a link to a declaration is taken from the data:
data/model.json (the component model and the status record of the reading project),
data/sync-log.json (one line per import of that record), data/source/PROVENANCE.json,
data/source/sources.json, data/source/native-scopes.json, assets/figures/facts.json and the logs in
verification/logs/. The explanatory prose is written here, in this file. The script refuses to
write a README that contains a link into a private place or a relative link to a missing file.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.parse
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_guide  # noqa: E402  (the table of cited Lean declarations is shared with the guide)

REPO = "nasqret/riemann-rev"
SITE = "https://nasqret.github.io/riemann-rev"      # GitHub Pages, built by .github/workflows/pages.yml
PROOF_ATLAS = "https://nasqret.github.io/riemann-proof-atlas/"   # the reading project's atlas: declarations on the paper map
ARCHIVE_URL = "https://alpo.ge/lean.tar.gz.part01"          # footnote 1 of the announcement: parts 01 to 14
ICON = {"two-kernels": "✅", "checked": "✅", "partial": "🟡", "covered": "🟢", "read": "🔵", "reported": "↗️",
        "motivation": "⚪"}


def load(rel: str):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def utc(stamp: str) -> str:
    """'2026-11-20T23:51:25Z' -> '2026-11-20 23:51 UTC'."""
    return stamp[:16].replace("T", " ") + " UTC"


def badge(label: str, message: str, colour: str, link: str | None = None) -> str:
    enc = lambda s: urllib.parse.quote(s.replace("-", "--").replace("_", "__").replace(" ", "_"), safe="")
    img = f'<img alt="{label}: {message}" src="https://img.shields.io/badge/{enc(label)}-{enc(message)}-{colour}">'
    return f'<a href="{link}">{img}</a>' if link else img


def big(number: str, caption: str, colour: str) -> str:
    """A key figure as a large badge."""
    enc = lambda s: urllib.parse.quote(s.replace("-", "--").replace("_", "__").replace(" ", "_"), safe="")
    return (f'<img alt="{number} {caption}" src="https://img.shields.io/badge/{enc(number)}-{enc(caption)}-{colour}'
            f'?style=for-the-badge&labelColor=24292f">')


def table(head: list[str], rows: list[list[str]], align: list[str] | None = None) -> str:
    cell = lambda s: str(s).replace("\n", " ").replace("|", "\\|")
    sep = align or ["---"] * len(head)
    out = ["| " + " | ".join(head) + " |", "| " + " | ".join(sep) + " |"]
    out += ["| " + " | ".join(cell(c) for c in r) + " |" for r in rows]
    return "\n".join(out)


def link(text: str, url: str | None) -> str:
    return f"[{text}]({url})" if url and url.startswith("http") else text


def who(operator: str) -> str:
    """The record calls the reading project by the name of the machine it runs on."""
    return "the reading project" if "reading project" in operator.lower() else operator


def first(stages: list[dict], needle: str) -> dict | None:
    return next((s for s in stages if needle.lower() in s["stage"].lower()), None)


# The seven steps of the argument, in the order of the guide (from the theorem back to its input).
# 'lean' lists (label, key) with keys of build_guide.LEAN; 'comps' are components of the model.
STEPS = [
    dict(n=1, slug="step-1-reflection", title="Reflection", stratum="dest", comps=["endpoints", "reflection", "descent"],
         one="A zero left of the critical line would have a mirror image right of it.",
         text="An $L$-function has a symmetry, its *functional equation*, which exchanges $s$ and $1-s$. A zero "
              "with $\\operatorname{Re}s<\\tfrac12$ would therefore produce a zero with $\\operatorname{Re}s>\\tfrac12$. "
              "So it is enough to prove that there are **no zeros to the right of the line**. A second classical "
              "step passes from the *primitive* characters to all characters, whose $L$-functions differ only by "
              "finitely many harmless factors.",
         math="\\Lambda(s,\\chi)=W(\\chi)\\,\\Lambda(1-s,\\bar\\chi)\\qquad\\Longrightarrow\\qquad"
              "\\text{it suffices that } L(s,\\psi)\\neq0\\ \\text{ for }\\operatorname{Re}s>\\tfrac12,\\ \\psi\\text{ primitive.}",
         where="$\\Lambda(s,\\chi)$ is $L(s,\\chi)$ completed by its Gamma factor, $W(\\chi)$ a complex number of "
               "absolute value $1$, $\\bar\\chi$ the complex conjugate character and $\\psi$ any primitive character.",
         lean=[("all characters", "imprimitive"), ("reflection", "strip"), ("reflection for ζ", "rh-right")]),
    dict(n=2, slug="step-2-the-statistic", title="The statistic", stratum="ana", comps=["statistic", "residues"],
         one="A weighted count of primes whose size encodes the zeros.",
         text="Instead of counting primes one weighs each prime power $n\\le y$ by a *ramp* $y/n-1$ and subtracts "
              "the expected main term. The resulting function $G(y)$ is of size $\\sqrt y$ exactly when the Riemann "
              "hypothesis holds, because every zero $\\rho$ of $\\zeta$ contributes an oscillating term $y^{\\rho}$. "
              "For a Dirichlet character $\\chi$ there is an analogous sum $g_\\chi(y)$.",
         math="G(y)=\\sum_{n\\le y}\\Lambda(n)\\Bigl(\\frac yn-1\\Bigr)-y\\,(\\log y-1-\\gamma)"
              "=\\log 2\\pi-\\sum_{\\rho}\\frac{y^{\\rho}}{\\rho(\\rho-1)}+O(y^{-2})",
         where="$\\Lambda(n)=\\log p$ if $n$ is a power of the prime $p$ and $0$ otherwise, $\\gamma$ is Euler's constant, "
               "and $\\rho$ runs over the zeros of $\\zeta$ in the critical strip.",
         lean=[("the two sums", "G"), ("transform of the ramp", "mellin"), ("poles and residues", "pole")]),
    dict(n=3, slug="step-3-a-localized-landau-theorem", title="A localized Landau theorem", stratum="ana",
         comps=["criterion", "choreography"],
         one="An upper bound on long intervals already excludes zeros.",
         text="This is the analytic heart, and it is elementary to state. One does not need $G$ to be small in "
              "absolute value, nor for all $y$. If a combination of such sums with **positive coefficients** stays "
              "below $y^{\\theta}$ throughout infinitely many long intervals (*windows*) $[Y,Y^{1+\\delta}]$, then "
              "none of the $L$-functions involved has a zero with real part larger than $\\theta$. One-sided, "
              "sparse information is enough. The arithmetic part of the proof has to deliver exactly this, in "
              "the form of statement $(\\star)$ below.",
         math="(\\star)\\qquad\\text{for every small }\\varepsilon>0\\text{ there are arbitrarily large }Y\\text{ with }\\ "
              "G_\\psi(x)\\le x^{1/2+9\\varepsilon}\\ \\text{ for all }x\\in[Y,Y^{3/2}]",
         where="$\\psi$ is the primitive character under study and $o$ its order; $G_\\psi$ is $G$ plus $1/(3o+1)$ times "
               "the real parts of the sums $g_\\chi$ for the other powers $\\chi$ of $\\psi$; $\\varepsilon$ is "
               "chosen after the hypothetical zero.",
         lean=[("the criterion", "landau"), ("the order of choices", "window-consumer"), ("", "zero-top")]),
    dict(n=4, slug="step-4-the-estimate-i-a-slope-inequality-for-a-chain-of-theta-lifts",
         title="The estimate, I: a slope inequality for a chain of theta lifts", stratum="est", comps=["family"],
         one="Numbers divisible by many primes cannot be small: an upper bound for a prime sum.",
         text="Where can an *upper* bound for a sum over primes come from? From divisibility. A non-zero "
              "algebraic integer that is divisible by many primes cannot be small. The proof builds such numbers "
              "from theta functions attached to number fields with complex multiplication and shows that they "
              "are highly divisible at the primes that stay prime (are *inert*) in an auxiliary quadratic field "
              "$K=\\mathbb Q(\\sqrt{-d})$. Weighing divisibility against size gives an inequality whose two sides "
              "are a prime sum ($\\mathrm{ASK}$) and its expected main term ($\\mathrm{MAIN}$). To make the error "
              "small the construction is iterated $m$ times, in a *chain of theta lifts* between unitary groups, "
              "and the bookkeeping is done by Bost's slope inequality. The two costs $x/m$ and $m$ balance at "
              "$m\\approx\\sqrt x$: this is where the square root of the Riemann hypothesis comes from.",
         math="\\begin{aligned}\\frac1b\\Bigl(\\mathrm{ASK}(a)-\\mathrm{MAIN}(a)\\Bigr)\\ &\\le\\ x^{O(\\varepsilon)}\\Bigl(\\frac xm+m+\\sqrt x\\Bigr),\\\\[6pt]"
              "\\mathrm{ASK}(a)-\\mathrm{MAIN}(a)\\ &=\\ w\\,\\bigl(G(y)-g_{\\chi_{-d}}(y)\\bigr)\\qquad\\text{for equal weights } w,\\ \\text{with } y=a/w.\\end{aligned}",
         where="$x$ is the point at which the bound is wanted and $m$ the number of lifts; $a>0$ is a size parameter "
               "(the *height*), and $w$, $b$ are weights with $a/b\\approx x$. "
               "$\\mathrm{ASK}(a)=\\sum_n\\Lambda(n)\\,(1-\\chi_{-d}(n))\\,\\max(a/n-w_n,0)$ measures the divisibility gained, "
               "$\\mathrm{MAIN}(a)=a\\,(\\log a-1-\\gamma+\\tfrac{L'}{L}(1,\\chi_{-d})-\\overline{\\log w})$ is its expected size, "
               "and $\\chi_{-d}$ is the quadratic character of $K$. $G$ and $g_\\chi$ are the sums of step 2.",
         lean=[("hosts", "ischifield"), ("integrality", "chainint"), ("local divisibility", "minor"),
               ("slopes", "slope"), ("periods", "chowla"), ("the two sides", "ask"), ("sizes", "rank"),
               ("the outcome", "topg")]),
    dict(n=5, slug="step-5-the-estimate-ii-from-the-slope-inequality-to-the-bound",
         title="The estimate, II: from the slope inequality to the bound", stratum="est",
         comps=["comparison", "hosts", "primes"],
         one="Fourier analysis isolates the wanted character with positive weights.",
         text="The inequality of step 4 involves the wrong characters, and with a minus sign. Fourier analysis on "
              "the Galois group of the auxiliary field, with deliberately unequal weights, isolates the character "
              "$\\psi$ under study and its powers, with coefficients that are positive *by design*. The remaining "
              "unwanted characters are removed with the help of two auxiliary primes $q$ and $d$, which an "
              "averaging argument allows one to choose so that the corresponding sums are small. The result is "
              "statement $(\\star)$ of step 3.",
         math="\\mathrm{ASK}(a)-\\mathrm{MAIN}(a)=\\frac1{\\lvert\\Phi\\rvert}\\sum_{\\chi}\\ \\sum_{\\sigma\\notin\\Phi}"
              "\\overline{\\chi(\\sigma)}\\;w_\\sigma\\;g_\\chi\\!\\Bigl(\\frac a{w_\\sigma}\\Bigr),\\qquad\\Phi=\\operatorname{Gal}(E/K)",
         where="$E$ is the auxiliary abelian number field containing $K$, built from $\\psi$ and the two primes; "
               "$\\chi$ runs over the characters of $\\operatorname{Gal}(E/\\mathbb Q)$, $\\sigma$ over its elements outside "
               "$\\Phi$, and $w_\\sigma$ are the weights; $g_1=G$.",
         lean=[("Fourier identity", "chbalance"), ("weights", "shares"), ("twisted characters", "bounded"),
               ("auxiliary primes", "pairex"), ("hosts at every scale", "supply"), ("the thick set", "behrend"),
               ("conclusion", "core-gm")]),
    dict(n=6, slug="step-6-the-price-of-divisibility-iwasawa-theory", title="The price of divisibility: Iwasawa theory",
         stratum="arith", comps=["cohomology"],
         one="The divisibility can fail a little; Galois cohomology measures by how much.",
         text="The divisibility used in step 4 holds only up to a loss, which is measured by Galois cohomology "
              "groups of the kind that occur in Vandiver's conjecture. No vanishing is needed, only a bound for "
              "their total size that holds throughout a whole window. Iwasawa theory (the theorem of Ferrero and "
              "Washington) shows that only boundedly many *twists* are expensive, and a pigeonhole argument finds "
              "a window that avoids them all.",
         math="\\sum_{\\ell}\\ \\log\\ell\\sum_{1\\le h<x^{401}}\\operatorname{len}\\,\\text{Ш}^1_\\ell(E,h)\\ \\le\\ \\exp\\bigl(x^{\\varepsilon}/2\\bigr)"
              "\\qquad\\text{for all }x\\in[Y,Y^2]",
         where="$\\ell$ runs over all primes and $h$ over the twists; $\\text{Ш}^1_\\ell(E,h)$ is the group of Galois "
               "cohomology classes of $E$ with coefficients $\\mathbb Q_\\ell/\\mathbb Z_\\ell(-h)$ that are trivial at the "
               "places above $\\ell$, and $\\operatorname{len}$ its length; $[Y,Y^2]$ is the window.",
         lean=[("the window", "vwin-def"), ("interval lemma", "window1")]),
    dict(n=7, slug="step-7-the-automorphic-foundation", title="The automorphic foundation", stratum="arith",
         comps=["galois", "inputs"],
         one="Galois representations attached to automorphic forms feed both branches.",
         text="Both the sizes in step 4 and the cohomology in step 6 are controlled by Galois representations "
              "attached to automorphic forms on $\\mathrm{GL}_n$ over CM fields, a central object of the Langlands "
              "programme. The archive does not cite the literature for them: it contains its own formal "
              "construction, together with the other inputs of the final assembly.",
         math="r_\\pi\\colon\\operatorname{Gal}(\\overline E/E)\\to\\mathrm{GL}_n(\\overline{\\mathbb Q}_\\ell),\\qquad"
              "\\iota\\,\\operatorname{charpoly}\\,r_\\pi(\\mathrm{Frob}_v^{-1})=\\prod_{\\alpha}\\bigl(X-q_v^{(n-1)/2}\\alpha\\bigr)",
         where="$\\pi$ is a cuspidal automorphic representation of $\\mathrm{GL}_n$ over the CM field $E$ (regular "
               "algebraic and polarized), $r_\\pi$ its $\\ell$-adic Galois representation, $\\mathrm{Frob}_v$ a Frobenius "
               "element, $q_v$ the size of the residue field, $\\alpha$ the Satake parameters of $\\pi$ at $v$, and "
               "$\\iota$ a fixed isomorphism $\\overline{\\mathbb Q}_\\ell\\cong\\mathbb C$.",
         lean=[("the Galois representations", "row-def"), ("", "row-prod"), ("the final assembly", "seven")]),
]

GLOSSARY = [
    ("Prime number theorem", "The number of primes up to $x$ is approximately $x/\\log x$. The Riemann hypothesis is a "
     "statement about the size of the error in this approximation."),
    ("Zeta function, $\\zeta(s)$", "The function $\\sum_{n\\ge1}n^{-s}$, extended to all complex $s\\ne1$. Its zeros "
     "control the distribution of the primes."),
    ("Critical strip, critical line", "The strip $0<\\operatorname{Re}s<1$, where all the interesting zeros lie, and its "
     "middle line $\\operatorname{Re}s=\\tfrac12$."),
    ("Dirichlet character, $L(s,\\chi)$", "A periodic multiplicative function $\\chi$ on the integers, and the series "
     "$\\sum\\chi(n)n^{-s}$ built from it. These govern the primes in arithmetic progressions."),
    ("GRH", "The generalized Riemann hypothesis. Here always in the form stated on this page: for Dirichlet "
     "$L$-functions."),
    ("Lean", "A proof assistant: a programming language in which statements and proofs are written so that a "
     "program can check every step."),
    ("Mathlib", "The community library of mathematics formalized in Lean. It contains the official formal "
     "definition `RiemannHypothesis`."),
    ("Kernel", "The small, carefully reviewed core of a proof assistant that checks finished proofs. Everything "
     "else may be unreliable; if the kernel accepts a proof, the proof is correct relative to the axioms."),
    ("NanoDA", "An independent kernel for Lean proofs, written in Rust. Agreement of two independently written "
     "kernels guards against a bug in either."),
    ("Axioms", "The unproved starting points. Lean's standard ones are `propext`, `Classical.choice` and "
     "`Quot.sound`; a proof that used anything else would be suspect."),
    ("Replay", "Re-checking, in the kernel, every declaration of a compiled library."),
    ("Challenge, comparator", "A separately written file that states the target theorems, and the tool that checks "
     "that a proof proves exactly those statements."),
    ("Window", "A long interval $[Y,Y^{1+\\delta}]$ of real numbers on which a bound is required."),
    ("Theta lift", "A classical construction that transfers automorphic forms from one group to another."),
    ("CM field", "A number field with complex multiplication, such as $\\mathbb Q(\\sqrt{-d})$ or a cyclotomic field."),
]


def build() -> str:
    model = load("data/model.json")
    st = model["status"]
    fp = st["full_proof"]
    stages = fp["stages"]
    pins = model["pins"]
    prov = load("data/source/PROVENANCE.json")
    sync = load("data/sync-log.json")
    src = load("data/source/sources.json")
    scopes = {s["id"]: s for s in load("data/source/native-scopes.json")}
    audit = load("verification/logs/axioms.json")
    zeta = load("verification/logs/mathlib-zeta-axioms.json") if (ROOT / "verification/logs/mathlib-zeta-axioms.json").exists() else None
    facts = load("assets/figures/facts.json")
    cond = load("data/condensed.json")            # scripts/measure_condensed.py: the editions of lsernau/grh-lean
    comps = {c["id"]: c for c in model["components"]}
    nodes = {n["id"]: n for n in model["nodes"]}
    tiers = model["tiers"]
    strata = {s["id"]: s for s in model["strata"]}
    mirror = f'{pins["mirror"]}/blob/{pins["mirror_commit"]}/src/'
    mirror_tree = f'{pins["mirror"]}/tree/{pins["mirror_commit"]}'

    def lean_url(key: str) -> tuple[str, str]:
        name, node, path = build_guide.LEAN[key]
        return name, (nodes[node]["url"] if node else mirror + path)

    def lean_links(items) -> str:
        out, last = [], None
        for label, key in items:
            name, url = lean_url(key)
            piece = f"[`{name}`]({url})"
            if label:
                out.append(f"{label} {piece}")
            else:
                out[-1] += f", {piece}"
        return " · ".join(out)

    def tier_text(t: str) -> str:
        return f'{ICON[t]} {tiers[t]["label"]}'

    as_of = utc(st["as_of"])
    imported = utc(prov["imported_utc"])
    modules = f'{src["lean_files"]:,}'
    assert modules in st["external"], "the module count of the archive is not in the status record"
    rust = first(stages, "Rust verification of the complete proof")
    compare = first(stages, "comparison with the independent Mathlib challenge")
    rebuilt = first(stages, "Recreate the reference")
    combined = first(stages, "Combined kernel and challenge check")
    axioms = first(stages, "Exact axiom set")
    n_rust = re.search(r"([\d,]+) declarations", rust["outcome"]).group(1) if rust else None
    own = [s for s in stages if "reading project" in s["operator"].lower()]
    others = [s for s in stages if "reading project" not in s["operator"].lower()]
    independent_ok = [s for s in others if re.search(r"(?i)accepted|justified|passed", s["outcome"]) and "url" in s]
    independent_people = list(dict.fromkeys(s["operator"] for s in independent_ok))
    n_decl = sum(1 for n in model["nodes"] if n["kind"] != "motivation")
    n_pinned = sum(1 for n in model["nodes"] if (n.get("url") or "").startswith(pins["mirror"]))
    two = fp["two_kernels"]
    dirichlet_modules = f'{scopes["dirichlet"]["original_project_module_count"]:,}'
    window_decls = f'{st["independent_window"]["declarations"]:,}'

    L: list[str] = []
    add = L.append

    # ------------------------------------------------------------------ header
    add('<div align="center">\n')
    add("# The announced proof of the Riemann hypothesis\n")
    add("**A map, a guide and a verification dashboard for the formal proof announced by Levent Alpöge "
        "on 20 November 2026, and for its condensed rewriting of 25 November**\n")
    add(f'<a href="{SITE}/"><img src="assets/figures/hero.svg" width="94%" '
        'alt="The centred prime sum (G(y) − log 2π)/√y computed for y up to ten million: it stays inside the band '
        'that the Riemann hypothesis predicts."></a>\n')
    ec, er = cond["editions"]["grh-compact"], cond["editions"]["grh"]
    row1 = [
        badge("condensed proof", f'{ec["all"]["lines"]:,} lines, {cond["factor_compact"]}× shorter', "8250df",
              "#the-condensed-proof-25-november-2026"),
        badge("status", "announced, machine-checked, not yet refereed", "8250df", "#status-dashboard"),
        badge("complete proof", "accepted by two independent kernels" if two else "full replay reported",
              "2ea44f" if two else "d4a72c", "#every-recorded-check-of-the-complete-proof"),
        badge("statements", "match the Mathlib challenge" if compare and "matched" in compare["outcome"].lower() else "see the record",
              "2ea44f", "#the-theorem"),
        badge("axioms", "propext · Classical.choice · Quot.sound", "2ea44f", "#status-dashboard"),
    ]
    row2 = [
        badge("record as of", as_of, "0969da", "#how-this-page-stays-current"),
        badge("archive", f"{modules} Lean modules", "57606a", mirror_tree),
        badge("Lean", pins["toolchain"].split(":v")[-1], "57606a"),
        badge("Mathlib", pins["mathlib"][:8], "57606a", f'https://github.com/leanprover-community/mathlib4/tree/{pins["mathlib"]}'),
        f'<a href="https://github.com/{REPO}/actions/workflows/checks.yml"><img alt="checks of this repository" '
        f'src="https://github.com/{REPO}/actions/workflows/checks.yml/badge.svg"></a>',
        f'<a href="https://github.com/{REPO}/actions/workflows/pages.yml"><img alt="build of the site" '
        f'src="https://github.com/{REPO}/actions/workflows/pages.yml/badge.svg"></a>',
    ]
    add(" ".join(row1) + "\n")
    add(" ".join(row2) + "\n")
    add(f"**New:** [the condensed proof, our note (PDF)]({SITE}/summary/grh-condensed-summary.pdf) · "
        f"[lsernau/grh-lean](https://github.com/{cond['repo']}/tree/{cond['commit']})\n")
    add(f"**Read it online:** [site]({SITE}/) · [atlas]({SITE}/atlas/) · [proof atlas]({PROOF_ATLAS}) · "
        f"[guide]({SITE}/guide/proof-guide.pdf) · [book]({SITE}/book/) · [blueprint]({SITE}/blueprint/atlas-blueprint.pdf)\n")
    add("[The condensed proof](#the-condensed-proof-25-november-2026) · [Status](#status-dashboard) · [The theorem](#the-theorem) · [New here?](#new-here-start-here) · "
        "[Route of the proof](#the-route-of-the-proof) · [Contents](#what-is-in-this-repository) · "
        "[Check it yourself](#check-it-yourself) · [Transparency](#transparency) · [FAQ](#questions-and-answers)\n")
    add("</div>\n")

    add("> [!IMPORTANT]\n"
        "> **What this page is.** A map of an announced proof and a record of who has checked what. It is not a "
        "proof, not a referee report and not an endorsement, and it is not an official companion to the "
        "announcement.\n>\n"
        "> **What is claimed.** On 20 November 2026 Levent Alpöge announced, in a four-page note written with the "
        f"AI system Claude, a proof of the Riemann hypothesis and of its analogue for Dirichlet $L$-functions. "
        f"The proof was published only as a formal proof in the Lean proof assistant: {modules} files that a "
        "computer can check, and that no human is expected to read from beginning to end.\n>\n"
        f"> **Where things stand** (record of {as_of}). {st['headline']} "
        "The human-readable mathematics has not been written up yet, and the argument has not been through the "
        "traditional refereeing of the mathematical community. Nothing here is this repository's own claim that "
        "the theorem is true; it reports the records listed below, with their sources.\n")

    # ------------------------------------------------------------------ the condensed proof (25 November 2026)
    tree = f"https://github.com/{cond['repo']}/tree/{cond['commit']}"
    blob = f"https://github.com/{cond['repo']}/blob/{cond['commit']}/grh-compact/"
    sub = cond["submission"]
    add("## The condensed proof (25 November 2026)\n")
    add("> [!NOTE]\n"
        f"> **The same five theorems in {ec['all']['lines']:,} lines of Lean instead of {sub['lines'] / 1e6:.1f} million.** "
        f"On 25 November 2026 [`lsernau/grh-lean`]({tree}) appeared: a rewriting of the proof \"produced in collaboration "
        "with my colleagues at Anthropic, and Claude\" (Luke Sernau), in two editions with byte-identical statements. "
        f"The argument itself, the folder `New` of the compact edition, is **{ec['New']['code_lines']:,} lines of code** "
        f"({ec['New']['theorems']:,} theorems); the background that Mathlib lacks is separated in `Lib` and labelled with "
        "references to the literature. Machines have checked it; **no mathematician has read it yet**, as its authors "
        "say.\n>\n"
        f"> **[Read our note: what happened, how the argument goes, what is checked (PDF)]({SITE}/summary/grh-condensed-summary.pdf)** "
        "· every Lean name in it links to its line at the pinned commit.\n")
    add(f'<p align="center"><a href="{SITE}/summary/grh-condensed-summary.pdf"><img src="assets/screens/condensed-note.png" '
        'width="70%" alt="The first page of the note on the condensed proof: what happened, and how large the simplification is."></a></p>\n')
    add("### What happened\n")
    add(table(["date (2026)", "event"], [
        ["20 Nov", f"Levent Alpöge announces the proof, written with Claude: a [four-page note](https://alpo.ge/remark.pdf) and a "
                   f"Lean archive of {sub['files']:,} files, {sub['lines']:,} lines. Independent kernel replays: "
                   "[the dashboard below](#status-dashboard)."],
        ["20 Nov", "The community repository [`leanprover-community/riemann-hypothesis`](https://github.com/leanprover-community/riemann-hypothesis) "
                   "opens and starts to clean up the archive."],
        ["25 Nov, 20:38 UTC", f"[`lsernau/grh-lean`]({tree}) is published: a readable edition (`grh/`, {er['all']['lines']:,} lines) "
                              f"and a compact one (`grh-compact/`, {ec['all']['lines']:,} lines) of the same five theorems."],
        ["25 Nov, 22:24 UTC", "The community repository moves its main branch to the readable edition; its CI builds every "
                              "commit and fails on `sorry` or on any axiom beyond the standard three."],
        ["26 Nov", "This repository publishes the note above and starts a complete human-readable write-up of the compact edition."],
    ]) + "\n")
    add("### How large the simplification is\n")
    add(table(["edition", "Lean files", "lines", "lines of code", "the argument (`New`)", "background (`Lib`)"], [
        [f"Alpöge's submission ([`{pins['mirror_commit'][:8]}`]({mirror_tree}))", f"{sub['files']:,}", f"{sub['lines']:,}", "", "", ""],
        [f"readable edition [`grh/`]({tree}/grh)", f"{er['all']['files']:,}", f"{er['all']['lines']:,}", f"{er['all']['code_lines']:,}",
         f"{er['New']['code_lines']:,} lines of code", f"{er['Lib']['code_lines']:,} lines of code"],
        [f"compact edition [`grh-compact/`]({tree}/grh-compact)", f"{ec['all']['files']:,}", f"{ec['all']['lines']:,}",
         f"{ec['all']['code_lines']:,}", f"**{ec['New']['code_lines']:,} lines of code, {ec['New']['theorems']:,} theorems**",
         f"{ec['Lib']['code_lines']:,} lines of code"],
    ], ["---", "---:", "---:", "---:", "---:", "---:"]) + "\n")
    add(f"Counted by `scripts/measure_condensed.py` on the pinned commits: the compact edition is {cond['factor_compact']} times "
        f"shorter than the submission, the readable one {cond['factor_readable']} times. `Lib` never imports `New`. A scan of "
        f"both editions finds {ec['all']['risky'] + er['all']['risky']} uses of `sorry`, `axiom`, `opaque`, `unsafe`, "
        "`native_decide`, `implemented_by`, custom syntax or code run at compile time.\n")
    add("### How the argument goes, in five lines\n")
    add(f"1. **GRH from a one-sided bound for primes** ([`entireL_ne_zero_of_primeError_le`]({blob}src/New/Endgame/OneSidedCriterion.lean#L28)): "
        "an upper bound $x^{-1/2+\\varepsilon}$ for a weighted count of the primes that do not split in $\\mathbb Q(\\sqrt{-d})$ "
        "rules out zeros with real part above one half; only one side is needed because the weights are non-negative (Landau 1905).\n"
        f"2. **The bound from the main inequality** ([`star_inequality`]({blob}src/New/Main.lean#L121)), "
        "with about $\\sqrt x$ theta lifts: \"the saving $x^{-1/2}$ is $1/m$\".\n"
        "3. **The main inequality from one covolume bounded from both sides**, for a lattice of theta lifts between unitary "
        "groups over a CM field.\n"
        f"4. **Upper bound:** Theorem A, short forms, and Theorem B, enough forms ([`ShortAndEnough`]({blob}src/New/Endgame/ShortAndEnough.lean#L138)).\n"
        f"5. **Lower bound:** Theorem C, integral forms are long ([`integral_forms_long`]({blob}src/New/Endgame/LongForms.lean#L63)), "
        "by the product formula for heights, with one twist for each prime chosen through Galois representations and Selmer groups.\n")
    add("The main amount appears in both bounds and cancels. The note explains each step and lists what is quoted from the "
        "literature: class field theory, Galois representations of eigenforms, $p$-adic Hodge theory, Shimura varieties, the "
        "Siegel–Weil and Rallis formulas, a bound for odd Tate–Shafarevich groups after Mazur–Wiles and Greither, and more, "
        "all proved inside `Lib`, not assumed. The theorem of Ferrero and Washington, central to the submission's route, "
        "is cited in neither edition.\n")
    add("### What is checked, and what is not\n")
    add("- **Reported by the authors:** every file builds without `sorry`; `#print axioms` lists only `propext`, "
        "`Classical.choice`, `Quot.sound`; the exported proof is accepted by nanoda, con-leche and con-ron; Comparator "
        f"accepts the five theorems against [`Challenge.lean`]({blob}Challenge.lean).\n"
        "- **By the community:** CI builds every commit of the readable edition and fails on `sorry` or extra axioms; the "
        "runs that have finished have passed.\n"
        "- **By us:** the source scan above, the statements read, and an independent replay of the build on a cluster, under way.\n"
        "- **By nobody yet:** a mathematician's reading of the argument.\n")
    add("The rest of this page records the **submission of 20 November**: its checks, its route and the notes on parts "
        "of it. A complete write-up of the compact edition, every classical input quoted by reference, is in progress here.\n")

    # ------------------------------------------------------------------ the proof atlas
    add("> [!TIP]\n"
        f"> **The proof atlas: [nasqret.github.io/riemann-proof-atlas]({PROOF_ATLAS}).** The theorems and lemmas "
        "of the archive placed on a map of the arXiv literature by subject. Search a Lean name, follow a theorem "
        "from its mathematical neighbourhood to its Lean code and to the endpoints that depend on it, and read the "
        "chapters on three levels: statements, structured proofs and Lean, beside the notes. Built by the reading "
        "project; the paper map is Leland McInnes's map of arXiv.\n")
    add(f'<p align="center"><a href="{PROOF_ATLAS}"><img src="assets/screens/riemann-proof-atlas.jpg" width="94%" '
        'alt="The proof atlas: the declarations of the Lean archive as points on a map of arXiv papers coloured by '
        'subject, with the explorer panel beside it."></a></p>\n')

    # ------------------------------------------------------------------ dashboard
    add("## Status dashboard\n")
    add(f"Record of the reading project as of **{as_of}**, imported here on {imported}. "
        "[How this page stays current](#how-this-page-stays-current) · "
        "[Where to follow the sources](#where-to-follow-the-sources)\n")
    tiles = [(modules, "Lean modules in the archive", "57606a")]
    if n_rust:
        tiles.append((n_rust, "declarations accepted by the Rust kernel", "2ea44f"))
    if compare:
        tiles.append(("5 of 5", "statements match the Mathlib challenge", "2ea44f"))
    tiles += [("3", "axioms, all standard", "2ea44f"),
              (str(len(independent_people)), "independent accepting reports", "2ea44f"),
              (str(n_decl), f"declarations mapped in {len(comps)} components", "0969da")]
    add('<p align="center">' + " ".join(big(a, b, c) for a, b, c in tiles) + "</p>\n")

    def cite(s: dict | None) -> str:
        if not s:
            return ""
        return (f'{s["stage"]} ({who(s["operator"])}): **{s["outcome"]}**'
                + (f' ([source]({s["url"]}))' if s.get("url", "").startswith("http") else ""))

    def person(name: str) -> str:
        mine = [s for s in independent_ok if s["operator"] == name]
        more = f", and {len(mine) - 1} more" if len(mine) > 1 else ""
        return f'**{name}**: {mine[0]["stage"]} — {mine[0]["outcome"]}{more} ([source]({mine[0]["url"]}))'

    def listing(items) -> str:
        """Several records in one table cell, one per line."""
        items = list(items)
        return items[0] if len(items) == 1 else "<br>".join("• " + x for x in items)

    rows = []
    rows.append(["Do the formal statements really say RH and GRH?",
                 "✅ **Yes, as far as a machine can tell.** The first theorem has Mathlib's own type "
                 "`RiemannHypothesis`, and the five statements were compared with a challenge written independently "
                 "of the proof." if compare else "🔵 Read at the source; see the theorem below.",
                 listing(x for x in (cite(compare), cite(rebuilt), cite(first(stages, "Five theorems justified"))) if x)])
    rows.append(["Does a proof checker accept the complete proof?",
                 ("✅ **Yes, two independent ones.** " if two else "↗️ **Reported by an external builder.** ")
                 + "Lean's kernel checks every step; NanoDA is a second kernel, written independently in Rust.",
                 listing(x for x in (cite(rust), cite(combined)) if x)])
    rows.append(["Has anyone else reproduced that?",
                 f"✅ **Yes.** {len(independent_people)} parties outside the reading project report accepting runs "
                 "of their own, from their own builds." if independent_people else "⏳ Not recorded.",
                 listing(person(n) for n in independent_people)])
    rows.append(["Which axioms does the proof rest on?",
                 "✅ **Only the three standard axioms of Lean**: `propext`, `Classical.choice`, `Quot.sound`. No "
                 "additional assumption about primes or zeros is hidden anywhere.",
                 listing(x for x in (cite(axioms), cite(first(stages, "Five transitive axiom lists"))) if x)])
    rows.append(["Is the mathematics understood and refereed?",
                 "⏳ **Not yet.** A kernel certifies that the theorem follows from the axioms. It does not explain "
                 "why, and it is no substitute for mathematicians reading the argument. No human-readable proof "
                 "exists so far; this repository is one attempt to map the formal one.",
                 "[What a formal check does and does not establish](#what-a-formal-check-does-and-does-not-establish)"])
    own_checks = (f'✅ The logical skeleton of the argument compiles in Lean {audit["lean"].split("version ")[1].split(",")[0]} '
                  f'with no axioms ({len(audit["axiom_free"])} axiom-free declarations)')
    if zeta and zeta.get("build") == "passed":
        own_checks += ("; the last step (no zeros right of the line ⇒ Mathlib's `RiemannHypothesis`) is re-proved "
                       "independently against Mathlib")
    own_checks += "; the numbers in the figures are computed and asserted."
    rows.append(["What has this repository checked itself?", own_checks,
                 "[axiom report](verification/logs/axioms.json) · [Mathlib check](verification/logs/mathlib-zeta-axioms.json) · "
                 "[computed facts](assets/figures/facts.json) · [checks on every push](https://github.com/" + REPO + "/actions)"])
    add(table(["Question", "Answer", "Record"], rows) + "\n")

    add("### What a formal check does and does not establish\n")
    add("| A kernel check establishes | It does not establish |\n|---|---|\n"
        "| that every step from the axioms to the stated theorems is logically valid, with no gap | that the "
        "statements mean what we intend. This is why the five statements were compared with Mathlib's own "
        "definition and with a challenge written independently of the proof |\n"
        "| that the result does not depend on the machine or the person who ran it, when independent builders "
        "reproduce it | that the checkers are free of bugs. This is why two independently written kernels were "
        "used |\n"
        "| that no extra assumption is used, when the axiom report lists only the standard three | *why* the "
        "theorem is true, or that mathematicians understand the argument. That takes people, and time |\n")

    # ------------------------------------------------------------------ updates
    add("### How this page stays current\n")
    add("The status above is not typed by hand. It is generated from a status record kept by a separate reading "
        "project, in which the announcement and the archive are read and the verification runs are carried out "
        "and collected. Each time that record is imported, the model, the figures, the guide and this page are "
        "rebuilt (`make data && make all`), and one line is added to the log below "
        "([`data/sync-log.json`](data/sync-log.json), [`data/source/PROVENANCE.json`](data/source/PROVENANCE.json)). "
        "The reading project itself is a private working copy; its public evidence is linked in the next table. "
        f"The [site]({SITE}/) is rebuilt from this repository on every push, the book with all its computations "
        "executed again.\n")
    add(table(["Imported (UTC)", "Record as of (UTC)", "Headline of the record"],
              [[utc(e["imported_utc"]), utc(e["status_as_of"]), e["headline"]] for e in reversed(sync)]) + "\n")

    add("### Where to follow the sources\n")
    follow = [[link(s["label"], s["url"]), urllib.parse.urlparse(s["url"]).netloc] for s in st["external_sources"]]
    follow += [["The Lean archive itself, in 14 parts (footnote 1 of the announcement)", f"[alpo.ge]({ARCHIVE_URL})"],
               [f"Public mirror of the archive, at the pinned commit `{pins['mirror_commit'][:8]}`", f"[github.com]({mirror_tree})"],
               ["Mathlib at the commit the archive uses",
                f"[github.com](https://github.com/leanprover-community/mathlib4/tree/{pins['mathlib']})"]]
    add(table(["Source", "Where"], follow) + "\n")
    if st.get("private_sources"):
        add(f"*Not public:* {'; '.join(st['private_sources']).lower()} (kept by the reading project).\n")

    add("### Every recorded check of the complete proof\n")
    add(f"<details>\n<summary><b>All {len(stages)} checks in the record</b>: {len(own)} by the reading project, "
        f"{len(others)} by others (click to open)</summary>\n")
    add(table(["Check", "Operator", "Outcome", "Detail", ""],
              [[s["stage"], who(s["operator"]), f'**{s["outcome"]}**', s.get("detail", ""),
                f'[source]({s["url"]})' if s.get("url", "").startswith("http") else "receipt in the reading project"]
               for s in stages]) + "\n")
    add("</details>\n")
    add("<details>\n<summary><b>What the reading project checked declaration by declaration</b></summary>\n")
    add(st["native"] + "\n")
    add("</details>\n")

    # ------------------------------------------------------------------ theorem
    add("## The theorem\n")
    add("Throughout, $s$ is a complex number and $\\operatorname{Re}s$ its real part. The Riemann zeta function and "
        "the $L$-function of a Dirichlet character $\\chi$ modulo $N$ (a function "
        "$\\chi\\colon\\mathbb Z\\to\\mathbb C$ with $\\chi(mn)=\\chi(m)\\chi(n)$, $\\chi(n+N)=\\chi(n)$, and "
        "$\\chi(n)\\ne0$ exactly when $n$ is coprime to $N$) are defined for $\\operatorname{Re}s>1$ by\n")
    add("```math\n\\zeta(s)=\\sum_{n=1}^{\\infty}\\frac1{n^{s}}=\\prod_{p\\ \\mathrm{prime}}\\frac1{1-p^{-s}},\\qquad\\qquad "
        "L(s,\\chi)=\\sum_{n=1}^{\\infty}\\frac{\\chi(n)}{n^{s}}=\\prod_{p\\ \\mathrm{prime}}\\frac1{1-\\chi(p)\\,p^{-s}},\n```\n")
    add("and extend to analytic functions of all complex $s$, except for a simple pole at $s=1$ when $\\chi$ is "
        "principal (in particular for $\\zeta$, which is the case $N=1$).\n")
    add("> **Theorem** (announced by L. Alpöge; the formal statements are those of the Lean archive). "
        "Let $N\\ge1$ be an integer and let $\\chi$ be **any** Dirichlet character modulo $N$. Then the following hold.\n")
    add("```math\n\\begin{aligned}"
        "&\\textbf{(1)}\\quad L(s,\\chi)\\neq0\\quad\\text{for every }s\\in\\mathbb C\\text{ with }\\operatorname{Re}s>\\tfrac12"
        "\\qquad(\\text{and }s\\neq1\\text{ if }\\chi\\text{ is principal});\\\\[6pt]"
        "&\\textbf{(2)}\\quad L(s,\\chi)=0\\ \\text{ and }\\ 0<\\operatorname{Re}s<1\\quad\\Longrightarrow\\quad\\operatorname{Re}s=\\tfrac12;\\\\[6pt]"
        "&\\textbf{(3)}\\quad \\zeta(s)=0,\\ \\ s\\notin\\{-2,-4,-6,\\dots\\},\\ \\ s\\neq1\\quad\\Longrightarrow\\quad\\operatorname{Re}s=\\tfrac12 ."
        "\\end{aligned}\n```\n")
    add("**(1)** says that there are no zeros to the right of the critical line (the pole of a principal character "
        "at $s=1$ is not a zero and is set aside). **(2)** says that the zeros in the critical strip lie on the "
        "critical line. **(3)** is the Riemann hypothesis itself, the case $N=1$: every zero of $\\zeta$ other than "
        "the trivial zeros $-2,-4,-6,\\dots$ has real part $\\tfrac12$.\n")
    add("Statements (1) and (2), for all $N$ and $\\chi$, are the generalized Riemann hypothesis for Dirichlet "
        "$L$-functions. For the primes, the Riemann hypothesis is equivalent to the sharpest possible form of the "
        "prime number theorem: with $\\pi(x)$ the number of primes up to $x$ and "
        "$\\operatorname{li}(x)=\\int_0^x dt/\\log t$ (Schoenfeld, 1976),\n")
    add("```math\n\\bigl\\lvert\\pi(x)-\\operatorname{li}(x)\\bigr\\rvert\\ <\\ \\frac1{8\\pi}\\,\\sqrt x\\,\\log x\\qquad\\text{for all }x\\ge2657 .\n```\n")
    add("**The five formal statements.** The archive exports exactly five theorems; all five follow from "
        "statement (1). Each name links to its line in the public mirror of the archive.\n")
    endpoint_rows = []
    words = {"main-rh": "the Riemann hypothesis, in Mathlib's own formulation",
             "main-zeta": "statement (3), with the quantifiers written out",
             "main-right": "statement (1), for every modulus and every character",
             "main-strip": "statement (2), for every modulus and every character",
             "main-prim": "statement (2) for primitive characters"}
    mathlib_rh = next((l["url"] for l in comps["endpoints"]["lean"] if "Mathlib RiemannHypothesis" in l["name"]), None)
    for nid in ("main-rh", "main-zeta", "main-right", "main-strip", "main-prim"):
        n = nodes[nid]
        typ = n["excerpt"].split(":", 1)[1].split(":=")[0].strip()
        stmt = next((x for x in model["nodes"] if x.get("declaration") == typ), None)
        typ_link = f"[`{typ}`]({stmt['url']})" if stmt else (f"[`{typ}`]({mathlib_rh}) (Mathlib)" if mathlib_rh else f"`{typ}`")
        endpoint_rows.append([f"[`{n['declaration']}`]({n['url']})<br>of type {typ_link}", words[nid], tier_text(n["tier"])])
    add(table(["Lean theorem and its type", "In words", "Status"], endpoint_rows) + "\n")
    add("<details>\n<summary><b>The formal definitions, quoted from the archive</b></summary>\n")
    for nid in ("stmt-zeta", "stmt-right", "stmt-strip", "stmt-prim"):
        n = nodes[nid]
        add(f"[`{n['declaration']}`]({n['url']})\n\n```lean\n{n['excerpt']}\n```\n")
    add("`RiemannHypothesis` is defined in Mathlib; the archive proves a term of that type. In Lean, "
        "`DirichletCharacter.LFunction χ s` is the analytically continued $L(s,\\chi)$ and `riemannZeta s` is $\\zeta(s)$.\n")
    add("</details>\n")
    add("<details>\n<summary><b>Fine print: what is and is not claimed</b></summary>\n")
    add("- The modulus $N$ is any positive integer and $\\chi$ any character modulo $N$, primitive or not. An "
        "imprimitive character has additional zeros on the line $\\operatorname{Re}s=0$, coming from finitely many "
        "Euler factors; they lie outside the open strip of statement (2) and to the left of the half-plane of "
        "statement (1).\n"
        "- The statements concern Dirichlet $L$-functions only. The announcement expects an extension to further "
        "$L$-functions; the archive contains no theorem about them.\n"
        "- The announcement is a claim by its author. The formal statements above are what the proof checkers "
        "have accepted; see the dashboard for by whom, when and with which caveats.\n")
    add("</details>\n")

    # ------------------------------------------------------------------ primer
    add("## New here? Start here\n")
    add('<img src="assets/figures/strip.svg" align="right" width="46%" alt="The critical strip: the first zeros of the '
        'zeta function, computed, on the line Re s = 1/2; a hypothetical zero off the line and its mirror image.">\n')
    add("**Primes and the zeta function.** The primes $2,3,5,7,11,\\dots$ thin out in a regular way: near a large "
        "number $x$ about one number in $\\log x$ is prime. In 1859 Riemann showed that the fine structure of this "
        "pattern is governed by a single function, $\\zeta(s)$, and more precisely by the complex numbers $s$ "
        "where it vanishes, its *zeros*.\n")
    add("**The hypothesis.** Apart from the trivial zeros $-2,-4,-6,\\dots$, all zeros of $\\zeta$ lie in the strip "
        "$0<\\operatorname{Re}s<1$. The Riemann hypothesis (RH) says that they all lie exactly in the middle of "
        "it, on the *critical line* $\\operatorname{Re}s=\\tfrac12$. Enormous numbers of zeros have been computed, all "
        "on the line; the figure shows the first ten. A proof must exclude every zero off the line, for ever.\n")
    add("**Why it matters.** RH is equivalent to the statement that the primes are distributed as regularly as "
        "they possibly can be: the error in the prime number theorem is of the order of $\\sqrt x$, no larger. "
        "Hundreds of theorems in number theory have been proved *assuming* RH or its generalization.\n")
    add("**The generalization.** A Dirichlet character $\\chi$ picks out the primes in an arithmetic progression, "
        "such as those ending in the digit 7. Each has its own function $L(s,\\chi)$, and the generalized Riemann "
        "hypothesis (GRH) says the same about its zeros. The announced theorem covers all of them.\n")
    add("**What a formal proof is.** In a proof assistant such as Lean, definitions, statements and proofs are "
        "written in a formal language, and a small program, the *kernel*, checks every single inference. "
        "Mathlib is the large community library in which, among much else, the Riemann hypothesis is formally "
        "*stated*. A formal proof can be far too long for a person to read, as here, and still be checked "
        "completely. What that buys, and what it does not, is set out "
        "[above](#what-a-formal-check-does-and-does-not-establish).\n")
    add("**The idea of this proof, in four sentences.** A certain weighted count of primes, $G(y)$, is as small as "
        "$\\sqrt y$ exactly when RH holds. Remarkably, it is enough to bound it *from above*, and only on some "
        "long intervals ([step 3](#step-3-a-localized-landau-theorem)). Such an upper bound comes from arithmetic "
        "geometry: numbers that are divisible by many primes cannot be small "
        "([step 4](#step-4-the-estimate-i-a-slope-inequality-for-a-chain-of-theta-lifts)). The rest of the "
        "argument makes this precise for every Dirichlet character at once and pays for the technical losses "
        "(steps [5](#step-5-the-estimate-ii-from-the-slope-inequality-to-the-bound), "
        "[6](#step-6-the-price-of-divisibility-iwasawa-theory) and [7](#step-7-the-automorphic-foundation)).\n")
    add('<br clear="right">\n')

    # ------------------------------------------------------------------ route
    add("## The route of the proof\n")
    add("The diagram shows the flow of the argument from its arithmetic input to the theorem; the numbers refer "
        "to the steps below, which are numbered as in the [guide](guide/proof-guide.pdf) and read the proof "
        "backwards, from the theorem to its input. The two dashed arrows are the places where the proof has also "
        "been machine-checked in isolation, as an implication from explicitly stated premises.\n")
    colour = {s["id"]: s["color"] for s in model["strata"]}
    add("```mermaid\n%%{init: {\"flowchart\": {\"wrappingWidth\": 460}}}%%\nflowchart TB\n"
        '  S7["<b>7 · Automorphic foundation</b><br/>Galois representations of automorphic forms"]\n'
        '  S6["<b>6 · Iwasawa theory</b><br/>cohomology bounded on a whole window"]\n'
        '  S4["<b>4 · Chain of theta lifts</b><br/>divisibility against size: a slope inequality"]\n'
        '  S5H["<b>5 · Hosts</b><br/>number fields rebuilt at every scale"]\n'
        '  S5["<b>5 · Character averaging</b><br/>positive weights, unwanted twists removed"]\n'
        '  S3["<b>2 · 3 · Localized Landau theorem</b><br/>an upper bound on windows excludes zeros"]\n'
        '  S1["<b>1 · Reflection</b><br/>functional equation"]\n'
        '  T(["<b>RH and GRH for Dirichlet L-functions</b>"])\n'
        '  S7 -- "periods" --> S4\n'
        '  S7 -- "base change" --> S6\n'
        '  S6 -- "loss of divisibility" --> S4\n'
        '  S6 -- "window bound" --> S5H\n'
        '  S5H -- "hosts" --> S5\n'
        '  S4 -. "checked cut: TopG" .-> S5\n'
        '  S5 -. "checked cut, two kernels: the bound (★)" .-> S3\n'
        '  S3 -- "no zeros right of the line" --> S1\n'
        "  S1 --> T\n"
        f"  classDef arith fill:#fff7ed,stroke:{colour['arith']},stroke-width:2px,color:#431407;\n"
        f"  classDef est fill:#f5f3ff,stroke:{colour['est']},stroke-width:2px,color:#2e1065;\n"
        f"  classDef ana fill:#ecfeff,stroke:{colour['ana']},stroke-width:2px,color:#083344;\n"
        f"  classDef dest fill:#fff1f2,stroke:{colour['dest']},stroke-width:2px,color:#4c0519;\n"
        "  class S7,S6 arith;\n  class S4,S5H,S5 est;\n  class S3 ana;\n  class S1,T dest;\n```\n")
    add("<sub>Colours: " + " · ".join(f'{c} {strata[k]["title"].lower()}' for k, c in
                                      (("arith", "🟧"), ("est", "🟪"), ("ana", "🟦"), ("dest", "🟥"))) + "</sub>\n")
    add("**All seven steps are part of the complete proof that the kernels accepted.** The last column says what "
        "has, in addition, been examined step by step: checked in isolation by the reading project, or read at "
        "the source. The links in the fourth column lead to the actual formal proofs, in the public mirror of the "
        "archive at a fixed commit.\n" if two else
        "The last column says how each step has been examined so far. The links in the fourth column lead to the "
        "actual formal proofs, in the public mirror of the archive at a fixed commit.\n")
    route_rows = []
    for s in STEPS:
        tl = list(dict.fromkeys(comps[c]["tier"] for c in s["comps"]))
        route_rows.append([f'[**{s["n"]}**](#{s["slug"]})', f'[{s["title"]}](#{s["slug"]})', s["one"],
                           lean_links(s["lean"]), "<br>".join(tier_text(t) for t in tl)])
    add(table(["", "Step", "In one sentence", "Where it is proved in Lean", "Examined step by step"], route_rows) + "\n")
    add("<details>\n<summary><b>What the labels mean</b></summary>\n")
    add(table(["Label", "Meaning"], [[tier_text(t), tiers[t]["meaning"]] for t in
                                    ("two-kernels", "checked", "partial", "covered", "read", "reported", "motivation")]) + "\n")
    add("</details>\n")

    for s in STEPS:
        add(f'### Step {s["n"]}: {s["title"]}\n')
        add(s["text"] + "\n")
        add("```math\n" + s["math"] + "\n```\n")
        add("**Notation.** " + s["where"] + "\n")
        names = " · ".join(f'{comps[c]["n"]}. {comps[c]["title"]} ({tier_text(comps[c]["tier"])})' for c in s["comps"])
        add(f'**Proved in Lean at:** {lean_links(s["lean"])}  \n'
            f'**Components of the map:** {names}  \n'
            f'**Explained in:** [guide](guide/proof-guide.pdf), §{s["n"]}'
            + (" and the opening pages" if s["n"] == 1 else "") + "\n")

    add("### The two implications checked in isolation\n")
    add("Independently of the complete proof, two implications were checked on their own, with their premises "
        "stated explicitly. They show how much of the argument is elementary analysis: everything to the right of "
        "the dashed arrows in the diagram.\n")
    cut_rows = []
    for c in model["cuts"]:
        cut_rows.append([f'**{c["title"]}**', f'${c["premise"]}$', c["conclusion"], f'`{c["lean"].split(".")[-1]}` in [`{c["source"]}`]({c["source"]})',
                         f'{tier_text(c["tier"])}<br><sub>{c["evidence"]}</sub>'])
    add(table(["Implication", "Premise", "Conclusion", "Lean theorem", "Check"], cut_rows) + "\n")

    add("### The fourteen components\n" if len(comps) == 14 else "### The components\n")
    add(f"<details>\n<summary><b>All {len(comps)} components of the map, with their main declarations</b></summary>\n")
    comp_rows = []
    for c in model["components"]:
        ll = [l for l in c["lean"] if l["url"].startswith(pins["mirror"])][:3]
        comp_rows.append([str(c["n"]), f'**{c["title"]}**', strata[c["stratum"]]["title"], c["gist"],
                          " · ".join(f'[`{l["name"].split(".")[-1]}`]({l["url"]})' for l in ll), tier_text(c["tier"])])
    add(table(["#", "Component", "Stratum", "What it does", "Main declarations", "Examined"], comp_rows) + "\n")
    add("</details>\n")

    # ------------------------------------------------------------------ contents
    n_digest = len(load("digests/tower-bound/concordance.json")["declarations"])
    n_second = len(load("digests/local-nilpotence/concordance.json")["declarations"])
    n_third = len(load("digests/layer-descent/concordance.json")["declarations"])
    add("## What is in this repository\n")
    add(table(["", "What", "Where"], [
        ["📄", "**The guide.** The whole argument in standard mathematical terminology: flow diagram, the theorem, the "
               "seven steps, and why each idea calls for the next. Every symbol is defined, and there is a page of notation.",
         f"[**read online**]({SITE}/guide/proof-guide.pdf) · [`guide/proof-guide.pdf`](guide/proof-guide.pdf) · "
         "[animated preview](guide/proof-guide.gif)"],
        ["🔬", f"**Deformalization 1: twisted cokernels in a cyclotomic tower.** One cluster of the archive rewritten as "
               f"ordinary mathematics: the statements in standard terms, complete proofs of the algebra, a concordance of "
               f"{n_digest} Lean declarations with their source lines, and computed examples.",
         f"[**read online**]({SITE}/digests/tower-bound.pdf) · "
         "[`digests/tower-bound/tower-bound.pdf`](digests/tower-bound/tower-bound.pdf)"],
        ["🔬", f"**Deformalization 2: local nilpotence over a cyclotomic tower.** An input of the first note proved in "
               f"full: every character of the cyclotomic kernel is killed by a power of γ − 1. Written from structured "
               f"proofs of the Lean text, with a concordance of {n_second} Lean declarations.",
         f"[**read online**]({SITE}/digests/local-nilpotence.pdf) · "
         "[`digests/local-nilpotence/local-nilpotence.pdf`](digests/local-nilpotence/local-nilpotence.pdf)"],
        ["🔬", f"**Deformalization 3: descent to a layer of the cyclotomic tower.** The two inputs of the first note on "
               f"the invariants under a generator and on the classes over a layer, from one whole unit of the archive; "
               f"the cohomological inputs are stated and taken from other units. A concordance of {n_third} Lean "
               f"declarations.",
         f"[**read online**]({SITE}/digests/layer-descent.pdf) · "
         "[`digests/layer-descent/layer-descent.pdf`](digests/layer-descent/layer-descent.pdf)"],
        ["🗺️", f"**The atlas.** An interactive map: the {len(comps)} components, a guided tour, the blueprint graph of "
               f"{n_decl} declarations with their dependencies, illustrated ideas and the verification ledger. One "
               "self-contained HTML file.",
         f"[**open the atlas**]({SITE}/atlas/) · [`atlas/index.html`](atlas/index.html)"],
        ["📘", "**The illustrated blueprint.** The same map as a PDF, with every declaration linked to its source line.",
         f"[**read online**]({SITE}/blueprint/atlas-blueprint.pdf) · "
         "[`blueprint/atlas-blueprint.pdf`](blueprint/atlas-blueprint.pdf)"],
        ["📓", "**The book.** Chapters with formulas, figures and computations that are executed at every build.",
         f"[**read the book**]({SITE}/book/) · sources in [`book/`](book/)"],
        ["🧩", "**A Lean skeleton of the argument.** Every component as an explicit hypothesis, and the proof that they "
               "compose; no imports, no axioms.",
         "[`lean/Atlas/Architecture.lean`](lean/Atlas/Architecture.lean)"],
        ["🔁", "**The last step against Mathlib.** No zeros right of the line implies Mathlib's `RiemannHypothesis`, "
               "re-proved here.",
         "[`lean-mathlib/AtlasZeta.lean`](lean-mathlib/AtlasZeta.lean)"],
        ["📊", "**The data.** The component model, the imported status record with its provenance, the log of syncs.",
         "[`data/`](data/)"],
        ["🧪", "**The logs.** Build logs and axiom reports of this repository's own checks.",
         "[`verification/`](verification/)"],
        ["⚙️", "**The scripts.** Everything above is generated; nothing on this page is typed by hand except the prose.",
         "[`scripts/`](scripts/) · [`Makefile`](Makefile)"],
    ]) + "\n")
    add("<details>\n<summary><b>Leaf through the guide</b> (animated, one page every five seconds)</summary>\n")
    add('<p align="center"><img src="guide/proof-guide.gif" width="72%" alt="The pages of the guide"></p>\n')
    add("</details>\n")

    # ------------------------------------------------------------------ check yourself
    add("## Check it yourself\n")
    add("**This repository** (a few minutes; Python with NumPy and Pillow, Poppler, and Lean through `elan`):\n")
    add("```sh\nmake check        # self-test of the numerics, provenance of the imported data, consistency of every page\n"
        "make lean         # build the Lean skeleton and write its axiom report\n"
        "make all          # regenerate the model, figures, atlas, PDFs, book and this page\n```\n")
    add("What each command needs, and what it should print, is in [`BUILDING.md`](BUILDING.md).\n")
    add("**The archive** (hours of computing, tens of gigabytes). The published verification material is linked "
        "[above](#where-to-follow-the-sources). To be sure you are checking the same objects, compare these "
        "fingerprints, which are part of the record:\n")
    rfe = load("data/source/status.json").get("reported_full_export", {})
    pin_rows = [["Lean archive (14 parts, concatenated)", f"`{pins['archive_sha256']}`", f"{modules} modules, {src['unpacked_bytes']:,} bytes unpacked"],
                ["Announcement (PDF)", f"`{pins['pdf_sha256']}`", "four pages"],
                ["Lean toolchain of the archive", f"`{pins['toolchain']}`", ""],
                ["Mathlib commit of the archive", f"`{pins['mathlib']}`", ""],
                ["Mirror commit used for all links here", f"`{pins['mirror_commit']}`", link("mirror", mirror_tree)]]
    if rfe.get("raw_sha256"):
        pin_rows.append(["Exported complete proof (the file the Rust kernel reads)", f"`{rfe['raw_sha256']}`",
                         f"{rfe['raw_bytes']:,} bytes" + (f", built by {rfe['builder']}" if rfe.get("builder") else "")])
    pin_rows.append(["Portable proof of the first checked implication", f"`{st['independent_window']['solution_sha256']}`",
                     f"{window_decls} declarations"])
    add(table(["Object", "SHA-256 or version", "Size"], pin_rows) + "\n")

    # ------------------------------------------------------------------ transparency
    add("## Transparency\n")
    add("**Where the statements on this page come from.**\n")
    add(f"- *Status and verification records*: imported from the reading project's status record "
        f"(as of {as_of}; imported {imported}; {len(prov['files'])} files with SHA-256 in "
        "[`PROVENANCE.json`](data/source/PROVENANCE.json)). "
        + (f"{sum(f.get('redactions', 0) for f in prov['files'])} link into a private place was replaced by a neutral "
           "token on import; nothing else was altered." if sum(f.get("redactions", 0) for f in prov["files"]) == 1 else
           f"{sum(f.get('redactions', 0) for f in prov['files'])} links into private places were replaced by neutral "
           "tokens on import; nothing else was altered."))
    add(f"- *Statements about the Lean archive*: read at the source lines that are linked ({n_pinned} pinned links). "
        "The guide lists, section by section, which declarations it relies on.\n"
        "- *Quotations of the announcement*: from its four pages, by entry number.\n"
        "- *Numbers in the figures*: computed by [`scripts/rhlib.py`](scripts/rhlib.py) and stored, with assertions, in "
        "[`assets/figures/facts.json`](assets/figures/facts.json). For instance the first zero of $\\zeta$ is "
        f"computed as ${facts['zeros']['first']:.6f}$, and $\\lvert G(y)-\\log2\\pi\\rvert/\\sqrt y$ stays below "
        f"${max(abs(facts['hero']['r_min']), abs(facts['hero']['r_max'])):.3f}$ for $10\\le y\\le10^{{7}}$, inside the "
        f"band $2+\\gamma-\\log4\\pi={facts['hero']['rh_band']:.4f}$ that RH predicts.\n")
    add("**What this repository does not do.**\n")
    add("- It does not re-run the complete proof. It reports the runs of others and of the reading project, with "
        "links where they are public; the receipts of the reading project's own runs are not public.\n"
        "- It is not a referee report. Reading a declaration at its source line is not the same as verifying the "
        "mathematics behind it.\n"
        "- The guide has been audited symbol by symbol against the Lean source. The atlas, the blueprint PDF and "
        "the book have not yet had the same audit and use an older, less concrete description of step 4.\n"
        "- The map covers the architecture: a selection of declarations out of an archive of "
        f"{modules} modules.\n")
    add("**How it was made.** The texts, figures and scripts were produced with an AI assistant (Claude) working "
        "under the direction of the repository owner; the reading project that supplies the records is likewise "
        "AI-assisted. Every statement about the archive was checked against the Lean source or the records listed "
        "above before it was written, and the build refuses to produce pages whose numbers or links do not match "
        "the data. Mistakes are nevertheless possible.\n")
    add(f"**Corrections.** If something here is wrong, unclear or out of date, please "
        f"[open an issue](https://github.com/{REPO}/issues). Corrections are recorded in the commit history.\n")

    # ------------------------------------------------------------------ glossary and FAQ
    add("## Glossary\n")
    add("<details>\n<summary><b>Fifteen terms used on this page</b></summary>\n" if len(GLOSSARY) == 15 else
        "<details>\n<summary><b>Terms used on this page</b></summary>\n")
    add(table(["Term", "Meaning"], [[f"**{a}**", b] for a, b in GLOSSARY]) + "\n")
    add("</details>\n")

    add("## Questions and answers\n")
    qa = [
        ("Is the Riemann hypothesis proved?",
         "A formal proof of the statement has been published and, according to the records collected here, accepted "
         "by two independent proof checkers and reproduced by several independent parties. That is strong evidence "
         "of a kind that did not exist for any previous claim. It is not yet the end of the story: the mathematical "
         "community has not read, understood and refereed the argument, and the author himself writes that a proper "
         "account remains to be written. This page reports; it does not pronounce."),
        ("What could still be wrong?",
         "Three things, in decreasing order of concern. The formal statements could fail to say what is meant: this "
         "has been addressed by comparing them with Mathlib's definition and with an independently written "
         "challenge. The checkers could have a bug: this is why two independently written kernels were used. And "
         "the logical foundations (Lean's type theory with its three standard axioms) could be inconsistent, which "
         "would affect all of formalized mathematics."),
        ("Why is there no proof one can read?",
         f"The proof was found and written as a formal object of {modules} files. In the announcement the author "
         "says that he chose to present only the Lean proof and intends to write the argument properly. The guide "
         "and the atlas in this repository are an attempt to make its architecture readable; they are not a "
         "substitute for that account."),
        ("What was the role of AI?",
         "The announcement says the proof was discovered by its author \"working with Claude\", and that the "
         "formalization was done together. This repository takes no position on who contributed what; it maps what "
         "was published. This repository itself was prepared with AI assistance, as stated above."),
        ("How current is this page?",
         f"The status record is as of {as_of} and was imported on {imported}. The log of imports is "
         "[above](#how-this-page-stays-current); the primary sources, which may be more recent, are linked "
         "[there](#where-to-follow-the-sources) too."),
        ("How can I check a claim made here?",
         "Every status has a source in the tables above, every Lean name links to its line in the public mirror, "
         "and every computed number can be regenerated with `make all`. For the proof itself, follow the published "
         "verification material and compare the fingerprints listed under [Check it yourself](#check-it-yourself)."),
    ]
    for q, a in qa:
        add(f"<details>\n<summary><b>{q}</b></summary>\n\n{a}\n\n</details>\n")

    # ------------------------------------------------------------------ credits
    people: list[str] = []               # the persons named as operators, each once ("A and B" is two persons)
    for stage in others:
        for name in stage["operator"].split(" and "):
            if not any(known.endswith(name) for known in people):
                people.append(name)
    add("## Credits and licence\n")
    add("- **The announcement and the Lean archive**: Levent Alpöge, with Claude (20 November 2026). The archive is "
        f"distributed by its author in 14 parts; all source links here go to the public mirror "
        f"[{pins['mirror'].split('github.com/')[-1]}]({mirror_tree}).\n"
        "- **Verification reports**: " + ", ".join(people) + ", and the reading project; "
        "each is cited with its source in the table of checks.\n"
        "- **Mathlib and Lean**: the Lean community and the Lean FRO.\n"
        "- **Licence**: [0BSD](LICENSE). Everything original here (texts, figures, scripts, Lean files) may be used "
        "for any purpose, without conditions. Quoted Lean code and quotations of the announcement belong to their "
        "authors.\n")
    add(f"<sub>Generated by <a href=\"scripts/build_readme.py\"><code>scripts/build_readme.py</code></a> from the record of "
        f"{as_of}. Do not edit this file by hand.</sub>\n")
    return "\n".join(L)


BLACKBOARD = {"C": "ℂ", "N": "ℕ", "Q": "ℚ", "R": "ℝ", "Z": "ℤ"}


def mathsafe(text: str) -> str:
    """Adapt the mathematics to GitHub's renderer, which turns TeX into MathML and lets the browser
    draw it: < and > as \\lt and \\gt (some are otherwise escaped twice); no \\operatorname, which
    GitHub refuses ("macro not allowed"); and an explicit thin space after a function name such as
    \\log when a letter, digit or symbol follows, because browsers put no space there; the letters
    of \\mathbb as Unicode characters (browsers ignore the variant of a plain letter); and a strut
    under a radical over a single letter, which is otherwise drawn too small."""
    def fix(m):
        seg = m.group(0).replace("<", "\\lt ").replace(">", "\\gt ")
        seg = re.sub(r"\\operatorname\{([A-Za-z]+)\}(?=[A-Za-z])", r"\\mathrm{\1}\\,", seg)
        seg = re.sub(r"\\operatorname\{([A-Za-z]+)\}", r"\\mathrm{\1}", seg)
        seg = re.sub(r"\\mathbb\s*(?:\{([A-Z])\}|([A-Z]))",
                     lambda b: " " + BLACKBOARD[b.group(1) or b.group(2)], seg)
        seg = re.sub(r"\\sqrt\s*(?:\{([a-z])\}|([a-z])(?![A-Za-z]))",
                     lambda r: "\\sqrt{\\mathstrut " + (r.group(1) or r.group(2)) + "}", seg)
        return re.sub(r"\\(log|exp|max|min)(?![A-Za-z])\s*(?=[A-Za-z0-9]|\\(?!bigl|Bigl|left|lvert|,|;|!)[A-Za-z])",
                      r"\\\1\\,", seg)
    text = re.sub(r"```math\n.*?\n```", fix, text, flags=re.S)
    inline = lambda m: "$`" + fix(m)[1:-1] + "`$"
    return re.sub(r"(?<![\\$`\w])\$(?![\s$`])[^$\n`]*?(?<![\s\\])\$(?![\w$])", inline, text)


def problems(text: str) -> list[str]:
    out = []
    refused = sorted(set(re.findall(r"\\(?:operatorname|href|require|newcommand|def|unicode|class|style)\b", text)))
    if refused:
        out.append("TeX macros that GitHub refuses: " + ", ".join(refused))
    formulas = re.findall(r"```math\n(.*?)\n```", text, flags=re.S) + re.findall(r"\$`([^`]*)`\$", text)
    for f in formulas:
        if f.count("{") - f.count("\\{") != f.count("}") - f.count("\\}"):
            out.append("unbalanced braces in the formula " + f[:60])
    if re.search(r"private:" + "//", text):
        out.append("a link into a private place")
    for target in sorted(set(re.findall(r"\]\((?!https?://|#)([^)\s]+)\)", text) + re.findall(r'(?:src|href)="(?!https?://|#)([^"]+)"', text))):
        if not (ROOT / target.split("#")[0]).exists():
            out.append(f"relative link to a missing file: {target}")
    anchors = {re.sub(r"[^a-z0-9 -]", "", h.lower()).strip().replace(" ", "-") for h in re.findall(r"(?m)^#{1,4} (.+)$", text)}
    for a in sorted(set(re.findall(r"\]\(#([^)]+)\)", text) + re.findall(r'href="#([^"]+)"', text))):
        if a not in anchors:
            out.append(f"link to a missing section: #{a}")
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    text = mathsafe(build())
    bad = problems(text)
    if bad:
        print("readme: " + "; ".join(bad))
        return 1
    target = ROOT / "README.md"
    if a.check:
        ok = target.exists() and target.read_text(encoding="utf-8") == text
        print("readme: up to date" if ok else "readme: README.md is not what the data give; run `make readme`")
        return 0 if ok else 1
    target.write_text(text, encoding="utf-8")
    print(f"readme: README.md, {len(text.splitlines())} lines, {len(text) // 1024} KiB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
