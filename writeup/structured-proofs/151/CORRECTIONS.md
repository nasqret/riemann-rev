# Corrections to the dossier of unit 151 (the endgame), 2026-11-26

Correction reader: a Claude agent (Opus 5.5) acting as reader, the only writer of this folder since the first
reader finished. Every correction was checked against the pinned source (`lsernau/grh-lean` @ `72fead1`,
`grh-compact/src`) before it was applied. Mathlib facts were read at the artifact's pin `56a00585` (raw files of
leanprover-community/mathlib4 at that commit; file hashes in `gen/spec151.py`, `PINNED_FILES`). Nothing was built.
The changes were made in the generator (`gen/spec151.py`, `gen/spec151_members.py`) and the dossier was emitted again.

**Messages applied:** a second-reader message (the second reading of 151: six corrections and the pin-checked zeta facts), a second-reader message
and a second-reader message (Landau, Jutila, `entireL_ne_zero`: verdicts and sources), a second-reader message (statement-boundary overlay), and
the Chapter II writer's findings passed on by the coordinator.

**Digests** (`dossier_sha256` of `check.json`): old `33c3a7b54780483a91864d07897d9590020b8b5526beb87ab41ef2ea6bfb08a1`
(the one the second reader read), new `6390d9d836f2e031261ffa9178ea8bf2307c551ae9d57f0ec95242f80025ec62`.
`python3 tools/rb.py check 151` exits 0 (29 statements, 18 proofs, 121 steps, 87 imports, 124 of 124 arguments).

## What changed (old → new)

