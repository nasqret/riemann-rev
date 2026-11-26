# Unit 147: The exchange identity: theta integrals of complementary rank agree up to a constant, and cruder forms complete a family to a basis in the lower bound

Merged from the chunks 147-a, 147-b, 147-c by `book/plan/merge_chunks.py` (2026-11-26 10:27 UTC). Each chunk was read by its own reader (`book/plan/SPLIT.md`); their notes follow.

## Chunk 147-a

## Dossier 147-a: unit 147 (New/Exchange), chunk a

Reader: the second reader (this run: a Claude reader standing in for the reading agent; see cost.json). Edition `grh-compact`,
commit 72fead102f663d5c7a407964a13dc0cf9d977207. Gate: `python3 tools/rb.py check 147-a` exits 0 (47 of 47
statements at their lines, 32 structured proofs, 337 steps, 316 leaves, longest leaf 8 lines, typed facts 33 of 33,
153 imports quoted, 727 of 727 arguments accounted for). The title and summary in unit.json are those of the whole
unit 147 (SPLIT.md rule 4).

### Modules (import order) and where to start

CharacterLiftNorm, NonnegativeVanishing, BlockPartners, PartnersMatch, StableSpaces, ExchangeDifference,
StandardCoefficients, LowRankIdentity, RealPair, DeterminantVectors.

Start with the chain that the exchange theorem (`exchange_theorem`, chunk b) uses:
1. `exists_isEquivariantLift` (ExchangeDifference): the difference thetaLarge(Φ) − c·thetaSmall(Ψ) is an
   equivariant functional 𝒟 of the partner Ψ alone (via `matchingPairs.exists_linear_factor`, BlockPartners).
2. `IsEquivariantLift.apply_stdColDatum_eq_zero` (StandardCoefficients): 𝒟 kills every standard datum once its
   centre coefficients vanish at unimodular and at non-represented indices (Freitag's lemma, Landherr's theorem,
   `IntegralFrame.partner_mem_of_unimodular_vanishing` from StableSpaces).
3. `stdExchange_of_periods` (LowRankIdentity): the exchange identity `StdExchange` from a period condition, using
   `thetaTerm_stdDatum_spec` and `centreCoeff_eq_zero_of_not_negative` (NonnegativeVanishing).
4. `exists_stdExchange_top` (RealPair): real data satisfying the period condition, built from a smooth local Witt
   theorem (`exists_contDiff_witt`) and `exists_rapid_with_realSlice`; DeterminantVectors supplies the cone
   integrals of determinant vectors used one floor down (`surjOn_cone_integral_detVectors`).
CharacterLiftNorm is separate: the Rallis inner product of the adjoint lift θ_j^* (`Data.auxLift_injective_and_
hasSum_inner`) and the squared norm of the lift of the constant from U(1) as a partial L-value
(`LValueData.inner_trivialLift_self_eq_L`).

### What I am unsure of

* **Arguments on Lean's rule (12 members)**: `binders_basis: "lean"` for the members listed in unit.json with
  `binders_lean`. Nothing is built on this machine, so `#check @Name` was NOT run: each `binders_lean` says so and
  states the rule applied by hand. Three causes: (a) a statement that starts with `let x := …` (the line census
  takes that `:=` for the start of the proof and reads almost no statement: levelIndicator_support_and_normSq,
  inner_trivialLift_self_eq_L, partner_mem_of_unimodular_vanishing, thetaTerm_stdDatum_spec, partner_block);
  (b) a bound variable that shadows a section variable of the same name (`∀ ϑ`, `∀ y`, `{y | …}`, `∃ c F`,
  `∀ 𝔠`), which the census counts as a mention (auxLift_injective_and_hasSum_inner, exists_common_coset_reps,
  isClopen_primitive, StdExchange, stdExchange_of_periods, detVectors); (c) `variable {E n : _}` declared anew
  in CharacterLiftNorm (auxPair_lifts_trivialLift). A reviewer with the built artifact should run `#check @Name`
  on these twelve.
