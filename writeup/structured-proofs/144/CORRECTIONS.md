# Corrections to the dossier of 144 (Elementary divisors of a Frobenius-twisted Hecke operator: twisting data, Frobenius inequalities for least terms, interlacing-cone volumes, flag counts and an approximate projector)

## 2026-11-26 — statement-boundary overlay (a second-reader message)

Source: the second reader's a second-reader message (`exchange/to-claude/a second-reader message/statement-range-inventory.json`, sha256 1749e406…). The census ends a statement at its first top-level `:=`; in the members below that `:=` belongs to a `let`/`letI`/`have` inside the type (or, where said, the census runs into an equation-style proof), so the census's statement lines stopped before the conclusion. Each declaration was read in full at the pin and the overlay's span confirmed (it ends just before the declaration's own `:=`). Applied by the generator: `gen/rbgen.py` (in main, after members and imports are built) calls `gen/statement_overlay.py`, which gives each listed member `statement_lines` (corrected), `statement_span` (span + SHA-256), `statement_lean_full` (the whole statement) and `statement_basis`, removes a truncated `statement_lean` (`rb.py check` compares `statement_lean` with the census's lines and refuses a longer quotation), and extends the quoted lines of imports to the end of their statements.

### Members (statement lines census → corrected; conclusion old → new)

- `volume_inter_slab_eq_signed_sum` (New.TwistedHecke.InterlacingCone:47:7; assignment inside type, manual review): lines 47–48 → 47–50. The overlay's manual-review case (an absolute-value bar `|` follows the `let`); its source reading, that |det(…)| defines Δ and the signed volume identity is the conclusion, is confirmed: the statement ends at line 50 before ` := by`. Old quotation stopped at `: let Δ τ` (line 48). Text already complete: vol(Ω ∩ slab k D) = Δ(id)/k!·(∑_{τ∈S_k} sgn(τ)/Δ(τ))·vol(slab k D), Δ(τ) = |det(1 − q⁻¹τ*)| → unchanged; its binders_note on the section variable k still holds.

### Proof steps and summaries

- volume_inter_slab_eq_signed_sum.json steps 0 and 0.1 (owning lines 48–50 of the statement because the line census takes the `let`'s `:=` for the start of the value, and the opening `|` for an equation arm): their claims now say that lines 48–50 are the rest of the statement (lines 47–50) and state it; the check passes as before.

### Imports re-quoted to the end of their statements

- none affected

### Not applied

- Nothing: every overlay span of this dossier was confirmed by reading the source.

### Digests and check

- dossier digest (`dossier_sha256`): old `0908f8d4d614c63956dcc4c6faf54c2ceb92edc02af553c9eed26d3abf5c6125` → new `e94707c028f3cced800c86d70e0fa704cdb2f01dfdd3600a27f2a205521cb901`
- `python3 tools/rb.py check 144`: exit 0 — unit 144: 78 of 78 statements at their lines; 32 structured proofs, 357 steps, 320 leaves (longest 8 lines, bound 8), 357 steps quote their lines; typed facts in the source: 50 of 50; imports quoted: 31 of 31; arguments accounted for: 930 of 930

## 2026-11-26 — second reading (a second-reader message)

Correction reader: a Claude agent (Opus 5.5), the only writer of this folder for this pass. Message applied: the second reader's
a second-reader message (second reading of the frozen dossier `0908f8d4…`; its points concern texts that the overlay pass did not
touch). No `by_name` statement-strength record of a second-reader message/0011/0012/0017/0019/0024/0032 names a member or an import of
144, so no `literature` record was added. Every correction was checked against the pinned source (`lsernau/grh-lean` @
`72fead1`, `grh-compact/src`); the Mathlib facts were read at the artifact's pin `56a00585` (raw files of
leanprover-community/mathlib4 at that commit, file SHA-256 in `gen/mathlib_pin.py`). Nothing was built. Changes were made
in the generator — `gen/r1.py`, `r2.py`, `r5.py`, `r6.py`, `r7.py`, the new `gen/mathlib_pin.py` (the quotes), and
`gen/rbgen.py` (a member may now give its whole argument list on `binders_basis` "lean") — and the dossier was emitted
again with `python3 reading/units/144/gen/gen.py`.

### What changed (old → new)

1. `TwistingData.exists_depth_factorization`, step 18 (ElementaryDivisors.lean 121–122): "l(γ) the least l with
   w^l ∤ (ρ(g)F)_γ for some g or ⌈x − ω·γ⌉₊ < l; L: minimality; G: the property at l(γ)" → l(γ) with ¬B_γ(l(γ)) and
   B_γ(l(γ)+1) from the successor lemma: L = w^{l(γ)} divides every translated coefficient at γ and l(γ) ≤ ⌈x − ω·γ⌉₊;
   G = w^{l(γ)+1} ∤ (ρ(g(γ))F)_γ or ⌈x − ω·γ⌉₊ < l(γ) + 1 (`Nat.exists_not_and_succ_of_not_zero_of_exists`,
   Mathlib Data/Nat/Order/Lemmas.lean 44–45: ∃ n, ¬p n ∧ p (n + 1)).
2. Same proof, step 20 (126–131): "w^{l(γ)} ∤ …, then l(γ) + depth(γ) > x … root lemma (…, the constant labelling,
   weights ω, l = 0, …); or ⌈x − ω·γ⌉₊ < l(γ)" → w^{l(γ)+1} ∤ …, then x ≤ l(γ) + depth(γ) (equality allowed: the term
   `fun d : _ ≤ x ↦ hg …` refutes depth(γ) + l(γ) + 1 ≤ x), and the root lemma at the constant Levi labelling τ = 0
   and the adic order l = l(γ); or ⌈x − ω·γ⌉₊ < l(γ) + 1. The call `T.root_lemma i ha.ne 0 ω _ (f := …)` (line 128)
   fills `root_lemma i (ha : a ≠ a') τ c {f α} (l : ℕ) (h) (h0 : ¬T.w ^ (l + 1) ∣ f.coeff α) (hτ) (hc)`
   (RootLemma.lean 88–91): the 0 is τ, and `_` is l, fixed to l(γ) by h0 (the case hypothesis).
