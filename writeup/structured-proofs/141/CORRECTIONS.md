# Corrections to the dossier of 141 (The seesaw identity for the chain of theta lifts, and the index types of the data)

## 2026-11-26 — statement-boundary overlay (a second-reader message)

Source: the second reader's a second-reader message (`exchange/to-claude/a second-reader message/statement-range-inventory.json`, sha256 1749e406…). The census ends a statement at its first top-level `:=`; in the members below that `:=` belongs to a `let`/`letI`/`have` inside the type (or, where said, the census runs into an equation-style proof), so the census's statement lines stopped before the conclusion. Each declaration was read in full at the pin and the overlay's span confirmed (it ends just before the declaration's own `:=`). Applied by the generator: `gen/gen.py` (in main, before unit.json is written) calls `gen/statement_overlay.py`, which gives each listed member `statement_lines` (corrected), `statement_span` (span + SHA-256), `statement_lean_full` (the whole statement) and `statement_basis`, removes a truncated `statement_lean` (`rb.py check` compares `statement_lean` with the census's lines and refuses a longer quotation), and extends the quoted lines of imports to the end of their statements.

### Members (statement lines census → corrected; conclusion old → new)

- `integral_theta_eq_lift₂` (New.Seesaw.DoubleLiftValue:27:7; assignment inside type): lines 27–29 → 27–32. Old quotation stopped at `let L o := …; ∃ t'', ∀ o y φ g, ∫ x,` (line 29). Text already complete: ∃ t″ ∀ o y φ g, ∫_{[U(X)]} algFormCoeff(1, t, φ)(x)·∫_{[U(X′)]} θ(tripleWeil(a(o), b(o))(x, r, g)(…)) = algFormCoeff(1, t″, L(o)(y)(φ))(g) → unchanged.
- `ArrowPair.integral_constTermAtT_mul` (New.Seesaw.DoubleLiftValue:58:7; assignment inside type): lines 58–59 → 58–63. Old quotation stopped at `let F g r := …` (line 59). Text already complete: ∫_{[B′]}∫_{[B]} F = ∫_{[U(X)]} P(inclX(g)t)·(z·∫ θ(tripleWeil(a, b)(g, r, embX k)(zeroTerm(…)))) → unchanged.
- `mul_apply_string_of_blockTriangular` (New.Seesaw.EqualLinesOrbit:24:7; assignment inside type): lines 24–26 → 24–27. Old quotation stopped at `letI i := e (.inr a);` (line 26). Text already complete: (A·B)_{ii} = A_{ii}·B_{ii} → unchanged (no structured proof: one-step).
- `Grading.IsAdaptedAt.gram_string_entry` (New.Seesaw.EqualLinesOrbit:54:7; assignment inside type): lines 54–55 → 54–56. Old quotation stopped at `letI k := (b⁻¹ * (V.xFin * y))⁻¹.1` (line 55). Text already complete: (kᴴk)(f(i), f(j)) = J_V(f(i), f(j))·(β̄_i β_j) → unchanged (no structured proof: computation).
- `Grading.exists_integral_eq_sum_over_cut` (New.Seesaw.IntegralAsCosetSum:67:7; assignment inside type): lines 67–69 → 67–73. Old quotation stopped at `let f :=` (line 69). Text already complete: ∃ κ, for all P, y, J, T, b: the five hypotheses (generic, automorphic, integrable, stable T, multiplicities, the [B]-integrals) → ∫_{B(E⁺)\G} f = κ·∑_{t∈T} b(t)/coverMultiplicity(…) → unchanged.
- `IsSplitLevel.LiftLaw.u₀_charDatum_eq_fourierOp` (New.Seesaw.NamesAtSplitLevel:212:7; assignment inside type): lines 212–213 → 212–215. Old quotation stopped at `let C := π'.ρ Λ.diagNInv (…)` (line 213). Text already complete: C = fourierOp(π′)(L[𝐛_e]φ) ∧ C = γ·L[𝐛_e](fourierOp(π)φ) → unchanged.
- `Data.exists_stage_cut` (New.Seesaw.SeesawTheorem:39:7; assignment inside type): lines 39–39 → 39–43. Old quotation stopped at `let Y := gradingY k hk;` (line 39, the whole statement being five lines). Text already complete: ∃ A, IsLevel A ∧ columnLevel(k) ≤ inclXFin⁻¹(A) ∧ ∀ ϑ ∃ T with (i) stability, (ii) integrality off n (and chosenLevel for k = 0), (iii) coverMultiplicity ∣ n^j → unchanged.

### Proof steps and summaries

- The five proofs of these members own the statement tails by `intro_lines` (no claim). The summaries of integral_theta_eq_lift₂ (intro 29–32) and IsSplitLevel.LiftLaw.u₀_charDatum_eq_fourierOp (intro 213–215) now say that these lines are the rest of the statement; the other three summaries already said so.

### Imports re-quoted to the end of their statements

- `Filling.Fits.integral_poincare` (unit 148): lines 143–144 → 143–145. Text was complete; now names F = y·poincare(X, φ, Δ) (the `let`) and the hypothesis V.IsForm(q, y).
- `Grading.integral_besselGroup_unfold` (unit 28): lines 359–359 → 359–361. Text gave the identity only in words; now states F = unfoldStep(Y, Y′, α, Φ, P, x)·y, Integrable F and the full equality of the [B]-period with ∫_{B′(E⁺)\G′} F.
- `Grading.integral_besselMeasure_eq_of_mean` (unit 28): lines 112–113 → 112–117. Text already complete (the `let row` is the coordinate map c·(n − 1)_{v,X}); unchanged.
- `integral_algFormCoeff_blockEmb` (unit 27): lines 151–152 → 151–156. Text was a summary; now the full statement (j = blockEmb(hσ) from the `let`; ∃ C ∀ ψ Φ u L K, IsAutomorphic Φ → Φ(x, g) = L_g(conjWeylRep(κ₀, e₀)(x)c) → the integral identity).
- `integral_quotMeasure_stages` (unit 114): lines 41–44 → 41–45. Text was complete; now names f (the `let`) and the hypothesis that F is measurable.
- `theta_tripleWeil_rat_mul` (unit 43): lines 155–155 → 155–156. Text was complete in substance; now states F(γg, δg′, k) = F(g, g′, k) for γ ∈ Γ_V, δ ∈ Γ_{V′}, with F from the `let`.

### Not applied

- Nothing: every overlay span of this dossier was confirmed by reading the source.

### Digests and check

- dossier digest (`dossier_sha256`): old `c9d80597d00991db4f078baab46f662e76f11c451dad078e448d1b60c18677ba` → new `1f4c5205f58737c7e76387457ff1475d84538aa09705ce9a22ca9672684837d6`
- `python3 tools/rb.py check 141`: exit 0 — unit 141: 312 of 312 statements at their lines; 83 structured proofs, 550 steps, 503 leaves (longest 8 lines, bound 8), 550 steps quote their lines; typed facts in the source: 68 of 68; imports quoted: 74 of 74; arguments accounted for: 3066 of 3066


## 2026-11-26 — second reading (a second-reader message, a second-reader message) and literature

Correction reader: a Claude agent (Opus 5.5), the only writer of this folder during this pass. Messages applied:
a second-reader message (the second reading of 141: six corrections to the seesaw argument and six bullets elsewhere), a second-reader message (the
reading of `Data.seesaw`), the `by_name` verdict for the one import of this unit that cites a named classical result
(a second-reader message `part-1-named.json`, the same row in a second-reader message `strength-classfield-local.json` and a second-reader message
`part-1-named.json`), and six findings of the writer of the notes passed on by the coordinator (own sub-heading below).
Every change was checked against the pinned source (`lsernau/grh-lean` @ `72fead1`, `grh-compact/src`) before it was
applied; nothing was built. The changes were made in the generator inputs (`gen/m_*.py`, `gen/meta.py`; `gen/gen.py`
now carries an import's optional `literature` record into `unit.json`) and the dossier was emitted again with
`python3 reading/units/141/gen/gen.py`.

### a second-reader message, the seesaw argument (old → new)

1. `Grading.exists_integral_eq_sum_over_cut` step 14 (IntegralAsCosetSum.lean 102–107): "split on whether t_f ∈ T; ψ
   is invariant under B_f" → the split is on m(t_f) = coverMultiplicity(B_f, A, T, t_f) ≠ 0 (the branch hypothesis
   `m` is what `measure_union_cosets` needs at line 106); in ψ(u⁻¹t_f) = 1_T(u⁻¹t_f)/m(u⁻¹t_f) only the denominator is
   B_f-invariant (`coverMultiplicity_smul`), the numerator only (B_f ∩ A)-invariant; m = 0 makes the integrand 0.
   Step 13: "the value required at t" → the cutoff identity ∫ψ(u⁻¹t_f)dη = 1 if m(t_f) ≠ 0, else 0 (the indicator of
   step 6.1, lines 82–86), which with hs is 1 on the support of f, also at points with t_f ∉ T. Step 15 and the proof
   summary: the same. `coverMultiplicity` text: + the count is of cosets in S/(S ∩ A) with some representative r,
   r⁻¹t ∈ T (lines 16–17); representative-independent when T is (S ∩ A)-stable.
2. `Data.exists_isAdmissibleComb_unfolding` step 3: "columnLevel(k) ≤ A (hA′)" → columnLevel(k) ≤ inclXFin_Y⁻¹(A)
   (SeesawTheorem.lean 39–40): the image inclXFin_Y(b) lies in A. Step 10: "b_k ∈ columnLevel(k) ⊆ A" → the image
   inclXFin_Y(b_k) lies in B_f and in A by hA′ (line 124). Text (iii): "the integrable product F … has ∫F = …" → with F
   = unfoldStage(…)·z (the `let`), integrability of F implies the period identity (lines 87–89); the hypothesis does not
   assert integrability; κ comes before ϑ, M, S. Step 7.1: + G is applied to the integrability given by
   `integral_besselGroup_unfold` (lines 110–112). `Data.exists_stage_cut` text: + A comes before ϑ, each ϑ has its own
   cut, the image formulation, and "as n ≥ 1 such a multiplicity is non-zero".
3. `Data.exists_isAdmissibleComb_reducedVacuum` steps 3 and 3.4: "x ∈ translations(q, π̄_g)" → translations(q, π_g):
   the weight is `star D.piGBar` (GoodDatumExists.lean 49), and `piGBar` is already the conjugate (IndexTypes.lean 37).
   Step 3.1: + g = π̄_g names the initial datum (line 51), its translations have conj(g)·x = π_g·x integral. Step 5:
   "lies in translations(q, π̄_g)" → lies in weightedTranslations(q, selfOrConj(π̄_g)): π̄_g on the conjugated first
   block, π_g on the second (lines 71–74; the input set of `IsAdmissibleEval`, AdmissibleEvaluation.lean 67–72);
   "size 1" → size at most 1 when Q = ∅.
4. `Data.exists_isAdmissibleComb_reducedVacuum` text: "for every twist ϑ" → for every tame character ϑ (the statement
   binds its own ϑ, typed by `levelNorm` and `evaluatedDatum`, GradingsOfY.lean 19, 216–222; `ϑ.7` at line 69 is the
   coprimality field, IndexTypes.lean 186–192); one C for all tame characters, denominator cutBound^{2m}, m = 2ϱ + 2;
   non-triviality on Q enters only with `Data.Twist`. Step 2: "fix ϑ" → fix a tame character ϑ. Step 8.1: "translateDatum
   (t, ·) is linear in the scalar" → for a fixed translation heisFinPart(t_j) is linear in the datum it acts on, so
   translateDatum(t, j) = κ₀^{rank}·heisFinPart(t_j)(vac) (line 80; CrudeModularData.lean 52–53, IntegralVacuum.lean 49).
   `Data.TameChar` text: + a tame character may mark a place of Q with trivial tame part (lines 186–199).
5. `Filling.Fits.poincare_bessel_normal_form`, `Filling.Fits.isGeneric_poincare`: "columnCoords(ψ)" → h.columnCoords(ψ),
   the coordinate map of arbitrary fitting data h, not D.columnCoords (BesselGeneric.lean 27–28, 58–62, 101–102);
   "⟨A(…), W(x_∞)⟩" → the bilinear dot product A(…) ⬝ W(x_∞) (`⬝ᵥ`, line 62); genericity = the three conditions of
   `Grading.IsGeneric` (FiniteBesselGroup.lean 48–52). Steps 4 (normal form) and 1.2 (isGeneric): the same dot product.
   `Data.unfoldStage` text: "columnCoords(φ)" → D.columnCoords(φ), φ translated by latticeScale(0) first
   (UnfoldingStages.lean 22–23). `Data.unfoldStage_even` step 11.1: + the generic normal form is applied to the
   translated column centralRep(latticeScale(0))(φ) (lines 56–60).
6. `IsAdmissibleComb.normUnit_smul` text: "So the scalar d/C clears both the factor C and the denominator d" → that holds
   when a·C ≠ 0; when a·C = 0 the output vector is 0 (normUnit(0) = 1; e.g. a = 0, d = C = 1, z ≠ 0), no hypothesis
   a·C ≠ 0 (AdmissibleComb.lean 79–83).

### a second-reader message, elsewhere in the unit (old → new)

7. `IsSplitLevel.pairWeilFinite_name` text: "name(liftFn(S ↦ f(k⁻¹·S·g)))(v)" → name(S ↦ f̃(k⁻¹·S·g))(v), f̃ = liftFn(f)
   the local lift (NamesAtSplitLevel.lean 119–121, 430–432: `liftFn f <| k⁻¹.1 * · * g.1`); the factors in the source's
   order. Step 1: f(k⁻¹Sg) → f̃(k⁻¹Sg). `IsSplitLevel.translateSum_eq_sum_name` step 15: "only the term y = b is
   non-zero" → every term y ≠ b is zero (`Fintype.sum_eq_single`, line 514); the term y = b may vanish (step 16, the
   case split of line 515).
