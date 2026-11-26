# Unit 155 — the five final theorems (module `Main`)

Dossier written by a Claude-side reader, 26 Nov 2026, against `lsernau/grh-lean` @ `72fead1`, edition `grh-compact`.

Five theorems, each proved by one term (no structured proof is required: at most one line after the statement).
Each member's `text` gives the statement in words and, in one sentence, its one-line proof. `python3 tools/rb.py check 155`
exits 0. Generator: `gen/spec155.py`.

## Points for the writer

* `riemannHypothesis : RiemannHypothesis` (Mathlib's statement) is proved by `New.zeta_zeros_on_line New.grh`, whose type is
  the artifact's `RiemannZetaZerosOnLine`; Lean accepts this because the two definitions agree up to unfolding (they are
  written identically, see the quoted Mathlib definition in `ambient_inputs`, from a local checkout at 3823257d, not the pin).
* `LFunction_eq_zero_re_of_isPrimitive` does not use primitivity: it is the general theorem specialised.
* Everything rests on `New.grh` (unit 154); the trust base is in the authors' guide (`GUIDE.md` §1): the statements here, the
  five theorems, and their `#print axioms`.
