# Corrections to the dossier of 133 (Discrete series coefficients near 1, Laplace's method, and explicitly large Bessel functions)

## 2026-11-26 — second reading (a second-reader message), statement-boundary overlay (a second-reader message) and literature records

Correction reader: a Claude agent (Opus 5.5), the only writer of this folder for this pass. Every correction was checked
against the pinned source (`lsernau/grh-lean` @ `72fead1`, `grh-compact/src`) before it was applied. Nothing was built.
The changes were made in the generator's inputs (`gen/content/*.py`) and in `gen/build.py`; the dossier was emitted again
with `cd reading/units/133/gen && python3 build.py`. `gen/statement_overlay.py` is the overlay helper of units 141, 144,
145, 150 (copied unchanged). `gen/verify.py` (the independent re-check) now checks a member that carries
`statement_span` by slicing and hashing the span instead of comparing `statement_lean`.

**Messages applied:** a second-reader message (the second reading of 133, five points and the Bessel paragraph); a second-reader message (the
statement-boundary overlay: four members and two imports of 133 are listed); the second reader's statement-strength
verdicts (`by_name` rows) for the four imports of 133 that have one: a second-reader message part-1-named.json
(`measurePreserving_orbitMeasure`, `lintegral_orbitMeasure_lintegral`, `witt`) and part-2-named.json
(`isIdempotentKernel_psiInFrame`, same verdict in a second-reader message strength-general.json and a second-reader message part-2-named.json). No
other import of 133 has a `by_name` row in a second-reader message, 0011, 0012, 0017, 0019, 0024 or 0032 (matched by declaration id).

### a second-reader message (old → new)

1. #1, the two norms: no text changed (the texts already said Frobenius in TwoFactorSetup, GaussianShape, MinorExpansion
   and operator norm in RestrictionLemma and BesselExistence). README: "`heuristic`; please confirm" → confirmed by the
   second reader from the source (`frobenius_norm_sq_eq_sum` in the proof of GaussianShape.lean 18–25; the operator norm
   invoked separately at 57–58); still a source reading.
2. #2, instance `Shape.besselGraphMeasure_isMulRightInvariant` (BesselExistence.lean 59–63): "right multiplication by t
   becomes, in the chart, conjugation of the 𝖴-coordinate by an element of 𝖲 … combined with right multiplication on
   U(κ)" → for t = (embedH(h₀)u₀, h₀) the chart coordinates go to (embedH(h₀)⁻¹·u·embedH(h₀)·u₀, h·h₀): conjugation by
   embedH(h₀) followed by right translation by u₀ (`… .mul_right _ t.1`, line 62), present even when h₀ = 1.
3. #2 (lines 73–77), member `lintegral_unfold_besselGraphMeasure` and import `besselQuotMeasure`
   (UnipotentCoords.lean 244): "the measure on G₁ computing integrals over 𝖴∖G₁" → + it is the project's orbit measure
   orbitMeasure(besselHaar(𝔰), volume) on the full group G₁(𝔰) (Haar measure weighted by a cutoff), not a measure on the
   quotient space.
4. #3, `norm_poincare_period_sub_le` step 12.2 (RestrictionLemma.lean 76–80): "= R·min(firstMinimum(V.move x),
   firstMinimum of the added line) (the line is definite, first minimum ≥ 1)" → the first minimum is cut off at 1, so
   firstMinimum(V.move x) ≤ 1 (`Space.firstMinimum_le_one`, a simp lemma, FirstMinimum.lean 37; definition
   MinkowskiSecond.lean 74–77) and the added definite line has first minimum exactly 1; the minimum leaves the original
   one unchanged. New import `Space.firstMinimum_le_one` (unit 121), cited in `uses`. Steps 12, 12.1,
   13, 14 (separation d², nonzero lattice vector after division by a, ‖f(o)‖ ≤ d, ‖f(γ)‖ ≥ d²/2) already agreed with the
   second reader; unchanged.