8. `residueOverN`, `residueOverN_apply` texts: + any natural N; representatives {0, …, N−1} for N > 0; N = 0 gives the
   zero adele (lines 33–38). `IsSplitLevel.exists_sub_residueOverN_mem_iff` text: + b is the reduction of Nz when Nz is
   integral at P; otherwise the equivalence holds for any b (lines 467–472).
9. `Grading.IsAdaptedAt.gram_string_entry` text: "(the Gram matrix of x_f·y is J_V)" → h = x_f·y has hᴴJ_Vh = 1
   (FiniteBesselGroup.lean 141; EqualLinesOrbit.lean 57), so k = (b⁻¹h)⁻¹ has kᴴk = bᴴJ_Vb, and triangularity leaves
   J_V(f_i, f_j)β̄_iβ_j for j ≤ i^rev.
10. `Data.lastResLevel` text: "(unrestricted at the places of Q)" → the full block parabolic at Q, 1 at the chosen places
    (GradingsOfY.lean 98–99). `card_parabolic_blockNumber` text and steps 1.2, 1.2.3: "every finite commutative ring R" →
    every commutative ring R, a `Nat.card` identity with one k (lines 163–173); the finite count is a special case.
11. `exists_branching_pairing` text: "⟨v′, B·v⟩" → the bilinear v′ ⬝ (B·v) (`⬝ᵥ`, PairTensorData.lean 26–32), also after
    the Weyl action and in the class integral; the bound in the norms of the positive definite Weyl Gram form; c_g after
    the quantifier over g and before V, η, φ, u, K, factor c_g/[K₀ : K], c_g = 0 allowed. `Data.exists_indexDvd_fourierOp_pow`
    text: "preimage … dim(columns)" → the pullback by F^{ϱ+1} of the lattice at diagPointN(0), dim_ℂ Column(D)
    (LiftCharacters.lean 128–131; the reading was already right, the wording is made exact).
