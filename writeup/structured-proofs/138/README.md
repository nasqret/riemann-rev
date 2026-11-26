# Unit 138: The choice of the twists: Galois representations of lifts, Selmer groups made short by one anticyclotomic twist, and congruence bounds by Ribet's method

Merged from the chunks 138-a, 138-b, 138-c by `book/plan/merge_chunks.py` (2026-11-26 10:25 UTC). Each chunk was read by its own reader (`book/plan/SPLIT.md`); their notes follow.

## Chunk 138-a

## Dossier 138-a — chunk a of unit 138 (New/Selmer, first 15 modules in import order)

> **2026-11-26, statement-boundary overlay (a second-reader message):** members whose statement contains a `let`/`have` now carry the whole statement (`statement_lines`, `statement_span`, `statement_lean_full`); the census's statement lines stopped at the binding's `:=`. Imports of such declarations quote them to their end. See `CORRECTIONS.md` of the merged unit.


Chunk a writes the title and summary of the whole unit 138 (see `unit.json`). Modules: BlocksAndCocycles,
DeterminantBound, LevelPlacesChosen, AptTupleDefs, AptTuples, HeckeStableSubspaces, Corepresentable,
ValueFamilies, LabelledColumns, BaseLevelOfLabel, ThickSpacing, CrystallineRank, CrystallineBound, HeckeString,
OnePlaceDefect. 118 members, 46 structured proofs (322 steps, 287 leaves), 374 imports with readings, 22 ambient
inputs. Gate: `python3 tools/rb.py check 138-a` exits 0 (verified, 2026-11-26).

### Where to start

1. The vocabulary of the unit is defined here: `IsColumn`, `IsRow`, `IsConjSelfDual`, `IsLabelledColumn`,
   `IsApt`, `tupleProj`, `HasRow`, `SelmerLengthLe`, `crudeUnit` (AptTupleDefs); `IsRowType`, `loss`,
   `lambdaLoss`, `blockLoss`, `crysRels` (DeterminantBound); `IsAuxiliary`, `IsFamily`, `IsAnticyclotomicAt`,
   `evenClasses`, `IsNewPlaces`, `IsPrimeTriangle`, `IsBalanced`, `IsPencil`, `tieRelations`, `IsAuxTwist`
   (Corepresentable). Their `text` fields unfold every field.
2. The arguments of the chunk: `exists_isAnticyclotomicAt` (an anticyclotomic character of order ℓ^N at one new
   prime, by Chebotarev and class field theory), `IsLabelledColumn.isRow` (labelled columns are rows),
   `exists_baseLevel` (a base level containing the image of e_c), `exists_isFamily` and
   `Data.Pair.exists_isIntegralMeasure` (families of L-values), `crystalline_defect_le` and
   `block_defect_le_at_place` (the local crystalline loss), `not_thick_of_short_arc` / `cmSign_eq_of_thick`
   (spacing of thick places).

### What a program cannot vouch for (uncertainties)

- **The English.** Claims were written from the source, the doc comments and the statements of the cited lemmas;
  no Lean was run. Several long automated steps (`simp_all`, `grind`, `grw` with long lemma lists) are described by
  what they establish, read from the surrounding statements; the exact rewriting is not reproduced. The least
  certain claims: ThickSpacing `not_thick_of_short_arc` step 1.3.1 (the power of 3 used in the case ℓ = 2),
  `cmSign_eq_of_thick` step 2, CrystallineBound steps 9.3–9.4 and 10.2, OnePlaceDefect steps 6.2.6.x, ValueFamilies
  `exists_isIntegralMeasure` steps 2.2.7.x, LabelledColumns `isRow` steps 1.3 and 1.9.2.
- **Arguments (signature rule).** 35 members carry `binders_basis: "lean"` with a list **reconstructed by hand**;
  `binders_lean` says so explicitly ("RECONSTRUCTED … Lean was not run"). Causes, all in the line census: section
  variables declared twice in a module (old instances listed), section variables whose names occur only as field
  names (`P.q`, `l.φ`, `D.t`, `O.ψ`) or as bound names (`⋃ v`, `∀ e`, `∃ ι`), statements containing `let x :=`
  (the census cuts the statement there and misses `h k j` or `ℓ`), `variable (…) in` prefixes, and instances
  needed only through elaboration (`PadicIso ℓ` for avatars, `Algebra ℤ_[ℓ] R` for `GalLattice`). For
  `pointChar` the reconstruction adds `hy` (used by `simp [*]` in the proof of multiplicativity). These lists
  should be confirmed with `#check @Name` once the artifact is built.
