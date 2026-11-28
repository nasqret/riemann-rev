# The deformation length and graded Euler characteristics

We isolate the commutative algebra of the one-character estimate, taking the
construction and rigidity of the deformation model from the archive. The numerical
part of Lemma M admits a short proof by generating functions.

## Cotangent lengths and Lemma M

The one-character estimate in {doc}`cohomological-window` is obtained in two
steps. Lemma M' bounds the cohomological length by the length of a saturated
cotangent quotient; Lemma M bounds the latter by twice a sum of valuations at
characteristic-zero points.

**From cocycles to derivations.** Let $O$ be the complete coefficient DVR,
with uniformizer $\varpi$, fraction field $F$ and finite residue field.
Write $\mathcal S$ for the locally trivial character cohomology module
of length Vlen. A continuous cocycle into the discrete torsion coefficient
module has finite image by compactness, and hence is killed by a power of
$\varpi$. Thus $\mathcal S$ is the union of its $\varpi^n$-torsion submodules.

The reducible base representation $r_0$ has diagonal characters
$\Psi,1,\Psi^{-1}$ and a quadratic multiplier. Conjugation by
$\operatorname{diag}(t,1,t^{-1})$ gives entry $(i,j)$ weight $w_i-w_j$,
where $(w_1,w_2,w_3)=(1,0,-1)$. Weight $-1$ consists of entries
$(2,1)$ and $(3,2)$. The normalization of cocycles embeds each torsion layer additively into
matrix cocycles of this weight satisfying the prescribed local coboundary
and global vanishing conditions.

Over the square-zero extension $O\oplus O/(\varpi^n)$, put
$r_\gamma(g)=(1+\gamma(g))r_0(g)$, with $\gamma$ taking values in the
square-zero ideal. Multiplication gives the cocycle equation

$$
 \gamma(gh)=\gamma(g)+\operatorname{Ad}(r_0(g))\gamma(h),
$$

where the adjoint action is that of the semidirect representation if the
multiplier is nontrivial. By the universal property of the normalized
deformation ring $R$, the deformation corresponds to an algebra map
$f\mapsto(x_0(f),D(f))$ at the base point $x_0:R\to O$, with

$$
 D(fg)=x_0(f)D(g)+x_0(g)D(f).
$$

On the $(i,j)$ matrix entry of the universal representation, the derivation
takes the value $\Psi(g)^{w_j}\gamma(g)_{ij}$. The scalars are units, so these
values recover the normalized cocycle. Additivity follows from uniqueness.

The model consists of a graded algebra $A=\bigoplus_j A_j$ with augmentation
$x:A\to O$ and a map $A\to R$ killing the homogeneous equations of the model.
The matrix entries belong to its image, so pullback preserves the injectivity
of the cocycle-to-derivation map. The integral lifting theorem, using the
local chart and a characteristic-zero lift of the local coboundary, shows
that each pulled-back derivation is the reduction of a weight-$-1$ derivation
$A\to O$ at $x$.

