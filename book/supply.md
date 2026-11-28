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

### The arithmetic assembly

The reference-layer bound spends $\varepsilon/2$ on exceptional twists and
$\varepsilon/4$ on the discriminant. The resulting pointwise bound has exponential
scale $x^{3\varepsilon/4}$, leaving room to sum over the twists within
$\exp(x^{4\varepsilon/5})$. At odd coefficient primes the character counts are
organized differently: Case I bounds arbitrary finite prime sets through a
common nonzero integer made from Frobenius trace differences; the remaining
cases either restrict the coefficient prime or use a fixed reference layer.
The negative-part estimate and the conductor bound absorb the remaining terms
into the requested $\exp(x^\varepsilon/2)$.

For the detailed inequalities and the order of the uniform choices, see
{doc}`cohomological-window`. Its Case I calculation uses a cotangent-length
estimate from graded commutative algebra; {doc}`deformation-length` develops
the saturated cotangent comparison, Lemma M, and the Euler-characteristic
rules used there.

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