5. #4, `IsTwoFactor.laplace_method` steps 6.1, 6.1.1, 6.1.2 (RestrictionLemma.lean 158–163), applied in part:
   6.1 "split by le_total … (both sides left to unification)" → the same, plus a reading from the shape of the rewrites
   (`grw [mul_assoc, ← e, ← pow_add]` merges two powers of one base in both cases: g(s)^(8N) against β⁻¹^(50N), giving
   16g(s)^(16N) in the first case and 16β⁻¹^(100N) in the second), plus the second reader's threshold g(s) ≤ β⁻⁵ as an
   alternative, both labelled as readings; 6.1.1 "the inequality follows from Re θ ≥ −|θ|" → + |θ(s)| ≤ g(s)^c with
   c ≤ 18N (p, now cited) gives 8(Re θ + 16g^c) ≥ 4|θ|; 6.1.2 "T = c·log β for the constant c read from the goal" → +
   in the reading of 6.1, T = N·log β, the value compatible with the default proofs of the hypotheses of
   `dsCoeff_gaussian_shape`. The near-diagonal and far-from-diagonal steps (6.1.2.4.x) already stated the second reader's
   arithmetic (10e-closeness and phase cancellation; real Gaussian factors in [0, 1] with error a tenth plus e^(−100T);
   (1 + e²)^(−h/4) ≤ e^(−100T) from hh); unchanged.
6. #5, `exists_principalMinor_eq_exp` step 24 (MinorExpansion.lean 100–104): "‖sA‖ ≤ ‖A‖ for s ≤ 1" → for a real scalar
   ρ with 0 ≤ ρ ≤ 1 (`norm_smul_le_of_le_one`, FramedCoefficient.lean 30–31, side condition `0 ≤ ρ ∧ ρ ≤ 1` by grind;
   here ρ = 1/4); its import text now states the hypotheses. Summary: + the theorem is about a lower set p; the
   triangularity identity I (lines 66–70) is for upper sets and is applied to ¬p (step 20) and to the full index set
   (det y(l) = det g, lines 91–96, step 21). Steps 8, 20, 21 already said so; unchanged.
7. Bessel paragraph (BesselExistence.lean 185–225): a verification; `exists_isBesselFunction` already states the
   lower-bound hypothesis La; nothing changed.

### a second-reader message, the statement-boundary overlay (members: statement lines census → corrected)

Each span was re-sliced and re-hashed from the pinned file and read: every one ends just before the declaration's own
`:=` (for `sum_norm_lie_coordProj_sq`, the overlay's manual-review case, the absolute-value bars belong to the `letI`).
All four texts already stated the whole conclusion (the first reader had read the statements to their end); unchanged.

- `sum_norm_lie_coordProj_sq` (GaussianShape:18:7): 18–18 → 18–20 (span (18,1)–(20,79)).
- `exists_principalMinor_eq_exp` (MinorExpansion:49:7): 49–49 → 49–53 (span (49,1)–(53,77)).
- `norm_poincare_period_sub_le` (RestrictionLemma:25:7): 25–31 → 25–40 (span (25,1)–(40,29)).
- `IsSteep.exists_isTwoFactor_restriction` (RestrictionLemma:200:7): 200–203 → 200–205 (span (200,1)–(205,90)).
- The four proofs keep the line-census basis (the statement tails stay in `intro_lines`, and in step 0 of
  `norm_poincare_period_sub_le`); their summaries and step 0 now say that those lines are the statement, not proof.
- Imports re-quoted to the end of their statements, texts completed: `integral_decay_le` (RegularRepL2 66 → 66–67:
  + the section hypotheses, f from the `letI`, the real measure), `trace_mul_logOneAdd` (FramedCoefficient 44 → 44–45:
  + f from the `let`, Lebesgue measure; its duplicate entry in `two_factor_setup.py` is marked as unused).

### Literature records (imports; old reference → the second reader's verdict)

- `measurePreserving_orbitMeasure` (Packing.lean 75–77): "(h, x) ↦ h·x carries orbitMeasure(ν, μ) × ν to μ (Weil's
  formula)" → the full statement with the section hypotheses (measurable action, ν s-finite and inversion invariant,
  μ s-finite H-invariant, a cutoff; the order (x, h) of the product fixed) and `literature`: unresolved (the Kallenberg
  specialization has incompatible hypotheses; the pushforward follows from s-finite Tonelli).
