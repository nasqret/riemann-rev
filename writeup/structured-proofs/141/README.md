# Unit 141 — the seesaw identity for the chain of theta lifts, and the index types of the data

> **2026-11-26, second reading (a second-reader message, a second-reader message), literature and the writer's findings:** 22 corrections (the
> seesaw reading, the cut multiplicities, the weights of the translations, tame characters, the generic Bessel normal
> form, normUnit at 0, and six bullets elsewhere); see `CORRECTIONS.md`, section "second reading".

> **2026-11-26, statement-boundary overlay (a second-reader message):** members whose statement contains a `let`/`have` now carry the whole statement (`statement_lines`, `statement_span`, `statement_lean_full`); the census's statement lines stopped at the binding's `:=`. Imports of such declarations quote them to their end. See `CORRECTIONS.md`.


Folder `New/Seesaw` of `grh-compact` (21 modules) at commit `72fead10`. Reader: a Claude-side reader following the
reader's skill and `tools/references/contracts.md`. Check: `python3 tools/rb.py check 141` exits 0 (line census;
no Lean was run here).

## Where to start
1. **`Data.seesaw`** (`SeesawTheorem.lean:135`) and `proofs/Data.seesaw.json` (7 steps). This is the input of
   Theorem A (`Data.short_forms` uses `D.seesaw`).
2. Its two engines in `SeesawTheorem.lean`: `Data.exists_isAdmissibleComb_unfolding` (induction over the lifts:
   move the last lift across the integral, unfold one Bessel period, cut it into a finite sum) and
   `Data.exists_stage_cut` (the finite cuts; multiplicities divide powers of the conductor of ϑ).
3. What they use, in order:
   - `UnfoldingStages`: `unfoldStage` (the function after k unfoldings), `unfoldStage_even` (after 2i+2 steps it is a
     coefficient of i+1 paired definite lifts), `hasNearLines_of_unfoldStage_ne_zero` (where it is non-zero, the
     lattice lines move little);
   - near lines of lattices: `EqualLinesOrbit`, `LinesStep`, `StandardLatticeLevel`;
   - cuts and periods as finite sums: `IntegralAsCosetSum`;
   - evaluation of a pair of lifts: `EdgePair` (zero terms, arrow pairs), `DoubleLiftValue`, `AdmissibleEvaluation`,
     `MovedVacuumComb`;
   - from an invariant combination to a good datum: `GoodDatumExists`;
   - bookkeeping of admissible combinations: `AdmissibleComb`, `LatticeAndTorsionDefs`, `IntegralAway`.
4. Shared objects defined here and used across the proof: `IndexTypes` (chosen places, ω, χ, μ⁰_j, pairs, the level
   prime N and π, tame characters and twists, index types X_j, Y_j, 𝖦, e₀), `GradingsOfY` (gradings of the Y_k, the
   lifts liftY, ι), `PairTensorData` (the grid spaces of `Exchange`), `NamesAtSplitLevel` and `LiftCharacters` (the
   Gauss-sum operator F at the level prime, used by `Columns`), `FramesForY`, `BesselGeneric`.

## Counts
312 members (160 lemmas, 91 definitions, 36 abbreviations, 16 instances, 8 structures, 1 class); 83 structured
proofs, 550 steps, 503 leaves (longest 8 lines, no indivisible leaf); 68 typed facts; 74 imports quoted at their
lines with their owning units; 9 Mathlib facts under `ambient_inputs` (statements recalled, not quoted: Mathlib is
not in this workspace). Lemma triage: 83 argument, 45 one-step, 28 automation, 4 computation.

## What I am unsure of
- **Binders** follow the text reading of `rb.py signature` and await comparison with `#check @Name`.
  Across 42 members, 80 entries are marked `listed by the text reading only`. Of these, 78 are section variables that the
  reader expects Lean to omit. Two further entries in `IsAdmissibleEval` flag the section type `q` and its
  `Fintype q` instance for comparison with the elaborated signature. Seven duplicate entries in four members
  come from `variable (x) in` prefixes (ArrowPair, IsSplitLevel.diagN, translateSum, coverMultiplicity).
  Fifteen members carry a `binders_note` about arguments the text reading misses. Examples include the split-level
  instance through `liftFn`/`diagNInv`/`embedGL`, `p`, `[Fact p.Prime]` and `[PadicPlace p]` through `ιₚ`,
  ε and `[Frame 𝔰 ε]` in `Filling.Fits.*`, E, X, X′ and X₀ in `integral_theta_eq_lift₂`, and P and D in
  `Data.exists_stage_cut`. See `unit.json` under `notes.binders` for the current account.
