# Corrections to the dossier of 147 (The exchange identity: theta integrals of complementary rank agree up to a constant, and cruder forms complete a family to a basis in the lower bound)

## 2026-11-26 — statement-boundary overlay (a second-reader message)

Source: the second reader's a second-reader message (`exchange/to-claude/a second-reader message/statement-range-inventory.json`, sha256 1749e406…). Applied in the three chunks through their generators (`gen/statement_overlay.py`, called from `gen/build.py`; texts and claims in `gen/ann/*.txt`), then merged with `book/plan/merge_chunks.py 147`. The chunk records below are the chunks' own `CORRECTIONS.md`, copied here (the merge does not carry them).

Summary: 24 members now carry the whole statement (`statement_lines`, `statement_span`, `statement_lean_full`; the truncated `statement_lean` is not used, since `rb.py check` compares it with the census's lines). All 24 member texts already stated the full conclusion; one wrong side remark was removed (`LValueData.inner_trivialLift_self_eq_L`: "C depends on X only through the places of M" — C contains no X). `Data.isPrimitiveMulChar_of_isTameFor` is the equation-style case: its statement is line 42 alone (the census ran into the proof up to the `have :=` on line 44). 24 step claims (statement tails owned by steps) and one summary now say that those lines are the rest of the statement. Import quotations were extended to the end of their statements; import texts that had hidden or wrong conclusions were corrected: `ReadsAt.sourceTerm_localDatum` (a missing premise, the wrong point and right-hand side), `IsSteep.exists_isTwoFactor_restriction` (two of its three conclusions missing), `integral_tail_le` (misread function), and vague summaries replaced by full statements (`norm_poincare_period_sub_le`, `Parameters.norm_jet_le_of_isAdmissibleComb`, `one_square`, and others listed below). No span contested.

### Digests and check

- dossier digest (`dossier_sha256`) of 147: old `f6a7a8424431161a10143eca7489648c7b0ddc3c8a81130b495f28010a4894a2` → new `69785ee85df12aad3abc64fe66d260b8ac08d2e7b37f6659300e0586245df3cd`
- `python3 tools/rb.py check 147`: exit 0 — unit 147: 305 of 305 statements at their lines; 122 structured proofs, 933 steps, 879 leaves (longest 9 lines, bound 8), 933 steps quote their lines; typed facts in the source: 68 of 68; imports quoted: 239 of 239; arguments accounted for: 2627 of 2627 (72 members by Lean's own signature, which this check cannot confirm)
- chunk 147-a: old `b055eafe209780b6fb7620c4fe329c76e3656510254da6d6e56247595d3b96d5` → new `21be9b6931f3094b3b2be5a604f6ed0444ede693e7a1cfd1e57ad20f0187c774`; `python3 tools/rb.py check 147-a`: exit 0
- chunk 147-b: old `083a3cd52b3a535687c068bad1389d251afb655d35b1e86b7f9180600302832d` → new `9e880c135729075887d5a7b794c78a5f03db2759535244ebc2dd83b93ed9bd6b`; `python3 tools/rb.py check 147-b`: exit 0
- chunk 147-c: old `bb7e64337f55b952bc347e523d5d7a17844c18bb98b9416ba8cf254890dc224b` → new `a7a0211fdad69a016400360edecd2ca0a4408928c531f4f3fd374f303c237995`; `python3 tools/rb.py check 147-c`: exit 0

## Chunk 147-a (its CORRECTIONS.md)

## Corrections to the dossier 147-a (chunk a of unit 147, Exchange)

### 2026-11-26 — statement-boundary overlay (a second-reader message)

Source: the second reader's a second-reader message, `exchange/to-claude/a second-reader message/statement-range-inventory.json`
(sha256 1749e406…). The census ends a statement at its first top-level `:=`; in the seven members below that `:=` is
the one of a `let` inside the type, so the census's statement lines (and every quotation taken from them) stopped
before the conclusion. Each corrected span was re-sliced and re-hashed against the pinned file and read in the source:
in all seven the statement ends right before the declaration's `:= by`. Nothing was contested.

How it is applied: `gen/statement_overlay.py` (the correction reader's helper), called from `gen/build.py` after the
records are built. A member listed in the overlay gets `statement_lines` (corrected), `statement_span` (span and
SHA-256), `statement_lean_full` (the exact text of the whole statement) and `statement_basis`; an import whose quotation
stopped before the end of the corrected statement is re-quoted to that end. (`statement_lean` is not used: `rb.py check`
compares it with the census's truncated lines.) Texts and claims were changed in `gen/ann/*.txt`.

#### Members (statement lines: census → corrected; the conclusion the census quotation had cut off)
- `AuxPair.levelIndicator_support_and_normSq` (62–62 → 62–65): quotation stopped at `let F :=`; whole conclusion
  F = #TwistGL(O, r)·levelIndicator(O), (F(y) ≠ 0 ⇒ inclMatrixᵀ·y = 1) ∧ ∑|F|² = #TwistGL(O, r)²·(∏ q(twistPlace))^{rankDiff·|r|}.
  Text already complete.
- `LValueData.inner_trivialLift_self_eq_L` (191–192 → 191–195): quotation stopped at `let C :=`; whole conclusion C ≠ 0 ∧
  ⟨trivialLift(X), trivialLift(X)⟩ = C·∏(q − 1)·hookNumber·#WeylIndex·L(μ(X)⁻¹, places(X), k)·(∏ q(twistPlace))^{|n|−1}.
  Text complete; one side remark corrected: "C depends on X only through the places of M" → "C does not depend on X
  (only on E and n)" (C = vol[U(I_n)]·vol[U(I₁)]/eulerProd(realZetaCoeff, |n|/2) has no X in it).
- `partner_block` (94–96 → 94–97): quotation stopped inside the second function, at `let y :=`; whole conclusion
  IsPartner(⊤, e, χ, Φ, Ψ) with Ψ(y) = χ⁻¹(det y₁)·f(−y₂y₁⁻¹). Text already complete.
- `IntegralFrame.partner_mem_of_unimodular_vanishing` (57–59 → 57–62): quotation stopped at `let S (z) y :=`; whole
  conclusion (∀ z, S_z ∈ M) → (∀ Ψ′ ∈ M, (admissible Λ kill Ψ′) → Ψ′ ∈ P) → Ψ ∈ P. Text already complete.
- `thetaTerm_stdDatum_spec` (27–30 → 27–40): quotation stopped at `let f :=`; whole conclusion: the three assertions
  (integrability, explicit theta term, vanishing coefficient). Text already complete.
- `frameAt_real_unitary` (45–46 → 45–47): quotation stopped at `let P :=`; whole conclusion (P*P = 1 ∧ PP* = 1) ∧
  diag(s)·P = P·B. Text already complete.
- `PositivePart.exists_slice_eq` (59–61 → 59–62): quotation stopped at `let v :=`; whole conclusion
  ∃ U, P₊(s)U = L(−a) + I·P₊(s′)u + K(−a) ∧ ∀ P, slice(mixedModel(h), a, v, u) = v(U). Text already complete.

#### Proof steps (9 claims changed)
Step 1 of each of the seven proofs owns the rest of the statement (the line census counts it as the value). Its claim
now says so explicitly — "Not a step of the proof: lines a–b are the rest of the statement … owned here only because the
line census takes the `:=` of `let …` for the start of the value" — and states those lines. In `thetaTerm_stdDatum_spec`
also the children 1.1 and 1.2 (assertions (1)–(2) and (3)) now say "Rest of the statement, not proof". No other step
restated a truncated statement; the check still passes on the line-census basis.

#### Imports re-quoted to the end of their statements (11)
Texts rewritten to state the whole statement: `IsEquivariantLift.centreCoeff_shear`,
`IsEquivariantLift.exists_linear_centreCoeff`, `Modulus.matrix_ext_modulusResidue`, `ReadsAt.sourceTerm_localDatum`
(the old text missed the premise "Φ(w) = stdDatum(adaptedFrame(h, D), G)(w) whenever w·K = π(y)", stated the source term
at x instead of scaleIdele(E)·x, and misnamed the right side, which is localDatum(W₁, V, realSlice(D, V, x, v), z ↦
[z integral]·G(fromCols(π(y), z)), h)), `Space.Splitting.centreCoeff_eq_integral_stabilizer` (F includes the factor
y(h)), `Space.Splitting.centreCoeff_sub`, `exists_integral_stages_eq_mul` (F also left Γ-invariant).
Quotation only (text already complete): `eulerProd_eq_exp`, `inner_product_formula`, `rallis_inner_product_euler`,
`shear_invariant`.

#### Not applied
Nothing refused. Not done: no `source_ranges` were added (the proofs keep the line-census basis, so the statement tail
stays owned by step 1, as the coordinator asked).

#### Digests and check
- old dossier digest: b055eafe209780b6fb7620c4fe329c76e3656510254da6d6e56247595d3b96d5
- new dossier digest: 21be9b6931f3094b3b2be5a604f6ed0444ede693e7a1cfd1e57ad20f0187c774
- `python3 tools/rb.py check 147-a`: exit 0 — "47 of 47 statements at their lines; 32 structured proofs, 337 steps,
  316 leaves (longest 8 lines, bound 8), 337 steps quote their lines; typed facts in the source: 33 of 33; imports
  quoted: 153 of 153; arguments accounted for: 727 of 727 (12 members by Lean's own signature, which this check cannot
  confirm)".

## Chunk 147-b (its CORRECTIONS.md)

## Corrections to the dossier 147-b (chunk b of unit 147, Exchange)

### 2026-11-26 — statement-boundary overlay (a second-reader message)

Source: the second reader's a second-reader message, `exchange/to-claude/a second-reader message/statement-range-inventory.json`
(sha256 1749e406…). The census ends a statement at its first top-level `:=`. In eleven members below that `:=` is the
one of a `let` inside the type, so the census's statement lines (and every quotation taken from them) stopped before
the conclusion; in one (`Data.isPrimitiveMulChar_of_isTameFor`) the proof is written by equations and the census ran
into it. Each corrected span was re-sliced and re-hashed against the pinned file and read in the source: every
statement ends right before the declaration's `:=` (or, for the equation-style one, before the `|` on line 43).
Nothing was contested.

How it is applied: `gen/statement_overlay.py` (the correction reader's helper), called from `gen/build.py` after the
records are built. A member listed in the overlay gets `statement_lines` (corrected), `statement_span` (span and
SHA-256), `statement_lean_full` (the exact text of the whole statement) and `statement_basis`; an import whose quotation
stopped before the end of the corrected statement is re-quoted to that end. (`statement_lean` is not used: `rb.py check`
compares it with the census's lines.) Texts, claims and the one summary were changed in `gen/ann/*.txt`.

#### Members (statement lines: census → corrected; the conclusion the census quotation had cut off)
- `exchange_of_partners` (97–102 → 97–105): quotation stopped at `let γ :=`; whole conclusion ∃ c, C·|c|² =
  lValueProdInt(𝔠, |r| − |n|/2)·equalRankThetaRatio(…) ∧ the exchange identity for all locally constant partners.
  Text already complete.
- `exchange_theorem` (16–19 → 16–21): quotation stopped at `let γ :=`; whole conclusion ∃ c ≠ 0, |c|² =
  C·lValueProd(places(𝔪), ν, e) ∧ the identity for all partners. Text already complete.
- `Data.Pair.ratio_ne_zero_and_real` (125–125 → 125–126): quotation stopped at `let r :=`; whole conclusion r ≠ 0 ∧
  conj r = r. Text already complete.
- `LValueData.map_trivialLift` (13–15 → 13–19): quotation stopped at `let Y :=`; whole conclusion: the three hypotheses
  on n, e, μ and the conjugation formula for σ(jetScale^{∑dg}·trivialLift(X)). Text already complete.
- `Data.isPrimitiveMulChar_of_isTameFor` (42–44 → 42–42; equation-style): the census statement ran into the proof
  (the pattern `| ⟨_, ψ, _, hψ, H⟩, a, n =>` and `have` up to its `:=` on line 44); the statement is
  IsTameFor(𝔪(D, ϑ, 1), ν, γ, χ) → IsPrimitiveMulChar(χ). Text already free of proof content (its gloss "for each a ≠ 0 some
  χ(1 + c·a) is neither 0 nor 1" is the definition of IsPrimitiveMulChar); unchanged.
- `integral_integral_sum_eq` (22–23 → 22–25): quotation stopped at `let μ :=`; whole conclusion (integrability and
  integrals of the F(i)) → ∫∫ ∑ c(i)F(i) = ∑ c(i)G(i). Text already complete.
- `exists_integrable_kernel_bound` (33–37 → 33–39): quotation stopped at `let F q :=`; whole conclusion Integrable(F) ∧
  ∀ q, |F(q)| ≤ C·weightedNorm_N(v). Text already complete.
- `one_square` (59–65 → 59–70): quotation stopped at `let u i x :=`; whole conclusion ∃ C κ, ∀ i, ∃ c ≠ 0, |c|² =
  C·lValueProd(…) ∧ SquareLaw(χ(i), σ, κ/c, …) for all f, l. Text already complete.
- `IsEdgeFamily.exists_adjoint_first_arrow` (35–36 → 35–38): quotation stopped at `let b i n [Fintype n] :=`; whole
  conclusion: given the second edge family, ∃ Ψ′ with ⟨x, modLift(…)(y)⟩ = ⟨modDescent(…)(x), formNegEquiv(S, l)(y)⟩.
  Text already complete.
- `Data.hasSum_inner_triLift` (77–78 → 77–82): quotation stopped at `let a y :=`; whole conclusion: the invariance
  property (1) and the series (2). Text already complete.
- `Data.stdLevelIndex_lastResLevel_eq` (19–20 → 19–21): quotation stopped at `let w :=`; whole conclusion the identity
  stdLevelIndex(…) = C·#(O_E/𝔪(D, ϑ, 0))^k·gramFactor(…)^m·w(m)/(w(0)·w(1)^m). Text already complete.
- `Data.inner_iotaAtLevel` (42–42 → 42–44): quotation stopped at `let u :=`; whole conclusion the inner-product
  identity. Text already complete.

#### Proof steps (11 claims changed) and one summary
Step 1 of each of the eleven `let` proofs owns the rest of the statement (the line census counts it as the value). Its
claim now says so explicitly — "Not a step of the proof: lines a–b are the rest of the statement … owned here only
because the line census takes the `:=` of `let …` for the start of the value" — and states those lines. No other step
restated a truncated statement. The summary of `Data.isPrimitiveMulChar_of_isTameFor` now says that the statement is
line 42 alone and that the line census wrongly counts lines 43–44 up to the `:=` of the `have` (the equation's pattern)
as statement; that proof keeps the line-census basis (no `source_ranges`), as asked. The check still passes.

#### Imports re-quoted to the end of their statements (7)
Texts changed: `Data.paramsCorrespond_first_arrow` (now the full statement, as the 147-c member text),
`LValueData.inner_trivialLift_self_eq_L` (full statement as the 147-a member; the wrong remark "C depending on X only
through the places of M" removed: C does not depend on X), `partner_block` (full statement as the 147-a member),
`Modulus.matrix_ext_modulusResidue` and `ReadsAt.sourceTerm_localDatum` (the texts written in 147-a; the old
sourceTerm text missed the premise on Φ, the point scaleIdele(E)·x and the right side), `pairWeil_modDatum_single`
(the text written in 147-c). Quotation only: `rallis_inner_product_euler`.

#### Not applied
Nothing refused. No `source_ranges` were added (line-census basis kept).

#### Digests and check
- old dossier digest: 083a3cd52b3a535687c068bad1389d251afb655d35b1e86b7f9180600302832d
- new dossier digest: 9e880c135729075887d5a7b794c78a5f03db2759535244ebc2dd83b93ed9bd6b
- `python3 tools/rb.py check 147-b`: exit 0 — "131 of 131 statements at their lines; 53 structured proofs, 297 steps,
  283 leaves (longest 9 lines, bound 8), 297 steps quote their lines; typed facts in the source: 11 of 11; imports quoted:
  94 of 94; arguments accounted for: 1210 of 1210 (36 members by Lean's own signature, which this check cannot
  confirm)". (The 9-line leaf is an indivisible leaf, unchanged.)

## Chunk 147-c (its CORRECTIONS.md)

## Corrections to the dossier 147-c (chunk c of unit 147, Exchange)

### 2026-11-26 — statement-boundary overlay (a second-reader message)

Source: the second reader's a second-reader message, `exchange/to-claude/a second-reader message/statement-range-inventory.json`
(sha256 1749e406…). The census ends a statement at its first top-level `:=`; in the five members below that `:=` is the
one of a `let` inside the type, so the census's statement lines (and every quotation taken from them) stopped before
the conclusion. Each corrected span was re-sliced and re-hashed against the pinned file and read in the source: in all
five the statement ends right before the declaration's `:= by`. Nothing was contested.

How it is applied: `gen/statement_overlay.py` (the correction reader's helper), called from `gen/build.py` after the
records are built. A member listed in the overlay gets `statement_lines` (corrected), `statement_span` (span and
SHA-256), `statement_lean_full` (the exact text of the whole statement) and `statement_basis`; an import whose quotation
stopped before the end of the corrected statement is re-quoted to that end. (`statement_lean` is not used: `rb.py check`
compares it with the census's truncated lines.) Texts and claims were changed in `gen/ann/*.txt`.

#### Members (statement lines: census → corrected; the conclusion the census quotation had cut off)
- `Data.endWeightData` (def; 161–161 → 161–163): quotation stopped at `let ι :=`; whole type Σ' κ, Σ' e, (∀ j,
  IsLiftWeight(ι j, ι (j+1), κ, gridWeight(D, z, j, ι (j+1)), e j) ∧ gridWeight(D, z, j, ι j) = e (j+1)) ∧ ∀ j ≤ m,
  IsHCParam(κ, e j, −gridParam(D, z, 0, j, m)), ι = EndIndex(D, z). Text already complete.
- `Data.IsTidy.exists_square_move` (242–253 → 242–254): quotation stopped inside the right side, at `let x :=`; whole
  conclusion ∃ Φ tidy of order n + 2 with Λ(…) = C·Φ(S ↦ L(f(S, x′₂))((S(v, r) | x′₁))). Text already complete.
- `Data.iotaPlus_adjoint_weightedChain` (21–22 → 21–25): quotation stopped at `let U :=`; whole conclusion: for i ≠ 0 the
  level invariance of ι(i − 1)(φ) and U, and ∫ ι(i)(φ)·U = ∫ ι(0)(φ)·y. Text already complete.
- `Data.conjHolWeight_kernelWeight_bounds` (78–78 → 78–80): quotation stopped at `let s :=`; whole conclusion: |k(i)| ≤ 5·b(D),
  the two K-dominance conditions and the two holomorphic-gap conditions. Text already complete.
- `Data.paramsCorrespond_first_arrow` (167–168 → 167–171): quotation stopped at `let δ n τ :=`; whole conclusion
  P(i + 1, j, i, j + 1) ∧ P(i, j + 1, i + 1, j). Text already complete.

#### Proof steps (4 claims changed)
Step 1 of the four proofs (`Data.endWeightData` is a def without one) owns the rest of the statement (the line census
counts it as the value). Its claim now says so explicitly — "Not a step of the proof: lines a–b are the rest of the
statement … owned here only because the line census takes the `:=` of `let …` for the start of the value" — and states
those lines (with D written where Lean's dot notation passes it). No other step restated a truncated statement; the check
still passes on the line-census basis.

#### Imports re-quoted to the end of their statements (7), all texts rewritten
- `IsEdgeFamily.isArrow_modDatum`: K and φ spelled out; arrows K: k(d) → k′(d) and K.swap: k′(¬d) → k(¬d).
- `IsSteep.exists_isTwoFactor_restriction`: the old text missed two of the three conclusions, the bound
  ‖ω‖ ≤ |n ⊔ {∗}|²·(6B)^{2M+1} and the identity (subOnePair(j, s))₂ = ω⁻¹·((subOnePair(j, s))₁ ⊕ 0)·ω.
- `Parameters.norm_jet_le_of_isAdmissibleComb` (member of 143-a): the vague summary replaced by the two bounds (jets along
  Q: ≤ M(L, w)·A; Schur jets: ≤ M(L, …)·√weylNormSq(σ∘ξ)) with u, M(L, w) and F defined.
- `integral_tail_le`: the old text spoke of "the norm of the inverse"; the function is formalDegree(l)·(2/‖g‖)^c; the
  integrability and the explicit bound 8·(2000(|n| + L + 1)⁶)^{2|n|²}·2^c are now stated, with the section hypotheses.
- `norm_poincare_period_sub_le` (unit 133): the vague summary replaced by the hypotheses, the definitions φ, ψ, L, v, X, K
  and the conclusion Integrable(ψ(1)) ∧ ‖∫ ∑_γ K·F − v·realConv(ψ(1), F)(x)‖ ≤ v·L·S·(10/d).
- `one_square` (member of 147-b, read here from the source): hypotheses, u(i, x), v(i, y) and the conclusion ∃ C κ, ∀ i,
  ∃ c ≠ 0, |c|² = C·lValueProd(…) ∧ SquareLaw(χ(i), σ, κ/c, …).
- `pairWeil_modDatum_single`: g = ((1, k), 1, k′) and the identity written out.

#### Not applied
Nothing refused. Not done: no `source_ranges` were added (the proofs keep the line-census basis, so the statement tail
stays owned by step 1, as the coordinator asked).

#### Digests and check
- old dossier digest: bb7e64337f55b952bc347e523d5d7a17844c18bb98b9416ba8cf254890dc224b
- new dossier digest: a7a0211fdad69a016400360edecd2ca0a4408928c531f4f3fd374f303c237995
- `python3 tools/rb.py check 147-c`: exit 0 — "127 of 127 statements at their lines; 37 structured proofs, 299 steps,
  280 leaves (longest 8 lines, bound 8), 299 steps quote their lines; typed facts in the source: 24 of 24; imports
  quoted: 67 of 67; arguments accounted for: 690 of 690 (24 members by Lean's own signature, which this check cannot
  confirm)".


## 2026-11-26 — second reading (a second-reader message with unit-147-a/b/c.md, and a second-reader message)

Correction reader: a Claude agent (Opus 5.5), the only writer of the chunk and unit folders during this pass. Messages
applied: a second-reader message (the second reader's second reading of all 305 statements and a passage of each of the 122 proofs, read against
dossier `f6a7a8424431…`; its payloads `unit-147-a.md`, `unit-147-b.md`, `unit-147-c.md`), a second-reader message (the same reading of
part b, sent first: exchange theorem, modulus and partial L-function), and the statement-strength verdicts of a second-reader message,
0011, 0012, 0017, 0019, 0024, 0032 for the imports that cite named classical results. Every change was checked against
the pinned source (`lsernau/grh-lean` @ `72fead1`, `grh-compact/src`; files and lines below), made in the chunk
annotations (`147-x/gen/ann/*.txt`) and, for the `literature` records, through `gen/literature.json` (written by the new
`gen/make_literature.py`, attached by `gen/build.py`); the chunks were emitted again, checked, and merged with
`book/plan/merge_chunks.py 147`. Nothing was built.

### What changed (old → new)

Chunk 147-a:
1. `LValueData.inner_trivialLift_self_eq_L` (a second-reader messagea; AutCharLFunction.lean 48–50): "L^S(k, μ⁻¹) without the Euler
   factors at the places of X" → L^{S∪S̄}(k, BC(μ⁻¹)), the Hecke L-value of the base change x ↦ μ⁻¹(x/x̄) without the
   factors at the places of X and their conjugates; likewise in its proof summary ("L^S(k, μ⁻¹)" → L^{S∪S̄}(k, BC μ⁻¹)).
   (That C does not depend on X was already corrected by the overlay pass.)
2. `matchingPairs.exists_linear_factor` steps 4, 5, 6, 8 (a second-reader messagea; BlockPartners.lean 18–29, 75–89, `(f := (·ᵀ * (r q).2))`
   with `.2` the inverse): "x ↦ Φ(x)·[xᵀ·r_q primitive]" → [xᵀ·r_q⁻¹ primitive]; the coset p(x) is the unique q in that
   direction; the representatives give uniqueness in both directions; the change of variables is by r_qᵀ.
3. `surjOn_cone_integral_detVectors` (a second-reader messagea; DeterminantVectors.lean 84–90): "maps detVectors … onto detVectors" →
   Set.SurjOn: every lower determinant vector is the cone integral of an upper one; no MapsTo is asserted.
4. `stdExchange_of_periods` (a second-reader messagea; LowRankIdentity.lean 105–124): denominator "ν_𝔠(z)·|z|^{|n|/2}" →
   BC(ν_𝔠)(z)·(√|z|_𝔸)^{|n|}, the base-change character (on ideles) at the idele with infinite components z.
5. `thetaTerm_stdDatum_spec`, `IsEquivariantLift.apply_stdColDatum_eq_zero` (a second-reader messagea; LineParabolic.lean 165–169): "not
   represented by t′ (as an adelic matrix)" + : at some infinite place v no complex c has c*·diag(t′)·c = T_v.
6. `thetaLarge_eq_apply_one_of_even_rank` summary: "strong approximation for isotropic unitary groups makes it constant"
   → the constancy criterion `IsAutFunction.apply_eq_apply_one` (see 15).

Chunk 147-b:
7. `exchange_theorem` text and step 1 (a second-reader message, a second-reader messageb; ExchangeTheorem.lean 16–21, LargeSideConstantTerm.lean
   23–25): + |c|² = C·(∏_{w∈S} Nw)^{e²}·∏_{j=1}^{e}|L^{S∪S̄}(j, BC ν)|², S = places(𝔪) (both products 1 at e = 0); C and x
   chosen before the triple, c per triple for all partners and all g, only |c|² specified; |n| = 2|b| + 2e.
8. `exchange_theorem` step 11 (a second-reader message; ExchangeTheorem.lean 31–34): "π the ring homomorphism from O_E/𝔪 to the local
   product at S that splits the reduction" → π : O_S → O_E/𝔪, surjective, from the integral local product at S to the
   modulus ring, with π∘evalPlaces = reduction (`RingHom.liftOfRightInverse`; the right inverse is auxiliary); step 13:
   liftFn = pull-back along π entrywise on integral matrices, 0 elsewhere (ColumnLattices.lean 160–165); step 14: the
   hypotheses of `IsPartner.lift_of_reduction` (π local, surjective, χ∘π) in this direction (PartnerAlgebra.lean 99–101);
   summary accordingly.
9. `Data.hasSum_inner_triLift` text and step 1 (a second-reader message, a second-reader messageb; TriangleArrows.lean 77–82, SharpData.lean 69–73):
   "(2) for every x ∈ triBase(D, z)" → for every form x of the ambient space TriForm(D, z, 0, 0) (only y lies in
   triBase); a and the test forms of (1) likewise on the ambient space.
10. `Data.Pair.log_norm_map_norm_sq_trivialLift` step 11 (a second-reader message; AlgebraicPartConjugates.lean 69–77,
    SemilinearWeilLaw.lean 18–20): "the multiplier ratios having absolute value 1" → J for σ and for conj∘σ∘conj, the two
    ratios multiply to 1 by σ(Δ)σ(Δ̄) = ΔΔ̄ (`map_finMultiplier_mul_conj`, new import with its reading); step 10: the
    lower bound −4f in every case, the upper 4f only when flat.
11. `one_square` step 5 (a second-reader message): + κ may be 0 and serves the whole family (already "not shown to be non-zero" in the
    text). `SquareLaw` already states the weighted sums; unchanged.
12. `Data.Pair.lValueProd_eq`: "|L^S(z, μ)|²" → |L^{S∪S̄}(z, BC μ)|² (same convention as 1, 7).
13. `LValueData` (a second-reader message): + the census's lines 91–98 end with `unseal Finset.univ in`, the prefix of the next
    declaration (AlgebraicPartDefs.lean 98).
14. Self-imports of 147-a updated to match (`LValueData.inner_trivialLift_self_eq_L`, `surjOn_cone_integral_detVectors`;
    dropped by the merge).

Imports with `literature` (all three chunks; the first reading's labels now stated as the authors'):
15. `IsAutFunction.apply_eq_apply_one` ("Strong approximation for isotropic unitary groups" → constancy, a consequence of
    strong approximation for SU with the torus hypothesis; weakens), `IsDualFamily.eq_zero_of_coeff` ("all of whose Fourier
    coefficients vanish" → only those i with χ_i(a) = c whenever cF(x + a) = F(x), a weaker hypothesis; FundamentalDomain.lean
    81–87; specializes), `inner_product_formula` and `rallis_inner_product_euler` (Rallis labels qualified; unresolved),
    `matrix_gauss_sum` (classical only at invertible frequencies over a field; unresolved), `AutChar.HasWeight.L_ne_zero`
    (+ base change and S ∪ S̄, AutCharLFunction.lean 64–68; specializes), `Space.exists_kernel_form` (+ k = 0 allowed;
    unresolved), `seesaw_periods` (an inference from Kudla's seesaw with extra hypotheses; weakens); records only, texts
    unchanged: `Space.exists_eq_move`, `Space.weak_approximation`, `exists_orthonormal_Ô`, `hecke_transfer_of_equivariant`,
    `witt`, `witt_Ohat_of_orthonormal`, `ParamsCorrespond.isEdge_jointHarmonic`, `Space.exists_mapsTo_ratVectors`,
    `Space.exists_splitting`, `Space.finite_levelSpace` — 18 records in all.

Chunk 147-c:
16. `Data.isTameFor_twistedChi` (a second-reader messagec; GridModuli.lean 110–115, LineCoordinates.lean 67): "a natural number j" → a
    lift index j ∈ D.LiftIndex (1 ≤ j ≤ m; `twistedChi` uses j.1); "c ≠ 0" → c a natural number with NeZero c; reading of j.
17. `Data.endPeriod_le` step 3 (a second-reader messagec; CrudeRows.lean 162–165): "the end level contains the principal level of
    gridLevelGen" → it contains the principal level K(g^{b₁}) of the natural number levelNorm(1)·g^{b₁}, which lies in
    the grid modulus ideal (`Data.norm_mul_gProd_pow_mem_modulus`, new import from 143); not the inclusion of
    `endLevel_le_principalLevel` (π̄^{b₁}). Text: + the bound is proved at the trivial twist only.
18. `Data.hasRoute_succ` summary and step 6 (a second-reader messagec; CrudeRows.lean 50–63): "cost 2j each" → a denominator of cost j
    and an order increase 2j per ladder; d's costs add to 2j + 1 ≤ 4j + 2, HasRoute using one bound 4j + 2 for both.
    `Data.descent_past_gridPathMap` summary: "the costs multiply" → the denominators multiply, their costs add.
19. `Data.gridPeriod_climb` step 4 (a second-reader message; CrudeRows.lean 113–116): + line 116 (`seal HCParam.dsKernel`) is the next
    command, counted by the line census; the induction closes on line 114.
20. `Data.crude_rows`: "isomorphism ι" → an l-adic place ι (PadicPlace l, an embedding ℂ → ℂ_l; AdicRingHomExt.lean 87).
21. READMEs of the three chunks: pointers to this section; 147-c also explains the equation proof of
    `Data.IsShortSum.bind` (lines 146–147, sampled by a second-reader messagec) and why `LValueRatio` has no proof file.

### Checked and found already right, or not applied

* a second-reader messagec's spanning statement of `Data.crude_rows` (c : twists → ℂˣ, CostsSquares 2m², the span is everything, the
  bound for the untwisted lift) and its remark on β: the dossier already chooses a unit t with β·t = β/β (step 6) and
  never cancels β; unchanged apart from item 20.
* `Data.hasSum_inner_triLift` step 6.1 (the `·` at line 91 is an argument placeholder): the claim already says so; the
  step keeps kind `case` because the checker's layout reading requires it; unchanged.
* The proof passages of a second-reader message (a, b, c) and a second-reader message were compared with the proof summaries; apart from the items
  above they agree with the dossier. The nine-line `erw` (AlgebraicPartConjugates 69–77) and `simp` (ChainNorms 28–36)
  stay indivisible leaves.
* Binders: the 72 members on Lean's word (derived by rule, "not printed by Lean") are unchanged; no Lean output is
  available here.
* `freitag` (Freitag's lemma, SingularForms.lean 248) has no `by_name` record in a second-reader message…0032; its first-reading label
  stays, without a `literature` record.

### Digests and checks

- dossier digest of 147: old `69785ee85df12aad3abc64fe66d260b8ac08d2e7b37f6659300e0586245df3cd` → new
  `6c7d75fd961f055cabe98a3925770e53bd7756444887657f48cd8e8c6b955e99`.
- chunks: 147-a `21be9b69…` → `27a87225920260566aee4fccddf774c5e3d1ba04851baf1c7a147145c4aa7e23`; 147-b `9e880c13…` →
  `dd547f30837f3ea1d18e8c1d7e40dea0261f08473e75ef2b63a4df545da04930`; 147-c `a7a0211f…` →
  `418334953b0069c1a81d96c3e71237d20ece5e734dfb9217511310751080ff7a`.
- `python3 tools/rb.py check 147-a`, `147-b`, `147-c` and `147`: exit 0 — unit 147: 305 of 305 statements at their lines;
  122 structured proofs, 933 steps, 879 leaves (longest 9 lines, an indivisible leaf; bound 8); typed facts 68 of 68;
  imports quoted 241 of 241 (two new: `map_finMultiplier_mul_conj`, `Data.norm_mul_gProd_pow_mem_modulus`); arguments
  accounted for 2627 of 2627 (72 members by Lean's own signature, which this check cannot confirm).

Cost: about 35 minutes of wall time for the three units 143, 147 and 132 together (08:22Z–08:57Z by `date -u`, the start estimated from the first command), shared among them; tokens not reported by the client.
