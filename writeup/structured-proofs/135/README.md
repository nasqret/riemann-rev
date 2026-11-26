# Unit 135 — heights of families indexed by ℓ-adic embeddings; the product formula; one Gram determinant

**Checked on 2026-11-26** against the second reading (a second-reader message) and the statement-boundary
overlay (a second-reader message): no correction was needed; see `CORRECTIONS.md`.

Reader: the reader role, performed by a Claude agent (claude-opus-5-5) spawned by the coordinator (dossier written 2026-11-26 against grh-compact at 72fead10). `python3 tools/rb.py check 135` passes:
18 of 18 statements at their lines, 7 structured proofs, 52 steps (47 leaves, longest 5 lines), 6 of 6 typed facts,
9 imports quoted, 178 of 178 arguments accounted for.

## Where to start

1. `HeightLe` (Heights.lean:21) — read its text first; everything else in the unit is about it. A height bound is
   witnessed by one nonzero H, a real α (archimedean, for all σ ∈ Aut ℂ) and reals e(ℓ) (ℓ-adic, for all ι : ℂ ≅ ℚ̄_ℓ),
   with α + Σ_{ℓ<M} e(ℓ) ≤ c eventually. Note that e may be negative: only `HeightLe.nonneg` rules out negative c, and
   only for the constant family 1.
2. `HeightLe.nonneg` (the product formula) — the structured proof shows the classical argument: N_{ℚ(H)/ℚ}(H) and the
   product formula for ℚ (`log_product_formula`).
3. `one_determinant` — the only member used by the main inequality besides the HeightLe calculus (cited in the head of
   `New/Main.lean`). Its text is long because every hypothesis is spelled out (Λ, w, l).
4. The rest of OneDeterminant.lean (`card_mul_sum_det_le`, `finrank_sub_le_re_inner_dyadSum`, `exists_few_translates`,
   `exists_extend_basis_of_span_eq_top`) is linear algebra for consumers in other units (Filling, Exchange, Rows).

## What I am unsure of (say so in the note, or check after a build)

* **Binders that Lean is expected to bind differently from the text reading** (the check compares with the text
  reading, so these lists follow it; the entries are marked `NOT expected in Lean: …` in `reads`, and the `text` says
  so). In each case a letter of the statement is a *bound* variable that the text reading mistakes for a section
  variable of the same name:
  - `inner_sum_sum_eq_card_mul`: m, [Fintype m], b (the statement's b is bound by `∀ a b`);
  - `card_mul_sum_det_le`: b (bound in `hu` and `h`), v (bound by `∀ v ≠ 0`);
  - `finrank_sub_le_re_inner_dyadSum`: G, [Group G], [Fintype G], v (v bound by `∀ v ∈ U`);
  - `exists_extend_basis_of_span_eq_top`: k, [Field k] (k bound by `∃ k z`);
  - `one_determinant`: m, [Fintype m] (m bound by `∃ m` in `l`).
  - `IsSpread`: the instance [Module.Finite ℂ V] (marked maybe) is left out, as the definition's term does not use it.
  Not confirmed with `#check @Name` (Lean is not run on this machine; `binders_basis` is therefore not "lean").
* `normDet` and `gram` are Mathlib's (not in the artifact); their meaning (normDet u = √det(u*u)) is taken from the
  readable edition's comments (grh/src/Lib/General/LinearAlgebra/GramDeterminant.lean) and recorded as an ambient input.
* `card_mul_sum_det_le`: the goal order after `apply ((sum_mono …).trans _).trans'` (step 5) and which goals
  `repeat' split` and `all_goals simp` close (steps 7, 11) are read from the text, not replayed. The mathematics of the
  claims (Fourier expansion, kernel count, positive-type Cauchy–Schwarz) is standard; the exact split of work between
  the automation calls may differ.
* `HeightLe.nonneg` step 1: the order of the eight names of `choose` (H, H ≠ 0, α, d, e, f, M₀, g) is my reading of how
  `simp` normalises `∃ H α e, …` (exists_and_left pulls the conjuncts out); the uses (`k rfl d`, `f ⟨default, ·⟩`,
  `g _ le_self_add`) confirm d, f, g.
* No hypothesis of any member looked unused.

## Sampled for a second reading

All steps of `HeightLe.nonneg`, `HeightLe.mul`, `one_determinant` and `exists_few_translates` were re-read against the
source after generation; the other proofs were read once.

## How the dossier is made

`gen/gen.py` (with `gen/rbgen.py`, its own tokenizer and slicer, sharing no code with `tools/`) reads the census and
the pinned source and emits `unit.json` and `proofs/*.json` from the hand-written `gen/readings.py` (texts, binder
readings, step trees with line ranges or spans, claims). Re-run: `python3 reading/units/135/gen/gen.py`.
