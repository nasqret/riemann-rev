# Unit 144 — elementary divisors of a Frobenius-twisted Hecke operator (New/TwistedHecke)

> **2026-11-26, statement-boundary overlay (a second-reader message):** members whose statement contains a `let`/`have` now carry the whole statement (`statement_lines`, `statement_span`, `statement_lean_full`); the census's statement lines stopped at the binding's `:=`. Imports of such declarations quote them to their end. See `CORRECTIONS.md`.
>
> **2026-11-26, second reading (a second-reader message) applied:** the depth factorization (failure at w^{l+1}, x ≤ l + depth, root lemma at labelling 0 and order l), m_i not a valuation and only d square, the projector's coefficient condition H, the final bound through `IndexDvd`, excessWeight at a = a′, the volume identities for every real P > 1 and D < 0, the rank shift in `index_mul_finrank_excessCond_le`, k first in the arguments of `volume_inter_slab_eq_signed_sum` (now `binders_basis` "lean", not Lean's output), and six Mathlib facts quoted at the pin. The counts below are those of the first hand-off; now 32 imports and 931 arguments (1 member on the "lean" basis). See `CORRECTIONS.md`.


Reader: the reader role, performed by a Claude agent (claude-opus-5-5) spawned by the coordinator (2026-11-26, grh-compact at 72fead10). `python3 tools/rb.py check 144` passes: 78 of 78 statements at
their lines, 32 structured proofs, 357 steps (320 leaves, longest 8 lines, no `indivisible` exception), 50 of 50 typed
facts, 31 imports quoted, 930 of 930 arguments accounted for.

## Where to start

The unit is one long argument ending in `TwistingData.hasType_twisted_hecke` (ElementaryDivisors.lean:217), which
New/Columns/TwistedHeckeType.lean uses. Read in this order:

1. **Vocabulary** (TwistingData.lean): the structure `TwistingData` (letters ι_s : W → R, s ∈ ℤ/N, consecutive letters
   congruent up to the P-power Frobenius mod p, alternating parity, w² = p, residue field of q = P^N elements);
   `letterMatrix` (g_s = ι_s(g) or ι_s((g⁻¹)ᵀ)), `polyAction`, `letterRep` (ρ = ⊗_s Sym^n(g_s)), `deepIndicator`,
   `depth`, `rootVar` (u_s, ū_s), `excessWeight`, and the spaces `translatesIn`, `excessCond`, `deepForms`.
2. **Root lemma** (RootLemma.lean): `stepanov_count`, the filtrations (`adicFiltration`, `gaussFiltration`,
   `IsRealFiltration`), `aeval_sub_mem_of_gaussFiltration`, then `TwistingData.root_lemma`: a term least for
   (w-valuation + weight) among all Levi translates has excess ≤ 0.
3. **Counting** (InterlacingCone.lean, Counting.lean, DeepFormCost.lean): the interlacing determinant and the volume
   of the cyclic interlacing cone (`prod_mul_volume_inter_slab`), the flag count, `finrank_excessCond_le_volume`
   (Frobenius amplification + lattice points + root lemma), `index_mul_finrank_excessCond_le`, and the deep-form bound
   `sum_finrank_deepForms_le` (via `exists_le_weight_of_mem_deepForms`, a Combinatorial Nullstellensatz argument).
4. **Projector** (ClassMeans.lean, FrobeniusFactors.lean): Levi-invariant means (`ClassMean.exists_mean`), the
   Frobenius-power operators and their filtration bounds (`frobOperator_mem`, `pow_dvd_coeff_conj_frobOperator`),
   then `exists_projector`.
5. **Assembly** (ElementaryDivisors.lean): `of_pairing`, `exists_depth_factorization`, `hasType_twisted_hecke`.

## Are all 78 members used?

The proposal says 3 are reached by name; the name search misses dot notation (`T.foo`, `.map`), instances and simp
sets. By reading, **every member is used** on the chain to `hasType_twisted_hecke`: a `grep -w` over the artifact for
each member's short name finds it in a proof or statement of another member of this chain (e.g. `X_mem_gaussFiltration`
in `pow_dvd_coeff_conj_frobOperator` and `degree_le_of_coeff_frobOperator`; `letterRep_map` in
`card_le_finrank_translatesIn` and `exists_projector`; `one_add_val_sub_one_sub` as a simp lemma in Counting and
FrobeniusFactors; `ClassMean.map_C_mul_mul_C` in `exists_projector`). The three instances are used implicitly:
`IsRealFiltration (adicFiltration w)` (RootLemma:46) and `IsRealFiltration (gaussFiltration F c)` (RootLemma:64) are
needed wherever a Gauss filtration over the w-adic filtration is passed as an `IsRealFiltration` (root_lemma, frobOperator_mem
applications); the parahoric `FiniteIndex` instance (Counting:24) is presumably needed by the index arithmetic in
`index_mul_finrank_excessCond_le` — this last one is a reading, not verified (instance use is invisible to text search).
So `out_of_scope` is empty.

