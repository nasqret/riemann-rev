# Unit 145 — New/Columns: columns, the chain of theta lifts, divisibility at each prime, size bounds

> **2026-11-26, statement-boundary overlay (a second-reader message):** members whose statement contains a `let`/`have` now carry the whole statement (`statement_lines`, `statement_span`, `statement_lean_full`); the census's statement lines stopped at the binding's `:=`. Imports of such declarations quote them to their end. See `CORRECTIONS.md`.

> **2026-11-26, second reading (a second-reader message):** the admissible translations are weighted by π_G (not π̄_G); `IndexDvd` and `HasType` are read as the determinant condition of `New/Core/ModuleIndex.lean` (not a cardinality); the commutation in `exists_move_markOperator` holds for every a and every b ∈ K_f; exp(−1) is the degree −1 element of ℤₘ₀; B_μ is written B_μ(ϑ, Ψ). See `CORRECTIONS.md`.


Dossier by the reader (Claude subagent acting as reader), 26 November 2026, on `lsernau/grh-lean` edition
`grh-compact` at `72fead102f663d5c7a407964a13dc0cf9d977207`. Nothing was built or run in Lean: every statement and
step was read from the source text.

## Where to start

The three results that leave the folder for `New/Endgame/ShortAndEnough` (Theorem A) are
`Data.exists_indexDvd_Bmu_divisible` (divisibility of B_μ at every prime on a submodule of small index),
`Data.weylNormSq_Bmu_le` (size of all conjugates of the untwisted chain) and `Data.span_short_ramifiedColumns`
(short ramified columns span), with the bookkeeping `Data.sum_allowedLoss_mul_log_le`, `Data.heightPerRow`,
`Data.nonsplitPrimes`, `Data.allowedLoss`. Reading order:

1. `ColumnDefs.lean`: the level `columnLevel`, the π-places, columns (`Column`), branching and `restrictToY`.
2. `ChainValuation.lean`: `IsShort` and `span_isShort_eq_top`; the central operator z_w, `ramifyingOp`,
   `ramifiedColumns`, `span_short_ramifiedColumns`; good data (`IsGoodDatum`), `exists_chain_eq_sum`,
   `gaugeLe_chain`. Its first part (`detKernel`, `detPeriod`, `detPeriod_insert`) serves `New/Selmer/ValueFamilies`.
3. `JetExponentBound.lean`: served primes, marked sets, `markOperator`, `jetExponent`, `le_jetExponent`,
   `collisionSum` bounds.
4. `TwistedHeckeType.lean` → `MarkedPrimeType.lean`: small elementary divisors of the mark operators
   (`Columns.hasType_markOperator`, `IsMarked.hasType_markOperator`) and the level prime N (`gaugeLe_Bmu_at_N`).
5. `LocalStatement.lean`: the Hecke transfer, the raise bounds, the gauge bounds and the two main results.
6. `SizeEstimates.lean`: sizes (row lengths, factorials, class counts, the sum of allowed losses).

**Reach.** The proposal says that by name only 1 member is reached from the root; that count misses dot notation
(MEMORY.md, 26 Nov). By a grep of the sources, the members listed at the end are used outside `New/Columns`, and all
the others are used inside the unit by those (e.g. the whole JetExponentBound/TwistedHeckeType/MarkedPrimeType chain
by `exists_indexDvd_Bmu_divisible`); `Data.instUbCastRealRrLogLx₁` is an instance of the size tactic and is used
implicitly. I found no member that is evidently unused; the kernel export will decide.

## How the dossier is made

As for unit 150: `gen/gen.py` with the readings in `gen/spec_*.py`; `python3 gen/gen.py`, then
`python3 tools/rb.py check 145`. Counts (last check): 105 members, 46 structured proofs, 350 steps, 331 leaves (the
longest 8 lines; no indivisible leaf), 44 imports, 738 binder entries.

## What I am unsure of (please read before writing)

