<a id="pdf-page-206"></a>

## PDF page 206 — Fractional parts, nested floors/ceilings and modulo

**Textbook cross-reference:** §8.7, *Remainder Arithmetic*, printed p. 265 (PDF p. 273), is related to integer remainders. The real-number floor/ceiling identities on this page are course-specific; no matching standalone textbook section was located.

The fractional part of a real number is

$$
\{x\}=x-\lfloor x\rfloor,\qquad x=\lfloor x\rfloor+\{x\},\qquad 0\le\{x\}<1.
$$

For $x,y\in\mathbb R$,

$$
\lfloor x+y\rfloor=\lfloor x\rfloor+\lfloor y\rfloor+
\lfloor\{x\}+\{y\}\rfloor.
$$

Since $0\le\{x\}+\{y\}<2$, the last term is either 0 or 1. Thus $\lfloor x+y\rfloor$ is either $\lfloor x\rfloor+\lfloor y\rfloor$ or that quantity plus 1.

The notes use $\ln$ for the natural logarithm and $\lg$ for $\log_2$. For example,

$$
2^5<35<2^6,\qquad\lceil\lg35\rceil=6.
$$

For a positive integer $n$ requiring $m$ binary digits,

$$
2^{m-1}\le n<2^m,\qquad
m=\lfloor\lg n\rfloor+1=\lceil\lg(n+1)\rceil.
$$

**Nested rounding identities:** $\lceil\lfloor x\rfloor\rceil=\lfloor x\rfloor$, and, for $x\ge0$,

$$
\left\lfloor\sqrt{\lfloor x\rfloor}\right\rfloor
=\lfloor\sqrt x\rfloor.
$$

The page proves the square-root identity as follows. Put $m=\lfloor\sqrt{\lfloor x\rfloor}\rfloor$. Then

$$
m\le\sqrt{\lfloor x\rfloor}<m+1
\iff m^2\le\lfloor x\rfloor<(m+1)^2.
$$

For an integer $r$, $r\le x\iff r\le\lfloor x\rfloor$, and $x<r\iff\lfloor x\rfloor<r$. Therefore

$$
m^2\le x<(m+1)^2
\iff m\le\sqrt x<m+1,
$$

so $m=\lfloor\sqrt x\rfloor$.

The following generalization is written in the notes:

$$
f(x)\in\mathbb Z\Longrightarrow x\in\mathbb Z;\qquad
\lfloor f(x)\rfloor=\lfloor f(\lfloor x\rfloor)\rfloor,
\quad
\lceil f(x)\rceil=\lceil f(\lceil x\rceil)\rceil.
$$

**Source qualification:** the displayed condition alone does not justify these identities for an arbitrary function. Additional hypotheses are needed; they are not stated clearly on this page. The specific square-root and integer-division identities below are well-defined with the indicated domains.

For integers $m$ and positive integers $n$, the page records

$$
\left\lfloor\frac{x+m}{n}\right\rfloor
=\left\lfloor\frac{\lfloor x\rfloor+m}{n}\right\rfloor,
\qquad
\left\lceil\frac{x+m}{n}\right\rceil
=\left\lceil\frac{\lceil x\rceil+m}{n}\right\rceil.
$$

One illustration is repeated truncation:

$$
\left\lfloor\frac{\left\lfloor\frac{\lfloor x/10\rfloor}{10}\right\rfloor}{10}\right\rfloor
=\left\lfloor\frac{x}{1000}\right\rfloor.
$$

**Exercise left in the notes:** prove $\lceil\sqrt{\lceil x\rceil}\rceil=\lceil\sqrt x\rceil$ for $x\ge0$.

**Modulo:** for a nonzero modulus $y$,

$$
x\bmod y=x-y\lfloor x/y\rfloor,
\qquad x=y\lfloor x/y\rfloor+(x\bmod y).
$$

The circular sketch shows the remainder wrapping back to 0 after one modulus. The examples on the page are

$$
5\bmod3=5-3\lfloor5/3\rfloor=2,
$$

followed by unfinished exercises $5\bmod(-3)$, $(-5)\bmod3$, and $(-5)\bmod(-3)$. They remain exercises here.

<a id="pdf-page-207"></a>

## PDF page 207 — Modulo signs and Iverson brackets

**Textbook cross-reference:** §8.7, printed p. 265 (PDF p. 273), for integer remainder arithmetic; §13.6, *Double Trouble*, printed p. 525 (PDF p. 533), for changing and regrouping summations. Iverson-bracket notation itself is supplied by the lecture notes.

The notes continue the modulo definition with its sign convention:

$$
0\le x\bmod y<y\quad(y>0),\qquad
y<x\bmod y\le0\quad(y<0).
$$

The fractional part is $\{x\}=x\bmod1$, so $x=\lfloor x\rfloor+\{x\}$.

**Iverson bracket:** for a proposition $P$,

