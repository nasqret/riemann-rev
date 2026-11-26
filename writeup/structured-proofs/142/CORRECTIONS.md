# Corrections to unit 142 (Fock coefficient decay)

Date: 2026-11-26. Correction reader: Claude (Opus 5.5), the only writer of this folder for the corrections. Edition
`72fead102f663d5c7a407964a13dc0cf9d977207`. Generator: `gen/spec.py` changed and `gen/engine.py` re-run (the engine now
also passes an optional `literature` record on imports and `binders_derivation` on members); no output was edited by hand.

## Messages applied
- `a second-reader message` (second reading of 142): both integrals have the same dilation and Jacobian; the middle calculation.
- The coordinator's relay of the note writer's findings (same three steps; the remark on `A ≠ 0`).
- Statement strength: the `realAction` record (`a second-reader message`, `a second-reader message`, `a second-reader message` part-2-other, identical verdicts).
- `a second-reader message` (statement boundaries): no member of 142 is listed; no import quotation of 142 is truncated.

Each correction was checked against `New/Weil/FockCoeffDecay.lean` lines 13–35 before it was applied.

## What changed (old → new)
- Step 3 (line 20): j integrates x ↦ |v(σx + y)|² → j integrates x ↦ |v((σx + y)/c)|², the dilated function of i composed
  with the measure-preserving T(x) = σx + y (`p.integrable_comp_of_integrable i`).
- Step 2 (lines 18–19): i named as the integrability of the *dilated* function x ↦ |v(x/c)|² (`comp_smul (R := c⁻¹)`).
- Step 5 (lines 23–24): pointwise bound (|v(x/c)|² + |v(σx + y)|²)·K/(c²)^|ι|/2 → (|v(x/c)|² + |v((σx + y)/c)|²)·K/(c²)^|ι|/2.
- Step 6 (lines 25–26): "c^(2|ι|)⟨v,v⟩ for the first term and ⟨v,v⟩ for the second" → both summands integrate to
  c^(2|ι|)·Re⟨v,v⟩ (measure preservation of T, then x ↦ x/c), so the factor 2 and c^(2|ι|) cancel; uses steps 2, 3.
- Step 7 (lines 27–30): generic → |v(z)| = c^d |v(z/c)| exp(−n|z|²/(2(A+n))) at z = x and z = σx + y, then 2ab ≤ a² + b².
- Step 8 (line 31): "Collect the powers and exponentials." → the scalar to absorb is c^(2(d+|ι|)) exp(−nS/(2(A+n))),
  S = |x|² + |σx + y|², to be bounded by (4(A+n)|σ|²/|y|²)^n.
- Step 9 (lines 32–33): → c² ≤ e^(n/A), c^(2(d+|ι|)) ≤ e^n (hA), t = S/(2(A+n)), e^(n(1−t)) ≤ t^(−n) by e·t ≤ e^t; it
  remains |y|² ≤ 2|σ|²S.
- Step 10 (lines 34–35): → |y| ≤ |σx + y| + |σ||x| ≤ |σ|(|σx + y| + |x|) (|σ| ≥ 1), then (a + b)² ≤ 2(a² + b²).
- Proof summary and unit summary: rewritten to the dilated second summand and the four inequalities.
- Member text: a remark added (writer's finding, checked): `A ≠ 0` follows from `[Nonempty ι]` and `hA : d + card ι ≤ A`;
  Lean still takes it as the argument `h0` (kept in the statement and in `binders`).
- Import `realAction`: text adds that the composition identity is proved inside the definition; `literature` added
  (unresolved: Davidson 1987 §1, (1.9a), Lemma 1.11, Thm 1.12; the kernel normalisation is not identified). The first
  reading cited no reference here.
- `ambient_inputs`: added `MeasureTheory.Integrable.comp_smul`, `MeasureTheory.MeasurePreserving.integrable_comp_of_integrable`,
  `Real.exp_one_mul_le_exp`, `norm_le_add_norm_add` (stated from memory, as before).

## Not applied
Nothing contested. The claims of steps 7–10 are the mathematics of the `simp`/`grw` chains as read from the source; the
intermediate goals were not replayed (nothing is built here).

## Digests
- Old (`dossier_sha256`, first reading, read by the second reader): `e65973fddadbc0ed64fbe06442047d31eb0a6283e7bea134d627a0207cfddd58`
- New: `e7eb64e16f6f4e7b3662be14116aee549ac81c55b925180a9ae192f503ca2e2b`
- `python3 tools/rb.py check 142` exits 0: 1 of 1 statements, 10 steps, 10 leaves, 12 of 12 imports quoted, 16 of 16 arguments.
