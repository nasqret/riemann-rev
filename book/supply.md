---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# The arithmetic supply

```{code-cell} ipython3
:tags: [remove-cell]
import sys
sys.dont_write_bytecode = True
sys.path.insert(0, '_lib')
import bookdata as bd

m = bd.model()
fx = bd.facts()
expected = {11: 'The cohomological window', 12: 'Auxiliary primes and Behrend towers', 13: 'The Galois row',
            14: 'Seven inputs at the decisive call'}
assert {c['n']: c['title'] for c in bd.comps('arith')} == expected
# constants and examples quoted below
coh = bd.comp('cohomology')
assert 'x^{401}' in coh['statement'] and '\\sqrt{\\exp(x^{\\varepsilon})}' in coh['statement']
assert 'J=4(2B)^R' in coh['explanation'][1] and 'U/(2^{R+2}B^R)' in coh['explanation'][1]
ex = fx['windows']['example']
assert (ex['Ct'], ex['eta'], ex['B'], ex['X']) == (2, 1, 2, '2^128')
assert ex['twists'] == ['2^16', '2^180'] and ex['starts'] == [8.0, 90.0] and ex['interval'] == ['2^16', '2^32']
um = fx['windows']['ultrametric']
assert (um['ell'], um['Z'], um['center'], um['exceptional'], um['if_mod_27']) == (3, 80, 1, [1], [1, 28, 55])
be = fx['behrend']
assert (be['S'], be['d'], be['L'], be['norm'], be['base'], be['checks']) == (3, 3, 2, 5, 24, 1440)
pr = bd.comp('primes')
assert 'z=Y^{\\varepsilon/5}' in pr['explanation'][0]
assert 'q\\equiv3\\ (8)' in pr['statement'] and 'd\\equiv7\\ (16)' in pr['statement']
assert 'y^{1/2+\\varepsilon/2}' in pr['statement']
seven = bd.node('seven')['assumptions']
assert len(seven) == 7 and len(m['audit']) == 5
assert {a['node'] for a in m['audit']} >= {'row-prod', 'definite'}
bd.glue('n_seven_mod', len(bd.node('seven')['assumptions']))
gal = bd.comp('galois')
import re
bd.glue('behrend_checks', f"{be['checks']:,}")
bd.glue('behrend_enc', ', '.join(str(e) for e in be['encodings']))
```

```{code-cell} ipython3
:tags: [remove-input]
bd.show(f"{bd.stratum_badge('arith')} {bd.esc(bd.stratum('arith')['blurb'])}")
```

This stratum is where the deep arithmetic lives: Galois representations attached to automorphic
representations, theta correspondences, and a bound for Galois cohomology along cyclotomic towers
that the announcement describes as a weakening of Vandiver's conjecture. It is also where the two
premises of the second verified cut, `TopG` and `VWinAt ψ 401`, are produced. Most of it is, in the
imported record, **source-read** rather than separately replayed; the kernel-checked steps are
implications with explicit premises:

```{code-cell} ipython3
:tags: [remove-input]
# declarations of this stratum (component Lean lists and blueprint nodes) that a native scope checked
arith = set()
for c in bd.comps('arith'):
    arith |= {l['name'].split()[0] for l in c['lean']}
    arith |= {bd.node(n)['declaration'] for n in c['nodes'] if bd.node(n)['declaration']}
match = lambda name: any(name == a or name.endswith('.' + a) for a in arith)
rows = []
for sc in bd.scopes():
    if sc['lean_version'] == '4.35.0':
        continue
    hits = [d['name'] for d in sc['declarations'] if match(d['name'])]
    if hits:
        rows.append(f"* **{bd.esc(sc['title'])}** ({sc['original_project_module_count']:,} original modules): "
                    + ", ".join(f"`{h}`" for h in hits) + f". *Premises:* {bd.esc(sc['assumption'])} "
                    f"*Conclusion:* {bd.esc(sc['conclusion'])}")
assert rows
bd.show("\n".join(rows))
```

(comp-cohomology)=
## 11 · The cohomological window

```{code-cell} ipython3
:tags: [remove-input]
bd.show(bd.card('cohomology'))
```

### The quantity that is bounded