## What I am unsure of

* **Binders Lean is expected to bind differently** (the dossier follows the text reading, which the check compares
  with; each such entry's `reads` starts with `NOT expected in Lean:` or `DUPLICATE in the text reading:`, and the `text`
  says so). Bound variables mistaken for section variables:
  - `letterMatrix`, `polyAction`, `letterRep`, `translatesIn`: g (bound by `fun g ↦` / `∀ g ∈`) — so Lean's explicit
    arguments are (T, s), (T), (T, n), (T, n, τ, I, B), matching every use (`T.letterMatrix s g`, `T.letterRep n g`);
  - `depth`: a (`(a := n)` is a named argument); `excessCond`: i (`∃ i`); `diagonal_pow_depth`: s (`fun s ↦`);
  - `frobOperator`: s; `frobOperator_map`, `frobOperator_mem`, `pow_dvd_coeff_conj_frobOperator`: s, d;
  - `exists_depth_factorization`: Q, R, β (bound in the statement); `exists_projector`: β; `hasType_twisted_hecke`: c
    (bound by `fun c i ↦` in hY); `root_lemma`: w (the statement mentions the field `T.w`); the instance at
    RootLemma:64: k, a (`fun (a, b)`);
  - `excessCone`: a listed twice (`variable (a) in`), Lean takes it once, explicitly.
  - **Missing in the text reading**: `volume_inter_slab_eq_signed_sum` — Lean also takes the implicit `{k : ℕ}` first;
    the text reading stops at the `:=` of `let Δ τ := …` inside the statement. Evidence: line 130 of the same file
    applies `@volume_inter_slab_eq_signed_sum k 0 P ⊤ q 1 (pieriCone ⊤ P) (…)`. Recorded in the member's `binders_note`;
    since the second reading (a second-reader message) its `binders` list starts with k, on `binders_basis` "lean" with `binders_lean`
    marked "NOT PRINTED BY LEAN" (see `CORRECTIONS.md`).
  - Instance arguments marked `maybe` that the definition's term does not use are left out (P, q, map, letterMatrix,
    deepIndicator, rootVar, excessWeight: [NeZero N]; conjSubst: [IsLocalRing W]; slab: [Add T], [One T];
    frobGenericMatrix, letterConj, indexWeight: [NeZero N]); the others are kept.
  None of this is confirmed with `#check @Name` (no Lean on this machine).
* **`volume_inter_slab_eq_signed_sum`**: because the line census starts the value at the `let`'s `:=`, the rest of the
  statement (lines 48–50) is part of "the value", and the absolute-value bar `|` that opens it is read by the checker as
  the first arm of a definition by equations. The proof file therefore has a top step `0` with a single `case` child
  `0.1` covering lines 48–106, whose head is the rest of the statement; the real proof steps are children of `0.1`.
  Nothing is split there; the claims say so.
* **Typed facts that the checker cuts at a line break**: for a `show` whose type continues on a line that starts at a
  column left of the `show` (e.g. FrobeniusFactors:68–69, 94–95; Counting:192–193), the checker's (and the generator's)
  `typed_fact` ends at the line break. The quoted fact is therefore a prefix of the written type in those places; the
  claims state the full fact.
* **Claims in the long golfed proofs** (`ClassMean.exists_mean`, `root_lemma`, `finrank_excessCond_le_volume`,
  `exists_depth_factorization`, `exists_projector`, `hasType_twisted_hecke`, `pow_dvd_coeff_conj_frobOperator`,
  `of_pairing`) describe what each block establishes as read from the text; goal order after `refine`/`apply` with
  several `?_`, and the division of work between `simp`/`grind`/`bound` calls, were not replayed. Where I could not
  pin a detail down, the claim says what is established at the level of the block (for example `of_pairing` steps
  7–13, `exists_projector` steps 13–18, `pow_dvd_coeff_conj_frobOperator` step 4.2.2's case condition q).
* `ClassMean.exists_mean`: the trace computation in step 18.3 and the nilpotence in 18.2 are my reading; the source
  gives only automation there.
* No hypothesis looked unused.

## Sampled for a second reading

Every step of `TwistingData.p_dvd_letterMatrix_of_mem_parahoric`, `sum_deepIndicator`, `stepanov_count`,
`aeval_sub_mem_of_gaussFiltration`, `det_interlacing_indicator`, `prod_mul_volume_inter_slab`,
`exists_mem_excessCone_mem_Icc`; and the first ten steps of `root_lemma` and of `exists_le_weight_of_mem_deepForms`.

## How the dossier is made

`gen/gen.py` + `gen/rbgen.py` (own tokenizer/slicer, no code shared with `tools/`) + `gen/b144.py` (binder readings
from the census list, with per-member overrides) + the hand-written parts `gen/r1.py` … `gen/r7.py` (one per pair of
source files), merged by `gen/readings.py`. Re-run: `python3 reading/units/144/gen/gen.py`.