$$
[P]=\begin{cases}1,&P\text{ is true},\\0,&P\text{ is false}.\end{cases}
$$

It allows conditions in summation limits to be moved into the summand:

$$
\sum_{k:P(k)}a_k=\sum_k a_k[P(k)].
$$

For example,

$$
\sum_{k=2}^{n-1}k(k-1)(n-k)
=\sum_{k=0}^{n}k(k-1)(n-k)[k\ge2][k<n].
$$

Also $[p\text{ is prime}]$ is 1 precisely for primes. Thus the number of primes at most $N$ can be written $\sum_{p\ge0}[p\text{ is prime}][p\le N]$. The page explicitly notes that the $p=0$ term is 0.

The longer example is, for a positive integer $n$,

$$
S=\sum_{1<k<2^{2^n}}
\frac{1}{2^{\lfloor\lg k\rfloor}4^{\lfloor\lg\lg k\rfloor}}.
$$

Introduce $\ell=\lfloor\lg k\rfloor$ and $m=\lfloor\lg\ell\rfloor$. The notes replace these definitions with integer intervals:

$$
2^\ell\le k<2^{\ell+1},\qquad
2^m\le\ell<2^{m+1},\qquad0\le m<n.
$$

Therefore

$$
\begin{aligned}
S&=\sum_{k,\ell,m}2^{-\ell}4^{-m}
[2^\ell\le k<2^{\ell+1}]
[2^m\le\ell<2^{m+1}][0\le m<n]\\
&=\sum_{\ell,m}4^{-m}[2^m\le\ell<2^{m+1}][0\le m<n]\\
&=\sum_m2^{-m}[0\le m<n]
=2(1-2^{-n}).
\end{aligned}
$$

The first regrouping uses $2^\ell$ possible integers $k$ for a fixed $\ell$. The next uses $2^m$ possible integers $\ell$ for a fixed $m$. This cancels the powers in the summand and leaves a geometric sum.

<a id="pdf-page-208"></a>

## PDF page 208 — The sum of floors of square roots

**Textbook cross-reference:** §13.3, *Approximating Sums*, printed p. 512 (PDF p. 520), and §13.6, printed p. 525 (PDF p. 533), give the related bounding and summation methods. This exact Iverson-bracket example is from the lecture.

Consider the sum $F(n)=\sum_{0\le k<n}\lfloor\sqrt k\rfloor$, for a nonnegative integer $n$. Introduce $m=\lfloor\sqrt k\rfloor$. Then

$$
\begin{aligned}
F(n)&=\sum_{k,m\ge0}m[k<n][m=\lfloor\sqrt k\rfloor]\\
&=\sum_{k,m\ge0}m[k<n][m\le\sqrt k<m+1]\\
&=\sum_{k,m\ge0}m[k<n][m^2\le k<(m+1)^2].
\end{aligned}
$$

Put $a=\lfloor\sqrt n\rfloor$. Split the sum into complete square intervals and a final partial interval. For $0\le m<a$, there are $(m+1)^2-m^2=2m+1$ terms; for $m=a$, there are $n-a^2$ terms. Thus

$$
I=\sum_{m=0}^{a-1}m(2m+1)=\frac{a(a-1)(4a+1)}6,
\qquad II=a(n-a^2).
$$

The handwritten example $n=90$ has $a=9$, and the partial block contributes $9(90-81)$.

Combining the two pieces gives

$$
\boxed{F(n)=an-\frac{a^3}{3}-\frac{a^2}{2}-\frac a6,
\quad a=\lfloor\sqrt n\rfloor.}
$$

The page also discusses using the floor sum as a lower bound on the square-root sum:

$$
\sum_{0\le k<n}\sqrt k\ge F(n).
$$

**Source qualification:** the intervening handwritten lower-bound line appears to read $\frac23a^3+\frac32a^2+\frac56a$, with an endpoint written as $n$ and $a=\sqrt n$. Those labels are inconsistent with the stated endpoint. That polynomial is the completed-block sum through $k=(a+1)^2-1$, not through $k=a^2$. The checked $I+II$ expression above follows the page's derivation; use its explicit endpoint. For the inclusive sum, replace $n$ by $n+1$ in $F$.

<a id="pdf-page-209"></a>

## PDF page 209 — Josephus, Hanoi and merge-sort recurrences

**Textbook cross-reference:** Ch. 21, especially §21.1, *The Towers of Hanoi*, printed p. 867 (PDF p. 875), and §21.2, *Merge Sort*, printed p. 870 (PDF p. 878). Josephus is a lecture-specific example.

**Josephus problem:** people numbered $1,\ldots,n$ stand in a circle. Repeatedly eliminate every second person; $J(n)$ is the surviving person's index. For $n=10$, the first pass removes $2,4,6,8,10$ and subsequent eliminations leave survivor 5.

| $n$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| $J(n)$ | 1 | 1 | 3 | 1 | 3 | 5 | 7 | 1 | 3 | 5 | 7 | 9 | 11 | 13 | 15 | 1 |

