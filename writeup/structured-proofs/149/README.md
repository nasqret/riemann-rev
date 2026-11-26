# Unit 149 — a crude class-number bound, and divisibility of indices of submodules (IndexDvd, HasType)

**Checked on 2026-11-26** against the second reading (a second-reader message) and the statement-boundary
overlay (a second-reader message): no correction was needed; see `CORRECTIONS.md`.

Reader: the reader role, performed by a Claude agent (claude-opus-5-5) spawned by the coordinator (2026-11-26, grh-compact at 72fead10). `python3 tools/rb.py check 149` passes: 11 of 11 statements at
their lines, 5 structured proofs, 24 steps (22 leaves, longest 4 lines), 21 imports quoted, 137 of 137 arguments.

## Where to start

* `IndexDvd` (ModuleIndex.lean:20) is the notion the rest of the unit (and unit 144) is about: "every finite family in
  M is moved into N by a square matrix whose determinant divides z" — a divisibility version of "[M : M ∩ N] divides z"
  that works over any commutative ring. Then `HasType` (y(M) ⊆ M and IndexDvd M (y(M) + pⁿM) (p^l), l ≤ c), the form in
  which `hasType_twisted_hecke` (unit 144) states the size of elementary divisors.
* The calculus: `comap`, `of_le`, `trans`, `map`, `sup`, `comp`, `HasType.prod`, and the determinant criterion
  `IndexDvd.of_det_dvd` (Hermite normal form over a valuation domain).
* `Space.card_classes_le` (ClassCountBound.lean) is independent of the rest: a crude explicit bound for the number of
  classes of the standard definite hermitian space, by an injective map into integral vectors of bounded size.

## What I am unsure of

* **`IndexDvd` binders**: the text reading lists M, N, z twice — as the implicit section variables of line 14 and as the
  explicit arguments made by `variable (M N z) in`. Lean takes each once, explicitly: expected signature
  `IndexDvd {O V} [CommRing O] [AddCommGroup V] [Module O V] (M N : Submodule O V) (z : O)`. The dossier follows the
  text reading (the check requires it) and marks the three implicit entries `DUPLICATE in the text reading`. Not
  confirmed with `#check` (no Lean here).
* `Space.card_classes_le`, step 12: the witness γ = Y_g·Y_{g'}⁻¹ and κ = A_{g'}A_g⁻¹ are read off the terms
  (`gram_mul_of_gram_eq rfl (gram_inv_of_gram_eq e.1)` and `IsIntMatrix.one.add ((o g g').sub (o g' g'))`); the exact
  arrangement of the double-coset relation (which side is γ·g'.out·κ) depends on `DoubleCoset.rel_iff`, not replayed.
* `Space.card_classes_le`, step 10: the archimedean estimates |n|·C² and |n|²·C²·(2f)²N ≤ C³ are my reconstruction of
  what `ring_nf; gcongr <;> norm_num` closes.
* `IndexDvd.sup` (after = 1 line) and `IndexDvd.comp` (one line) carry triage `assembly`/`one-step` and no structured
  proof, as the check allows.
* No member looked unused; no hypothesis looked unused.

## Sampled for a second reading

`IndexDvd.of_det_dvd` (all steps, against `IsValuationPair.hermite`) and `Space.card_classes_le` steps 5–12.

## How the dossier is made

`gen/gen.py` + `gen/rbgen.py` (own tokenizer/slicer) + hand-written `gen/readings.py`; re-run
`python3 reading/units/149/gen/gen.py`.