- **Census misreadings kept.** Where the census reads `→*` or `∀ᶠ` as binders (`blockRep`, `Data.TameChar.invAvatar`,
  `pointChar`, `block_defect_le_at_place`), the extra entries are kept (the check requires them) with a reading
  that says they are not arguments.
- **Instance variables of definitions** that the census marks "maybe" are kept or dropped by judgment of use; kept
  ones carry the note "a definition takes it only if its term uses it; not confirmed with Lean".
- **Statements cut by `let`.** For `avatar_conjGal_mul`, `isLabelledAt_avatar`, `exists_inertia_eigenvalues`,
  `exists_baseLevel`, `block_defect_le_at_place` the line census puts the start of the value inside the statement;
  the structured proofs therefore begin with a step of kind `statement` that owns the rest of the statement and
  says it is not a proof step.
- **Import order.** `New.Selmer.FitTwists` (chunk c) is imported by chunk-a modules through other units; its
  declarations used here are listed as imports with `"unit": "138"`.
- **Imports.** `uses` lists the principal artifact inputs of each step (the lemmas the claim rests on), not every
  lemma of a `simp`/`grind` set; the name-level dependencies are in the census. Import readings come from the doc
  comment and the statement of each declaration; the first reading of a name (in module order) is kept.
- **Mathlib facts** (`ambient_inputs`) are stated from their names and use; Mathlib at the pin is not checked out
  here (a local Mathlib of an older revision was consulted for Artin–Rees and `bilinearCombination`).

### Sampled for a second reading

Suggested: every step of `exists_isAnticyclotomicAt` (Corepresentable), `IsLabelledColumn.isRow`
(LabelledColumns), `exists_baseLevel` (BaseLevelOfLabel), and the texts of `IsRow`, `IsBalanced`, `IsPencil`,
`IsPrimeTriangle`, `SelmerLengthLe`.

### How it was made

`gen/build.py` emits `unit.json` and `proofs/*.json` from the census, the sources at the pin and the reader's
annotations `gen/ann/m00…m15_*.py` (texts, binder readings, step trees with claims, import and ambient readings).
Lines, hashes, quotations, written intermediate types, spans and import quotations are computed from the sources;
`tools/rb.py check 138-a` (which shares no code with the generator) is the independent check.

## Chunk 138-b

## Dossier 138-b — chunk b of unit 138 (New/Selmer, modules 16–23 in import order)

> **2026-11-26, statement-boundary overlay (a second-reader message):** members whose statement contains a `let`/`have` now carry the whole statement (`statement_lines`, `statement_span`, `statement_lean_full`); the census's statement lines stopped at the binding's `:=`. Imports of such declarations quote them to their end. See `CORRECTIONS.md` of the merged unit.


Chunk b writes the title and summary of its chunk (see `unit.json`; the unit's own title and summary are in
`138-a`). Modules: RootsOfUnityPoints, LinePointPowers, TiltingLemma, TwistTheorem, RowBalanced, RibetCramer,
RibetFirstOrder, TateTwistSteps. 30 members, 22 structured proofs (337 steps, 320 leaves), 112 imports with
readings (39 of them declarations of chunks a and c, listed with `"unit": "138"`), 21 ambient inputs.
Gate: `python3 tools/rb.py check 138-b` exits 0 (verified, 2026-11-26).

### Where to start

1. Roots of unity at which polynomials keep their valuations low: `exists_root_of_unity_eval_large`,
   `exists_roots_of_unity_ellVal_le` (RootsOfUnityPoints); the mirror lemma `card_le_torsion_of_isotropic` and
   `exists_sharp_fitting_poly` (LinePointPowers).
2. Pencils and ties: `IsPencil.length_le_of_drop_ties`, `IsPencil.length_le_of_unseen_class` and `tilting`
   (TiltingLemma); `exists_isPencil` and the twist theorem `exists_anticyclotomic_twist` (TwistTheorem).