3. Same proof, step 19 (123–125): + why H holds: ⌈l(γ) + ω·γ − ω·δ⌉₊ ≤ l(δ) by minimality, and L at δ.
4. Same proof, step 23 (134): + "in both cases x ≤ l(γ) + ω·γ" (ω·γ = depth(γ) − excess_i(γ)/2 ≥ depth(γ) when
   excess_i(γ) ≤ 0; in the cutoff case ⌈x − ω·γ⌉₊ ≤ l(γ)).
5. Same proof, summary: "the number of τ < x with t_i ∤ w^τ is its valuation" → m_i = #{τ < x : t_i ∤ w^τ} counts the
   initial failures and t_i ∣ w^{m_i}; m_i is not the valuation in general (w = π², t_i = π in a discrete valuation
   ring: m_i = 1, valuation 1/2 when v(w) = 1); "(iv) … a term least for valuation plus the weight ω … weighs at least
   x, by the root lemma" → the argument of items 1–4.
6. Same proof, step 10 (106–108): "(t_i ∣ w^x and O is a valuation ring)" → the τ < x with t_i ∤ w^τ are the first m_i
   (divisibility by w^τ is monotone in τ) and t_i ∣ w^x; m_i need not be the valuation.
7. Same member, text: "there are square matrices Q, d over O, Q indexed by (E × Fam) × (X × Fam) …" → Q has rows
   E × Fam and columns X × Fam; only d (rows and columns X × Fam) is square; R has the type of Qᵀ (lines 78–81:
   `∃ (Q d : Matrix _ _ O) (R : type_of% Qᵀ), (Q * d = of fun (e, α) (x, β) ↦ …) ∧ d.det ∣ …`).
8. `TwistingData.exists_projector`, summary: "Key: for a Levi-invariant tuple, y·Z(m)F ∈ w^c·O" → key needs the
   conjugation hypothesis e and the coefficient condition H on the contributing rows (zero product of values, or the
   hypotheses e and g of `pow_dvd_coeff_conj_frobOperator`: equal row and column indexWeight-weights at j ≠ i, a gap
   > 2c + 1 at i; FrobeniusFactors.lean 102–107; ElementaryDivisors.lean 167–178); invariance alone fails
   (evaluation at the identity is invariant and sends the generic Frobenius operator to 1, so the pairing can be 1);
   the means supply H (h1, h2; lines 182–185); scalar p^{(k+k²)o₀N·N}, y tested at θ − (4c + 2).