1. `lambdaClass` text (a second-reader message #1): + the weight lives on prime powers ν = p^j, the congruence is tested on p^j,
   factor 1 − χ_d(ν) is 0 / 2 or 0 (odd or even j) / 1 for χ_d(p) = 1 / −1 / p = d; the reading as the character
   of ℚ(√−d) needs d ≡ 3 mod 4 (example d = 5, p = 3).
2. `primeError` text (#1): "the normalised error in the weighted count of the primes ≡ 1 mod M that do not split in
   ℚ(√−d)" → a smoothed sum over the prime powers ν ≡ 1 mod M weighted by Λ(ν)(1 − (ν/d)), less log x/φ(M) and the
   constant, with the same note; the instances `Fact (Nat.Prime d)`, `NeZero M` named.
3. Import `chiK` (#1): + it is χ_K of ℚ(√−d) only for d ≡ 3 mod 4.
4. `logDerivMean` text and import `entireL` (#2): principal L̃ "the entire function (s − 1)L(s, ψ)" → its entire
   continuation, with value ∏_{p∣n}(1 − 1/p) = φ(n)/n at s = 1 (`LFunctionTrivChar₁`, quoted at the pin); + ξ (mod M)
   is compared with its twist (mod M·d).
5. `re_logDerivMean_one` steps 1.1, 1.2 (#2, pin-checked): "these must be simp facts of Mathlib at the pin, inferred
   …, not checked" → ζ₁(1) = 1 and ζ₁′(1) = γ are the simp lemmas `riemannZeta₁_one`, `deriv_riemannZeta₁_one`
   (ZetaAsymp.lean 572, 599 at the pin); step 1.1 now says why L̃(·, 1) = ζ₁ (both are (s − 1)ζ(s) off 1, value 1 at 1).
6. Ambient inputs: `riemannZeta₁`, `riemannZeta_eq_inv_sub_mul` re-quoted at the pin (were recalled); new
   `riemannZeta₁_one`, `deriv_riemannZeta₁_one`, `DirichletCharacter.LFunctionTrivChar₁` (quoted at the pin);
   `LSeries_eq_mul_integral'` 150–152 → 155–157 and `residueClass_apply` 262–264 → 218–220 (byte-identical text,
   now at the pin's lines; a second-reader message).
7. `isPolar_primeError` text and import `IsPolar` (#3): + Φ is defined at 1, so (s − 1)Φ(s) vanishes there and Φ has
   no pole at 1; residue formula "r(s) = …/(s(1 − s))" → for s ∉ {0, 1}, with r(0) = r(1) = 0 stated separately.
8. Import `summable_taylor_of_removable` and `IsPolar.eventually_moment_le` step 7 (#3): + H(1) = 0, the removable
   singularity, the extension having Φ's derivatives at 4 (analyticity of H alone would allow a simple pole).
9. `Data.remainder_eq` step 1 (#4; the writer's finding 1): "(−ν)·τ runs bijectively over the places of class ≡ −ν
   mod N₀" (only for ν prime to N₁) → the identity-place convention of `placeOfInt` for ν not prime to N₁ (e.g. ν = 0),
   re-indexing by σ = (−ν)·τ, and the exact test `Parameters.placeClass_placeOfInt_eq_neg_one` (Different.lean
   217–220, a simp lemma used by the step; new import); + the non-unit terms are 0 on both sides.
10. `Data.remainder` text: + the identity convention and (t)⁺ = max(t, 0).
11. `Data.abs_mainHeight_add_remainder_le` step 2 (#5; the writer's finding 2): "∑ λ(ν)·|y/ν − w|⁺ ≤ a·2|y|" →
    "∑ |λ(ν)|·(y/ν − w)⁺ ≤ a·2|y|", each term ≤ 2ν·|y|/ν (w ≥ 0, ν ≥ 1), as at ShortAndEnough.lean 78–81.
12. `Data.mainHeight` text (#6): "k_D = r_D + 1 − m_D the rank of the columns" → the rank n_D(0) = #X₀ of the
    stage-zero hermitian space, not dim Column(D) (`finrank ℂ D.Column`), which Theorems A and B use.
13. `IsPolar.eventually_moment_le` (a second-reader message): `statement_lines` 41–42 (census) → 41–43; new `statement_corrected`
    (span (41,1)–(43,65), hash `68d0ddd3…` = the overlay's = the existing `source_ranges`); text + "the threshold for
    t may depend on R, not on k"; F_k is the statement's own `let`.
14. `entireL_ne_zero_of_primeError_le` text (a second-reader message, quantitative paragraph): + the threshold may depend on d;
    Re ρ > β is strict.
15. Imports `IsPolar.landau`, `entireL_ne_zero`, `exists_entireL_quadTwist_ne_zero` (a second-reader message, a second-reader message): texts
    completed (all hypotheses; y of any sign; one prime d for all ξ at once); new `literature` records with the
    verdicts and sources (Widder II §5 Thm 5b / Montgomery–Vaughan 15.1; two Mathlib results at the pin; Jutila
    Thm 2 concerns real characters only, the artifact proves its own per-twist estimate).
16. Import `exists_entireL_quadTwist_ne_zero`: + `census_note`: the census's ξ is a phantom (bound after ∃ d) — the
    writer's and this reader's reading, not Lean's output.
17. Proof summary of `entireL_ne_zero_of_primeError_le` and the unit summary: "zero density" / "zero-density input"
    → one prime d whose twists of all characters mod M have no zero in the box, proved by the artifact's own estimate.
18. `Data.projectedPoincare`, phantom binder: + the writer and the second reader read the source the same way.
19. `Data.exists_family_covolumeSq_le`, `binders_lean`: + the second reader's reading and the writer's, from
    New/Main.lean:122 (`D.exists_family_covolumeSq_le.elim fun n ⟨y, …⟩`); still not Lean's output.
20. README: pointer to this file; the Mathlib note updated; 87 imports.

## Not applied, and why

* Nothing of the six corrections was rejected. One qualification: the writer's reason for finding 1 ("those terms
  vanish because every prime dividing N₁ has χ_K(p) = 1", Different.lean 54–58) is true but is not what Lean's step
  uses: the simp set at ShortAndEnough.lean 92–93 contains no `chiK_eq_one_of_dvd` (which has no simp attribute);
  the @[simp] lemma `placeClass_placeOfInt_eq_neg_one` (Different.lean 217–220) decides the count. The claim states
  the Lean route and mentions the writer's reason as a second one, "not used by this step".
* a second-reader message #2's advice on a change of level (factor 1 − ψ(p)p^(−s), ψ ≠ 1 or s ≠ 1) concerns the note; no step of
  151 changes level (`LFunction_changeLevel` is not used here).
* Open, as before: the binders of `Data.exists_family_covolumeSq_le` and the order of goals after `refine` await
  Lean's own output.

Cost: about 40 minutes of wall time for the four units together (07:35Z–08:15Z by `date -u`, start estimated from
the first files written); tokens not reported by the client.
