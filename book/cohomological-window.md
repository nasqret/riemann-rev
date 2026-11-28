# From tower bounds to the cohomological window

Starting from the tower estimates of {ref}`comp-cohomology`, we derive a bound for
the weighted sum of cohomological lengths over an arbitrary finite set of coefficient primes.
The argument combines exceptional-twist estimates with automorphic counts; the commutative
algebra used in Case I is treated in {doc}`deformation-length`.

## Uniform bounds for the twist sum

The first tower estimate controls all but finitely many twists. On the exceptional set,
we use the second estimate, which reduces the problem to a fixed reference layer where
Lemma K applies. The window is chosen so that the resulting bound remains small enough.

**Pointwise estimates.** Write $L_m/L_0$ for a layer of degree $\ell^m$,
$j=\operatorname{NatLog}_\ell(R)+3$ (the integer logarithm is zero at $R=0$),
and $s(h,m)=s_{\ell,h}(L_m)$. For every integer $Z\ge1$ there is an
exceptional set $T_Z\subset\{1,\ldots,Z\}$ of cardinality $|T_Z|\le R$ such that

$$
\begin{aligned}
 s(h,m)&\le R(\max(m,j)+c+\lfloor\log_\ell Z\rfloor)
                  &&(h\notin T_Z,\ 1\le h\le Z),\\
 s(h,m)&\le v(h,j)+R(m-j)_+
                  &&(h\ge1).
\end{aligned}
$$

Here $v(h,j)=\operatorname{length}_{\mathbf Z_\ell}H^2(G_{L_j,S},\mathbf Z_\ell(h+1))$,
with $S$ the places over $\ell$, and $(m-j)_+=\max(m-j,0)$.
The integer $c$ is supplied by the centres estimate, with a primitive
$\ell^c$-th root of unity in $L_0$.

Suppose $L_0$ contains a primitive $\ell$-th root for odd $\ell$, or a primitive
fourth root for $\ell=2$. Then the reference layer $L_j$ is totally imaginary and
inherits the required roots. Let $n=[L_j:\mathbf Q]$ and $D=|\operatorname{disc}L_j|$.
Lemma K, with constant $C_K>0$, gives finiteness of the group defining
$v(h,j)$ and

$$
 v(h,j)\log\ell
 \le \exp\big((2hn)^{C_K}\log(2D)\big).
$$

Here we use the fact that a finite $\mathbf Z_\ell$-module of length $v$
has order $\ell^v$. Since $\log\ell>1/2$, division by $\log\ell$ costs a
factor of at most $2$.

Fix $0<\varepsilon<1/52$, $X>1$ and $C_t\ge1$. Take $Z=\lfloor X^{C_t}\rfloor$
and $\eta=\varepsilon/(2C_K)$. Suppose $1\le x\le X$ lies in the window
associated with $T_Z$ and that

$$
 n\le n_0,\qquad
 \log(2D)\le c_0x^{\varepsilon/4},\qquad
 m\le a(1+\log x).
$$

If $1\le h\le x^{C_t}$ is exceptional, the window condition gives
$h\le x^\eta$. Consequently

$$
 (2hn)^{C_K}\log(2D)
 \le (2n_0)^{C_K}c_0 x^{3\varepsilon/4}.
$$

The twist contributes $\varepsilon/2$ to the exponent and the discriminant
contributes $\varepsilon/4$. For nonexceptional $h\le x^{C_t}$ we have $h\le Z$,
so the first tower estimate applies. Thus all lengths in the indicated range
are finite and satisfy

$$
 s(h,m)\le R(m+j+c+\lfloor\log_\ell Z\rfloor)
          +2\exp\big(B_0x^{3\varepsilon/4}\big),
 \qquad B_0=(2n_0)^{C_K}c_0.
$$

**The sum over twists.** The lower endpoint $X^{1/J}\le x$ gives
$\log X\le J\log x$. Since $\log\ell>1/2$,

$$
 \lfloor\log_\ell Z\rfloor\le 2C_tJ\log x.
$$

For a uniform bound $c\le c_1$, take
$C=R(a+j+c_1+2C_tJ)+1+B_0$. The preceding inequality implies

$$
 s(h,m)+1\le C(1+\log x)+2\exp(Cx^{3\varepsilon/4}).
$$

The extra unit accounts for the two-adic field comparison. For an integer
cutoff $t(x)\le x^{C_t}$, multiply the bound by $x^{C_t}$. The logarithm of
the resulting bound is $O(\log x+x^{3\varepsilon/4})=o(x^{4\varepsilon/5})$.
With the parameters fixed, we therefore have, for all sufficiently large $x$,

$$
 \sum_{1\le h<t(x)}(s(h,m)+1)\le \exp(x^{4\varepsilon/5}).
