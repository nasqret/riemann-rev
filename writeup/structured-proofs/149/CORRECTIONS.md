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

## Pass 7 (2026-11-26): a second-reader message, the outstanding correction to an import

Correction reader: a Claude agent (Opus 5.5), the only writer of this folder during the pass. Message: a second-reader message (second
reader's revision check of 149), section "Outstanding correction to an import"; its other sections confirm the present
texts and ask for nothing. Checked against the pinned source (`lsernau/grh-lean` @ `72fead1`, `grh-compact/src`):
`New/Filling/BoxPartition.lean` 214–215 (section variables `[Field E'] [NumberField E']`) and 284–292 (the lemma: the
instance `[PlaceEmbedding E']`, `(o : 0 ≤ r)`, `(h : ∀ᵉ (a ∈ A) (i), IsIntegral ℤ (f a i) ∧ ∀ v, ‖Φ v (f a i)‖ ≤ r)`,
`(j : InjOn f A)`, conclusion `A.encard ≤ ENNReal.ofReal ((1 + 2 * r) ^ (card ι * numInfPlaces E' * 2))`);
`Lib/Adelic/Adeles/CoprimeValuation.lean` 15–29 (`PlaceEmbedding` gives only the embeddings Φ; `CMType` extends
`NumberField`, `IsCMField`, `PlaceEmbedding`); `New/Core/ClassCountBound.lean` 14–25 (the use, with `[CMType E]`).
Changed in `gen/readings.py` and re-emitted with `gen/gen.py` (which first reproduced the old dossier byte for byte).
Nothing was built.

### Change (old → new)

- Import `Filling.encard_integral_le` (unit 148), text: “For a field E' with chosen embeddings Φ_v at its infinite
  places, a finite type ι, a real r ≥ 0 and a map f sending a set A injectively to E'^ι, all of whose values have entries
  that are algebraic integers with |Φ_v(entry)| ≤ r at every infinite place v: the cardinality of A (in ℕ∞) is at most
  (1 + 2r)^{|ι|·m·2}, m the number of infinite places of E'.” → “For a number field E' ([NumberField E'], a section
  variable of BoxPartition.lean 214–215, beside [Field E']) with chosen complex embeddings Φ_v inducing its infinite
  places v ([PlaceEmbedding E'], which supplies only the embeddings, not the number-field structure), a finite type ι, a
  set A in a type α, a real r ≥ 0 (o) and a map f : α → E'^ι injective on A (j) such that for every a ∈ A and every
  i ∈ ι the entry f(a)_i is integral over ℤ and |Φ_v(f(a)_i)| ≤ r at every infinite place v (h): the cardinality of A,
  an element of ℕ∞ coerced to [0, ∞], is at most (1 + 2r)^{|ι|·m·2} = (1 + 2r)^{2|ι|m} (ENNReal.ofReal of that real
  number), m the number of infinite places of E'. (In Space.card_classes_le, E' = E and the number-field instance comes
  from CMType E.)”

### Not applied

Nothing else: a second-reader message confirms the class count, the injection, the index divisibility and its directions. The expected
Lean signature of `IndexDvd` (M, N, z explicit once) still awaits Lean's output, as before.

### Digests and check

- `dossier_sha256`: old `b5c04f1abcba5c25d9d69ce65596cfea1e6e9cc03159e0526c4b2beaa1309bdd` → new
  `931a95ece44cb8dc2fc41352aa5d16f00375d2a25ea1642e12e0b295c82a9b81` (only that import text changed; proofs unchanged).
- `python3 tools/rb.py check 149`: exit 0 — 11 of 11 statements, 5 structured proofs, 24 steps, 22 leaves, imports
  quoted 21 of 21, arguments 137 of 137.