* **Instance arguments of definitions** marked `maybe` in the census are all listed (with "taken if the
  definition's term uses it"); Lean may drop unused ones.
* **Coarse claims**: in long automation steps the claim names the facts used and the result, not every rewrite.
  Least certain (read these first in a review): `LValueData.inner_trivialLift_self_eq_L` steps 12–27 (the
  doubling computation), `centreCoeff_eq_zero_of_not_negative` steps 9.8–9.14 and 21.x (no invariant functional,
  circle means), `IsEquivariantLift.apply_stdColDatum_eq_zero` steps 1.1.x (Freitag, Landherr), 
  `stdExchange_of_periods` steps 19–37, `exists_stdExchange_top` steps 14.x and 23–26,
  `surjOn_cone_integral_detVectors` steps 1.13–1.20, `IntegralFrame.partner_mem_of_unimodular_vanishing` steps
  8–14.
* **Statement remainders as steps**: where the line census reads a `let` of the statement as the start of the
  value, the rest of the statement is a step of kind `statement` (cut into pieces of at most 8 lines in
  thetaTerm_stdDatum_spec); its claim restates that part of the statement.
* **Cuts inside terms**: long single terms were cut at sub-term boundaries with spans (annotation `cut L:C`):
  centreCoeff_eq_zero_of_not_negative step 21, apply_stdColDatum_eq_zero step 1, thetaTerm_stdDatum_spec step 1.
  No leaf exceeds 8 lines; no `indivisible` leaf was needed.
* **Import readings** paraphrase the quoted statement lines (and doc comments); `ambient_inputs` state Mathlib
  facts from the library's documented meaning, not from its source (no Mathlib source here).
* Nothing was sampled for a second reading (no second reader in this run).

### Letters

As in MEMORY.md. New in this chunk (local to the statements): S for the ramified places of a split tame character
𝔠 (`SplitTameChar.S`), χ_𝔠 its local character, ν its character of [U(1)]; P₊ = posProj; Ψ₀ the standard datum of
the adapted frame; Π(e) = lValueProdInt(𝔠, e).

### How it is made

`gen/` holds the generator: `skeleton.py` cuts each proof into steps by layout (commands of tactic blocks at their
column; bullets and trailing `by` blocks as parents; nested typed `have`/`show` as their own span steps; `cut L:C`
from the annotations), `build.py` emits unit.json and proofs/*.json from census + source + `gen/ann/*.txt` (texts,
argument readings, claims, uses, import and ambient readings, written by the reader). `gen/PROGRESS.md` records the
state. Rebuild: `python3 reading/units/147-a/gen/build.py && python3 tools/rb.py check 147-a`.

2026-11-26: statement-boundary overlay (a second-reader message) applied through the generator; members whose statement has a `let` now carry the whole statement (`statement_lines`, `statement_span`, `statement_lean_full`); see `CORRECTIONS.md`.

2026-11-26: second-reading corrections applied through the generator by the correction reader (a second-reader message with its payloads unit-147-a/b/c.md, and a second-reader message): texts, step claims and summaries in `gen/ann/*.txt`; the second reader's statement-strength verdicts (a second-reader message/0011/0012/0017/0019/0024/0032, `by_name` records) attached to the imports as `literature` records (`gen/literature.json`, written by `gen/make_literature.py`, attached by `gen/build.py`). See `CORRECTIONS.md` of the merged unit 147.

## Chunk 147-b

## Dossier 147-b: unit 147 (New/Exchange), chunk b

Reader: a Claude reader standing in for the reading agent (claimed with `mkdir` after 147-a passed its gate, SPLIT.md
rule 7). Edition `grh-compact`, commit 72fead102f663d5c7a407964a13dc0cf9d977207. Gate: `python3 tools/rb.py check
147-b` exits 0 (131 of 131 statements at their lines, 53 structured proofs, 297 steps, 283 leaves, longest leaf 9
lines (two indivisible leaves, reasons given), typed facts 11 of 11, 94 imports quoted, 1210 of 1210 arguments
accounted for). The title and summary in unit.json are those of the chunk (rule 4).

### Modules (import order) and where to start

SquareLawFourier, EqualRankValue, ExchangeTheorem, TriangleLevelExponent, AlgebraicPartConjugates,
AlgebraicPartDefs, TriangleNorms, CostOfSquares, OneSquare, TriangleArrows, ChainNorms, CrudeModularData.

Start with `exchange_theorem` (ExchangeTheorem): it combines `exists_equalRankThetaRatio_value` (the equal-rank
constant is the same for all split tame characters) and `exchange_of_partners` (EqualRankValue), which descends the
top-of-tower identity of chunk a with `exists_stdExchange_removing_planes`. Then `one_square` (OneSquare), which
turns the exchange identity into the square law (`SquareLaw`, SquareLawFourier) for lift/descent composites, and
`Data.exists_isTriangle` (TriangleArrows), which builds the triangle of lifts and descents (abstract triangle in
TriangleNorms; costs in CostOfSquares) from which ChainNorms gets `Data.iotaAtLevel_injective`. The lift of the
trivial character from U(1) (AlgebraicPartDefs) has squared norm a constant times an L-value
(`Data.Pair.intAlgPart_eq_mul_L`) and is interpolated by one integral group-ring element
(`Data.Pair.isIntegralMeasure_intAlgPart`); its Galois conjugates are in AlgebraicPartConjugates.

### What I am unsure of

* **Arguments on Lean's rule (36 members)**, listed in unit.json with `binders_basis: "lean"`; nothing is built here,
  so `#check` was NOT run and each `binders_lean` says so and states the rule applied by hand. Causes: (a) `let`
  statements (exchange_theorem, one_square, integral_integral_sum_eq, inner_iotaAtLevel, ratio_ne_zero_and_real,
  exists_adjoint_first_arrow, stdLevelIndex_lastResLevel_eq); (b) section variables redeclared in a later
  `variable` line (SquareLawFourier after line 64: the instances of the old n, a; AlgebraicPartDefs' old
  `[Fintype n]`, dropped with `drop:` where the census marks them `maybe`); (c) bound variables or dot notation
  read as section variables (`∀ ϑ`, `∀ 𝔠`, `fun i`, `∀ (σ : ℂ ≃+* ℂ)`, `D.s`, `D.n`, a pattern variable n of an
  equation); (d) `variable {P D}` without written types (the census omits P); (e) `variable (D n c) in`,
  `variable (p W) in`; (f) instance arguments used through notation (ιₚ of `PadicPlace p`) in inducedPlace,
  evenPlaces, markExponent, IsFullMark — whether Lean keeps `[Fact p.Prime]` separately is not certain; also
  `Data.integralColumns` and `Data.IsMarked` keep the census list and may take p-related instances by Lean's rule.
* **Tool issues (reported to the coordinator)**: (1) the census reads the arrow inside `∀ F : _ → ℂ` of
  `isForm_neg_iff_and_integral_neg` and the linear-map arrow `→ₗ[ℂ]` in the type of `Data.triLift` as premises; the
  check then requires an entry for them, so each has an entry whose `reads` says it is NOT a Lean argument. (2) In
  `Data.hasSum_inner_triLift` the check's layout reading takes the argument placeholder `(· <| …)` at the start of
  line 91 for a branch of `cases z` on line 90; step 6.1 (kind `case`) covers it, and its claim says so.
* **Anonymous instances** (TriangleLevelExponent lines 48 and 175) are annotated by id.
* **Coarse claims** in long automation steps (read first in a review): `Data.exists_isTriangle` 12–25,
  `one_square` 3–26, `exists_stdExchange_removing_planes` 12–20, `exchange_of_partners` 9–14,
  `exists_equalRankThetaRatio_value` 9.x (the first case, where all ratios vanish) and 13–18,
  `LValueData.map_trivialLift` 3.x, `Data.Pair.log_norm_map_norm_sq_trivialLift` 11–13, `Data.isHCParam_Y` 1.2.
* Import readings paraphrase quoted statement lines; members of chunks a and c used here are imports with unit
  "147" and are marked "(chunk 147-a)" / "(chunk 147-c)" in their readings.
* Nothing was sampled for a second reading.

### Letters

As in MEMORY.md and 147-a's README. Local: Π(e) = lValueProdInt(𝔠, e); ρ for an equal-rank ratio; u(i, x),
v(i, y) for the two composites of one_square.

### How it is made

The generator of 147-a, copied to `gen/` (chunk from the folder name, modules from SPLIT.md), extended by: `drop:`
for census entries marked `maybe` that refer to shadowed variables; `(-)` for an unnamed premise in `lb:`;
annotations by declaration id for anonymous instances; definitions by equations as one parent with `case`
children. Rebuild: `python3 reading/units/147-b/gen/build.py && python3 tools/rb.py check 147-b`.

2026-11-26: statement-boundary overlay (a second-reader message) applied through the generator; members whose statement has a `let` (and one equation-style member) now carry the whole statement (`statement_lines`, `statement_span`, `statement_lean_full`); see `CORRECTIONS.md`.

2026-11-26: second-reading corrections applied through the generator by the correction reader (a second-reader message with its payloads unit-147-a/b/c.md, and a second-reader message): texts, step claims and summaries in `gen/ann/*.txt`; the second reader's statement-strength verdicts (a second-reader message/0011/0012/0017/0019/0024/0032, `by_name` records) attached to the imports as `literature` records (`gen/literature.json`, written by `gen/make_literature.py`, attached by `gen/build.py`). See `CORRECTIONS.md` of the merged unit 147.

## Chunk 147-c

## Dossier 147-c: unit 147 (New/Exchange), chunk c

Reader: a Claude reader standing in for the reading agent (a fork of the reader of 147-a); see cost.json. Edition
`grh-compact`, commit 72fead102f663d5c7a407964a13dc0cf9d977207. Gate: `python3 tools/rb.py check 147-c` exits 0
(127 of 127 statements at their lines; 37 structured proofs, 299 steps, 280 leaves, longest leaf 8 lines; typed facts
24 of 24; 67 imports quoted; 690 of 690 arguments accounted for, 24 members on Lean's rule). The title and summary in
unit.json describe this chunk only (SPLIT.md rule 4); chunk a writes those of the unit.

### Modules and where to start

GridMove, RowLadder, GridFirstColumns, SteepParameters, RowsReached, CrudeRows, GridModuli, GridParameters,
LValueRatio (the order of SPLIT.md; GridModuli, GridParameters, LValueRatio are imported from other folders).

Start with `Data.crude_rows` (CrudeRows), the input of Theorem C, and read backwards:
1. `Data.exists_isTidy_integral_eq_gridPeriod`: the chain period of r(φ) is α·(grid period) of tidy data; r is onto
   because rows pair with restrictions (`Data.eq_zero_of_orthogonal_gridLevelForms`, RowsReached) and the untwisted
   descent is onto (`Data.gridLevelForms_eq_map_iotaPlus`).
2. `Data.hasRoute_succ`, `Data.gridPeriod_climb`: the climb from path 0 to path m, cost 2m² squares, using
   `Data.descent_past_gridPathMap` (RowLadder) and `Data.IsTidy.exists_square_move` (GridMove).
3. `Data.gridPeriod_eq_endPeriod`, `Data.endPeriod_mem` (GridFirstColumns): the end period as a short sum;
   `Data.exists_mul_endPeriod_mem_embValRing`, `Data.endPeriod_le`: its integrality and size.
GridMove and GridParameters hold the vocabulary (tuples, tidy data, paths, grid indices, signs, parameters).

### What I am unsure of

* **Arguments on Lean's rule (24 members)**: listed in unit.json with `binders_basis: "lean"`. Nothing is built here,
  so `#check @Name` was NOT run; each `binders_lean` says so and states the rule applied by hand. Causes: statements
  `let x := …` (the census reads them as values); bound variables or dot notation (`D.n`, `D.r`, `D.w`, `D.b`) or a
  named argument `(n := …)` taken by the census for mentions of section variables of the same name; `variable … in`.
  A reviewer with the built artifact should run `#check @Name` on these 24.
* **Tool issue (please look)**: for `Data.legDescents` and `Data.gridPathMap` the census reads the linear-map arrow
  `→ₗ[ℂ]` of the type as a premise and lists a nameless explicit argument that Lean does not have. The check requires
  every entry of the census reading (also on Lean's basis), so the dossier lists that entry and says in its `reads`
  that it is not a Lean binder (it stands for the form to which the linear map is applied). Without it the check
  reports "its `binders` leave out an argument that the declaration itself writes".
* **Coarse claims** in long automation and analytic steps: `eq_zero_of_petersson_restrict_eq_zero` steps 8–22,
  `Data.hasRoute_succ` steps 16–24, `Data.endPeriod_mem` steps 1.4–12, `Data.crude_rows` steps 12–21,
  `Data.exists_mul_endPeriod_mem_embValRing` 1.5–1.9, `Data.IsTidy.exists_square_move` 7.x–13.
* **Statement remainders as steps**: where the census reads a `let` of the statement as the start of the value, the
  rest of the statement is a step of kind `statement`.
* **Cuts and cases**: `cut 220:5@214:5` (exists_isLevelTidy_iotaPlus_eq) and `cut 151:60`
  (eq_zero_of_orthogonal_gridLevelForms) split commands of more than 8 lines; `gridParam_interlace` has one written
  case branch (the base case of an induction), as a `case` child. No `indivisible` leaf.
* Import readings paraphrase the quoted statement lines; ambient facts are stated from Mathlib's documented meaning.
* Nothing was sampled for a second reading.

### Letters

As in MEMORY.md; in this chunk also: the grids V (z false) and Z (z true), nodes (z, a, b), S a tuple of matrices on
edges, Λ, Φ data (functionals of tuples), 𝔟 = M^{b₁}, gridModulus(ϑ) = 𝔟Q, [z] = 1 for z true and 0 otherwise.

### How it is made

`gen/` holds a copy of the 147-a generator (common.py takes the chunk from the folder name and its modules from
SPLIT.md); skeleton.py here also makes `case` children for written splits and accepts targeted cuts `L:C@L0:C0`;
build.py reads `gen/ann/*.txt`. Rebuild: `python3 reading/units/147-c/gen/build.py && python3 tools/rb.py check 147-c`.

2026-11-26: statement-boundary overlay (a second-reader message) applied through the generator; members whose statement has a `let` now carry the whole statement (`statement_lines`, `statement_span`, `statement_lean_full`); see `CORRECTIONS.md`.

2026-11-26: second-reading corrections applied through the generator by the correction reader (a second-reader message with its payloads unit-147-a/b/c.md, and a second-reader message): texts, step claims and summaries in `gen/ann/*.txt`; the second reader's statement-strength verdicts (a second-reader message/0011/0012/0017/0019/0024/0032, `by_name` records) attached to the imports as `literature` records (`gen/literature.json`, written by `gen/make_literature.py`, attached by `gen/build.py`). See `CORRECTIONS.md` of the merged unit 147.

Note for the writer (a second-reader message, part c): `Data.IsShortSum.bind` (GridMove.lean 143–147) is the only member triaged `argument` without a structured proof file: its proof is the equation clause on lines 146–147, which the line census counts as statement. It takes the support W ×ˢ ⊤ of the old finite support with the whole new finite type X, so the cardinalities multiply (|W|·|X| ≤ tupleBound^n·tupleBound^k) and the exponents add; the new coefficients (c·κ∘s) have finite order when non-zero (IsOfFinOrder.mul), and the new support property is the hypothesis H on the updated tuples t∘s. `LValueRatio` (nine members) has no structured proof file: none of its theorems has more than one line after its statement.