Write $n=2^m+\ell$, where $m\ge0$ and $0\le\ell<2^m$. The observed pattern is

$$
J(n)=J(2^m+\ell)=2\ell+1.
$$

The recurrence relations are

$$
J(1)=1,\qquad J(2n)=2J(n)-1,\qquad J(2n+1)=2J(n)+1.
$$

The lecture connects a recursive algorithm to a recurrence relation and then to an induction proof.

**Towers of Hanoi:** $T_1=1$ and $T_n=2T_{n-1}+1$. The guessed formula is $T_n=2^n-1$. Expanding the recurrence gives

$$
\begin{aligned}
T_n&=4T_{n-2}+2+1\\
&=8T_{n-3}+4+2+1\\
&=2^kT_{n-k}+2^{k-1}+\cdots+2+1\\
&=2^kT_{n-k}+2^k-1.
\end{aligned}
$$

Verify the pattern by induction on $k$: substituting the recurrence for $T_{n-k}$ changes the expression into $2^{k+1}T_{n-(k+1)}+2^{k+1}-1$. Use $k=n-1$ and $T_1=1$ to get $T_n=2^n-1$.

The page labels the methods “induction / expansion / plug & chug” and emphasizes identifying and then verifying a pattern.

**Merge sort:** when $n$ is a power of 2, the comparison-count recurrence is

$$
T_1=0,\qquad T_n=2T_{n/2}+n-1.
$$

The first values for input sizes $1,2,4,8,16$ are $0,1,5,17,49$. Expansion gives

$$
\begin{aligned}
T_n&=4T_{n/4}+(n-2)+(n-1)\\
&=2^kT_{n/2^k}+kn-2^{k-1}-\cdots-2^0\\
&=2^kT_{n/2^k}+kn-2^k+1.
\end{aligned}
$$

Substituting once more verifies the pattern for $k+1$. The next page uses the initial condition to finish the solution.

<a id="pdf-page-210"></a>

## PDF page 210 — Finishing the merge-sort solution

**Textbook cross-reference:** §21.2, printed pp. 870–873 (PDF pp. 878–881).

Use $T_1=0$. Setting $k=\lg n$ gives $T_{n/2^k}=T_1$, so

$$
T_n=nT_1+n\lg n-n+1
=\boxed{n\lg n-n+1}.
$$

This exact solution uses the power-of-two input-size assumption from the preceding page.

<a id="pdf-page-211"></a>

## PDF page 211 — Homogeneous linear recurrences and characteristic roots

**Textbook cross-reference:** §21.3, *Linear Recurrences*, printed pp. 874–880 (PDF pp. 882–888).

The notes distinguish linear recurrences, which use $f(n-1),f(n-2),\ldots$, from divide-and-conquer recurrences, which use smaller fractional inputs such as $f(n/2)$. The sketches include $f(1)=1$, $f(n)=2f(n-1)+1-2^n$, another forcing-term example $-n^{100}$, and a divide-and-conquer form $f(n)=2f(n/2)+n-1$.

The Fibonacci-type example is

$$
f(0)=1,\quad f(1)=1,\qquad f(n)=f(n-1)+f(n-2)\quad(n\ge2).
$$

A homogeneous linear recurrence with constant coefficients has the form

$$
f(n)=a_1f(n-1)+a_2f(n-2)+\cdots+a_df(n-d).
$$

Try $f(n)=r^n$. For the Fibonacci recurrence,

$$
r^n=r^{n-1}+r^{n-2}
\Longrightarrow r^2-r-1=0
\Longrightarrow r=\frac{1\pm\sqrt5}{2}.
$$

Write $\phi=(1+\sqrt5)/2$ and $\psi=(1-\sqrt5)/2$. A general solution is $f(n)=s\phi^n+t\psi^n$. The initial conditions give $s+t=1$ and $s\phi+t\psi=1$.

**Textbook clarification / source correction:** for the written initial values $f(0)=f(1)=1$, the resulting constants are $s=\phi/\sqrt5$ and $t=-\psi/\sqrt5$, giving

$$
\boxed{f(n)=\frac{\phi^{n+1}-\psi^{n+1}}{\sqrt5}}.
$$

The handwritten constants/final line appear to use a plus sign on the $\psi$ term. That sign does not satisfy the written initial conditions. The supplied textbook uses the same $f(0)=f(1)=1$ convention as these notes. For comparison, the common alternative $F_0=0,F_1=1$ convention gives $F_n=(\phi^n-\psi^n)/\sqrt5$ and $f(n)=F_{n+1}$.

The page mentions Binet's formula and the dominance of the $\phi$ term for large $n$. Its numerical illustration uses $\phi^{20}/\sqrt5\approx6765.00003$, rounded to 6765. The adjacent handwritten sequence index is [unclear in source]. **Textbook clarification:** printed p. 877 identifies this value as $f(19)$ for the written initial conditions, with $f(n)=\phi^{n+1}/\sqrt5+o(1)$.