- **Claims of long rewrite and simp chains** state the mathematical effect read from the lemma names and the shape
  of the terms, not from running Lean. Sample these first: `ArrowPair.zeroTerm_splitting_tripleWeil` (steps 4–11),
  `exists_isAdmissibleEval_std` (14–24), `isAdmissibleEval_finEval` (8–15),
  `Data.exists_isAdmissibleComb_reducedVacuum` (3–10), `Grading.HasNearLines.step` (9–18),
  `IsSplitLevel.translateSum_eq_sum_name` (5–20), `Data.exists_indexDvd_fourierOp_pow` (3–15),
  `Filling.Fits.poincare_bessel_normal_form` (4–9), `Grading.exists_integral_eq_sum_over_cut` (6–15),
  `exists_branching_pairing` (4–9).
- **Statements with a top-level `let`** (exists_stage_cut, Grading.exists_integral_eq_sum_over_cut,
  integral_theta_eq_lift₂, ArrowPair.integral_constTermAtT_mul, IsSplitLevel.LiftLaw.u₀_charDatum_eq_fourierOp,
  Grading.IsAdaptedAt.gram_string_entry): the line census ends the statement at the `:=` of the `let`, so the rest
  of the statement counts as proof text; it stands in `intro_lines` of the proofs (the last one is triaged
  computation). The `text` gives the whole statement.
- **Exempt lemmas with proofs longer than one line** (12): IsAdmissibleComb.of_sum, .single, .map, .smul,
  localLevel_le_integralAbove_of_coprime, Data.charUnramifiedAt_rankTwist_of_N_mem, IsSplitLevel.reduction_eq_iff,
  Data.isConjKernelPair_gridKernel (one-step: a single citation or term), Parameters.norm_finMultiplier_eq_one
  (automation), Grading.IsAdaptedAt.gram_string_entry, Data.lastColDatum_conj_ne_zero_iff,
  IsSplitLevel.lastRowDatum_conj_u₀ (computation: unfolding and entrywise algebra). Each text says what the
  computation is.
- **The signature rule in the words.** Functions of the data that take D explicitly are written `D.name(…)` (the
  generator adds `D.` from the census binders; HasLogBound, HasLogLower and chosen by hand). Values of the data
  are still written as bare letters (N, m, ϱ, π, π_g, M_ω, ω, χ, 𝒫, X_j, Y_j, e₀, …); `unit.json` →
  `notes.letters` gives the Lean term of each (all are definitions of `IndexTypes` or fields, D explicit).
  MEMORY.md's full forms are binding for notes ("everything attached to the data is written as a function of D"),
  so a note must expand them (N(D), m(D), 𝒫_D, …). I did not do this in the dossier: an automatic rewrite cannot
  tell D.N from a bound N (the split-level files have their own N, π, E, n).
- **Instances and definitions with proofs inside** are not held to the structured-proof rule by the check. By
  judgment: `Data.hasLogBound_varpi` (9 lines) and `Data.hasLogBound_rootDisc` (4 lines) are triaged computation
  (simp and grind over the norms of ϖ, product formula for the root discriminant); the other instances are one line
  or a `simpa using` citation. Definitions are triaged `assembly`.
- **Members not used by the seesaw argument.** By name, every member is referenced somewhere in the sources except
  six that act implicitly (instances `Data.instNonemptyY`, `Data.hasLogBound_rootDisc`, `instFintypeYT`; simp
  lemmas `Data.piG_ne_zero`, `residueOverN_apply`, `scalarFin_atPlace`). Many members are used only outside this
  folder: by `Columns` (the Gauss-sum operator: compUpTo_pairs_eq_smul, translateSum_eq_sum_name,
  exists_indexDvd_fourierOp_pow, …), by `Exchange` (grid spaces, gridChar_det, levelIndex_eq_untwisted,
  exists_branching_pairing, entrySign, card_parabolic_blockNumber, …), by `Rows` (iotaAtLevel, iota_principalRep,
  liftTamePart_eq_of_mem_Q, …). Whether the root `Main` reaches each member needs the kernel export, which I did
  not have; nothing is put out of scope.
- Unused hypotheses: not determined (no Lean).

## Second reading
Suggested sample: every step of `Data.seesaw`, `Data.exists_isAdmissibleComb_unfolding` and `Data.exists_stage_cut`,
and every tenth leaf of the other proofs; then the risky proofs listed above.

## How the dossier is made
`gen/gen.py` (run from the workspace: `python3 reading/units/141/gen/gen.py`) reads the census, the proposal and the
pinned source, and the hand-written readings `gen/m_<File>.py` (texts, binder readings, triage, proof trees with
line or anchored-span locations), `gen/common.py` (shared readings, span helpers) and `gen/meta.py`; it writes
`unit.json` and `proofs/*.json` with lines, hashes, quotations, spans and typed facts. `gen/scan.py` lists typed
sites and branch keywords (a planning aid). The generator shares no code with `tools/rb.py`; the check is
independent.
