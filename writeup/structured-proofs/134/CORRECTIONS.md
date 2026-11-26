# Corrections to unit 134 (the auxiliary pair and the theta lift)

Date: 2026-11-26. Correction reader: Claude (Opus 5.5). Edition `72fead102f663d5c7a407964a13dc0cf9d977207`. Generator:
`gen/spec.py`, `gen/spec_proofs.py` changed and `gen/engine.py` re-run; no output edited by hand.

## Messages applied
- `a second-reader message` (second reading of 134): integration variable, both conjugations, the inverse character, the signed ordering.
- `a second-reader message` (statement boundaries): no member listed; the truncated quotation of the import `staircase_harmonic_highest`
  extended.
- Statement strength: `IsMatch.exists_isJointHarmonic` (`a second-reader message` part 1), `isEdge_of_isJointHarmonic` (`a second-reader message`,
  `a second-reader message`, `a second-reader message`), `staircase_harmonic_highest` (`a second-reader message`, `a second-reader message`, `a second-reader message`, `a second-reader message`), identical verdicts.

Checked against `New/Forms/AuxiliaryPair.lean` 13–179, `New/Rows/StackedDeterminants.lean` 84–99 and 140–163,
`Lib/Weil/DualPair/Lift.lean` 17–20, `Lib/GLn/SchurModule/SchurOrthogonality.lean` 20–29,
`Lib/Weil/Lift/Staircase.lean` 180–198, `Lib/Weil/Lift/Edge.lean` 113–119, `Lib/DiscreteSeries/Theta/OscillatorDefs.lean`
100–133, `Lib/DiscreteSeries/Theta/JointHarmonicExists.lean` 85–91.

## What changed (old → new)
- `pairWeil_upsilon`, text: adds auxLevelChar(O)(j) = ∏_{w∈Q} ψ(O, w)(det j_{w,00})⁻¹: both the chosen and the twist places
  contribute inverse character values (the theorem's statement itself was right).
- `pairWeil_upsilon` step 3 (lines 61–64): "the reduction of k' is j … the determinant by det j_00" → the translated
  residue function involves k'⁻¹, whose reduction at Q is j⁻¹; the determinant is multiplied by det(j_00)⁻¹, giving
  ψ_w(det j_00)⁻¹. Proof summary accordingly.
- `theta_eq_smul_star_lift_swap`, text: → θ(O)(Ξ)(h) = c·conj(∫_{[U(I_n)]} θ(ω(g, h)φ)·conj(F_Ξ(g)) dg), g the integration
  variable on the definite source with its quotient measure, h on the target W; both conjugations stated (input conj F_Ξ,
  output conjugated again); θ(O) is *defined* as the finite class sum (AuxPair.θ), the integral form is the theorem.
  Proof summary: the evaluation point named and the conjugations explained.
- `FitsParams.exists_isJointHarmonic` step 3.5 (lines 134–138): "ord(O) is the ordering by decreasing l" → the signed
  ordering: among indices of the same sign, decreasing s(c)l(w, c), i.e. decreasing l at +1 and increasing l at −1.
- Imports: `Space.lift` (integration variable, quotient measure, linear in the input, no conjugation inside),
  `AuxPair.θ` (marked as the definition, letters of its variables).
- `staircase_harmonic_highest`: lines [191, 196] → [191, 198]; "nonzero, harmonic and highest … of explicit weights" →
  the full statement (hypotheses hl, hl', the signed ordering ho, hk, fit, hw; P the product of minors;
  IsJointHighest with the weights ν and staircaseWeight) + `literature` (specializes: Kashiwara–Vergne Prop. 6.1, Thm 6.3;
  Davidson Thm 2.9).
- `IsMatch.exists_isJointHarmonic`: "Known result …" → the statement (IsJointHarmonic spelled out), the authors' label
  quoted, `literature` (specializes: Howe §3, Paul–Trapa Lemma 3.2).
- `isEdge_of_isJointHarmonic`: "Known result …" → the statement (positive ranks, the std pair and parameters, IsEdge in both
  directions), the authors' label quoted, `literature` (unresolved: Ichino Prop. 7.2, Lemma 7.8; Howe Thm 1).
- The eight members whose `binders_basis` is "lean" (`isHCParam_paramV`, `realPairWeil_fockLetters`,
  `realPairWeil_harmonicPoly`, `FitsParams.exists_isJointHarmonic`, `FitsParams.isEdge`, `pairWeil_fockDatum`,
  `conjKernel_equivariant`, `theta_eq_smul_star_lift_swap`): `binders_derivation` added, stating that the list is
  source-derived (Lean 4's section-variable rules applied to the `variable` commands at lines 18, 69, 140), not
  elaborator output.

## Not applied, or applied with a difference
- a second-reader message notes that the eight binder lists "await native signatures". They cannot be printed here (nothing is built; the
  replay build is incomplete). `binders_basis` still reads "lean" because `rb.py check` accepts a list that differs from its
  text reading under no other value (contracts.md); the new `binders_derivation` field says what the list stands on. When
  the build exists, `#check @Name` should replace `binders_lean`.
- The second reader's account of `upsilon_eq_sum` (lines 39–50) and of the Fock substitutions (lines 97–101) confirms the
  dossier; nothing to change.

## Digests
- Old: `330514c4d76137ce4e3e3a756600415f9144a62506239183f2c613e541d50070`
- New: `a38d5312d5448289bb307aaee8aea00dc76f88c207022844141bb9a33ca9d885`
- `python3 tools/rb.py check 134` exits 0: 16 of 16 statements, 31 steps, 29 leaves, 76 of 76 imports quoted, 159 of 159
  arguments (8 members by the "lean" basis, which the check cannot confirm).
