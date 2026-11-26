# Corrections to the dossier of 145 (Columns and the chain of theta lifts: levels and branching on the spaces X_j, short ramified columns, divisibility of the chain at each prime (marked primes and scaled Hecke operators), and size bounds)

## 2026-11-26 — statement-boundary overlay (a second-reader message)

Source: the second reader's a second-reader message (`exchange/to-claude/a second-reader message/statement-range-inventory.json`, sha256 1749e406…). The census ends a statement at its first top-level `:=`; in the members below that `:=` belongs to a `let`/`letI`/`have` inside the type (or, where said, the census runs into an equation-style proof), so the census's statement lines stopped before the conclusion. Each declaration was read in full at the pin and the overlay's span confirmed (it ends just before the declaration's own `:=`). Applied by the generator: `gen/gen.py` (after the records are built) calls `gen/statement_overlay.py`, which gives each listed member `statement_lines` (corrected), `statement_span` (span + SHA-256), `statement_lean_full` (the whole statement) and `statement_basis`, removes a truncated `statement_lean` (`rb.py check` compares `statement_lean` with the census's lines and refuses a longer quotation), and extends the quoted lines of imports to the end of their statements.

### Members (statement lines census → corrected; conclusion old → new)

- `Data.IsGoodDatum.exists_hecke_transfer` (New.Columns.LocalStatement:50:7; assignment inside type): lines 50–52 → 50–55. Old quotation stopped at `let C := …;` (line 52). Text already complete: there are c with c_i ∈ O_ι for j < m such that for every x ∈ supp Ψ, with C = chain(liftKernel ϑ)(translateDatum x)(j+1): (a) target-sphericity at l and (b) ∑_{i≤𝔯} c_i T_{l,i}(Cφ) = p^{δ_p} C(T_{l,𝔯}φ) → same, now with 𝔯 = ceilLogM(D, p) and T_{l,i} = heckeSplit(hw, i) named.
- `Data.IsGoodDatum.exists_move_markOperator` (New.Columns.LocalStatement:148:7; assignment inside type): lines 148–149 → 148–155. Old quotation stopped at `let Φ := t (translateDatum x` (line 149). Text already complete ((a) equivariance of t, (b) the lift identity with ∏_L markOperator, (c) the raise bound p^{∑_L(δ_p − A_l) + ∑_Λ A_l + liftLoss(Λ, j)}) → same, with the order of the hypotheses of (c) as in Lean (j < m, then the condition on g) and A_l, δ_p, 𝔯 named.

### Proof steps and summaries

- Data_IsGoodDatum_exists_hecke_transfer.json step 1 and Data_IsGoodDatum_exists_move_markOperator.json step 1 (kind statement, owning the tails 52–55 and 149–155): claims now begin "Not a step of the proof: lines … are the rest of the statement" and say what they state; they stay, because the line census still takes the `let`'s `:=` for the start of the value.

### Imports re-quoted to the end of their statements

- `Parameters.mem_raises_of_jet_bound` (unit 150): lines 121–125 → 121–126. Text was a one-line summary ("Gauge bound for ω(1, xdy)Ψ from a jet bound"); now the full statement (kernel k from the `let`, hypotheses hΦ, hx, hy, hu, h; conclusion k.ω(1, x·d·y)Ψ ∈ raises(k, 1, 1, B)).
- `norm_schurJet_le` (unit 150): lines 65–69 → 65–71. Text was "Divisibility of Schur jets"; now the full statement (N, B, m from the `let`s; IsIntegralOnNullCone(…) → |schurJet_κ(Θ)_{i′,i}| ≤ p^{m − (…)}).
- `Parameters.norm_jet_le_of_isAdmissibleComb` (unit 143): lines 47–50 → 47–59. Text was "Archimedean bound for jets of admissible combinations"; now the full statement (u, M, F from the `let`s; the jet bound (i) and the operator bound (ii) for schurJet).

### Not applied

- Nothing: every overlay span of this dossier was confirmed by reading the source.

### Digests and check

- dossier digest (`dossier_sha256`): old `044d4983db128d9a083ce89e046a4b7392d16561801bfbf0dc4bfe42b2d67805` → new `0de5384ddf99ea4c4cd62bb227aa8e9710d18de1f8ad488d61ac3ee2594a7390`
- `python3 tools/rb.py check 145`: exit 0 — unit 145: 105 of 105 statements at their lines; 46 structured proofs, 350 steps, 331 leaves (longest 8 lines, bound 8), 350 steps quote their lines; typed facts in the source: 43 of 43; imports quoted: 44 of 44; arguments accounted for: 746 of 746


## 2026-11-26 — faults found by the writer of the notes (coordinator's message, checked against the Lean)

- `Data.jetExponent`: the text wrote the sum as ∑_{e ≤ log_p N, e odd or p = d}, which the writer read as omitting e = 0 for p = d. Lean has `∑ e ≤ p.log N with Odd e ∨ p = P.d` (New/Columns/JetExponentBound.lean:115–118), a sum over 0 ≤ e ≤ ⌊log_p N⌋; the text now says that for p = d every e from 0 to ⌊log_p N⌋ is summed, e = 0 included (and names ρ_p, f, κ).
- `Data.mem_integralAfter`: one data argument, D′ (section variable `(D' : Data P)`, New/Columns/ChainValuation.lean:259); the census also lists the section variables w and D. Their binder readings already said "NOT an argument"; the `binders_remark` ("D likely not used") is now definite, with the reason (the implicit data of `admissibleTranslations q` is assigned D′ by unification) and the three uses `D.mem_integralAfter ht …` that pass one data argument.
- Phantom census argument w in `Data.ramifyingOp`: its binder reading already said "NOT an argument of the Lean declaration (by the source)"; unchanged.

- dossier digest: `0de5384ddf99ea4c4cd62bb227aa8e9710d18de1f8ad488d61ac3ee2594a7390` (after the overlay) → `b73f5c4b3efa9df70887f1015f06b7743698cc5c28d612a64cf70589a488fb45`
- `python3 tools/rb.py check 145`: exit 0 — unit 145: 105 of 105 statements at their lines; 46 structured proofs, 350 steps, 331 leaves (longest 8 lines, bound 8), 350 steps quote their lines; typed facts in the source: 43 of 43; imports quoted: 44 of 44; arguments accounted for: 746 of 746



## 2026-11-26 — second reading (a second-reader message)

Correction reader: a Claude agent (Opus 5.5), the only writer of this folder for this pass. Every correction was checked
against the pinned source (`lsernau/grh-lean` @ `72fead1`, `grh-compact/src`) before it was applied; nothing was built.
The changes were made in the generator's inputs (`gen/spec_*.py`) and the dossier was emitted again with
`python3 reading/units/145/gen/gen.py`. No import of 145 has a `by_name` statement-strength row (a second-reader message, 0011, 0012,
0017, 0019, 0024, 0032, matched by declaration id), so no `literature` record was added. Nothing was contested.

### a second-reader message #1, the translation denominator (ChainValuation.lean 267–269; IndexTypes.lean 37)
- `Data.admissibleTranslations` text: "every t_k lies in translations(q, π̄_G): π̄_G·t_k is integral at every place not
  dividing q" → translations(q, conj(π̄_G)) (Lean `translations _ q (star D.piGBar)`; `Data.piGBar` is already the
  conjugate of π_G, so the weight is π_G): every entry of π_G·t_k is integral at every finite place not dividing q, and
  t_k itself is integral there unless w̄ is chosen.
