# Unit 136: Lifting crystalline extension classes in large weight: Kisin modules with exponents, cokernel killers and cup products that vanish up to a power of p

Merged from the chunks 136-a, 136-b by `book/plan/merge_chunks.py` (2026-11-26 10:26 UTC). Each chunk was read by its own reader (`book/plan/SPLIT.md`); their notes follow.

## Chunk 136-a

## Chunk 136-a — Lift: Kisin modules with exponents, cokernel killers, cup products (New/Lift, five modules)

> **2026-11-26, statement-boundary overlay (a second-reader message):** members whose statement contains a `let`/`have` now carry the whole statement (`statement_lines`, `statement_span`, `statement_lean_full`); the census's statement lines stopped at the binding's `:=`. Imports of such declarations quote them to their end. See `CORRECTIONS.md`.


Reader's dossier of chunk a of unit 136 (`book/plan/SPLIT.md`): `New.Lift.CupProductBound`, `ExponentLattices`,
`HodgeExpansion`, `CokernelKillers`, `LongGap`. As chunk a it carries the unit's title and summary. Built by
`gen/build.py` from `gen/content*.py` (one content file per module; texts, readings and claims written by the reader;
lines, hashes, quotations, spans and typed facts computed by the program). Gate: `python3 tools/rb.py check 136-a`
exits 0 (122 of 122 statements, 56 structured proofs, 271 steps, 235 leaves, 15 of 15 typed facts, 128 imports quoted,
1035 of 1035 arguments). No member of chunk 136-b is used.

### Where to start
1. Vocabulary (imports): `JumpLattice` (a crystalline lattice with jump sets U_i per letter), `kisinAinf` (M),
   `kisinLocAinf`/`kisinLoc` (M and 𝒩 with all φ^aE inverted), `letterPart`, `formsOfType`, `valueAt` (μ∘φ^{−a}),
   `hodgeFil` (t^nB_dR^+). Then `withExponents` (ExponentLattices): the module of elements with exponent c(a, u) at φ^aE.
2. `mem_withExponents_stdExponent_iff` (HodgeExpansion): standard exponents ⇔ φ^l(M) at the letter — the bridge between
   exponents and Kisin modules.
3. `liftIdeal`, `KillsCokernel` and `killsCokernel_of_isUnramified` (CokernelKillers): p^sE^t kills the cokernel when
   all jumps are ≤ (p − 3)(s + t), via derivations (`mem_liftIdeal_of_derivation`) and Nakayama.
4. `ScaledCupBounds.of_isSafe` (CupProductBound), then in LongGap: points over constants (`pointsOver`), the cost of
   deepening (`exists_reaches_deep`), safety (`isSafe_of_exponents`), the walk (`scaledCupBounds_of_points_at_cuts`)
   and its two applications (`scaledCupBounds_of_killsCokernel`, `pointsOver_nonempty_of_long_gap`).

### Letters
Lean names are kept: p (the prime; ℓ in the Selmer bound), O = (O, ζ) coefficient ring, S, S' sides of a pairing with
lattices Y, C (Ỹ = Y × C the extension), P a pairing modulo p^m, E the Eisenstein element of the chart, z its
coordinate, τ = [ε^{1/p}] − 1, σ: j ↦ j^p on letters (σ^{−a}(i) = stepBack(i, a)), λ₀ = coord₀, K' the field fixed by
Γ', 𝒦_a = valueField(a). Clashes with MEMORY.md: `a` is an index of φ^aE or an exponent (not the multiple of N₁), `c`
an element of C or an exponent function, `t` a jump/exponent or the period t of B_dR (texts say which), `N` a degree
(long gap), `H` a hypothesis name or a bound, κ an exponent of p (not a weight), `W` a window width or a submodule.

### What I am unsure of
- Claims of the long golfed terms were reconstructed from the terms, docstrings and the cited lemmas' statements; the
  least certain are `exists_depth_step` (steps 8–11: the lifting-the-exponent bookkeeping), `exists_reaches_depth_succ`
  (step 1.1.4), `mem_withExponents_stdExponent_iff` (steps 4.2.2.x), `ScaledCupBounds.of_isSafe` (steps 7–10: the
  cohomological reduction to Γ'), `scaledCupBounds_of_points_at_cuts` (steps 13–18: which tool is used in which of the
  four cases), `exists_comb_of_jumpMultiplicity_le` (Auerbach part) and `pointsOver_nonempty_of_long_gap` (step 6).