A differential-equation comparison sketches $(D+3)(D-3)Dy=15$ and the associated homogeneous terms $c_1+c_2e^{3n}+c_3e^{-3n}$. This is an analogy about roots and solution forms; no full differential-equation solution is worked out.

For the general recurrence, the characteristic polynomial is

$$
r^d-a_1r^{d-1}-a_2r^{d-2}-\cdots-a_d=0.
$$

- A distinct root $r$ contributes $r^n$.
- A root $r$ of multiplicity $k$ contributes $r^n,nr^n,\ldots,n^{k-1}r^n$.
- Combine all contributions linearly, then use the initial values to determine their coefficients.

The page illustrates three distinct roots $s,t,u$, with $u$ repeated, using $as^n+bt^n+cu^n+dnu^n$. Four initial values determine the four coefficients.

The nonhomogeneous example $f(1)=1$, $f(n)=2f(n-1)+1$ is then introduced. Its associated homogeneous recurrence is $f(n)=2f(n-1)$.

<a id="pdf-page-212"></a>

## PDF page 212 — Nonhomogeneous recurrences and particular solutions

**Textbook cross-reference:** §21.3.3, *Solving General Linear Recurrences*, printed pp. 879–881 (PDF pp. 887–889).

The general form is

$$
f(n)=a_1f(n-1)+\cdots+a_df(n-d)+g(n).
$$

Separate the homogeneous part from a particular solution. The page compares $f(n)=2f(n-1)+1$ with the modified problem

$$
f(1)=1,\qquad f(n)=2f(n-1)+n.
$$

The homogeneous solution is $c2^n$. For the linear forcing term $n$, try a particular solution $an+b$. Substitute:

$$
an+b=2(a(n-1)+b)+n
\Longrightarrow0=(a+1)n+(b-2a).
$$

Thus $a=-1,b=-2$, so a particular solution is $-n-2$. The full solution is $f(n)=c2^n-n-2$. Using $f(1)=1$ gives $c=2$, hence

$$
\boxed{f(n)=2^{n+1}-n-2}.
$$

The final handwritten comparison $2^n-1$ is the solution of the original constant-forcing Hanoi recurrence. The modified recurrence takes about twice as much time asymptotically, as the textbook comparison on printed p. 881 explains.

The methods named at the bottom are **method of undetermined coefficients** and **variation of parameters**. Only the undetermined-coefficients example above is worked out on this page.

<a id="pdf-page-213"></a>

## PDF page 213 — Particular-solution guesses and the Akra–Bazzi formula

**Textbook cross-reference:** §21.3.4, printed p. 881 (PDF p. 889), for particular-solution guesses; §21.4.1, printed pp. 883–884 (PDF pp. 891–892), for Akra–Bazzi.

To guess a particular solution, follow the form of the forcing term $g(n)$:

- For a constant $g(n)$, try a constant, then a linear polynomial if needed.
- For a linear/polynomial forcing term, try a polynomial of the same degree, then increase its degree if needed.
- For $g(n)=2^n$, try $c2^n$, then $cn2^n$, then a higher-degree polynomial times $2^n$ if the trial overlaps homogeneous solutions.

For divide-and-conquer recurrences,

$$
T(n)=\sum_{i=1}^k a_iT(b_i n)+g(n),
\qquad a_i>0,\quad0<b_i<1.
$$

Akra–Bazzi gives

$$
T(n)=\Theta\!\left(n^p\left(1+\int_1^n\frac{g(u)}{u^{p+1}}\,du\right)\right),
\qquad\sum_{i=1}^ka_i b_i^p=1,
$$

under its regularity and base-case assumptions.

**Merge sort:** $a_1=2,b_1=1/2,g(n)=n-1$. Solve $2(1/2)^p=1$, giving $p=1$. Thus

$$
T(n)=\Theta\!\left(n\left(1+\int_1^n\frac{u-1}{u^2}\,du\right)\right)
=\Theta(n\log n).
$$

**Unequal subproblem example:**

$$
T(n)=2T(n/2)+\frac89T(3n/4)+n^2.
$$

Here $a_1=2,b_1=1/2,a_2=8/9,b_2=3/4,g(n)=n^2$. Since $2(1/2)^2+(8/9)(3/4)^2=1$, $p=2$ and

$$
T(n)=\Theta\!\left(n^2\left(1+\int_1^n\frac{u^2}{u^3}\,du\right)\right)
=\Theta(n^2\log n).
$$

The page compares different base values, such as $T_1=1$ and $T_1=10$, and rounded half-size inputs. The rounded merge-sort recurrence is $T_1=0$ and $T_n=T(\lceil n/2\rceil)+T(\lfloor n/2\rfloor)+n-1$. For $n=15$, the two integer subproblem sizes are 8 and 7, rather than 7.5 and 7.5.

