# Corrections to the dossier of 143 (The rows: target forms on an indefinite U(r), the volume of the chain of lifts as a product of lift volumes, and the height of each lift volume)

## 2026-11-26 — statement-boundary overlay (a second-reader message)

Source: the second reader's a second-reader message (`exchange/to-claude/a second-reader message/statement-range-inventory.json`, sha256 1749e406…). The census ends a statement at its first top-level `:=`; in the members below that `:=` belongs to a `let`/`letI`/`have` inside the type (or, where said, the census runs into an equation-style proof), so the census's statement lines stopped before the conclusion. Each declaration was read in full at the pin and the overlay's span confirmed (it ends just before the declaration's own `:=`). Applied by the generator: the chunk generators `143-a/gen/build.py` and `143-b/gen/build.py` (before unit.json is written), then `book/plan/merge_chunks.py 143`, calls `gen/statement_overlay.py`, which gives each listed member `statement_lines` (corrected), `statement_span` (span + SHA-256), `statement_lean_full` (the whole statement) and `statement_basis`, removes a truncated `statement_lean` (`rb.py check` compares `statement_lean` with the census's lines and refuses a longer quotation), and extends the quoted lines of imports to the end of their statements.

### Members (statement lines census → corrected; conclusion old → new)

- `Parameters.norm_jet_le_of_isAdmissibleComb` (New.Rows.MemberKernels:47:7; assignment inside type): lines 47–50 → 47–59. Chunk 143-a. Old quotation stopped at `let u := …` (line 50). Text complete in substance (u, M, F; (i) the jet bound, (ii) the operator bound for schurJet) but hypothesis (i) was garbled ("for all z and R ≥ … with") → now "if, for all z and all real R with Σ|σ(z_i)|² ≤ e^u(2L+2)R, |σ(Q(z))| ≤ A·exp(w + LR), then |σ(jet_Q F)| ≤ M(L, w)·A", and λ_{τ,i} = diagramWeight(rankAt n′, κ)(τ, i) as in Lean.
- `exists_modKernel_integral_bound` (New.Rows.MemberKernels:143:7; assignment inside type): lines 143–146 → 143–150. Chunk 143-a. Old quotation stopped at `let v := c * modKernelI …` (line 146). Text already complete: (i) |ι_p(v)| ≤ 1 for p ∤ q at points integral above p and Q with integral coefficients, (ii) for q = 1, |L|, |N| ≤ 40k, d ≤ g: |σ(v)| ≤ exp(x₁)·M·B → unchanged.
- `DividedSplitting.theta_stdClassSum_productForm` (New.Rows.GluedFormTheta:372:7; assignment inside type): lines 372–374 → 372–377. Chunk 143-a. Old quotation stopped inside the sum, at `let g := g * (liftMod Y.1).1` (line 374), hiding the summand. Text already complete: θ-lift of the class sum = conj(L.weilScalar·c)·Σ_{Y} conj(cosetKernelSum(…)(g_Y)·θ^{W,I_m}_{O.a,b′}[𝟙_{I_z}, letterPoly(−1)(η̄)](g_Y, h′)) → unchanged.
- `Data.exists_test_form_inner_kernelForm` (New.Rows.HeckeValueHeight:87:7; assignment inside type): lines 87–89 → 87–95. Chunk 143-b. Old quotation stopped at `let X := lValueData hE.1 ϑ; let u := …` (line 89). Text already complete: two hypotheses on α and b ⇒ ∃ Ξ, the pairing identity for every g ∧ IsTestForm(l, Ξ) → unchanged except κ₀ = P.vacuumScale(D.s) now named.
- `Data.weylNormSq_linePolyCoords_le` (New.Rows.LineCoordinates:201:7; assignment inside type): lines 201–201 → 201–204. Chunk 143-b. Old quotation stopped at `let y := …` (line 201). Text already complete: toPoly y = image of inFirstCols(stackedDetProd …) ∧ (bounds ⇒ weylNormSq y ≤ (g⁹)^{31m·Σ|DetIndex|}) → unchanged.
- `Data.exists_denom_linePolyCoords` (New.Rows.LineCoordinates:248:7; assignment inside type): lines 248–250 → 248–251. Chunk 143-b. Old quotation stopped at `let Q := H • linePolyCoords j i Y l;` (line 250). Text already complete: homogeneity of degree d and coefficients in every subring containing the τ(Y_ab) → unchanged.
- `Data.lineMultiplier_integral_and_small` (New.Rows.LineArithmetic:30:7; assignment inside type): lines 30–30 → 30–32. Chunk 143-b. Old quotation stopped at `let y := star (c •` (line 30). Text already complete: (i) weylGauge ≤ 1 for p ∤ levelNorm(ϑ), (ii) for Q_ϑ = ∅, weylNormSq(φ∘y) ≤ exp(rB₀) → unchanged.

### Proof steps and summaries

- The proofs own the statement tails by steps of kind statement (S1/S2/S3), whose claims already begin "(Part of the statement: … the line census of the checker takes that := for the declaration's, so these lines count as the value.)" and state the lines; unchanged.

### Imports re-quoted to the end of their statements

- `Data.exists_isFrobPacking` (unit 150): lines 34–36 → 34–38. Chunk 143-a, unit 150. The old text had lost part of the conclusion: it said only "there are i and y with Σ(v_p(n_σ!) − y_σ) ≤ L, or else …", dropping IsFrobPacking(p, n, i, y) and, in the first alternative, χ_K(p) = −1 and i = 1. Now the full statement.
- `exchange_theorem` (unit 147): lines 16–19 → 16–21. Chunk 143-a, unit 147. Text gave the identity loosely; now with γ = rankTwist(ν⁻¹, n) from the `let`, IsTameFor, IsPartner ⊤ σ χ Φ Ψ and "for every point g" with thetaIntegral and pairTheta of the modDatum's.
- `partner_block` (unit 147): lines 94–96 → 94–97. Chunk 143-a, unit 147. Text already complete; the `let`s (x.submatrix id e, y.submatrix e id) and IsPartner ⊤ e χ Φ Ψ now named.
- `Data.hasSum_inner_triLift` (unit 147): lines 77–78 → 77–82. Chunk 143-a, unit 147. Old text was a summary ("a is injective on triBase and its inner products are given by a convergent series of Rallis terms"); now the full statement: ∃ C ∀ ϑ y, with a(y) = triLift(…)(triNegEquiv(…)(y)): (1) the representing vector v of x ↦ ⟪a(y), a(x)⟫ lies in triBase and v = 0 ⇒ y = 0; (2) Σ_γ C·cosetTerm(…)/#(…) = triangleOrder(z, ϑ, 0)·⟪a(x), a(y)⟫.
- `Data.stdLevelIndex_lastResLevel_eq` (unit 147): lines 19–20 → 19–21. Chunk 143-a, unit 147. Text already complete; N(Q), δ and w = triangleOrder false ϑ (the `let`) now named precisely.
- `exists_dual_isometry` (unit 19): lines 102–104 → 102–106. Chunk 143-b, unit 19. Old text was a summary ("some integer matrices make the dual Weyl module isometric"), hiding the evaluation identity and the intertwining; now the full statement (J, J′ inverse, Jᵀ G_κ J = G_κ′, and over every field of characteristic 0: j·weylEval(n, κ′, permArray e) = weylEval(n, κ, permArray e′) and S_κ(g^{−T})·j = j·weylRep(κ′, −Σκ)(g)).
- `Data.conjHolWeight_kernelWeight_bounds` (unit 147): lines 78–78 → 78–87. Chunk 143-b, unit 147; its quotation already covered the whole declaration (lines 78–87). Old text was a summary ("dominance, gaps and sizes"); now the full statement (|k_i| ≤ 5b, K-dominance of k and kernelWeight, holomorphic gaps ≥ 300·nStar(D)).

### Not applied

- Nothing: every overlay span of this dossier was confirmed by reading the source. The chunk self-imports Data.lineMultiplier_integral_and_small (143-a, lines 30–30 → 30–32) and exists_modKernel_integral_bound (143-b, lines 143–146 → 143–150) were re-quoted in the chunks; the merge drops them (they are members).

### Digests and check

- dossier digest (`dossier_sha256`): old `d703b0e5245f863a11df0ce3fd77b96d4666ebded854bae1a56ec39aadb50e16` → new `f09e2120fa248968de81441117452bf61f829a96a6ef6118ea4a34b6772b7715`
- `python3 tools/rb.py check 143`: exit 0 — unit 143: 219 of 219 statements at their lines; 85 structured proofs, 680 steps, 634 leaves (longest 8 lines, bound 8), 680 steps quote their lines; typed facts in the source: 57 of 57; imports quoted: 135 of 135; arguments accounted for: 2273 of 2273


- chunk digests: 143-a old `e2a7444d7905b4b7ca831644edc35db7720f97c031b6455c1531117145aae3f0` → new `480d2d64cb2ca62f389c0d83b813abf6db494cdf05f269c3b265ddb7609be3bc`; 143-b old `a462135936b35e3370eb7db788988d8945b920585fced99e229419593dd5be5a` → new `f1da640810e328f1965b1df55b67b66c3583f6032dc4f07a58f8885232374f16`. `python3 tools/rb.py check 143-a` and `check 143-b`: exit 0.

## 2026-11-26 — second reading (a second-reader message) and the note writer's findings

Correction reader: a Claude agent (Opus 5.5), the only writer of the chunk and unit folders during this pass. Messages
applied: a second-reader message (the second reader's second reading of all 219 statements and of a sample of every proof, read against dossier
`d703b0e5…`), the note writer's four findings passed on by the coordinator, and the statement-strength verdicts of
a second-reader message, 0011, 0012, 0017, 0019, 0024, 0032 for the imports that cite named classical results. Every change was checked
against the pinned source (`lsernau/grh-lean` @ `72fead1`, `grh-compact/src`; files and lines below) and made in the
chunk generators (`143-a/gen/spec/*.py`, `143-b/gen/spec/*.py`; `gen/build.py` of both chunks now also accepts a
Lean-basis argument list and attaches `gen/literature.json`, written by the new `gen/make_literature.py`), then the
chunks were emitted again, checked, and merged with `book/plan/merge_chunks.py 143`. Nothing was built.

### What changed (old → new)

Chunk 143-a:
1. `descentsVanish_hypSum` text (writer's finding; a second-reader message; DescentsVanishDef.lean 9–13, MemberOrthogonality.lean 21–43,
   PairDefs.lean 142–145, LevelForms.lean 65): "for every datum f that is the vacuum at the places of O and their
   conjugates" → for every f with projOn(S) f = f, S the complement of the conjugate closure of the places of O (chosen
   and twist places): f is the vacuum *outside* those places and their conjugates.
