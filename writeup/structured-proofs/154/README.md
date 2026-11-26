# Unit 154 — the top of the argument (module `New.Main`)

Dossier written by a Claude-side reader, 26 Nov 2026, against `lsernau/grh-lean` @ `72fead1`, edition `grh-compact`.
Nothing was built or run.

## Where to start

`proofs/star_inequality.json` (the inequality (⋆): Theorems A–B against Theorem C, h_main cancels), then
`proofs/eventually_primeError_le_rpow.json` (the one-sided bound: move log x₁ into the window, then (⋆) for the modified
data), then `proofs/grh.json` (Landau's criterion on the class N₀/2 − 1 modulo N₀ = 18480q), and the two reflections by the
functional equation (`zeros_on_line.json`, `zeta_zeros_on_line.json`). Letters: `unit.json`, field `notation`.

5 members, 5 structured proofs, 34 steps, 27 leaves (longest 4 lines), 32 imports quoted, 5 typed facts.
`python3 tools/rb.py check 154` exits 0. Re-run the generator: `python3 reading/units/154/gen/spec154.py`.

## What I am unsure of

* The one-line automation steps (`grind`, `simp_all`) are described by what they establish and by the lemmas they are
  given; which rewriting does what inside them is my reading (e.g. `zeta_zeros_on_line` step 1.2, where I assume the simp
  lemma `LFunction_modOne_eq` turns L(s, 1 mod 1) into ζ(s)).
* `eventually_primeError_le_rpow`, step 7.3: the exponent comparison is closed by `grind` inside the size calculus; my claim
  follows the authors' comment (first term ≤ φ(N₀)(log b)⁶/√x, log b = x^ε).
* The hypothesis `0 < ε/6` of `eventually_primeError_le_rpow` just says ε > 0 (it is the form `exists_data` asks for).
* Mathlib facts are recalled or quoted from a local checkout at 3823257d, not at the pin 56a00585 (see each entry's `basis`).
* Readings of imports from units 151, 152, 148, 140, 143, 106, 102 are from their statements; the dossiers of those units
  are the reference.