- `Data.mem_integralAfter` proof summary: "π̄_G·x_j is integral at w; … or π̄_G is a unit at w" → π_G·x_j is integral
  at w (weight conj(π̄_G) = π_G); δ = π_G, or π_G is a unit at w (w̄ not chosen). Steps 1–2 already had π_G; the estimate
  of lines 288–292 (case δ = π_G) uses the condition directly, as the second reader says.

### a second-reader message #2, the index bound (`IndexDvd`, New/Core/ModuleIndex.lean 17–20 and 52–56; LocalStatement.lean 285–307)
- `Data.exists_indexDvd_Bmu_divisible` text: "IndexDvd(integralColumns, S, p^l) (every finite family in the integral
  columns has an integral combination with determinant dividing p^l lying in S) … p^{−β}·B_μφ is integral at every point"
  → one l ≤ err(p)·dim Column and one O_ι-submodule S such that for every finite family v_1, …, v_n of integral columns
  a square n×n matrix A over O_ι with det A ∣ p^l has every row combination ∑_k A_{ik}v_k in S (not a cardinality of a
  quotient), and for every twist ϑ, every good Ψ for ϑ with p prime to levelNorm(ϑ) and every ramified φ ∈ S:
  p^{−β}·B_μ(ϑ, Ψ)(φ) ∈ integralFormsAt(⊤, 1) (gauge ≤ 1 at every point); the same l and S serve all ϑ, Ψ, φ.