$$

The margin $4\varepsilon/5-3\varepsilon/4=\varepsilon/20>0$ absorbs the
constants as well as the number of twists.

**Uniformity in the auxiliary primes.** At each odd prime in the fixed
auxiliary set the reference field is fixed. At $\ell=2$, however, the base
field varies with $q,d$: its degree is bounded by $8\deg M$ and it embeds
in $\mathbf Q(\zeta_{4m_Mqd})$, where $m_M$ is the fixed conductor parameter
of the abelian field $M$. Uniformity follows from a conductor calculation.

More generally, suppose
$L_0\subset\mathbf Q(\zeta_{N_0P})$, $[L_0:\mathbf Q]\le n_1$,
where $P$ varies. The layer $L_j$ is generated over $L_0$ by roots of
unity of order $\ell^k$ for some $k$. It embeds in
$\mathbf Q(\zeta_{\ell^kN_0P})$. Since $\varphi(\ell^k)\ge \ell^k/2$
and $L_j$ contains these roots,

$$
 [L_j:\mathbf Q]\le n_1\ell^j,\qquad
 \ell^k\le 2[L_j:\mathbf Q].
$$

For any subfield $E$ of $\mathbf Q(\zeta_N)$ the discriminant tower formula
and the cyclotomic discriminant formula give
$|\operatorname{disc}E|\le N^{[E:\mathbf Q]}$: the absolute norm of the
relative different is at least one, and the cyclotomic discriminant has
absolute value at most $N^{\varphi(N)}$. Taking
$n_0=(n_1+1)\ell^j$, it follows that

$$
 \log(2|\operatorname{disc}L_j|)
 \le \log 2+n_0\log(2n_0N_0)+n_0\log P.
$$

In the two-adic application $P=qd$, $N_0=4m_M$, and the auxiliary-prime
hypothesis gives $\log P\le X^{\varepsilon/(4J)}\le x^{\varepsilon/4}$.
Since $x\ge1$, the constant term can also be absorbed into $c_0x^{\varepsilon/4}$.
Both $c_0$ and $n_0$ are independent of $q,d$. The same totient inequality
in $L_0$ bounds $c$: $2^c\le2[L_0:\mathbf Q]\le16\deg M$,
so in particular $c\le16\deg M$. The moving layer satisfies $m\le e(x)+2$. For $x\ge2$ the bounds in PageN
give $2^{e(x)}\le 2x^{2+8\varepsilon}\le x^{3+8\varepsilon}$.
Taking $A_1=3+8\varepsilon$ gives $m\le(2|A_1|+2)(1+\log x)$, since
$\log 2>1/2$. The two-adic comparison now transfers the estimate to the
desired field, at a cost of at most one unit of length per twist.

To obtain a single window, choose a rank bound for the moving two-adic
tower uniformly in $q,d$, and fix the ranks of the odd-prime towers.
Their sum $R_*$ bounds the cardinality of the union of the exceptional
sets; take $J=4(2C_t/\eta)^{R_*}$. Enlarge the finitely many pointwise
thresholds to a common $x_1\ge1$ before choosing $X,q,d$. If
$X\ge\max(2,x_1^J)$, the entire window lies above every threshold.
Although the exceptional sets depend on $X$ and on the moving field,
the interval is chosen after their union is formed. All the tower
estimates therefore hold on the same interval.

