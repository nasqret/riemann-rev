# Corrections to the dossier of 150 (Theta functions of the CM curve: periods and scales, tight frames, the integral vacuum, Galois conjugates of jets, and divisibility of jets at non-split primes)

## 2026-11-26 — statement-boundary overlay (a second-reader message)

Source: the second reader's a second-reader message (`exchange/to-claude/a second-reader message/statement-range-inventory.json`, sha256 1749e406…). The census ends a statement at its first top-level `:=`; in the members below that `:=` belongs to a `let`/`letI`/`have` inside the type (or, where said, the census runs into an equation-style proof), so the census's statement lines stopped before the conclusion. Each declaration was read in full at the pin and the overlay's span confirmed (it ends just before the declaration's own `:=`). Applied by the generator: `gen/gen.py` (after the records are built) calls `gen/statement_overlay.py`, which gives each listed member `statement_lines` (corrected), `statement_span` (span + SHA-256), `statement_lean_full` (the whole statement) and `statement_basis`, removes a truncated `statement_lean` (`rb.py check` compares `statement_lean` with the census's lines and refuses a longer quotation), and extends the quoted lines of imports to the end of their statements.

### Members (statement lines census → corrected; conclusion old → new)

- `Parameters.mem_raises_of_jet_bound` (New.Curve.ConjugatesOfJets:121:7; assignment inside type): lines 121–125 → 121–126. Old quotation stopped at `let k := thetaKernel hκ c ha hb K` (line 125). Text already complete: k.ω(1, x·d·y)Ψ ∈ raises(k, 1, 1, B) → unchanged.
- `Data.exists_isFrobPacking` (New.Curve.DepthPairs:34:7; assignment inside type): lines 34–36 → 34–38. Old quotation stopped at `let L := …` (line 36). Text already complete: ∃ i y, IsFrobPacking(p, n, i, y) ∧ [with L = forcedPart + ∑ v_p(depthLossInt)] ((χ_K(p) = −1 ∧ i = 1 ∧ ∑(v_p(n_s!) − y_s) ≤ L) ∨ ∑((1/(p−1) − ρ_p)n_s + 4b₂ − y_s) ≤ L) → same, with ρ_p = nonsplitWeight(P.d, p) and b₂ = D.b₂ written out.
- `norm_schurJet_le` (New.Curve.JetDivisibility:65:7; assignment inside type): lines 65–69 → 65–71. Old quotation stopped at `let N := card n'; let B := …; let m := …` (line 69). Text already complete: IsIntegralOnNullCone(pr, S, ϖ, θ, B, Θ) → |schurJet_κ(Θ)_{i′,i}| ≤ p^{m − ((1/(p−1) − ρ)B + ω∑ couplingCount − |Φ|N³(⌊log_p B⌋+1))} → unchanged.

### Proof steps and summaries

- The first steps of the three proofs (Parameters_mem_raises_of_jet_bound.json step 1, Data_exists_isFrobPacking.json step 1, norm_schurJet_le.json step 1) already say that their lines end the statement and are owned there only because of the line census; unchanged.

### Imports re-quoted to the end of their statements

- `CMLattice.complex_multiplication_theta` (unit 110): lines 38–39 → 38–43. Text was complete; "cluster point at infinity of the finite ideles a(S)" corrected to a cluster point β (in the finite adeles of K) of S ↦ a(S), and the `let D := galConjugate C σ` named.
- `Parameters.relDifferent_spec` (unit 152): lines 299–300 → 299–301. Text already complete (y ∣ N₁, (y) = different of E/K, 𝓞_E = 𝓞_K[z]); unchanged.

### Not applied

- Nothing: every overlay span of this dossier was confirmed by reading the source.

### Digests and check

- dossier digest (`dossier_sha256`): old `7f875a3bb90b1e6737fb4493a2b9ab1ae3e26136add860d6e5c6b580938a9083` → new `45742a354039fd7ebf7b3736db3ab4915cc42b1067104e3ae54b0e885a7a3e77`
- `python3 tools/rb.py check 150`: exit 0 — unit 150: 89 of 89 statements at their lines; 36 structured proofs, 435 steps, 407 leaves (longest 9 lines, bound 8), 435 steps quote their lines; typed facts in the source: 39 of 39; imports quoted: 72 of 72; arguments accounted for: 768 of 768


## 2026-11-26 — faults found by the writer of the notes (coordinator's message, checked against the Lean)

- `CMLattice.exists_formal_parameter`, step 7 (lines 158–159): the claim said that (ζ^i, 1) lies in normPairClosure(d). The source applies `mem_normPairClosure_of_pow_eq`, whose conclusion is `(ζ, ζ ^ (p + 1)) ∈ normPairClosure d` (Lib/CM/KroneckerLimit/LogTheta.lean:115–116), to ζ^i: the pair is (ζ^i, ζ^{i(p+1)}). The claim now says so and lists what hL then gives (φ(ζ^i z), exp(ζ^{i(p+1)}L)·θ(ζ^i z) and (ζ^{i(p+1)}L − L(ζ^i z))′ in 𝔬[[φ]]); the lemma is cited in `uses` and added as an import with its statement.
- Same proof, step 35.6 (lines 229–233): the factors are rescale(ζ^i) of the second clause of hL at −i (`(hi (-i)).2.1`), i.e. exp(ζ^{−i(p+1)}·L(ζ^i z))·θ(z), not exp(L(ζ^i z))·θ(z); the claim now has the weight ζ^{−i(p+1)} (which is what makes ψ a series in the degrees ≡ p + 1 mod m in step 35.7).
- Phantom census arguments τ (`Data.gain`, `Data.collisionSum`) and h (`couplingCount`): their binder readings already said "NOT an argument of the Lean declaration (by the source)", with the uses that pass the real arguments; unchanged.

- dossier digest: `45742a354039fd7ebf7b3736db3ab4915cc42b1067104e3ae54b0e885a7a3e77` (after the overlay) → `a6ad64afc46fd89262feb5196cf0f18076d71f28d6552a6c02ad7ea64c52e95d`
- `python3 tools/rb.py check 150`: exit 0 — unit 150: 89 of 89 statements at their lines; 36 structured proofs, 435 steps, 407 leaves (longest 9 lines, bound 8), 435 steps quote their lines; typed facts in the source: 39 of 39; imports quoted: 73 of 73; arguments accounted for: 768 of 768


## 2026-11-26 — second reading (a second-reader message) and literature

Correction reader: a Claude agent (Opus 5.5), the only writer of this folder for this pass. Messages applied: the second reader's
a second-reader message ("CM curve, 89 readings and the character in the log-theta rotation"; frozen dossier `7f875a3b…`) and, for
the imports that cite named classical results, the `by_name` rows of a second-reader message (`part-1-named.json`, SHA-256
`1b6fa149…`). Of the other payloads with `by_name` records (a second-reader message, 0011, 0012, 0017, 0019, 0024) none has a row
for an import or member of 150; the overlay a second-reader message was applied before (section above). Every correction was read
against the pin (`grh-compact/src` at `72fead10`); nothing was built. Changes were made in the generator's inputs
(`gen/spec_*.py`; new `gen/spec_Literature.py`; `gen/gen.py` attaches the records) and the dossier was emitted again
with `python3 gen/gen.py`; no output was edited by hand. Quotations, lines, spans and typed facts are unchanged; only
words, two `uses`/`ambient_uses` and the records below changed (14 member texts, 1 binder reading, 7 import texts,
4 `literature` records, 11 proof summaries, 32 step claims, 1 ambient input).

### Changes (old → new), by the number of a second-reader message

1. Character in the rotation average (FormalParameter 158–159, 229–238; LogTheta 99–100, 115–116, 144–149;
   IsogenyIntegrality 140–142). Step 7 and 35.6 were already right (writer-findings pass). Remaining:
   - `CMLattice.exists_formal_parameter` summary: "torsion translates are θ^N times units" → θ^{(nm)²} times an
     integral u ∈ 𝔬[[φ]] (no unit asserted); the norm pair (a, a^{p+1}) and the weight a^{−(p+1)} extract the degrees
     ≡ p + 1 mod m (an unweighted average would give degree 0 mod m).
   - step 7: + the second coordinate ζ^{i(p+1)} is not 1 in general (order p − 1 at an inert prime, i = 1).
   - step 35.7: "write the sum over the rotations as m times a congruence part" → ∑_{i<m} ζ^{−i(p+1)}L(ζ^i z) =
     m·congruencePart(m, p + 1, L) (`congruencePart_eq_sum` with r = p + 1, IsogenyIntegrality 125–126).
   - import `rescale_translate_eq_theta_pow_mul`: + u is integral, no unit for an arbitrary translate. The unit of
     `exists_hasLargeSplit_of_pairs` step 14.4 (Θ(0) = 1, Ψ(0) = 0; DepthPairs 132–133) was already stated; unchanged.
2. Coefficient fields and quantifiers.
   - `CMLattice.jet_theta_prod_integral` text and binder c: "c : I → σ → ℂ" → c : I → σ → ℂ_p (the hypothesis k
     multiplies it by ιₚ(δ̄)⁻¹ ∈ ℂ_p, FormalParameter 28–29); δ, y complex; Q over ιₚ⁻¹(𝔬); |…|_p ≤ 1.
   - `CMLattice.exists_formal_parameter` text: + |π| = p^{−1/2} (p = d) or p^{−1} (inert); the first part for every p,
     the second under χ_K(p) ≠ 1 and p ≥ 13; N, κ depend on n and serve every y with ny ∈ Λ; V may depend on y.
   - `CMLattice.katz_divisibility_limit` text: + the witness f depends on (p, ιₚ, n); a lower bound, not one series
     for all n, not an equality (KatzDivisibility 15–17).
3. Determinant in the divisor position (JetDivisibility 34–47; ModuleIndex 17–20, 66–72).
   - `exists_null_coupling_frames` summary and step 4: "a determinant divisible by those roots" → det M_{τ,h}
     divides the product A_{τ,h} of the selected roots (hM).
   - step 7: "If x divides det M_{τ,h} then |x| ≤ |det M_{τ,h}|" → |A_{τ,h}| ≤ |det M_{τ,h}| because det M ∣ A
     (`Valuation.Integers.le_of_dvd`, new ambient input; uses step 4).
   - steps 11–12: "exponent from the selected rows ≥ the coupling count" → `congr!` reduces the inequality of powers
     of |θ| to an equality of exponents, which holds after the minima are split (an inequality would point the wrong
     way for a base in [0, 1]); the equality also covers θ = 0.
   - import `IndexDvd.of_det_dvd`: "a matrix whose determinant is divisible by d" → the full statement: det A ∣ z
     and A·O^ι ⊆ N give IndexDvd(O^ι, N, z), matrices with det m ∣ z.
   - `norm_schurJet_le` summary: "the factorials cost at most p^{|Φ|N³(⌊log_p B⌋+1)}·p^{B/(p−1)}" → the factor from
     ∏_x d_x! is ≤ p^{−B/(p−1) + |Φ|N³(⌊log_p B⌋+1)} for B > 0 (sign of the main exponent); text: + ⌊log_p B⌋ is
     Lean's Nat.log, 0 at B = 0 (JetDivisibility 69–71, 98–106).
4. Taylor coefficient and homogeneous part (FrameSections 27–38, 57–61; ZerosCostDegree 162).
   - `Space.taylor_line_eq_subst_jetSeries` summary and step 3(b): "the coefficient of u^k equals the jet along
     (∑ v_i z_i)^k" → k! times that coefficient equals the jet.
   - `Space.jetSeries_eq_prod` summary, steps 2.2–2.3: "the truncation of S to a finite set of monomials containing
     α" → the homogeneous part of total degree |α|, whose value at v is [u^{|α|}]S(v·u).
5. Expansion size and shifts (ConjugateGenerator 37–41, 57–65; ConjugateJetDefs 15–17, 30–36).
   - `exists_isJetConjugate_generator` steps 4, 5, 14.1, 14.5: "|K| = N^{2f|n|}" → (N²)^{2f|n|} = N^{4f|n|} (norm
     parameter (Ne)² at e = 1); the logarithm 4f|n|·log N ≤ 4N²|n| is what the additive 4 of C = ⌈M⌉ + 4 absorbs.
   - `exists_finitePart_of_isTightFrame` text (3): "∑_j m′·ℓ(ϱ(αx_j)vac)·ϱ(−αx_j)F" → ∑_j m′·ℓ(ϱ(finVec x_j)vac)·
     ϱ(finVec(−x_j))F (no α, shifts distinct from finiteImage γ = α⁻¹γ; the imported docstring's α is not in the field).
6. Conjugation conventions.
   - `Parameters.periodFactor` text and import `CMLattice.chowla_selberg`: "for every σ ∈ Aut(ℂ)" → σ ∈ Aut(ℂ/K)
     (galConjugate's σ : Gal(ℂ/QuadField d), ConjugateCurve 11, 71; FormalHeight 82–84).
   - `exists_isJetConjugate_generator` step 1, 17, 18, summary, and import `complex_multiplication_theta`: "β_σ, a
     cluster point of finite ideles a_S" → a_S ∈ K, β_σ ∈ 𝔸_f(K) a cluster point of their diagonal images; no
     invertibility asserted (FormalHeight 38–43); Aut(ℂ) → Aut(ℂ/K).
   - texts of `exists_isJetConjugate_generator` and `exists_semilinear_isJetConjugate`: "places permuted by
     placePerm" → σ on the coefficients on the left, variables (τ, k) renamed to (π⁻¹τ, k) on the right
     (ConjugateJetDefs 38–42).
   - `exists_semilinear_isJetConjugate` text, summary, step 6: "L : 𝒮(V) → 𝒲_f" → a σ-semilinear endomorphism of
     𝒮(V), `V.finitePart.subtype ∘ₛₗ L` (ConjugatesOfJets 173–175, 184); identities on 𝒲_f.
   - step 21.3: "σ(per·conj Φ_τ(w)) = t·conj Φ_{π(τ)}(w)" → the entire coefficients: Ω₀/(NA)·per = s₁/N and
     Ω_σ/(NA)·t = σ(s₁)/N, matched by σ (FrameSections 93–97; t at ConjugateGenerator 51–52).
7. Geometric sums (LiveSum 96–102, 35; DepthPairs 23–26).
   - `hasSum_live_inv_pow` summary and step 1: "c/2 times (∑ p^{−e} − ∑ (χ/p)^e)" → term c/(1 − χ)·(p^{−e} − (χ/p)^e),
     0 at e = 0 (multiplier c/2 inert, c ramified; sums cp/(p² − 1) and c/(p − 1)).
   - `Data.summable_localAsk` text: "dominated by the family of hasSum_live_inv_pow" → bounded by its norm, |y|/p^e
     on the live indices (y any real).
   - `Data.IsShortPrime` text: + the congruence reading is for p ≥ 1; IsShortPrime(D, 0) holds (0 − 1 = 0 in ℕ).
8. Packing (DepthPairs 50–56, 66–69, 101–106).
   - `Data.exists_isFrobPacking` step 8.3: n_s − c → n_s ∸ c; step 8.4: "p·y_t ≤ n_t − c, … y_σ ≤ c, so ≤ n_t" →
     incoming count ≤ min(n_t, c) by its minimum; if n_t < c the outgoing count vanishes.
   - step 8.5: "v_p(n_s!) = v_p((n_s − c)!) + …" → ≤, from n_s! ∣ (l + c)! = l!(l+1)⋯(l+c), l = n_s ∸ c (equality
     only for n_s ≥ c).
   - summary and step 9.4: "for each thick s take the unique odd e" → only where an admissible e exists; otherwise
     y_s = 0, thick places without partner included.
   - `IsFrobPacking` and `exists_hasLargeSplit_of_pairs` texts: + at p = d (1) forces y = 0, so b = τ = 0 and the
     bound is 1; no optimal coefficient at n is asserted.
9. Frame witnesses (TightFrameExists 36–43, 116–117, 129–139; WeilDataOfE 24; ConjugateJetDefs 19–25).
   - `norm_iota_periodFactor` step 1: "for every integer u" → every infinite place u ∈ P.Φ(s) (galOfPlaceInt takes
     a place).
   - `exists_isTightFrame` summary and step 12: "u_{p,0,1,0} if p ∣ N and 1 otherwise" → 1 = ζ^0 is tried first;
     only if it fails for some τ is p ∣ N deduced and u_{p,0,1,0} used; one index for every τ.
   - "length" in `exists_finitePart_of_isTightFrame`, `thetaProducts`, `exists_isTightFrame`: + the length is the
     scalar of the weighted Gram identity, not the number of vectors or ∑ m_i.
10. Two proof formulas.
   - `sum_pow_eq_zero_of_null` step 1: "a + b = 1 + e(l + l′)" → that for t_i^p·t_i and 1 + e(l + l′ + 1) for
     t_i^p·t_i^{p^e} (ThetaProducts 21–25).
   - `katz_divisibility_limit` step 5.3: "(n+k)!·|(φ^j)_{n+k}| ≤ n!|…|·k!|…|" → factorials inside the p-adic norms
     (KatzDivisibility 22–30).
   - steps 7, 8, 10 and summary: "P∘(X − X^{p^e})", "S̄∘(X − X^{p^e}) = X" → (X − X^{p^e})∘P = P − P^{p^e} = X
     (`natDegree_comp` with p := X − X^{p^e}, KatzDivisibility 35–39).
- Evidence remark (typed-fact fragments): the claims of `exists_null_coupling_frames` 7, `norm_coeff_le_of_deriv`
  2.5 and `exists_isTightFrame` 16 now say that the recorded `typed_fact` is a fragment and give the whole type;
  README item 2(b) says that "typed facts 39 of 39" counts textual matches.

### Literature (a second-reader message, `part-1-named.json`; new `gen/spec_Literature.py`)

Each record: relation, verdict, sources ("title <url>"), record, statement_range (= the row's source_range, checked
equal to the import's quoted lines), catalogue_row_sha256, basis "the second reader's comparison … replaces the
first reading's reference and relation". The generator also checks the row's id, file and file SHA-256 against the
import and the pinned file. The import texts were rewritten from the Lean statements (first-reading labels removed):
- `CMLattice.complex_multiplication_theta` (FormalHeight 38–43): unresolved, row `d296eb5b…`; text "Main theorem of
  complex multiplication … (known result)", σ ∈ Aut(ℂ) → the full statement, σ ∈ Aut(ℂ/K), a(S) ∈ K, cluster point
  of diagonal images, no invertibility, the authors' label, the second reader's relation.
- `CMLattice.exists_unit_coeff_degree_le` (FormalHeight 172–176): weakens, row `950d3595…`; text "g(Z) = ιₚ(a)·Z" →
  Z(g) = ιₚ(a)·Z (`subst g Z`), with all hypotheses (Z(0) = 0, Z₁ = 1, hZ, IsIsogeny(E, E, a, q), q odd, g integral,
  g(0) = 0).
- `CMLattice.norm_a₁_le_one` (IntegralParameter 153): weakens, row `50a2f904…`; text completed (C, p, ιₚ named).
- `CMLattice.one_le_norm_coeff_translatedWp_nonsplit` (FormalHeight 135–137): unresolved, row `9359394f…`; "Height of
  the formal group (known result)" → the statement, the authors' label, the second reader's relation.

### Not applied, and why

- Nothing of a second-reader message was refused; every point was confirmed at the pin. Items stated in a second-reader message as checks that
  passed (its table of sampled passages) needed no change where the dossier already agreed (e.g. 14.4 of
  `exists_hasLargeSplit_of_pairs`, 3(a) of `taylor_line_eq_subst_jetSeries`, the conditional size in
  `isAdmissibleComb_name`).
- Not done: native binder lists (a second-reader message's evidence section) still await Lean's output; no `source_ranges` added.

### Digests and check

- dossier digest (`dossier_sha256`): old `a6ad64afc46fd89262feb5196cf0f18076d71f28d6552a6c02ad7ea64c52e95d` → new
  `c8c9fac7a678429697450b6607c60da32fa27ed915ba2392b0488f520e826b50`
- `python3 tools/rb.py check 150`: exit 0 — unit 150: 89 of 89 statements at their lines; 36 structured proofs, 435
  steps, 407 leaves (longest 9 lines, bound 8), 435 steps quote their lines; typed facts in the source: 39 of 39;
  imports quoted: 73 of 73; arguments accounted for: 768 of 768

## 2026-11-26 — Pass 8: two wording corrections (a second-reader message, a second-reader message)

Correction reader: a Claude agent (Opus 5.5), the only writer of this folder during this pass. Messages: the second reader's
a second-reader message (second reading of the corrected dossier `c8c9fac7…`, which was still the present one: "two phrases still need a
change") and a second-reader message (cross-check against the published edition: both edits are confined to the structured records;
the note already uses the weak inequality and names the coefficient of X^{m+1}). Each item was read against the pin
(`grh-compact/src` at `72fead10`) before it was written; nothing was built. The changes are in the generator's inputs
(`gen/spec_DepthPairs.py`, `gen/spec_FormalParameter.py`); the dossier was emitted again with `python3 gen/gen.py` (the
unchanged generator was run first and reproduced the dossier byte for byte). Only these two strings changed.

### Applied (old → new)

1. `Data.exists_isFrobPacking`, step 8.5 (a second-reader message item 1, a second-reader message row 1; DepthPairs.lean 54–56:
   `v (factorial_dvd_factorial le_tsub_add)`, `← factorial_mul_ascFactorial`, only `grw`, i.e. inequalities):
   “(an equality only when n_s ≥ c)” → “(equality holds when n_s ≥ c, where l + c = n_s; it can also hold when n_s < c,
   and only the inequality is used)”. Checked: with l = n_s ∸ c, l + c = n_s exactly when n_s ≥ c; for n_s < c the
   two valuations can still agree (p = 13, n_s = 13, c = 14: v_13(13!) = v_13(14!) = 1), so “only when” was false. The
   packing argument uses only v_p(n_s!) ≤ v_p((l + c)!).
2. `CMLattice.exists_formal_parameter`, proof summary (a second-reader message item 2, a second-reader message row 2; FormalParameter.lean 164
   (`Z1`: coeff 1 Z = 1), 170–172 (`hX`: the coefficients of Z − X vanish below degree m + 1, `X_pow_dvd_iff.2 hX`),
   172–173 (ϖ from `IsAIC.exists_pow_eq m (-coeff (m + 1) Z)⁻¹`), 181 (`τt : coeff (m + 1) Z = -(ϖ ^ m)⁻¹`)): “its
   inverse Z has only degrees ≡ 1 mod m, and the leading coefficient Z_{m+1} = −(ϖ^m)⁻¹ defines ϖ” → “its inverse Z has
   only degrees ≡ 1 mod m, linear coefficient 1 and X^{m+1} ∣ Z − X, and the coefficient of X^{m+1}, Z_{m+1} =
   −(ϖ^m)⁻¹ (the first nonlinear coefficient), defines ϖ”. Z is a power series; Z_{m+1} is the first coefficient after
   the linear one, not a leading coefficient.

### Verified and already present

- a second-reader message, third paragraph (the pair (a, a^{p+1}) and the weight a^{−(p+1)} of the rotation average, the integral
  transformed theta series, |product| ≤ |det M| in the jet bound, the sign of the factorial exponent, k! times the k-th
  Taylor coefficient, the quantifier on shifts, the size of the vacuum expansion, the four literature records): the
  corrections of the a second-reader message pass above; present, unchanged.
- a second-reader message, row 3 (the Gaussian scale T = N log β of the discrete-series note): unit 133, not this unit; nothing here.

### Not applied

- Nothing refused. Native binder lists (a second-reader message's evidence paragraph: 16 lists) still await Lean's output.

### Digests and check

- dossier digest: old `c8c9fac7a678429697450b6607c60da32fa27ed915ba2392b0488f520e826b50` → new
  `2e0090ec8a535e43e369f8d281078c0d125228b73378af3d071e6d7c88b2b710`
- `python3 tools/rb.py check 150`: exit 0 — unit 150: 89 of 89 statements at their lines; 36 structured proofs, 435
  steps, 407 leaves (longest 9 lines, bound 8), 435 steps quote their lines; typed facts in the source: 39 of 39;
  imports quoted: 73 of 73; arguments accounted for: 768 of 768

Cost: about 25 minutes of wall time for the nine units of pass 8 together (about 15:45Z–16:10Z by `date -u`, the start
estimated from the first backup at 15:51Z), shared among them; tokens not reported by the client.
