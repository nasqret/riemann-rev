# Corrections to unit 146 (vanishing of theta descents)

Date: 2026-11-26. Correction reader: Claude (Opus 5.5). Edition `72fead102f663d5c7a407964a13dc0cf9d977207`. Generator:
`gen/spec_proofs.py` changed and `gen/engine.py` re-run; no output edited by hand.

## Messages applied
- `a second-reader message` (second reading of 146): the large-height hypothesis and the finite coset coefficients.
- The coordinator's relay of the note writer's findings (step 1.2.18.3; steps 13.3.8–10): the same faults, applied once.
- `a second-reader message` (statement boundaries): no member listed; the truncated quotation of the import `exists_norm_name_le` extended.
- Statement strength: `q_binomial_submodule`, `Space.witt` (`a second-reader message` part 1), `hecke_transfer_of_equivariant`,
  `Space.Splitting.iwasawa` (`a second-reader message`, `a second-reader message`), `Space.Splitting.zeroTerm` (`a second-reader message`, `a second-reader message`, `a second-reader message`).

Checked against `New/SiegelWeil/AuxPairVanishing.lean` 101–158, `Lib/Weil/MixedModel/AdelicSum.lean` 127–132,
`New/SiegelWeil/DescentsVanishPlanes.lean` 49–109, `Lib/Weil/DualPair/KernelDecay.lean` 41–88,
`Lib/Adelic/Unitary/SpaceBasic.lean` 58–59, `Lib/Weil/MixedModel/ZeroTerm.lean` 535–561,
`Lib/SiegelWeil/SingularForms/AdaptedHom.lean` 62–66, `Lib/Weil/Unramified/HeckeTransfer.lean` 80–89.

## What changed (old → new)
- `descentsVanish_of_reflectionSum` step 12 (lines 103–105): "rows diag(d_j) z_j and then t_j 1_r" → x_j has upper block
  diag(d_j) z_j and lower block t_j I_r; [0 | t_j⁻¹ I_r] is a left inverse whatever the upper block; ι = incl(O) into the
  upper block.
- Step 13.3.8 (lines 130–133): "Ψ is a finite sum of multiples F_q of coset indicators" → there is a finite set F of coset
  representatives q with Ψ(q) ≠ 0 (hF) and Ψ = Σ_{q∈F} Ψ(q)·cosetIndicator(places(O), t, q) (h): F is a set, the coefficient
  of the indicator of q is Ψ(q).
- Step 13.3.10 (lines 135–138): "sum over q of F_q C_q(y); (number of terms) Ψ(z) C_z(y) = 0" → Σ_{q∈F} Ψ(q) C_q(y), each
  term equal to C_{incl A⁻¹}(y) = Ψ(z) C_z(y) by H, so |F|·Ψ(z)·C_z(y) = 0.
- Step 13.3.11 (line 139): "there is at least one term" → F is nonempty because otherwise Ψ = 0 by h, against Ψ(z) ≠ 0.
- Proof summary: the Ψ-expansion over F added.
- `descentsVanish_add_planes` step 1.2.16 (line 85): short isotropic ξ at a point of height > 2, its facts available from a
  proof of "height > 2".
- Step 1.2.17 (lines 86–87): "γ carrying the frame to these isotropic vectors" → given a proof l that the height exceeds 2,
  γ ∈ U(W')(E) with γξ = k (Witt with X = ξ, Y = k; left inverses from ξ ≠ 0 and gram_lk; Gram condition from i, gram_kk).
- Step 1.2.18 (head, line 88): bound independent of g → independent of g and h (estimate bound times the bound of |Y|).
- Step 1.2.18.1 (lines 89–93): → the decay estimate with N = 0, A, C + C, Z = c; ρ = height of V at h = 1 (V definite), so
  the bound is uniform.
- Step 1.2.18.2 (lines 93–95): → the norm hypothesis of the estimate, via cov, triangle inequality, rational invariance and
  moderate growth.
- Step 1.2.18.3 (lines 95–100): "the lattice data for each plane l" → l is a proof that the height H of W' at g exceeds 2
  (not a plane index); d = short basis of V at h, c = the frame column k, short at γg because γξ = k; x·y = Zρ(2/H); c
  isotropic; ℓ invariant under the rational maps (zeroTerm_rho_kAdelic now under `uses`).
- Step 1.2.18.4 (lines 100–104): → the last alternative of the estimate, which is cov for translates along k.
- Step 1.2.18.5 (line 104): adds why |Y| is bounded (automorphic on the definite space).
- Step 1.2.19 (lines 105–107): adds that this is the boundedness the maximum principle needs; no fundamental domain.
- Proof summary of `descentsVanish_add_planes`: the boundedness paragraph rewritten (estimate with N = 0, height 1 on the
  definite side, large-height hypothesis, Witt) instead of "moving g into a Siegel domain".
- Import `exists_norm_name_le`: lines [80, 81] → [80, 88]; text "a bound … decaying in the height" → the full statement,
  including the hypothesis `2 < H → ∃ d c x y, …` whose argument is a proof that H exceeds 2.
- Import `hecke_transfer_of_equivariant`: "Known result (Hecke transfer)" → the statement with A = a.frobValue(n, w),
  B = b.frobValue(n + k, w) spelled out; the authors' label quoted; `literature` (unresolved: Mínguez Thm 1).
- Imports `Space.Splitting.iwasawa` (full conclusion: b block upper triangular for wt, gκ acts on the frame through b;
  `literature` specializes: Arthur §1), `q_binomial_submodule` (`literature` matches: Stanley 1.7.2),
  `Space.witt` (`literature` specializes: First Cor. 4.9), `Space.Splitting.zeroTerm` ("integration over the isotropic
  directions" → the chosen bounded operator with (zeroTerm f)(y) the mean of f(iy + kb) over A^p/E^p; `literature`
  unresolved: Gan–Qiu–Takeda §2.7), `v_uniformizer` (exp(−1) is the uniformiser value in ℤᵐ⁰, not 1/e).

## Not applied, or applied with a difference
- a second-reader message says Witt "carries the one-plane frame to" the short isotropic vector; the source gives γξ = k
  (`W'.witt (.of_ne_zero (h1 l …)) ⟨_, D'.gram_lk⟩ (D'.gram_kk ▸ i l)`, DescentsVanishPlanes.lean 86–87, with
  `Space.witt : … → ∃ g, g X = Y`, SpaceBasic.lean 58–59): γ carries ξ to k. Step 1.2.17 states this direction.
- Point 3 of a second-reader message (sampled passages) confirms the dossier; nothing to change.

## Digests
- Old: `96df23350ccf668992c333b340e9528292a6bf7e47466a203b11750ff388f2ca`
- New: `684b321815570348bde5d694d045c1982d9b477ba736b99782a8db6d7b38f17a`
- `python3 tools/rb.py check 146` exits 0: 8 of 8 statements, 104 steps, 89 leaves, 10 of 10 typed facts, 108 of 108
  imports quoted, 137 of 137 arguments.