2. `stdClassSum_period_eq_zero` step 8 (lines 78–80, `hφ : projOn _ O.places.conjClosureᶜ (φ j) = φ j`): "φ_j is the
   vacuum at the places of O" → the vacuum outside them; step 15.2: "a datum that is the vacuum at the places" → outside
   the places of O and their conjugates (step 8 now under `uses`); `descentsVanish_hypSum` step 3: "data at the level" →
   data that are the vacuum outside the places of O and their conjugates.
3. Imports `AuxPair.descentsVanish_of_reflectionSum` ("for data at the level" → for all data vacuum off M, Q and
   conjugates, AuxPairVanishing.lean 54–64) and `descentsVanish_add_planes` (+ the set S and DescentsVanish W V a S Y ⇒
   DescentsVanish W' V (a·υ^{|p|}) S Y, DescentsVanishPlanes.lean 45–53).
4. `exists_modKernel_integral_bound` (writer's finding: "lacks its index sets L, N"; MemberKernels.lean 131–150): the text
   now introduces L and N (finite types, the explicit section variables of line 134) and says c depends on L, N, D, d
   only; `binders`: the census's text reading (E, n, h, b and instances; no L, N) → Lean's list by rule,
   (L N : Type) [Fintype L] [Fintype N] {P} (D : Data P) (d), `binders_basis: lean`, with the call sites as evidence
   (LineArithmetic.lean 36–38, ValueFamilies.lean 53); not printed by Lean.
5. `posFockVector` (a second-reader message; RealMatching.lean 38–42, PairDefs.lean 235–273): "the space Hom(I_a, V_j)" → Hom(V_j, I_a):
   a × n matrices, rows in a, columns in n, (g, h) acting by X ↦ hXg⁻¹.
6. `stdClassSum_carrierXi_eq_carrierForm` (a second-reader message; Carrier.lean 173–199, StackedDeterminants.lean 284–298): "θ^{S, I_m}"
   → θ^{S, I_{3m}}: S of signature (2m, m), the outer definite group U(I_{3m}) on Fin (2m) ⊕ Fin m (χ∘det needs square
   matrices), the outer class sum over U(I_{3m}); carrierXi is the class sum over U(I_m); C chosen before (𝔪, c, χ).
7. `Data.goodProjTranslate_mem_integralForms` step 3 (a second-reader message; MonomialCoefficientVector.lean 53–54, MackeyFormula.lean
   239–246): "the coefficients of e₀ are algebraic integers" → |𝖦|·e₀(t) are (g ↦ |𝖦|e₀(g) is a character).
8. `exists_int_vector_harmonicPoly_eq` step 2.1 (a second-reader message; lines 92–94): "g fixes the rows e involved" → the substitution
   is by the transposes (g_i)ᵀ, whose rows e(a) are those of the identity because the columns e(a) of g_i are (h).
9. `DividedSplitting.exists_congruenceGroup_inv_eq_one_sub` step 1 (a second-reader message; GluedFormTheta.lean 252–256): "Y is
   nilpotent of order 2" → Y² = 0, nilpotent of index at most 2 (Y = 0 allowed).
10. `Data.groupAlgAction_auxLift`, `Data.range_goodLift_le` and import `Data.goodLift` (a second-reader message; RowVolume.lean 66–82,
    FitTwists.lean 199–237): "a twist ϑ" → a tame character ϑ (Data.TameChar; `auxLift` takes ϑ : D.TameChar).
11. Import `period_eq_zero` (PeriodVanishing.lean 20–30): the loose summary ("fixed by a level, with all theta lifts to
    the complementary group vanishing") → the full statement (level Kf ∩ supportedOn T, DescentsVanish(ℍ^{n₁}, I_n,
    υ^{|n₁|}, T, Y), the period for every h₁); the authors' label kept as theirs; `literature` (unresolved: Walls's
    identity is for a different dual pair).