**Perturbed Akra–Bazzi theorem:** for sufficiently large $n_0$,

$$
T(n)=\sum_{i=1}^k a_iT(b_i n+h_i(n))+g(n)\qquad(n>n_0),
$$

with bounded base values on the initial interval, positive constant $a_i$, $0<b_i<1$, and $|h_i(n)|=O(n/\log^2n)$, the same formula applies when the theorem's growth assumptions on $g$ hold.

**Textbook clarification:** the handwritten $|g'(n)|<\infty$ is abbreviated. The textbook's stated requirement is that $|g'(n)|$ be bounded by a polynomial; mere finiteness at each point is insufficient. The page explicitly contrasts suitable polynomial work with an unsuitable $2^n$ forcing term for this version of the theorem.

<a id="pdf-page-214"></a>

## PDF page 214 — Floor/ceiling perturbations, Master theorem and recurrence growth

**Textbook cross-reference:** §21.4.2–21.4.3, within printed pp. 884–887 (PDF pp. 892–895), and §21.5, *A Feel for Recurrences*, printed p. 888 (PDF p. 896).

For rounded merge sort, use two terms with $a_1=a_2=1$, $b_1=b_2=1/2$,

$$
h_1(n)=\lceil n/2\rceil-n/2,\qquad
h_2(n)=\lfloor n/2\rfloor-n/2,
\qquad g(n)=n-1.
$$

The perturbations have bounded absolute value, so they satisfy $O(n/\log^2n)$. Hence integer rounding preserves the $\Theta(n\log n)$ asymptotic result.

For $T(n)=aT(n/b)+g(n)$, put $p=\log_ba$. The **Master theorem** cases written on the page are:

1. If $g(n)=O(n^{p-\varepsilon})$ for some $\varepsilon>0$, then $T(n)=\Theta(n^p)$.
2. If $g(n)=\Theta(n^p\log^k n)$ with $k\ge0$, then $T(n)=\Theta(n^p\log^{k+1}n)$.
3. If $g(n)=\Omega(n^{p+\varepsilon})$ for some $\varepsilon>0$, and $a g(n/b)\le c g(n)$ eventually for some $c<1$, then $T(n)=\Theta(g(n))$.

The lecture's comparison table is:

| Problem | Recurrence | Growth |
| --- | --- | --- |
| Hanoi | $T_n=2T_{n-1}+1$ | $T_n\sim2^n$ |
| Disk-size-dependent Hanoi | $T_n=2T_{n-1}+n$ | $T_n\sim2\cdot2^n$ |
| Fibonacci-type sequence | $T_n=T_{n-1}+T_{n-2}$ | $T_n\sim\phi^{n+1}/\sqrt5$ under the notes' initial values |
| Merge sort | $T_n=2T_{n/2}+n-1$ | $T_n\sim n\lg n$ on power-of-two inputs |

Changing the number and size of subproblems changes the growth. An example $T_n=3T_{n-1}+1$ grows on the order of $3^n$.

For $T_1=0$ and $T_n=aT_{n/2}+n-1$, the final sketch gives

$$
T_n=\begin{cases}
\Theta(n),&1\le a<2,\\
\Theta(n\log n),&a=2,\\
\Theta(n^{\log_2a}),&a>2.
\end{cases}
$$

The numbers 1.95 and 2.01 emphasize how crossing $a=2$ changes the applicable case. **Domain clarification:** the sketch simply writes $a<2$ in the first branch; the conventional algorithmic interpretation uses positive call counts, and the displayed branch here is stated for $a\ge1$.

<a id="pdf-page-215"></a>

## PDF page 215 — Generating functions, constrained choices and convolution

**Textbook cross-reference:** §15.1–15.2, printed pp. 627–634 (PDF pp. 635–642).

The opening counting problem asks for 87 ice-creams of four types: an even number of vanilla, a multiple of 5 mango, at most 4 strawberry and at most 1 chocolate.

A sequence $f_0,f_1,f_2,\ldots$ is encoded by its ordinary generating function

$$
F(x)=f_0+f_1x+f_2x^2+\cdots,\qquad[x^n]F(x)=f_n.
$$

The handwritten variable is reused in several roles; $x$ denotes the formal series variable here and $n$ the coefficient index.

For $1,1,1,\ldots$, write $G(x)=1+x+x^2+\cdots$. Subtract $xG(x)$ to obtain $(1-x)G(x)=1$, hence

$$
G(x)=\frac1{1-x},\qquad[x^n]G(x)=1.
$$

For $1,2,3,\ldots$, let $N(x)=1+2x+3x^2+\cdots$. Then $N(x)-xN(x)=G(x)$, so

$$
N(x)=\frac{G(x)}{1-x}=\frac1{(1-x)^2},\qquad[x^n]N(x)=n+1.
$$