12. `IsAdmissibleEval`: the text no longer lists the section's finite type q; the q of `∀ n q` is the proposition of the
    size bound (AdmissibleEvaluation.lean 67–72); the binder entries `q : Type` and `[Fintype q]` are now marked
    "listed by the text reading only, text-inferred pending Lean's elaborated signature". `isAdmissibleEval_finEval` text:
    hA and hM written out (lines 167–171): a zero entry or equal valuations at every place; integral frame coordinates
    of both components of the scaled embedded neighbour vector, under s(a/ā) = ε̄δ and ts = 1.
    `exists_isAdmissibleEval_std` step 15.6: "the single term y = b" → at most the term y = b is non-zero, and all terms
    vanish off the box (lines 133–139).

### a second-reader message, the reading of `Data.seesaw` (old → new)

13. `Data.seesaw` text: "a non-zero complex number c … a good datum Ψ … for every ramified column φ" → a unit c ∈ ℂˣ
    chosen before the twist quantifier (depends on D only), a finitely supported Ψ : Translations(D) →₀ ℂ with
    IsGoodDatum(ϑ, Ψ) (glossed from ChainValuation.lean 267–279), the identity for every element of ramifiedColumns,
    φ = 0 included, with no shortness, integrality or non-vanishing condition (SeesawTheorem.lean 135–136,
    ChainValuation.lean 197–202); + the level-index scalars of the lifts, the factor ∏_τ τ(π̄)^{−branchExp(τ)} of
    restrictToY (ColumnDefs.lean 91–93), no bound on |c|. Unit summary (`gen/meta.py`): the same.