1. **Binders: the text reading versus Lean.** The lists are the census's (text) lists. This folder redeclares
   section variables several times (E, n in ChainValuation at lines 19 and 85; p and its instances in
   JetExponentBound at lines 13, 38, 124; D, Ψ, ϑ in ChainValuation at line 259), and uses `include`/`omit`, so the
   text reading differs from Lean in many places; each such member carries `reads` beginning "NOT an argument …"
   and/or a `binders_remark`:
   * phantom entries: instances of shadowed variables (IsShort.sub_translate, span_isShort_eq_top,
     exists_eq_sub_centralGen, collisionSum_le, mul_collisionSum_le_loss, collisionSum_evenPlaces_eq_zero,
     le_jetExponent, sum_lowColumns_le); bound names (w in mem_columnLevel, mem_chosenLevel_of_supportedOn,
     ramifyingOp, mem_integralAfter; j in pairTranslates, exists_chain_eq_sum, gaugeLe_chain; e in jetExponent,
     collisionSum_le; Λ in exists_isMarked; p in weylNormSq_Bmu_le; ϑ, Ψ in exists_indexDvd_Bmu_divisible;
     κ in sum_height_mul_kappa_le); projections read as variables (E in centralRep; n, K in norm_map_star_piG_sq);
   * hidden arguments: H and hQ re-included by `include H hQ hv` (line 242 of LocalStatement) for gaugeLe_one,
     gaugeLe_Bmu_of_isMarked, gaugeLe_collisionSum, gaugeLe_pow_jetCeil_smul (the text reading treats the earlier
     `omit H hQ` as final); hΛ in exists_move_markOperator (used after the statement's `let`, where the text reading
     stops); p and its instances through ιₚ or `D.IsMarked Λ` (outParam) in norm_star_piG_le_one, inducedPlace_mul,
     IsMarked.card_le, notMem_thick, sum_inducedPlace_sub_star_eq_zero, star_ne, maxCompactAt_le_columnLevel.
   For definitions, `maybe` instances of shadowed variables are left out (IsShort, algFormCentralRep, centralRep,
   pairTranslates), as the contract allows. Everything here should be confirmed with `#check @Name` after the build.
2. **Census artifacts.** (a) For `Data.IsGoodDatum.exists_hecke_transfer` and `exists_move_markOperator` the
   statement contains `let … :=` at depth 0, which the line census takes for the start of the value; the first step
   owns the rest of the statement and says so. (b) The census counts the next command of the file into two members:
   `Data.name_lastColDatum_mem_raises` (line 76: `seal liftKernel Kernel.lift SmoothForm`) and `Data.weylNormSq_Bmu_le`
   (line 228: `seal Space.weightRep Space.embFin`); a last step of kind `not-proof` owns that line. (c) Truncated
   `typed_fact`s by the checker's rule: `IsMarked.hasType_markOperator` step 4 (`t (s + 1) =`) and `le_jetExponent`
   step 18 (`D.lowColumns _ σ /`); the claims state the full types.
3. **Claims of lower confidence** (dense automation; second reading recommended): `Columns.hasType_markOperator`
   steps 20–35; `IsMarked.hasType_markOperator` 13–18 (which HeckeSizes condition each line proves);
   `le_jetExponent` 11–18; `exists_hecke_transfer` 10.x and 11–13; `mem_raises` 8.2 and 9–16;
   `weylNormSq_Bmu_le` 6–10; `detPeriod_insert` 5.x and 7; `span_isShort_eq_top` 14–21;
   `chain₂_pairTranslates_eq_smul_chain` 3–5.
4. Size comparisons of the data (`le_of_hasLogBound`, which compares exponents of x, x₁, b, log b, …) are named
   "size" in the claims without the exponents.

## Sampled for a second reading

Every step of `Data.exists_indexDvd_Bmu_divisible`, `Data.IsGoodDatum.mem_raises`,
`Data.IsGoodDatum.exists_move_markOperator`, `Data.le_jetExponent`, `Columns.hasType_markOperator`; the texts of
`Data.IsGoodDatum`, `Data.columnLevel`, `Data.restrictToY`, `Data.IsMarked.markOperator`, `Data.jetExponent`.

## Members used outside New/Columns (by name, grep over the sources)

`detKernel`, `detPeriod`, `detKernel_embFin_mul`, `detPeriod_eq_stdClassSum_sum`, `detPeriod_insert`,
`span_isShort_eq_top`, `algFormCentralRep`, `not_isChosen_of_N_mem`, `mem_columnLevel`,
`mem_chosenLevel_of_supportedOn`, `exists_centralGen`, `centralGen`, `scalarFin_centralGen_mem`, `centralRep`,
`ramifyingOp`, `ramifiedColumns`, `exists_eq_sub_centralGen`, `sum_height_mul_kappa_le`,
`ramifyingOp_finrank_comap_and_short`, `span_short_ramifiedColumns`, `pairTranslates`, `admissibleTranslations`,
`IsGoodDatum`, `notMem_piPlaces_of_ne`, `mem_integralAfter`, `projOn_translateDatum`, `norm_star_piG_le_one`, all of
`ColumnDefs.lean` except `π_ne_zero`, `principalLevel_le_columnLevel`, `isLevel_columnLevel`, `le_branchExp`;
`p_mem_inducedPlace`, `inducedPlace_mul`, `IsMarked.card_le`, `weylNormSq_Bmu_le`, `exists_indexDvd_Bmu_divisible`,
`heightPerRow`, `nonsplitPrimes`, `primeSum_eq_sum_localAsk`, `norm_map_star_piG_sq`, `jetSize_le_add`,
`card_stdClasses_le_exp_mul_log`, `card_stdClasses_le_exp`, `allowedLoss`, `sum_allowedLoss_mul_log_le`.
