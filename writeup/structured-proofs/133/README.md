# Dossier 133: discrete series coefficients near 1, Laplace's method, Bessel functions with a peak

> **2026-11-26, second reading (a second-reader message), statement-boundary overlay (a second-reader message) and literature records:** corrections
> applied by a correction reader; four members carry their whole statement (`statement_span`, `statement_lean_full`),
> four imports carry the second reader's `literature` verdict, and one import was added (`Space.firstMinimum_le_one`,
> 174 imports now). The norm conventions below are confirmed by the second reader. See `CORRECTIONS.md`.

Reader: a Claude reader standing in for astra. Edition `grh-compact` at `72fead102f663d5c7a407964a13dc0cf9d977207`.
Nothing was built. Every statement about what Lean does is read from the source, and the labels below say so.

Unit 133 is `New.DiscreteSeries.{TwoFactorSetup, GaussianShape, MinorExpansion, RestrictionLemma, BesselExistence}`.
It has 37 members, 17 structured proofs (260 steps, 235 leaves, the longest 8 lines, no indivisible leaf), 174 quoted
imports and 36 ambient (Mathlib) inputs. Gate: `python3 tools/rb.py check 133` exits 0 (`verified`, that command).
`python3 reading/units/133/gen/verify.py` checks hashes and quotations again, with code that does not use the tools'
tokenizer (`verified`, that command).

## Where to start
1. **TwoFactorSetup**: the vocabulary. `IsSteep(l, B, e)` (steep weights on M indices, zero weights on X),
   `IsTwoFactor(l, k, j, τ, B, e, φ)` (j : S → U(ε) × U(η); additive imaginary phase φ = phase(l, k, j(·) − 1); U(X)
   embedded diagonally), and θ_{l,k,j,φ} = laplaceIntegrand. The key lemma is `IsTwoFactor.exists_near_one`: close to
   the block-diagonal locus, a translate by the diagonal U(X) is close to 1 and leaves θ unchanged.
2. **GaussianShape** and **MinorExpansion**: `dsCoeff_gaussian_shape` gives ψ_l(g)/exp tr(diag(Λ(l))·lg(g − 1)) ≈ κ ∈ [0, 1]
   for g near 1. It rests on `exists_principalMinor_eq_exp` (second-order expansion of the principal minors of the
   Flensted-Jensen argument y) and on `exists_det_compress_eq_exp_logOneAdd`.
3. **RestrictionLemma**: `IsTwoFactor.laplace_method` is the lower bound ν{‖j₁ − 1‖ ≤ 1} ≤ β^(20(|n|+|m|)²)·|∫θ dν|.
   `IsSteep.exists_isTwoFactor_restriction` builds one instance, the restriction r ↦ (r, ω⁻¹(r ⊕ 1)ω), with ω from
   Lagrange weights; unit 147 uses it. `norm_poincare_period_sub_le` (unfolding of a deep-level Poincaré series) stands
   apart; unit 147 uses it too.
4. **BesselExistence**: the Bessel graph S = 𝖧𝖴 ⊆ G₁(𝔰) × U(κ), its measure and unfolding. The second instance is
   `IsSteep.exists_isTwoFactor_besselPairHom`, at a point x with besselSize(x) ≤ b^(5n). `exists_isBesselFunction`
   then gives `HasPeakAt`. Units 148 (`Data.exists_besselSystem`) and 132 (`HasPeakAt.exists_cut_isCutPair`) use them.

## Conventions of the texts
* Letters follow Lean's local names (n, m, X index types; ε, η signs; l, k parameters; S the group; τ, B, M, e, φ). They
  clash with MEMORY's global letters: k is a parameter here, not the rank of the columns; d is the separation scale of
  the period lemma, not the prime; s is an element of S, not the exponent; σ is simpleRootSum (as in 132-a), not a
  place. The writer should rename them in a note.
* New symbols (each with all explicit arguments):
  * U(ε) = USign(ε), K_ε = maxCompactU(ε), ψ_l(g) = dsCoeff(l, g), Λ(l) = lowestKType(l), μ(l) = paramAddRho(l);
  * a_ε(g) = blockDiagPart(ε)(g), diag(w) = intDiagonal(w), lg(X) = logOneAdd(X), P_p = coordProj(p),
    Δ_p(y) = principalMinor(y, p), m_w(g) = weightMinors(w, g), c_w = kTypeNormSq(w);
  * FJ_l(g, z) = flenstedJensen(l, g, z), deg(l), e_l(g) = dsKernel(l, g), ι_ℂ(σ) = inclMatrix(ℂ, σ);
  * θ_{l,k,j,φ}(s) = laplaceIntegrand(l, k, j, φ, s), phase(l, k, x), subOnePair(j, s) = (j₁(s) − 1, j₂(s) − 1);
  * fr = frameEquiv (y ↦ p⁻¹yp), ν_S = besselGraphMeasure(𝔰), f_E = numInfPlaces(E), K_n(a) = principalLevel(n, a).
  A text says which norm it uses. TwoFactorSetup, GaussianShape and MinorExpansion use the Frobenius
  (Hilbert–Schmidt) norm. RestrictionLemma and BesselExistence (from line 28) use the operator norm.
  GaussianShape opens both scoped norms. I read Frobenius as the default there: its docstring says so, its proof
  invokes the operator norm explicitly, and it applies Frobenius-only lemmas to its own hypotheses. The second reader
  confirmed this from the source (a second-reader message #1: `frobenius_norm_sq_eq_sum` in the proof of lines 18–25, the
  principal-minor lemma applied to the hypothesis of lines 48–54, the operator norm invoked separately at 57–58; in
  RestrictionLemma the ball of the Laplace estimate and the bound on the second component use the operator norm). Still
  a source reading, not Lean's output.