This also counts unrestricted splits of $n$ objects into two flavours: $(n,0),(n-1,1),\ldots,(0,n)$.

More generally, if $a_n$ counts ways to choose $n$ items of one family and $b_n$ counts ways for a second, then choosing $k$ from the first and $n-k$ from the second gives $a_kb_{n-k}$ possibilities. Summing over $k$ gives

$$
[x^n](A(x)B(x))=\sum_{k=0}^na_kb_{n-k}.
$$

This is **convolution**. A variant sketch splits chocolate into dark and mint types, introducing another generating-function factor. Another example allows mango only in groups of 6:

$$
A(x)=1+x^6+x^{12}+\cdots=\frac1{1-x^6},\qquad B(x)=N(x).
$$

The coefficient in $A(x)B(x)$ then counts the admissible combinations; the next page continues this example and the general product rule.

<a id="pdf-page-216"></a>

## PDF page 216 — Product rule, the ice-cream calculation and rational generating functions

**Textbook cross-reference:** §15.2, printed pp. 629–634 (PDF pp. 637–642), and §15.3, *Partial Fractions*, printed p. 635 (PDF p. 643).

The initial example repeats $A(x)=1/(1-x^6)$ and $B(x)=1/(1-x)^2$. For a total of $n$ items, split the choices into $k$ apples and $n-k$ bananas (a relabelling of the two-family example). There are

$$
a_0b_n+a_1b_{n-1}+\cdots+a_nb_0
$$

combinations. The theorem is

$$
\boxed{[x^n](A(x)B(x))=\sum_{i=0}^na_ib_{n-i}.}
$$

The drawn multiplication table has entries $a_ix^i\cdot b_jx^j$. Entries on a diagonal with $i+j=n$ contribute to $x^n$. The same rule is illustrated as splitting an $n$-element choice across two disjoint families, and as concatenating a choice from each family.

For two unrestricted flavours, $G(x)G(x)=1/(1-x)^2$, whose $x^n$ coefficient is $n+1$.

The page records the standard identity

$$
[x^n]\frac1{(1-x)^k}=\binom{n+k-1}{n}\qquad(k\ge1).
$$

A nearby derivative notation is [unclear in source]; the coefficient identity itself is clear.

**Constrained ice-cream example:** the factor assignment on this page is vanilla even, chocolate a multiple of 5, mango at most 4, strawberry at most 1. It permutes the flavour names from page 215, while preserving the four constraints and the total count. Write

$$
V(x)=\frac1{1-x^2},\quad C(x)=\frac1{1-x^5},\quad
M(x)=1+x+x^2+x^3+x^4=\frac{1-x^5}{1-x},\quad S(x)=1+x.
$$

Then

$$
V(x)C(x)M(x)S(x)
=\frac{1+x}{(1-x^2)(1-x)}
=\frac1{(1-x)^2}.
$$

Consequently $[x^n](VCMS)=n+1$, so the 87-item case has 88 choices.

**Partial fractions with distinct roots:** if the denominator is $\prod_{i=1}^m(1-\alpha_i x)$ with distinct $\alpha_i$ and the numerator has smaller degree, express the rational function as

$$
\frac{P(x)}{\prod_i(1-\alpha_i x)}
=\sum_i\frac{c_i}{1-\alpha_i x}.
$$

Example: $R(x)=x/(1-x-x^2)$. The denominator zeros are $\rho_1=(-1-\sqrt5)/2$ and $\rho_2=(-1+\sqrt5)/2$. In the factor form, use their reciprocals

$$
\alpha_1=\frac{1+\sqrt5}{2},\qquad
\alpha_2=\frac{1-\sqrt5}{2},\qquad
1-x-x^2=(1-\alpha_1x)(1-\alpha_2x).
$$

This example continues on the next page.

<a id="pdf-page-217"></a>

## PDF page 217 — Partial fractions, repeated roots and the binomial theorem

**Textbook cross-reference:** §15.3, printed pp. 635–638 (PDF pp. 643–646); the binomial/counting interpretation is also related to Ch. 14.

Continue $R(x)=x/(1-x-x^2)$ with the factors from page 216. Write

$$
R(x)=\frac{c_1}{1-\alpha_1x}+\frac{c_2}{1-\alpha_2x}.
$$

Multiplying by the denominator gives $x=c_1(1-\alpha_2x)+c_2(1-\alpha_1x)$. Therefore $c_1=1/\sqrt5$ and $c_2=-1/\sqrt5$, so

$$
R(x)=\frac1{\sqrt5}\left(\frac1{1-\alpha_1x}-\frac1{1-\alpha_2x}\right).
$$

Expanding each geometric series and subtracting gives

$$
[x^n]R(x)=\frac{\alpha_1^n-\alpha_2^n}{\sqrt5}
=\frac1{\sqrt5}\left(\left(\frac{1+\sqrt5}{2}\right)^n-
\left(\frac{1-\sqrt5}{2}\right)^n\right).
$$

