# Unit 148: Translates of Poincaré series fill the rows: a Petersson-type second moment along a Bessel subgroup

Merged from the chunks 148-a, 148-b, 148-c, 148-d by `book/plan/merge_chunks.py` (2026-11-26 09:57 UTC). Each chunk was read by its own reader (`book/plan/SPLIT.md`); their notes follow.

## Chunk 148-a

## Dossier 148-a — chunk a of unit 148 (New/Filling): set-up, frames and links, box partitions, amplitude sums

Chunk a of unit 148 (book/plan/SPLIT.md): the modules EichlerFlag, BesselSystem, Setup, LevelBridge, CrudeBoundDefs,
LatticeChart, GramLiouville, StableCells, NearTerms, BoxPartition, UnipotentCovolume, AmplitudeSums (307 members,
77 structured proofs). As chunk a it carries the title and summary of the whole unit (`unit.json`).
Gate: `python3 tools/rb.py check 148-a` exits 0 (text basis; Lean was not run).

### Where to start
1. `Filling` (Setup.lean:22): the record of the data, and `Filling.IsAdmissible` (Setup.lean:301), the standing
   hypotheses. Then the objects named in Setup: 𝖦 = `GRes`, `Classes`, `termsOver`, `classUnip` (𝖴_c(g)),
   `IsBoxPartition`, `classCutoff` (β_c), `besselKernel`, `amplitude`, `amplitudeSum` (A_T(c, s, c')), the constants.
2. `SieveSystem` and `BesselSystem` (EichlerFlag, BesselSystem): the abstract inputs from the real places.
3. The dictionary LevelBridge / LatticeChart: `principalLevel_eq_unitaryLevel`, `besselFn_adelicToInf_mul`,
   `inclHFin_mem_latStabilizer`.
4. Links and levels: `link`, `mem_link_iff_orthogonal` (Lagrangian), `finrank_link`, `link_besselU_mul`,
   `IsNormalForm`, `HasLevel`, `HasLevel.exists_shared_frame_vector`.
5. Lattices: `siegel_lemma`, `tsum_sublatticeDisc_inv_le`, `sublatticeDisc_mul_index_sq_le`, `liouville_gram`.
6. Strong approximation and characters: `besselU_dense`, `exists_besselU_approx`, `exists_besselS_mem_termsOver`,
   `le_genIndex_det_of_fixesNormAtLeast` (agreeing characters force shared vectors up the flag).
7. Boxes and covolume: `isBoxPartition_epsilon`, `tsum_classCutoff_box_le` (frame count),
   `lintegral_classCutoff_eq_unipCovolume` (ν exactly).
8. Amplitude sums: `amplitudeAbs_lt_top_and_cut_le`, `hasSum_amplitudeSum_change_of_weight`, `amplitudeSum_move`,
   `amplitudeSum_besselU_mul`, `amplitudeSum_eq_zero_of_not_agrees`, `amplitudeSum_besselS_one` (identity term = ν·δ).

### How it was made
`gen/build.py` generates `unit.json` and `proofs/*.json` from the census and the sources at the pin (lines, hashes,
quotations, typed facts, binder lists, the declarations each step names) and from the hand-written readings
`gen/m_<Module>.py` (texts, triage, binder readings, step trees and claims), `gen/reads.py`, `gen/imports.py`
(readings of the 232 imported declarations; statements of 246 Mathlib facts). The check `tools/rb.py` shares no code
with the generator. `gen/report.txt` lists what the generator could not resolve and every positional binder reading.

### What I am unsure of (please second-read)
* **Claims of automation-heavy steps** are my reading of what the step establishes; the boundaries and quotations are
  exact, the mathematics is not machine-checked. Least certain, at the level of individual steps:
  `le_genIndex_det_of_fixesNormAtLeast` (steps 5–15: the descending induction, the Eichler elements and the agreement
  argument), `isBoxPartition_epsilon` (2.3.x: the size bookkeeping), `tsum_classCutoff_box_le` (4–12),
  `amplitudeAbs_lt_top_and_cut_le` (6–17), `lintegral_classCutoff_eq_unipCovolume` (12.x), `siegel_lemma` (4, 11).
* **Binders follow the census's text reading** (`rb.py signature`), as the check requires without a Lean run. About 40
  members carry a `binders_note` where Lean's own signature evidently differs: section variables that the text
  reading takes because a bound variable or a name like `S.b`, `𝔰.k`, `TraceOne.τ` repeats their letter; variables it
  misses because it stops at a `:=` inside the statement (`let … :=`) or reads `Rˣ` as one word; instances of shadowed
  section variables (BoxPartition, three `variable {E …}` lines); `→*` read as a function arrow (`reduction`,
  `ratToAdelic`, `adelicToInf`, `adelicToFin`); the instance `σ : Side` dropped after `omit σ` (`besselFn`,
  `besselKernel`, `amplitude`, `amplitudeAbs`, `amplitudeSum`, `amplitudeSum_move`). Evidence is quoted from the
  artifact's own uses; `#check @Name` after the Helios build would settle them.
* **`IsNear.norm_frameProducts_le`** has no structured proof: its proof is a pattern-matching arm on the statement's
  last line, which the line census reads as part of the statement (no value range); its `proof_note` gives the argument.
* **Letters.** The source writes f both for the frame (e₁, …, e_ϱ, z) and for the number of infinite places of E
  (MEMORY.md's f); the dossier follows the source, a note should rename the frame (e.g. 𝔣). New letters of this folder:
  𝔰 = (ϱ, κ, k₀), n = ϱ+1, k = |κ| (MEMORY's k), r = 2ϱ + k + 1 (MEMORY's r, m = 2ϱ + 2), V = H^ϱ ⊕ X₀ ⊕ Ez, Z(γ),
  𝗀(γ), 𝖴, 𝖴⁰, 𝖧, 𝖲, K, K(g), K_c, 𝖦, h_c, β_c, ν, c_G, Θ, τ (tailScale), 𝖽, 𝖽₁, Q₁, T°; g = q₀q₁ is MEMORY's g = g₀g₁.
* Imports from the other chunks of 148 (b, c, d) do not occur: chunk a precedes them in import order.

## Chunk 148-b

## Unit 148, chunk b — reader's notes

Modules (import order): `New.Filling.SchurTest`, `ThinClasses`, `BlockBound`, `PoincareSeries`, `ColumnCoords`,
`CrudeEnergy`, `DegreeBounds`, `GlobalSieve`, `StandardLevel`. 84 members (all declarations of these modules that
`reading/units.proposal.json` lists for unit 148), 40 structured proofs, 451 leaves.
Gate: `python3 tools/rb.py check 148-b` exits 0 (source-only; nothing was built, no Lean was run).

Everything in `unit.json` and `proofs/` is generated by `gen/build.py` from the specifications `gen/spec_*.py`
(texts, readings, claims written by hand; spans, quotations, hashes and typed facts computed from the pinned
source by `gen/lib.py` and `gen/steps.py`, which share no code with `tools/`). `gen/look.py` is a reading aid.

### Where to start

1. The energy chain (the content of the chunk): `Filling.energy` → `energy_add_le`, `energy_sub_cut_le` (full vs cut
   Bessel functions) → `amplitudeSum_eq_zero_of_not_charsAgree` and `CharsAgree.exists_hasLevel` (incoherent and
   degenerate terms) → `energy_le_of_level_pairs` (the main estimate) → `energy_le_of_level_lt` →
   `energy_le_of_linkEnergy_le` (the crude estimate used downstream).
2. Its inputs: the Schur test on a thin class (`tsum_schurIntegral_le`, `tsum_amplitudeAbs_class_le`, with
   `lintegral_boxCutoff_le_of_average` and `amplitudeAbs_sq_le`), the block bounds
   (`enorm_amplitudeSum_le_classSize_top`, `enorm_amplitudeSum_le_classSize`), and the counts
   (`sum_latticeDisc_inv_le`, `tsum_invPowWeight_le_of_codim_le` with `HasLevel.norm_shared_vector_lt`,
   `sum_pairWeight_le`).
3. Independent pieces: the Poincaré series and unfolding (`Fits`, `poincareMap`, `petersson_poincare`), the adelic
   sieve (`sum_frequencies_le`, `one_sided_poisson`, `sieve`), the standard level at a finite place
   (`exists_isLatticeLevel`, `heisenbergMeasure_eq_floorModulus`, `groupMeasure_boxSet_le`,
   `le_stackMeasure_boxSet`), and the degree bounds of `Data.filling` (`DegreeBounds`, also the last stage of the
   seesaw `Data.exists_last_stage_map`, which is in this module but belongs to the seesaw argument).

### Letters used (beyond `MEMORY.md`)

From the docstrings of `New/Filling/Setup.lean` and kept as there: 𝖦 = `GRes` (∏ over the chosen places of
GL_r of the residue fields), ν = `unipCovolume`, τ = `tailScale` = b^{kf/4}, 𝖽 = `mainEnergy`, 𝖽₁ = `besselEnergy`,
S̄ the reduction of the Bessel subgroup, β_c = `classCutoff`, K, K(g) = `latStabilizer`, `principalLevel`,
𝖴, 𝖴⁰, 𝖲, 𝖧 the Bessel unipotent group, its frame-fixing part, the Bessel subgroup and U(X₀); Z(γ) = `frameProducts`,
D_j its leading minors, 𝗀(γ) = `termDisc`; Δ = `frameVolume`; [ξ] = `genIndex`, den(ξ) = `denomIndex`;
f = number of infinite places, k = |κ|, n = ϱ + 1, r = 2ϱ + k + 1 (= k + m − 1 of `MEMORY.md`), g = q₀q₁, b = S.b.
New letters in this chunk's texts: ι = `inclHFin` in PoincareSeries, c_a and hd in `one_sided_poisson` (from the
Lean `let`s), x_f the finite point of V.

### What I am unsure of (please read)

**Binders.** All `binders` follow the census's text reading (the check requires it); nothing was confirmed with
`#check`. Entries I believe Lean does *not* bind are kept and their `reads` say so:
* shadowed section variables: SchurTest after line 60 and 117 (second `[StablyUnram E]`, `[S.IsAdmissible]` for the
  old E, S), BlockBound after line 228 (`S` re-declared; the old `[S.IsAdmissible]`), StandardLevel (instances of
  the first `A`, which line 65 re-declares; in `exists_isLatticeLevel` also `T`, `F`, `h`, which the statement does
  not use — it binds its own F);
* bound variables with the name of a section variable: `c`, `γ` in `sum_pairWeight_le`,
  `enorm_amplitudeSum_le_classSize(_top)`; `a`, `φ`, `g` in `Fits.poincare`, `Fits.poincareMap`.

Entries Lean binds but the census misses: in `form_tailVector` the shape 𝔰 and t, x; in `one_sided_poisson` and
`sieve` everything the type binds after its `let` (the census reads the `let … :=` as the start of the value, so
those statements' remainders are `intro_lines` of the proofs). The texts state these arguments in words.

**Automation that hides a real argument** (claims describe what is established, not how the tactic finds it):
the logarithmic linear combination in `IsNear.le_classSize_and_cellMass_le` (steps 7–10); the final numerics of
`tsum_schurIntegral_le` (1.15–1.22) and of `energy_le_of_level_pairs` (1.13–1.19, 1.24); the class-integral
averaging in `sum_latticeDisc_inv_le` (1.10); the lattice-inclusion argument in `sum_pairWeight_le` (11.x); the
open-cell step in `enorm_amplitudeSum_le_classSize_top` (12–17); the Fourier-coefficient identities in
`one_sided_poisson` (14.x); the level axioms in `exists_isLatticeLevel` (13–15, one `refine` split by spans);
the Weyl-formula bookkeeping in `Data.log_filling_besselDegree_mem_Icc`. Several long single terms are cut into
consecutive spans so that each leaf has ≤ 8 lines; no leaf is marked indivisible.

**Readings of other units' lemmas** in `imports` are short, taken from their docstrings and statements; a few
(`Filling.pairInvariant_mul_le`, `Filling.exists_link_split_le_classGauge`, `exists_mulVec_eq_of_annihilator`,
`exists_mem_besselU_eq_eichlerMap`, `Data.nominalWeight_le_w_sub`, `Data.log_w_le`) are paraphrased from their use
and should be checked against their own dossiers. `ambient_inputs` are Mathlib facts stated from their names (Mathlib
is not on this machine).

**Not treated by a structured proof** (allowed by the contract, by judgment): the definitions with tactic bodies
`IntegralPlace.IsStdLevel.gauge` (47 lines: the verification of the gauge axioms) and `Filling.Fits.weylBesselEquiv`,
and the instance `isHaarMeasure_groupMeasure`. `Fits.poincareMap` (a definition) does have one. Triage exemptions:
8 `automation`, 8 `one-step`, 27 `computation` (definitions and short entrywise identities); 41 `argument`.

**Sampled for a second reading:** the step structure of every proof was checked against the source by the program;
the English was reread for `energy_sub_cut_le`, `IsNear.le_classSize_and_cellMass_le` (the linear combination
matches the Lean coefficients), `tsum_amplitudeAbs_class_le` (product of the two Schur bounds) and
`energy_le_of_level_lt`. The rest has had one reading.

## Chunk 148-c

## Unit 148, chunk c — reader's notes

Modules: `New.Filling.TopFloor`, `GlobalToLocal`, `FillingAdmissible`, `FillingData`. 79 members (all declarations
of these modules listed for unit 148), 38 structured proofs (35 lemmas, the `IsAdmissible` instance of
`FillingAdmissible`, and the definitions-with-proofs none), 271 leaves. Gate: `python3 tools/rb.py check 148-c` exits 0
(source only; nothing built). Generated by `gen/build.py` from `gen/spec_*.py` (same generator as chunk b, `gen/lib.py`,
`gen/steps.py`; it shares no code with `tools/`).

### Where to start
1. TopFloor, the local theory at one finite place with a standard level: the finite Bessel function `IntegralPlace.phase`
   (χ_g), the finite Bessel vector `Level.IntermediateGroup.besselVector` (W_Z) of an intermediate group K(g) ≤ Z ≤ K,
   its inner-product formula `unipotentMass_mul_inner_besselVector`, the mass bound `pairingNorm_mul_le_massRatio`,
   the shell bound `lintegral_shells_le` (the technical core), its consequences `enorm_floorForm_le` and the bottom value
   `floorZeroForm_le_main_term`; then the top kernel (`Level.correlation`, `Level.topKernel`, `Level.energy`) with
   `floorForm_top_eq_integral` and `lintegral_energy_le_topKernel`.
2. GlobalToLocal: the filling level at the places T (`Filling.IsFillingLevel`, `exists_isFillingLevel`), the dictionary
   (`toPlaces`, `mem_unitaryLevel_iff`, `reduction_eq_iff`, `md_g`), `card_reducedImage_besselS`, and the unfolding of
   coset amplitudes into local correlations `IsFillingLevel.correlation_smul_eq_cosetAmplitude`, with
   `exists_hasSum_cosetAmplitude` (big-cell decomposition of a block).
3. FillingAdmissible / FillingData: `Data.filling` (the filling data of the admissible data D, with Bessel systems from
   `Data.exists_besselSystem`) and its admissibility (the instance at FillingAdmissible:40).

### What I am unsure of
* This chunk was read faster than chunk b (it was claimed after chunk b passed, under rule 7): the claims follow the
  Lean structure step by step but are terser, and several inputs from `New/RealPlace/*` (gauges: `Gauge.*`,
  `Size.minors_mem_ofSize`, `Level.enorm_floorForm_le`, `Level.pairingNorm`, …) are described from their names and
  use, not from a reading of their own dossiers. The longest arguments (`lintegral_shells_le`,
  `correlation_smul_eq_cosetAmplitude`, `exists_isFillingLevel`, `Data.exists_besselSystem`, the admissibility instance)
  deserve a second reading against the source before a note relies on them.
* Binders follow the census's text reading; many entries of TopFloor (second half) are section variables (x, y, u, k,
  g, a second `A`/`T` declaration at line 419) that Lean probably does not bind; their `reads` say so where clear. Not
  confirmed with `#check`.
* `let` statements read by the census as values: `eventually_sum_packets_le_energy`, `floorForm_top_eq_integral`,
  `lintegral_energy_le_topKernel`, `termPosition_floorGroup_spec`, `correlation_smul_eq_cosetAmplitude`,
  `exists_gauge_depth_of_ne_zero` (and the body opening of `lintegral_formMajorant_ne_top`): their statement remainders
  are `intro_lines`.
* Not given structured proofs (by judgment, allowed): the definitions `Data.filling` (13 lines of field checks), the
  instance `Data.unitarySignFrameY`, `Fintype` of cosets; triage exemptions: 22 computation, 13 one-step, 6 automation.
* Letters as in chunk b's README; new: χ_g = phase, W_Z = besselVector, 𝖬 = groupMeasure, v = unipotentMass, κ_ϱ =
  headDensity, 𝒥 = correlation, w_p the Weyl element of length ϱ, T also the finite set of places (GlobalToLocal).

### Second reading (2026-11-26)

A second reader (Claude) re-read this chunk after chunk d, with less time; the corrections live in `gen/spec_second.py`
(imported last by `gen/build.py`, which also applies its `CLAIM_FIX` table and quotes imports to the end of their
statements through `IMPORT_LINES`); the first reading's `spec_*.py` are unchanged. `unit.json` and `proofs/` were
re-emitted by the generator. Gate: `python3 tools/rb.py check 148-c` exits 0.

**What changed.**
* All 59 import readings rewritten from the quoted statements (none from names); truncated quotes extended to the full
  statement (`amplitudeAbs_lt_top_and_cut_le`, `exists_eichler_orbitPoint_eq`, `exists_isBesselFunction`,
  `Gauge.formMajorant_sq_le`, `Gauge.hasMatSize_sub_one_of_floorValues`, `Gauge.lintegral_positions_le`,
  `Gauge.pivotModulus_sq_le_of_capped`, `unfold_besselU`, `ascConv_unitaryLevel`, `lintegral_le_idealZeta_mul`,
  `weylDimensionPoly`, …).
* 2 member texts corrected (below); 28 claims rewritten where they said "simplify", "exponent comparison" and the like.

**Corrections (wrong, not only terse).**
* Import readings that were wrong: `Data.abs_gridParam_le` (the bound is ⌈20b⌉, not 3a; the 3a of `exists_besselSystem`
  step 3 comes from a further size comparison), `Data.hasGap_signsY_paramW` (gap h(D), not "large gap"),
  `Level.pairingNorm` (a double integral of |⟨W x, W' y⟩|² for upperMeasure(F, 0), not a "supremum-type norm"),
  `inv_mul_simpleRootSum_mem` (u ∈ K(g) ⇒ g⁻¹σ(u) ∈ R), `simpleRootSum_mul` (additive on 𝖲, not only 𝖴),
  `card_classes_eq_classSum` (no hypothesis in the statement).
* `IntegralPlace.IsStdLevel.enorm_floorForm_le`: the character ω is ψ(ξ·frameGram(x)_{jj}) with j counted from 0 (the old text
  wrote j+1, following the docstring, which counts from 1).
* `IntegralPlace.IsStdLevel.floorForm_top_eq_integral`: ξ is any element of A ("unit-free" was misleading).

**Still unsure.** Only the claims listed in `CLAIM_FIX` and the import readings had a second reading; the step trees and the
other claims are the first reading's. The longest arguments (`lintegral_shells_le`, `correlation_smul_eq_cosetAmplitude`,
`exists_isFillingLevel`, `Data.exists_besselSystem`, the `IsAdmissible` instance) were compared with the source step by step
only where a claim was rewritten; their other claims were checked for agreement with the quoted lines but not rewritten.

**Members that need `#check` on a build.**
* `IntegralPlace.IsStdLevel.enorm_floorForm_le`: Lean binds the section hypothesis `hj : j ≤ ϱ` (used by `by lia` inside the
  statement's index); the census omits it.
* The TopFloor members after line 114 and 419: the census lists section variables (`x`, `y`, `u`, `k`, `g`, the second `A`, `T`)
  that the statements do not use; Lean does not bind them (their `reads` say so where the first reading noticed).

## Chunk 148-d

## Unit 148, chunk d — reader's notes

Modules: `New.Filling.FixedLines`, `FiniteSystem`, `Moments`, `RowDimension`, `FillingTheorem`, `LinkPairing`.
27 members, 24 structured proofs, 374 leaves. Gate: `python3 tools/rb.py check 148-d` exits 0 (source only; nothing
built). Generated by `gen/build.py` from `gen/spec_*.py` (RowDimension and FillingTheorem are in `spec_fixed.py`).

### Where to start
1. The filling theorem `Data.ramifiedColumns_fill_rows` (FillingTheorem) and its abstract form
   `Filling.Fits.exists_translate_finrank_comap_le` (Moments): translates of the Poincaré series spread over the rows.
2. Its inputs in Moments: the main-term estimate `energy_fixingSet_le` (via the crude estimate of chunk b, the coset
   amplitudes, the top-kernel domination and the sieve), `sum_le_of_positive_type` (second moment with constant one),
   `re_trace_besselS_le`, `energy_compl_besselS_le`, `sum_norm_amplitudeSum_le`; and `Data.finrank_rows_le_mass`.
3. FiniteSystem: Siegel's formula at T (`siegel_sum_le_lintegral_quadric`), the top-kernel domination of the phase sums
   (`sum_blocks_le_topKernel`) and the finite sieve system (`exists_finite_sieveSystem`); FixedLines: the intermediate
   groups that fix lines (`exists_intermediateGroup_lines`).
4. LinkPairing: the discriminant gain (`exists_lifts_linkDiscSq_le`, `minorNorm_sq_le_linkDiscSq_mul`,
   `exists_link_split_le_classGauge`, `pairInvariant_mul_le`) used by `energy_le_of_level_pairs` in chunk b.

### What I am unsure of
* Read last and fastest of the three chunks of this reader (claimed under rule 7 after 148-c): the step trees follow the
  Lean commands faithfully (program-checked), but many claims are short and describe the role of a command rather than
  the full intermediate statement; the long proofs (`siegel_sum_le_lintegral_quadric`, `energy_fixingSet_le`,
  `sum_blocks_le_topKernel`, `exists_lifts_linkDiscSq_le`, `minorNorm_sq_le_linkDiscSq_mul`) need a second reading
  against the source before a note relies on them. Several readings of inputs (`card_mul_sum_det_le`,
  `Filling.liouville_gram`, `Filling.le_genIndex_det_of_fixesNormAtLeast`, `classSum_norm_eq`,
  `IntegralPlace.mass_near_quadric_off_places_le`, `Gauge.integral_floorForm_succ`) are paraphrased from names and use.
* `let` statements read by the census as values: `exists_intermediateGroup_one_prime`, `_lines`,
  `siegel_sum_le_lintegral_quadric` (intro [48, 54]; its root step's head holds the statement end on line 55),
  `sum_blocks_le_topKernel` (intro [160, 167] and a step 0 for the statement's conclusion, lines 168–169, because an
  introduction may hold at most 8 lines), `abs_norm_bordered_det`, `exists_lifts_linkDiscSq_le`,
  `HasIntegralLifts.exists_isIntMatrix`, `exists_link_split_le_classGauge`. The arguments these statements bind after
  their `let` are not in the census binders; the texts state them.
* Binders follow the census's text reading (not confirmed with #check).

### Second reading (2026-11-26)

A second reader (Claude) read the six modules again against the Lean source at the pin and rewrote the generator's readings;
`unit.json` and `proofs/` were re-emitted by `gen/build.py` (nothing edited by hand). Gate: `python3 tools/rb.py check 148-d`
exits 0 (27 members, 24 structured proofs, 400 steps, 361 leaves, 133 imports all quoted at their lines).

**What changed.**
* All 27 `text`s rewritten from the statements and the definitions they use: every hypothesis in Lean's order, the defined
  functions with all explicit arguments (b(S), N(S), q_i(S), g(S), k(𝔰), ϱ, n(𝔰); for data b_D, 𝖦_D, rows(D), Column(D)),
  and the objects unfolded (IsSpread, goodProjTranslate, ramifyingOp, IsFillingLevel, IntermediateGroup, floorZeroForm,
  fixingSet/vectorFixer, SieveSystem's six axioms, HasLevel, HasIntegralLifts, linkDiscSq, minorNorm, classGauge,
  pairInvariant, commonLink). The filling theorem is stated with its domain Column(D) (not the ramified columns): the
  bound is ((1 + φ)/2 + b_D⁻²)·dim Column(D).
* All import readings (71 before, 133 now) rewritten from the quoted statements, none from names. Imports whose census
  statement lines stop at a `let … :=` are now quoted to the end of their statement (`IMPORT_LINES` in `gen/readings.py`,
  checked in `gen/build.py`): `classSum_norm_eq`, `termPosition_floorGroup_spec`, `lintegral_energy_le_topKernel`,
  `eventually_sum_packets_le_energy`, `correlation_smul_eq_cosetAmplitude`, `Gauge.integral_floorForm_succ`,
  `floorForm_top_eq_integral`, `mass_near_quadric_off_places_le`, `jacobi_perp_discriminant`,
  `sublatticeDisc_mul_index_sq_le`, `le_genIndex_det_of_fixesNormAtLeast`, `norm_sq_middle_part_eq`, `Filling.sieve`,
  `card_mul_sum_det_le`, `energy_le_of_linkEnergy_le` (with its section hypotheses hC, hT, h₁, hx, hq, hw, hz), and the
  class `IsAdmissible` (all its fields). 62 declarations that the proofs use but the first reading did not cite were added.
* 396 of 400 claims rewritten to state the mathematics, with the facts each automation call combines; leaves that bundled a
  case split were regrouped into `case` branches (FixedLines `exists_intermediateGroup_one_prime` step 3,
  `re_trace_besselS_le` step 19, `abs_norm_bordered_det` step 3, `exists_mem_link_termDisc_eq` step 2,
  `minorNorm_sq_le_linkDiscSq_mul` step 12).

**Corrections (wrong, not only terse).**
* The binder `P` of the FixedLines members was read as "the parameters P of the data"; it is the integral place structure on
  LocProd(T) (a default of `gen/readings.py` keyed by the name; now keyed by the type).
* `energy_compl_besselS_le`: the fixed-norm witness has both flags at every chosen place above q_i, so X = q_i^{2f}, not q_i^f.
* `exists_translate_finrank_comap_le`: the side of `amplitudeSum` in statements without `(σ := …)` is the instance
  `Side.full` (`attribute [instance] Side.full`, BesselSystem.lean 111); the defect 19/2 = 9/2 + 1 + 4 is now traced.
* `HasLevel.abs_norm_bordered_det`: the columns are γf_a for a < j and e*_a for a ≥ j (the docstring says a ≤ j and a > j;
  the code's `sumCompl (· < j)` decides).
* `siegel_sum_le_lintegral_quadric`, `sum_blocks_le_topKernel`, `exists_finite_sieveSystem`: the old texts omitted the
  quantifier "for all sufficiently small L" (small-sets filter) and the conditions on L (clopen, resp. open, compact, ∋ 0).

**Still unsure.**
* Exponents inside automation were read, not computed: e.g. FixedLines step 5.10 (b⁹ ≤ b¹⁰ ≤ q₀ then q₀^{t+1} ≤
  q₀^{2ϱ+k+1} − 1 with t = k − 10¹⁰n⁴), `sum_le_of_positive_type` steps 14–15, the numerics of `energy_fixingSet_le` 1.20.
* `finrank_rows_le_mass` step 4 and `ramifiedColumns_fill_rows` steps 7–8 (identification of ρ(g₀ ⊗ g₁) with e₀(D)) are
  read from the lemma names in the `simp` sets.
* `Data.decrPosition_paramW`: "paramW(D, v) is strictly decreasing along basisNumber" is inferred from `paramW_lt_iff` in
  its one-line proof.
* Mathlib (pin 56a00585) is not on this machine: `ambient_inputs` are stated from names and use.

**Members that need `#check` on a build** (argument lists the text reading gets wrong):
* `Filling.IsFillingLevel.sum_blocks_le_topKernel`: Lean also binds the section variable `{π : Side}` (cosetAmplitude needs
  a Side; Moments line 146 passes `(«π» := .cut)`); the census omits it.
* `Filling.HasIntegralLifts.exists_isIntMatrix`: the statement names τ (`Matrix 𝔰.BesselIndex τ _`, line 131), so Lean binds
  the section variable τ; the census omits it.
* `Filling.exists_link_split_le_classGauge`: the census lists the section variable `m`, which the statement shadows by its
  own ∃ m; Lean does not bind it.
* `Data.poincare`: the census reads the type `D.Column →ₗ[ℂ] …` as an explicit premise (a phantom argument, as in unit 151).

