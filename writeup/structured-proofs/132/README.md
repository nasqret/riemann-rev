# Unit 132: The analysis at the real places: tower measures, gauges, open-cell charts and Plancherel bounds

Merged from the chunks 132-a, 132-b by `book/plan/merge_chunks.py` (2026-11-26 08:54 UTC). Each chunk was read by its own reader (`book/plan/SPLIT.md`); their notes follow.

## Chunk 132-a

## Dossier 132-a — the analysis at the real places, chunk a

> **2026-11-26, statement-boundary overlay (a second-reader message):** members whose statement contains a `let`/`have` now carry the whole statement (`statement_lines`, `statement_span`, `statement_lean_full`); the census's statement lines stopped at the binding's `:=`. Imports of such declarations quote them to their end. See `CORRECTIONS.md` of the merged unit.

> **2026-11-26, second-reading corrections (a second-reader message):** applied through the generator by the correction reader: `RealPlaceSizes.complexLevel`, the definition the census misses, is recorded below (Notes) and in the texts of the members that use it; `literature` records on the imports that cite named classical results (a second-reader message/0011/0012/0017/0019/0024/0032, `gen/literature.json`). See `CORRECTIONS.md` of the merged unit.


Reader: a Claude reader standing in for astra (coordinator's split, `book/plan/SPLIT.md`). Edition `grh-compact` at
`72fead102f663d5c7a407964a13dc0cf9d977207`. Nothing was built: every statement about what Lean does is read from the
source, and claims are labelled accordingly below.

Chunk 132-a = the modules `New.RealPlace.{Size, LevelGauge, FrameNorm, GramSectionBounds, GramSection,
CellNeighbourhood, BesselOrthonormal, SobolevCell, ComplexGauge, FlatCharts, FloorKernels, WeightPlancherel}`:
182 members, 74 structured proofs (368 steps, 349 leaves, longest 8 lines, no indivisible leaf), 207 quoted imports,
27 ambient (Mathlib) inputs. Gate: `python3 tools/rb.py check 132-a` exits 0 (`verified`, that command).
`python3 reading/units/132-a/gen/verify.py` re-checks hashes and quotations with code independent of the generator.

### Where to start
1. `LevelGauge`: the structures `Size` (in `Size`), `Level`, `IsPairingKernel`, `Gauge`, and the measures
   `floorMeasure` θ^F_l, `stackMeasure`, `groupMeasure` 𝖬^F, `upperMeasure` — the tower method: a Haar measure of the
   unitary group as a convolution of floor measures, and kernels averaged floor by floor.
2. `FlatCharts`, `FloorKernels`, `WeightPlancherel`: the per-floor estimates (fibre bounds, Cauchy–Schwarz on a floor,
   weight integrals `lintegral_floorWeight_le`, `lintegral_mul_invWeight_le`, Plancherel on a Heisenberg radical
   `parseval_heisenbergMeasure_of_box`). These feed `LocalTheorem` (chunk 132-b).
3. `FrameNorm`, `GramSectionBounds`, `GramSection`, `CellNeighbourhood`, `SobolevCell`: the open-cell double-coset
   chart of G₁(𝔰) (section γ_Z, Jacobian 𝗀(Z)^{k−1}·Cayley densities, injectivity) and the Sobolev bound
   `lintegral_gramSection_integral_le`.
4. `ComplexGauge`: at ℂ the tower measure is λ_hF·Haar with (vol U(k)/vol U(r))·λ_hF ≤ 1 (`haarRatio_spec`), and the
   gauge `RealPlaceSizes.gauge`.

### Conventions of the texts (letters as in MEMORY.md where they overlap)
* Hyperbolic pairs are indexed from 0 as in Lean (`Fin ϱ`): the pair of floor a is (e_a, e*_a), a < ϱ; the frame is
  f_b = besselFrame(b), f_b = e_b (b < ϱ), f_ϱ = z; n = ϱ + 1; k = |κ|; r = 2ϱ + k + 1 (rank of V).
* Signature rule: shorthand symbols carry their explicit arguments: J_T = splitGram(T), G_T = U(J_T),
  θ^F_l = floorMeasure(F, l), 𝖬^F = groupMeasure(F), B^S_i = S.ofSize(i) (sizes) and B^Γ_i (gauges), Λ_Γ,
  δ^(b)_F = floorQuadric(F, b) (default β), E^F_b = floorBasis(F, b), O_F = orthonormalPart(F), Bx_F, Cm_F, 𝔅_F,
  s_F = volumeExponent(F), G₁(𝔰), J₁(𝔰), F_𝔰 = frameCols(𝔰), F'_𝔰 = dualFrameCols(𝔰), c_G(𝔰) = openCellConst(𝔰),
  at ℂ: 𝖬_hF, θ^{hF}_l, λ_hF = haarRatio(hF). New letters introduced here: these superscripts/subscripts, and 𝒢, 𝒥
  for local Gram matrices in two claims. Q_l, H_l, 𝒩_{<l}, 𝒩_l, w_l(p), η_l keep Lean's only explicit argument l.
* The structure texts (`Size`, `Level`, `Gauge`) define their fields with bare names (B_i, Bx, Cm, 𝔅, Λ).
* Definitions, structures and abbreviations carry no `triage` (the skill requires one for theorems and lemmas).

### What the census reads wrongly (`heuristic` until Lean is asked; please confirm on the built artifact)
* **43 members stand on a derived signature** (`binders_basis: "lean"`). `binders_lean` says plainly that it was NOT
  printed by Lean: no build here. The derivation: the census counts a name that the declaration binds anew (`∀ a`,
  `fun i ↦`, `{v : n → A | …}`, `∑ a ∈ …`, `∫ x, …`, a structure field's own `{n : Type}` / `j`, a tactic's
  `split_ifs with h`, `𝔰.n` read as the variable n) as a use of the section variable of that name (38 members, found by
  `gen/scopes.py`, which reruns the census reader with scope-aware names, then read by hand); it misses section
  variables after a statement's `let x := …` (`Size.mem_vecsOfSize_of_heisenbergElem`: i, a); and it drops the section
  variable `m` when a hypothesis is named `m` although the type of `F : Level ι T m` needs it
  (`Level.lintegral_mul_left_eq_of_factor`, `Gauge.lintegral_heisenbergMeasure_le`,
  `Gauge.setLIntegral_orthonormalPart_le`). To confirm: `#check @Name` for these 43 names.
* For definitions, `maybe` instance arguments are kept, except `[F.groupMeasure.IsHaarMeasure]`, which no definition
  after line 206 of LevelGauge uses (left out; allowed by the check).
* `RealPlaceSizes.complexLevel` (ComplexGauge.lean 31–41) is **not in the census** (its `@[simps …]` attribute wraps
  onto the line of `def`), so it is in no unit; its content is stated in words where used. Record (a second-reader message, verified
  at the pin by the correction reader, 2026-11-26): file `New/RealPlace/ComplexGauge.lean` (file SHA-256
  `f0e59c67632fa29571ece3545a697a35fadcee2aa2092bb0b73ec4e6cbba6bcb`); the attribute `@[simps toHyperbolicBasis θ
  measureH g 𝔅 boxSet` begins at line 31 and its continuation `positions]` closes on line 32, where the keyword `def`
  stands at column 28; the type `Level {i // i ≠ 𝔰.k₀} (𝔰.middleGram (1 : ℂ)) 0` ends on line 33 and the construction
  on line 41; SHA-256 of the command (lines 31–41 with the final newline; bytes 1393–2332 half-open) =
  `751e5e56cbce8b21b993dd1b19aa26bb99dfb8db4d0633ca0c6aeb787d10f3de`. It is the level at ℂ (a section variable
  hF : RealPlaceSizes 𝔰 ρ s b): the complex hyperbolic basis complexBasis 𝔰, the floor measure cellLaw ϱ ∗ (Haar
  probability of U(κ) carried by embedH), the measure on the compact factor (the same Haar measure carried by
  embedH), basepoint g = 1, the ball 𝔅 = preimage under toLp 2 of the open ball of radius 1/4, the box
  {x : ‖x‖ ≤ ρ} (operator norm), and all positions; it is distinct from the constant `RealPlaceSizes.haarRatio`
  (lines 45–46). Because the census does not know it, it is not a member of 132 (the check would refuse such a member)
  and the census counts (10,967 declarations) and the unit's 239 members are unchanged; the member texts that use it
  (`RealPlaceSizes.haarRatio`, `…haarRatio_spec`, the instance at line 113, `RealPlaceSizes.gauge` here; in 132-b the
  `IsCutBessel` lemmas of ComplexShells and the BandLimits members) name it and say that it lies outside the census.
  The second reader's scan of all 794 pinned files for this multi-line-attribute pattern found no other omitted
  declaration (a second-reader message, `multiline-attribute-receipt.json`); other failure modes of the census were not scanned.
* The line census takes a statement's `let … :=` for the start of the proof in `Size.head_entries_mem_ofSize`
  (lines 159–160), `logDerivU_unipotentOf_mul_embedH` (45–47), `Size.mem_vecsOfSize_of_heisenbergElem` (22–24) and
  `Gauge.amplitude_support_and_plancherel` (143–147): those statement lines stand in `intro_lines`.
  `Level.invWeight_mul` is given lines 80–83 by the census; line 83 is the `seal … in` prefix of the next declaration
  and is quoted in the last step with that remark.
* Proofs inside definitions (`gramSection`, `RealPlaceSizes.gauge`, and the unlisted `complexLevel`) are described in
  the definition's text, not given structured proofs (the check does not require them).

### What I am unsure of (`heuristic`)
Claims of steps that are long `simp`/`grw`/`grind` chains were reconstructed from the lemma names and the goals' shape,
without Lean. Least certain: `openCellChart_jacobian` steps 9–17; `lintegral_gramSection_integral_le` 12–16;
`RealPlaceSizes.haarRatio_spec` 5–22; `Gauge.amplitude_support_and_plancherel` 10–13; `Gauge.lintegral_floorWeight_le`
8–12; `Gauge.lintegral_mul_invWeight_le` 10–15; `Gauge.parseval_heisenbergMeasure_of_box` 5–7;
`norm_sectionMatrix_le` 1.3–1.5; `Gauge.hasFibreBound_floorQuadric_of_le` 3 (the Mathlib lemma `measure_le_of_sub_mem`
is read from its use). The statements (`text`) were each compared with the Lean statement lines; the definitions'
words were checked against their definitions, not their names.

Proposed for a second reading (by the writer; not done by me): every step of `Size.det_mem_ofSize`, `Level.stackMeasure_mconv_dirac`,
`besselSize_le_of_dual`, `exists_eq_mul_gramSection_mul`, `Level.IsPairingKernel.upperPairing_invariant`.

### Files
`unit.json`, `proofs/*.json` are generated by `gen/build.py` from `gen/content/*.py` (the words) and the census;
`gen/scopes.py` (argument lists), `gen/survey.py`, `gen/sig.py`, `gen/premises.py` (aids), `gen/verify.py`
(independent re-check). Run: `cd reading/units/132-a/gen && python3 build.py && cd ../../../.. && python3 tools/rb.py
check 132-a`.

## Chunk 132-b

## Dossier 132-b — the analysis at the real places, chunk b

> **2026-11-26, statement-boundary overlay (a second-reader message):** members whose statement contains a `let`/`have` now carry the whole statement (`statement_lines`, `statement_span`, `statement_lean_full`); the census's statement lines stopped at the binding's `:=`. Imports of such declarations quote them to their end. See `CORRECTIONS.md` of the merged unit.

> **2026-11-26, second-reading corrections (a second-reader message):** applied through the generator by the correction reader: `RealPlaceSizes.complexLevel`, the definition the census misses, is recorded below (Notes) and in the texts of the members that use it; `literature` records on the imports that cite named classical results (a second-reader message/0011/0012/0017/0019/0024/0032, `gen/literature.json`). See `CORRECTIONS.md` of the merged unit.


Reader: a Claude reader standing in for astra (coordinator's split, `book/plan/SPLIT.md`; chunk claimed by `mkdir` under
rule 7 after 132-a passed). Edition `grh-compact` at `72fead102f663d5c7a407964a13dc0cf9d977207`. Nothing was built: every
statement about what Lean does is read from the source.

Chunk 132-b = the modules `New.RealPlace.{LocalTheorem, ComplexShells, BandLimits, OpenCellBound, BesselCut,
VolumeKernel}`: 57 members, 34 structured proofs (297 steps, 290 leaves, longest 8 lines, no indivisible leaf), 187 quoted
imports (unit 132 = chunk 132-a, 133 = DiscreteSeries, 148 = Filling, and the library units), 1 ambient (Mathlib) input.
Gate: `python3 tools/rb.py check 132-b` exits 0 (`verified`, that command). `python3 reading/units/132-b/gen/verify.py`
re-checks hashes and quotations with code independent of the generator. The unit's title and summary stand in 132-a.

### Where to start
1. `LocalTheorem`: the forms 𝓘_j = `floorForm` (pairings of a cut Bessel function with its Weyl translates, averaged
   floor by floor), their moduli `formModulus` and majorants `formMajorant`, the descent identities
   `Level.integral_succ_floor_eq` / `Gauge.integral_floorForm_succ`, and the three local bounds by the self-norm product:
   `Gauge.formMajorant_sq_le` (volume cap), `Gauge.formModulus_sq_le_of_char` (a character on the floor),
   `Gauge.formModulus_sq_le_of_heads` (unequal heads; Plancherel on a Heisenberg radical).
2. `ComplexShells`: at ℂ (`IsCutBessel`), the local theorem summed over shells of gauges:
   `IsCutBessel.formConst_mul_lintegral_le`, `IsCutBessel.norm_floorForm_le`.
3. `BandLimits`: `hasBandLimits_of_isCutBessel` assembles the sieve system J_i = formConst·𝓘_i, J_{ϱ+1} = ⟨Ξ(p), Ξ(q)⟩.
4. `OpenCellBound` (`BesselSystem.open_cell`), `BesselCut` (Schur bounds from a convolution identity; normalising and
   cutting a peaked Bessel function to a cut pair), `VolumeKernel` (lattice-translate lemmas for the Filling, the volume
   weight Δ and its Hua-type kernel bound `exists_kernel_frameVolume_le`).

### Conventions
As in 132-a (`reading/units/132-a/README.md`): pairs indexed from 0, frame f_b, n = ϱ + 1, k = |κ|, r the rank; shorthand
symbols carry their explicit arguments (J_T, G_T, θ^F_l, 𝖬^F, 𝗆^F_j = stackMeasure(F)(0, j), κ_j(p, q) = headDensity,
G₁(𝔰), c_G(𝔰), L_hF = complexLevel(hF), λ_hF, gauge(hF, h), Δ = frameVolume, …). Import words taken over from 132-a are
marked "(member of chunk 132-a)" or reuse 132-a's import words; G₁ and c_G are written with their argument (𝔰) there too.
Definitions and structures carry no `triage`.

### What the census reads wrongly (`heuristic` until Lean is asked; please confirm on the built artifact)
* **12 members stand on a derived signature** (`binders_basis: "lean"`, each `binders_lean` says it was NOT printed by
  Lean): the census takes a name bound anew in the declaration for the section variable of that name — x in
  `Place.IsBessel`, `Level.IsCut`, `Level.pairingNorm`, `Gauge.lintegral_selfNorm_le`, `Level.enorm_floorForm_le`,
  `Level.integral_succ_floor_eq`, `Gauge.integral_floorForm_succ`, `Gauge.lintegral_positions_le`, L in
  `IsCutBessel.exists_gauge_isHead`; it reads `variable (F) in` as a second variable F (`sieveVector`); and it stops at a
  statement's `let … :=`, missing 𝔰 and the instance p : Frame 𝔰 ε (`IsBesselFunction.hasSchurBound_of_convolve_eq`) and
  the section variable c (`Filling.HasLevel.exists_frameImage_toRows₂_eq_add`). To confirm: `#check @Name`.
* The same `let` reading puts statement lines into the "value": they stand in `intro_lines` for
  `Gauge.integral_floorForm_succ` (311–313), `IsBesselFunction.hasSchurBound_of_convolve_eq` (29–31),
  `Filling.HasLevel.middle_shared_vector_le` (56–57), `Filling.HasLevel.exists_frameImage_toRows₂_eq_add` (90–96, with the
  value's own `let x := …`), `exists_kernel_frameVolume_le` (165–171).
* `RealPlaceSizes.complexLevel` is not in the census (see 132-a, with the record of a second-reader message: ComplexGauge.lean 31–41, command SHA-256 `751e5e56…`); it is written `complexLevel(hF)` = L_hF in words, and the member texts that use it say that it lies outside the census and is no member of the unit.

### What I am unsure of (`heuristic`)
Claims of steps that are long `simp`/`grw`/`refine` chains were reconstructed from lemma names and the shape of the goals,
without Lean. Least certain: `Gauge.lintegral_selfNorm_le` 5–17 (the decreasing induction and its invariant);
`Gauge.formModulus_sq_le_of_heads` 4–12 (the twist identity on floor i); `Gauge.formModulus_sq_le_of_char` 7–12;
`Level.integral_succ_floor_eq` 3.1–3.5; `IsCutBessel.formConst_mul_lintegral_le` 5–16 (the shell constants);
`IsCutBessel.norm_floorForm_le` 4–11; `hasBandLimits_of_isCutBessel` 19–35 (the energy bound); `BesselSystem.open_cell`
10, 13–18, 22–28; `IsBesselFunction.hasSchurBound_of_convolve_eq` 1, 8, 13; `HasPeakAt.exists_cut_isCutPair` 12, 13.1,
21–26; `Filling.tsum_inv_index_pow_le_of_congr` 1–10 (Hermite form and the two colourings);
`Filling.IsLabelledTerm.eq_of_frameImage_eq` 3; `Filling.HasLevel.exists_frameImage_toRows₂_eq_add` 2–5;
`exists_kernel_frameVolume_le` 5, 9, 14, 17–27 (the determinant identities). The statements (`text`) were each compared
with the Lean statement lines.

Proposed for a second reading (by the writer; not done by me): every step of `Gauge.lintegral_selfNorm_le`,
`BesselSystem.open_cell` and `exists_kernel_frameVolume_le`.

### Files
`unit.json`, `proofs/*.json` are generated by `gen/build.py` from `gen/content/*.py` (the words) and the census; import
words of chunk-a declarations are taken from `../132-a/unit.json`. Aids: `gen/scopes.py` (scope-aware argument lists),
`gen/survey.py`, `gen/sig.py`, `gen/premises.py`; `gen/verify.py` (independent re-check). Run:
`cd reading/units/132-b/gen && python3 build.py && cd ../../../.. && python3 tools/rb.py check 132-b`.