Thus $R$ generates the Fibonacci sequence with initial values 0 and 1.

For a denominator factor repeated with multiplicity $m$, include terms $c_k/(1-\alpha x)^k$ for $1\le k\le m$. Their coefficients are

$$
[x^n]\frac c{(1-\alpha x)^k}
=c\alpha^n\binom{n+k-1}{n}.
$$

The scaling identity behind this is $[x^n]F(\alpha x)=\alpha^n[x^n]F(x)$.

The final drawing has $m$ distinguishable boxes, each with a factor $1+x$. Selecting or not selecting the item in each box gives

$$
(1+x)^m,\qquad[x^n](1+x)^m=\binom mn.
$$

This recovers the binomial theorem by counting the ways to select $n$ of $m$ items.

<a id="pdf-page-218"></a>

## PDF page 218 — Recurrences through generating functions and formal factorial series

**Textbook cross-reference:** §15.4, *Solving Linear Recurrences*, printed pp. 638–643 (PDF pp. 646–651); §15.5, *Formal Power Series*, printed pp. 643–646 (PDF pp. 651–654); §21.1 for Hanoi.

**Fibonacci:** $f_0=0,f_1=1$, and $f_n=f_{n-1}+f_{n-2}$ for $n\ge2$. Form $F(x)=f_0+f_1x+f_2x^2+\cdots$. Subtract the shifted series $xF(x)$ and $x^2F(x)$. The coefficient of $x^n$ is zero for $n\ge2$, leaving

$$
(1-x-x^2)F(x)=x,\qquad F(x)=\frac{x}{1-x-x^2}.
$$

The partial-fraction result from page 217 now provides the closed-form coefficients.

**Hanoi:** the peg-and-disk drawings explain the matching bounds. Move the top $n-1$ disks aside, move the largest disk, then move the $n-1$ disks back, giving an upper bound $t_n\le2t_{n-1}+1$. Any legal solution must do these stages, giving $t_n\ge2t_{n-1}+1$. Hence

$$
t_0=0,\qquad t_n=2t_{n-1}+1\quad(n\ge1).
$$

The notes mention 64 disks, approximately $2^{64}$ seconds at one move per second, and more than 500 billion years. The isolated number “1941” is also written near the sketch; its context is [unclear in source].

For $T(x)=\sum_{n\ge0}t_nx^n$, subtract $2xT(x)$ and $1/(1-x)$. The positive-degree coefficients cancel and the constant term is $t_0-1=-1$. Thus

$$
T(x)(1-2x)=\frac1{1-x}-1=\frac x{1-x},
$$

$$
T(x)=\frac x{(1-2x)(1-x)}
=\frac1{1-2x}-\frac1{1-x},\qquad
[x^n]T(x)=2^n-1.
$$

The page then notes the general method for $f_n=a_1f_{n-1}+\cdots+a_df_{n-d}+g(n)$: subtract shifted/scaled generating functions for the homogeneous terms and include the generating function for $g(n)$. Initial terms must be accounted for separately. A circled half-index term $f_{n/2}$ contrasts divide-and-conquer recurrences with this fixed-shift technique.

**Formal factorial series:** let

$$
F(x)=\sum_{n\ge0}n!x^n=1+x+2x^2+\cdots,
\qquad H(x)=\sum_{n\ge0}n\,n!x^n=0+x+4x^2+\cdots.
$$

These series are manipulated in the ring of formal power series; numerical convergence is not required. Coefficient shifting gives

$$
[x^n]\frac{F(x)-1}{x}=(n+1)!,\qquad
n\,n!=(n+1)!-n!.
$$

Therefore $H(x)=(F(x)-1)/x-F(x)$, so

$$
F(x)=\frac{xH(x)+1}{1-x}.
$$

The numerator has constant coefficient 1 and, for $n\ge1$, coefficient $(n-1)(n-1)!$. Multiplication by $1/(1-x)$ takes prefix sums. Consequently

$$
\boxed{n!=1+\sum_{i=1}^n(i-1)(i-1)!.}
$$

<a id="pdf-page-219"></a>

## PDF page 219 — Graph definitions, degrees, standard graphs and isomorphism

**Textbook cross-reference:** §11.1–11.4, printed pp. 393–401 (PDF pp. 401–409); directed graphs also appear in Ch. 9.

The lecture introduces graph theory, distinguishing undirected simple graphs from directed graphs. For an undirected edge, the order of its two endpoints does not matter; directed edges have an arrow and an ordered source/target. A graph is $G=(V,E)$, with vertex set $V(G)$ and edge set $E(G)$. The notes use $|V(G)|\ge1$ and $|E(G)|\ge0$, and illustrate a graph consisting entirely of isolated vertices.

The degree $\deg(v)$ is the number of vertices adjacent to $v$ in a simple graph. In the labelled example, $B$ is adjacent to $A,C,E$, so $\deg(B)=3$.