- `lintegral_orbitMeasure_lintegral` (Packing.lean 91–92): "Unfolding … over H∖X" → full statement and `literature`:
  unresolved (the equality exceeds the cited proper Haar-action setting).
- `witt` (FrameAction.lean 140–141): "Witt's extension theorem: two families … (and nondegeneracy)" → the hypotheses hz,
  hJ, hJ', hX, hY, h stated (left-invertible X, Y with XᴴJX = YᴴJY, J hermitian invertible, z − z* a unit) and
  `literature`: matches (First, Remark 2.1 and Cor. 4.9).
- `isIdempotentKernel_psiInFrame` (FramedCoefficient.lean 142–144): "a continuous integrable minimal idempotent kernel"
  → the five fields of `IsIdempotentKernel` (CircleMean.lean 84–89) and the hypotheses (n nonempty, J a hermitian
  involution, a sign frame, large gap A); "minimal" removed (not in the definition); `literature`: unresolved
  (Harish-Chandra II, pp. 87–88; threshold and normalization need separate work).

Each record carries relation, verdict, sources, the payload, `statement_range`, `catalogue_row_sha256` and the basis
sentence used by the earlier passes; `gen/build.py` now passes an import's `literature` field through.

### Not applied, and why

- a second-reader message #4, the second reader's threshold g(s) ≤ β⁻⁵ with 100T = 90N·log β as the constants of the source. It is
  offered as "one way" and is valid arithmetic for the inequality A, but it does not fit the source: (i) after
  `grw [← e]` with e : β⁻⁵ ≤ g(s) the term is β⁻¹^(50N)·(β⁻¹^5)^(8N), two powers of different bases, which `← pow_add`
  (RestrictionLemma.lean 158) does not merge; (ii) `dsCoeff_gaussian_shape` is applied at 165–166 with the hypotheses
  `a : card n ^ 2 ≤ T := by nlinarith` and `b : card n ^ 2 * log (card n + L + 1) ≤ T := by bound` (GaussianShape.lean
  48–51), and with T = 0.9N·log β the local facts (|n|² ≤ N, 1 ≤ log β, |n| + L + 1 ≤ β) do not give b, since
  |n|² ≤ 0.9(|n| + |m|)² fails for |m| = 1, |n| ≥ 19. The claims keep the comparison open ("left to unification"),
  give the reading g(s)^(8N) against β⁻¹^(50N) with T = N·log β as a heuristic, and quote the second reader's version
  as an alternative.
- Nothing else was refused. The ten binder lists flagged by the first reader still await Lean's own signatures.

### Digests and check

- dossier digest (`dossier_sha256`): old `ee855d2d981189dfa3f7524ae0afa26cec2d9424c3e86afc562e2774bbbc8ff9` (the one the
  second reader read) → new `2c3bfff916748f17c306aa741d7c9ecb3ba1c97383dfc645f68e0b0ea9dc4a9b`
- `python3 tools/rb.py check 133`: exit 0 — unit 133: 37 of 37 statements at their lines; 17 structured proofs, 260
  steps, 235 leaves (longest 8 lines, bound 8), 260 steps quote their lines; typed facts in the source: 35 of 35;
  imports quoted: 174 of 174; arguments accounted for: 372 of 372
- `python3 reading/units/133/gen/verify.py`: 37 members, 174 imports, 260 steps; all quotations and hashes agree with
  the sources

Cost: about 30 minutes of wall time for this pass on 133 and 145 together (after 08:15Z, the time of the last check
before it, to 08:45Z by `date -u`); tokens not reported by the client.
