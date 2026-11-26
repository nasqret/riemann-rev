#!/usr/bin/env python3
"""Measure the condensed editions of the proof: data/condensed.json, read by scripts/build_readme.py.

    python3 -B scripts/measure_condensed.py PATH     # PATH: a checkout of github.com/lsernau/grh-lean at the pinned commit

The repository lsernau/grh-lean (one commit, frozen) holds two Lake projects with the same five theorems: `grh/`, the
readable edition, and `grh-compact/`, the compact edition. For each, and for its parts `src/Lib` (background) and
`src/New` (the argument), this counts Lean files, physical lines, lines of code (comments, docstrings and blank lines
removed), and theorem and definition commands. It also scans the code for constructs that add axioms or bypass the
kernel and records how many it found (expected: none). The submission's size comes from data/census.json.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO = "lsernau/grh-lean"
COMMIT = "72fead102f663d5c7a407964a13dc0cf9d977207"
RISKY = r"\bsorry\b|(?<![\w.])admit\b|^\s*(?:private |protected )?axiom\s|^\s*(?:private |protected |noncomputable )*opaque\s|" \
        r"implemented_by|@\[\s*extern|\bunsafe\b|native_decide|ofReduce(?:Bool|Nat)|^\s*(?:run_cmd|run_elab|run_meta|#eval)\b|" \
        r"^\s*(?:@\[[^\]]*\]\s*)?(?:local |scoped )?(?:elab|macro|syntax|macro_rules|elab_rules)\b"


def count(files: list[Path]) -> dict:
    out = {"files": len(files), "lines": 0, "code_lines": 0, "theorems": 0, "definitions": 0, "risky": 0}
    for f in files:
        t = f.read_text(encoding="utf-8")
        out["lines"] += t.count("\n")
        code = re.sub(r"--.*", "", re.sub(r"/-.*?-/", "", t, flags=re.S))
        out["code_lines"] += sum(1 for ln in code.split("\n") if ln.strip())
        out["theorems"] += len(re.findall(r"^(?:@\[[^\]]*\]\s*)?(?:private |protected )*(?:theorem|lemma)\s", code, re.M))
        out["definitions"] += len(re.findall(r"^(?:@\[[^\]]*\]\s*)?(?:private |protected |noncomputable )*"
                                             r"(?:def|abbrev|structure|class|inductive|instance)\b", code, re.M))
        out["risky"] += len(re.findall(RISKY, code, re.M))
    return out


def main() -> int:
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    path = Path(sys.argv[1]).resolve()
    head = subprocess.run(["git", "-C", str(path), "rev-parse", "HEAD"], capture_output=True, text=True, check=True).stdout.strip()
    if head != COMMIT:
        sys.exit(f"measure: {path} is at {head}, not at the pinned commit {COMMIT}")
    census = json.loads((ROOT / "data/census.json").read_text(encoding="utf-8"))
    out = {"repo": REPO, "commit": COMMIT, "date_utc": "2026-11-25T20:38:07Z",
           "submission": {"files": census["totals"]["modules"], "lines": census["totals"]["lines"]},
           "editions": {}}
    for ed in ("grh", "grh-compact"):
        src = path / ed / "src"
        rec = {"all": count(sorted(src.rglob("*.lean")))}
        for part in ("Lib", "New"):
            rec[part] = count(sorted((src / part).rglob("*.lean")))
        stm = (src / "Statements.lean").read_text(encoding="utf-8")
        rec["statements_lines"] = stm.count("\n")
        rec["lib_imports_new"] = sum(1 for f in (src / "Lib").rglob("*.lean")
                                     if re.search(r"^\s*(?:public\s+)?import\s+New\.", f.read_text(encoding="utf-8"), re.M))
        out["editions"][ed] = rec
    a, b = out["editions"]["grh"], out["editions"]["grh-compact"]
    same = all((path / "grh" / f).read_bytes() == (path / "grh-compact" / f).read_bytes()
               for f in ("src/Statements.lean", "Challenge.lean", "comparator.json", "lean-toolchain", "lakefile.toml"))
    out["same_statements_and_settings"] = same
    out["factor_compact"] = round(out["submission"]["lines"] / b["all"]["lines"])
    out["factor_readable"] = round(out["submission"]["lines"] / a["all"]["lines"])
    (ROOT / "data/condensed.json").write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    print(f"condensed: grh {a['all']['lines']:,} lines, grh-compact {b['all']['lines']:,} lines "
          f"(New {b['New']['code_lines']:,} lines of code); factors {out['factor_readable']} and {out['factor_compact']}; "
          f"risky constructs {a['all']['risky'] + b['all']['risky']}; same statements {same}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