14. `Data.seesaw` summary and steps 1, 3, 4: c = normUnit(a·C/cutBound^{2m}) is a unit also at 0 and clears the
    constants only when a·C ≠ 0; C serves all tame characters; T(ξ) is independent of ϑ, φ, y (UnfoldingStages.lean 40);
    a comes before the quantifiers over ϑ, M, S, with denominator 1 and size cutBound^m (lines 140–141). Step 5: "it is
    the paired chain of a good datum Ψ" → w′ = normUnit(…)·a·w is a vector of finite data (denominator 1, size
    cutBound^{3m}; normUnit_smul needs only cutBound^{2m} ≠ 0), and the paired lift applied to w′ and φ equals
    chainComb(ϑ, Ψ, translateDatum, m)(φ) (GoodDatumExists.lean 121–126).
15. `Data.seesaw` step 7: "⟨Ξ, R(liftChainY(𝒫(cφ)))⟩ = ⟨Ξ, R(chainComb(Ψ)(φ))⟩" → ⟨Ξ, liftChainY(ϑ, m)(𝒫(c·φ))⟩ =
    ⟨Ξ, R(paired lift of w′ applied to φ)⟩: the Y-chain is paired with Ξ directly, R (defined on forms of X_m,
    `D.Stage M`, DegreeBounds.lean 18–22, ColumnDefs.lean 74) acts on the definite chain; the unfolding tests against
    conj(Ξ) (lines 145, 152–154).