| Step | Archive reference |
| --- | --- |
| Two estimates and the prime-dependent base-field contracts | [SecondBound, ABound, FirstBound, TwoBase, TwoIn](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/LayeredIsomorphisms/SecondBound.lean#L11-L50) |
| Extraction of a finite exceptional set | [exc](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/LayeredIsomorphisms/Exc.lean#L8-L41) |
| Finiteness and conversion of Lemma K to a length bound | [klen](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/LayeredIsomorphisms/Klen.lean#L24-L46) |
| Exponent budget and the two cases | [kexp](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/LayeredIsomorphisms/Kexp.lean#L8-L37), [point](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/LayeredIsomorphisms/ImportsAlt.lean#L9-L61) |
| Fixed constant and the sum over twists | [point2](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/LayeredIsomorphisms/Point2.lean#L8-L49), [final](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/LayeredIsomorphisms/Final.lean#L8-L68), [vvat](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/LayeredIsomorphisms/Vvat.lean#L8-L21) |
| Uniform conductor and discriminant estimates | [rootdeg](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/LayeredIsomorphisms/Rootdeg.lean#L8-L27), [layeremb](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/LayeredIsomorphisms/Layeremb.lean#L8-L35), [disc](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/LayeredIsomorphisms/Imports.lean#L8-L45), [layerdisc](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/LayeredIsomorphisms/Layerdisc.lean#L9-L71) |
| Moving two-adic and fixed odd-prime towers | [partA](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/LayeredIsomorphisms/PartA.lean#L24-L78), [partB](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/LayeredIsomorphisms/PartB.lean#L50-L95) |
| Choice of ranks, common threshold and common window | [thmBab_of](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/LayeredIsomorphisms/ThmBabOf.lean#L11-L103) |

## Case I: a common integer for the coefficient primes

In Case I a nonzero integer attached to a character kernel controls its
contribution at every coefficient prime except the auxiliary prime used in
the integer's construction. Two auxiliary primes suffice to cover all cases.

**The trace difference.** Fix an imaginary quadratic field $K$, a level
$N$, a twist $h\ge1$, and a rational prime $p\nmid30N|\operatorname{disc}K|$.
Choose a place $w$ above $p$ and let $q_w=|\kappa(w)|=p^f$, where $f\le2$.
The archive uses inverse arithmetic Frobenius. The reference trace for a
character $\psi$ is the trace of the reducible representation with diagonal
characters $\Psi,1,\Psi^{-1}$, where $\Psi=\chi_\ell^h\psi$ and
$\chi_\ell$ is the cyclotomic character. At inverse Frobenius it becomes
the complex number

$$
 E(z)=q_w^{-h}z+1+q_w^hz^{-1},
 \qquad z=\psi(q_w)^{-1}.
$$

The admissible representations arise either from the rank-three unitary family
or from rank-two descent, realized in dimension three. The automorphic count
supplies a finite set $D$ of eigensystems, each with a trace $t_d$, satisfying
three properties:

- $|t_d|\le3$ and $q_w^ht_d$ is an algebraic integer.
- Complex field automorphisms permute the labels compatibly with their
  traces.
- For every odd coefficient prime $\ell\ne p$, the admissible
  representations can be classified by labels in $D$, with matching
  inverse Frobenius traces under the chosen field isomorphism to
  $\mathbf C$. Equality of labels implies isomorphism of representations.

The indexing by eigensystems is essential: different representations can have
the same trace at $w$.

Put $Q_w=q_w^h\ge7$. Since $z$ is a root of unity, the cleared difference

$$
 A(z,d)=Q_w(t_d-E(z))
       =Q_wt_d-z-Q_w-Q_w^2z^{-1}
$$

is an algebraic integer. It is nonzero, because
$|Q_wt_d-z-Q_w|\le4Q_w+1<Q_w^2$. The same triangle inequality gives
$|A(z,d)|\le2Q_w^2$, hence

$$
 \log|A(z,d)|\le2h\log q_w+1.
$$

**An integral product.** Let $G=(\mathbf Z/N\mathbf Z)^\times$, and let
$H'$ be a subgroup occurring as the kernel of a character of $G$.
Write $\mathcal C_{H'}$ for all complex characters with exactly that
kernel. If $m=[G:H']$, the quotient is cyclic of order $m$, and
$|\mathcal C_{H'}|=\varphi(m)$: its faithful characters are obtained by
sending a generator to each primitive $m$-th root of unity. Form

$$
 I_{H',p}=
 \prod_{\psi\in\mathcal C_{H'}}\prod_{d\in D}
          A(\psi(q_w)^{-1},d).
$$

The factors are nonzero algebraic integers, and Galois automorphisms permute
them, preserving character kernels and the index set $D$. Indeed one may
work in a finite normal field containing the factors, extending its
automorphisms to $\mathbf C$. Hence $I_{H',p}\in\mathbf Z\setminus\{0\}$
(with the empty product equal to $1$), and the archimedean estimate gives

$$
 \log|I_{H',p}|
 \le\varphi(m)|D|(2h\log q_w+1).
$$

Take the disjoint union of the rank-three and rank-two trace data. Write $\Delta=|\operatorname{disc}K|$
and $Y=N(h+1)$. The first set has cardinality at most $c_1Y^{A_1}$;
the second is counted at level $N\Delta$ and has cardinality at most
$c_2(\Delta Y)^{A_2}$. Thus $|D|\le(c_1+c_2\Delta^{A_2})Y^{A_1+A_2}$.
Since $\log q_w\le2\log p$ and $\log p\ge1$,

$$
 2h\log q_w+1\le 5Y\log p .
$$

With $c_K=5(c_1+c_2\Delta^{A_2})$ and $A_K=A_1+A_2+1$, we obtain

$$
 \log|I_{H',p}|
 \le c_K\varphi(m)(N(h+1))^{A_K}\log p,
$$

The constants depend only on $K$. For the rank-three count the inverse
cyclotomic twist shifts the weights from $(h,0,-h)$ to $(h-1,-1,-h-1)$,
after which the traces are transported back to inverse Frobenius. The
rank-two count uses descent at level $N\Delta$. Both counts refer to
the specified admissibility and level conditions; existence, classification
and cardinality of the eigensystems are the automorphic inputs.

**From the integral product to a local length.** Fix an odd $\ell\ne p$
and a coefficient ring as in the character reduction. Under the chosen
embedding into $\mathbf C$, a nonempty family of characters with kernel
$H'$ identifies with $\mathcal C_{H'}$: all faithful characters of the
cyclic quotient are coprime powers of any one of them. No roots of unity
of unrelated orders are needed. These powers preserve the order, parity,
quadratic local component and kernel after removing the local component.
Thus the character conditions in GD hold for the entire family if they
hold for one member; the field, level, prime and twist are unchanged.

For each such $\psi$, the one-character estimate gives finiteness and a
set $X_\psi$ of pairwise nonisomorphic admissible representations such that

$$
 v_\ell(\psi,h)
 \le 2\sum_{\rho\in X_\psi}
             v_\ell(\operatorname{tr}\rho(\operatorname{Frob}_w^{-1})
                         -E_\psi).
$$

Here $E_\psi$ is the reference trace in the coefficient field and
$v_\ell(\ell)=1$. The proof compares the character cohomology with the
cotangent lattice of a graded deformation model and applies Lemma M
to the trace difference (see {doc}`deformation-length`). This element has
weight zero, vanishes at the reducible base point and is nonzero at
the two-sided points by the trace estimate. Rigidity and automorphy
identify their specializations with the two admissible families.
Isomorphic restrictions to $G_K$ lie in the same grading-torus orbit,
so distinct orbit representatives give distinct representation classes.
The passage to unramified coefficients uses the prime-to-$\ell$ order
of $\psi$ and invariance of normalized length under coefficient extension.

For each $\psi$, the set $X_\psi$ injects into $D$. Since $Q_w$ is an
$\ell$-adic unit, clearing the denominator leaves valuations unchanged;
all the cleared differences are integral. Consequently

$$
 \sum_{\psi}\sum_{\rho\in X_\psi}
 v_\ell(\operatorname{tr}\rho(\operatorname{Frob}_w^{-1})-E_\psi)
 \le v_\ell(I_{H',p}).
$$

The product is indexed by pairs, so an injection for each character suffices.
The sum of normalized lengths over the kernel family is at most
$2v_\ell(I_{H',p})$.

**Two auxiliary primes.** The preceding argument cannot use the prime
$p$ as its own coefficient prime. Choose distinct auxiliary primes
$p,p'$ satisfying the same coprimality requirements. For any finite
set $S$ of relevant odd coefficient primes, the one-character finiteness
statement and the valuation bound at each $\ell$ follow from the
integer for $p$ if $\ell\ne p$, and from the integer for $p'$ otherwise.
By unique factorization,

$$
 \sum_{\ell\in S}v_\ell(I)\log\ell\le\log|I|
 \qquad(I\in\mathbf Z\setminus\{0\}).
$$

It follows that, for the primes in which the kernel family contains
a GD character,

$$
 \sum_{\ell\in S}\log\ell
          \sum_{\ker\psi=H'}v_\ell(\psi,h)
 \le 2c_K\varphi([G:H'])(N(h+1))^{A_K}
                    (\log p+\log p').
$$

The bound is independent of the finite set $S$.

**Application to Case I.** In Case I the quadratic field is fixed
as $K=\mathbf Q(\sqrt{-p_K})$ by the original character $\chi$.
The conditions outside $B_\chi$ ensure $\ell$ is prime to the
character order and to the discriminant and class number of $K$.
The field cut out by the residual cyclotomic character together
with the local-component-removed character is unramified at $p_K$,
whereas $K$ is ramified there. Thus it cannot contain $K$, giving
the remaining disjointness condition of GD. The other GD conditions
are the host parity, the local quadratic-component condition,
even level and $\ell-1\nmid2h$.

Choose the two auxiliary primes larger than $30Qp_K$, with $Q$ the
original conductor, and require the moving primes $q,d$ to exceed
both. Since $N=\operatorname{lcm}(2^{e(x)+2},Q)qd$, neither auxiliary
prime divides $30N|\operatorname{disc}K|$. They may therefore be
fixed before the host is chosen.

Let $\mathcal H$ be the distinct character kernels occurring among
the chosen coefficient primes. Each quotient $G/H'$ for
$H'\in\mathcal H$ is cyclic. The sets of complex characters with
these kernels are disjoint, and the character group of $G$ has
order $|G|$. Hence

$$
 \sum_{H'\in\mathcal H}\varphi([G:H'])
 \le |G|=\varphi(N)\le N.
$$

Summing the joint bound over kernels gives at most
$A_0N(N(h+1))^{A_K}$, where
$A_0=2c_K(\log p+\log p')$ is fixed. Since $h+1\le t$ and $N\ge16$,
choose an integer $k\ge0$ with $A_0\le16^k$. The sum is then at most
$(Nt)^{k+1+A_K}$, giving the joint bound of Case I, with all character lengths finite.

| Step | Archive reference |
| --- | --- |
| Construction of the counting data and constants | [numberU3U_of_adm2A_imp_adm2B, numberU3U_of_prints](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/KeepNumU.lean#L25-L80), [rank-two and rank-three trace counts](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/FrobeniusTraceCountBoundOfCmEigensystemCount.lean#L348-L466) |
| Actual counting and one-character interfaces | [NumberU3U_s, OneCharU_s](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/NumberU3US.lean#L27-L59) |
| Cleared trace difference and the integer product | [eisenstein_trace_difference_log_bound](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/BuildingsResidueChars/EisensteinTraceDifferenceLogBound.lean#L4-L61), [frobenius_trace_norm_nonzero_log_bound](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/BuildingsResidueChars/FrobeniusTraceNormNonzeroLogBound.lean#L7-L58) |
| Integral Galois-invariant product and the injection of label sets | [exists_int_eq_prod_of_galois_permuted_integral](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/BuildingsResidueChars/ExistsIntEqProdOfGaloisPermutedIntegral.lean#L6-L22), [adicNorm_prod_le_prod_of_injective_classes](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/BuildingsResidueChars/AdicNormProdLeProdOfInjectiveClasses.lean#L5-L20) |
| Cotangent comparison and one-character reduction | [vlen_le](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/UnitaryThreeGroups/VlenLe.lean#L47-L68), [model_upper](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/UnitaryThreeGroups/ModelUpper.lean#L112-L251), [oneChar_unramU and its coefficient descent](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/FOneCharU.lean#L19-L96) |
| Transport to the kernel family and the common integer | [propGK_of_numberU3U_of_oneCharU](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/FPropGKU.lean#L110-L173), [gdFacts](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/HeightAndVanishing/GdFacts.lean#L29-L102) |
| Two-prime argument | [corGK](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/UnitaryThreeGroups/CorGSumLog.lean#L8-L74) |
| Host hypotheses and the sum over kernels | [gdOfHost](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/HeightAndVanishing/GdOfHost.lean#L37-L95), [orbSum](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/HeightAndVanishing/OrbSum.lean#L44-L59), [countI](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/UnitaryThreeGroups/CountI.lean#L25-L137) |
| The actual call to these results | [count_i_of_printed_bound_k_kato_automorphy](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/LinkedUnlE.lean#L49-L54) |

## From character counts to the sum over all coefficient primes

The tower argument controls the prime $2$ on the moving field and the odd
primes in $B_\chi$ on their reference layers. We now estimate the odd-prime
contribution on the moving field itself.

**Character reduction and the cases.** Fix the primitive character $\chi$,
of conductor $Q$ and order $o$. In the following argument $N$ is the host
conductor, $t\ge2$ is the twist cutoff and $M=Nt$. The fixed set $B_\chi$ consists of $3$ and the odd prime factors of $oQp_K h_*p_1$, where $p_K,h_*,p_1$ are the fixed auxiliary
quantities in the definition of [Bchi](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/StmtFields.lean#L54-L67). Assume the host size hypotheses throughout,
including the lower bounds on $q,d$ relative to $t$ and the fixed auxiliary
quantities. Let $c$ be the action of complex conjugation on the locally trivial
cohomology of the moving CM field at twist $h$. The positive and negative parts are respectively the $(-1)^h$- and
$(-1)^{h+1}$-eigenspaces of $c$. Write $a_\ell(h)$ for the length of the
positive part, allowing infinite lengths at this stage.

Let $H$ be the host subgroup of $(\mathbf Z/N\mathbf Z)^\times$.
At each odd $\ell$ choose a coefficient discrete valuation ring $O$
finite over $\mathbf Z_\ell$ and containing the character values. Let $X_h$
be the characters of $(\mathbf Z/N\mathbf Z)^\times$ trivial on $H$ with
$\psi(-1)=(-1)^h$. Write $v_\ell(\psi,h)$ for the character length Vlen
divided by the ramification index of $O/\mathbf Z_\ell$ (the normalized
length Vn). The character reduction inequalities, expressed in extended
lengths, are

$$
 a_\ell(h)\le
 \begin{cases}
 \displaystyle\sum_{\psi\in X_h}v_\ell(\psi,h),&\ell\notin B_\chi,\\[4pt]
 \displaystyle\sum_{\psi\in X_h}
       (v_\ell(\psi,h)+\lambda_\ell(N,h)),&\ell\in B_\chi,
 \end{cases}
$$

where $\lambda_\ell(N,h)=\operatorname{lossAll}(\ell,N,[G:H],h)$
with $G=(\mathbf Z/N\mathbf Z)^\times$. In particular, finiteness of the
character lengths implies finiteness of $a_\ell(h)$. The first inequality
uses $\ell\nmid[G:H]$, a consequence of the host size conditions outside
$B_\chi$; the second accounts for the loss in integral character decomposition
when the index is divisible by $\ell$. We use $\lambda_\ell(N,h)\le(Nh)^6$.
Both $X_h$ and the union $X_0\cup X_1$ of the two parity families contain
at most $N$ characters.

The counting estimates divide into the following cases. The notation $\chi_\ell'(\psi)$
denotes its prime-to-$\ell$, local-component-removed character chiP;
$R_1$ and $c_2$ are the conductor quantities in Case V.

| Coefficient prime | Twist and character condition | Bound used |
| --- | --- | --- |
| Outside $B_\chi$ | $\ell-1\nmid2h$ | I |
| Outside $B_\chi$ | $\ell-1\mid2h$, $\psi=1$ | Z |
| Outside $B_\chi$ | $\ell-1\mid2h$, $\psi$ of even order | II |
| Outside $B_\chi$ | $\ell-1\mid2h$, $\psi\ne1$ of odd order | III |
| Inside $B_\chi$ | $h\ge2$, $\chi_\ell'(\psi)$ of even order | II |
| Inside $B_\chi$ | $h\ge2$, $\chi_\ell'(\psi)$ of odd order | IV |
| Inside $B_\chi$ | $h=1$, $R_1\le2^{c_2}$ | V |
| Inside $B_\chi$ | $h=1$, $R_1>2^{c_2}$ | Vs |

Outside $B_\chi$ we have $\chi_\ell'(\psi)=\psi$ when $\ell-1\mid2h$.
The table gives a covering by cases, not necessarily a partition of the
counting predicates. In particular the Case IV estimate sums over all twists
of a character of the indicated odd order. We derive IV and Vs below
from the reference-layer and bounded-degree estimates.

**Primes outside $B_\chi$.** Let $S$ be any finite set of odd primes
outside $B_\chi$. Fix $1\le h<t$. On the subset with $\ell-1\nmid2h$,
Case I bounds the entire weighted sum by $M^{C_1}$, with $C_1$ independent
of $S$ and $h$. Its two auxiliary primes are fixed in terms of $\chi$
before the host is chosen.

For the remaining primes, $\ell-1\mid2h$ implies $\ell\le 2t$.
Set $K=\max(C_Z,C_{II},C_{III})$. The corresponding pointwise bounds
include finiteness and give

$$
 v_\ell(\psi,h)\log\ell\le(\ell Nh)^K\le M^{3K},
$$

since $\ell Nh\le 2tM\le M^3$ for $t\le M$ and $M\ge2$.
Each prime contributes at most $NM^{3K}$, and there are at most $2t$
such primes. Thus

$$
 \sum_{\ell\in S}\log\ell\sum_{1\le h<t}a_\ell(h)
 \le t(M^{C_1}+2M^{3K+1})
 \le M^{C_1+3K+4}.
$$

The last inequality follows from $t\le M$ and $M\ge2$. The same case
division gives finiteness, uniformly for arbitrary $S$.

**Primes inside $B_\chi$.** Fix $\ell\in B_\chi$ and suppose that its
reference-layer twist sum is at most $B\ge0$, including finiteness.
Let $K'=\max(C_{II},C_V,C_{Vs})$. Since $\ell\le N$ by the host's size
conditions, the three pointwise counts give $v_\ell(\psi,h)\log\ell\le M^{2K'}$
whenever their respective cases apply.

Collect the characters of the indicated odd order in the set
$\mathcal O=\bigcup_{1\le h<t}\{\psi\in X_h:\operatorname{ord}\chi_\ell'(\psi)\text{ is odd}\}$.
The arithmetic of the host shows that
these characters have conductor dividing $Q$, so $|\mathcal O|\le Q$,
not merely $Nt$. Case IV gives a bound on the whole twist sum for each
such character:

$$
 \sum_{1\le h<t}v_\ell(\psi,h)\le B+M^{C_4}.
$$

To retain a constant coefficient of $B$, sum first over twists and then
over characters. By nonnegativity,

$$
 \log\ell\sum_{1\le h<t}\sum_{\psi\in X_h}v_\ell(\psi,h)
 \le Q\log\ell(B+M^{C_4})+tN M^{2K'}.
$$

Indeed the terms in $\mathcal O$ are bounded by their complete twist
sums, and there are at most $N$ of the other terms at each twist.
The character-reduction loss adds at most
$(\log\ell)Nt M^6\le M^8$. Consequently

$$
 \sum_{1\le h<t}\log\ell\, a_\ell(h)
 \le M^{C_\ell}+C_\ell B,\qquad
 C_\ell=C_4+2K'+9+\ell Q.
$$

Indeed $Q\log\ell\le\ell Q\le C_\ell$, and the three other terms
are bounded by $M^{C_4+2}$, $M^{2K'+1}$ and $M^8$. Their sum is at
most $M^{C_\ell}$ because $M\ge3$ and each exponent is at most
$C_\ell-1$. The factor multiplying the tower budget now depends
only on $\chi$, $\ell$ and the fixed reference layer.

**The reference-layer and bounded-degree estimates (IV and Vs).** Case IV uses the fixed field
$L_j$ above $\mathbf Q(\zeta_{\ell Q})$. It is Galois over $\mathbf Q$,
contains the field cut out by $\psi$, and has degree at most
$n_4=\ell Q\ell^j$. Character transport from that field gives
$v_\ell(\psi,h)\le s_{\ell,h}(L_j)+n_4\nu_\ell(N,h)$, with
$\nu_\ell(N,h)\le2Nh$. The reference-layer hypothesis bounds the sum
of the first terms by $B$. The second terms sum to at most
$2n_4Nt^2\le(Nt)^{n_4+3}$. This gives Case IV with $C_4=n_4+3$,
including finiteness. Here we use the character transport theorem as an arithmetic input.

In Vs, the strict reverse conductor threshold and $h=1$ allow a different
field $L$, containing the character field and $\ell$-th roots of unity,
of degree at most $n_0(\chi)$, embedded in
$\mathbf Q(\zeta_{\ell N})$. The degree bound uses the character-order
estimate vsOrd; the field construction is vsField. By the discriminant
inequality above,
$\log|\operatorname{disc}L|\le n_0\log(\ell N)$.
Increase the Lemma K exponent to a nonnegative integer $k$. At twist
one its exponential expression is bounded by the polynomial

$$
 \exp((2[L:\mathbf Q])^k\log(2|\operatorname{disc}L|))
 \le(\ell N)^{A},\qquad A=(2n_0)^k(n_0+1).
$$

Here $\ell N\ge2$. Duality and character transport then give a finite
normalized length at most $2(\ell N)^A+2n_0N$. Multiplication by
$\log\ell\le\ell$ yields a polynomial bound, for example
$(\ell N)^{A+n_0+3}$. This gives the uniform bound in Vs, since the degree is bounded and
the twist is one.

**The positive part on the common interval.** Combine the outside bound
$M^{C_0}$ with the inside bounds. Write $b=|B_\chi|$ and
$D=\sum_{\ell\in B_\chi}C_\ell$. For every finite set of odd primes the
positive-part sum is at most

$$
 M^{C_0}+bM^D+bDB\le M^C+CB,
 \qquad C=C_0+D+b+bD.
$$

Indeed $b+1\le2^b\le M^b$ and $bD\le C$. The exponents and the
two auxiliary primes from CountI are fixed before the host. In the
tower window take $B=\exp(x^{4\varepsilon/5})$.
The host conductor is the conductor of the moving field (hostCond);
hence $M=(\operatorname{cond}E)t(x)$. The positive-part estimate holds on the interval already selected by
the tower argument; no further window selection is needed.

| Step | Archive reference |
| --- | --- |
| Counting hypotheses and exhaustive case division | [Counts](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/HeightAndVanishing/Counts.lean#L53-L73), [cases](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/HeightAndVanishing/Cases.lean#L8-L48), [bchiFacts](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/HeightAndVanishing/BchiFacts.lean#L8-L101) |
| Integral character reduction and its loss | [redPrime](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/HeightAndVanishing/RedPrime.lean#L11-L57), [redAll](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/HeightAndVanishing/RedAll.lean#L6-L21), [lossLe](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/HeightAndVanishing/LossLe.lean#L8-L54) |
| Sum outside the fixed set | [sumOut](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/HeightAndVanishing/SumOut.lean#L50-L231) |
| Normalization and finiteness of character reduction | [nrm, SumLe](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/CharacterLevelBounds/ShaFamMono.lean#L71-L78), [sumBack](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/CharacterLevelBounds/SumBack.lean#L7-L59) |
| Character conductor and fixed-layer estimate | [hostOdd](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/HeightAndVanishing/HostOdd.lean#L1-L111), [countIV](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/HeightAndVanishing/CountIV.lean#L39-L89) |
| Fields for the two exceptional character estimates | [ivField](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/HeightAndVanishing/IvField.lean#L32-L82), [vsOrd](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/HeightAndVanishing/PowTotientConductor.lean#L26-L48), [vsField](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/HeightAndVanishing/VsField.lean#L24-L126) |
| Strict reverse threshold at twist one | [countVs](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/HeightAndVanishing/CountVs.lean#L86-L171) |
| Inside-set sum and combined positive part | [sum_split, sumIn](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/HeightAndVanishing/FinalLe.lean#L14-L263), [point](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/HeightAndVanishing/PointArith.lean#L36-L92) |
| Host conductor and evaluation on a tower interval | [hostCond](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/HeightAndVanishing/HostCond.lean#L256-L323), [thmHV](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/HeightAndVanishing/ThmHV.lean#L6-L40), [jointWin_of](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/PrimeSetBoundDataOfPrimitiveChar.lean#L145-L158) |

## The final exponential comparison

On the joint interval the prime $2$ contributes at most
$(\log2)\exp(x^{4\varepsilon/5})$. The odd positive part contributes
$u^C+C\exp(x^{4\varepsilon/5})$, where $u=(\operatorname{cond}E)t(x)$.
For the negative part we use the arithmetic estimate of ThmBcFree, whose
constants depend on the fixed character order.

Write $n=[E:\mathbf Q]$, $N=\operatorname{cond}E$ and $o=\deg M_\chi$,
where $M_\chi$ is the abelian field cut out by the original character.
The negative-part bound is

$$
 3nt^2\log(Nt)
 +C_b\sum_{\ell\mid o,\ \ell\ne2}\ell n^2t^2\log(\ell Nt)^2 .
$$

The sum is over distinct odd prime divisors of $o$. Since $n\le N$,
$t\ge1$ and $\log z\le z$ for $z\ge1$, the first term is at most
$3u^4$, and each summand before multiplication by $C_b$ is at most
$\ell^3u^4$. Thus the negative bound is at most $K_bu^4$, with
$K_b=3+|C_b|\sum_{\ell\mid o,\ell\ne2}\ell^3$.

The conductor bound and PageN give

$$
 \begin{aligned}
 N&\le 2^{e(x)+2}Qqd,\\
 2^{e(x)}&\le 2x^{2+8\varepsilon},\qquad t(x)\le x^{C_t}.
 \end{aligned}
$$

Together with $\log(qd)\le x^{\varepsilon/4}$, these imply
$\log u\le x^{\varepsilon/4}+(2+8\varepsilon+C_t)\log x+\log(8Q)$.
For sufficiently large $x$ this is at most $2x^{\varepsilon/4}$.
The threshold is uniform in $q,d$ and $E$.
In particular $K_bu^4\le K_b\exp(8x^{\varepsilon/4})$.

For odd $\ell$, put $s=(-1)^h$. Since $2$ is invertible, the two projectors
$(1+sc)/2$ and $(1-sc)/2$ split the locally trivial module into its two
sign parts. Additivity of extended length gives the sum of their lengths;
no such splitting is used at $2$. Combining the sign decomposition at odd primes with the separate
two-adic estimate proves finiteness and gives, for every finite set
of coefficient primes, the bound

$$
 (\log2+C)\exp(x^{4\varepsilon/5})
     +K_b\exp(8x^{\varepsilon/4})+u^C .
$$

Since $\log u\le2x^{\varepsilon/4}$ and all constants are fixed, the logarithm
of the last expression is $O(x^{4\varepsilon/5})=o(x^\varepsilon)$.
It is therefore at most $x^\varepsilon/2$ for sufficiently large $x$.
Choose this final threshold before $X$, so that every point of the
selected interval lies above it. This proves the required
$\sqrt{\exp(x^\varepsilon)}$ bound on the common window.

| Step | Archive reference |
| --- | --- |
| Negative bound and its exponential form | [minusBound](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/StmtFields.lean#L69-L71), [minusBound_le_exp_of_log_le](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/CMFieldExponentialBounds/minusle.lean#L6-L76) |
| Conductor budget | [log_conductor_mul_height_le_of_pageN](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/CMFieldExponentialBounds/LogConductorMulHeightLeOfPageN.lean#L6-L57) |
| Final comparison | [error_terms_le_sqrt_exp_rpow](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/CMFieldExponentialBounds/ErrorTermsLeSqrtExpRpow.lean#L6-L89) |
| Sign decomposition and summation over arbitrary finite prime sets | [shaLen_eq_add, vvle_of_parts](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/LengthEqAddEigen.lean#L88-L193) |
| Assembly of the three parts and VWin | [vwinAt_of_joint, vwin_of_joint](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/CMFieldExponentialBounds/AdmissibleOfPageN.lean#L41-L134), [vwin_of_counts](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/HeightAndVanishing/JointWinOfCounts.lean#L16-L33) |