- `Data.IsMarked.hasType_prod_markOperator_pow`, `Data.IsMarked.hasType_markOperator`, `Columns.hasType_markOperator`
  texts: "[M : Y·M + p^s·M] divides p^c" / "the index of markOperator(M) + p^s·M in M divides p^c" → Y maps M into M and
  IndexDvd(M, Y·M + p^s·M, p^c) for a natural c below the bound, with the determinant meaning spelled out (the authors'
  doc comment's index notation noted).
- Proof of `Data.exists_indexDvd_Bmu_divisible`: summary "S = M (index 1)" → "(IndexDvd with l = 0)"; step 1 with
  B_μ(ϑ, Ψ)(φ) and integralFormsAt(⊤, 1); step 3.3 "a submodule of index dividing N^l, l ≤ 4mfb·dim, on which F^{ϱ+1}φ is
  integral at diagPointN 0" → e ≤ 4mfb·dim Column and IndexDvd(integral columns, S, N^e) for S the columns φ with
  F^{ϱ+1}φ ∈ integralFormsAt(Column, diagPointN 0); step 6.1 "[M : S] divides p^l" → IndexDvd(M, S, p^l).
- Import `Data.exists_indexDvd_fourierOp_pow` (unit 141, LiftCharacters.lean 128–131): "a submodule of the integral
  columns of index dividing N^l …" → the full statement (instance [PadicPlace N], optional split level, ∃ e ≤
  4·m·f·b·dim Column with IndexDvd(integralFormsAt(Column, 1), pull-back by F^{ϱ+1} of integralFormsAt(Column,
  diagPointN 0), N^e)), as the second reader also wrote in a second-reader message.
- Unit summary: "B_μ applied to a submodule of the integral columns of small index is divisible by the predicted power
  p^{gain(p) − err(p)}" → for each p and each integer β < g(p) − err(p) + 1 there are one l and one S (small index in the
  sense of `IndexDvd`) such that B_μ(ϑ, Ψ) maps the ramified columns of S to forms divisible by p^β (the quantifier order
  of the statement: β before l and S).

### a second-reader message #3, the domain of commutation (LocalStatement.lean 148–155)
- `Data.IsGoodDatum.exists_move_markOperator` text (a): "for all a and b ∈ K_f" → for every a in the whole finite adelic
  unitary group G_f(X_j) and every b in the maximal compact K_f of G_f(X_{j+1}) (Lean `∀ a, ∀ b ∈ Kf ..`; the kernel's ω
  acts on G_f(X_j) × G_f(X_{j+1}), BranchingPeriod.lean 47–48). `gaugeLe_chain`'s text already quantifies over the
  level groups only (ChainValuation.lean 324–327); unchanged.

### a second-reader message #4, the valuation convention (ChainValuation.lean 161–164; JetExponentBound.lean 94–99)
- `Data.mem_columnLevel` text: "… is ≤ e^{−1}" → ≤ exp(−1), the element of degree −1 of the value group ℤₘ₀ (not the real
  number e^{−1}): the entry has additive w-adic valuation ≥ 1 (last row ≡ (0, …, 0, 1) mod w).
- `Data.IsMarked.valuation_p` text: "the l-adic valuation of p is e^{−1}" → exp(−1) in ℤₘ₀: p has additive l-adic order
  one (a uniformizer at l).