3. Balanced rows: `inClass_of_isLatticeIn`, `relLength_obeyingCocycles_le`, `IsRow.eventually_isBalanced`
   (RowBalanced).
4. Ribet's method to first order: `exists_ribet_element_cramer` (Cramer's rule twice, RibetCramer);
   `HasTriangleCost`, `IsTraceIdeal`, `IsRibetElement`, `exists_mem_fittingIdeal_block`, `ribet_first_order`
   (RibetFirstOrder); `hasTriangleCost_tateTwist` (TateTwistSteps), which supplies `HasTriangleCost` for Tate twists
   from `IsPrimeTriangle`.

### What a program cannot vouch for (uncertainties)

- **The English.** Claims were written from the source, the doc comments and the statements of the cited lemmas;
  no Lean was run. Long `simp`/`grw`/`linear_combination` steps are described by what they establish. Least certain:
  `ribet_first_order` steps 25.3.x, 30.x, 35 and 38; `IsRow.eventually_isBalanced` steps 10.4–10.9 and 12;
  `relLength_obeyingCocycles_le` steps 12–14 (the cup-product orthogonality); `hasTriangleCost_tateTwist` step
  3.2.3.3; `IsPencil.length_le_of_unseen_class` (the mirror argument).
- **Arguments (signature rule).** 7 members carry `binders_basis: "lean"` with a list **reconstructed by hand**
  (`binders_lean` says "RECONSTRUCTED … Lean was not run"): the four `IsPencil.*` lemmas of TiltingLemma and
  `ribet_first_order` (modules that declare the same variables in two `variable` blocks: the census lists the
  instances of the first, shadowed block), `IsRow.eventually_isBalanced` (the same, and `u` occurs only as the
  variable bound by `∃ u`), `inClass_of_isLatticeIn` (statement cut at `let v :=`; Lean takes ℓ, O, n, `PadicIso ℓ`
  and u). To be confirmed with `#check @Name`.
- **Instance variables of definitions marked "maybe".** Dropped: `[DVR O]` of `HasTriangleCost` and `[Group G]` of
  `IsTraceIdeal` (their terms do not use them), and the first-block instances of `IsTraceIdeal`, `IsRibetElement`
  (over shadowed variables). Kept ones carry the note of the generator. Not confirmed with Lean.
- **Census misreadings kept** with a reading saying they are not arguments: `ribetNormaliser` #10 (the arrow of
  `G →₀ R`), `IsRow.eventually_isBalanced` #21–#22 (`∀ᶠ O … in .atTop`).
- **Statements cut by `let`.** `IsPencil.pointChar_idOrConjInv`, `IsPencil.length_le_of_drop_ties`,
  `IsPencil.length_le_of_unseen_class`, `exists_isPencil`, `inClass_of_isLatticeIn`, `relLength_obeyingCocycles_le`
  begin with a step of kind `statement` that owns the rest of the statement and says it is not a proof step.
- **Leaves over 8 lines** (indivisible, with the reason in the step): `exists_roots_of_unity_ellVal_le` step 7 (one
  `choose … using` whose argument is a single term), `IsPencil.length_le_of_unseen_class` step 1.17 (one
  `grw … at h₁`).
- **Imports.** `uses` lists the principal artifact inputs of a step, not every lemma of a `simp` set. Import readings
  come from the doc comment and statement; for chunk-a declarations the readings of `138-a` were reused.
- **Mathlib facts** (`ambient_inputs`) are stated from their names and use; Mathlib at the pin is not checked out.

### Letters (rule 5)

