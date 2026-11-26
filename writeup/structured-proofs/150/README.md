# Unit 150 — New/Curve: theta functions of the CM curve, tight frames, the integral vacuum, jets

> **2026-11-26, statement-boundary overlay (a second-reader message):** members whose statement contains a `let`/`have` now carry the whole statement (`statement_lines`, `statement_span`, `statement_lean_full`); the census's statement lines stopped at the binding's `:=`. Imports of such declarations quote them to their end. See `CORRECTIONS.md`.
>
> **2026-11-26, second reading (a second-reader message) and literature:** the second reader's ten corrections are applied (the character a ↦ a^{p+1} in the rotation average, the direction det M ∣ A in the coupling frames, k! in the Taylor coefficient of a jet, (N²)^{2f|n|} vacuum shifts, Aut(ℂ/K), the multiplier c/(1 − χ), truncated subtraction in the packing, the unit index of the tight frame, composition order in Katz's limit, …), and four imports carry `literature` records (a second-reader message). See `CORRECTIONS.md`, section "second reading (a second-reader message) and literature".


Dossier by the reader (Claude subagent acting as reader), 26 November 2026, on `lsernau/grh-lean` edition
`grh-compact` at `72fead102f663d5c7a407964a13dc0cf9d977207`. Nothing was built or run in Lean: every statement and
step was read from the source text.

## Where to start

Read in this order (definitions first, then the results that leave the folder):

1. `New/Curve/PeriodDefs.lean`: s₀ = `vacuumRoot`, the curve 𝓔 = `cmCurve` with period Ω₀, s₁ = `periodFactor`,
   per = `jetScale`; `norm_gal_vacuumRoot` (|σ s₀|² = rd_E/√d).
2. `TightFrameExists.lean` → `FrameSections.lean` → `IntegralVacuum.lean`: tight frames
   (`exists_isTightFrame`), the vector F of `exists_finitePart_of_isTightFrame` whose theta function is a product of
   translates of θ_𝓔, the scaled vacuum θ° = `intVacuum` and the standard data `standardData`.
3. `ConjugateGenerator.lean` → `ConjugatesOfJets.lean`: Galois conjugation of jets
   (`exists_isJetConjugate_generator`, `exists_semilinear_isJetConjugate`) and the p-adic gauge bounds for theta
   kernels (`norm_jetSeries_le`, `norm_jet_jetSeries_le_one`, `Kernel.raises`, `mem_raises_of_*`).
4. `FormalParameter.lean` → `ThetaProducts.lean` → `JetDivisibility.lean`: the normal form at non-split primes
   (`CMLattice.exists_formal_parameter`, `thetaProducts_normal_form`) and the divisibility of Schur jets
   (`norm_schurJet_le`).
5. `KatzDivisibility.lean`, `DepthPairs.lean`: sharpness (`katz_divisibility_limit`, `exists_isFrobPacking`,
   `exists_hasLargeSplit_of_pairs`), used by `New/Rows/GluedFormTheta`.
6. `LiveSum.lean`: the definitions `localAsk`, `forcedPart`, `gain`, `loss`, `ceilLogM`, `deltaP`, `jetCeil`, `o₀`,
   `IsServed`, `IsCollision`, `collisionSum`, `couplingCount`, `κ`, `lastEntry`, `keptColumns`, `columnsY`, used by
   unit 145.

