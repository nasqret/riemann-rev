# Corrections to the dossier of 132 (The analysis at the real places: tower measures, gauges, open-cell charts and Plancherel bounds)

## 2026-11-26 — statement-boundary overlay (a second-reader message)

Source: the second reader's a second-reader message (`exchange/to-claude/a second-reader message/statement-range-inventory.json`, sha256 1749e406…). The census ends a statement at its first top-level `:=`; in the members below that `:=` belongs to a `let`/`letI`/`have` inside the type (or, where said, the census runs into an equation-style proof), so the census's statement lines stopped before the conclusion. Each declaration was read in full at the pin and the overlay's span confirmed (it ends just before the declaration's own `:=`). Applied by the generator: the chunk generators `132-a/gen/build.py` and `132-b/gen/build.py` (before unit.json is written; 132-b reads 132-a's dossier for its self-imports, so 132-a was emitted first), then `book/plan/merge_chunks.py 132`, calls `gen/statement_overlay.py`, which gives each listed member `statement_lines` (corrected), `statement_span` (span + SHA-256), `statement_lean_full` (the whole statement) and `statement_basis`, removes a truncated `statement_lean` (`rb.py check` compares `statement_lean` with the census's lines and refuses a longer quotation), and extends the quoted lines of imports to the end of their statements.

### Members (statement lines census → corrected; conclusion old → new)

- `Size.head_entries_mem_ofSize` (New.RealPlace.Size:158:7; assignment inside type): lines 158–159 → 158–160. Chunk 132-a. Old quotation stopped at `let N := S.ofSize (10 * 𝔰.n)` (line 159). Text already complete: p_a, p_a⁻¹ and every s_{i,e*_a} lie in N = B^S_{10n} → unchanged.
- `logDerivU_unipotentOf_mul_embedH` (New.RealPlace.CellNeighbourhood:43:7; assignment inside type): lines 43–45 → 43–47. Chunk 132-a. Old quotation stopped at `let F p := …;` (line 45). Text complete in substance, but it introduced the map as Φ and then stated the conclusion for "F", which the content's notation rule rewrote to F_𝔰 (the frame columns) → now "Φ is real differentiable at p and logDerivU(Φ, p)(v) = besselTangent(…)", with the second `let` (η, b, c) = z′(v) named.
- `Size.mem_vecsOfSize_of_heisenbergElem` (New.RealPlace.FlatCharts:21:7; assignment inside type): lines 21–22 → 21–24. Chunk 132-a. Old quotation stopped at `let v := inclMatrix A (↑) *ᵥ t.1;` (line 22). Text already complete: if some ν ∈ 𝒩_{<a} has u⁻¹((ν·ν(t) − 1)e*_a) of size i, then u⁻¹v and u⁻¹(β − τh(v, v)) have size i → unchanged.
- `Gauge.amplitude_support_and_plancherel` (New.RealPlace.WeightPlancherel:141:7; assignment inside type): lines 141–143 → 141–147. Chunk 132-a. Old quotation stopped at `let f σ := …;` (line 143). Text already complete: (1) the support statement a.e., (2) the Plancherel bound ≤ M·Λ^{99(ϱ+1)(j+12)}·(c/md ξ)^{|ι|}·∫|f|² → unchanged.
- `Gauge.integral_floorForm_succ` (New.RealPlace.LocalTheorem:310:7; assignment inside type): lines 310–311 → 310–314. Chunk 132-b. Old quotation stopped at `let f c := …` (line 311). Text already complete: f integrable and ∫ f = t·floorForm(a, p, q, W, x′ ↦ ψ(η·frameGram(T, x′)_{aa})) → unchanged.
- `IsBesselFunction.hasSchurBound_of_convolve_eq` (New.RealPlace.BesselCut:27:7; assignment inside type): lines 27–28 → 27–31. Chunk 132-b. Old quotation stopped at `let e :=` (line 28). Text already complete: F ∗ e = F and (r+1)⁴(L + r + 1 + 2(ϱ+1)²) ≤ B ⇒ HasSchurBound(F, rep, B, deg_λ⁻¹∫|F|²) → unchanged.
- `Filling.HasLevel.middle_shared_vector_le` (New.RealPlace.VolumeKernel:55:7; assignment inside type): lines 55–56 → 55–57. Chunk 132-b. Old quotation stopped at `let y := …` (line 56). Text already complete: y_{e*_a} = 0 for all a and 5Σ|Φ_v(y_{x_i})|² ≤ 1 → unchanged.
- `Filling.HasLevel.exists_frameImage_toRows₂_eq_add` (New.RealPlace.VolumeKernel:87:7; assignment inside type): lines 87–90 → 87–96. Chunk 132-b. Old quotation stopped at `let ξ := …` (line 90). Text already complete: the lattice hypothesis ⇒ ∃ l with classCoordX₀(c)·l integral and (γ′f).toRows₂ = (γf).toRows₂ + ((g·l·ξ; 0); 0) → unchanged.
- `exists_kernel_frameVolume_le` (New.RealPlace.VolumeKernel:164:7; assignment inside type): lines 164–165 → 164–171. Chunk 132-b. Old quotation stopped at `let i := castLE l` (line 165). Text already complete: det z ≠ 0 ⇒ ∀ V ∃ measurable K with the bound on ∫K and (Δ(y)/Δ(γ⁻¹y))^{k+ϱ+1} ≤ K(A) → unchanged.