9. `TwistingData.hasType_twisted_hecke`, text: "the index of Y(range f) + p^m·range f in range f divides p^l" →
   IndexDvd L (Y(L) + p^m·L) (p^l), L = range f: every finite family in L has a square matrix over O with determinant
   dividing p^l whose row combinations lie in Y(L) + p^m·L (New/Core/ModuleIndex.lean 20, 55–56); a determinant
   condition, not a cardinality, meaningful also with torsion or an infinite quotient.
10. Same member, proof summary and step 5 (229–230): + the dimensions are over the residue field κ_O of O (S = T mod 𝔪),
    which can differ from the residue field of W (q = P^N elements); κ_O has characteristic p because p is not a unit
    in O (`CharP.of_eq_zero S.prime ((residue_eq_zero_iff _).2 hp)`).
11. Same proof, step 6 (231–235): "(Q, d, R, …) for e ↦ (src e, g e)" → for s(h, e) = (h, src e) and the transposed
    matrices g(e)ᵀ = transposeGL(g e), whose inverse cosets are those of hs (line 221); the second factorisation uses
    the projection (h, (x, b)) ↦ (h, x) and the inverses b.out⁻¹ of the chosen coset representatives (lines 234–235);
    + the transposes matter for the symmetry hρ used at the end (line 261).
12. Imports: new `IndexDvd` (New/Core/ModuleIndex.lean:20, unit 149) with its definition; `HasType`'s text now spells
    out its arguments and points to it.
13. `TwistingData.excessWeight`, text: + the case a = a′ (TwistingData.lean 81–82: then u_s = ū_s = (a, s), the terms
    add, (a, i) weighs 1 − 1/q and (a, s), s ≠ i, weighs 0, using `one_add_val_sub_one_sub`, lines 144–145, N > 0); the
    separate weights of u_s and ū_s now stated for a ≠ a′ only.
14. `TwistingData.translatesIn`, text and binder τ: "a labelling τ of Fin k (its codomain is not written; ℕ in every
    use)" → τ : Fin k → ℕ, fixed by the call `@levi k W _ τ` (TwistingData.lean 86; Lib/General/LinearAlgebra/
    ExtendColumns.lean 112, 175).
15. `prod_mul_volume_inter_slab`, text: "the cyclic interlacing cone fills the share 1/[number of full flags over a field
    with q elements] of the slab" → an identity for every real P > 1 and every D, multiplicative, true also when the slab
    has volume 0; the flag count only when q = P^N is a prime power (N = 1, P = 3/2, k = 2 give 5/2). Summary: "the
    ratio vol(Ω ∩ slab)/vol(slab) …" → vol(Ω ∩ slab k D) = C·vol(slab k D); the only volume cancelled is that of the
    one-letter test slab slab k 1, shown positive and finite (InterlacingCone.lean 116, 130–135).
16. `volume_sum_mem_Icc_le`, text, summary and step 3: "integrate the first coordinate x ∈ [0, D] … ∫_0^D" → D of either
    sign (when d ≤ D < 0 the set is empty); the integrand is supported in the unordered interval uIcc D 0 and the
    integral is taken over uIoc D 0 (Counting.lean 149–159, `(s := .uIcc D 0)` on line 154).
17. `TwistingData.index_mul_finrank_excessCond_le`, summary and steps 1, 3, 4.1–4.5, 5, 7: the old claims mixed the rank of
    the statement with the variable Lean renames at line 176 (`obtain ⟨_ | k, …⟩ := k`) → k is the rank of the statement
    and k′ = k − 1 Lean's renamed variable: τ = (h + N(k+1))σ; slab endpoint n + k + 1 → D(j) = n + k + 1 + Σ_b τ(b, j);
    simplex bound |(e^{1/h}n)^{k−1}/(k−1)!|; the level bound D(j) ≤ e^{1/h}·n from the size condition
    (h + N(k+1))·k·P^{3a'} + k + 2 ≤ n/h. Step 4.2: "[GL_k(W) : ℐ], which is the index of the lower Borel subgroup in
    GL_k of the residue field" → [GL_k(W) : ℐ] ≤ [GL_k(κ_W) : B] by a relative-index inequality (`index_comap`,
    `relIndex_le_of_le_right`, `relIndex_top_right`; lines 184–186).