- Census readings of the arguments (the check compares `binders` with them; nothing could be confirmed with `#check`,
  nothing is built here). Where they differ from what Lean takes, `binders` follows the census and the entry's
  reading says so:
  * section variables named only through a bound variable (`∀ a`, `∑ l`, `∀ ⦃i c x⦄`, `{x | …}`, `∃ a`) are listed by the
    census although Lean does not take them (e.g. `withExponents`: an extra `a`; `exists_depth_step_zero`: `l`;
    `exists_reaches_deep`: S', c, i, c', x, n; `Reaches`: i; several `i`, `a`, `y`, `n`);
  * section variables that only the types of other arguments mention (p, [ThePrime p], Γ, k behind `S : PairingSide O`
    or `L : JumpLattice O`) are not listed by the census although Lean takes them; the texts name them;
  * arrows of bundled maps (`→ₗ`, `→+`) read as premises (`wittPairing`, `constantAt`): kept, read as the arguments of
    the map; `constantAt` lists S and i twice (implicit and again from `variable (S i) in`);
  * `mem_hodgeFil_of_hodge_basis`: an extra leading `[ThePrime p]` kept from before `p` is declared again (line 76).
- `let` in the statement: `wittPairing_constantAt_and_thirdPairing` (`letI B := …`) and `coeff_mem_constantsModE`
  (`let d := …`): the census takes that `:=` for the start of the value. Both members carry `source_ranges` read from
  the text by the reader (not by Lean's parser; `source_ranges_basis` says so) and no `statement_lean`.
- Mathlib facts (`ambient_uses`, `ambient_inputs`) are named from memory and not quoted (Mathlib is not in the
  workspace).

### Sampled for a second reading
Every step of `ScaledCupBounds.of_isSafe`, `exists_depth_step`, `mem_liftIdeal_of_derivation`, `exists_reaches_deep`,
`isSafe_of_exponents`, `scaledCupBounds_of_killsCokernel`; every leaf of `mem_withExponents_stdExponent_iff` and of
`pointsOver_nonempty_of_long_gap`.

## Chunk 136-b

## Chunk 136-b — Lift: few low jumps, sparse thick letters, tame types (New/Lift, three modules)

Reader's dossier of chunk b of unit 136 (`book/plan/SPLIT.md`): `New.Lift.FewLowJumps`, `SparseThickLetters`,
`ExponentTheorems`. Claimed by `mkdir` after 137 and 136-a passed their gates (SPLIT.md rule 7). Built by
`gen/build.py` from `gen/content*.py`; `gen/content_zimports.py` makes the imports of chunk-a declarations (unit "136")
from the texts of the 136-a dossier. Gate: `python3 tools/rb.py check 136-b` exits 0 (19 of 19 statements, 13 structured
proofs, 159 steps, 140 leaves, 19 of 19 typed facts, 72 imports quoted, 373 of 373 arguments).

### Where to start
1. `ExponentTheorems`: the two results of the unit, `few_low_jumps` (length bound) and `tame_types_exponent`
   (exponent independent of the ramification index), both through `mem_cupOrthogonal_of_scaledCupBounds` and the
   universal side (`universalSide`: C = Z_f(L), α = id).
2. `FewLowJumps`: `exists_scaledCupBounds_few_low_jumps` (the submodule V), resting on
   `exists_relLength_deepConstants_le` and the one-step bound `relLength_deepConstants_le`.
3. `SparseThickLetters`: `TameChart`, `exists_tameChart`, `killsCokernel_of_isKilledBy` (tame cokernel killer), then
   the cut-window walk `scaledCupBounds_of_cut_windows` and its two applications.

### Letters
As in 136-a. New in this chunk: f the residue degree of the chart, e its index (Lean `k.e`/`d.e`) — the texts write
e_k where a section variable `e` is also present; ζ_E and s = tameGen of a tame chart; ϖ with ϖ^e = p; T the thick
letters; β, b, G window positions; X, J, s₀, n size parameters (all as in Lean).

### What I am unsure of
- Claims of the longest proofs are reconstructions from golfed terms: `relLength_deepConstants_le` (steps
  6.2.2.13–6.2.2.22: the cost-zero operator and the identity E^{p^a} = φ^a(E) + p·r'), `scaledCupBounds_of_cut_windows`
  (step 5), `scaledCupBounds_sparse_thick` (steps 5–6), `exists_tameChart` (steps 5–10), `tame_types_exponent` (6.3).
- Census readings of the arguments (followed in `binders`, each deviation said in its reading; not confirmed with
  `#check`): duplicates from `variable (cut s b n J s₀ G) in` and `variable (p r N) in` (listed implicit and explicit);
  `variable [Γ]` read as an extra instance of type Γ (TameChart lemmas); `k.e` read as the section variable `e`
  (`killsCokernel_at_cut`, `scaledCupBounds_sparse_thick`); bound variables read as section variables (`∀ b` in
  `relLength_deepConstants_le`, `∀ s` in `scaledCupBounds_sparse_thick`, `∀ i`/`c` in
  `exists_scaledCupBounds_few_low_jumps`). `universalSide` also takes the section hypothesis `hF`, which the census
  does not list (its `note` says so).
- Mathlib facts are named from memory and not quoted.

### Sampled for a second reading
Every step of `killsCokernel_of_isKilledBy`, `few_low_jumps`, `tame_types_exponent`; steps 6.2.2.x of
`relLength_deepConstants_le`.