### Proof steps and summaries

- All nine proofs own the statement tails by `intro_lines` (no claim); their summaries already said that these lines are the end of the statement (Size.head_entries_mem_ofSize, logDerivU_unipotentOf_mul_embedH, Size.mem_vecsOfSize_of_heisenbergElem, Gauge.amplitude_support_and_plancherel, Gauge.integral_floorForm_succ, IsBesselFunction.hasSchurBound_of_convolve_eq, both VolumeKernel lemmas and exists_kernel_frameVolume_le). The summary of logDerivU_unipotentOf_mul_embedH no longer writes the `let` as "F_𝔰" (a notation artefact).

### Imports re-quoted to the end of their statements

- `Filling.frameDisc_weylElem_mul` (unit 148): lines 87–88 → 87–90. Chunk 132-a, unit 148. Text already complete (frameDisc(N, Z(w_ϱ(p)σ)) = d·d̄·(t·t̄ − N²), t and d the `let`s); unchanged.
- `integral_tail_le` (unit 116): lines 59–59 → 59–61. Chunk 132-b, unit 116. Text already complete (f = deg_λ·(2/‖g‖)^c integrable with ∫ f ≤ 8(2000(n+L+1)⁶)^{2n²}·2^c); unchanged.
- `Filling.norm_sq_middle_part_eq` (unit 148): lines 215–217 → 215–218. Chunk 132-b, unit 148. The truncated quotation (to line 217) had hidden the last conclusion, and the text lacked it: "if s_v ≤ 0 at some infinite place v, then t lies in the span of the frame f" (line 218). Now stated, with s_v from the `let`.

### Not applied

- Nothing: every overlay span of this dossier was confirmed by reading the source. The chunk self-imports Gauge.amplitude_support_and_plancherel (132-b: lines 141–143 → 141–147) and Size.head_entries_mem_ofSize (132-b: lines 158–159 → 158–160) were re-quoted in 132-b, with the member texts of 132-a; the merge drops them.

### Digests and check

