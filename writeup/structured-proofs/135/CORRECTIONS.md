# Corrections to the dossier of unit 135 (heights), 2026-11-26

Correction reader: a Claude agent (Opus 5.5) acting as reader, the only writer of this folder since the first
reader finished. Checked against the pinned source (`lsernau/grh-lean` @ `72fead1`, `grh-compact/src`). Nothing
was built.

**Messages applied:** a second-reader message (second reading of 135) and a second-reader message (statement-boundary overlay).

**Result: no correction applied; the dossier is unchanged.** Digest (`dossier_sha256`) before and after:
`88bf2e5315784846c9b44970731571c19674d4523ef1ae76207b7468d64c54c4`. Re-running `gen/gen.py` reproduces it byte for
byte, and `python3 tools/rb.py check 135` exits 0 (18 statements, 7 proofs, 52 steps, 9 imports, 178 of 178
arguments).

Note on the digest: a second-reader message reviewed `f4509d706f58db47…` (the digest of the hand-off a second-reader message). The present dossier,
`88bf2e53…`, was emitted by the first reader at 07:07Z with its late fixes (its README: "second reading and fixes
added afterwards"); the second reader froze this version at 07:28Z. The earlier files are not kept here, so the two
versions could not be compared line by line; instead every point of a second-reader message was checked against the present texts.

## The points of a second-reader message, checked against the present dossier

* One common nonzero multiplier H for all primes and embeddings, an eventual bound over prime prefixes
  (α + Σ_{ℓ<M} e(ℓ) ≤ c for large M): `HeightLe` text, Heights.lean 21–23. Present.
* `HeightLe.of_le` bounds every finite set of primes instead (Σ_{ℓ∈T} e(ℓ) ≤ c): its text, lines 42–43. Present.
* `PrimePadicIso` uses the algebraic closure of ℚ_ℓ (Mathlib's `PadicAlgCl ℓ`); the map j of `one_determinant` goes
  to the completion ℂ_ℓ. Present in both texts.
* In `one_determinant` the cost 2δ comes from two integral recombinations, at j and at j∘conj (proof steps 3, 5, 7,
  8); the factor k·g carries the family |γ(ι)|⁻² of height ≤ g (hypothesis hγ, step 2); the target is a ratio of
  squared volumes normDet(u_θ)²/normDet(u_o)² and u_o must be injective (hu). Present.
* a second-reader message: no member of 135 is in the overlay's inventory (its statement boundaries are the census's), and no
  quoted import of this dossier is in it either.
* a second-reader message has a literature record for the import `exists_ringEquiv_extend` (Stacks 030D, 09GV); it confirms the
  dossier's reading of that import, so nothing was changed.

## Not applied

Nothing: a second-reader message asks for no source-level correction. The five binder lists that the README marks as expected to
differ in Lean (bound letters that repeat section variables) still await Lean's output.
