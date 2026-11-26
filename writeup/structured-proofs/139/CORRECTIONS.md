# Corrections to unit 139 (label uniqueness)

Date: 2026-11-26. Correction reader: Claude (Opus 5.5). Edition `72fead102f663d5c7a407964a13dc0cf9d977207`. Generator:
`gen/spec.py` changed and `gen/engine.py` re-run; no output edited by hand.

## Messages applied
- `a second-reader message` (second reading of 139): the shared Hecke polynomial, the quantifiers, the product-of-roots argument.
- `a second-reader message` (statement boundaries): no member listed; two truncated import quotations extended.
- Statement strength: `exists_ringEquiv_extend` (`a second-reader message`, `a second-reader message`, `a second-reader message`, identical), `Attached.isLabelledAt`
  and `sphericalCompat_std` (`a second-reader message`, `a second-reader message`, identical).

Checked against `New/GaloisRep/LabelUniqueness.lean` 13–59, `New/Selmer/FitTwists.lean` 150–159,
`New/Trace/BadShare.lean` 27–51, `Lib/General/Algebra/InertResidue.lean` 19–32, `Lib/Weil/Unramified/SphericalHecke.lean`
129–175, `Lib/GaloisRep/LocalGlobal/{ParahoricTypeLabel,LabelCompatibility,TameExponent}.lean`,
`Lib/GaloisRep/Main/{AttachedDefs,SphericalAllRanks,LocalEmbedding}.lean`.

## What changed (old → new)
- `occurringLabels_subsingleton`, text: "spherical with Hecke eigenvalues F(w)" → F(w) : ℂ → ℂ, and for every complex X the
  Hecke polynomial operator Σ(−X)^i q^(i choose 2) T_{w,i} acts on the smooth form of L(y) by the scalar F(w)(X);
  hk: "F_y(g)" → the function g ↦ L(principalRep(D, V)(g at x)(y)) of g ∈ GL_{RowIndex(D)}(k_x) (no clash with F); conclusion: at most one label,
  no existence (a label occurs only through a witness of eigenPart; if eigenPart = 0 none occurs). Readings of `F`, `hF` too.
- Proof 1.1 (lines 29–30): the scalars t_{w,i} depend only on w and F(w), so one family Q of Hecke polynomials serves every
  form and every occurring label (new sentence).
- Proof 1.4, 1.4.3, 1.4.4 (lines 35–43): "an attached representation; every attached r is labelled" → some representation
  attached to Q exists, and every r attached to Q is labelled by c'∏(X − x_{χ_l})^(t_l); Q depends neither on c nor on y.
- Proof 1.5 (lines 44–46): → the r attached to Q found for c1 is labelled by B h, and by B' h because Q is the same for c2
  (no two independently chosen representations are compared).
- Proof 1.7 (lines 48–50): adds that it is the product of the roots that has order q − 1 (an individual root can have
  order q^r − 1).
- Proof 1.8 (head, lines 51–54): → det r(s) = ∏_{roots of c1'} ι(T(x))·∏_l ι(T(x_{χ_l}))^(t_l) (B h, 2 a unit at x), the second
  factor M_ω-torsion (e); det r(s) is the product of the eigenvalues; it suffices that every eigenvalue is M_ω-torsion.
- Proof 1.8.1–1.8.3 → 1.8.1–1.8.2 (renumbered): the administrative `clear` (old 1.8.1, line 55) is merged into the unfolding
  step (new 1.8.1, lines 55–57: distinct monic irreducible labels have no common root); old 1.8.3 (lines 58–59) is new
  1.8.2: an eigenvalue of r(s) is a root of both labelling polynomials, cannot come from c1' and c2' at once, so it is some
  ι(T(x_{χ_l})) and M_ω-torsion. Old 1.8.2 (lines 56–57) "a root of c1' must match one of the x_{χ_l}" is replaced.
- Proof summary and unit summary rewritten accordingly (shared Q; eigenvalue route; product of roots).
- `isEigenform_of_hasHeckePolyAt` step 2: adds that a prime-norm place is split because E(D) is stably unramified (a
  conjugation-fixed place has square norm), and that only away from the discarded places is the polynomial needed.
- Imports: `isSplit_of_q_prime` (stably unramified hypothesis and reason), `Data.occurringLabels` (degree |RowIndex(D)|,
  witness y, empty when eigenPart = 0), `IsSphericalWith` (p : ℂ → ℂ, operator formula), `HasParahoricType` (its last
  argument renamed Φ), `IsPrimitiveLabel.isPrimitiveRoot_prod_roots` (product vs. individual root),
  `HasParahoricType.hasProductLabel` (full statement; lines [31, 33] → [31, 35]), `Data.dvd_card_resField_sub_one`
  (lines [155, 155] → [155, 156]).
- `sphericalCompat_std`: "Known result …; unramified or crystalline with the expected Frobenius" → the full statement of
  SphericalCompat (attachment; good type; jumps; ι(Q) kills r(s) for geometric Frobenius s, PolyKillsAt) + `literature`
  (weakens: Chenevier–Harris Thm 3.2.3, BLGGT Thm 2.1.1, Labesse Cor. 5.3).
- `Attached.isLabelledAt`: "Known result (local-global compatibility …)" → full hypotheses (HasProductLabel) and
  conclusion (finite type, jumps, IsLabelledAt for PolyKillsAt and det = product of roots) + `literature` (unresolved:
  BLGGT II Thm 1.1, Taylor–Yoshida Thm A; the squarefree-label predicate needs a separate identification). The summaries
  now name it as the authors' local-global compatibility at tame level.
- `exists_ringEquiv_extend`: full statement (g = σ ∘ f) + `literature` (specializes: Stacks 9.26.3, 9.10.6).

## Not applied, or applied with a difference
- The second reader describes the last contradiction as "a root of the first polynomial falls among the auxiliary
  character roots". Lean's route (lines 51–59) is through the eigenvalues of r(s): `isRoot_of_isRoot_charpoly` with
  `(B h).1.1 l` and `(B' h).1.1 l` (line 58) makes every eigenvalue a common root, and `(B h).2 l` (line 53) gives
  det r(s) as the product of the roots of the first labelling. Steps 1.8–1.8.2 follow the source; the substance of her
  two facts (disjoint roots after the common twist; the product has exact order q − 1) is kept.

## Digests
- Old: `c53cc409f013c8d932fa160a48170e6e1353676c4a482b30c5856a6a66217135`
- New: `c014be5bce36e8ed363b6a7bb62013e55398cbd801b4b77bff38f258966bc8cd`
- `python3 tools/rb.py check 139` exits 0: 2 of 2 statements, 17 steps (was 18), 14 leaves, 39 of 39 imports quoted,
  36 of 36 arguments.