- `Data.IsGoodDatum.exists_hecke_transfer` step 8.2: "(v_l(p) = e^{−1})" → the same convention.
- Same convention, not flagged by the second reader but the same Lean constant: `Data.isSplitLevel_piPlaces` text,
  "N has valuation e^{−1}" → exp(−1) ∈ ℤₘ₀, additive order one (IsSplitLevel.v_natCast, NamesAtSplitLevel.lean 28).

### The signature rule (with the second reader's form B_μ(ϑ, Ψ)φ)
- `Data.Bμ` takes ϑ and Ψ explicitly (CrudeModularData.lean 62). "B_μv", "B_μ(Y^m v)", "B_μφ" → B_μ(ϑ, Ψ)(v) etc. in the
  texts of `gaugeLe_markOperator_pow`, `gaugeLe_one`, `gaugeLe_Bmu_of_isMarked`, `gaugeLe_collisionSum`,
  `gaugeLe_pow_jetCeil_smul` (and its step 1), `exists_indexDvd_Bmu_divisible` (and its step 1), and
  `Data.gaugeLe_Bmu_at_N` step 3; `weylNormSq_Bmu_le`: B_μ(1, Ψ) (Lean `D.Bμ .one Ψ φ`, LocalStatement.lean 202).

### Not applied
- Nothing refused. The remarks of a second-reader message on the sampled arguments (central translation cost, shortness factor 4,
  class expansion, full marks, p = N, SizeEstimates 37–38) agree with the dossier; unchanged.

### Digests and check
- dossier digest (`dossier_sha256`): old `b73f5c4b3efa9df70887f1015f06b7743698cc5c28d612a64cf70589a488fb45` → new
  `415c29c6a95420d3e4c1eac9609c829edb452aa5051ab3f2400e0bc6554c40d8` (the second reader read the frozen
  `044d4983…`; the overlay and the writer's findings came in between, see above)
- `python3 tools/rb.py check 145`: exit 0 — unit 145: 105 of 105 statements at their lines; 46 structured proofs, 350
  steps, 331 leaves (longest 8 lines, bound 8), 350 steps quote their lines; typed facts in the source: 43 of 43;
  imports quoted: 44 of 44; arguments accounted for: 746 of 746

Cost: about 30 minutes of wall time for this pass on 145 and 133 together (after 08:15Z, the time of the last check
before it, to 08:45Z by `date -u`); tokens not reported by the client.

## 2026-11-26 — Pass 8: a second-reader message (verified; nothing to apply)

Correction reader: a Claude agent (Opus 5.5). the second reader's a second-reader message verified the revised dossier `415c29c6…`, which is still
the present one, and gave the statement it would use for Chapter V; it asks for no change. Each passage was re-read in
the present dossier and at the pin (`grh-compact/src` at `72fead10`):

- `Data.exists_indexDvd_Bmu_divisible` text: β < g(p) − allowedLoss(p) + 1 with g(p) = gain(p) at non-split primes and
  0 otherwise; one l ≤ allowedLoss(p)·dim Column and one submodule S; IndexDvd quantified over every finite family of
  integral columns, with one square A, det A ∣ p^l and the combination in S for every row i; the same l and S for every
  twist prime to p, every good Ψ and every ramified φ ∈ S (LocalStatement.lean 285–288; Core/ModuleIndex.lean 17–20) —
  present, as a second-reader message states it.
- `Data.admissibleTranslations`: every entry of π_G·t_k integral at the places not dividing q, the conjugation already
  inside piGBar (ChainValuation.lean 267–269; IndexTypes.lean 37) — present.
- `Data.IsGoodDatum.exists_move_markOperator`, clause (a): a in all of G_f, b ∈ K_f (LocalStatement.lean 148–151) —
  present.
- `Data.IsMarked.valuation_p`: exp(−1) in ℤₘ₀, additive order one (JetExponentBound.lean 96–97) — present.
- the two endgame calls (Endgame/ShortAndEnough.lean 149–156): evidence of use, no dossier change asked.

Dossier unchanged (`415c29c6a95420d3e4c1eac9609c829edb452aa5051ab3f2400e0bc6554c40d8`); `python3 tools/rb.py check 145`:
exit 0.