18. `volume_inter_slab_eq_signed_sum`, binders: seven entries from m (the census's text reading) → eight entries
    {k} {m} (P) {v} (hP) (D) {Ω} (hΩ) on `binders_basis` "lean", with `binders_lean` beginning "NOT PRINTED BY LEAN"
    (read from the source: section variables of line 10 named by the statement lines 47–50, and the explicit
    application `@volume_inter_slab_eq_signed_sum k 0 P ⊤ q 1 (pieriCone ⊤ P) (by …)` at line 130 with eight arguments);
    text and `binders_note` updated. The check therefore reports "1 members by Lean's own signature": that is this
    reading, as in unit 151's `Data.exists_family_covolumeSq_le`, not Lean's output.
19. Ambient inputs (the message's last paragraph), quoted at the Mathlib pin: `Module.subsingleton_tensorProduct
    (Nakayama), LinearMap.liftBaseChangeEquiv` ("a finite module …") → `IsLocalRing.subsingleton_tensorProduct`
    (LocalRing/Module.lean 91–92, `[Module.Finite R M]`; the first reading had the wrong namespace — ClassMeans.lean
    opens IsLocalRing) and `LinearMap.liftBaseChangeEquiv` (not quoted, as before); step 2.1 of
    `ClassMean.eq_top_of_eval_monomial` cites the corrected name and says the quotient is finitely generated.
    `Module.free_of_flat_of_isLocalRing, flat iff torsion-free over a Bezout domain` ("A finitely presented flat module
    over a local ring is free; over a Bezout domain … flat is torsion-free") → `Module.free_of_flat_of_isLocalRing`
    (LocalRing/Module.lean 298–299: finitely generated, not finitely presented) and
    `Module.Flat.flat_iff_torsion_eq_bot_of_isBezout` (Flat/TorsionFree.lean 91–94: an equivalence; ClassMeans.lean
    107–108 uses torsion-free ⇒ flat, `.2`); step 12 of `ClassMean.exists_mean` says so.
    `MvPolynomial.IsHomogeneous.eq_zero_of_forall_eval_eq_zero_of_le_card` (MvPolynomial/Homogeneous.lean 458–460,
    n ≤ #R) and `tendsto_card_div_pow_atTop_volume` (BoxIntegral/UnitPartition.lean 456–459: bounded, measurable, null
    frontier) now quoted. New: `Nat.exists_not_and_succ_of_not_zero_of_exists` (item 1).
20. README: a pointer to this section.

### Not applied, and qualifications

* Nothing of a second-reader message was refused; every point was confirmed in the source at the lines cited above.
* Two ambient points were already right in substance: the homogeneous zero test already read "degree at most the
  cardinality" (equality allowed) and the lattice-point limit already named boundedness, measurability and a null
  frontier. They are now quoted at the pin; their texts were not weakened or changed in meaning.
* Notation: the message writes K for the original rank in `index_mul_finrank_excessCond_le`; the dossier keeps k for
  the rank of the statement and writes k′ = k − 1 for Lean's renamed variable, because K is the field of Counting.lean.
* Steps 0 and 0.1 of `volume_inter_slab_eq_signed_sum` stay (the second reader calls them bookkeeping for the line
  census's truncation; without `source_ranges` the check needs them). No `source_ranges` were added.
* Open, as the second reader says: the 23 binder entries that the first reader flagged in 17 members (duplicated or
  not expected in Lean), native signatures and replay of the long `simp`/`grind` blocks await Lean; of the 20 ambient
  records, the 14 not quoted keep "statement read from its name and use".

### Digests and check

- dossier digest (`dossier_sha256`): old `e94707c028f3cced800c86d70e0fa704cdb2f01dfdd3600a27f2a205521cb901` → new `adefd18a23a5081b2f36a4334ee00a35f38edd517abe284b78bc428c734bbb94`
- `python3 tools/rb.py check 144`: exit 0 — unit 144: 78 of 78 statements at their lines; 32 structured proofs, 357 steps, 320 leaves (longest 8 lines, bound 8), 357 steps quote their lines; typed facts in the source: 50 of 50; imports quoted: 32 of 32; arguments accounted for: 931 of 931 (1 members by Lean's own signature, which this check cannot confirm)

Cost: about 25 minutes of wall time (≈08:15Z–08:40Z by `date -u`, the start estimated from the first scratch files);
tokens not reported by the client.