* Definitions, structures and instances carry no `triage`. Instance proofs (closedness, measure properties, right
  invariance) are described in the instance's `text`, not in a structured proof.

## What the census reads wrongly (`heuristic` until Lean is asked)
In 10 members the census's argument list is not Lean's. The dossier keeps the list the check accepts
(`binders_basis` is not "lean": nothing was built). The `reads` of each spurious entry starts "census reading only",
and each member's `reader_note` gives the list Lean is expected to print. To confirm, run `#check @Name` for:
`subOnePair` (Lean also takes n, m, Fintype n, Fintype m: {ε}, {η} have no written type), `IsTwoFactor` (u is bound
by ∀ u ∈ …), `norm_sq_add_re_trace_le` (S, Group S, η, j: j is the bound variable of ∀ i j),
`sum_norm_lie_coordProj_sq` (no binders given: the census stops the statement at `letI a :=`; Lean takes
{n} [Fintype n] (w) (X)), `exists_principalMinor_eq_exp` (section X: the statement's `let X :=`),
`lintegral_unfold_besselGraphMeasure`, `HasPeakAt`, `exists_isBesselFunction` (section s: bound by ∫ s / {s | …} /
fun s), `IsSteep.exists_isTwoFactor_besselPairHom` (s and x: fun s, ∃ x), `besselPairHom` (the census reads
`→*` as an arrow and adds an explicit argument).

The line census takes a statement's first `let … :=` for the start of the proof. The statement lines therefore stand
in `intro_lines`: `sum_norm_lie_coordProj_sq` [18, 20], `exists_principalMinor_eq_exp` [49, 53] and
`IsSteep.exists_isTwoFactor_restriction` [203, 205]. In `norm_poincare_period_sub_le` the statement runs to line 40.
Lines 31–38 are the introduction (8 lines, the bound), and step "0" quotes lines 39–40 as the statement's
conclusion. Since 2026-11-26 these four members carry the whole statement from the a second-reader message overlay
(`statement_lines`, `statement_span`, `statement_lean_full`), and the imports `integral_decay_le` and
`trace_mul_logOneAdd` are quoted to the end of their statements; the proofs keep the line-census basis.

## What I am unsure of (`heuristic`)
The `text` fields were each compared with the Lean statement lines, and the definitions with their definitions. The
step claims of the long `simp`/`grw`/`grind` blocks were reconstructed from lemma names and goal shapes, without
Lean. The least certain are:
* `IsTwoFactor.exists_near_one` 14: the bound Re tr c − Re tr T ≤ (‖T‖ + ‖c‖)·‖c‖ is right (the closing `nlinarith`
  needs it), but which side of the `trans_eq'` identity is which could not be checked.
* `IsTwoFactor.laplace_method`:
  * 6.1: what `le_total _ (β⁻¹ ^ _)` compares is left to unification; since 2026-11-26 the claim gives a reading
    from the shape of the rewrites (g(s)^(8N) against β⁻¹^(50N)) and the second reader's alternative (g(s) against
    β⁻⁵, a second-reader message #4), both labelled;
  * 6.1.2: the constant in T (read as T = N·log β, the value compatible with the default proofs of the hypotheses of
    `dsCoeff_gaussian_shape`; the second reader's 0.9N·log β is not, see `CORRECTIONS.md`);
  * 6.1.2.4.1.2: how conj ψ_k is handled through −k;
  * 9: the two numeric side goals.
* `exists_principalMinor_eq_exp` 21–25: `on_goal 7` and `on_goal 4` are read as the postponed hypotheses of the
  second and third applications of the compression lemma (the order of postponed goals was inferred).
* `norm_poincare_period_sub_le`: 2.2–2.6 (the dominating function); 12.2–12.6 (which postponed goal each step closes);
  20–24.
* `IsSteep.exists_isTwoFactor_besselPairHom`: 7.2, 10.1–10.3, 11 (the exact power of b), 17, 19–21, 24–25.
* `IsSteep.exists_isTwoFactor_restriction` 9.1, 9.2, 13, 14 (the interpolation identities).
* `dsCoeff_gaussian_shape` 9.1.4–9.1.6 (signs of the correction terms) and 14.2.

For a second reading by the writer (I did not do one), I suggest every step of `IsTwoFactor.exists_near_one`, steps 6.x
of `IsTwoFactor.laplace_method`, step 9 of `dsCoeff_gaussian_shape`, and steps 15–21 of
`IsSteep.exists_isTwoFactor_besselPairHom`.

## Files
`unit.json` and `proofs/*.json` are generated by `gen/build.py` from `gen/content/*.py` (the words) and the census.
`gen/common.py` handles positions, quotations and typed facts, `gen/verify.py` is the independent re-check, and
`gen/survey.py`, `gen/sites.py`, `gen/show.py` and `gen/signature.json` are reading aids. To rebuild:
`cd reading/units/133/gen && python3 build.py && cd ../../../.. && python3 tools/rb.py check 133`.