Chunk 143-b:
12. `firstMinimum_mul_le_hom` text (writer's finding; a second-reader message; MinkowskiSecond.lean 73–76): "λ the first minimum
    (shortest nonzero vector length)" → the first minimum cut off at 1 (inf of 1 and the lengths, so λ ≤ 1); steps 1–2
    now say the characterisation and the bound use the cut-off (le_firstMinimum_iff, firstMinimum_le_one).
13. `isolation` steps 2, 5, 6, 8, 9 (a second-reader message; SparseThetaSum.lean 67–84): step 2 had the labels interchanged ("the
    orthogonality r and the bound hK") → hK holomorphy, r approximation, the unnamed field orthogonality; step 6 "vanishes
    (r)" → the orthogonality field; the approximant at angle 0, written "K_0" beside the given "K₀", is now K^(0)
    (K₀ keeps Lean's name); steps 8–9 keep the two apart: |K^(0)(1)| ≤ 4εB^{7m}, |K₀(1)| ≤ |K^(0)(1)| + ε.
14. `Data.norm_det_compressedGramOp_padic_le` summary and steps 5–9 (a second-reader message; LiftVolumeHeight.lean 44–70, FitTwists.lean
    46–53): second family "y' = 𝗁·z (in L)" → y'_b = gl(gl*(𝗁·z_b)) in the ambient space (tst's type), integral at ι and
    tested; first family integral at every ℓ-adic place; matrix ⟨y_a, pr_L y'_b⟩; step 8 "the entries of f are integers"
    → the integer entries are those of the Fock-pairing matrix before the transport (f_a applies weightRep at δ⁻¹ and
    conjugation); step 9: the second family by the Auerbach coordinates.
15. `Data.norm_det_compressedGramOp_arch_le` steps 5, 7.1 (a second-reader message; lines 84–88): "ζ^σ the table σ-twisted entrywise" →
    conj∘σ⁻¹∘conj∘σ applied entrywise (σ need not commute with conjugation).
16. `Data.heightLe_liftVolume_ratio` summary and steps 1, 1.10, 1.11 (a second-reader message; LiftVolumeHeight.lean 103–127,
    Heights.lean 19–23, FitTwists.lean 251–263): "dim·r·Σβ_ℓ log ℓ" → local exponents dim·r·β_ℓ with Σ_{ℓ∈T} β_ℓ ≤ B₀ for
    every finite set T of primes (no log ℓ); "up to an integer power of the norm of the modulus" → exponent 0 (line 123);
    archimedean part 2·dim·r·B₀ from the multiplier u(1); η = (θ ι)^j in steps 1.10 and 1.11.
17. Imports `Data.IsFitFamily` (two spec files, the wrong one won: "Σγ_ℓ log ℓ ≤ B₀" → Σ_{ℓ∈T} γ_ℓ ≤ B₀ for every finite
    set T, with the coprimality and height fields), `DenominatorLe` (⟨pr_Z y_a, pr_Z y'_b⟩ → ⟨y_a, pr_Z y'_b⟩, as in
    the source), `exists_comparison_forms` (integrality at ℓ coprime to the level norm; size bound at the trivial twist).
18. `Data.lineMultiplier_integral_and_small` (a second-reader message; LineArithmetic.lean 25–32, IndexTypes.lean 184–207): "(ii) if
    Q_ϑ = ∅ (the trivial twist)" → Q_ϑ = ∅ makes every finite tame component trivial, ϑ need not be the trivial
    character; c uniform in i, ϑ, h; `binders`: none (census) → {P} {D : Data P} (j : D.LiftIndex) by rule, call site
    ComparisonForms.lean 59 (`binders_basis: lean`, replaces the reader's `binders_note`); proof summary and step 11.4:
    "at the trivial twist" → when Q_ϑ = ∅ (N(Q_ϑ) = 1).
19. `Data.linePair` (a second-reader message; Separation.lean 44–58, IndexTypes.lean 112–123): "the pair … of weight σ ↦ w_j(σ) − n_j /
    of constant weight e_s" → those are the coordinates c; the characters have weights n_j − w_j(σ) and −e_s.
20. `carrierForm_spec` step 1 (a second-reader message; NaturalFormNear.lean 26, LevelModulus.lean 76–79): "n: χ ≠ 0 on units" → n: the
    places of 𝔪 are nonempty (first clause of IsTameFor, needed by isRapid_modKernel); θ^{S, I_m} → θ^{S, I_{3m}}.
21. Imports with `literature` (the second reader's verdicts; first-reading labels now stated as the authors'):
    `Space.exists_short_basis` (weakens; text "with entries bounded by c/λ_S … and a dual matrix" → columns in the lattice
    ball of radius 6N(fn)²/λ, λ cut off at 1, no dual matrix in the statement, MassBasic.lean 76–84), `exists_auerbach`
    ("Auerbach's lemma" → a determinant-maximisation extension, no published source located; full hypotheses),
    `exists_near_max` ("(Siegel's argument)" → the authors' label; only an analogue (Poor–Yuen) located; full hypotheses,
    NearMaximum.lean 21–31), `reproducing_formula_modKernel` ("(basis problem in the stable range)" → the authors' label;
    the formula is the artifact's own; full statement, ReproducingFormula.lean 93–107). Self-imports of the other chunk
    updated to match (dropped by the merge).
22. READMEs of both chunks: a pointer to this section; "Second readings: none" → a second-reader message.
23. `Data.heckeValueProd` (the convention of the partial L-function, as corrected in unit 147 from a second-reader message/0044;
    AutCharLFunction.lean 48–50): "lValueProd(S, ν, e) = …·∏|L^S(z, ν)|²" → |L^{S∪S̄}(z, BC ν)|², the Hecke L-function of
    the base change x ↦ ν(x/x̄) without the Euler factors at S and at the conjugate places.

### Checked and found already right, or not applied

* Writer's finding "`Parameters.norm_jet_le_of_isAdmissibleComb` has an unfinished text (R ≥ …)": already corrected by
  the statement-boundary pass above (the text states the implication for all z, R, and L positive in the Schur bound;
  MemberKernels.lean 47–59); no "R ≥" remains in the dossier. Nothing to change.
* a second-reader message on the two volume statements, the comparison theorem (γ_η = conj(κ_1/κ_η), testing for every y, integrality
  at primes coprime to the level norm, size at the trivial twist), separation and the approximation theorem, the
  jet-depth lower bound p^{−F(p)}, the rank-one multiplicities p.c(τ) − p.z, the log ℓ in the rank-one exponents
  γ_ℓ + 2F(ℓ)·log ℓ (HeckeValueHeight.lean 177, correct there), and the unrelated k : ℂ of LiftVolumeHeight: the dossier
  already agrees; nothing changed.
* a second-reader message's renaming of the target K₀ to "K_tar": not applied, K₀ is Lean's argument name (the signature rule); only
  the approximant at angle 0 was renamed (K^(0)).
* Step 1 of `DividedSplitting.exists_congruenceGroup_inv_eq_one_sub` writes ϖ⁻¹X beside the hypothesis ϖ̄·Y = 0: this is
  consistent with the chunk's letters (README of 143-a: ϖ̄ is the residue `genResidue` of the generator ϖ of M, not a
  complex conjugate); unchanged.

### Digests and checks

- dossier digest of 143: old `f09e2120fa248968de81441117452bf61f829a96a6ef6118ea4a34b6772b7715` → new
  `0fdd0ee61a46d42964293ded98ccbafb82c7bc8daf768deca979b9ae6e423d6b`.
- chunks: 143-a `480d2d64…` → `0fdacda10b7d25862b200e77960b1354d2035c725e3789202087f727696bebb2`; 143-b `f1da6408…` →
  `67f22fd37d3f10afc0517bfcb6c63b25db6242c7e525d28204c6d11b2e289e5d`.
- `python3 tools/rb.py check 143-a`, `check 143-b`, `check 143`: exit 0 — unit 143: 219 of 219 statements at their lines;
  85 structured proofs, 680 steps, 634 leaves (longest 8 lines, bound 8); typed facts 57 of 57; imports quoted 135 of
  135; arguments accounted for 2271 of 2271 (2 members by Lean's own signature, derived by rule, which the check cannot
  confirm).

Cost: about 35 minutes of wall time for the three units 143, 147 and 132 together (08:22Z–08:57Z by `date -u`, the start estimated from the first command), shared among them; tokens not reported by the client.

## 2026-11-26 — Pass 8: a second-reader message (verified; nothing to apply)

Correction reader: a Claude agent (Opus 5.5). the second reader's a second-reader message verified the revised dossier `0fdd0ee6…`, which is still the present one; it asks for no change. Each verified passage was re-read in the present dossier and at the pin (`grh-compact/src` at `72fead10`):

- `descentsVanish_hypSum`: S is the complement of the conjugate closure of the places of O; the datum is the vacuum outside the chosen and twist places and their conjugates (MemberOrthogonality.lean 35–36; DescentsVanishDef.lean 9–13) — present.
- `stdClassSum_period_eq_zero` step 8: the same complement in the projected data hφ (MemberOrthogonality.lean 78–80) — present.
- `posFockVector`: a × n matrices, Hom(V_j, I_a), (g, h) acting by X ↦ hXg⁻¹ (Lib/Weil/Construction/PairDefs.lean 255–258; RealMatching.lean 43) — present.
- `Data.heightLe_liftVolume_ratio` steps 1.10–1.11: the local exponent at ι is rowDim·r·β_ℓ with no factor log ℓ (the height predicate already sums the local exponents, Heights.lean 19–23); Σ_{ℓ∈T} β_ℓ ≤ B₀ for every finite set T (g); the exponent of the modulus at line 123 is 0 (LiftVolumeHeight.lean 117–127) — present.

Dossier unchanged (`0fdd0ee61a46d42964293ded98ccbafb82c7bc8daf768deca979b9ae6e423d6b`); `python3 tools/rb.py check 143`: exit 0.
