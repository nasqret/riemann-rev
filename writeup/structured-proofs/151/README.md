# Unit 151 — the endgame (folder `New/Endgame`)

**Corrected on 2026-11-26** after the second reading (a second-reader message, a second-reader message, a second-reader message), the Chapter II writer's
findings and the statement-boundary overlay (a second-reader message): see `CORRECTIONS.md`. The rest of this file is the first
reader's.

Dossier written by a Claude-side reader (following the reader's skill and contracts), 26 Nov 2026, against
`lsernau/grh-lean` @ `72fead1`, edition `grh-compact`. Nothing was built or run: every reading is from the source text.

## Where to start

1. `unit.json`, field `notation`: the letters used in every `text` and `claim` (a function of the artifact is always
   written with all its explicit arguments: R_{d,M}(x), λ_{d,M}(ν), h_main(D), rem(D), 𝓑(D), P_{D,s}, IndexLe(D, y, δ), …).
2. The three statements the top of the proof uses: `Data.integral_forms_long` (Theorem C), `Data.exists_family_covolumeSq_le`
   (A and B together), `entireL_ne_zero_of_primeError_le` (the one-sided criterion), with `IsPolar.exists_window_sub_mul_le`
   and `Data.remainder_eq` (used by unit 154).
3. Then the proofs, in the order of the files: `proofs/isPolar_primeError.json` (the Mellin/Laplace identity and the residues),
   `proofs/entireL_ne_zero_of_primeError_le.json` (Landau), `proofs/eventually_moment_le.json` and
   `proofs/exists_window_sub_mul_le.json` (the window), `proofs/remainder_eq.json`, `proofs/heightPerRow_le.json`,
   `proofs/short_forms.json` (Theorem A), `proofs/enough_forms.json` (B), `proofs/heightLe_volume_rows.json`,
   `proofs/heightLe_volume_ratio_sq.json`, `proofs/integral_forms_long.json` (C), `proofs/exists_family_covolumeSq_le.json`.

29 members, all treated (none out of scope); 18 structured proofs, 121 steps, 104 leaves (longest 8 lines);
87 imports quoted at their lines (86 before the corrections); 16 typed facts. `python3 tools/rb.py check 151` exits 0.

## How it was made

`gen/spec151.py` (proofs, imports, ambient facts) and `gen/spec151_members.py` (statements and binder readings) hold the
reader's words and the source ranges; `gen/rbgen.py` slices the pinned files, quotes, hashes and extracts the written
intermediate types; `tools/rb.py check` is the independent check. Re-run: `python3 reading/units/151/gen/spec151.py`.

## What I am unsure of (please read before writing)

* **Binders not confirmed by Lean.** `Data.exists_family_covolumeSq_le` stands on `binders_basis: "lean"`, but
  `binders_lean` is *not* Lean's output (nothing is built here): it is my reading of Lean 4's rule for theorems. After
  `omit I hV i hn` (line 73) the statement binds its own n, y, δ under ∃ and its own explicit D, so I expect
  `{P : Parameters} (D : Data P)`; the census lists the section variables n, y, δ too. Confirm with `#check` on the Helios build.
* **A phantom binder the check requires.** The census reads `D.ramifiedColumns →ₗ[ℂ] D.rows` (the type of
  `Data.projectedPoincare`) as a premise and lists an unnamed explicit argument; the check compares entry by entry, so the
  dossier lists it with a `reads` that says it is *not* an argument (Lean: `{P} (D) (s : D.G)`; the value is a linear map,
  applied to columns by coercion and also used unapplied, through its range, in Theorem B). This is a tool issue: without
  the entry the check reports "its `binders` are not the arguments of the declaration (3 listed). The text gives 4: {P};
  (D : Data P); (s : D.G); (D.ramifiedColumns)", and with `binders_basis: "lean"` it reports "its `binders` leave out an
  argument that the declaration itself writes. The text gives: {P}; (D : Data P); (s : D.G); (D.ramifiedColumns)"
  (reproduced by calling `binder_problems` of `tools/rb.py` on the member without the entry).
* **Census boundary error.** In `IsPolar.eventually_moment_le` the statement contains `let F v := …`; the line census takes
  that `:=` for the start of the value (statement_lines 41–42). The member carries `source_ranges` computed by my generator
  from the text (statement to the end of `k ! * t / R ^ k` on line 43, value from `h.elim`), not by Lean's parser.
* **Goal order inferred, not observed.** In `isPolar_primeError` the `refine` leaves three holes; I read them as
  [the bound `?_`, `?q`, `?B`], closed by lines 88–89, 90–110 and 111 (Lean orders new goals by occurrence). The last line
  `grind [ofReal_one]` then proves the analyticity of (s − 1)Φ(s) from `A` and `this` (G(1) real). Likewise, in
  `short_forms`, `heightLe_volume_rows`, `eventually_moment_le` and `exists_window_sub_mul_le`, steps that "prove the hole of
  step …" are inferred from the term structure.
* **Mathlib.** The pin 56a00585 is not on this machine. Mathlib facts are recalled, or quoted where the entry says so.
  Since the corrections of 2026-11-26 (`CORRECTIONS.md`) the zeta facts used by `re_logDerivMean_one` (ζ₁(1) = 1,
  ζ₁′(1) = γ, ζ(s) = (s − 1)⁻¹ζ₁(s)), `LFunctionTrivChar₁` and the two older quotes are quoted from Mathlib at the pin.
* **Hypotheses used only weakly.** `isPolar_primeError` uses `hd : d % 8 = 7` only to get d ≠ 2 (for `quadTwist_ne_one`).
  `IsPolar.eventually_moment_le` discards the meromorphy of Φ and the residue limits of `IsPolar` (only measurability, the
  bound, the Laplace identity and analyticity of (s − 1)Φ on Re s ≥ 1 are used); the residues enter only through Landau.
* **Imports' readings** are from their statements and doc comments, not from their proofs; the deep ones (seesaw identity,
  `one_determinant`, `exists_indexDvd_Bmu_divisible`, `crude_rows`, `IsFitFamily`) are summarised, and their owning units
  should be the reference.

## Second reading done

Every leaf of `short_forms`, `heightLe_volume_rows`, `isPolar_primeError`, `eventually_moment_le`, `re_logDerivMean_one`
and `remainder_eq` was compared with its quoted span after generation (argument order of `one_determinant` and of
`hasDerivAt_integral_of_dominated_loc_of_deriv_le` checked against their statements; the domination bound corrected to the
neighbourhood {Re z > 2 + 2ε′}). The English is not checked by any program.
