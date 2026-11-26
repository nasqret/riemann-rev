# Corrections to unit 137 (one-prime patching)

Date: 2026-11-26. Correction reader: Claude (Opus 5.5). Edition `72fead102f663d5c7a407964a13dc0cf9d977207`. Generator:
`gen/content.py` changed; `gen/build.py` extended (passes an optional `literature` record on imports; quotes a member's
full statement from a given span as `statement_full` and checks it against `source_ranges.statement`; keeps a member's
own `source_ranges_basis`) and re-run; no output edited by hand.

## Messages applied
- `a second-reader message` (second reading of 137): the character-test implication; the truncated valuation.
- `a second-reader message` (statement boundaries): the member `BaseLevel.exists_tie`; four truncated import quotations.
- Statement strength: `galRep_of_parahoric_type`, `hecke_eq_frob_on_parahoricEigenspace`, `BaseLevel.exists_higman_operator`
  (`a second-reader message`, `a second-reader message` part 2), `IsPlaceOver.exists_localArtin_eq`, `IsPlaceOver.exists_localArtin_eq_tameGenerator`
  (`a second-reader message`, `a second-reader message`, `a second-reader message` part 1), `Isotypic.attached_galRep` (`a second-reader message` part 1, the payload that `a second-reader message`
  describes); identical verdicts where repeated.
- The value-group convention that `a second-reader message` raised for unit 140 (exp(−1) in ℤᵐ⁰), applied to the same notation here.

Checked against `New/Patching/OnePrimeTie.lean` 33–59 and 96–178, `Lib/ClassField/Places/SelmerDefs.lean` 25–26,
`Lib/LocalGL/TaylorWiles/AuxPlaceOperators.lean` 66–102, `Lib/LocalGL/Iwahori/HeckeOnLineStabiliser.lean` 24–33,
`Lib/GaloisRep/LocalGlobal/TypeFrobenius.lean` 13–54, `Lib/Adelic/CuspForms/BaseLevel.lean` 115–117.

