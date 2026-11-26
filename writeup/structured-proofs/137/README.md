# Unit 137 — A Taylor–Wiles prime at a time (New/Patching)

Reader's dossier for the writer. Built by `gen/build.py` from `gen/content.py` (texts, readings and claims written by
the reader; lines, hashes, quotations, spans and typed facts computed by the program from the pinned sources).
Gate: `python3 tools/rb.py check 137` exits 0 (10 of 10 statements, 6 structured proofs, 144 steps, 122 leaves,
22 of 22 typed facts, 91 imports quoted, 226 of 226 arguments).

## Where to start
1. `exists_line_stabilizer_log` (OnePrime): the line stabiliser H ⊂ GL_N(k_w), a character a = l(h_00) to ℤ/m whose
   transfer is d∘det, and N!·d(ū) = N!. Elementary and self-contained.
2. `one_prime_first_order` (OnePrime): the abstract first-order lemma (rings, a finite group, a transfer). Read its
   statement slowly: its two conclusions (i), (ii) are exactly what `exists_tie` uses.
3. `exists_tie` (OnePrimeTie): the tie at one auxiliary place; steps 11.x map each argument of
   `one_prime_first_order`, step 12 is the chain-lemma argument, steps 13–18 the conversion of (ii).
4. `exists_diagOp_mem_ellIntegralForms`: the unit's result; steps 3–9 set up Ribet's element, 11 the module B,
   14–23 the operators Θ_d and the induction "the lifts do not move", 24–30 the conclusion.

## Letters (clashes with MEMORY.md)
The Lean names of this unit reuse letters of the write-up with other meanings; the texts keep Lean's names, so:
- `N` (OnePrimeTie) is the family of twisted Galois representations N_x = a·ρ_x, not the level N; the rank is
  written N = |n| in the texts (Lean `card n`).
- `a` is a character Gal(Ω/E) → O (not the multiple of N₁); `t` is the length of a root string (not 5r); `m` is a
  modulus (OnePrime) or a multiplier in Q̄_ℓ (exists_diagOp), not the number of theta lifts; `c` is the parameter of
  the base datum (a common multiple of stabiliser orders); in `weightedSum_ext` Lean's `c` is a character, written c′.
- Inside the proof of `exists_diagOp_mem_ellIntegralForms`, Lean's local `κ` is 2·N! (written κ′), not the weight.

## What I am unsure of
- The proofs are golfed terms; the claims were reconstructed from the terms, the doc comments and the statements
  of the cited lemmas. Least certain: step 12.2 of `exists_tie` (the exact linear form tested against u: the text
  says "the pairing of the T-twisted w with u"), steps 27–30 of `exists_diagOp_mem_ellIntegralForms` (how the
  unit factors (p_0c²)^k and w are cancelled), and step 9 of `one_prime_first_order` (signs).
- Signature (binders) of `exists_diagOp_mem_ellIntegralForms`: Lean also takes the section hypotheses `hQ` and `ha`
  (`include hQ ha`, line 87; the proof uses both). The census's text reading attaches that `include` to the next
  declaration only, because the `include` line is followed by `seal weightedSum in` and `attribute [-instance] … in`
  and the block then ends in `in`. `binders` follows the census (the check compares with it); the member's `text`
  states hQ and ha, and its `note` records this. Not confirmed with `#check` (nothing is built here).
- Signature of `BaseLevel.weightedSum_ext`: its signature binds a new `c` ({c g b}); the census then drops the
  section variable `c` (the base parameter), which Lean includes because `D : BaseLevel V κ c` depends on it.
- `weightedSum`: the census reads the arrow of the type `(ZMod m → ℤ) →+ R` as an argument; the entry is kept and its
  reading says it is the function to which the additive map is applied.
- `exists_tie`: the census takes the `:=` of the `let ρ := …` in the statement for the start of the value. The
  member carries `source_ranges` read from the text by the reader (not by Lean's parser; `source_ranges_basis`
  says so): statement from `lemma` to the end of the signature, value from `by` (line 103) to the end. The statement
  range equals the corrected span of the second reader's overlay (a second-reader message), and `statement_full` quotes it.
- Mathlib facts (`ambient_inputs`) are stated from memory, not quoted (Mathlib's sources are not in the workspace).

## Sampled for a second reading
Every step of `exists_line_stabilizer_log` and `one_prime_first_order`; in `exists_tie` steps 5, 10, 11.5, 12.8,
17.2, 18.2.2; in `exists_diagOp_mem_ellIntegralForms` steps 3, 11, 12, 22, 23, 29.

## Corrections (2026-11-26)
The second reader's corrections and statement-strength verdicts were applied by a correction reader (Claude); the
list, what was not applied and the old and new digests are in `CORRECTIONS.md`. Imports that name a classical result
now carry a `literature` record (relation, verdict, primary sources, the message it comes from).