- dossier digest (`dossier_sha256`): old `8cbc095a870fb4248c4ed134d2c77ff85c236f7570b56a858337ed4a61bb79c6` → new `6801c3d2f2bb7790fe6cec92cf76f6efa5f584da011ff6f5c895927e61f50e49`
- `python3 tools/rb.py check 132`: exit 0 — unit 132: 239 of 239 statements at their lines; 108 structured proofs, 665 steps, 639 leaves (longest 8 lines, bound 8), 665 steps quote their lines; typed facts in the source: 72 of 72; imports quoted: 266 of 266; arguments accounted for: 3158 of 3158 (55 members by Lean's own signature, which this check cannot confirm)


- chunk digests: 132-a old `d7ce5b7550405c693caf4e839d8e3c578a11ff4f625b9e431e21099a078a8078` → new `8a1f7b194837bc429927e8d89ac2245e332edb0dc7c838c06e375216d354472a`; 132-b old `5c4f58bed6fac79b46f120ceabf15b44a18d291196e612d7190bacfc56adeee4` → new `b25b52906cc726d504a08a632dacd4ed96c6933f65f9546c0350a4f59f2513cb`. `python3 tools/rb.py check 132-a` and `check 132-b`: exit 0.

## 2026-11-26 — the missing declaration `complexLevel` (a second-reader message) and statement-strength verdicts

Correction reader: a Claude agent (Opus 5.5), the only writer of the chunk and unit folders during this pass. Messages
applied: a second-reader message (the second reader: `RealPlaceSizes.complexLevel`, which the written census misses) and the statement-strength
verdicts of a second-reader message, 0011, 0012, 0017, 0019, 0024, 0032 for the imports that cite named classical results. Checked
against the pinned source (`lsernau/grh-lean` @ `72fead1`, `grh-compact/src`); changes made in the chunk generators
(`132-x/gen/content/*.py`; `gen/build.py` of both chunks now attaches `gen/literature.json`, written by the new
`gen/make_literature.py`), the chunks emitted again (132-a first, since 132-b reads its words), checked, and merged with
`book/plan/merge_chunks.py 132`. Nothing was built.

### What changed (old → new)

1. a second-reader message verified at the pin: `New/RealPlace/ComplexGauge.lean` (file SHA-256 `f0e59c67…`), the attribute begins at
   line 31, its continuation `positions]` closes on line 32 where `def RealPlaceSizes.complexLevel` stands (keyword at
   32:28), the type ends on line 33 and the construction on line 41; the SHA-256 of lines 31–41 with the final newline
   (bytes 1393–2332) is `751e5e56cbce8b21b993dd1b19aa26bb99dfb8db4d0633ca0c6aeb787d10f3de`, as in
   `multiline-attribute-receipt.json`; the census (10,967 declarations) indeed has no record of it.
2. README of 132-a (and so of the merged unit): the one-line remark → the full record (place, hashes, what the level
   consists of, distinct from `haarRatio` at 45–46, why the census misses it, why it is no member, the members that use
   it); README of 132-b points to it.
3. Member texts that use it: 132-a (`RealPlaceSizes.haarRatio`, `…haarRatio_spec`, the instance at line 113,
   `RealPlaceSizes.gauge`): "(a definition at lines 31–41 of the file that the census does not list, see README)" →
   names RealPlaceSizes.complexLevel, its keyword position, the reason (two-line @[simps …] attribute) and that it is
   therefore no member of the unit; 132-b (the `IsCutBessel` members of ComplexShells, `IsCutBessel.continuous_sieveVector`,
   `hasBandLimits_of_isCutBessel`): "L_hF = complexLevel(hF)" + (RealPlaceSizes.complexLevel, ComplexGauge.lean 31–41,
   outside the census and so no member of the unit). It is not added as a member (the check would refuse a member that
   the census does not know) nor as an import (an import must be a census declaration).
4. Imports with `literature` (9): `norm_sub_le_of_holomorphic_bdd` (weakens: + a consequence of the scalar Schwarz lemma on
   a complex line, no derivative estimate), `lintegral_orbitMeasure_lintegral` ("∫_{H∖X}" → the integral against
   orbitMeasure ν μ = β·μ with the cutoff, all hypotheses, infinite values allowed; Packing.lean 86–92; unresolved),
   `exists_eq_smul_haar` (+ d = 0 and ∞ allowed; unresolved), `Place.plancherel_inequality` (weakens: a one-sided
   consequence of Plancherel), `isIdempotentKernel_psiInFrame` (unresolved: threshold and normalisation the artifact's
   own), `hua_integral_le` (weakens: follows from Hua's exact integral); records only: `witt` (matches),
   `cartan_decomposition` (specializes), `ostrowski_taussky` (matches).

### Not applied

* a second-reader message (a second reading of unit 132 by the second reader, sent after a second-reader message) is not part of this pass's brief and was not
  applied; the next correction pass should take it.

### Digests and checks

- dossier digest of 132: old `6801c3d2f2bb7790fe6cec92cf76f6efa5f584da011ff6f5c895927e61f50e49` → new
  `7629ae37a16cd00d55a9f964721db47d7ed55928bc92d7e669775d873e6809f1`.
- chunks: 132-a `8a1f7b19…` → `2cdcd8b90b5ac0b9315c7fd79cb625f672c87cf2b348026edca61f753c8d6a04`; 132-b `b25b5290…` →
  `671d04a08cc6e317bc002c37b867db583b4cf125d250c24e62a0b759a142c8d1`.
- `python3 tools/rb.py check 132-a`, `132-b`, `132`: exit 0 — unit 132: 239 of 239 statements at their lines; 108
  structured proofs, 665 steps, 639 leaves (longest 8, bound 8); typed facts 72 of 72; imports quoted 266 of 266;
  arguments accounted for 3158 of 3158 (55 members by Lean's own signature, which this check cannot confirm).

Cost: about 35 minutes of wall time for the three units 143, 147 and 132 together (08:22Z–08:57Z by `date -u`, the start estimated from the first command), shared among them; tokens not reported by the client.
