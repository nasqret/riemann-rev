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

# The analytic engine: from one-sided windows to a zero-free half-plane

```{code-cell} ipython3
:tags: [remove-cell]
import sys
sys.dont_write_bytecode = True
sys.path.insert(0, '_lib')
from fractions import Fraction as F
import bookdata as bd

m = bd.model()
fx = bd.facts()
expected = {4: 'The centered prime sum', 5: 'Mellin transform and positive residues',
            6: 'The window criterion', 7: 'The order of choices'}
assert {c['n']: c['title'] for c in bd.comps('ana')} == expected
# numbers quoted in the prose below
sp = fx['spotlight']
assert sp['sigma'] == 1.0 and sp['delta'] == 0.5
masses = {int(U): w['mass_inside'] for U, w in sp['windows'].items()}
bd.glue('spot_U', ', '.join(str(U) for U in sorted(masses)))
bd.glue('spot_masses', ', '.join(f"{100 * masses[U]:.1f}%" for U in sorted(masses)))
bd.glue('rh_band', f"{fx['hero']['rh_band']:.4f}")
bd.glue('r_min', f"{fx['hero']['r_min']:.4f}")
bd.glue('r_max', f"{fx['hero']['r_max']:.4f}")
sup = str.maketrans('0123456789', '⁰¹²³⁴⁵⁶⁷⁸⁹')
e = len(str(fx['hero']['y_max'])) - 1
assert fx['hero']['y_max'] == 10 ** e and fx['hero']['y_min'] == 10
bd.glue('hero_ymax', '10' + str(e).translate(sup))
assert fx['zeros']['count'] == 100
assert fx['balance']['total_eps'] == '9' and fx['balance']['eD'] == 2 and fx['balance']['eL'] == 0
assert '\\tfrac12+\\tfrac12\\min' in bd.comp('choreography')['statement']
# the worked example of the order of choices: beta = 0.52
beta = F(52, 100)
theta = F(1, 2) + F(1, 2) * min(beta - F(1, 2), F(1, 2))
eps_max = (theta - F(1, 2)) / 9
assert theta == F(51, 100) and eps_max == F(1, 900)
bd.glue('ex_theta', f"{float(theta):.2f}")
bd.glue('ex_eps', f"1/{eps_max.denominator}")
```

```{code-cell} ipython3
:tags: [remove-input]
bd.show(f"{bd.stratum_badge('ana')} {bd.esc(bd.stratum('ana')['blurb'])}")
```

This stratum is the part of the argument that can be stated, and has been checked, entirely
within classical analytic number theory. Its input is a *one-sided* estimate for a weighted prime
sum on sparse but long intervals; its output is a zero-free half-plane. The mechanism is Landau's
oscillation theorem, made local: positivity forces the transform of the prime sum to have a pole
with an uncancellable residue at any zero, and high derivatives of the transform, which sample the
prime sum essentially on one window, cannot be small near such a pole.

(comp-statistic)=
## 4 · The centered prime sum

```{code-cell} ipython3
:tags: [remove-input]
bd.show(bd.card('statistic'))
```

### Why exactly these centering terms

Write $\psi(t)=\sum_{n\le t}\Lambda(n)$ and $E(t)=\psi(t)-t$. Each jump $\Lambda(n)$ of $\psi$ at $n\le x$
contributes $x\int_n^x t^{-2}\,dt=x/n-1$ to $x\int_1^x\psi(t)t^{-2}\,dt$, so

$$
\sum_{n\le x}\Lambda(n)\Big(\frac xn-1\Big)=x\int_1^x\frac{\psi(t)}{t^2}\,dt=x\log x+x\int_1^x\frac{E(t)}{t^2}\,dt .
$$

Integrating the Dirichlet series of $-\zeta'/\zeta$ by parts gives, for real $s>1$,
$-\zeta'(s)/\zeta(s)=s/(s-1)+s\int_1^\infty E(t)t^{-s-1}\,dt$; comparing with the Laurent expansion
$-\zeta'/\zeta(s)=1/(s-1)-\gamma+O(s-1)$ and letting $s\downarrow1$ yields
$\int_1^\infty E(t)t^{-2}\,dt=-1-\gamma$. Hence

$$
G(x)=-x\int_x^\infty\frac{E(t)}{t^2}\,dt ,
$$

so the linear term $(1+\gamma)x$ is exactly the one that cancels the main terms, and the size of $G$
is governed by the tail of the prime number theorem's error. The same identity shows why $G$ is the
natural *ramp-smoothed* object: it is a weighted average of $E$ over $[x,\infty)$.

