# Unit 143: The rows: target forms on an indefinite U(r), the volume of the chain of lifts as a product of lift volumes, and the height of each lift volume

Merged from the chunks 143-a, 143-b by `book/plan/merge_chunks.py` (2026-11-26 19:36 UTC). Each chunk was read by its own reader (`book/plan/SPLIT.md`); their notes follow.

## Chunk 143-a

## Dossier 143-a — chunk a of unit 143 (Rows)

> **2026-11-26, statement-boundary overlay (a second-reader message):** members whose statement contains a `let`/`have` now carry the whole statement (`statement_lines`, `statement_span`, `statement_lean_full`); the census's statement lines stopped at the binding's `:=`. Imports of such declarations quote them to their end. See `CORRECTIONS.md` of the merged unit.

> **2026-11-26, second-reading corrections (a second-reader message and the note writer's findings):** applied through the generator by the correction reader (texts, step claims, Lean-basis argument lists of `exists_modKernel_integral_bound` and `Data.lineMultiplier_integral_and_small`, `literature` records on the imports that cite named classical results, from a second-reader message/0011/0012/0017/0019/0024/0032). See `CORRECTIONS.md` of the merged unit.


Reader: the second reader's stand-in (a Claude reader, 26 Nov 2026). Artifact `lsernau/grh-lean` at `72fead10`, edition
`grh-compact`, read from the source only (nothing built here). Gate: `python3 tools/rb.py check 143-a` exits 0
(141 of 141 statements at their lines, 53 structured proofs, 375 steps, 350 leaves of at most 8 lines, 32 of 32
written types in their own steps, 120 imports quoted, 1723 arguments accounted for).

As chunk a, this dossier carries the **title and summary of the whole unit 143**; `chunk_title` and `chunk_summary`
describe this chunk. Members of chunk 143-b that texts or steps use are listed under `imports` with `"unit": "143"`.

### Where to start

1. `New.Rows.RowVolume`: `Data.volume_iota_eq_prod_liftVolume` (the volume 𝔷(ϑ) of the chain on the rows is
   |c(ϑ)|^{rowDim}·∏_j λ_j(ϑ^j)) — one of the two inputs of Theorem C named in the head of `src/New/Main.lean`;
   its proof is eight steps over the Rallis inner product formula and the triangle of lifts.
2. `New.Rows.ComparisonForms`: `exists_comparison_forms`, the input of `Data.heightLe_liftVolume_ratio` (chunk
   143-b): integral comparison forms gl_ϑ whose adjoints through the lifts differ only by constants γ(ϑ) with
   |γ(ϑ)/γ(1)|² a ratio of Hecke L-value products.
3. Then the machinery in import order: `StackedDeterminants` (the record `AuxPair` of an auxiliary dual pair, its
   forms `FormV`, descent `θ`, Hecke operators, `DividedSplitting`, the carrier), `RealMatching` and `Carrier`
   (explicit matching of determinant polynomials, the carrier identity), `MemberKernels` (crude jet bounds, point
   forms), `GluedFormTheta` (a jet no more divisible than predicted; glued lattices; product forms and their theta
   lifts), `MemberOrthogonality` (vanishing theta periods), `CartanIntegrality` (the loss of the Cartan product),
   `MonomialCoefficientVector`.

### Generation

`gen/build.py` writes `unit.json` and `proofs/*.json` from the census, the source at the pin and the hand-written
readings in `gen/spec/*.py` (one file per module; `_common.py` the unit's title/summary, `_ambient.py` the Mathlib
facts). Ids, lines, hashes, quotations, spans, typed facts, binder names and kinds, and owning units of imports are
computed; texts, binder readings, claims and summaries are written by hand. `gen/skel.py NAME` proposes a step
skeleton from the layout; `gen/find.py NAME` looks up declarations. The checker shares no code with the generator
(the typed facts, for instance, are extracted by `gen/lib.py` independently and compared by the check).

### What I am unsure of (read these first)

1. **Arguments that the text reading lists and Lean presumably does not take.** `rb.py signature` reads arguments
   from the text; the check requires the dossier to list exactly that list. In 23 members 42 entries are, by Lean's
   inclusion rule, not arguments: section variables whose letter occurs only as a bound name (`fun τ ↦`, `∏ τ`,
   `∀ {𝔪 …}`, `∃ L`), as a projection (`O.a`, `O.b`, `D.E`) or as a named argument (`(S := R)`), and instances over
   them. Each such entry is kept, with a `reads` that says so: AuxPair.Lifts (w, hw), map_block_eq_blockGL (S),
   stackedDet (a), carrierForm (Φ, τ), twoSidedSubst (l, n, n', τ, j, a), inFirstCols (τ, a), stackedDetProd (τ),
   twoSidedSubst_stackedDetProd (τ), realPairWeil_stackedDetProd (τ), real_matching (τ, η), explicit_matching,
   stdClassSum_det_modKernel_eq, stdClassSum_carrierXi_eq_carrierForm (𝔪), exists_modKernel_integral_bound (E, n,
   h, b and four instances), theta_pointForm (b), cosetKernelSum (E, n, h), DividedLattice.reducedInverse,
   DividedLattice.weilScalar (a), DividedLattice.exists_reducedInverse_eq, DividedSplitting.exists_isGlued (L),
   DividedSplitting.theta_pointForm (b), descentsVanish_hypSum (a), exists_comparison_forms (ϑ). In addition,
   instances over an earlier variable `E` (or `n`, `N`) that a later `variable` command shadows are listed in the
   theorems of `StackedDeterminants` and `exists_det_fromCols` with a reading that says so (in definitions, where
   the check allows it, they are left out). **Not confirmed by `#check @Name`**: the artifact is not built here;
   the Helios build could settle all of them at once. The texts state the declarations with Lean's real arguments.
2. **Statement tails counted as values.** Three statements contain a top-level `let … :=`
   (`Parameters.norm_jet_le_of_isAdmissibleComb`, `exists_modKernel_integral_bound`,
   `DividedSplitting.theta_stdClassSum_productForm`). The census takes that `:=` for the declaration's, so the
   check counts the rest of the statement as proof text; steps of kind `statement` (ids `S1`–`S3`) own those lines
   and say so.
3. **Depth of the long proofs.** The claims of `Data.depth_indicator_jet` (105 lines, p-adic: Katz divisibility,
   tight frames, Frobenius packings), `real_matching` (archimedean matching by density and polarisation),
   `Parameters.norm_jet_le_of_isAdmissibleComb`, `stdClassSum_period_eq_zero`, `DividedSplitting.exists_isGlued`
   and `DividedSplitting.theta_pointForm` are a first reading: they say which facts combine at each step, but the
   exact intermediate goals after `simp`, `grind` and `grw` were not reconstructed (no Lean). Sample these first.
4. **Inputs read from docstrings.** The `text` of each import paraphrases its docstring and statement line; the
   imports were not read in full. The Mathlib facts under `ambient_inputs` are stated from their names and use,
   not quoted (Mathlib is not on this machine); `LinearMap.normDet` is described as the volume factor with
   normDet(u)² = det(u*u).
5. Definitions whose proofs are inside the definition (`AuxPair.auxLevelChar`, `AuxPair.chosenGLRep`,
   `AuxPair.heckePolyOnForms`, `comparisonForm`, `splittingV`) are described in their texts and not structured
   (the check does not ask for them).

### Letters

The letters of `MEMORY.md`, plus, local to this chunk and following the docstrings of the code: M and Q (products of
the chosen and of the twist places of an auxiliary pair; M² = `chosenModulusSq`), ϖ (the chosen generator
`AuxPair.genIdele` of M) and ϖ̄ (its residue `DividedSplitting.genResidue` in O_E/M²), W and V = I_n (the spaces of
an auxiliary pair), k⁺, k⁻ (`colsPlus`, `colsMinus`), ψ (the tame part of μ), S_κ (the Schur matrix), I_e (the
inclusion matrix of an embedding e), θ (the descent `AuxPair.θ`), Ψ (data on matrices modulo a modulus). Two
clashes to note for the writer: `g` is the level g₀g₁ (`D.gProd`) of MEMORY.md but also Lean's name of points in many
statements (the texts keep Lean's name for the point and write D.gProd for the level); and in `CartanIntegrality`
`M` is a natural number in the ideal of the chosen places (Lean's binder), not the ideal itself.

### Second readings

The second reader's reading of the whole unit is a second-reader message (2026-11-26); its corrections are applied (see `CORRECTIONS.md` of the merged unit). Every `text` was written against the Lean statement (not the docstring alone); the
check confirms lines, hashes, quotations, ownership and typed facts, not the English.

## Chunk 143-b

## Dossier 143-b — chunk b of unit 143 (Rows)

> **2026-11-26, statement-boundary overlay (a second-reader message):** members whose statement contains a `let`/`have` now carry the whole statement (`statement_lines`, `statement_span`, `statement_lean_full`); the census's statement lines stopped at the binding's `:=`. Imports of such declarations quote them to their end. See `CORRECTIONS.md` of the merged unit.

> **2026-11-26, second-reading corrections (a second-reader message and the note writer's findings):** applied through the generator by the correction reader (texts, step claims, Lean-basis argument lists of `exists_modKernel_integral_bound` and `Data.lineMultiplier_integral_and_small`, `literature` records on the imports that cite named classical results, from a second-reader message/0011/0012/0017/0019/0024/0032). See `CORRECTIONS.md` of the merged unit.


Reader: the same Claude reader as chunk 143-a (claimed by `mkdir` after 143-a passed its gate, 26 Nov 2026).
Artifact `lsernau/grh-lean` at `72fead10`, edition `grh-compact`, read from the source only (nothing built here).
Gate: `python3 tools/rb.py check 143-b` exits 0 (78 of 78 statements at their lines, 32 structured proofs, 305 steps,
284 leaves of at most 8 lines, 25 of 25 written types in their own steps, 75 imports quoted, 550 arguments accounted
for). The title and summary of this dossier are those of the chunk (rule 4 of `book/plan/SPLIT.md`); the unit's title
and summary are in 143-a. Members of chunk 143-a used here are imports with `"unit": "143"`.

### Where to start

1. `New.Rows.LiftVolumeHeight`: `Data.heightLe_liftVolume_ratio`, the second input of Theorem C named in the head of
   `src/New/Main.lean` (each lift volume ratio has height at most rowDim·k·(log b·B₀ − 𝖴)); its proof combines the
   comparison forms of 143-a with `norm_det_compressedGramOp_padic_le`, `…_arch_le` and
   `Data.heightLe_inv_heckeValueProd_div`.
2. `New.Rows.HeckeValueHeight`: `Data.heightLe_inv_ratio` (one ratio repays one direction) and its product version.
3. `New.Rows.Separation`: `Data.cosetKernelSum_eq_fNatural` (the twist survives only as a constant of squared modulus
   C/heckeValueProd) and `Data.eq_zero_of_integral_fNatural_tableTheta` (the products detect every good form).
4. The supporting files: `LineCoordinates` (index sets, characters, polynomials; coordinates of the determinant
   product), `LineArithmetic` (integrality and size of the line multipliers), `SparseThetaSum` (isolation, sparse
   theta sums), `NaturalFormNear` (the carrier is rapid, holomorphic and nonzero; F♮ approximates a test function).

### Generation

As in 143-a: `gen/build.py` (a copy of 143-a's generator; the folder name selects the chunk) writes the records from
the census, the source at the pin and the readings in `gen/spec/*.py`.

### What I am unsure of (read these first)

1. **Statements cut by the census.** Four statements contain a top-level `let … :=`
   (`Data.weylNormSq_linePolyCoords_le`, `Data.lineMultiplier_integral_and_small`,
   `Data.exists_denom_linePolyCoords`, `Data.exists_test_form_inner_kernelForm`). The census takes that `:=` for the
   declaration's: the rest of the statement counts as proof text (steps of kind `statement`, ids `S1`), and the text
   reading of the signature sees only the cut statement. Consequences: for `Data.lineMultiplier_integral_and_small`
   it lists **no argument** and for `Data.weylNormSq_linePolyCoords_le` **only z**, while Lean's signatures
   presumably also take the section variables {P} {D} (j) (and i, Y, φ). The check demands the text reading, so the
   `binders` follow it; each such member carries a `binders_note`, and its `text` states the full statement.
   **This is a limit of the tool, reported to the coordinator.**
2. **Census artifacts.** Three declarations' line ranges include a command that follows them (`seal … in` after
   `Data.Pair.smul_apply_xiSum` and `Data.exists_test_form_inner_kernelForm`, `unseal …` after
   `Data.cosetKernelSum_eq_fNatural`); steps of kind `census-artifact` (id `X`) own those lines and say so.
3. **Arguments the text reading lists and Lean presumably does not take** (letters that occur only bound or as
   projections): norm_modKernel_sub_realInner_le (w), Data.Pair.xiSum, xiSum_mem, smul_apply_xiSum (E),
   Data.exists_test_form_inner_kernelForm (E, n, [Fintype n], X — the statement binds X by `let`),
   Data.heightLe_inv_heckeValueProd_div (m: only D.m), Data.heightLe_liftVolume_ratio (k : ℂ — only D.k occurs),
   Data.negIndex, DetIndex, linePoly, carrierChar, detRows, card_detIndex (h), Data.exists_denom_linePolyCoords
   (i, Y). Kept, with readings that say so; not confirmed by `#check` (no build here).
4. **Depth of the long proofs.** `Data.exists_fNatural_approx` (82 lines), `Data.lineMultiplier_integral_and_small`
   (73), `Data.heightLe_inv_ratio` (61), `Data.exists_test_form_inner_kernelForm` (59), `Data.cosetKernelSum_eq_fNatural`
   (47), `Data.eq_zero_of_integral_fNatural_tableTheta` (35) and `norm_modKernel_sub_realInner_le` (32): the claims say
   which facts combine at each step; intermediate goals after `simp`/`grind`/`grw` were not reconstructed. Sample these
   first.
5. **Written types as the checker reads them.** One `show` (in `Data.heightLe_liftVolume_ratio`, line 106) continues
   on the next line at a smaller column; the checker's layout rule (and so `typed_fact`) stops at `TameChar.pow _ j =`.
   The claim states the full identity.
6. Inputs are read from their docstrings and statement lines; Mathlib facts under `ambient_inputs` are stated from
   their names (Mathlib is not on this machine).

### Letters

Those of `MEMORY.md` and of 143-a, plus, following the code's docstrings: ϖ̄ = `D.piGBar` (ϖ̄·conj ϖ̄ = g), F♮_i =
`Data.fNatural j i`, Ξ (the trivial lift), 𝗁 = `smallHookNumber j`, ν = `nStar D` (in `exists_fNatural_approx`),
mh = `holMinorsPi`, λ = first minimum, ‖·‖ = `maxOpNorm` on archimedean groups.

### Second readings

The second reader's reading of the whole unit is a second-reader message (2026-11-26); its corrections are applied (see `CORRECTIONS.md` of the merged unit). The check confirms lines, hashes, quotations, ownership and typed facts, not the English.

