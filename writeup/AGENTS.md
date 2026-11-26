# For AI agents: using this reading of the condensed proof

This folder is a machine-checkable reading of the Lean proof of RH and GRH in
[`lsernau/grh-lean`](https://github.com/lsernau/grh-lean), edition `grh-compact`, commit
`72fead102f663d5c7a407964a13dc0cf9d977207`. It is meant to be read, verified, explained and rewritten by you. Please
keep to the rules below: they are what makes the material trustworthy.

## Rules

1. **The headline is a claim.** The authors report that Lean's kernel accepts the five final theorems. Never write or
   imply that the Riemann hypothesis is proved. Say what kind of evidence stands behind a sentence:
   *kernel-checked as reported by the authors* · *quotation checked by program* (`check.json`) · *read by an AI reader*
   · *refereed by an AI referee* · *taken for granted (an Input, or a quoted classical result)* · *not checked*.
2. **Quote Lean only from the pinned commit.** A link has the form
   `https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh-compact/src/<file>#L<a>-L<b>`
   (`<file>` and lines from `structured-proofs/<unit>/unit.json`). The SHA-256 of a member is that of its source lines
   joined by line feeds plus a final line feed: recompute it to confirm a quotation.
3. **Keep every argument and every hypothesis.** A function, relation or predicate that the formal text defines is
   written with all its explicit arguments; every hypothesis of a theorem stands inside its statement. A rewrite that
   drops one ("for fixed P …") misstates the formal result.
4. **Cite your source**: the note (slug) and the Lean declaration with its lines, or the unit and step id of a
   structured proof.

## The files

- `MANIFEST.json`: the pin, the edition date, the list of notes and units, counts, and the SHA-256 of every file.
  Check it first: an edition is identified by it.
- `structured-proofs/<unit>/unit.json` (schema `readback/unit/1`): `title`, `summary`, and `members`: for each
  declaration `id` (`Module:line:col`), `name`, `kind`, `file`, `lines`, `sha256`, `text` (the statement in words,
  complete), `binders` (its arguments in Lean's order: `name`, `kind` ∈ explicit | implicit | strict | instance,
  `reads`), `triage` (argument, assembly, computation, automation, one-step, restatement, alias); `imports` (what the unit
  takes from other units, quoted at their lines, with a reading); `ambient_inputs` (facts of Mathlib). Some members carry
  `statement_lean_full` (the full statement where a line census cut it short) and notes on arguments that were derived
  by hand (`binders_basis: "lean"` with `binders_derivation`: **not** printed by Lean; to be confirmed on a build).
- `structured-proofs/<unit>/proofs/<name>.json` (schema `readback/proof/1`): `declaration` (the member's id) and
  `steps`: each with `id`, `parent`, `kind`, `claim` (the mathematics the step establishes), `lines` and `lean` (the
  exact source it quotes), `uses` (`{"step": …}` or `{"decl": …}`), `typed_fact` (the exact intermediate type, when the
  step states one), `ambient_uses` (Mathlib facts).
- `structured-proofs/<unit>/check.json`: the program check of the dossier (problems, counts, digest).
  `CORRECTIONS.md`: what the second reading changed, old → new.
- `notes/<slug>/<slug>.tex`: the note (LaTeX; it needs its `data.tex`); `concordance.json`: every declaration the note
  cites, with its file, lines and statement; `spec.json`: the note's account of each declaration's arguments;
  `reader.json`: where each declaration is treated.
- `catalogue/catalogue.json`: every background declaration the argument uses: `class` (definition, elementary,
  named, substantial), `says`, `reference`, `place`, `relation`. `catalogue/second-reading-verdicts.json`: for named
  theorems, the second reader's `verdict`, `comparison` and `sources` (with places). Prefer the verdict where both
  exist.

## Useful tasks, and how to do them well

- **Explain a chapter or a theorem.** Start from `handout.pdf` (the overview, then the chapter), use the note's `.tex`
  for the exact statements, and the unit's `unit.json` for the precise reading of each declaration.
- **Rewrite** (for a seminar, a survey, another level of detail, another language). Keep the statements exactly (rule 3)
  and say which results you take as inputs. Do not strengthen a statement: the formal results are often weaker
  forms of classical theorems, and the catalogue says which.
- **Check a statement against Lean.** Open the pinned file at the member's lines; compare quantifiers, hypotheses and
  arguments with `text`; for a proof, follow the steps of `proofs/<name>.json` and their quoted lines.
- **Find what something depends on.** `imports` of each unit (with the owning unit), and the notes' Inputs. A
  kernel-level dependency export of this edition is not published yet.
- **Report a problem.** Open an issue at https://github.com/nasqret/riemann-rev/issues with the note, the declaration
  and the pinned lines.

## What is known to be incomplete

- No human has refereed the notes. AI referees' reports are being applied chapter by chapter; unapplied points remain.
- Some proofs in the notes are outlines of the formal proof (they say so in "How this note was written").
- Several argument lists were derived from the source by hand, not printed by Lean (marked as above).
- References marked "to be confirmed" have no confirmed place yet.
- An independent build of this edition is pending (a cluster's scheduled downtime interrupted it).
