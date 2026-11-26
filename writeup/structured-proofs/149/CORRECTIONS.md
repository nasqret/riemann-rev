# Corrections to the dossier of unit 149 (class count and index calculus), 2026-11-26

Correction reader: a Claude agent (Opus 5.5) acting as reader, the only writer of this folder since the first
reader finished. Checked against the pinned source (`lsernau/grh-lean` @ `72fead1`, `grh-compact/src`). Nothing
was built.

**Messages applied:** a second-reader message (second reading of 149) and a second-reader message (statement-boundary overlay).

**Result: no correction applied; the dossier is unchanged.** Digest (`dossier_sha256`) before and after:
`b5c04f1abcba5c25d9d69ce65596cfea1e6e9cc03159e0526c4b2beaa1309bdd`. Re-running `gen/gen.py` reproduces it byte for
byte, and `python3 tools/rb.py check 149` exits 0 (11 statements, 5 proofs, 24 steps, 21 imports, 137 of 137
arguments).

Note on the digest: a second-reader message reviewed `1b9ff36b7047f75a…` (the digest of the hand-off a second-reader message). The present
dossier, `b5c04f1a…`, was emitted by the first reader at 07:07Z with its late fixes; the second reader froze this
version at 07:28Z. The earlier files are not kept here, so every point of a second-reader message was checked against the present
texts instead.

## The points of a second-reader message, checked against the present dossier

* `Space.card_classes_le` (ClassCountBound.lean 14–37): a nonzero natural number N in the different, a CM type, the
  bound (1 + 2C³)^{4f|n|²} with C = 6N(f|n|)²; the two integral matrices are in its structured proof. Present.
* `IndexDvd M N z` (ModuleIndex.lean 20) is defined for arbitrary submodules M, N of an O-module over a commutative
  ring, neither need contain the other, and the determinant of the matrix divides z: the text states exactly this
  definition (every finite family in M is moved into N by a square matrix whose determinant divides z); the phrase
  "the index of N in M divides z" is marked there as a gloss. The second reader's advice, to use the definition when
  a note speaks of an index outside an actual lattice quotient, concerns the note.
* `IndexDvd.of_det_dvd` (68–73): "valuation domain" (ValuationRing O) and "the image of A lies in N" are hypotheses
  of the text. Present.
* a second-reader message: no member of 149 is in the overlay's inventory, and no quoted import of this dossier is in it either.

## Not applied

Nothing: a second-reader message asks for no correction. The expected Lean signature of `IndexDvd` (M, N, z explicit once; the text
reading lists them twice, see the README) still awaits Lean's output.