A two-sided diagram partitions the vertices into $X$ and $Y$, with every drawn edge crossing the partition. Each edge contributes once to each side's degree total:

$$
\sum_{v\in X}\deg(v)=\sum_{v\in Y}\deg(v).
$$

For nonempty sides,

$$
\boxed{\operatorname{avgdeg}(X)=\frac{|Y|}{|X|}\operatorname{avgdeg}(Y).}
$$

The handwritten manipulation divides the same total by $|X||Y|$ before rearranging. **Domain clarification:** this argument requires the crossing-edge/bipartite setup shown in the drawing; it is not an identity for arbitrary partitions.

**Handshaking theorem:** $\sum_{v\in V(G)}\deg(v)=2|E(G)|$.

**Standard graphs:**

- The complete graph $K_n$ joins every pair of distinct vertices and has $\binom n2=n(n-1)/2$ edges; a $K_4$ sketch illustrates this.
- The path graph has vertices $v_1,\ldots,v_n$ and edges $\{v_i,v_{i+1}\}$ for $1\le i<n$. The notes call the drawing a “line graph”; here “path graph” identifies the intended chain.
- A cycle graph adds the closing edge from the last vertex back to the first.

**Graph isomorphism:** graphs $G,H$ are isomorphic if there is a bijection $f:V(G)\to V(H)$ such that

$$
\{u,v\}\in E(G)\iff\{f(u),f(v)\}\in E(H).
$$

The page compares two drawings of a square with one diagonal: their vertex positions differ, but an adjacency-preserving relabelling makes the graphs identical. It also compares a pentagon drawing with a five-pointed-star drawing of the same cycle; edge crossings do not automatically create new vertices.

The note “equivalence relation” records that graph isomorphism is reflexive, symmetric and transitive. The closing lines begin a vertex correspondence, but do not complete the mapping; no finished mapping is supplied on the page.

<a id="pdf-page-220"></a>

## PDF page 220 — Other textbook recommendations and assessment notes

This page contains reference and administrative notes rather than a new mathematical topic.

- Rosen — “Discrete Math”.
- Epp — the book-title line is left blank.
- Gersting — “Math Structures for CS”.
- Hein — “Discrete Structures”.

The lower half contains “40% — 10% + 50%”, the numbers “35” and “55”, and a further “40 50” annotation. **Source qualification:** their association with particular assessment components is not specified clearly enough to reconstruct a grading scheme. These are transcribed as written, not treated as an authoritative current marks distribution.

<a id="pdf-page-221"></a>

## PDF page 221 — Graph coloring and the maximum-degree bound

**Textbook cross-reference:** §11.5, *Bipartite Graphs & Matchings*, printed p. 401 (PDF p. 409); §11.7, *Coloring*, printed pp. 413–417 (PDF pp. 421–425). SAT is related to §3.5, printed p. 55 (PDF p. 63).

A proper vertex coloring assigns different colors to adjacent vertices. The opening drawing uses three colors: $A,E$ red, $B$ blue, and $C,D$ green. A graph is $k$-colorable if it admits a proper coloring with at most $k$ colors. Its chromatic number $\chi(G)$ is the least such $k$, so $k$-colorability means $\chi(G)\le k$.

The example graph has edges $AB,AC,AD,BC,BD,BE,CE,DE$. The displayed coloring is proper, and a triangle requires three colors, establishing chromatic number 3.

The notes list

$$
\chi(C_{\text{even}})=2,\qquad
\chi(C_{\text{odd}})=3,\qquad\chi(K_n)=n.
$$

Bipartite graphs have a partition into two independent sides. The drawing colors each side uniformly. **Domain clarification:** $\chi(G)\le2$ for bipartite graphs; equality holds when there is at least one edge. An edgeless nonempty graph needs only one color.

The page mentions SAT, “NP-complete,” and graph-coloring applications. **Textbook clarification:** fixed-$k$ colorability is NP-complete for $k\ge3$; 2-colorability is efficiently decidable. The word “NP-complete” should not be applied to all $k$ indiscriminately.

**Theorem:** a graph whose maximum degree is at most $n$ is $(n+1)$-colorable, equivalently $\chi(G)\le\Delta(G)+1$.

The proof is by induction on the number of vertices $k$, with the degree bound $n$ held fixed. The one-vertex base case uses one color. For a graph $G$ with $k+1$ vertices, remove a vertex $v$. The resulting graph $H$ has $k$ vertices and maximum degree at most $n$, so the induction hypothesis colors it with $n+1$ colors. When $v$ is restored, its at most $n$ neighbors forbid at most $n$ colors. At least one of the $n+1$ colors is available for $v$.

The sketches compare a triangle/complete graph and a star with maximum degree 6; the degree bound guarantees 7 colors even though the star is 2-colorable. The page ends by naming **distributed graph coloring** and **online graph coloring** problems, without developing their algorithms.
