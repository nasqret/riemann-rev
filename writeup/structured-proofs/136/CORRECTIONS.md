# Corrections to the dossier of 136 (Lifting crystalline extension classes in large weight: Kisin modules with exponents, cokernel killers and cup products that vanish up to a power of p)

## 2026-11-26 — statement-boundary overlay (a second-reader message)

Source: the second reader's a second-reader message (`exchange/to-claude/a second-reader message/statement-range-inventory.json`, sha256 1749e406…). The census ends a statement at its first top-level `:=`; in the members below that `:=` belongs to a `let`/`letI`/`have` inside the type (or, where said, the census runs into an equation-style proof), so the census's statement lines stopped before the conclusion. Each declaration was read in full at the pin and the overlay's span confirmed (it ends just before the declaration's own `:=`). Applied by the generator: the chunk generator `136-a/gen/build.py` (before unit.json is written; chunk 136-b has no affected member or import, so it is unchanged), then `book/plan/merge_chunks.py 136`, calls `gen/statement_overlay.py`, which gives each listed member `statement_lines` (corrected), `statement_span` (span + SHA-256), `statement_lean_full` (the whole statement) and `statement_basis`, removes a truncated `statement_lean` (`rb.py check` compares `statement_lean` with the census's lines and refuses a longer quotation), and extends the quoted lines of imports to the end of their statements.

### Members (statement lines census → corrected; conclusion old → new)

- `Lift.KummerChart.PairingSide.wittPairing_constantAt_and_thirdPairing` (New.Lift.LongGap:229:7; assignment inside type): lines 229–230 → 229–234. Chunk 136-a. Already carried `source_ranges` read from the text by the first reader (statement 229:1–234:6, value from `⟨diagTensor_induction`), which agree with the overlay. Text already complete: with B = wittPairing(lsmul): (1) B(constantAt(thirdSide P, i)(1), w) = letterProj(S, i)(w) and (2) the identity for the third pairing → unchanged; its `note` now gives both the census lines and the whole statement's lines.
- `Lift.KummerChart.JumpLattice.coeff_mem_constantsModE` (New.Lift.LongGap:430:7; assignment inside type): lines 430–434 → 430–435. Chunk 136-a. Already carried `source_ranges` (statement 430:1–435:92, value from `by`), which agree with the overlay. Text already complete: d = ∑_a w(tⁿ(s_a))v_a − f_n·c lies in constantsModE(L, l, A, i) and in withExponents(L, i, shiftedStd(l, u ↦ 0 if o(u) ≤ n else A)) → unchanged; `note` updated as above.

### Proof steps and summaries

- No step claim restated a truncated statement (both proofs start at the value given by `source_ranges`); unchanged.

### Imports re-quoted to the end of their statements

- `Lift.TateTwist.smallPart_spec` (unit 82): lines 100–101 → 100–103. Chunk 136-a; quote_sha256 recomputed by the generator. Text already complete (p^m kills M, φ − 1 onto, φd − d ∈ S ⇒ d ∈ ℤ/p^m(1) + S, S ∩ ℤ/p^m(1) = 0, and L(hv − v) ∈ S for h near 1, S = smallPart(m) from the `let`); unchanged.

### Not applied

- Nothing: every overlay span of this dossier was confirmed by reading the source.

### Digests and check

- dossier digest (`dossier_sha256`): old `a8893db5f9986a61b959b126449820c9e23b8b1f994bbc0bd4b02e067bdb9884` → new `8f098a961fe45f5f09fd27a383a255a613e95336375dc5601ff89ad555e1a5d4`
- `python3 tools/rb.py check 136`: exit 0 — unit 136: 141 of 141 statements at their lines; 69 structured proofs, 430 steps, 375 leaves (longest 8 lines, bound 8), 430 steps quote their lines; typed facts in the source: 34 of 34; imports quoted: 146 of 146; arguments accounted for: 1408 of 1408


- chunk digests: 136-a old `4feb3a852f8880f5bb1d25ea8be1b6ca9840f079f9e4547dffe7f45d42f729cc` → new `424f4f2720784b6d8b4cc8ef51bda64879b42032a92f268d597754494739fb64`; 136-b unchanged `dccd5a2baff1612de4be3053030ba3d0501475c2ce79922b340402ef759c58ae`. `python3 tools/rb.py check 136-a`: exit 0.

## 2026-11-26 — the second reading (a second-reader message), the three early corrections (a second-reader message), literature verdicts

Correction reader: a Claude agent (Opus 5.5), the only writer of 136, 136-a and 136-b during this pass. Messages applied: a second-reader message (Kisin exponents: all 141 member texts, all 69 proofs sampled), a second-reader message (three corrections before the Kisin-exponent chapter), and the `by_name` statement-strength records of a second-reader message, 0008, 0011, 0012, 0017, 0019, 0024, 0032 for the imports of this unit. Every correction was read against the pinned source (`lsernau/grh-lean` @ `72fead1`, `grh-compact/src`) before it was applied; Mathlib facts were read at the artifact's pin `56a00585` (files fetched from raw.githubusercontent.com, hashes in the records). Changes were made in the chunk generators (`136-a/gen/content_*.py`, `136-b/gen/content_*.py`; new `gen/make_literature.py`, `gen/attach_literature.py`, `gen/content_zambient.py`; a hook in each `gen/build.py`), the chunks were emitted again and checked, and the unit was merged with `book/plan/merge_chunks.py 136`.

### Changes (old → new)

ExponentTheorems (136-b):
1. `universalSide`, `mem_cupOrthogonal_of_scaledCupBounds` texts (a second-reader message §1, a second-reader message #2): "a filter F containing Γ' (hF)" → every member of F contains Γ' (hF: 𝓟(Γ') ≤ F, `map k.Γ'.subtype ⊤ ≤ F`, lines 33–34); Γ' ∈ F is not required (F = ⊤ allowed). The second text also states what p^e·x ∈ cupOrthogonal(Q, L) means.
2. Import `Lift.cupOrthogonal` (a second-reader message §1): a one-line summary → the definition (GaloisLattices.lean 49–75): the pairing P = (m, ψ, λ, c₃) with p^m·c₃(g) = gψ − ψ; CupBounds asks for a continuous primitive with values in Q̄_p^× (the cochain lies in μ_{p^m}, the primitive need not).
3. `few_low_jumps` text: + relLength(S, T) = O-length of S/(S ∩ T); conclusion (2) does not assume the alternative of (1). Step 2: "as length_O(O/pO) is positive and finite, bound the length over Z_p" → multiply by length_{Z_p}(k_O) = [k_O : F_p] (length_restrictScalars). Step 4: "length(O/pO) = dim_{F_p}(O/pO)" → length_O(O/pO)·[k_O : F_p] = length_{Z_p}(O/pO) = dim_{F_p}(O/pO) = rank_{Z_p}(O) (a second-reader message §2, lines 78–87).
4. `tame_types_exponent` summary and step 8 (a second-reader message §3, a second-reader message #1): "d = differentExp = 0 as p ∤ e" → d = 0 if e = 1, d = v_p(e) + 1 = 1 otherwise (KummerChartExists.lean 161–162); κ = r²(N+1)² (hp is passed as the hypothesis n + κ + 2 < p of killsCokernel_of_isKilledBy); 3(κ + (48(η+W) + 4)d) ≤ 3κ + 150(η+W+1) for d ≤ 1.
5. `tame_types_exponent` steps 6.3–6.4 and summary (a second-reader message §3, lines 122–130): "inertia acts through its tame quotient … β_{s,0} is a power of β at the tame generator" → the stabilizer clause (`.1`, TameInertia.lean 79–81) of tame_inertia applied to s ↦ β_{s,0} (a character with open kernel and order dividing e): it is trivial on the stabilizer of ϖ, which contains the inertia of Γ' (d.apply_varpi).

FewLowJumps (136-b):
6. Texts of `relLength_deepConstants_le`, `exists_relLength_deepConstants_le`, `exists_scaledCupBounds_few_low_jumps`: "with hn and hr" / "with ha, hb, hs, hU, hn, hr" → the hypotheses written out (lines 25–29: f·Σ_{u∈[−η,η]} mult ≤ n(j), f·Σ_{u∈U_j} mult ≤ r(j) at every letter; ha, hb, hs, hU); "for every v" → "for every integer v"; only the last lemma assumes η ≥ 1 (the residue degree is f_k in the first text, whose hypothesis is named f).
7. `relLength_deepConstants_le` steps 6.2.2.18–21 (a second-reader message, lines 84–93): the kernel element n = r'Y₀ − (A(X) − X) with Y₀ = E^{−p^a}A(W₀); the identity p(X − n) = A(pX − W₀) + φ^a(E)Y₀ (plus sign, add_mem); "p ∤ φ^aE" → no φ^b(E) divides p (not_frobE_dvd_p).

SparseThickLetters (136-b):
8. `aeval_linearFrob_extLattice_eq_zero` step 1.2 and summary: "(q(X − 1))(β)y" → the product q·(X − 1): q(β)(β − 1)y.
9. `exists_tameChart` steps 9, 10.1 and summary (lines 139–153): "U normal (both conditions are invariant under conjugation)" → c ∈ U fixes μ_N and ϖ, hence every g⁻¹ϖ ∈ μ_N·ϖ (the stabilizer of ϖ alone need not be normal); "Γ/Γ' has exponent dividing N" → g^f has trivial character mod N and (g^f)^N ∈ U (step 8 needs g in the kernel), so the exponent divides f·N, prime to p (`hp.out.not_dvd_mul hf n`); e | N.
10. `scaledCupBounds_sparse_thick` steps 5–6 and summary (lines 266–270): "a thick letter can occur only at one place" → for 0 ≤ a < n with T: a = 0 or a + J + 1 = n, both possible (J = 1, n = 3, offsets 0 and 1); "either no thick letter occurs (t = 0) or the long-gap alternative" → either every a < n passes the sign/width test against t = 0 (constant signs pass it even with thick letters) or a failing a > 0 gives t with t + J + 1 = n and the long-gap alternative.
11. Texts of `killsCokernel_at_cut` and `scaledCupBounds_of_cut_windows` ("as in the setting with hX, …" / "in the sparse-thick-letters setting (…)") → all hypotheses written out (lines 164–178, 196–205: hX, hκ, hδ, h₈, hs, hy, hK, hz; for the second also hW, hU of width V, hη); `scaledCupBounds_sparse_thick`, `scaledCupBounds_two_sizes`: "opposite windows (hU)" → the windows of width V written out.

ExponentLattices, HodgeExpansion, CupProductBound, CokernelKillers, LongGap (136-a):
12. `exists_depth_step` steps 9–11, 11.1 (a second-reader message, lines 56–64): θ(Δ) in the first-order term (which is 0) → E is cancelled before θ: ω·γ(G) = G + F'(z)τuG_a z + rE(…)², then θ(G)(θ(ω) − 1) = p^a·θ(F'(z))·θ(τuz) (θ(G_a) = p^a); step 11 → p^{a+d}θ(τ)θ(z) | p^{d+3a}·θφ^{−a}(zτ). Step 8 (own reading of line 50): "p^{d+3a}·θ(zτ)" → "p^{d+3a}·θφ^{−a}(zτ)". Step 1 (own reading, Mathlib quote): "(θ(τ) + 1)^p = θ(τ)^p + 1 + p·t" → "+ p·θ(τ)·t" (exists_add_pow_prime_eq: (x+y)^p = x^p + y^p + p·x·y·r).
13. `valueAt_mem_valueField` summary, steps 3, 3.1, 4 (lines 203–214): "φ^{−a}λ_i(t_l)", coordinate of r·τ^h → apply φ^a first, then λ_i: D = φ^{−a}(λ_i(φ^a(τ^h r))), numerator φ^{−a}(λ_i(φ^a t_l))·μ(v_l); the sign of the moved coefficient.
14. `mem_withExponents_of_deep` step 2: "if lo > 0 then … positive index" → the case split on m = improvedExponent: m ≤ 0 (c ∈ B_dR^+), m > 0 ⇒ lo > 0 and hi > 0 ⇒ c = 0.
15. `exists_reaches_depth_succ` summary, 1.1.2, 1.1.4, 1.2 (lines 55–74): "Galois differences of 𝒦_a lying in hodgeFil(m) lie in hodgeFil(m+1)" → for the particular t of exists_depth_step (hypothesis p_a | ts − s): with D = φ^{−a}(p_a), B = D^{−n}(V − c), t(V − c) − (V − c) = (ω'^n − 1)(V − c) + ω'^nD^n(tB − B), tB − B ∈ hodgeFil(1) (from 0 to 1 only).
16. `mem_hodgeFil_of_hodge_basis` summary, steps 2–5 (a second-reader message, a second-reader message #3, lines 107–118): "the rows of A" → row m of A⁻¹ (A.2); D_m(μ) = (basisValues(μ)·A)_m; reconstruction by A⁻¹ (rows of A twice would give A²).
17. `mem_withExponents_stdExponent_iff` summary and step 4 (lines 150–170): "x' lies in the saturation" → φ^l x' lies in the φ^l(τ)-saturation; line 170 untwists.
18. `of_isSafe` steps 9, 9.4 (lines 110–119): "ζ_m commutes with multiplication by the index" → two annihilators: [Γ:Γ']·x = 0 (restriction/corestriction) and p^m·x = 0 (nsmul_zmodPowToUnits, new import), coprime (nsmul_eq_zero_iff_of_coprime).
19. `isSafe_sum` step 1.1: "the pairing is O-bilinear" → Z_p-bilinear and O-balanced (O-bilinear ψ then Z_p-linear λ).
20. `exists_extend_form` summary, steps 8, 10 (lines 109–120): "ν on C by c ↦ Λ(v_c) − a_c" → ν on a Z_p-basis e_j, extended linearly; invariance by expanding c in the basis (the chosen v_c, a_c are not linear in c).
21. `exists_reaches_deep` steps 1, 1.2: "in increasing order / larger than the second coordinates" → induction_on_max_value: n ≥ every second coordinate, ties allowed.
22. `scaledCupBounds_of_killsCokernel` steps 3, 5, 6 (lines 331–350): "a point over p^κc'" → over p^{κ+(8·6(a+η+W)+4)d}c' after deepening; the cost counted three times in hH; the opposing signs and the third pairing named.
23. `exists_z_pow_mem_liftIdeal` step 2 (lines 178–188): + the factorial condition v_p(M!) ≤ v_p((pa')!) of mem_liftIdeal_zero_of_mem_one, with equality (the < p factors in (pa', M] are prime to p).
24. Import `BdR.exists_sub_mem_of_smul_sub_mem`: "t^mB_dR^+" → any B_dR^+-submodule S (DeRhamFiltration.lean 60–61; Γ over G_p with open image).
25. Seal envelopes (a second-reader message §coverage): `note` on `cost` (line 26), `smul_sub_mem_zTau_kisinLocAinf` (188; also step 1.2), `frobExponent` (98), `raiseExponent` (361): the trailing `seal` line is a separate command in the census range.
26. `exists_comb_of_jumpMultiplicity_le` step 4: `exists_auerbach` was an `ambient_uses` entry, but it is a lemma of the artifact (CommonEigenvectors.lean 19) → `uses` and a new import with its statement.
27. `ambient_inputs` (a second-reader message noted it empty): the 12 Mathlib facts named in `ambient_uses` are now quoted at the pin `56a00585` (`gen/content_zambient.py`), with file hashes; and `IsLocalRing.length_restrictScalars` (LocalRing/Length.lean 54–55: ℓ_A(M) = ℓ_B(M)·[κ(B) : κ(A)]), which steps 2 and 4 of `few_low_jumps` use without naming it before, is added to their `ambient_uses` and quoted (13 in all).
28. Literature (`literature` records, `gen/literature.json`): BdR.exists_sub_mem_of_smul_sub_mem, Lift.TateTwist.smallPart_spec, exists_auerbach (136-a); IsPotCrys.exists_hasJumps, IsPotCrys.isCrystalline_of_inertia_fixes (136-b). The Lean side of each record (file hash, quoted lines) was checked; texts end with "The relation to the literature is the second reader's (literature)."

### Not applied, and why

- Nothing contested: every item of a second-reader message and a second-reader message agrees with the pinned lines. Items of a second-reader message that confirm the dossier (the positivity hypotheses of isSafe_of_exponents/isSafe_smul_sub with −u−u'−1, NoMultipleNear with v_p(0) = 0, the table of sampled steps) needed no change.
- The step quotations that include a trailing `seal` line keep it (the census's ranges and the check require it); claims and notes say so.

### Digests and check

- dossier digest of 136: old `8f098a961fe45f5f09fd27a383a255a613e95336375dc5601ff89ad555e1a5d4` → new `97661ebe12eae50d8d53f621ce1ef102adf4b82a3fee3889fd5b3658b32abdc1`
- chunk 136-a: old `424f4f2720784b6d8b4cc8ef51bda64879b42032a92f268d597754494739fb64` → new `d298509e999e024117abec02a8a492f5cb13b7a052cf0223c0bac028bdf8021d`; 136-b: old `dccd5a2baff1612de4be3053030ba3d0501475c2ce79922b340402ef759c58ae` → new `07bbf3293a95ae076a6d58b7e3633c258b1036194a0aa3027d43740ac01ff4aa`
- `python3 tools/rb.py check 136`: exit 0 — 141 of 141 statements at their lines; 69 structured proofs, 430 steps, 375 leaves (longest 8 lines); typed facts 34 of 34; imports quoted 148 of 148; arguments accounted for 1408 of 1408. `check 136-a`, `check 136-b`: exit 0.

## 2026-11-26 (third pass) — the note writer's findings

Correction reader: a Claude agent (Opus 5.5), the only writer of 136 and its chunks during this pass. Applied: the two findings of the note writer, each read against the pinned source (`lsernau/grh-lean` @ `72fead1`, `grh-compact/src`) before it was written. The changes are exact replacements in the generated records of chunk 136-b, made by a new module `gen/pass3.py` (with `gen/fixlib.py`; applied fixes logged in `gen/pass3.log.json`), called by `gen/build.py` after the literature records; 136-a needed no change. 136-b was emitted again, checked, and the unit merged with `book/plan/merge_chunks.py 136`. Nothing was built.

### What was applied

- `exists_relLength_deepConstants_le` (summary): q·p is the least multiple of p that is at least b(i) + W + 2a (FewLowJumps.lean 130–131: `existsUnique_add_zsmul_mem_Ico` with q·p ∈ [b(i) + W + 2a, b(i) + W + 2a + p)), not a Euclidean quotient, which rounds down.
- `Lift.KummerChart.universalSide` (arguments): the section hypothesis hF : map k.Γ'.subtype ⊤ ≤ F (ExponentTheorems.lean 31), which the census omits, is an explicit argument between ζ and h — the uses `k.universalSide ζ hF (hc Y a)` and `k.universalSide ζ hF hL` (lines 57–58) pass it — so the list is now hand-derived (`binders_basis` "lean", `binders_lean` saying that Lean was not asked, `binders_derivation`), with hF added after F. The text already wrote universalSide(k, ζ, hF, h).

### Changes (old → new)

#### Chunk 136-b (5 recorded fixes; `gen/pass3.py`, log `gen/pass3.log.json`)
- `Lift.KummerChart.PairingSide.exists_relLength_deepConstants_le` proof summary: “(q from the Euclidean division of b(i) + W + 2a by p)” → “(q·p the least multiple of p that is ≥ b(i) + W + 2a: b(i) + W + 2a ≤ q·p < b(i) + W + 2a + p, existsUnique_add_zsmul_mem_Ico — not the quotient of a Euclidean division, which rounds down)”. [writer: FewLowJumps.lean 130–131 (existsUnique_add_zsmul_mem_Ico p 0 (b i + W + 2a): q·p ∈ [b(i) + W + 2a, b(i) + W + 2a + p))]
- `Lift.KummerChart.universalSide` binders: + hF (explicit, map k.Γ'.subtype ⊤ ≤ F) at position 13. [writer: ExponentTheorems.lean 28–31 (section hypothesis (hF : map k.Γ'.subtype ⊤ ≤ F)), 50–52, 57–58 (`k.universalSide ζ hF (hc Y a)`)]
- `Lift.KummerChart.universalSide` binders_basis: set to “lean”. [writer]
- `Lift.KummerChart.universalSide` binders_lean: set to “NOT printed by Lean: nothing is built on this machine, so `#check @Lift.KummerChart.universalSide` was not run. The list is the census's text reading with the s…”. [writer]
- `Lift.KummerChart.universalSide` binders_derivation: set to “source-derived, not elaborator output: the section variables of New/Lift/ExponentTheorems.lean 28–31 end with (k) (ζ) (ho) {F} (hF : map k.Γ'.subtype ⊤ ≤ F); th…”. [writer]

### Not applied, and why

- Nothing contested.

### Digests and checks

- dossier digest of 136: old `97661ebe12eae50d8d53f621ce1ef102adf4b82a3fee3889fd5b3658b32abdc1` → new `be353f4efee4e4b2693285236b5782e4144fb6029f07bae9dff573f05a368d2a`
- chunks: 136-a unchanged `d298509e999e024117abec02a8a492f5cb13b7a052cf0223c0bac028bdf8021d`; 136-b `07bbf3293a95ae076a6d58b7e3633c258b1036194a0aa3027d43740ac01ff4aa` → `7b4f46c93c61ff50465fdfac31b3479d89171ef0ff43eddd8e16549719a3fd9d`
- `python3 tools/rb.py check 136`: exit 0 — 141 of 141 statements at their lines; 69 structured proofs, 430 steps, 375 leaves (longest 8 lines, bound 8); typed facts 34 of 34; imports quoted 148 of 148; arguments accounted for 1409 of 1409 (1 member by Lean's own signature, which this check cannot confirm: universalSide). `check 136-a`, `136-b`: exit 0.

Cost: about 75 minutes of wall time for the five units 148, 132, 138, 136 and 147 together (about 09:20Z–10:35Z by the clock, the start estimated from the first backup at 09:47Z and the reading before it), shared among them; tokens not reported by the client.

## 2026-11-26 — Pass 8: a second-reader message and a second-reader message, and the rounding in step 5.2

Correction reader: a Claude agent (Opus 5.5), the only writer of 136 and 136-b during this pass (136-a untouched). Messages: the second reader's a second-reader message (tame ramification and change of coefficient ring, verified on `97661ebe…`) and a second-reader message (the upward multiple and both explicit filter arguments, verified on `be353f4e…`, the present dossier). Each item was read against the pin (`grh-compact/src` at `72fead10`); nothing was built. The change is an exact replacement made by a new module `136-b/gen/pass8.py` (with `gen/fixlib.py`; log `gen/pass8.log.json`), called by `gen/build.py` after `gen/pass3.py`; 136-b was emitted again, checked, and the unit merged with `book/plan/merge_chunks.py 136`.

### Applied (old → new)

1. `Lift.KummerChart.PairingSide.exists_relLength_deepConstants_le`, step 5.2 (chunk 136-b; FewLowJumps.lean 130–131: `obtain ⟨q, h₀, -⟩ := existsUnique_add_zsmul_mem_Ico (natCast_pos.2 p.pos_of_neZero) 0 (b i + W + 2 * a)`, i.e. 0 + q • p ∈ Ico (b i + W + 2a) (b i + W + 2a + p) with q an integer; `(q * p).toNat` at line 140): “ε(i) ≠ 1: write b(i) + W + 2a = qp + ρ with 0 ≤ ρ < p;” → “ε(i) ≠ 1: take the integer q with b(i) + W + 2a ≤ qp < b(i) + W + 2a + p, i.e. qp is the least multiple of p that is ≥ b(i) + W + 2a (existsUnique_add_zsmul_mem_Ico; not the quotient of a Euclidean division, which rounds down);”. From a second-reader message, which verified that the dossier places qp in [b(i) + W + 2a, b(i) + W + 2a + p): pass 6 had corrected the proof summary only, and the head of step 5.2 still gave the Euclidean division (qp ≤ b(i) + W + 2a), against the summary and the source.

### Verified and already present

- a second-reader message, `differentExp` (Lib/PadicHodge/WachKisin/KummerChartExists.lean 161–162: 0 if e = 1, else v_p(e) + 1, so 1 for a tame chart with e > 1): `tame_types_exponent` step 8 keeps the different term and checks both cases (ExponentTheorems.lean 131–139) — present.
- a second-reader message, the filter hypothesis hF : map k.Γ'.subtype ⊤ ≤ F (ExponentTheorems.lean 31–34: every member of F contains Γ'; F = ⊤ allowed), in the texts and binders of `universalSide` and `mem_cupOrthogonal_of_scaledCupBounds` — present.
- a second-reader message, `few_low_jumps` step 2: length over ℤ_p = length over O times [k_O : F_p] (length_restrictScalars; ExponentTheorems.lean 76–87) — present.
- a second-reader message, the proof summary of `exists_relLength_deepConstants_le` (the least multiple of p, pass 6) and hF as an explicit argument of `universalSide` between ζ and h (ExponentTheorems.lean 50–58, pass 6) — present.

### Not applied

- Nothing refused.

### Digests and checks

- dossier digest of 136: old `be353f4efee4e4b2693285236b5782e4144fb6029f07bae9dff573f05a368d2a` → new `ffdfbaf551389850ccc939610049ae523c3f7497fdc49628eca7b127d11d4a69`
- chunks: 136-a unchanged `d298509e999e024117abec02a8a492f5cb13b7a052cf0223c0bac028bdf8021d`; 136-b `7b4f46c93c61ff50465fdfac31b3479d89171ef0ff43eddd8e16549719a3fd9d` → `5b18071f48d2aec7f3c733192f7bccf21bb0ea933aff2b40ad9bd8717beafc6f`
- `python3 tools/rb.py check 136-b`, `check 136` (after the merge): exit 0 — 141 of 141 statements at their lines; 69 structured proofs, 430 steps, 375 leaves (longest 8 lines, bound 8); typed facts 34 of 34; imports quoted 148 of 148; arguments accounted for 1409 of 1409 (1 member by Lean's own signature, which this check cannot confirm: universalSide). `check 136-a`: exit 0.

Cost: about 25 minutes of wall time for the nine units of pass 8 together (about 15:45Z–16:10Z by `date -u`, the start estimated from the first backup at 15:51Z), shared among them; tokens not reported by the client.