### Literature

16. Import `AutChar.exists_hasWeight_of_prod_eq_one` (CharacterConjugates.lean 82–83): text "A unitary character … exists,
    provided the product … is 1 on every global norm-one unit" → the full statement (CM type Φ_v, S, ψ with hS, the
    criterion h on integral u with uū = 1, HasWeight(μ, e, ψ) as in CharacterDefs.lean 56–59); + a `literature` record:
    relation unresolved, verdict "The cited full idèle-class character existence result has a different domain and
    compatibility condition", sources Weil (Tokyo–Nikko), Raghuram §3.1 Prop. 13 and §4.3.2 Prop. 25, the pinned
    definitions; statement_range [82, 83]; catalogue row add71b50…. The first reading's import text gave no relation;
    the record replaces the catalogue's earlier "special case (Raghuram §4)" (the row's `catalogue_row_at_review`), and
    the text now says the relation is the second reader's. No other import or member of 141 has a `by_name` row in
    a second-reader message, 0011, 0012, 0017, 0019, 0024, 0032.

### Faults found by the writer of the notes (coordinator's message, checked against the Lean)

17. (1) `card_parabolic_blockNumber` "finite ring" → every commutative ring: correct (GradingsOfY.lean 163–164), applied
    as item 10.
18. (2) `IsSplitLevel.pairWeilFinite_name`, the lift placed inside: correct (NamesAtSplitLevel.lean 432), applied as
    item 7.