For a number field $E$ in a prescribed family, a prime $\ell$ and a twist $h$, let $s_{\ell,h}(E)$ be
the $\mathbf Z_\ell$-length of the locally trivial part of $H^1$ of $E$ with coefficients in
$\mathbf Q_\ell/\mathbf Z_\ell$ twisted by the $h$-th power of the inverse cyclotomic character (the
archive's `shaLen`). The predicate `VVle E t B` asks that all these lengths be **finite** for
$1\le h<t$ — a separate clause, because converting an extended natural number to a natural number
sends $\infty$ to $0$ in Lean — and that $\sum_{\ell\in S}\log\ell\sum_{1\le h<t}s_{\ell,h}(E)\le B$ for
every finite set of primes $S$. The window `VWinAt ψ 401` asks for this with $t=\lfloor x^{401}\rfloor$
and $B=\sqrt{\exp(x^{\varepsilon})}$, at **every** real $x$ of an interval $[Y,Y^2]$, uniformly over the
fields attached to $\psi$, the layer $e(x)$ and the auxiliary primes $q,d$. The bound is enormous;
what matters is that it is uniform, finite, and sub-exponential in the scale that the
estimate stratum can absorb.

### How many twists can be expensive

In one tower the relevant length is a cokernel length for a twisted operator, and an $\ell$-adic
determinant estimate supplies centres $s_1,\dots,s_{R'}$, the same for every twist $h$ and every
layer $m$, with

$$
\operatorname{twLen}(h,m)\le\sum_{i=1}^{R'}\big(\max(m,j_0)+c+v_\ell(s_i-h)\big).
$$

A twist $1\le h\le Z$ is *exceptional* if $|h-s_i|_\ell<\ell^{-k}$ for some $i$, where
$k=\lfloor\log_\ell Z\rfloor$. Each centre accounts for at most one exceptional twist: two of them would
satisfy $\ell^{k+1}\mid a-b$ with $0<|a-b|<Z<\ell^{k+1}$. So there are at most $R$ exceptions however
large $Z$ is — this integer core is proved in this repository's Lean file `Atlas/Separation.lean`
(see {ref}`lean-separation`). The strict inequality matters: for $\ell=3$, $Z=80$ and centre $1$ only
$h=1$ is exceptional, while with "$\le$" the twists $28$ and $55$ would also qualify
({doc}`windows`). The total count $R=R_0(M)+\sum_{\ell\in B'}R_\ell(L_\ell)$ is fixed before the
auxiliary primes are chosen; the rank bounds behind it use the archive's Ferrero–Washington
formulation.

### Why one interval survives

Put $\eta=\varepsilon/(2C_K)$, $u=\log x$, $a=(\log h)/C_t$ and $B=C_t/\eta$ with $C_t=401$. An exceptional
twist $h$ is harmless at $x$ if $h\le x^{C_t}\Rightarrow h\le x^{\eta}$, and this fails exactly for
$u\in[a,Ba)$. The real-variable lemma `UpperTheory.V.Win.window1` (kernel-checked) finds $[y,2y]$
inside $[0,U]$, $U=\log X$, missing all $R$ forbidden intervals, with $y\ge U/(2^{R+2}B^R)$: if no
start lies in $(U/2B,U]$ take $y=U/2$; otherwise delete one such start and recurse below
$U/2B$. Exponentiating gives $[Y,Y^2]\subset[X^{1/J},X]$ with $J=4(2B)^R$. In the computed example
($C_t=2$, $\eta=1$, $X=2^{128}$, exceptional twists $2^{16}$ and $2^{180}$) the induction deletes
the start $90$, lowers the ceiling from $128$ to $32$ and returns $[Y,Y^2]=[2^{16},2^{32}]$; a
randomized test of the lower bound is in {doc}`windows`.

On the surviving interval, unexceptional twists have valuations at most $\lfloor\log_\ell Z\rfloor$, and
each exceptional twist that is still active is small ($h\le x^{\eta}$) and is handled by a fixed-layer
estimate; the choice of $\eta$ keeps that secondary cost at $x^{O(\varepsilon)}$. The positive part,
the negative part and the prime $2$ are then evaluated on the same field at the same $x$, and an
elementary comparison absorbs their sum into $\sqrt{\exp(x^\varepsilon)}$.

### Where the bound itself comes from

The window is produced through the call `vwin_of_row` from the Galois row of {ref}`comp-galois`.
Along the way, tower estimates (for each prime $\ell$, lengths controlled away from finitely many
centres and in terms of a fixed layer) are combined into one record of constants valid for every
cutoff exponent, and counting cases I, II, III and V bound the lengths over arbitrary finite sets of
coefficient primes. One of the reading project's itineraries follows exactly this path; each step is
listed with its contract and tier (the premises of the checked steps — global Poitou–Tate duality,
local finiteness and local Tate duality, a Ferrero–Washington rank bound, a uniform exponent for a
reference layer — are among the source-read steps):

```{code-cell} ipython3
:tags: [remove-input]
its = m['itineraries']
best = max(its, key=lambda it: sum(bd.node(n)['component'] == 'cohomology' for n in it['nodes']))
assert sum(bd.node(n)['component'] == 'cohomology' for n in best['nodes']) >= 3
bd.show(f"**{bd.esc(best['title'])}.** " + bd.itinerary_md(best))
```

This is the precise place to compare the announcement's "weakening of Vandiver" with the
mathematics: the window bounds *sums of lengths*, for a selected family of fields and a bounded range
of twists. Positive finite lengths are compatible with it, and the announcement's further remarks
about individual $K$-groups would require additional theorems.

### What global duality supplies to the window

Global duality enters the window argument through two finite-level results: the last
arrow of the nine-term sequence and the perfect pairing of locally trivial classes
in degrees one and two. The passage to integral coefficients is carried out in
[the archive's length comparison](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/FoundationProofs/LengthEqLengthInvariantsOfTorsionLevels.lean#L517-L541).

Write $\chi$ for the cyclotomic character, $L=\mathbf Z_\ell(e+1)$
for the rank-one integral module of character $\chi^{e+1}$, and
$V=(\mathbf Q_\ell/\mathbf Z_\ell)(-e)$ for its torsion Tate dual (character $\chi^{-e}$).
Let $G_S$ be the restricted-ramification group of the number field $F$, where
$S$ consists of the places above $\ell$ (as in `LData`). Suppose that $\ell$ is
odd or $F$ is totally imaginary. At level $r\ge1$ the dual pair is
$L_r=L/\ell^r L$ and $V_r=V[\ell^r]$. Write $P^i(M)$ for the product of
local cohomology groups of a coefficient module $M$ at $S$, and $\Sha^i(M)$
for the kernel of localization in degree $i$. The nine-term sequence and
Sha duality give

$$
 \operatorname{coker}\big(H^2(G_S,L_r)\to P^2(L_r)\big)
 \simeq H^0(G_S,V_r)^*,
 \qquad \Sha^2(L_r)\simeq\Sha^1(V_r)^* .
$$

Here the star denotes the character dual into $\mathbf Q/\mathbf Z$. Reduction and an eventual
saturation argument relate the finite groups to the integral localization map
$f:H^2(G_S,L)\to P^2(L)$ and give

$$
 \operatorname{length}_{\mathbf Z_\ell}(\operatorname{coker} f)
 =\operatorname{length}_{\mathbf Z_\ell} H^0(G_S,V),
 \qquad
 \operatorname{length}_{\mathbf Z_\ell}(\ker f)
 =\operatorname{length}_{\mathbf Z_\ell}\Sha^1(V).
$$

The local equality is $\operatorname{length}H^2(F_v,L)=\operatorname{length}H^0(F_v,V)$.
All lengths are allowed to be infinite. The three identities are assembled in
[archimedeanSignatureMatching_of_poitouTate and twist_cohomology_inputs](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/FoundationProofs/LengthEqLengthInvariantsOfTorsionLevels.lean#L529-L541).
In the archive's [definitions](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/GaloisCohomology/Statement.lean#L67-L106),
the second equality identifies the length of the integral kernel with `shaLen`,
while `VLen` is the length of $H^2(G_S,L)$. Inclusion of the kernel gives

$$
 s_{\ell,e}(F)=\operatorname{length}\Sha^1(V)
 \le \operatorname{length}H^2(G_S,L).
$$

This is the inequality [shaLeV](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/AdditiveValuationNorms/ShaLeV.lean#L7-L16).
The two short exact sequences for $f$, together with the local length formula,
also give the additive balance

$$
 \operatorname{length}H^2(G_S,L)+\operatorname{length}H^0(G_S,V)
 =
 \operatorname{length}\Sha^1(V)+\sum_{v\in S}\operatorname{length}H^0(F_v,V).
$$

The additive form avoids subtracting infinite lengths. At the reference layer,
[aBound_of_descends](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/AdditiveValuationNorms/ABoundOfDescends.lean#L36-L55) uses this inequality: it identifies the tower
cokernel length with `shaInv`, bounds the reference-layer length by `VLen`,
and adds the growth allowance. The determinant and descent
estimates described above then control the exceptional twists. In the
[window assembly](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/HVCore.lean#L19-L22), the Poitou–Tate input
is used in the tower bound, the counting argument and the odd-prime reciprocity
calculation, through the normalized-duality adapter
[pt_s](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/HVFinalU.lean#L11-L11). The normalization and conjugation compatibility of that interface are separate
from the construction of the compact pairing below.

The first three notes below reconstruct the finite-coefficient theorem from its
arithmetic inputs; the fourth proves the length comparisons.

:::{dropdown} A closer look: the compact trace in Poitou–Tate duality

The construction of global duality begins with the trace on compactly supported
cohomology in degree three. It follows from local invariants, Brauer reciprocity
and the Kummer sequence for $S$-units.

Let $F$ be a number field, $\ell$ a prime, $n=\ell^k$ with $k\ge1$, and $S$ a finite set of finite
places containing all the places above $\ell$. Suppose $n$ is odd or $F$ is totally imaginary.
Write $F_S$ for the maximal extension unramified at finite places outside $S$,
$G_S=\operatorname{Gal}(F_S/F)$ and $D=\mu_n(F_S)$, with its natural Galois action.
All the $n$-th roots of unity lie in $F_S$. Let
$P^i(D)=\prod_{v\in S}H^i(F_v,D)$, where the local action is obtained by restriction.
The compact complex is the shifted cone of the finite-place localization map $f$.
Its degree-$i$ term is $C^i(G_S,D)\oplus\prod_{v\in S}C^{i-1}(F_v,D)$ and its
differential is $(a,b)\mapsto(da,f(a)-db)$. Fix an embedding of the algebraic
closure into a local algebraic closure for every place in $S$, so that restriction
is a specified cochain map. The local-to-compact map sends a local cocycle $b$
to $(0,b)$, and the compact-to-global map sends $(a,b)$ to $a$.
Its exact sequence contains

$$
H^2(G_S,D)\xrightarrow{\mathrm{res}}P^2(D)
 \xrightarrow{\partial}H_c^3(D)\longrightarrow H^3(G_S,D).
$$

All cohomology is continuous. Under the hypothesis on $n$ and $F$ the modified
archimedean Tate terms vanish. We normalize the local Brauer invariant using
arithmetic Frobenius and identify $\mathbf Z/n\mathbf Z$ with the $n$-torsion in $\mathbf Q/\mathbf Z$
by $a\mapsto a/n$. Denote the local invariant on $H^2(F_v,D)$ in this convention by $t_v$.

**Arithmetic inputs.** We use the vanishing $H^3(G_S,D)=0$ and the local invariant
isomorphisms $t_v$. The coefficient comparison with the local roots of unity is
an isomorphism since $S$ contains the places above $\ell$; no assumption that
$F$ itself contains the roots is needed here. The other input is the $S$-unit
comparison.

Put $U=\mathcal O_{F_S,S}^{\times}$ (the union of the $S$-unit groups in the finite
subextensions) and let $b:H^2(G_S,U)\to\bigoplus_w\operatorname{Br}(F_w)$ be the
map through the global Brauer group. The archive proves that on the $\ell$-primary
subgroup this map is an isomorphism onto the group of $\ell$-primary families
of local Brauer classes which vanish at finite places outside $S$ and whose invariant
sum is zero. The archimedean places are included in this comparison. The $S$-unit Kummer
sequence is exact: an $n$-th root of an $S$-unit is again an $S$-unit, and adjoining it is
unramified outside $S$ since $n$ is invertible there. Thus
$1\to D\to U\xrightarrow{(\cdot)^n}U\to1$ gives a map $H^2(G_S,D)\to H^2(G_S,U)$
with image $H^2(G_S,U)[n]$.

By the Albert–Brauer–Hasse–Noether exact sequence, localization identifies the global Brauer group with
the kernel of the sum of local invariants. A local family killed by a power of $\ell$ lifts
to a global Brauer class killed by the same power, by injectivity of localization. If the
family vanishes at finite places outside $S$, the archive's $S$-unit lifting theorem supplies
a preimage in $H^2(G_S,U)$. That group is torsion, so one can project a preimage onto its
$\ell$-primary component without changing its primary Brauer image. The separate primary injectivity theorem for $S$-units completes the comparison.

**Construction of the trace.** For a class $x\in H^2(G_S,D)$, its image in $H^2(G_S,U)$
is killed by $n$. By the primary comparison its local Brauer family vanishes at finite places outside $S$.
At a complex place the Brauer group is zero; at a real place it is killed by $2$, hence its
$n$-torsion is zero when $n$ is odd. Global Brauer reciprocity now gives
$\sum_{v\in S}t_v(\mathrm{res}_v x)=0$.
Thus $t=\sum_{v\in S}t_v$ vanishes on the image of restriction. Since
$H^3(G_S,D)=0$, the connecting map $\partial$ is onto, and exactness gives a unique
homomorphism $T:H_c^3(D)\to\mathbf Z/n\mathbf Z$ satisfying $T\partial=t$.

**Bijectivity.** Since $S$ contains the places above $\ell$, it is nonempty.
A class supported at one place with prescribed local invariant proves surjectivity.

For injectivity, take $\xi\in P^2(D)$ with $T(\partial\xi)=t(\xi)=0$.
Let $\beta$ be its family of local Brauer classes, extended by zero outside $S$. This is an $\ell$-primary family killed by $n$ with invariant sum zero.
The $S$-unit comparison gives an $\ell$-primary lift $y\in H^2(G_S,U)$ with $b(y)=\beta$.
Although the comparison gives only a primary lift, $b(ny)=n\beta=0$.
Since $ny$ is primary, injectivity gives $ny=0$.
Kummer exactness now lifts $y$ to $x\in H^2(G_S,D)$. By compatibility with localization,
$\mathrm{res}_v x$ and $\xi_v$ have the same local invariant for each $v\in S$.
Local injectivity gives $\mathrm{res}(x)=\xi$. Exactness gives $\partial\xi=0$,
proving the trace isomorphism

$$
H_c^3(D)\ \xrightarrow[\quad T\quad]{\sim}\ \mathbf Z/n\mathbf Z.
$$

In particular, the sequence

$$
H^2(G_S,D)\xrightarrow{\mathrm{res}}
\prod_{v\in S}H^2(F_v,D)\xrightarrow{\sum_v t_v}\mathbf Z/n\mathbf Z\longrightarrow0
$$

is exact at the local product and the last term. If a global degree-two class restricts to
zero at all but one place of $S$, it must restrict to zero there as well. This consequence needs only reciprocity and local injectivity. The trace isomorphism
also provides the target of the compact cup-product pairings.

**Reciprocity at the auxiliary prime.** The odd-prime argument applies this
consequence to a cup product of two one-cocycles. Here the coefficients are written additively as
$A=\mathbf Z/\ell^r\mathbf Z$ with $r>0$ and cyclotomic action $\chi$, and $\ell$ is odd.
Consider a continuous two-cocycle $w$ on the absolute Galois group of a number field.
Suppose it is constant on the cosets of the restricted-ramification kernel in each
variable, and that the finite set $S$ contains the places above $\ell$.
Then $w$ descends to a continuous two-cocycle of $G_S$ for this action: the cocycle identity
descends because the cyclotomic action also factors through $G_S$.
If its local restrictions at all $v\ne v_0$ in $S$ are coboundaries, the sum-of-invariants
arrow forces its restriction at $v_0$ to be a coboundary as well.
In the archive this implication is taken from the last arrow of the nine-term
sequence and the local invariant isomorphisms.

The specific cocycle is a cup product. Let $B$ be a commutative discrete $A$-algebra and
$\lambda:B\to A$ an $A$-linear map. Write $\alpha,\beta$ for the two continuous characters
into $B^\times$ whose product is $\chi$ (viewed in $B$), and let $c,z$ be continuous
one-cocycles with actions $\alpha,\beta$ respectively. In particular,

$$
 c(gh)=c(g)+\alpha(g)c(h),\qquad
 z(gh)=z(g)+\beta(g)z(h).
$$

Set $w(g,h)=\lambda(z(g)\alpha(g)c(h))$. To check the two-cocycle identity, expand

$$
\begin{aligned}
(\mathrm dw)(g,h,j)
={}&\chi(g)w(h,j)-w(gh,j)+w(g,hj)-w(g,h).
\end{aligned}
$$

The two one-cocycle identities make the terms involving $z(h)c(j)$ cancel,
using $\alpha(g)\beta(g)=\chi(g)$; the remaining terms involving $z(g)c(h)$
and $z(g)c(j)$ cancel separately. If on a local decomposition group
$c(g)=\alpha(g)m-m$ for a fixed $m\in B$, an explicit local primitive is

$$
 b(g)=-\lambda(z(g)\alpha(g)m).
$$

Indeed $\chi(g)b(h)-b(gh)+b(g)=\lambda(z(g)\alpha(g)(\alpha(h)m-m))=w(g,h)$.
In the archive's calculation, these primitives give the local coboundaries
away from the auxiliary prime. Reciprocity gives the remaining coboundary;
local orthogonality at that prime then constrains the two one-cocycles.

**Concordance with the archive.**

| Step | Declaration in the archive |
| --- | --- |
| Primary injectivity, lifting and restriction to the primary part | [eq_zero_of_sUnitsBrauer_eq_zero, exists_sUnitsBrauer_eq_iff, sUnitsBrauerPrimary_bijective](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/GroundTheory/ProfiniteCohomology/RestrictedRamification/Brauer.lean#L282-L365) |
| Primary $S$-unit comparison and its map | [sUnitsH2PrimaryEquiv, coe_sUnitsH2PrimaryEquiv_apply](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/GroundTheory/ProfiniteCohomology/RestrictedRamification/Brauer.lean#L376-L421) |
| Local invariant without the roots-in-$F$ assumption | [bijective_gsRootsLocalMor_of_places, bijective_gsLocalInvRoots_of_places](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/GroundTheory/ProfiniteCohomology/RestrictedRamification/BijectiveGsLocalInvRootsOfPlaces.lean#L25-L43) |
| Local invariant comparison and the roots-in-$F$ specialization | [gsLocalInvRoots_eq, bijective_gsLocalInvRoots](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/GroundTheory/ProfiniteCohomology/RestrictedRamification/BaseLocal.lean#L188-L214) |
| Vanishing of the sum on global classes | [sum_brauerInvZ_gsLocalRes_sUnits, gsSumInvRoots_globalToLocal](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/GroundTheory/ProfiniteCohomology/RestrictedRamification/BaseDefs.lean#L256-L291) |
| Descending the sum through the cone | [localToCompact_two_surjective, gsCompactInv, gsCompactInv_localToCompact](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/GroundTheory/ProfiniteCohomology/RestrictedRamification/BaseDefs.lean#L293-L321) |
| Surjectivity of the trace | [surjective_gsCompactInv](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/GroundTheory/ProfiniteCohomology/RestrictedRamification/BaseInv.lean#L97-L108) |
| Primary lift, Kummer step and bijectivity | [exists_sUnits_of_mem_localPrimaryKernel, injective_gsCompactInv, bijective_gsCompactInv, bijective_gsCompactInv_of_mem](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/GroundTheory/ProfiniteCohomology/RestrictedRamification/BaseInv.lean#L196-L270) |
| Use of the trace in the pairing | [compactZmodDualityMap](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/GroundTheory/ProfiniteCohomology/RestrictedRamification/BaseFormal.lean#L25-L36) |
| Last-place reciprocity for a descended cocycle | [glob](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/PrimitiveFrobeniusFixed/OverIff.lean#L23-L53) |
| Cup product and the explicit local primitive | [core](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/PrimitiveFrobeniusFixed/OverIff.lean#L225-L295) |
:::

:::{dropdown} From the compact trace to the duality pairing

Assume in this note that $F$ contains the $n$-th roots of unity, and put
$A=\mathbf Z/n\mathbf Z$ with trivial action. The pairing

$$
H^i(G_S,A)\ \times\ H_c^{3-i}(D)\ \longrightarrow\ A,
\qquad (x,y)\longmapsto T(y\smile x)
$$

is perfect for $0\le i\le3$: either factor identifies with the additive character
dual of the other into $A$. The compact argument of the cup product comes first.
Besides the trace isomorphism, we use local Tate duality, global degree-three
vanishing for $A$ and $D$, finiteness of $H^1(G_S,A)$ and $H_c^2(D)$, and the
compatibility of compact cup products with localization. The arithmetic heart
of the proof is the degree-one pairing.

**Compact Kummer theory.** For $U=\mathcal O_{F_S,S}^{\times}$ as above, the notation
$H_c^i(U)$ now uses local coefficient groups $\overline{F_v}^{\,\times}$, not just the
restriction of $U$; the localization map includes the natural embeddings into these
groups. The same cone construction and its long exact sequence apply.
The global and local Kummer sequences form a compatible pair, giving a connecting map
$\delta_n:H_c^1(U)\to H_c^2(D)$.

This map is onto. Indeed, the primary subgroup of $H_c^2(U)$ is zero:
if $y$ is killed by a power of $\ell$, its image in $H^2(G_S,U)$ has zero local Brauer
components at places in $S$ by compact exactness, outside $S$ by the $S$-unit comparison,
and at infinity by the odd-or-totally-imaginary hypothesis. Primary injectivity of that
comparison gives zero global image. Compact exactness now expresses $y$ as the image
of a tuple of classes in $H^1(F_v,\overline{F_v}^{\,\times})$; all are zero by Hilbert 90.
Consequently the map $H_c^2(D)\to H_c^2(U)$ is zero, since its source is killed by $n$.
Exactness gives surjectivity of $\delta_n$ and identifies its kernel with $nH_c^1(U)$.

**The idelic presentation of compact classes.** Write $C_S$ for the quotient of the idele
class group in which local units outside $S$ and the archimedean factors are killed.
It has a presentation by the local multiplicative groups at $v\in S$ and divisors at
finite places outside $S$, modulo the diagonal principal presentation.
In cochains and homomorphisms we write the multiplicative groups additively.

A datum $d=(t,(a_v)_{v\in S})$ consists of $t\in F_S^\times$ whose Galois ratios
$\sigma(t)/t$ belong to $U$, and elements $a_v\in F_v^\times$.
The divisor of $t$ away from $S$ descends to a divisor of $F$: the extension is
unramified there and the valuations of $t$ at primes over a given prime agree.
Write this divisor as $\operatorname{div}_{\bar S}(t)$.
The datum gives a compact class $q(d)\in H_c^1(U)$ represented by
$(dt,(\iota_v(t)+a_v)_v)$ in additive notation, where $\iota_v$ is the chosen
local embedding and $dt$ is the Galois coboundary of $t$. Its idele class $c(d)\in C_S$ is represented
by $( (a_v)_v,-\operatorname{div}_{\bar S}(t))$.

We need three properties of these data.

1. Every compact degree-one class has such a datum. A global one-cocycle with values
   in $U$ is a coboundary in $F_S^\times$ by Hilbert 90; its local null-homotopies
   then differ from the local images of that cobounding element by local invariants
   $a_v\in F_v^\times$.
2. If $c(d)=0$, then $q(d)=0$. In the principal presentation there is $x\in F^\times$
   with local entries $a_v$ and divisor $-\operatorname{div}_{\bar S}(t)$.
   Thus $tx$ is an $S$-unit and the cone representative of $q(d)$ is exactly the
   compact coboundary of $tx$.
3. For every $a\in C_S$ there is a datum $d$ and a positive integer $m$ prime to
   $\ell$ with $c(d)=ma$. In the divisor presentation of $a$, the class of the
   outside-$S$ divisor has finite order $\ell^j m$. The principal multiple $\ell^j m$ of the divisor is
   the outside-$S$ divisor of some $x\in F^\times$. Take $y$ with $y^{\ell^j}=x$.
   At every place outside $S$, the valuation of $x$ is divisible by $\ell^j$;
   after dividing by the corresponding power of a uniformizer, adjoining the
   root is the same as adjoining a root of a unit of degree prime to the residue
   characteristic. The unit-root polynomial defines a finite étale algebra over
   the valuation ring, so the extension is unramified there. Hence $y\in F_S^\times$,
   and its outside-$S$ divisor is the pullback of $m$ times the original divisor.
   Its Galois ratios are roots of unity, hence $S$-units. Taking $t=y^{-1}$
   and multiplying the local entries by $m$ gives the required datum.
   Thus the image of the datum map contains a prime-to-$\ell$ multiple of
   every idele class.

Class field theory identifies $H^1(G_S,A)=\operatorname{Hom}_{\rm cont}(G_S,A)$ with
$\operatorname{Hom}(C_S,A)$. The archive uses *all additive homomorphisms* on the
idelic side of this isomorphism. Let $\chi_x$ denote the character attached to $x$.

**The evaluation formula.** The degree-one pairing is given by

$$
 T(\delta_n q(d)\smile x)=\chi_x(c(d)).
$$

Here $\delta_n$ includes the local comparison of root modules. Compute the
invariants in $\mathbf Q/\mathbf Z$ via the embedding $A\hookrightarrow\mathbf Q/\mathbf Z$.
Let $z:G_S\to A$ represent $x$, take integer lifts
$\tilde z(g)$ between $0$ and $n-1$, and let

$$
 B_z(g,h)=\frac{\tilde z(g)+\tilde z(h)-\tilde z(gh)}{n}.
$$

This represents the integral Bockstein of $x$ and its class is killed by $n$.
The compact Kummer/Bockstein product identity says that the image of
$\delta_n q(d)\smile x$ in $H_c^3(U)$ is $q(d)\smile[B_z]$.
The sign is positive: the connecting-map product rule in compact degree one
gives the difference of these two expressions.

The global part of this latter cup is $dt\smile B_z$. Its cohomology class in
$H^3(G_S,U)$ is killed by $n$; the archive's separate vanishing theorem for the
$\ell$-primary part of this group therefore gives a two-cochain $Q$ in $U$ with
$dQ=dt\smile B_z$. In the larger multiplicative module $F_S^\times$ put
$W=t\smile B_z-Q$ in additive notation. The cochain $W$ is a cocycle, since
$d(t\smile B_z)=dt\smile B_z$.
Subtracting the compact coboundary of $(Q,0)$ from the product leaves global
component zero and local components $\operatorname{res}_v W+a_v\smile B_z$.
Thus the two local terms come from the global divisor and the local entries,
respectively.

Choose a local degree-two tuple $\xi$ representing the original compact
root-valued cup, using the surjectivity of the local-to-compact map in degree
two. Let $\xi^U_v$ be its image in the local Brauer group. By cone exactness,
the two local tuples $(\xi^U_v)_v$ and
$(\operatorname{res}_v W+a_v\smile B_z)_v$ differ by restrictions of a global
$S$-unit degree-two class. Its Brauer invariants vanish at finite places outside $S$.
At a finite place $w$ outside $S$, the valuation of $W$ is
$\operatorname{ord}_w(t) B_z$ because $Q$ is $S$-unit-valued. The unramified
local reciprocity formula identifies its invariant with the character on
that divisor. On the other hand local reciprocity identifies
$\operatorname{inv}_v(a_v\smile B_z)$ with $\chi_x$ on the idele supported at $v$
with entry $a_v$.

Subtract this global $S$-unit correction from $W$ so that its local
restrictions inside $S$ equal $\xi^U_v-a_v\smile B_z$ in the Brauer group.
This does not change the outside-$S$ invariants. The sum of the inside-$S$
invariants of this corrected global Brauer class is killed by $n$: both
the root-valued tuple and the local Bockstein terms have $n$-torsion invariants.
Global reciprocity expresses this sum as minus the outside-$S$ sum and minus
the archimedean sum. The outside-$S$ sum is also killed by $n$, by the divisor
formula. Hence the archimedean sum is killed by $n$, as well as by $2$; it
vanishes if $n$ is odd, and is zero in the totally imaginary case.
Only the *sum* of the archimedean contributions is needed.

Adding the local-entry contributions gives the value of the character on
$((a_v)_v,-\operatorname{div}_{\bar S}(t))$, as required. The minus sign in the
divisor term is the sign from global reciprocity.

**Nondegeneracy.** For a nonzero $x$, choose $a\in C_S$ with
$\chi_x(a)\ne0$. Property 3 gives $c(d)=ma$ with $(m,\ell)=1$, so
$T(\delta_n q(d)\smile x)=m\chi_x(a)\ne0$.

Conversely, let $y\in H_c^2(D)$ annihilate all of $H^1(G_S,A)$.
By compact Kummer surjectivity and property 1, write $y=\delta_n q(d)$.
The evaluation identity says that every homomorphism $C_S\to A$ kills $c(d)$.
For any abelian group $C$, such homomorphisms separate points of $C/nC$:
if an element of the quotient is nonzero, map its cyclic subgroup nontrivially
to $\mathbf Q/\mathbf Z$ and extend using injectivity of $\mathbf Q/\mathbf Z$.
The image lies in its $n$-torsion, hence in $A$. Therefore $c(d)=na$ for some $a$;
no finiteness of $C_S/nC_S$ has been assumed.
Choose $d'$ with $c(d')=ma$, $(m,\ell)=1$. Then $c(md-nd')=0$,
so property 2 yields $mq(d)=nq(d')$. Applying $\delta_n$ gives $my=0$.
Since $ny=0$ and $(m,n)=1$, we get $y=0$.
Both cohomology groups are finite, and each has the same order as its
character dual. Nondegeneracy in both variables therefore gives a perfect pairing.

**The remaining degrees.** Let $\partial$ denote each
local-to-compact map and $j$ each compact-to-global map, with coefficients and
degrees understood. In degrees zero and three, scalar multiplication and the
trace give the degree-zero pairing, while both groups in the degree-three
pairing are zero: $H^3(G_S,A)=0$ and $H_c^0(D)=0$, the latter because $S$ is
nonempty and localization is injective on invariants.

In degree two use local duality and the compact cup product identities.
For a local tuple $u$ and a global class $x$ of complementary degree,
$T(\partial u\smile x)$ is the sum of the local invariants of
$u\smile\operatorname{res}x$. For $y_c\in H_c^1(D)$ and $x_c\in H_c^2(A)$,
the signed compact cup comparison gives

$$
 T(y_c\smile j x_c)=T(x_c\smile j y_c).
$$

The compact cup interchange identity has sign $(-1)^{1\cdot2}=+1$.
Choose an identification $D\simeq A$ of trivial cyclic modules. Transporting
the degree-one pairing along it gives a perfect pairing of $H_c^2(A)$ with
$H^1(G_S,D)$.

Suppose $x\in H^2(G_S,A)$ annihilates $H_c^1(D)$. Testing against
$\partial P^0(D)$ and applying local duality gives $\operatorname{res}x=0$.
Choose $x_c$ with $jx_c=x$. The functional $z\mapsto T(x_c\smile z)$ on
$H^1(G_S,D)$ vanishes on the kernel of localization: there $z=jy_c$ and
the compact cup comparison reduces the value to $T(y_c\smile x)=0$.
It therefore factors through the image of localization in $P^1(D)$ and
extends to the entire group by injectivity of $\mathbf Q/\mathbf Z$.
By local duality the extension is represented by a tuple $\eta\in P^1(A)$,
using local products in the order $\eta_v\smile z_v$.
The class $x_c-\partial\eta$ now annihilates all of $H^1(G_S,D)$,
so it vanishes by degree-one duality. Applying $j$ gives $x=0$.

To prove surjectivity, let $\lambda:H_c^1(D)\to A$ be any functional.
By local duality its composite with $\partial:P^0(D)\to H_c^1(D)$ is represented by
a tuple $\xi\in P^2(A)$, with local products in the order
$u_v\smile\xi_v$. The functional kills the diagonal invariants
$H^0(G_S,D)$ by exactness. Testing a generator of the trivial cyclic $D$
shows that the sum of the invariants of $\xi$ after coefficient identification
$A\simeq D$ is zero. The trace isomorphism and exactness therefore give a lift
$x_0\in H^2(G_S,A)$ of $\xi$.
Subtract from $\lambda$ the functional given by $x_0$.
The difference vanishes on $\partial P^0(D)$ and hence descends to the image
of $j:H_c^1(D)\to H^1(G_S,D)$. Extend it to all of $H^1(G_S,D)$ and apply
degree-one perfectness to obtain a representing $x_c\in H_c^2(A)$.
The compact cup comparison shows that $x_0+jx_c$ represents the original
$\lambda$. This completes all four degrees over a field containing the
roots of unity.

**Concordance with the archive.**

| Step | Declaration or proof in the archive |
| --- | --- |
| Compact primary vanishing and Kummer surjectivity | [eq_zero_of_gsUnitsCompact_two](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/GroundTheory/ProfiniteCohomology/RestrictedRamification/BaseKummer.lean#L228-L266), [surjective_gsKummerCompactδ](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/GroundTheory/ProfiniteCohomology/RestrictedRamification/BaseKummerDelta.lean#L38-L64) |
| Datum representation and prime-to-$\ell$ realization | [exists_gsUnitsDatum, gsUnitsData_surjective](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/GroundTheory/ProfiniteCohomology/RestrictedRamification/BaseClassIdele.lean#L197-L224), [gsUnitsClass, gsUnitsData_eq_zero_of_gsUnitsClass_eq_zero, exists_coprime_gsUnitsClass_eq](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/GroundTheory/ProfiniteCohomology/RestrictedRamification/BaseClassIdele.lean#L260-L332) |
| All idelic characters | [charEquiv](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/GroundTheory/ProfiniteCohomology/RestrictedRamification/ClassFieldGSFull.lean#L77-L82) |
| Compact Kummer/Bockstein identity | [gsKummerCompactδ_cup](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/GroundTheory/ProfiniteCohomology/RestrictedRamification/BaseCupKummer.lean#L296-L319) |
| Global correction cocycle | [exists_gsUnitsData_cup_bock](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/GroundTheory/ProfiniteCohomology/RestrictedRamification/BaseCupGlobal.lean#L219-L277) |
| Local tuple and divisor correction | [gsRootsToUnitsCompact_cup_eq](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/GroundTheory/ProfiniteCohomology/RestrictedRamification/GsRootsToUnitsCompactComparisonCup.lean#L60-L104), [zmodToQZ_gsCompactInv_gsCupClass](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/GroundTheory/ProfiniteCohomology/RestrictedRamification/ZmodToQZGsCompactInvLocalToCompactEqLocalInvU.lean#L100-L150) |
| Evaluation and the two kernels | [gsCompactInv_gsCupClass, gsCompactInv_ker_left, exists_nsmul_eq_of_forall_zmod, gsCompactInv_ker_right](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/GroundTheory/ProfiniteCohomology/RestrictedRamification/BasePairing.lean#L87-L202) |
| Compact cup interchange | [compactCupRes_zmodMulPairingRight_swap](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/GroundTheory/ProfiniteCohomology/RestrictedRamification/BaseSwap.lean#L28-L52) |
| Degree zero, one and three | [bijective_three, bijective_zero, bijective_one](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/GroundTheory/ProfiniteCohomology/RestrictedRamification/BaseFormal.lean#L395-L440) |
| Degree two, both directions | [injective_two, surjective_two](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/GroundTheory/ProfiniteCohomology/RestrictedRamification/BaseFormal.lean#L536-L751) |
| Assembly over the base field | [BaseDualityHypotheses.of_gs, bijective_gs_compactZmodDualityMap](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/GroundTheory/ProfiniteCohomology/RestrictedRamification/BijectiveGsCompactZmodDualityMap.lean#L23-L73) |
:::

:::{dropdown} Descent, general coefficients and the nine-term sequence

Return to the original field $F$, which need not contain the roots of unity.
Write $G=G_S$ and let $M$ be a finite discrete $G$-module killed by $n$.
Its dual is $M^D=\operatorname{Hom}(M,D)$ with the contragredient action,
where $D=\mu_n(F_S)$. Write $B_i^M(x,y)=T(y\smile x)$, with the evaluation
pairing of coefficients understood. The goal is to identify

$$
H^i(G,M)\ \simeq\ \operatorname{Hom}(H_c^{3-i}(M^D),A).
$$

We use the dimension bound $H_c^4(N)=0$ for every finite $n$-torsion module
$N$, together with the Shapiro and Mackey isomorphisms and their compatibility
with compact cup products.

**Open subgroups and the normalization of the trace.** Choose an open
subgroup $W_0$ of $G$ fixing $D$. Every open subgroup $W\subset W_0$
corresponds to a finite extension $E/F$ in $F_S$ containing the $n$-th roots
of unity. The maximal extension of $E$ unramified outside the places over
$S$ is $F_S$. The assumptions on $S$ and on oddness or imaginary places
pass to $E$. The preceding cyclic pairing theorem therefore applies there.

The compact corestriction in degree three is onto, even if the index
$[G:W]$ is divisible by $\ell$. Indeed the coefficient trace

$$
\operatorname{Coind}_W^G(D|_W)\longrightarrow D
$$

is onto: a coinduced function supported on the identity coset with the
prescribed value there maps to that value. Its kernel is a finite
$n$-torsion module. Compact degree-four vanishing for this kernel makes
the degree-three cohomology map of the coefficient trace onto. The
compact Shapiro–Mackey isomorphism identifies it with corestriction.
In particular, no division by the extension degree is needed.

Let $T_E$ and $T_F$ be the trace isomorphisms over $E$ and $F$. The composite
of compact corestriction with $T_F$ is a surjection from $H_c^3(E,D)\simeq A$
to $A$. It is therefore $uT_E$ for some $u\in A^\times$.
Multiplication by a unit preserves perfectness, so the Mackey cup comparison
transports the pairing over $E$ without requiring the identity $u=1$.

Via the global and compact Shapiro isomorphisms, compatible with evaluation
and coefficient trace, we obtain perfect pairings in every degree for
$\operatorname{Coind}_W^G A$ and its finite direct sums.

**Embedding a general coefficient module.** Choose $W\subset W_0$
open and acting trivially on $M$; this is possible because $M$ is finite
and discrete. For every additive character $f:M\to A$, adjunction
gives a $G$-map $M\to\operatorname{Coind}_W^G A$, whose evaluation at
the identity recovers $f$. Taking all these maps gives an injection
into a finite direct sum $I$ of such coinduced modules: characters
separate points of any $n$-torsion abelian group by the extension
argument above. Write the resulting sequence as

$$
0\longrightarrow M\xrightarrow{i} I\xrightarrow{p} Q\longrightarrow0.
$$

Its dual sequence is exact in the opposite direction, since
$\operatorname{Hom}(-,A)$ is exact on $n$-torsion groups (identify $A$
with the $n$-torsion of the injective group $\mathbf Q/\mathbf Z$).
All the modules remain finite and killed by $n$.
The pairing for $I$ is known in every degree; the quotient $Q$ will enter
through the induction hypothesis.

**Induction in cohomological degree.** In degree zero, injectivity
for $M$ follows by naturality from injectivity for $I$ and of the map
on invariants. For surjectivity, compact degree-four vanishing makes
$H_c^3(I^D)\to H_c^3(M^D)$ onto. The pullback of a functional along this map is represented by a class in
$H^0(G,I)$, by duality for $I$.
Its image in $H^0(G,Q)$ pairs to zero, because the two consecutive
maps of the dual sequence compose to zero. Degree-zero injectivity
for every module, already proved, makes that image zero. The class
lifts to $H^0(G,M)$ and represents the original functional by
surjectivity of the compact map.

For the induction step let $r+1+s=3$. Assume perfectness in degree
$r$ for every finite $n$-torsion module. Write $\delta$ for the global
connecting map and $\delta_c$ for the compact connecting map of the
dual exact sequence. The compact product rule supplies the signed
identity

$$
 B_{r+1}^{M}(\delta q,y)
   =(-1)^{s+1}B_r^{Q}(q,\delta_c y)
$$

for $q\in H^r(G,Q)$ and $y\in H_c^s(M^D)$.
All the other squares express naturality of evaluation.

For injectivity, suppose $x\in H^{r+1}(G,M)$ annihilates the compact group. Its image in
$H^{r+1}(G,I)$ is zero by perfectness for $I$, so $x=\delta q$ for
some $q\in H^r(G,Q)$. The signed identity says that $B_r^Q(q,-)$
annihilates the image of $\delta_c$, which is the kernel of
$H_c^{s+1}(Q^D)\to H_c^{s+1}(I^D)$. Extend the resulting functional
on the image to the whole target. By the induction hypothesis
for $I$, the extension is represented by a class $v\in H^r(G,I)$.
Naturality and degree-$r$ injectivity for $Q$ give $p_*v=q$.
Hence $x=\delta p_*v=0$. This establishes injectivity in degree
$r+1$ for every module before proceeding to surjectivity.

For surjectivity, take a functional $\lambda:H_c^s(M^D)\to A$ and pull it back to
$H_c^s(I^D)$. Perfectness for $I$ represents it by
$v\in H^{r+1}(G,I)$. The image of $v$ in $H^{r+1}(G,Q)$ is zero
by naturality and the just-proved degree-$(r+1)$ injectivity for $Q$.
Choose a lift $x'\in H^{r+1}(G,M)$. The difference
$\nu=\lambda-B_{r+1}^M(x',-)$ kills the image of $H_c^s(I^D)$,
which is the kernel of $\delta_c$. Extend $\nu$ through $\delta_c$
to a functional on $H_c^{s+1}(Q^D)$; by the induction hypothesis
it has the form $B_r^Q(q,-)$. The signed identity shows that

$$
 x'+(-1)^{s+1}\delta q
$$

represents $\lambda$. This completes the induction through degree three. The induction is on the
degree, with injectivity established for every coefficient module before
surjectivity in that degree.

**Beyond prime powers.** For a finite module killed by a positive integer
$N$, split it into its primary summands. Assume $S$ contains the places above every prime
factor of $N$, and $N$ is odd or $F$ is totally imaginary. The case $N=1$ is trivial. If a summand is killed by
$q=\ell^k$ dividing $N$, its dual into $\mu_N$ is identified with the
dual into $\mu_q$ by the inclusion $\mu_q\hookrightarrow\mu_N$.
The local invariant maps are compatible with this inclusion after
embedding their targets in $\mathbf Q/\mathbf Z$.
Surjectivity of the degree-two local-to-compact map then gives the
same compatibility for the global compact traces. This allows the
primary pairings to be added, with zero cross-pairings for different
primes, to obtain the general finite-coefficient compact duality.

**The nine terms and the Sha pairing.** In this note use $D=\mu_N(F_S)$ and let $M^D=\operatorname{Hom}(M,D)$.
Write $P^j(M)=\prod_{v\in S}H^j(F_v,M)$ and
$X^*=\operatorname{Hom}(X,\mathbf Q/\mathbf Z)$.
Compact duality identifies $H_c^{j+1}(M)$ with $H^{2-j}(G,M^D)^*$,
using the bidual coefficient identification and finiteness (the latter follows
from the separate global and local finiteness theorems and the cone sequence).
Transport the cone localization sequence through these isomorphisms.
The map from the local product to the dual global group is explicitly
the sum of the local cup-product invariants, since cup with a
local-to-compact class is the local cup followed by that map.
Degree-zero compact vanishing and global degree-three vanishing give
the two endpoints. The resulting sequence is

$$
\begin{aligned}
0&\to H^0(G,M)\to P^0(M)\to H^2(G,M^D)^*\\
 &\to H^1(G,M)\to P^1(M)\to H^1(G,M^D)^*\\
 &\to H^2(G,M)\to P^2(M)\to H^0(G,M^D)^*\to0 .
\end{aligned}
$$

Here $\Sha^j(M)=\ker(H^j(G,M)\to P^j(M))$ uses this same finite
set of places. Compact exactness identifies $\Sha^1(M)$ with
$H_c^1(M)/\partial P^0(M)$. The annihilator of $\Sha^2(M^D)$
in $H^2(G,M^D)^*$ is precisely the image of $P^2(M^D)^*$:
functionals annihilating the kernel factor through the image of
localization and extend to its target. Local Tate duality identifies
that image with the image of $\partial P^0(M)$ under compact duality.
Taking the quotient therefore gives
$\Sha^1(M)\simeq\Sha^2(M^D)^*$, with the pairing independent of the
choice of compact lift. This gives the Sha pairing.

**Concordance with the archive.**

| Step | Declaration or proof in the archive |
| --- | --- |
| Degree-three corestriction surjectivity | [surjective_compactCores_three](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/GroundTheory/ProfiniteCohomology/RestrictedRamification/BaseCores.lean#L100-L131) |
| Trace comparison up to a unit and transport | [exists_isUnit_mul_of_surjective_of_bijective, bijective_of_transport](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/GroundTheory/ProfiniteCohomology/RestrictedRamification/BaseLevel.lean#L19-L58), [bijective_zmodCompactDualityMap_gsOpenSubgroup](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/GroundTheory/ProfiniteCohomology/RestrictedRamification/BaseLevel.lean#L83-L110) |
| Arithmetic inputs on all sufficiently small open subgroups | [gsBaseBijective_of_le](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/GroundTheory/ProfiniteCohomology/RestrictedRamification/BijectiveGsLocalInvRootsOfPlaces.lean#L83-L118), [exists_compactDualityHypotheses_gs](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/GroundTheory/ProfiniteCohomology/RestrictedRamification/BaseMain.lean#L37-L66) |
| Compact Mackey cup compatibility | [mackeyCompactCohomologyIso_compactCupRes](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/GroundTheory/ProfiniteCohomology/PoincarePairs/MackeyCup.lean#L457-L490) |
| Connecting sign, coinduced embedding | [compactDualityMap_δ, exists_injective_biproduct_coind_le](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/GroundTheory/ProfiniteCohomology/PoincarePairs/Devissage.lean#L106-L170) |
| Degree induction | [injective_zero, surjective_zero, injective_succ, surjective_succ, bijective_compactDualityMap](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/GroundTheory/ProfiniteCohomology/PoincarePairs/Devissage.lean#L253-L448) |
| Primary decomposition and coefficient transport | [bijective_compactDualityMap_of_primePow](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/GroundTheory/ProfiniteCohomology/PoitouTate/Primary.lean#L200-L257), [zmodToQZ_gsCompactInv_gsRootsIncl](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/GroundTheory/ProfiniteCohomology/PoitouTate/ZmodToQZCompactCohomologyResMapOfLocalInv.lean#L170-L188) |
| Nine terms and Sha | [exact_stage, nineTerm, bijective_ptShaPairing](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/GroundTheory/ProfiniteCohomology/PoitouTate/Abstract.lean#L176-L278), [poitouTate_duality_gs, poitouTate_sha_gs, poitouTate_nineTerm_gs](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/GroundTheory/ProfiniteCohomology/PoitouTate/PoitouTateNineTermGs.lean#L36-L70) |
:::

:::{dropdown} From finite-level duality to the integral length formulas

**Reduction of integral cohomology.** Use the setting in the main text.
Write $X=H^2(G_S,L)$, $Y=P^2(L)$, $f:X\to Y$, and $f_r$ for finite-level
localization. We establish finite generation of $X,Y$ and compatible
isomorphisms $X/\ell^rX\simeq H^2(G_S,L_r)$ and
$Y/\ell^rY\simeq P^2(L_r)$ using finiteness and degree-three vanishing at finite coefficient levels.

A finite-level two-cocycle lifts to a
continuous two-cochain at the next level: choose a section between the
finite discrete coefficient groups. Its differential is a three-cocycle
in the kernel, identified with $L_1$. The vanishing of $H^3(L_1)$
allows a correction by a two-cochain in that kernel. Iterating gives
compatible two-cocycles whose inverse limit is a continuous integral
two-cocycle. Conversely, if an integral two-cocycle reduces to a boundary
modulo $\ell^r$, lift its finite-level primitive to an integral
one-cochain. After subtracting its differential the original cocycle is
divisible pointwise by $\ell^r$; dividing yields a continuous integral
two-cocycle since the coefficient lattice has no torsion. Thus the
reduction kernel is exactly $\ell^r H^2(L)$.

To prove separation, suppose an integral two-cocycle is a boundary at
every finite level. The sets of its finite-level primitives modulo
one-coboundaries are nonempty torsors under the finite groups $H^1(L_r)$.
The reduction maps form an inverse system of nonempty finite sets, so
there is a compatible sequence of primitive classes (no surjectivity of
the transition maps is needed). Recursively adjust representatives by
one-coboundaries: a zero-cochain witnessing the difference at level $r$
lifts to level $r+1$. The resulting compatible actual primitives have
a continuous integral limit, showing that the original class is zero.
Hence $\bigcap_r\ell^r X=0$, and similarly for the local groups.
To prove finite generation, choose finitely many lifts of generators modulo $\ell$.
Successive approximation expresses each element modulo $\ell^r$ by
linear combinations of these lifts with compatible coefficients.
Completeness of $\mathbf Z_\ell$ gives limiting coefficients, and separation
then gives an equality in the original module. See
[reduction_h2_eq_zero_iff, reduction_h2_surjective, finite_h2_padic_representation](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/FoundationProofs/LengthEqLengthInvariantsOfTorsionLevels.lean#L75-L135).
Global finiteness in degrees one and two follows from finiteness of the local
and Sha groups (see [global_lim](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/FoundationProofs/LengthEqLengthInvariantsOfTorsionLevels.lean#L337-L351)).

**The cokernel length.** Write $C=\operatorname{coker} f$.
Right exactness of reduction gives

$$
 C/\ell^r C=Y/(f(X)+\ell^rY)\simeq\operatorname{coker} f_r .
$$

The last arrow of the nine-term sequence gives
$|C/\ell^r C|=|H^0(G_S,V)[\ell^r]|$ for every $r>0$, since the coefficient
embedding $V_r\hookrightarrow V$ is equivariant. The subgroups on the right
exhaust $H^0(G_S,V)$. On the left, $\log_\ell |C/\ell^r C|$ tends to the
extended length of the finitely generated module $C$. A free summand gives an unbounded sequence; for a
torsion module it eventually gives its length. Taking the suprema
proves the cokernel formula, without a finiteness assumption on either
length. The same argument with local Tate duality gives the local
length formula.

**The kernel length.** Put $K=\ker f$.
The natural injection $K/(K\cap\ell^r X)\to\ker f_r$ is onto if

$$
 f(X)\cap\ell^rY=\ell^r f(X).
$$

Indeed, if $f(x)=\ell^r y$ and the equality holds, write
$f(x)=\ell^r f(x')$ and replace $x$ by $x-\ell^r x'\in K$.
This condition is not automatic for a map of integral modules; for
example multiplication by $\ell$ on $\mathbf Z_\ell$ is injective
but its reduction modulo $\ell$ has nonzero kernel.

On the discrete side put $P_r=\operatorname{im}(\Sha^1(V_r)\to\Sha^1(V))$.
These subgroups increase and exhaust $\Sha^1(V)$: a continuous
one-cocycle on the compact global group has finite image in the
discrete torsion module, and the finitely many local null-homotopies
can all be chosen in a sufficiently large torsion level.
We still need injectivity of $\Sha^1(V_r)\to P_r$ at sufficiently large levels. A global cocycle in $V_r$ becoming a
boundary in $V$ is $g\mapsto ga-a$ for some $a\in V$. If its local
restrictions are boundaries in $V_r$, there are $b_v\in V_r$ with
$a-b_v\in V^{G_{F_v}}$. It suffices to find a global primitive in $V_r$.
This is the discrete counterpart of the saturation condition.

For $e\ne0$, at each finite place the cyclotomic character has infinite
image: away from $\ell$ an arithmetic Frobenius acts by the residue cardinality,
which has infinite order in $\mathbf Z_\ell^\times$, and above $\ell$ the
local cyclotomic tower has unbounded degree. Thus some element acts on $V$
by a scalar different from $1$.
The local invariant group is killed by a fixed power of $\ell$.
The local length equality makes $Y$ a finitely generated torsion
$\mathbf Z_\ell$-module, hence killed by a power of $\ell$.
For sufficiently large $r$, $\ell^rY=0$, so saturation holds. At the same
levels the local invariant groups are contained in $V_r$. Since $S$ is
nonempty, any equality
$a-b_v\in V^{G_{F_v}}$ shows that $a\in V_r$. Thus the global primitive already lies in $V_r$.

For $e=0$ the action on $V$ is trivial and the second condition holds
with global primitive zero. The cokernel cardinality formula gives
$|C/\ell^r C|=\ell^r$ at every positive level.
By the structure theorem, for large $r$ the exponent of $\ell$ in this
cardinality is $r\operatorname{rank} C$ plus the length of its torsion
submodule. Thus $C$ is free of rank one, and its torsion-freeness gives
saturation for every $r$.

For all sufficiently large $r$ in either case, finite Sha duality now
gives

$$
 |K/(K\cap\ell^r X)|=|\Sha^2(L_r)|=|\Sha^1(V_r)|=|P_r|.
$$

The descending filtration on $K$ is separated, and the increasing
filtration $P_r$ exhausts $\Sha^1(V)$. The lengths of the finite
quotients of $K$ have supremum equal to its extended length:
this follows from finite generation, since the topology on a submodule
of a finitely generated $\mathbf Z_\ell$-module is its $\ell$-adic
topology (or directly by the elementary divisor theorem).
The finite subgroups on the right have supremum of lengths equal to
the extended length of $\Sha^1(V)$. Taking the suprema proves the kernel formula.

| Step | Declaration in the archive |
| --- | --- |
| Reduction and finite generation | [reduction_h2_eq_zero_iff, reduction_h2_surjective, finite_h2_padic_representation](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/FoundationProofs/LengthEqLengthInvariantsOfTorsionLevels.lean#L75-L135) |
| Local duality at the limit | [local_tate_duality_h2_limit](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/FoundationProofs/LengthEqLengthInvariantsOfTorsionLevels.lean#L295-L302) |
| Reduction of localization, last arrow and cokernel length | [cok_ker, card_cok, ptCokerAt](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/FoundationProofs/LengthEqLengthInvariantsOfTorsionLevels.lean#L358-L397) |
| Bounded local invariants and local torsion | [exists_kill, exists_kill_pi](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/FoundationProofs/LengthEqLengthInvariantsOfTorsionLevels.lean#L399-L460) |
| Kernel and Sha filtration, including the separate zero twist | [ptShaAt](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/FoundationProofs/LengthEqLengthInvariantsOfTorsionLevels.lean#L462-L513) |
| The finite input and its integral output | [finite_level, archimedeanSignatureMatching_of_poitouTate, twist_cohomology_inputs](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/FoundationProofs/LengthEqLengthInvariantsOfTorsionLevels.lean#L517-L541) |
:::

(comp-primes)=
## 12 · Auxiliary primes and Behrend towers

```{code-cell} ipython3
:tags: [remove-input]
bd.show(bd.card('primes'))
```

### What the two primes buy

```{code-cell} ipython3
:tags: [remove-input]
scope = next(s for s in bd.scopes() if s['id'] == 'suppliers-primes')
bd.show(f"The kernel-checked theorem `QH.pairEx` (scope “{bd.esc(scope['title'])}”, "
        f"{scope['original_project_module_count']:,} original modules) assumes: *{bd.esc(scope['assumption'])}* "
        f"It concludes: *{bd.esc(scope['conclusion'])}*")
```

The primes $q$ and $d$ enter the definition of the fields over which the cohomological window is
taken (through the admissibility condition `WinPair`) and the host fields. The twists of a
character modulo $M$ by the quadratic characters at $q$, at $d$, or at both, have square-root
prime-sum bounds on $[Y,Y^A]$; bounds of this shape are what the finite comparison assumes for the
characters it discards, and how exactly the chosen primes feed the window for a fixed target
character is listed as still to be checked (card above). The choice is sequential: a counting theorem gives a positive share of
admissible first primes, and for each of them a positive share of second primes; taking the share
parameter $\tfrac12$ leaves at least one choice at each stage. Changing $Y$ may change both primes,
hence the twisted characters; applying the analytic criterion to a *fixed* $L$-function still
requires the host construction on arbitrarily late windows.

### The Behrend set in the tower

The choice of the tower uses an additive-combinatorial construction. Take the integer vectors in
$\{0,\dots,d-1\}^S$ of a fixed squared norm and encode them in base $4Ld$. A relation
$j(s_2-s_1)=i(s_3-s_1)$ between encodings, with $1\le|i|,|j|\le L$ and $i\neq j$, forces the same
relation between the vectors, because the large base prevents carries; and three distinct points
of a sphere cannot satisfy it, because a line meets a sphere at most twice. In the computed example
($S=3$, $d=3$, $L=2$, squared norm $5$) the sphere consists of the six permutations of $(0,1,2)$,
their base-$24$ encodings are {glue:text}`behrend_enc`, and all {glue:text}`behrend_checks`
relations fail ({doc}`behrend`). Choosing the most populous sphere gives the quantitative lower bound
of `hostThickExists`, and the property `HostThickOrbit` bounds the intersection of a translate
with a short segment of a high-order orbit by two points. The archive's theorems `sphere_rel`,
`noRel_image` and `hostThickExists` are kernel-checked; this repository's independent proof of the
sphere lemma is `BehrendReading.sphere_rel` ({ref}`lean-teaching`).

(comp-galois)=
## 13 · The Galois row

```{code-cell} ipython3
:tags: [remove-input]
bd.show(bd.card('galois'))
```

### Inputs and outputs

Fix a CM field $E$, an algebraic closure $\Omega/E$, a prime $\ell$, an isomorphism
$\iota:\overline{\mathbf Q}_\ell\simeq\mathbf C$ and $a\ge1$. An input is a cuspidal automorphic
representation $\pi$ of $\mathrm{GL}_a(\mathbf A_E)$ — in Lean a nonzero, invariant, irreducible space of
cusp forms — which is **regular algebraic** (at each embedding the infinitesimal-character exponents
are distinct and lie in $\tfrac{a-1}2+\mathbf Z$) and **polarized** (a Hecke character $\chi$ of the
maximal totally real subfield $E^+$ with the right sign at the real places, and an equivariant
nondegenerate pairing between $\pi\otimes(\chi\circ N_{E/E^+})^{-1}$ and $\pi$).

The output is a continuous semisimple $r:G_E\to\mathrm{GL}_a(\overline{\mathbf Q}_\ell)$, an integer
$w_\pi$ and Hodge–Tate multisets $H_\tau$ with $H_{\tau\circ c}=w_\pi-H_\tau$, such that for all but
finitely many places $v$, with $q=Nv$ and $\sigma$ a Frobenius lift,

$$
\iota\big(\operatorname{charpoly}\rho(\sigma^{-1})\big)=\prod_{\alpha\in B_v}\big(X-q^{(a-1)/2}\alpha\big),
$$

where $B_v$ is the (unique) multiset of Satake parameters of $\pi_v$, characterized through the
eigenvalues of the spherical Hecke operators on a nonzero spherical vector. The exported row also
records local–global compatibility at $v\nmid\ell$ under stated conditions on the local parameter,
and crystalline, de Rham and potentially semistable comparisons above $\ell$.

### The construction, as the source organizes it

The producer `galoisLocalGlobalStrong_recParameter` feeds two inputs into the construction: a
geometric seed (`geoOne_holds`, built from a holomorphic Lefschetz formula) and a theta-lifting
theorem (`tLiftK`, with hypotheses on Hermitian and skew-Hermitian spaces, characters and weights).
It then climbs through three domains: a restricted case with a prescribed polarizing character and
extra field and place conditions; the general "good" case, reached by **twisting** $\pi$ by a Hecke
character to meet the prescription and untwisting the Galois side; and the general case, reached by
**quadratic descent**. For the last step one takes primes $p\equiv-1$ modulo a modulus $M$ collecting
the finitely many bad primes, adjoins $\sqrt{-p}$ — inertia at $p$ moves it, so $K=E(\sqrt{-p})$ is a
new quadratic CM extension — base-changes $\pi$ to $K$, applies the good case, and patches the
resulting $r_K$ by an index-two theorem on conjugation-invariant trace identities that agree on
pairwise intersections. The result is one $\rho$ over $E$ whose restriction to $G_K$ is $r_K$ for all
but finitely many $K$; for each place $v$ a good $K$ (depending on $v$) transfers the Frobenius
formula to $\rho$. A rank-one example with the constant cuspidal line shows that the hypotheses are
inhabited and that the polarization sign matters.

### What this component is, and is not

The row is stated for **all** regular algebraic polarized cuspidal $\pi$ on $\mathrm{GL}_a$ over CM
fields; it is the input that both the cohomological window and the automorphic assembly consume. Its
verification status is the one on the card above. A proof of this local–global statement would still
leave the global estimates of the other strata to be justified, and conversely a mathematical
assessment of the theta lift, the geometric seed, base change and trace patching is a larger task
than reading their types.

(comp-inputs)=
## 14 · Seven inputs at the decisive call

```{code-cell} ipython3
:tags: [remove-input]
bd.show(bd.card('inputs'))
```

### The seven groups of hypotheses

The theorem `UpperTheory.Lit.every_character_of_theta_integrals_local_matching` takes exactly
{glue:text}`n_seven_mod` arguments, as recorded in the blueprint:

```{code-cell} ipython3
:tags: [remove-input]
meaning = ["the unitary-group hypotheses at an auxiliary place (the eigenvalue package)",
           "the local theta inputs (the local theta package)",
           "agreement of theta integrals",
           "local matching",
           "a covolume bound",
           "existence of local Langlands parameters",
           "the cohomological window"]
items = [f"{k}. `{a}` — {meaning[k - 1]}" for k, a in enumerate(seven, 1)]
assert [a.split(':')[0].strip() for a in seven] == ['P', 'F', 'hA', 'hM', 'hX', 'hL', 'hV']
bd.show("\n".join(items))
```

From them it constructs a nonempty package of definite-side data (test vectors, grids of Fourier
coefficients, linked bundles) and a "Green" input about characters of finite general linear groups,
and passes them to `every_character_of_green_v_win`, which fixes the window width $3/2$, obtains the
primitive half-plane statement through the second verified cut's chain (`TopG` from the family
shape, hosts from the window) and descends to all characters.

### How the type loses its premises

`UpperTheory.FinalTheorems.everyCharacter_of_row` takes one hypothesis, the Galois row `Row0b`
(with the archive's local-parameter convention). It inserts that same term into two fields of the
literature record `OpenLiteratureStatements` (whose fields are a row, a local-parameter
statement and a row again), adds the existence of local Langlands parameters, and obtains the
cohomological window `VWin` from the same row. The next line, `everyCharacter`, supplies the row by
name — `galoisLocalGlobalStrong_recParameter` — so the half-plane theorem, and with it the five
exports, have **no explicit arithmetic premise in their types**.

That is a statement about types, not about mathematics. Names such as `published_results_eigen`,
`published_results_first` or `theta_integrals_agree_and_local_matching_of_literature` are where to
start verifying what the supplied terms establish; they are not explanations. Two of the five open
audit questions of the reading project sit exactly here: the source comparison of the Galois input,
and the existence of nonempty compatible data for one geometric family ({doc}`verification`).