### The explicit formula

Shifting the contour in the Perron-type integral for the ramp sum picks up the residues of
$-\frac{\zeta'}{\zeta}(s)\,\frac{y^s}{s(s-1)}$: at $s=1$ the double pole produces $y\log y-(1+\gamma)y$,
which $G$ subtracts; at $s=0$ the residue is $\log 2\pi$; each nontrivial zero $\rho$ contributes
$-y^\rho/(\rho(\rho-1))$ and each trivial zero $-2n$ a term of size $y^{-2n}$:

$$
G(y)=\log 2\pi-\sum_\rho\frac{y^{\rho}}{\rho(\rho-1)}-\sum_{n\ge1}\frac{y^{-2n}}{2n(2n+1)} .
$$

If every $\rho$ has real part $\tfrac12$, then $\rho(\rho-1)=-|\rho|^2$ and
$\sum_\rho|\rho|^{-2}=\sum_\rho\frac1{\rho(1-\rho)}=2+\gamma-\log4\pi$, so that
$|G(y)-\log2\pi|\le(2+\gamma-\log4\pi)\sqrt y+O(y^{-2})$; the constant is
{glue:text}`rh_band`. The computed normalized sum $(G(y)-\log2\pi)/\sqrt y$ stays between
{glue:text}`r_min` and {glue:text}`r_max` for all sampled $y$ from 10 to {glue:text}`hero_ymax`, and
the sum over the first hundred zeros reproduces it; both computations are redone in
{doc}`explicit-formula`.
A single zero $\rho=\beta+i\gamma$ with $\beta>\tfrac12$ would add an oscillation of amplitude
$\asymp y^{\beta}$ *in both directions*. The whole engine rests on the observation that, thanks to
positivity, it is enough to forbid the *upward* swings.

```{code-cell} ipython3
:tags: [remove-input]
bd.show(bd.figure_md('ramp', 'fig-ramp'))
```

### Families of characters

For a nonprincipal primitive $\chi$ the source uses
$g_\chi(y)=\sum_{n\le y}\Lambda(n)\chi(n)(y/n-1)+y\,(L'/L)(1,\chi)$; the linear term again removes the
contribution of $s=1$ to the transform. Fix a primitive $\psi$ of order $o$ and let $P$ be the set of
primitive characters inducing the elements of the cyclic group $\langle\psi\rangle$. The **level**
$G_P(x)=G(x)+\frac1{3o+1}\sum_{\chi\in P\setminus\{1\}}\Re g_\chi(x)$ is a positive combination; the
weight $\frac1{3o+1}$ is small enough that the comparison of the next stratum can control it. A
principal member of a family must have modulus one, because removing Euler factors would change the
linear main term.

(comp-residues)=
## 5 · Mellin transform and positive residues

```{code-cell} ipython3
:tags: [remove-input]
bd.show(bd.card('residues'))
```

### The computation

For $n\ge1$ and $\Re s>1$, the ramp vanishes below $n$, and

$$
\int_1^\infty\Big(\frac yn-1\Big)_{\!+}y^{-s-1}\,dy=\int_n^\infty\Big(\frac{y^{-s}}{n}-y^{-s-1}\Big)dy
=\frac{n^{-s}}{s-1}-\frac{n^{-s}}{s}=\frac{n^{-s}}{s(s-1)} .
$$

Summing against $\Lambda(n)\chi(n)$ gives $-\frac{L'}{L}(s,\chi)/(s(s-1))$, and the linear term of
$g_\chi$ integrates to $\frac{L'}{L}(1,\chi)/(s-1)$, so

$$
\int_1^\infty g_\chi(y)\,y^{-s-1}\,dy=-\frac{\frac{L'}{L}(s,\chi)-s\,\frac{L'}{L}(1,\chi)}{s(s-1)} ,
$$

whose numerator vanishes at $s=1$: the transform continues analytically to wherever $L'/L$ does,
and its only singularities in $0<\Re s<1$ are at zeros of $L(s,\chi)$.

### Why the weights must be positive

On real arguments $\Re g_\chi=\tfrac12(g_\chi+g_{\bar\chi})$, so the transform of
$G_F=\sum_i a_i\Re g_{\chi_i}$ has at $s=\rho$ the residue

$$
-\frac{S(\rho)}{\rho(\rho-1)},\qquad S(\rho)=\tfrac12\sum_i a_i\big(m_{\chi_i}(\rho)+m_{\bar\chi_i}(\rho)\big),
$$

where $m_\chi(\rho)\ge0$ is the order of vanishing. With $a_i>0$, $S(\rho)>0$ as soon as one member
(or its conjugate) vanishes at $\rho$: the contributions of different characters point in the same
complex direction and cannot cancel. For a real zero $0<\beta<1$ the residue is even positive,
because $\beta(\beta-1)<0$, and the same one-sided bound excludes exceptional (Siegel) zeros of
the family. In Lean this is `Deduction.poleData`; the archive also proves the positivity of
$S(\rho)$ separately (both are linked on the card).

(comp-criterion)=
## 6 · The window criterion

```{code-cell} ipython3
:tags: [remove-input]
bd.show(bd.card('criterion'))
```

### High derivatives as a spotlight

Put $u=\log y$, $g(u)=G_F(e^u)$ and let $\Phi(z)=\int_0^\infty g(u)e^{-zu}\,du$ be the Laplace
transform (the Mellin transform above). For $z=\sigma+it$,

$$
A_k(z):=\frac{(-1)^k}{k!}\Phi^{(k)}(z)=\int_0^\infty g(u)\,\frac{u^ke^{-\sigma u}}{k!}\,e^{-itu}\,du .
$$

The kernel $u^ke^{-\sigma u}/k!$ is a Gamma density up to the factor $\sigma^{-(k+1)}$: it peaks at
$u=k/\sigma$ and has width $\asymp\sqrt k/\sigma$. With $k=\lceil(1+\delta/2)\sigma U\rceil$ it is
aimed at the middle of the logarithmic window $[U,(1+\delta)U]$, i.e. of $[Y,Y^{1+\delta}]$ with
$U=\log Y$, and the fraction of its mass inside the window tends to $1$ exponentially fast. For
$\sigma=1$, $\delta=\tfrac12$ and $U=${glue:text}`spot_U` the computed fractions are
{glue:text}`spot_masses` ({doc}`spotlight`). The tails outside the window are controlled by a
crude global bound $|g(u)|\le C_0e^{2u}$ and a choice $\sigma>2$.

### The one-sided trick

Inside the window only an *upper* bound $g\le R$ is available. The elementary identity

$$
|g|+g=2\max(g,0)\le 2R\qquad(R\ge0,\ R\ge g)
$$

integrated against the kernel bounds $|A_k(\sigma+it)|+\Re A_k(\sigma)$ — the shifted moment
together with the *signed, unshifted* one. Along the derivative orders aimed at the windows this
gives $|A_k(\sigma+it)|+\Re A_k(\sigma)\ll e^{\eta U}(\sigma-\theta)^{-k}$ for every $\eta>0$ when
$g(u)\le Ce^{\theta u}$ on the windows.

### Why a pole cannot hide

A simple pole $c/(z-\rho)$ of $\Phi$ contributes $c/(z-\rho)^{k+1}$ to $A_k(z)$. If $\Re\rho>\theta$,
the source separates two cases. Either a vertical shift isolates a unique nearest pole with a
pole-free disc around the unshifted point, and Cauchy estimates make the analytic remainder
geometrically smaller than the pole's contribution; or a real pole dominates, and its positive
residue makes $\Re A_k(\sigma)$ large. In both cases the pole contributes $\asymp d^{-k}$ while the
window bound gives $e^{\eta U}r^{-k}$ with $d<r\le\sigma-\theta$. Since $k\ge U$,
$(r/d)^k\ge e^{U\log(r/d)}$, which beats $e^{\eta U}$ once $\eta<\log(r/d)$. So no member of the family
vanishes in $\Re s>\theta$. Because only the *existence* of arbitrarily late windows is used, the
windows may be extremely sparse.

(window-strength)=
### How strong is the window condition?

For the singleton family $\{\zeta\}$ the window condition is not only sufficient for RH but also
necessary. Under RH, Schoenfeld's Theorem 10
([Math. Comp. 1976](https://doi.org/10.1090/S0025-5718-1976-0457374-X)) gives
$|\psi(t)-t|<\sqrt t\log^2t/(8\pi)$ for $t\ge73.2$, and the identity $G(x)=-x\int_x^\infty E(t)t^{-2}dt$ of {ref}`comp-statistic` integrates
this to

$$
|G(x)|\le\frac{\sqrt x}{8\pi}\big(2\log^2x+8\log x+16\big)\qquad(x\ge73.2),
$$

which is $\le C_\theta x^\theta$ for every $\theta>\tfrac12$ and every large $x$ — on every window, not
just on sparse ones. The first verified cut is therefore an *equivalence* in disguise: it isolates
the analytic engine as correct and moves all of the difficulty of RH into its premise. (The
computed values of $G$ satisfy this bound with a large margin on the range of
{doc}`explicit-formula`; that is consistent with, not evidence for, the hypothesis.)

### Related work: a criterion with ordinary primes

*Not checked in this project.* A Lean repository by L. Crossley
([`prime-window-rh-criterion`, commit `3206456`](https://github.com/leecrossley/prime-window-rh-criterion/blob/3206456c860df1bb565de076457f7d0253000258/PrimeWindow.lean#L195-L198), theorem `ThetaTransfer.rh_of_prime_sign_windows`)
states a form of the window criterion in which only primes, not prime powers, are counted. For $y>0$ let

$$
P(y)=\sum_{y<p\le 4y}w\!\left(\frac{y}{p}\right)\log p,\qquad
w(t)=\begin{cases}2(1-t), & \tfrac12\le t<1,\\ 4t-1, & \tfrac14\le t<\tfrac12,\end{cases}
$$

the sum over primes $p$. The theorem says: if for some $\delta>0$ there are arbitrarily large $X$ such that
$P(x/4)\le\tfrac{x}{2}\log 2$ for every $x\in[X,X^{1+\delta}]$, then the Riemann hypothesis holds. The right-hand
side is the main term that the prime number theorem gives for $P(x/4)$: with $y=x/4$,
$\int_y^{4y}w(y/t)\,dt=y\big(\int_1^2 2(1-\tfrac1s)\,ds+\int_2^4(\tfrac4s-1)\,ds\big)=2y\log 2$. The proof imports
the archive's window theorem (the module `…LandauTheorems.WindowHypOfRpow`), compares the sum over primes
with the sum over prime powers, and ends with the archive's reflection step `Formalism.VW.rh_of_right`, which
turns a zero-free right half-plane into RH. So it rests on the engine of this chapter. We have not built the
repository or checked its proof.

Crossley gives the same criterion in [Theorem 3.2 of *The Crossley Criteria*](https://github.com/leecrossley/crossley-criteria-riemann-hypothesis/releases/download/v1.0/crossley-criteria-riemann-hypothesis.pdf#page=7) ([archived edition](https://doi.org/10.5281/zenodo.24466908)).

(comp-choreography)=
## 7 · The order of choices

```{code-cell} ipython3
:tags: [remove-input]
bd.show(bd.card('choreography'))
```

### Quantifiers, in the order the proof uses them

The arithmetic has to deliver, for each primitive $\psi$, a statement of the shape

$$
\exists\,e_D,e_L\ \exists\,\varepsilon_1>0\ \forall\,\varepsilon\in(0,\varepsilon_1)\ \exists\,\text{family}\ \exists\,C\
\forall\,Y_0\ \exists\,Y\ge Y_0\ \forall\,x\in[Y,Y^{3/2}]:\quad G_P(x)\le x^{\frac12+(e_D+e_L+7)\varepsilon}.
$$

The loss exponents $e_D,e_L$ come first and do not depend on $\varepsilon$; the family, the constants
and the windows may. Given a hypothetical zero with real part $\beta>\tfrac12$, the proof takes
$\theta=\tfrac12+\tfrac12\min(\beta-\tfrac12,\tfrac12)$, so that $\tfrac12<\theta<\min(\beta,1)$, then any
$\varepsilon$ with $\tfrac12+(e_D+e_L+7)\varepsilon\le\theta$, and applies the window criterion at
exponent $\theta$. With the source's $e_D=2$, $e_L=0$: for $\beta=0.52$ one gets
$\theta=${glue:text}`ex_theta` and may take any $\varepsilon\le${glue:text}`ex_eps`.

This order is why the argument never needs a bound with $\varepsilon=0$: a bound
$G_P(x)\le x^{1/2+o(1)}$ along windows, with the $o(1)$ controlled uniformly in the sense above, is
enough. It is also why the uniformity of $e_D,e_L$ is a genuine requirement on the arithmetic:
losses that grew as $\varepsilon\to0$ would break the choice of $\varepsilon$ after $\theta$.

In this repository's Lean skeleton the order of choices is the field `Supply.choose` and the
deduction is `Atlas.primitiveHalfPlane_of_supply` (axiom-free; see {ref}`lean-skeleton`).