19. (3) Import `Space.Splitting.homTarget_zeroTerm_pairWeil` text: "intertwines … under the stated side conditions" →
    the full statement (PairSplitting.lean 259–262, 314–316) with the factor a.spaceChar(n′)(det m)·|det m|^{n′/2} and
    the character b·υ^{|p|} on the left, evaluated at det h. `ArrowPair.zeroTerm_splitting_tripleWeil` step 6:
    "zeroTerm(pairWeil(1, 1 ⊕ r)f) = pairWeil(r)(zeroTerm f)" → zeroTerm(pairWeil(1, υ^{|q|})(h, 1 ⊕ r)f) =
    pairWeil(1, 1)(h, r)(zeroTerm f) (EdgePair.lean 195–197, a = b = 1, m = 1); with (1, 1) on both sides the factor
    υ(det h)^{|q|} appears (pairChar, PairDefs.lean 291–296). Correct; applied. The member statement itself (an exact
    intertwining of the two tripleWeil actions) was already right.
20. (4) `exists_branching_pairing` step 7: "|⟨v′, A·b·v⟩| = |⟨v″, b·v⟩| …" (the dual-pairing vector taken for v′) → hA is
    applied to the right-hand vector b·v: v′ ⬝ (A·(b·v)) = G(w, v′) with weylNormSq(w) = weylNormSq(b·v)
    (DualWeights.lean 20; PairTensorData.lean 53–55), then Cauchy–Schwarz for the Weyl Gram form and b2 with L = M.
    Correct; applied (the final bound was right, the route was not).
21. (5) `Data.exists_char_hasWeight` step 3: "ω_w(ζ) has order dividing M_ω, which N₁d divides; the product is 1 after
    reducing exponents" → the tame factors are 1 because ω_w = T_w^{M_ω} (IndexTypes.lean 76) and ζ^{M_ω} = 1 (N₁ ∣ N₁d ∣
    M_ω, `N₁_mul_d_dvd_M_omega`, line 95); b₁, b₂ are multiples of N₁ (`roundUp`, AdmissibleData.lean 88, 105–109, 131),
    so every infinity factor has the exponent −a·k·h₂, leaving a power of ∏_vΦ_v(ζ) for step 4. Correct; applied.
22. (6) `Data.exists_stage_cut`, census binders: checked; the census lists no phantom section variable for this member
    (only k and hk, both arguments). The opposite holds: it misses {P} and (D : Data P), which Lean takes because D occurs
    after the statement's `let` (lines 39–43). Recorded as a `binders_note` (expected Lean order {P} (D) (k) (hk), a text
    reading, not Lean's output); the binder list stays as the census gives it, so the check is unchanged. The text was
    already complete; it got the clarifications of item 2.

### Not applied, and why

* Nothing of a second-reader message or a second-reader message was rejected. Item 22 is applied with the qualification stated there (the coordinator's
  "lists unbound section variables" does not describe this member's census record).
* Not done: no Lean signatures (`binders_basis: lean`) — nothing was built; the binder notes stay readings of the text.
* a second-reader message's ambient-input remark (nine recalled Mathlib facts) is unchanged: no Mathlib file was read in this pass.

### Digests and check

- dossier digest (`dossier_sha256`): old `1f4c5205f58737c7e76387457ff1475d84538aa09705ce9a22ca9672684837d6` → new
  `e0f402b5dd80710777b6792120455ff3afc153a4c3a2a7eb7ac62aa413a06d6b`
- `python3 tools/rb.py check 141`: exit 0 — unit 141: 312 of 312 statements at their lines; 83 structured proofs, 550
  steps, 503 leaves (longest 8 lines, bound 8), 550 steps quote their lines; typed facts in the source: 68 of 68; imports
  quoted: 74 of 74; arguments accounted for: 3066 of 3066
- Changed records: 21 member texts (one also its binders, one a new binders_note), 2 import texts (one with a
  `literature` record), 31 step claims, 2 proof summaries, the unit summary and the binder note of `gen/meta.py`.