## What changed (old → new)
- `weightedSum_ext`, proof summary: "nonzero unless ψ⁻¹(k) = i" (the reversed implication) → T(ψ) = (ψ⁻¹(k) − i)·Σ ψ(c'(g))ρ(g)y
  vanishes whenever ψ⁻¹(k) = i and may vanish otherwise; where T(ψ) ≠ 0 one has ψ⁻¹(k) ≠ i and h applies (lines 54–58).
  Steps 1.2.3–1.2.4 already had the right direction; the statement was right.
- `exists_diagOp_mem_ellIntegralForms`, text: "the ℓ-adic valuation normalised by ellVal(ℓ) = 1" → ellVal on all of Q̄_ℓ,
  ∞ at 0 and max(0, −log_ℓ|z|) otherwise (ENNReal.ofReal), so 0 whenever |z| ≥ 1, e.g. ellVal(1/ℓ) = 0; reading of γ
  accordingly.
- `exists_tie`: `statement_full` added, the statement quoted from the corrected span [96, 1, 103, 90] of the overlay
  (SHA-256 `d220ee26…`, equal to the dossier's `source_ranges.statement`); `source_ranges_basis` records the agreement. The
  text already stated the full conclusion (i) and (ii), with the group sum 𝒩 and the factor 2·N!; checked against
  lines 99–103, unchanged.
- Steps `exists_tie` 11.4 and `exists_diagOp_mem_ellIntegralForms` 9: "Higman's criterion" → `exists_higman_operator` (the
  authors' Higman criterion up to c; the classical criterion needs c invertible).
- Step `exists_tie` 3 and import `heckeCoset_mem_parahoricEigenspace`: v(ϖ) = e^{−1} marked as the uniformiser value in the
  multiplicative value group ℤᵐ⁰ (additive order 1).
- Import quotations extended to the full statements: `BaseLevel.exists_localOps_aeval_hecke` [73, 74] → [73, 75],
  `heckeCoset_mem_parahoricEigenspace` [31, 32] → [31, 33], `galRep_of_parahoric_type` [26, 26] → [26, 30],
  `hecke_eq_frob_on_parahoricEigenspace` [50, 51] → [50, 54]; their texts state the full conclusions (the last two
  rewritten with the section hypotheses: s geometric Frobenius, τ in inertia, Art(ϖ) = s, Art(u) = τ; no hypothesis
  tr((τ − 1)M) ≠ 0 or y ≠ 0 in the last).
- `literature` records added to the six named imports; texts rewritten where the first reading asserted a relation:
  `BaseLevel.exists_higman_operator` ("Higman's criterion up to c" → the statement, c possibly 0, the authors' label quoted;
  unresolved), `galRep_of_parahoric_type` and `hecke_eq_frob_on_parahoricEigenspace` (unresolved),
  `Isotypic.attached_galRep` (Attached spelled out; weakens), `IsPlaceOver.exists_localArtin_eq` (geometric Frobenius;
  additive order n; weakens), `IsPlaceOver.exists_localArtin_eq_tameGenerator` (weakens).

## Not applied
Nothing contested. The second reader's remark that the tame generator and the chosen Frobenius enter different traces,
and that the group sum and the factor 2·|n|! must be kept, is already true of the text of `exists_tie` (checked).

## Digests
- Old (the bytes the second reader reviewed): `91b71ff7408abf3cf4449f7bb1be534519321a48b3d98ce77d9869ceef7808d3`
- New: `063710f9078921c971ee7d9dea8087e062c3b08182c19ca27e1849dd9e99a597`
- `python3 tools/rb.py check 137` exits 0: 10 of 10 statements, 144 steps, 122 leaves, 22 of 22 typed facts, 91 of 91
  imports quoted, 226 of 226 arguments.

## Pass 7 (2026-11-26): a second-reader message, the exponent in the local reciprocity gloss

Correction reader: a Claude agent (Opus 5.5), the only writer of this folder during the pass. Message: a second-reader message (second
reader's check of the revised 137, dossier `063710f9…`). It confirms the character-test implication, the truncated
valuation, the full tie (span [96, 1, 103, 90], SHA-256 `d220ee26…`) and the six named imports, and requests one
correction: the reading of `IsPlaceOver.exists_localArtin_eq` called g a geometric Frobenius for every n ≥ 0. Checked
against the pinned source (`lsernau/grh-lean` @ `72fead1`, `grh-compact/src`): `Lib/ClassField/Local/ArtinMapAtPlace.lean`
144–147 (`hs : IsFrob A q g⁻¹`, `(n : ℕ)`, `e : q = w.q ^ n`; conclusion `v x.1 = exp (-↑n)` and the class of g),
`Lib/ClassField/Places/GaloisDefs.lean` 74–76 (`IsFrob A q σ`: σ in the decomposition group and σx ≡ x^q modulo the
maximal ideal of A; for n = 0, q = 1, so σ acts trivially on residues, i.e. lies in inertia), and
`New/Patching/OnePrimeTie.lean` 104–108 (the tie uses `exists_localArtin_eq θ.isFrob 1`, n = 1, so the step that applies
it was right). Changed in `gen/content.py` and re-emitted with `gen/build.py` (which first reproduced the old dossier
byte for byte). Nothing was built.

### Change (old → new)

- Import `IsPlaceOver.exists_localArtin_eq` (unit 89), text: “… if g⁻¹ is a Frobenius at A for q = q_w^n (n ≥ 0; g is a
  geometric Frobenius), then …” → “… if g⁻¹ is a Frobenius at A for q = q_w^n (n ≥ 0: g⁻¹ lies in the decomposition group
  of A and acts on the residues of A as the q_w^n-th power, so g induces the n-th power of the geometric Frobenius on
  residues; g is a geometric Frobenius only for n = 1, and for n = 0 it lies in the inertia group of A), then …” (the
  rest — the class of g, v(x) = e^{−n}, additive order n, the literature record — unchanged).

The same correction was carried to unit 138's reading of this import (138-a, pass 7 there), and chunk 138-c, which reads
this import in dossier 137 by name, took the new text when it was re-emitted.

### Not applied

Nothing else: a second-reader message requests no other correction.

### Digests and check

- `dossier_sha256`: old `063710f9078921c971ee7d9dea8087e062c3b08182c19ca27e1849dd9e99a597` → new
  `92531c23f202fc8ec689605afd84f8800851b7ba07fe687e045401835980869d` (only that import text changed; proofs unchanged).
- `python3 tools/rb.py check 137`: exit 0 — 10 of 10 statements, 6 structured proofs, 144 steps, 122 leaves, typed facts
  22 of 22, imports quoted 91 of 91, arguments 226 of 226.
