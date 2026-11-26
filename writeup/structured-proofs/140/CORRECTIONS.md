# Corrections to unit 140 (good idempotents, labels, transfer of traces)

Date: 2026-11-26. Correction reader: Claude (Opus 5.5). Edition `72fead102f663d5c7a407964a13dc0cf9d977207`. Generator:
`gen/spec.py`, `gen/spec_proofs.py` changed and `gen/engine.py` re-run (the engine now passes `literature` on imports and
`binders_derivation` on members); no output edited by hand.

## Messages applied
- `a second-reader message` (second reading of 140): the discrete valuation convention; six signature receipts.
- `a second-reader message` (statement boundaries): no member listed; two truncated import quotations extended.
- Statement strength: `Space.exists_trace_eq`, `labelChar_degree_bounds`, `isCentralProj_sum_tupleIdem` (`a second-reader message`,
  `a second-reader message` part 2), `exists_orthonormal_Ô`, `Space.finite_levelSpace` (`a second-reader message` part 1, the payload that `a second-reader message`
  describes); identical verdicts where repeated.

The second reader read the dossier `435c0da6f0d9da9a…` (the hand-off of `a second-reader message`). The dossier at the start of this
correction was `70ef6940…` (re-checked 07:14Z, same counts: 46 members, 16 proofs, 126 steps, 118 imports, 6 members on the
"lean" basis); I could not recover the earlier bytes (first committed later). Her points were checked against the
present text and the source, and all apply to it.

Checked against `New/Trace/GoodIdempotent.lean` 12–23, 60–66, 78–91, 132–174, `New/Trace/BadShare.lean` 24–60 and 88–96,
`New/Trace/GoodFormTransfer.lean` 90–118, `New/Seesaw/LatticeAndTorsionDefs.lean` 56–59,
`Lib/LocalGL/Green/LabelDegree.lean` 32–37, `Lib/LocalGL/TraceFormula/TraceComparison.lean` 183–199,
`Lib/GaloisRep/Pseudocharacter/FibreSum.lean` 67–72.

## What changed (old → new)
- `Data.piIdele_spec`, text: "the valuation … is exp(-1) if w is in piPlaces(D) and 1 otherwise" → the same, with
  exp(−1) identified as the element of the multiplicative value group ℤᵐ⁰ that marks a uniformiser (not 1/e): additively
  ord_w = 1 on piPlaces(D) and 0 off it. Same in proof step 1.2 and the import `Data.intValuation_pi`.
- The six members on the "lean" basis — `goodTuples`, `bad_share_le`, `Data.exists_spaceY`, `Data.isCuspKernel_paramW`,
  the instance at GoodIdempotent.lean:157, `Data.reflectionSum_mul_e₀`: `binders_derivation` added, each a source
  derivation with its lines (the `variable` commands at BadShare.lean 25 and GoodIdempotent.lean 21 and 132; the scope
  `namespace Data` … `end Data` at 23–160; the bound `c` of lines 56 and 96; the ∃ V of line 80; the instance hs whose
  variables are s and D; `D.s` as a field at line 171). The lists themselves were re-derived and are unchanged.
- `det_heckeOnGood_eq` step 2: "tr(A^m) = tr(B^m) for every m" → for every m ≥ 0, m = 0 being the equality of the two
  dimensions, which are not assumed equal (the second reader's remark; `charpoly_eq_mul_of_trace_pow_add` quantifies
  over all m).
- Import quotations extended: `labelChar_degree_bounds` [35, 36] → [35, 37], `Data.dvd_card_resField_sub_one`
  [155, 155] → [155, 156]; their texts already stated the full conclusions.
- `Space.exists_trace_eq`: "Known result (…): … H large" → the statement with its hypotheses (stably unramified E with
  μ_5040 and evenly many infinite places, B ≥ 16[E:ℚ](|n|+1)³, H ≥ gapThreshold(n, 10|n|⁵)), the authors' label quoted,
  `literature` (unresolved: Labesse Thms 5.1, 5.4; Arthur–Clozel I.2.4–2.6). README updated likewise.
- `literature` added to `labelChar_degree_bounds` (weakens: Green Thm 14), `isCentralProj_sum_tupleIdem` (weakens: Green),
  `exists_orthonormal_Ô` (specializes: Wall, Jacobowitz), `Space.finite_levelSpace` (specializes: Borel §8.3).

## Not applied, or applied in part
- a second-reader message point 2 asks for elaborator output or an explicitly source-derived basis for the six lists. Elaborator output
  cannot be recorded (nothing is built here; the replay build is incomplete). The derivation is now explicit in
  `binders_derivation`, but `binders_basis` still reads "lean": `rb.py check` accepts a list that differs from its text
  reading under no other value (contracts.md), and setting it to anything else fails the gate. A tool value such as
  "source" would settle this; `#check @Name` should replace `binders_lean` when the build exists.
- The second reader's remaining remarks (one Hecke operator for both Rallis pairings, the gap and rigid-label hypotheses
  on both spaces, the dimension equality as the trace comparison at 1) agree with the dossier; only the m = 0 remark was
  made explicit.

## Digests
- Old: `70ef6940e6a7dc52cd084349d0a0165fb1daf812f19a54c0a53834dd134cd03b` (the second reader reviewed `435c0da6f0d9da9a…`)
- New: `705e307de06998e6c4bde8b64f267c0544a2cb534ec325156aa62a2ecea730f0`
- `python3 tools/rb.py check 140` exits 0: 46 of 46 statements, 126 steps, 99 leaves, 6 of 6 typed facts, 118 of 118
  imports quoted, 243 of 243 arguments (6 members by the "lean" basis, which the check cannot confirm).