**The saturated cotangent lattice (Lemma M').** Put $\mathfrak a=\ker x$
and let

$$
 \mathfrak a^{[2]}=\{f\in A:\exists\,0\ne b\in O,\ bf\in\mathfrak a^2\}.
$$

Since $A/\mathfrak a\simeq O$ is torsion-free, the saturation is contained
in $\mathfrak a$ and $\mathfrak a/\mathfrak a^{[2]}$ is torsion-free.
Let $P$ be the image of $A_{-1}\cap\mathfrak a$ in this quotient and
$L$ the span over $O$ of the weight-$-1$ equations $F_0,\ldots,F_r$.
Put $C=P/L$; its extended length is the archive's cotLen.

An $O$-valued derivation at $x$ kills $\mathfrak a^2$ by the Leibniz rule
and hence its saturation, since $O$ is torsion-free. Its reduction also
kills the saturation and vanishes on the equations, so the reduced derivation induces a map
$C\to O/(\varpi^n)$. A derivation of weight $-1$ is determined by its
restriction to that weight, giving an injection

$$
 \mathcal S[\varpi^n]\longrightarrow
                    \operatorname{Hom}_O(C,O/(\varpi^n)).
$$

If $C$ has finite length, write $C\simeq\bigoplus_i O/(\varpi^{b_i})$.
The target has length $\sum_i\min(n,b_i)\le\sum_i b_i$. A module of finite
length $b$ has $q_O^b$ elements, where $q_O$ is the residue cardinality.
Thus injectivity even as a map of sets gives finiteness of each torsion
layer and bounds its length by that of $C$. If $C$ has infinite length
the bound is automatic. Taking the supremum over $n$ gives

$$
 \operatorname{length}_O\mathcal S\le\operatorname{length}_O C.
$$

Indeed every finite strict chain in a torsion module can be tested by
finitely many elements, all lying in one torsion layer. The integral lift
is essential here: a derivation with torsion coefficients need not kill
the saturated square.

**Hypotheses of Lemma M.** Let $O$ be a complete DVR of characteristic zero
and fix an algebraically closed extension of its fraction field with
valuation $v_O(\varpi)=1$. Suppose the weight-zero ring $B=A_0$ is a
complete Noetherian local $O$-algebra with the same residue field as $O$;
the augmentation induces a local retraction $B\to O$. The algebra $A$ is
finitely generated over $B$ by elements of weights $-2,-1,1,2$, and $x$
kills nonzero weights. A formal chart over $F$ identifies the rational
cotangent space via linear coefficients. Its dimensions in weights
$-2,-1,0,1,2$ are $s,r,m,r'+1,s'+1$, respectively, with $r\ge1$. The homogeneous equation ideal $J_0$ has generators
$r+1$ equations $F_i$ of weight $-1$, $s$ equations $G_i$ of weight
$-2$, $r'$ equations $E_i$ of weight $1$, $s'$ equations $E'_i$ of
weight $2$, and $m$ weight-zero equations $Z_i$ vanishing at $x$.
The $F_i,G_i,Z_i$ span their rational cotangent spaces (M1).

The image of $A_0$ in $A/J_0$ is finite over $O$ (M2). At a fixed
point of $A/J_0$ other than $x$, there cannot be both a positive-only
and a negative-only point with the same weight-zero restriction
(M3). At a two-sided point (nonzero values in both signs), the
derivations killing $J_0$ have dimension at most one (M4).
Finally, a separating element $a\in A_0$ vanishes at $x$ and is nonzero
at every two-sided point (M5). In the deformation model these hypotheses
are supplied by finiteness and rigidity; the separating element is the
trace difference, constant along grading-torus orbits.

**Smith invariants.** By the chart and finite generation, $P$ is free of
rank $r$ over $O$; the spanning condition makes $L$ a full-rank sublattice.
An invertible change of the $r+1$ equations puts their images in Smith
normal form: $\varpi^{b_i}y_i$ for $1\le i\le r$, where the $y_i$ form
a basis of $P$, and zero for the final equation $F_*$. This leaves the
equation ideal unchanged and gives $F_*\in\mathfrak a^{[2]}$ and
$\operatorname{length}_O C=\sum_i b_i$.

Eliminate the $m$ weight-zero variables using the formal implicit-function
theorem, obtaining a chart $\phi$ with $\phi(Z_i)=0$. If $\phi(a)=0$,
add to $a$ the product of a weight-$1$ element and an $F_i$ whose images
under $\phi$ are both nonzero. The chart and spanning condition provide
such elements; their product is nonzero in the power-series domain.
It lies in $J_0$, has weight zero and vanishes at $x$. This achieves
$\phi(a)\ne0$ without changing the values of $a$ on the equation scheme.

**The Rees algebra.** Consider the multigraded Rees algebra over $A_0$
of the submodules

$$
 N_0=A_{-2},\quad N_1=A_2,\quad
 N_2=A_0F_*^2+A_{-2}^2A_2 .
$$

The component of multidegree $d=(d_0,d_1,d_2)$ is
$N_0^{d_0}N_1^{d_1}N_2^{d_2}$, placed in degree $d$.
Let $U$ be its quotient by the coefficientwise kernel of $\phi$.
Let $\mathbf f$ be the list of sections consisting of the first
$r$ squares $F_i^2$ and the $G_i$ in degree $(1,0,0)$,
the $E_i^2,E'_i$ in degree $(0,1,0)$ and $F_*^2$ in degree $(0,0,1)$.
Multiplication by $a$ on $U$ is injective since $\phi(a)\ne0$.

Write $\chi_{\mathbf f}(V;d)$ for the Euler characteristic of the
graded Koszul complex on $\mathbf f$ with coefficients in $V$.
The admissibility condition ensures finite homology lengths in large
degrees. The central comparison in Lemma M is, for $d$ sufficiently
large in every coordinate,

$$
 \begin{aligned}
 2^{r+r'}\sum_i b_i
 &\le\chi_{\mathbf f}(U/aU;d)\\
 &\le\chi_{(a)}(U/(\mathbf f)U;d)\\
 &\le 2^{r+1+r'}\sum_{\xi\in T}v_O(\xi(a)).
 \end{aligned}
$$

Here $T$ is a finite set of representatives covering the two-sided
orbits over the chosen algebraically closed valued field. The middle
inequality follows from regularity of $a$ and the Euler comparison proved
below, without requiring regularity of $\mathbf f$. We compute the two
outer multiplicities in turn.

**The lower multiplicity.** In the leading-term quotient the
first $r$ squared equations have leading terms
$\varpi^{2b_i}y_i^2$, by the negative-weight filtration and
$F_i-\varpi^{b_i}y_i\in\mathfrak a^{[2]}$.
The Hilbert function of that quotient modulo $\varpi$ counts
monomials of total negative and positive weights

$$
 (u,v)=(2d_0+4d_2,\,2d_1+2d_2).
$$

The corresponding generating series is

$$
 H(X,Y)=\frac{1}{(1-X)^r(1-X^2)^s
                       (1-Y)^{r'+1}(1-Y^2)^{s'+1}} .
$$

A backward difference in the first multigrading direction
corresponds to multiplication by $1-X^2$; the other directions
give $1-Y^2$ and $1-X^4Y^2$.
Extracting the powers of $\varpi$ from the squared equations, as proved
below, bounds the Euler characteristic from below by $\sum_i2b_i$ times
the Hilbert function with $r-1+s$ differences in the first direction,
$r'+s'$ in the second and one in the third. The generating series
of this difference simplifies to

$$
 \frac{(1+X)^{r-1}(1+Y)^{r'}(1-X^4Y^2)}
      {(1-X)(1-Y)(1-Y^2)}.
$$

For $u\ge4$ and $v\ge2$, the coefficient of $X^uY^v$ in the
fraction without the two factors $(1+X)^{r-1}(1+Y)^{r'}$ is

$$
 (\lfloor v/2\rfloor+1)-(\lfloor(v-2)/2\rfloor+1)=1.
$$

For sufficiently large $u,v$, the two polynomial factors multiply
this constant by the sum of their coefficients, $2^{r-1+r'}$.
The lower multiplicity is therefore
$(\sum_i2b_i)2^{r-1+r'}=2^{r+r'}\sum_i b_i$.
This uses the leading-term and Hilbert-function comparisons of the archive;
monotonicity for the leading-term quotient transfers the bound to the
original model.

**The upper multiplicity.** In large degrees the characteristic-zero
support consists of primes obtained by restricting two-sided points
to weight zero. At these primes rigidity bounds the localized length
of each weight piece of $A/J_0$ by one.
Squaring an equation at most doubles a uniform localized length bound:
the quotient by $f^2$ is an extension of the quotient by $f$ by the
image of $f$, which is itself a quotient of the module modulo $f$ with
a grading shift. Apply this to the $r+1$ negative and $r'$ positive
equations in succession. The resulting bound $2^{r+1+r'}$ passes to the
localized graded pieces of $U/(\mathbf f)U$ by the Rees-piece comparison.

For a large piece $W$, the Euler characteristic of multiplication
by $a$ is

$$
 \theta_a(W)=\operatorname{length}_{A_0}(W/aW)
                   -\operatorname{length}_{A_0}W[a].
$$

Both lengths are finite. The norm formula expresses their difference as
a sum over the $O$-algebra maps $\sigma:B\to K$ in the characteristic-zero
support of $W$: each summand is the length of $W_{\ker\sigma}$ over
$B_{\ker\sigma}$ multiplied by $v_O(\sigma(a))$. Here $K$ is the chosen
algebraically closed valued field.

To prove the formula, use that $B/\operatorname{Ann}_B W$ is finite over
$O$ and take a prime filtration of $W$. The snake lemma gives additivity
of the kernel-cokernel difference, and localization gives additivity of
the localized lengths. A factor $D=B/\mathfrak p$ with
$\mathfrak p\cap O\ne0$ is finite over the residue field of $O$ and
contributes zero on both sides. Otherwise $D$ is a finite free $O$-module
and its fraction field is a finite extension of $F$. By the support
hypothesis $a$ is nonzero in $D$. Smith normal form for multiplication
by $a$ gives the $O$-length of its cokernel as the valuation of the
determinant, namely the field norm. Finite lengths over $B$ and $O$
agree because their residue fields agree. The norm is the product over
all embeddings of the fraction field into $K$; these are precisely the
maps $B\to K$ with kernel $\mathfrak p$. Each localized prime factor has
length one. This proves the formula with the correct multiplicity for
distinct embeddings having the same kernel.

Since $a$ is constant on torus orbits, the local multiplicity bound now
gives the upper estimate. Repetitions in the list of weight-zero
restrictions only enlarge the sum: their evaluations of $a$ are integral
and have nonnegative valuation.

Dividing the outer bounds by $2^{r+r'}$ gives

$$
 \operatorname{length}_O C\le2\sum_{\xi\in T}v_O(\xi(a)).
$$

The factor $2$ comes from the ratio of the two multiplicities.
Since $v_O=e(O/\mathbf Z_\ell)v_\ell$, dividing by the ramification
index yields the normalized one-character estimate. The chart, rigidity
and support theorems remain geometric inputs; the general Euler
comparisons are proved next.

| Step | Archive reference |
| --- | --- |
| Normalized cocycles and torsion layers | [sha_inj](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/UnitaryThreeGroups/ShaInj.lean#L27-L38), [vlen_le](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/UnitaryThreeGroups/VlenLe.lean#L46-L68) |
| Derivations and integral lifting | [main_der, model_lower](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/UnitaryThreeGroups/ModelLower.lean#L296-L402), [mprime_holds](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/CommutativeAlgebra/GradedModulesLength/Mprime.lean#L6-L81) |
| Hypotheses and statement | [M1–M5, LemmaM, LemmaM'](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/CommutativeAlgebra/OrbitVanishingLocal.lean#L21-L131) |
| Trace difference | [model_upper](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/UnitaryThreeGroups/ModelUpper.lean#L103-L251), [oneChar_unramU](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/FOneCharU.lean#L19-L74) |
| Smith normalization and chart | [sm_holds](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/CommutativeAlgebra/GradedModulesLength/SmHolds.lean#L55-L113), [cut_holds](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/CommutativeAlgebra/GradedModulesLength/CutHolds.lean#L101-L132), [nz_holds](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/CommutativeAlgebra/GradedModulesLength/NzCoeffMul.lean#L33-L90), [main_holds](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/CommutativeAlgebra/GradedModulesLength/MainCotSpan.lean#L32-L71) |
| Rees algebra and lower bound | [mN, ts, cnt](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/CommutativeAlgebra/GradedModulesLength/ToDegInjective.lean#L187-L234), [lk_holds](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/CommutativeAlgebra/GradedModulesLength/LkHolds.lean#L8-L80), [hf_holds](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/CommutativeAlgebra/GradedModulesLength/ReesGradedPieceSurjection.lean#L199-L271), [la_holds](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/CommutativeAlgebra/GradedModulesLength/LaDifPerm.lean#L77-L125), [low_holds](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/CommutativeAlgebra/GradedModulesLength/AdmissibleMonoIdeal.lean#L191-L323) |
| Numerical finite differences | [num_holds](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/CommutativeAlgebra/GradedModulesLength/FrobeniusInclusionXEqMulQ.lean#L206-L284) |
| Local multiplicity and norm | [locLen_quotientWeightPiece_le_one](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/CommutativeAlgebra/GradedModulesLength/LocLenQuotientWeightPieceLeOne.lean#L70-L149), [locLen_aPiece_ideal2_le_two_pow](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/CommutativeAlgebra/GradedModulesLength/LocLenAPieceIdeal2LeTwoPow.lean#L69-L116), [th_holds](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/CommutativeAlgebra/GradedModulesLength/HerbrandFinLen.lean#L189-L260), [up_holds](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/CommutativeAlgebra/GradedModulesLength/TwoSigned.lean#L17-L96) |
| Finite orbit cover and comparison | [fin_holds](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/CommutativeAlgebra/GradedModulesLength/FinHolds.lean#L49-L99), [core_holds](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/CommutativeAlgebra/GradedModulesLength/AlgMemCoef.lean#L92-L144) |

## The graded Euler-characteristic argument

We now prove the algebraic rules used in the Rees calculation. They hold
for admissible lists of homogeneous sections, including nonregular sequences.

**Admissibility and finite lengths.** Let $(B,\mathfrak m)$ be a
Noetherian local ring and $R$ a standard $\mathbf N^k$-graded $B$-algebra:
$R_0$ is the image of $B$, each $R_{e_i}$ is finite over $B$, and
$R_{d+e_i}=R_dR_{e_i}$ for $d\ge0$. All modules below are finitely
generated $\mathbf Z^k$-graded $R$-modules. Put $I_i=(R_{e_i})$ and
$I_{\rm irr}=\prod_i I_i$. The ring $R$ is Noetherian, since it is
generated by finitely many elements from the $R_{e_i}$.

For homogeneous sections $\mathbf s=(s_1,\ldots,s_n)$ of nonnegative
multidegrees $\delta_i$, the pair $(\mathbf s,M)$ is admissible if

$$
 (\mathfrak m R\,I_{\rm irr})^N
 \subseteq\operatorname{Ann}_R M+(s_1,\ldots,s_n)
$$

for some $N$. Write $d\gg0$ for all degrees above a fixed threshold
in the coordinatewise order.

Choose homogeneous generators $u_j$ of degrees $a_j$. The module
$M_d=\sum_j R_{d-a_j}u_j$ is finite over $B$; for $d\gg0$ each coordinate
of $d-a_j$ is at least $N$, so $M_d\subseteq I_{\rm irr}^N M$.
Admissibility of the empty list then implies $\mathfrak m^N M_d=0$,
and hence finite $B$-length. Similarly, $I_{\rm irr}^N M=0$ implies
$M_d=0$ for $d\gg0$.

In the graded Koszul complex $K(\mathbf s;M)$ multiplication by each
$s_i$ is null-homotopic, using exterior multiplication by the
corresponding generator. Its homology is thus annihilated by
$\operatorname{Ann}_R M+(\mathbf s)$ and is finitely generated.
Admissibility makes its graded pieces finite-length for $d\gg0$.
Consequently we may form

$$
 \chi_{\mathbf s}(M;d)=
 \sum_{j=0}^n(-1)^j\operatorname{length}_B H_j(K(\mathbf s;M))_d .
$$

Only the homology pieces, not necessarily the terms of the complex,
have finite length.

**Recursion and additivity.** Use $M(-\delta)_d=M_{d-\delta}$.
The two-term complex on a section $s$ of degree $\delta$ has homology
$M/sM$ in degree zero and $M[s](-\delta)$ in degree one. The spectral
sequence obtained by first taking homology in the $s$ direction of
the Koszul bicomplex on $(s,\mathbf t)$ has these two rows, followed
by Koszul homology for $\mathbf t$. Both pairs are admissible, since
their annihilators contain $\operatorname{Ann}M+(s)$.
Their second-page homology pieces have finite length for $d\gg0$;
the alternating sum is preserved on subsequent pages and equals
that of total homology. Hence

$$
 \chi_{(s,\mathbf t)}(M;d)=
 \chi_{\mathbf t}(M/sM;d)-\chi_{\mathbf t}(M[s](-\delta);d).
$$

Induction identifies this expression with the archive's recursive
Euler characteristic in large degrees. If multiplication by $s$ is
injective the second term vanishes.

A graded short exact sequence $0\to M'\to M\to M''\to0$ gives a short
exact sequence of Koszul complexes and a long exact sequence of
homology. Admissibility passes to $M',M''$ because their annihilators
contain that of $M$. Taking alternating sums of finite lengths gives

$$
 \chi_{\mathbf s}(M;d)=\chi_{\mathbf s}(M';d)+
                       \chi_{\mathbf s}(M'';d)\qquad(d\gg0).
$$

Permuting the exterior generators gives an isomorphic Koszul
complex, proving order independence. Shifting a module shifts
the degree of its homology; replacing a section by one of the
same degree congruent modulo $\operatorname{Ann}M$ leaves the
complex unchanged. These identities hold for the recursive
invariant in its eventual range.

**Positivity.** We prove nonnegativity for $d\gg0$ by induction on the
length of the list; the empty list gives ordinary length. Take a finite
homogeneous prime filtration of $M$ with factors $(R/\mathfrak p)(-\alpha)$.
Such a filtration is obtained by choosing a nonzero homogeneous element with
maximal annihilator among homogeneous elements in the current
quotient. Its annihilator is homogeneous. If homogeneous $u,v$
have product in it and $v$ is outside it, maximality applied to
the element multiplied by $v$ forces $u$ into it. Taking leading homogeneous terms modulo the ideal in a translation-invariant
total order on $\mathbf Z^k$ gives primality.
Continue in successive quotients; the ascending chain condition on $M$
ensures termination.
Each prime in the filtration contains $\operatorname{Ann}M$.

By additivity and shifts it suffices to prove positivity on
$D=R/\mathfrak p$. If $I_{\rm irr}\subseteq\mathfrak p$, the
large graded pieces of $D$ and its Koszul complex vanish.
Otherwise choose $u_i\in R_{e_i}\setminus\mathfrak p$ for every
$i$. For any nonnegative degree $\delta$, their product
$\prod_i u_i^{\delta_i}$ is a section of degree $\delta$ outside
$\mathfrak p$. Let $s$ be the first section, of degree $\delta$.
If $s\notin\mathfrak p$, it acts injectively on $D$ and the
recursion reduces to the shorter list on $D/sD$.
If $s\in\mathfrak p$, the tail $\mathbf t$ is already admissible on $D$.
Choose a section $\sigma$ of the same degree outside $\mathfrak p$ as above.
The exact sequence

$$
 0\to D(-\delta)\xrightarrow{\sigma}D\to D/\sigma D\to0
$$

and additivity give

$$
 \begin{aligned}
 \chi_{(s,\mathbf t)}(D;d)
 &=\chi_{\mathbf t}(D;d)-\chi_{\mathbf t}(D;d-\delta)\\
 &=\chi_{\mathbf t}(D/\sigma D;d).
 \end{aligned}
$$

The right side is nonnegative by induction. In degree zero take $\sigma=1$.
Summing over the filtration, with a threshold large enough to accommodate
all shifts, proves eventual nonnegativity. The construction works over a
finite residue field as well.

**Quotient comparisons.** For a graded quotient $M\twoheadrightarrow Q$
with kernel $L$, additivity and positivity give

$$
 \chi_{\mathbf s}(M;d)-\chi_{\mathbf s}(Q;d)
 =\chi_{\mathbf s}(L;d)\ge0\qquad(d\gg0).
$$

Likewise the recursion and positivity on the shifted kernel give
$\chi_{(s,\mathbf t)}(M;d)\le\chi_{\mathbf t}(M/sM;d)$. Iterating over the
prefix $\mathbf f$ gives

$$
 \chi_{(\mathbf f,\mathbf t)}(M;d)
 \le\chi_{\mathbf t}(M/(\mathbf f)M;d).
$$

At each step the quotient remains admissible for the remaining list.
The sign of the discarded term is justified by positivity.

**Finite differences and products.** When the empty list is
admissible on $M$, all large graded pieces have finite length.
In that range we can take the alternating sum of the terms
of the Koszul complex, rather than its homology. With
$h_M(d)=\operatorname{length}_B M_d$ and
$\Delta_\delta h(d)=h(d)-h(d-\delta)$, we obtain

$$
 \chi_{\mathbf s}(M;d)=
 \Delta_{\delta_1}\cdots\Delta_{\delta_n}h_M(d).
$$

Here admissibility of the empty list is essential.

Let $b,c$ have degrees $\beta,\gamma$ and suppose $(bc,\mathbf t)$
is admissible on $M$. The kernel-cokernel sequence of the
composition of multiplication by $c$ and by $b$ is

$$
 \begin{aligned}
 0&\to M[c](-\beta-\gamma)\to M[bc](-\beta-\gamma)\\
 &\xrightarrow{c} M[b](-\beta)\to (M/cM)(-\beta)\\
 &\xrightarrow{b} M/bcM\to M/bM\to0 .
 \end{aligned}
$$

The unlabelled map is reduction modulo $cM$. All six modules are
annihilated by $bc$ and $\operatorname{Ann}M$, so the tail is admissible
on each. Additivity along the sequence gives the product rule

$$
 \chi_{(bc,\mathbf t)}(M;d)=
 \chi_{(b,\mathbf t)}(M;d)+\chi_{(c,\mathbf t)}(M;d-\beta).
$$

For a degree-zero factor $b$ there is no shift.

**Application to Lemma M.** Return to the leading-term quotient $V$
of the Rees module.
Multiplication by $\varpi$ is injective and the empty list
is admissible on $V/\varpi V$. The first $r$ sections in $V$
are $\varpi^{2b_i}z_i$, where $z_i$ is the section corresponding
to $y_i^2$, of multidegree $e_0=(1,0,0)$. For an exponent
$n_i\ge0$, the degree-zero product rule and regularity of
$\varpi$ give

$$
 \begin{aligned}
 \chi_{(\varpi^{n_i}z_i,\mathbf u)}(V;d)
 ={}& n_i\chi_{\mathbf u}(V/\varpi V;d)\\
 &+\chi_{(z_i,\mathbf u)}(V;d).
 \end{aligned}
$$

Here $\mathbf u$ is the rest of the list. Removing a scalar factor
enlarges the equation ideal, preserving admissibility. The finite-difference
formula shows that the first term depends only on the degrees of $\mathbf u$.
Thus we may extract the scalar factors in succession and apply positivity
to the final list. Taking $n_i=2b_i$ gives

$$
 \chi_{\mathbf f}(V;d)\ge
 \left(\sum_{i=1}^r2b_i\right)
 \Delta_{e_0}^{r-1+s}\Delta_{e_1}^{r'+s'}
             \Delta_{e_2}h_{V/\varpi V}(d).
$$

The generating-function calculation evaluates the final factor to
$2^{r-1+r'}$. The leading-term ideal contains the chart kernel and the
degree-zero element $a$ vanishing at $x$, so $U/aU$ surjects onto $V$.
Monotonicity transfers the lower bound to $U/aU$. For the upper comparison,
use regularity of $a$ on $U$, order independence and the quotient inequality:

$$
 \begin{aligned}
 \chi_{\mathbf f}(U/aU;d)
 &=\chi_{(a,\mathbf f)}(U;d)\\
 &=\chi_{(\mathbf f,a)}(U;d)\\
 &\le\chi_{(a)}(U/(\mathbf f)U;d).
 \end{aligned}
$$

It remains to specify the geometric admissibility input. In the archive,
the radical inclusion for the Rees sections together with $a$ is proved
by considering primes containing the chart-kernel and section ideals.
For a prime outside the irrelevant locus, the weight-zero contraction is
either the maximal ideal or the kernel of a characteristic-zero point.
In the latter case it contains the weight-zero equation ideal. If a product
of elements of weights $-2$ and $2$ is nonzero at the point, the lifting
theorem gives a two-sided point of the equation scheme. Since $a$ vanishes
there, this contradicts M5. All such products must therefore vanish,
and the one-sided support comparison forces the prime to contain the
extended maximal ideal. Finite generation turns the radical inclusion
into a power inclusion, as required for admissibility. These support
and lifting results are the geometric inputs to the Euler argument.

| Step | Archive reference |
| --- | --- |
| Grading, admissibility and recursion | [Std, admitted, chi](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SharpRestriction/ValuationFrobeniusEpsilon/LeastPrimeTwists/QuotientShiftIrreducible/NoetherianQuotientCalc/EulerVanishingBelowDimension.lean#L66-L119), [ruleFin](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SharpRestriction/ValuationFrobeniusEpsilon/LeastPrimeTwists/QuotientShiftIrreducible/NoetherianQuotientCalc/RuleFin.lean#L345-L365), [ruleIrr](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SharpRestriction/ValuationFrobeniusEpsilon/LeastPrimeTwists/QuotientShiftIrreducible/NoetherianQuotientCalc/RuleIrr.lean#L9-L22) |
| Additivity, order and regular sections | [euler_additivity_of_rules](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SharpRestriction/ValuationFrobeniusEpsilon/LeastPrimeTwists/QuotientShiftIrreducible/NoetherianQuotientCalc/EulerAdditivityExactSequence.lean#L378-L428), [EulerIndependenceOfOrder](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SharpRestriction/ValuationFrobeniusEpsilon/LeastPrimeTwists/QuotientShiftIrreducible/NoetherianQuotientCalc/EulerIndependenceOfOrder.lean#L580-L621), [ruleNzd](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SharpRestriction/ValuationFrobeniusEpsilon/LeastPrimeTwists/QuotientShiftIrreducible/NoetherianQuotientCalc/RuleNzd.lean#L29-L42) |
| Homogeneous prime filtration and replacement | [ruleDev](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SharpRestriction/ValuationFrobeniusEpsilon/LeastPrimeTwists/QuotientShiftIrreducible/NoetherianQuotientCalc/RuleDev.lean#L352-L372), [exists_sec](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SharpRestriction/ValuationFrobeniusEpsilon/LeastPrimeTwists/QuotientShiftIrreducible/NoetherianQuotientCalc/VanishingBelowDimensionRule.lean#L177-L198), [dev_reduce, prime_step](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SharpRestriction/ValuationFrobeniusEpsilon/LeastPrimeTwists/QuotientShiftIrreducible/NoetherianQuotientCalc/VanishingBelowDimensionRule.lean#L260-L337), [rulePos](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SharpRestriction/ValuationFrobeniusEpsilon/LeastPrimeTwists/QuotientShiftIrreducible/NoetherianQuotientCalc/RulePos.lean#L22-L48) |
| Quotient inequalities | [ruleMono](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SharpRestriction/ValuationFrobeniusEpsilon/LeastPrimeTwists/QuotientShiftIrreducible/NoetherianQuotientCalc/RuleMono.lean#L11-L25), [ruleUB](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SharpRestriction/ValuationFrobeniusEpsilon/LeastPrimeTwists/QuotientShiftIrreducible/NoetherianQuotientCalc/RuleUB.lean#L20-L45) |
| Differences and products | [ruleSmall](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SharpRestriction/ValuationFrobeniusEpsilon/LeastPrimeTwists/QuotientShiftIrreducible/NoetherianQuotientCalc/RuleSmall.lean#L124-L141), [euler_rule_product_zero](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SharpRestriction/ValuationFrobeniusEpsilon/LeastPrimeTwists/QuotientShiftIrreducible/NoetherianQuotientCalc/EulerRuleProductZero.lean#L17-L69) |
| Rees application | [admissibility_holds](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/CommutativeAlgebra/GradedModulesLength/AdmissibilityHolds.lean#L30-L78), [la_peel, la_holds](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/CommutativeAlgebra/GradedModulesLength/LaDifPerm.lean#L49-L125), [low_holds](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/CommutativeAlgebra/GradedModulesLength/AdmissibleMonoIdeal.lean#L191-L323), [core_holds](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/CommutativeAlgebra/GradedModulesLength/AlgMemCoef.lean#L92-L144) |