Members referenced outside the folder (by name; the proposal's `reached` count is name-based): see the list at the
end. Every member is used by another member of the unit or outside it (`kappa₀_ne_zero` through `simp`).

## How the dossier is made

`gen/gen.py` (the reader's own program; it shares no code with `tools/`) reads the census, the source and the
hand-written readings in `gen/spec_*.py` (one module per Lean file: `text`, `triage`, binder readings, and the steps of
each structured proof with their claims), and writes `unit.json` and `proofs/*.json`: quotations, line ranges and
spans, written intermediate types and the owning unit of every import are mechanical. Regenerate with
`python3 gen/gen.py`, then check with `python3 tools/rb.py check 150`.

Counts (from the last check): 89 members, 36 structured proofs, 435 steps, 407 leaves (one indivisible leaf of 9
lines: the single `rcases` of `Space.taylor_line_eq_subst_jetSeries`, lines 27–35, whose term is one application of
dominated convergence), 73 imports (four with `literature` records), 28 ambient inputs, 768 binder entries.

## What I am unsure of (please read before writing)

1. **Binders: the text reading versus Lean.** The binder lists are the census's (text) lists, as the check requires
   without a build. Where the source shows they differ from Lean's, the member says so:
   * *phantom entries* (`reads` begins "NOT an argument of the Lean declaration"): section variables that the text
     reading takes because a bound variable or a projection has the same name — τ in `Data.gain` and
     `Data.collisionSum` (bound by a sum; the source applies them to (D, p) and (D, p, ev)), h in `couplingCount`
     (applied to seven arguments in `JetDivisibility.lean:27`), J in `Parameters.thetaProducts` (∃ J), Q and its
     instances in `Parameters.exists_frame_rows_frob`, p/ι in `Parameters.exists_cyclotomic_different_factor`
     (∀ p ∈ N.primeFactors), E in `norm_map_psi₀` and `exists_finitePart_of_isTightFrame` (`Parameters.E`), c, K in
     `exists_semilinear_isJetConjugate`, the shadowed `[Fintype n]` in five IntegralVacuum lemmas, `[V.IsStd]` in
     `Space.jetSeries_eq_prod`;
   * *hidden arguments* (`binders_remark`, `binders_inferred`): arguments Lean takes through notation, which the text
     reading cannot see — the section's p, `[Fact p.Prime]`, `[PadicPlace p]` through ιₚ in
     `norm_iota_periodFactor`, `norm_periodFactor_mul_conj_le_one`, `exists_isTightFrame`, `Kernel.raises`,
     `Kernel.smul_mem_raises`, `mem_raises_of_standardData`, `mem_raises_of_dvd`.
   All of these should be confirmed with `#check @Name` (or the kernel export) after the Helios build. The `text`
   fields state the functions with the arguments that the source shows (e.g. gain(D, p), collisionSum(D, p, ev)).
2. **Census artifacts.** (a) For `Parameters.mem_raises_of_jet_bound`, `Data.exists_isFrobPacking` and
   `norm_schurJet_le` the statement contains `let … :=` at depth 0, which the line census (and the checker) take for
   the start of the value; the first step of each of these proofs owns the rest of the statement and says so.
   (b) Some `typed_fact`s follow the checker's typed-site rule literally and are therefore not the whole written type:
   `exists_null_coupling_frames` step 7 (`‖(_ :\n valRingCp p`, cut at a line break), `norm_coeff_le_of_deriv` 2.5
   (`_ * _ = p * P ^ I *`), and `Parameters.exists_isTightFrame` step 16, whose fact runs on into the pattern-matching
   alternative `| ⟨c, _⟩ =>` of the `have`. The claims state the full types (and, since the second reading, a second-reader message,
   say in a parenthesis that the recorded fragment is not the whole type): the check's count "typed facts in the
   source: 39 of 39" counts textual matches of fragments, not complete types.
3. **Claims of lower confidence** (dense automation whose exact intermediate goals I could not see without Lean;
   recommended for the second reading): `Parameters.exists_semilinear_isJetConjugate` steps 7–8.3 (the character
   identity hψ) and 13.x (the packing bound); `CMLattice.exists_formal_parameter` steps 19–23 and 36–41 (which goal each
   of the last lines closes); `exists_null_coupling_frames` 3–4 and 12–13.4; `norm_schurJet_le` 3 and 15–21;
   `CMLattice.katz_divisibility_limit` 5.x; `Data.exists_isFrobPacking` 9.2, 9.12–9.17;
   `Parameters.exists_cyclotomic_different_factor` 3–5; `Parameters.exists_isTightFrame` 8, 13.x, 14.x.
4. Imports are quoted at their statement lines with a short reading; readings of Lib results marked "known result"
   follow their docstrings. For the four imports that cite named classical results and have a `by_name` row in the
   second reader's catalogue (`CMLattice.complex_multiplication_theta`, `CMLattice.exists_unit_coeff_degree_le`,
   `CMLattice.norm_a₁_le_one`, `CMLattice.one_le_norm_coeff_translatedWp_nonsplit`), the relation to the literature is
   the second reader's `literature` record (a second-reader message), not the first reading's. Facts of Mathlib (`ambient_inputs`)
   are stated from knowledge of Mathlib, not quoted.

## Sampled for a second reading

Every step of `Parameters.exists_isJetConjugate_generator`, `Parameters.exists_semilinear_isJetConjugate`,
`CMLattice.exists_formal_parameter`, `Parameters.thetaProducts_normal_form`, `norm_schurJet_le`,
`exists_hasLargeSplit_of_pairs`; and the texts of all definitions in `LiveSum.lean` (they are used throughout unit 145).

## Members used outside New/Curve (by name, grep over the sources)

`bigOmega_pos`, `exists_isJetConjugate_generator`, `finHeisOp_mem_standardData`, `norm_jetSeries_le`,
`norm_jet_jetSeries_le_one`, `Kernel.raises`, `Kernel.smul_mem_raises`, `pairWeil_mem_standardData`,
`mem_raises_of_jet_bound`, `mem_raises_of_standardData`, `mem_raises_of_dvd`, `exists_semilinear_isJetConjugate`,
`ne_d_of_placeClass_eq`, `summable_localAsk`, `depthLossInt`, `exists_isFrobPacking`, `exists_hasLargeSplit_of_pairs`,
`latticeModule_cmCurve`, `omega₀_mem_cmCurve_lattice`, `norm_map_psi₀`, `exists_finitePart_of_isTightFrame`,
`isAdmissibleComb_name`, `vacuumScale`, `intVacuum`, `integralAfter`, `standardData`, `norm_intVacuum_le`,
`exists_intVacuum_ne_zero`, `norm_schurJet_le`, `katz_divisibility_limit`, all of `LiveSum.lean`, `cmCurve`, `Ω₀`,
`periodFactor`, `jetScale`, `thetaProducts_normal_form`, `norm_periodFactor_mul_conj_le_one`,
`norm_iota_periodFactor_eq_one`, `exists_isTightFrame`. The others are used inside the folder.