The texts use the binder names of each Lean statement as local letters. Clashes with the fixed letters of
`MEMORY.md`, local to this chunk: N (a submodule or a finite type in RibetCramer/RibetFirstOrder, not the level),
K (a property of polynomials, an index type, a submodule; not ℚ(√−d)), t (the number of characters ξ_e or of twists
in RibetFirstOrder/TateTwistSteps; RowBalanced's t is the row's), a (an element of G), c (a coefficient or a cost),
x (points of Y), r (a finite type in RibetFirstOrder), f (Ribet's element f ∈ S; in RowBalanced f is f(D)).
New letters: Λ = O[X_J], 𝒥 (the trace submodule), 𝓧 and π ∈ 𝓧, ϵ : r ⊕ Fin t ≃ σ, ω (the normaliser vector), 𝔮
(polynomials without monomials ≤ ∏X_j), U(g), κ, μ, χ_x, ψ_x, η_e, ψ₀, B₀, Γ_e, 𝔞 (a left ideal of O[G]).

### Sampled for a second reading

Suggested: every step of `ribet_first_order` and `exists_ribet_element_cramer`; `IsRow.eventually_isBalanced`;
`hasTriangleCost_tateTwist`; the texts of `HasTriangleCost`, `IsTraceIdeal`, `IsRibetElement`.

### How it was made

`gen/build.py` emits `unit.json` and `proofs/*.json` from the census, the sources at the pin and the annotations
`gen/ann/m00…m08_*.py` (texts, binder readings, step trees with claims, import and ambient readings); it falls back
on `../138-a/unit.json` for readings of chunk-a declarations. Lines, hashes, quotations, written types, spans and
import quotations are computed from the sources; `tools/rb.py check 138-b` is the independent check.

## Chunk 138-c

## Dossier 138-c — chunk c of unit 138 (New/Selmer, the last 9 modules in import order)

> **2026-11-26, statement-boundary overlay (a second-reader message):** members whose statement contains a `let`/`have` now carry the whole statement (`statement_lines`, `statement_span`, `statement_lean_full`); the census's statement lines stopped at the binding's `:=`. Imports of such declarations quote them to their end. See `CORRECTIONS.md` of the merged unit.


Modules: RibetElement, ReciprocityLaw, TrianglePrimes, DenominatorBound, FitTwists, RowsExist, TwistForRows,
FitTwistsExist, RankOneDenominator. 57 members (every declaration of these modules that the proposal puts in unit
138), 28 structured proofs (432 steps, 368 leaves, longest leaf 7 lines, no `indivisible` exception), 51 of 51 typed
facts, 338 imports, 168 ambient inputs. Gate: `python3 tools/rb.py check 138-c` exits 0 (verified 2026-11-26).

| module | members | structured proofs | steps | leaves |
|---|---|---|---|---|
| RibetElement | 5 | 4 | 91 | 78 |
| ReciprocityLaw | 6 | 2 | 88 | 77 |
| TrianglePrimes | 1 | 1 | 63 | 55 |
| DenominatorBound | 2 | 2 | 74 | 61 |
| FitTwists | 33 | 11 | 32 | 26 |
| RowsExist | 2 | 2 | 27 | 25 |
| TwistForRows | 1 | 1 | 21 | 18 |
| FitTwistsExist | 1 | 1 | 21 | 16 |
| RankOneDenominator | 6 | 4 | 15 | 12 |

### Where to start

1. `exists_isFitFamily` (FitTwistsExist), the end point of unit 138: for all P and admissible data D there is
   θ : PrimePadicIso → D.MFoldTwist with `D.IsFitFamily θ`. Its `text` unfolds the three fields of `Data.IsFitFamily`
   (FitTwists lines 256–263): coprime, denominator_le (with `DenominatorLe`, `goodLift`, `B₀`, `IsRankOne`,
   `lValueData`, `trivialLift`), height_le (`IsRamified`, `ratio`, `HeightLe`).
2. The vocabulary of FitTwists: `DenominatorLe`, `AuxPair.IsTested`, `AuxPair.IsTestForm`, `AuxPair.groupAlgAction`,
   the Hecke algebra away from g (`Data.heckeAlgebra`, `heckeOperator`, `eigenPart`, `iSup_eigenPart`), the auxiliary
   lifts (`exists_theta_to_principalForms`, `auxLift`, `goodLift`), pairs (`IsRamified`, `IsRankOne`, `RankOneIndex`), `B₀`.
3. The chain behind the denominator clause: `denominatorLe_rowBudget` (DenominatorBound) uses `ribet_columns` and
   `sum_blockLoss_le` (RibetElement), `exists_isPrimeTriangle` (TrianglePrimes), which uses `exists_isLaw`
   (ReciprocityLaw). The rows come from `exists_row_for_all_twists` and `exists_hasRow_auxPair` (RowsExist), the twist
   from `exists_mFoldTwist_selmerLengthLe` (TwistForRows). `DenominatorLe.rank_one_bound` (RankOneDenominator) is not
   used by `exists_isFitFamily`; it is used in New/Rows/HeckeValueHeight.lean (another unit).

### The signature rule: members that need `#check`

Lean was not run (the artifact is not built here), so no member carries `binders_basis: "lean"`. Every `binders` list
is the line census's list, as the check requires; where the census misreads the text, the entry is kept and its
`reads` says that it is not an argument (or which argument is missing), "to be confirmed with #check". The `text` of
each member states the mathematics with Lean's presumable arguments. Members to confirm with `#check @Name`:

- Section variable read from a field name or a bound name (Lean presumably does not take it):
  `IsSplitPlace`, `IsLaw` (#7 `w`), `exists_isLaw` (#6 `w`) — `w` occurs only as the field `x.w`;
  `AuxPair.IsTested` (`w`, `hw`, `hS`, bound by the definition's own `∀ w hw hS`); `Data.heckeAlgebra` (`E`, `s`, `V`,
  `p`, `y`); `Data.heckeOperator`, `Data.eigenPart` (`E`); `Data.occurringLabels` (`E`, `y`); `Data.heckeOnGood` (`E`,
  `p`, `y`); `Data.isSphericalWith_of_mem_eigenPart`, `Data.commute_heckeAlgebra_principalRep`,
  `Data.principalRep_mem_eigenPart` (`E` and its three instances); `Data.exists_hecke_proj_eigenPart` (`E`, three
  instances, `s`, `V`, `y`); `Data.finite_eigenPart`, `Data.iSup_eigenPart` (`E`, three instances, `p`);
  `Data.Pair.IsRamified` (`w`); `Data.Pair.IsRankOne` (`w`, `r`); `Data.IsFitFamily` (`ℓ`, `ι`, `e₀`, `s`, `p`, `E`,
  `r`, `n`, `O`, `j`: Lean presumably takes only `{P} (D) (θ)`). Here `E` occurs only as the field `D.E`.
- Instances of shadowed section variables: `AuxPair.theta_mul_eq_theta_formAction` (#1–#5, the instances of the
  `{E r n}` of line 28, shadowed by those of line 199).
- Arrows read as premises: `Data.heckeOnGood` (#11, the arrow of `→*`), `Data.auxLift` (#5, the arrow of `→ₗ[ℂ]`).
- A filter quantifier read as binders: `sum_blockLoss_le` (#26 `ᶠ`, #27 `O`, and #28–#35, which lie inside
  `∀ᶠ O : CoeffRing ℓ in atTop` and are part of the conclusion).
- Arguments the census misses: `Data.dvd_card_resField_sub_one` (the statement begins with `let q :=`; Lean also takes
  `{P}` and the section variable `(D : Data P)` before `x`); `exists_row_for_all_twists` and `exists_hasRow_auxPair`
  (the statements use `ιℓ`, so Lean takes the section variables `{ℓ} [ThePrime ℓ] (ι : PadicIso ℓ)`; the calls
  `exists_row_for_all_twists ι …` and `exists_hasRow_auxPair ι …` in FitTwistsExist confirm the explicit `ι`).
- Instance variables of definitions that the census marks "maybe" are kept where the definition uses them (their
  `reads` say "not confirmed with Lean") and dropped where they sit on a variable the definition does not take.

### What a program cannot vouch for (uncertainties)

- **The English.** Claims were written from the source, the doc comments and the statements of the cited
  declarations; no Lean was run. Automated steps (`simp`, `grind`, `grw`, `simpa using!`) are described by what they
  establish, read from the surrounding statements. Least certain claims, by proof:
  `ribet_columns` 12.1.1.3, 16.5, 16.9, 16.10, 16.16 and 17–20 (the arithmetic of the final bound ?H);
  `sum_blockLoss_le` 9.3.1, 10, 11; `isTraceIdeal_withConjInv` 1.1.4;
  `exists_isLaw` 7.2, 9, 29.11–29.12, 29.14.3, 29.19, 33.3, 33.4.3, 33.4.6.2.1;
  `exists_isPrimeTriangle` 5, 13.9, 13.10.3, 13.12.4, 13.14, 19.3;
  `denominatorLe_rowBudget` 9, 20, 22.2.3, 23, 29.5, 34.4.1.5; `exists_cycChar_pow_sub_one_dvd` 1.1.3;
  `exists_row_for_all_twists` 2.2.4–2.2.9 (the Frobenius computation); `exists_hasRow_auxPair` 8, 12–14;
  `exists_mFoldTwist_selmerLengthLe` 9, 13.2; `exists_isFitFamily` 1.3, 4.1.4, 4.1.7;
  `DenominatorLe.rank_one_bound` 3.2.3; `AuxPair.theta_mul_eq_theta_formAction` 2.
- **Imports.** 211 of the 338 import readings are the statement in words that another dossier of the workspace gives
  for the same declaration, taken by name (each such import says so in `reading_from`); the others were written from
  the doc comment and the statement. `uses` lists the principal inputs of each step, not every lemma of a `simp` set.
  Imports from chunks 138-a and 138-b carry `"unit": "138"` (the merge drops them).
- **Mathlib facts** (`ambient_inputs`, 168) are stated from memory and from their use; Mathlib at the pin 56a00585 is
  not on this machine.
- **Unifier-chosen values.** In `denominatorLe_rowBudget` the exponent j left open by `W _ .univ` and the constant c₀
  are fixed later by unification; the claims give the values read from `ribet_columns`'s statement and the comment.

### Letters

The letters of MEMORY.md and of 138-a (ℓ, ιℓ, Ω, Gal(Ω/E), ℚ̄_ℓ, E⁺, cyc, v_ℓ, cr_ℓ = crudeUnit ℓ D, Mk = chosenGroupOrder,
h₂, f, …). The RibetElement and DenominatorBound texts write D.h₂, D.f, D.chosenGroupOrder and crudeUnit ℓ D in full.
New letters, all local to proofs: t_V = V.rankDiff, X_D (the integer of exists_length_shaOdd_le in rowBudget), O′, T_x,
u′_x, F_x, z, δ_k, o_k, B_g, b₀, b_e, C = ℓ^{h₂h}, p₀ = ℓ^{m₀}, ω (RibetElement); res, c₀, p, κ, ρ, V, M, A, Y(P′), Z,
W = M[ℓ], K_ψ, γ₀, 𝒲, x′, n₀, s′ (ReciprocityLaw); p, J, κ, m, H, I(j), f(j) = (x_j, T_j, z_j), B_b, v_b, y_b, w₀, u, c_b,
P_d, δ, σ, σ₀, g(i) (TrianglePrimes); e₀ (Lean's `E`, a group-algebra element, not the field), A, x₀, N_x, 𝓧, R_x, M_x(θ),
P_z, z′, Q′, a₁, E_s, G, J₀, c₀, b (DenominatorBound); γ(ℓ) = rowBudget D ℓ·log ℓ, R(j, q), R′(p, j), τ_κ (FitTwistsExist);
T = twistedCentralOp, s_c, h′ (RankOneDenominator).

### Sampled for a second reading

Suggested: every step of `exists_isFitFamily` and of `denominatorLe_rowBudget`; the texts of `Data.IsFitFamily`,
`DenominatorLe`, `AuxPair.IsTested`, `IsLaw`, `exists_isPrimeTriangle` (its text unfolds `IsPrimeTriangle` and
`TaylorWilesPlaces`), `ribet_columns`; steps 1–6 and 29 of `exists_isLaw`, 16.x of `ribet_columns`.

### How it was made

Five hands, one generator. The 138-c reader set up `gen/` (adapted from 138-a's generator) and wrote `gen/ann/m00`,
`m05`–`m09` (FitTwists, RowsExist, TwistForRows, FitTwistsExist, RankOneDenominator); four forks of the same reader,
working in parallel, each wrote one annotation file: `m01` RibetElement, `m02` ReciprocityLaw, `m03` TrianglePrimes,
`m04` DenominatorBound. `gen/build.py` emits `unit.json` and `proofs/*.json` from the census, the sources at the pin and
the annotations (lines, hashes, quotations, written intermediate types, spans and import quotations are computed;
words come from the annotations). `gen/partcheck.py MODULE` builds a partial dossier into a scratch folder outside the
workspace and runs the workspace's own check on it, so the hands could check their modules without touching this
folder. `gen/show.py NAME` prints a declaration with the readings other dossiers give. `tools/rb.py check 138-c`, which
shares no code with the generator, is the independent check.

