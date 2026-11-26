# Unit 153 — the statements (module `Statements`)

Dossier written by a Claude-side reader, 26 Nov 2026, against `lsernau/grh-lean` @ `72fead1`, edition `grh-compact`.

Four definitions of propositions, stated with Mathlib's ζ and Dirichlet L-functions only (the module imports nothing but
Mathlib). No arguments, no proofs. `python3 tools/rb.py check 153` exits 0. Generator: `gen/spec153.py`.

## Points for the writer

* `RiemannZetaZerosOnLine` excludes s = 1 explicitly: Mathlib's ζ is a total function with a conventional value at the pole.
  The trivial zeros are written −2(n + 1), n natural.
* `DirichletLNonvanishingRightOfHalf` excludes only the pair (χ principal, s = 1); `1` is Mathlib's principal character
  modulo N (1 on units, 0 elsewhere), so for N = 1 it is the constant 1 and L(s, 1) = ζ(s).
* `PrimitiveDirichletLZerosOnLine` is the same as `DirichletLZerosOnLine` restricted to primitive characters (conductor N).
* The Mathlib definitions are quoted from a local checkout at 3823257d (2026-10-04); the pin 56a00585 is not on this machine.
