<a id="pdf-page-151"></a>

## PDF page 151 — Direct proof and parity definitions

**Proof techniques: direct proof.** To prove an implication (p\Rightarrow q), start from (p) and derive (q).

An integer (n) is **even** if there is a (k\in\mathbb Z) such that (n=2k=2k+0). It is **odd** if there is a (k\in\mathbb Z) such that (n=2k+1).

**Textbook cross-reference:** §1.5, “Proving an Implication,” printed pp. 11–12 (PDF pp. 19–20).

<a id="pdf-page-152"></a>

## PDF page 152 — The square of an odd integer is odd

**Claim.** If (n) is an odd integer, then (n^2) is odd.

Since (n) is odd, write (n=2k+1) for some (k\in\mathbb Z). Then
\[
n^2=(2k+1)^2=4k^2+4k+1=2(2k^2+2k)+1.
\]
The quantity (2k^2+2k) is an integer, so (n^2) is odd.

**Source correction:** the handwritten last factor appears as (2(2k+2)+1). The preceding expansion (4k^2+4k+1) requires (2(2k^2+2k)+1); the corrected algebra is displayed above.

**Textbook cross-reference:** §1.5, printed pp. 11–12, for the direct-proof pattern.

<a id="pdf-page-153"></a>

## PDF page 153 — Product of two perfect squares

**Claim.** If (m,n) are perfect squares, then (mn) is a perfect square.

Write (m=i^2) and (n=j^2) for some (i,j\in\mathbb Z). Therefore
\[
mn=i^2j^2=(ij)^2.
\]
Since (ij\in\mathbb Z), this is a perfect square.

**Textbook cross-reference:** §1.5, printed pp. 11–12, for direct proof from the definitions.

<a id="pdf-page-154"></a>

## PDF page 154 — Proof by contraposition

**Claim.** If (n\in\mathbb Z) and (3n+2) is odd, then (n) is odd. The source labels the hypothesis (p) and conclusion (q).

A direct attempt begins:
\[
3n+2=2k+1\quad\Rightarrow\quad 3n+1=2k.
\]
The alternative observation is that if (n) is even, then (3n+2) is even.

**Proof by contraposition:**
\[
(p\Rightarrow q)\equiv(\neg q\Rightarrow\neg p).
\]
Thus prove the assertion “(n) even implies (3n+2) even.”

**Textbook cross-reference:** §1.5.2, “Method #2 – Prove the Contrapositive,” printed p. 13 (PDF p. 21).

<a id="pdf-page-155"></a>

## PDF page 155 — Factor bounds and contradiction

**Claim/exercise.** If (n=ab), with (a,b\in\mathbb Z^+), then
\[
a\le\sqrt n\quad\text{or}\quad b\le\sqrt n.
\]

**Exercise.** Show that (\sqrt2) is irrational.

The contradiction pattern written below is
\[
q\Rightarrow\cdots\Rightarrow(p\land\neg p).
\]
The expression (p\land\neg p) is the contradiction to be reached.

**Textbook cross-reference:** §1.8, “Proof by Contradiction,” printed pp. 16–17 (PDF pp. 24–25); the textbook proves irrationality of (\sqrt2) here.

<a id="pdf-page-156"></a>

## PDF page 156 — Irrationality of the square root of two

Assume (\sqrt2) is rational. Then
\[
\sqrt2=\frac pq,
\qquad p\in\mathbb Z,\quad q\ne0,\quad\gcd(p,q)=1.
\]
Squaring and clearing denominators gives
\[
2=\frac{p^2}{q^2}\quad\Rightarrow\quad 2q^2=p^2.
\]
Hence (p^2) is even, so (p) is even. Write (p=2r); then
\[
2q^2=4r^2\quad\Rightarrow\quad q^2=2r^2.
\]
Thus (q^2), and therefore (q), is even too. This implies (\gcd(p,q)\ne1), contradicting the choice of the fraction in lowest terms. Therefore (\sqrt2) is irrational.

**Marginal source fragment:** (p^2=nq^2\Rightarrow p^2/q^2=n=m^2). No hypotheses or proof for the final equality are supplied on this page; it is retained as a fragment, not used in the argument above.

**Textbook cross-reference:** §1.8, printed pp. 16–17 (PDF pp. 24–25), gives the same contradiction argument.

<a id="pdf-page-157"></a>

## PDF page 157 — Mathematical induction template

The goal is a universally quantified statement (\forall n\,P(n)). The source writes (n\in\mathbb Z), then starts at (1).

**Base case:** prove (P(1)).

**Inductive step:** prove (P(k)\Rightarrow P(k+1)).

The inference is written as
\[
\left(P(1)\land\forall k\,[P(k)\Rightarrow P(k+1)]\right)
\vdash\forall n\,P(n).
\]

**Textbook clarification:** a base case at (1) with a forward step establishes the statement for integers (n\ge1), not automatically for every integer. The corresponding induction principle is §5.1, printed pp. 115–116 (PDF pp. 123–124).

<a id="pdf-page-158"></a>

## PDF page 158 — Induction proof for the sum of the first integers

**Claim.** For (n\ge1),
\[
1+2+\cdots+n=\frac{n(n+1)}2.
\]

**Base case:** (n=1). Both sides equal (1).

**Inductive hypothesis:** assume
\[
\sum_{i=1}^{n}i=\frac{n(n+1)}2.
\]
For the next case, the desired equality is
\[
\sum_{i=1}^{n+1}i=\frac{(n+1)(n+2)}2.
\]
Using the hypothesis,
\[
\sum_{i=1}^{n+1}i
=\left(\sum_{i=1}^{n}i\right)+(n+1)
=\frac{n(n+1)}2+(n+1)
=\frac{(n+1)(n+2)}2.
\]

**Textbook cross-reference:** §5.1.2, “A Familiar Example,” Theorem 5.1.1, printed p. 117 (PDF p. 125), gives the induction proof of this sum formula.

<a id="pdf-page-159"></a>

## PDF page 159 — Further induction statements

The page lists the following statements to prove by induction:
\[
1+3+5+\cdots+(2n-1)=n^2;
\]
\[
1+2+2^2+2^3+\cdots+2^n=2^{n+1}-1;
\]
\[
2^n<n!\qquad(n\ge4);
\]
\[
n<2^n.
\]
No proofs are written on this page.

**Textbook cross-reference:** §5.1, printed pp. 115–123 (PDF pp. 123–131), for induction; §13.1.2, “The Perturbation Method,” printed pp. 505–506 (PDF pp. 513–514), for the geometric-series calculation.

<a id="pdf-page-160"></a>

## PDF page 160 — A faulty induction about balls of one color

**Proposed claim.** Any set of (n) balls has balls of the same color.

**Base case:** one ball.

**Inductive hypothesis:** any (k) balls all have the same color.

The diagram numbers (k+1) balls (1,2,3,\ldots,k,k+1), with overlapping groups
\[
A=\{1,2,\ldots,k\},\qquad B=\{2,3,\ldots,k+1\}.
\]
The intended argument compares the colors in (A) and (B). A small sketch also shows (A=\{1\}) and (B=\{2\}).

**Textbook clarification:** the step fails at \(k=1\), because these two groups have no common ball. For larger \(k\), the overlap would let one compare their colors, but the first inductive step is still missing. See §5.1.6, “A Faulty Induction Proof,” printed pp. 123–124 (PDF pp. 131–132), with the analogous example about horses.

<a id="pdf-page-161"></a>

## PDF page 161 — Informal comments about proof

The handwritten page lists:

- “Proof by sampling” — crossed out.
- “Proof by bullying” — crossed out.
- “Proof by insulting” — checked [the final method name is unclear in source; it may be a humorous expression rather than a formal method].

**Textbook cross-reference:** §1.9, “Good Proofs in Practice,” printed pp. 17–19 (PDF pp. 25–27), gives related guidance about what constitutes a proof. The three expressions above are source comments, not textbook methods.

<a id="pdf-page-162"></a>

## PDF page 162 — Proof by cases and a Ramsey example

**Proof by cases.** The diagrams show a complete graph on four vertices (a square with its diagonals), a complete graph on five vertices (a pentagon with diagonals), and a six-vertex cycle outline. In the five-vertex picture, the five perimeter edges are blue and the five diagonal edges are red.

The stated Ramsey number is
\[
R(3,3)=6,
\]
with the annotation “monochromatic clique.”

**Textbook clarification:** \(R(3,3)=6\) means that every red/blue coloring of all edges of \(K_6\) contains a triangle whose three edges have the same color, while an appropriate coloring of \(K_5\) has none. The rightmost sketch only shows the perimeter of six vertices; the complete graph requires all pairwise edges. See §1.7, “Proof by Cases,” printed pp. 15–16 (PDF pp. 23–24).

<a id="pdf-page-163"></a>

## PDF page 163 — Additional Ramsey numbers

The page records
\[
R(4,4)=18
\]
and
\[
43\le R(5,5)\le47.
\]
The lower bound \(43\le\) is written separately below the upper-bound line.

**Textbook cross-reference:** §1.7, printed pp. 15–16, supplies the smaller \(R(3,3)\) proof-by-cases example. The numerical bounds on this page are lecture statements, not derived on the page.

<a id="pdf-page-164"></a>

## PDF page 164 — Prime products and the induction schema

For \(n>1\), the desired representation is written schematically as
\[
n=\prod_i p_i,
\]
where the \(p_i\) are prime factors.

The page then returns to an induction predicate \(P(n)\), with truth value \(T/F\):

- \(P(0)\) is true.
- Prove \(P(n)\Rightarrow P(n+1)\) for \(n\ge1\) [this lower bound is as written in the source].
- Conclude \(P(n)\) for \(n\in\mathbb N\).

**Textbook clarification:** starting at \(P(0)\) requires the successor implication also at \(n=0\); excluding that first step leaves a gap. See §5.1, printed pp. 115–118. For prime-factorization existence, §5.2, printed pp. 124–126, uses strong induction.

<a id="pdf-page-165"></a>

## PDF page 165 — Strong induction and prime-factorization existence

The strengthened induction scheme is:
\[
P(0)\text{ is true};\qquad
P(0),P(1),\ldots,P(k)\Rightarrow P(k+1).
\]

The example is prime factorization: integers \(2,\ldots,n\) have prime factorizations. Consider \(n+1\).

- If \(n+1\) is prime, its prime factorization is itself.
- Otherwise, \(n+1=pq\), with \(p,q\le n\). Apply the hypothesis to the two smaller factors.

**Textbook cross-reference:** §5.2, “Strong Induction,” printed pp. 124–126 (PDF pp. 132–134), proves that every integer at least \(2\) is a product of primes. Here “prime factorization” concerns existence; uniqueness has not been proved by this argument.

<a id="pdf-page-166"></a>

## PDF page 166 — Ordinary versus strong induction

**Ordinary induction**, for a predicate on \(\mathbb N\):
\[
P(0);\qquad
\forall n\,[P(n)\Rightarrow P(n+1)]
\quad\Longrightarrow\quad
\forall n\in\mathbb N\,P(n).
\]

**Strong induction:** the red annotation replaces the single hypothesis \(P(n)\) by the accumulated hypotheses
\[
P(0),P(1),\ldots,P(n)\Rightarrow P(n+1).
\]

**Textbook cross-reference:** §5.2, printed pp. 124–128, and §5.3, printed pp. 129–130, compare these principles and show their equivalence.

<a id="pdf-page-167"></a>

## PDF page 167 — Weights of three and five kilograms

A heading refers back to prime factorization, followed by the new example: weights of **3 kg** and **5 kg**.

The predicate is written as \(P(n):n+8\), for \(n\ge0\): the intended property is that the weight \(n+8\) can be formed using these weights.

The source considers the first two successor indices, \(n+1=1\) and \(n+1=2\), beside the calculations
\[
3\times3,\qquad2\times5.
\]
For \(n+1>2\), it notes
\[
0\le n-2\le n.
\]

**Textbook clarification:** the natural full property is “\(n+8=3a+5b\) for some nonnegative integers \(a,b\).” The first three target weights are \(8=3+5\), \(9=3+3+3\), and \(10=5+5\). The source writes the two latter calculations and supplies the index inequality needed for the general step. This is an application of the strong-induction method in §5.2, printed pp. 124–128; this precise 3 kg/5 kg example is lecture material.

<a id="pdf-page-168"></a>

## PDF page 168 — Completing the weight example

**Case \(n+1>2\).** The index satisfies
\[
0\le n-2\le n.
\]
Use the earlier case \(P(n-2)\), which represents the weight
\[
(n-2)+8.
\]
Add \(3\) kg to obtain
\[
(n-2)+8+3=n+9=(n+1)+8,
\]
which establishes \(P(n+1)\).

**Textbook cross-reference:** §5.2, printed pp. 124–128, for applying the hypothesis to an earlier index rather than only to the immediately preceding one.

<a id="pdf-page-169"></a>

## PDF page 169 — Prime factorization using well ordering

**Prime factorization.** Let \(P(n)\) mean “a prime factorization of \(n\) exists.” The source mentions \(\mathbb Z_{\ge0}\) and \(\mathbb N\) alongside the notation.

Form the set of counterexamples:
\[
C=\{n:P(n)\text{ does not hold}\}.
\]
Assume \(C\) is a nonempty set of nonnegative integers. By the **well-ordering principle (WOP)**, \(C\) has a smallest element.

**Textbook clarification:** for this property the domain should be integers \(n\ge2\) (or include \(1\) using the empty product); \(0\) is not a product of primes. This domain restriction is essential to the counterexample argument. See §2.3, “Factoring into Primes,” printed p. 30 (PDF p. 38), for this well-ordering argument, and §5.2, printed pp. 124–126 (PDF pp. 132–134), for strong induction.

<a id="pdf-page-170"></a>

## PDF page 170 — The smallest-counterexample argument

Let \(n\in C\) be the smallest counterexample to prime-factorization existence.

It cannot be prime. Therefore
\[
n=ab,\qquad1<a,b<n.
\]
Because \(a,b\) are smaller than \(n\), they each have prime factorizations:
\[
a=p_1p_2\cdots p_r,\qquad
b=q_1q_2\cdots q_s.
\]
Combining them gives
\[
n=p_1p_2\cdots p_rq_1q_2\cdots q_s,
\]
a prime factorization of \(n\), contrary to its membership in \(C\).

**Textbook cross-reference:** Ch. 2, printed pp. 27–29, for the smallest-counterexample proof template; §5.3, printed pp. 129–130, explains its connection to induction.

<a id="pdf-page-171"></a>

## PDF page 171 — The well-ordering proof template

**Well-ordering principle (WOP).** Given a predicate \(P(n)\), define
\[
C=\{n:P(n)\text{ is not true}\}.
\]
Assume \(C\) is nonempty, and use WOP to choose its smallest element \(n_0\in C\). The aim is to derive that \(P(n_0)\) is true, contradicting \(n_0\in C\).

The last handwritten line reads “\(n<n_0\) — \(P(n)\) is not true.” **Source correction:** minimality of the counterexample gives the reverse: \(P(n)\) is true for every eligible \(n<n_0\). The line \(P(n_0)\) “true,” above it, is the contradiction the argument is meant to establish.

**Textbook cross-reference:** §2.2, “Template for Well Ordering Proofs,” printed pp. 28–29 (PDF pp. 36–37).

<a id="pdf-page-172"></a>

## PDF page 172 — Strong-induction proof for three/five kilogram weights

Let \(P(n)\) mean that there exists a combination of the weights giving \(n+8\).

**Base case:** \(P(0)\), representing \(8\) kg.

**Inductive hypothesis:** assume \(P(k)\) for every \(0\le k\le n\). The target \(P(n+1)\) represents \(n+1+8\).

The source splits the successor case into:

1. \(n+1=1\): target weight \(9\).
2. \(n+1=2\): target weight \(10\).
3. \(n+1\ge3\): use \(0\le n-2\le n\).

**Textbook cross-reference:** §5.2, printed pp. 124–128, for the strong-induction structure. The actual target values are quantities represented by the predicate, rather than truth values of \(P\).

<a id="pdf-page-173"></a>

## PDF page 173 — Which earlier case is needed?

The weight represented by \(P(n-2)\) is
\[
(n-2)+8.
\]
Adding \(3\) gives
\[
(n-2)+8+3=(n+1)+8,
\]
the weight needed for \(P(n+1)\).

The diagram crosses out \(P(n)\) and \(P(n-1)\), and leaves \(P(n-2)\) beneath the target \(P(n+1)\), emphasizing that this earlier case is the useful one.

**Textbook cross-reference:** §5.2, printed pp. 124–128.

<a id="pdf-page-174"></a>

## PDF page 174 — Well ordering for a sum and equivalence of induction methods

**Claim.**
\[
1+2+\cdots+n=\frac{n(n+1)}2.
\]

The well-ordering principle says that every nonempty set of nonnegative integers has a smallest element.

Define the counterexample set
\[
C=\left\{n\in\mathbb N:
1+2+\cdots+n\ne\frac{n(n+1)}2\right\}.
\]
Assume \(C\ne\varnothing\). Choose its smallest element \(c\). At \(n=c\), the left and right sides differ, whereas the formula holds for \(n<c\). The page explicitly checks \(n=0\): \(0=0\). Therefore \(c>0\), and \(c-1\ge0\) with \(c-1<c\).

At that smaller value,
\[
1+2+\cdots+(c-1)=\frac{c(c-1)}2.
\]
Add \(c\):
\[
1+2+\cdots+c
=\frac{c(c-1)}2+c
=\frac{c(c+1)}2.
\]
This contradicts \(c\in C\), so \(C=\varnothing\). The red annotation \(C=\varnothing\) records the desired conclusion.

The bottom of the page compares **ordinary induction**, **strong induction**, and **WOP**. To convert accumulated hypotheses into one predicate, it introduces
\[
P'(n)=\bigwedge_{i=1}^{n}P(i).
\]
The brace groups \(P(0),\ldots,P(n)\), beside the strong successor implication to \(P(n+1)\). [Source indexing mismatch: the displayed conjunction appears to start at \(1\), while the brace starts at \(0\).]

**Textbook clarification:** with a base case at \(0\), use \(Q(n)=\bigwedge_{i=0}^{n}P(i)\); ordinary induction on \(Q\) packages the strong-induction hypotheses. See §5.3, printed pp. 129–130 (PDF pp. 137–138). The sum proof by WOP is §2.2, printed pp. 28–29, and by induction is §5.1.2, printed p. 117.

<a id="pdf-page-175"></a>

## PDF page 175 — Recursive objects: bases and constructors

Examples of objects discussed before recursive definitions:

- Natural numbers: \(0,1,2,3,4,\ldots\), with \(0\in\mathbb N\) and \(\operatorname{Succ}(n)=n+1\).
- The string “A BROWN FOX.”
- An arithmetic expression \(4n^2+(3n+1)\).
- Chess.
- A rooted tree: the root has a left leaf and a right child; that right child has two leaf children.
- A string of nested brackets [exact bracket sequence unclear in source].

The red annotations identify **base** cases and **constructors**, and show the recursive-function proof pattern \(f(0)\), followed by a relation from \(f(n)\) to \(f(n+1)\). A small pair notation beside the bracket example is [unclear in source].

**Textbook cross-reference:** §6.1, “Recursive Definitions and Structural Induction,” printed pp. 173–176 (PDF pp. 181–184); §6.2, “Strings of Matched Brackets,” printed pp. 177–179 (PDF pp. 185–187); §6.4, “Arithmetic Expressions,” printed pp. 183–188 (PDF pp. 191–196).

<a id="pdf-page-176"></a>

## PDF page 176 — Recursive definitions need valid base cases

For \(\mathbb N\):

- **Base:** \(0\).
- **Constructor:** \(\operatorname{Succ}(n)=n+1\).

The page lists \(n!\) and a summation symbol as further recursive examples.

It then writes
\[
f(n)=3+f(n-1),\qquad n\in\mathbb N,
\]
and another proposed definition
\[
f(n)=
\begin{cases}
0,&n=0,\\
f(n+1),&\text{otherwise}.
\end{cases}
\]
These are grouped for discussion.

**Textbook clarification:** the first needs a specified starting value and must use its step only when \(n\ge1\). The second calls larger arguments and does not reduce a positive input to the given base case, so it does not by itself uniquely define the intended function. See §6.3, “Recursive Functions on Nonnegative Integers,” printed pp. 180–182 (PDF pp. 188–190).

<a id="pdf-page-177"></a>

## PDF page 177 — Overlapping cases and the Collatz recursion

A crossed-out piecewise proposal is
\[
f(n)=
\begin{cases}
0,&n\text{ divisible by }2,\\
1,&n\text{ divisible by }3,\\
2,&\text{otherwise}.
\end{cases}
\]
**Clarification:** the first two cases overlap at multiples of \(6\), where they assign different outputs; the cross indicates that this is invalid without a priority rule or disjoint cases.

The next proposal is
\[
f(n)=
\begin{cases}
1,&n\le1,\\
f(n/2),&n\text{ even},\\
f(3n+1),&n\text{ odd}.
\end{cases}
\]
The page labels this **Collatz conjecture**, writes “\(3n+1\),” and indicates \(n\in\mathbb N\longrightarrow1\). It notes “claim.”

**Textbook cross-reference:** §6.3.2, “Ill-formed Function Definitions,” printed pp. 181–182 (PDF pp. 189–190), contains both the overlapping divisibility example and the Collatz recursion. The base condition has priority; the even/odd cases apply for \(n>1\).

<a id="pdf-page-178"></a>

## PDF page 178 — Ackermann function and very rapid growth

The source labels the following recursion **Ackermann**:
\[
A(m,n)=
\begin{cases}
2n,&m=0\text{ or }n\le1,\\
A(m-1,A(m,n-1)),&\text{otherwise}.
\end{cases}
\]
[The first condition's \(m=0\) is handwritten with a dash/equality mark; the displayed condition is the most readable interpretation.]

The examples recorded are
\[
A(1,2)=4,\qquad A(3,2)=29.
\]
For \(A(4,2)\), the source draws a tower of powers of \(2\), subtracts \(1\), writes an up-arrow expression that appears to be \(2\uparrow\uparrow2-1\), and notes “approximately 20,000 digits.” [The exact tower height/arrow parameter is unclear in source.]

**Source consistency note:** the displayed recurrence and the listed value \(A(3,2)=29\) do not fit the same convention: under the displayed base \(2n\) for \(n\le1\), \(A(3,2)=4\). Ackermann-function conventions vary; this page mixes notation or contains a copying error. The uncertain tower formula is therefore retained descriptively instead of silently repaired.

**Textbook cross-reference:** §6.3.2, printed pp. 182–183 (PDF pp. 190–191), equations (6.6)–(6.7), gives exactly the displayed recurrence. Problem 6.17, printed pp. 199–200 (PDF pp. 207–208), asks for its well-definedness proof.

<a id="pdf-page-179"></a>

## PDF page 179 — Repeated operations

\[
\operatorname{Succ}(n)=n+1.
\]

**Addition:** \(3+5\) is obtained by applying the successor operation five times to \(3\), giving \(8\). The source writes a successor expression with an index \(i=0,\ldots,4\).

**Multiplication:**
\[
3\times5=\underbrace{3+3+3+3+3}_{5\text{ terms}}.
\]

**Exponentiation:**
\[
3^5=\underbrace{3\times3\times3\times3\times3}_{5\text{ factors}}.
\]

**Textbook cross-reference:** §6.3, printed pp. 180–182, for defining numerical operations recursively. The operation hierarchy is lecture context.

<a id="pdf-page-180"></a>

## PDF page 180 — Tetration, pentation, and Knuth arrows

**Tetration** repeats exponentiation. The page writes
\[
{}^{3}3=3^{\,3^3}=3^{27}\approx7\times10^{12}.
\]
This is \(3\uparrow\uparrow3\) in **Knuth's arrow notation**; an ordinary exponentiation is \(3\uparrow3\).

**Pentation** repeats tetration. The main expression is
\[
3\uparrow\uparrow\uparrow3
=3\uparrow\uparrow(3\uparrow\uparrow3).
\]
The inner \(3\uparrow\uparrow3\) is annotated as roughly \(7\times10^{12}\). Red notes restate the relation between arrows and the nested power-tower drawing.

**Textbook cross-reference:** §6.3, printed pp. 180–182, gives related recursive-function background. Tetration, pentation, and Knuth arrows are lecture material and are not developed in that section.

<a id="pdf-page-181"></a>

## PDF page 181 — Recursive data type of strings

A **recursive data type (RDT)** is specified by **base case(s)** and **constructor case(s)**.

**Example: strings of characters.** Let \(A\) be an alphabet, \(a\in A\), and let \(A^*\) be the set of strings.

**Base:** the empty string \(\lambda\in A^*\).

**Constructor:** if \(a\in A\) and \(s\in A^*\), then
\[
\langle a,s\rangle\in A^*.
\]
Here \(\langle a,s\rangle\) prepends character \(a\) to string \(s\).

**Textbook cross-reference:** §6.1, printed pp. 173–174 (PDF pp. 181–182), defines strings using this base and constructor.

<a id="pdf-page-182"></a>

## PDF page 182 — String length and structural induction

Write \(|s|\) for the **length** of \(s\).

**Base:** \(|\lambda|=0\).

**Constructor:**
\[
|\langle a,s\rangle|=1+|s|.
\]

**Structural induction.**

- Prove \(P\) for the base cases.
- Show that each constructor preserves \(P\) from its component objects.
- Then all elements of the recursive data type have \(P\).

**Textbook cross-reference:** §6.1, Definition 6.1.2, printed p. 174 (PDF p. 182), defines string length; §6.1.1, “Structural Induction,” printed pp. 175–176 (PDF pp. 183–184), gives the proof method.

<a id="pdf-page-183"></a>

## PDF page 183 — Formal structural-induction principle

Let \(P\) be a predicate defined on a recursive data type \(R\).

If:

1. \(P(b)\) holds for every base object \(b\in R\), and
2. each constructor preserves \(P\), for example
\[
[P(r)\land P(s)]\Rightarrow P(c(r,s)),
\]

then \(P(r)\) holds for all \(r\in R\).

**Textbook cross-reference:** §6.1.1, “Structural Induction,” printed pp. 175–176 (PDF pp. 183–184).

<a id="pdf-page-184"></a>

## PDF page 184 — Length of concatenated strings

**Claim.** For all \(s,t\in A^*\),
\[
|s\cdot t|=|s|+|t|.
\]
An example string “abcd” is written at the upper right.

Define
\[
P(s):\quad\forall t\in A^*,\ |s\cdot t|=|s|+|t|.
\]
Prove \(P(s)\) by structural induction on \(s\).

**Base \(s=\lambda\):**
\[
|\lambda\cdot t|=|t|=0+|t|=|\lambda|+|t|.
\]

**Constructor \(s=\langle a,r\rangle\):** assuming \(P(r)\),
\[
\begin{aligned}
|\langle a,r\rangle\cdot t|
&=1+|r\cdot t|\\
&=1+|r|+|t|\\
&=|\langle a,r\rangle|+|t|\\
&=|s|+|t|.
\end{aligned}
\]

**Textbook cross-reference:** §6.1.1, Theorem 6.1.4, printed pp. 175–176 (PDF pp. 183–184), includes this structural-induction argument.

<a id="pdf-page-185"></a>

## PDF page 185 — Arithmetic expressions as a recursive data type

The data type is **Aexp**, the set of arithmetic expressions. Examples written at the side include \(x^3+x+1\) and \(3x+1\).

**Base cases:**
\[
x\in\mathrm{Aexp},\qquad k\in\mathrm{Aexp}\quad(k\in\mathbb Z).
\]

**Constructor cases:** for \(e,f\in\mathrm{Aexp}\),
\[
\operatorname{sum}(e,f)=[e+f]\in\mathrm{Aexp};
\]
\[
\operatorname{product}(e,f)=[e*f]\in\mathrm{Aexp};
\]
\[
[-e]\in\mathrm{Aexp}.
\]

**Textbook cross-reference:** §6.4, “Arithmetic Expressions,” Definition 6.4.1, printed pp. 183–184 (PDF pp. 191–192), defines the Aexp data type.

<a id="pdf-page-186"></a>

## PDF page 186 — Hyperoperations and Graham's number

The heading is **hexation**, illustrated by four up-arrows. The page defines a sequence using the following indexing:
\[
g_0=3\uparrow\uparrow\uparrow\uparrow3
\]
(four arrows),
\[
g_1=3\underbrace{\uparrow\cdots\uparrow}*{g_0\text{ arrows}}3,
\qquad
g_2=3\underbrace{\uparrow\cdots\uparrow}*{g_1\text{ arrows}}3,
\]
and, at the last step,
\[
g_{63}=3\underbrace{\uparrow\cdots\uparrow}*{g*{62}\text{ arrows}}3.
\]
An arrow labels \(g_{63}\) as **Graham's number**. “HYPEROPERATIONS” is written in red at the bottom.

**Textbook cross-reference:** §6.3, printed pp. 180–183, provides recursive-function context; the hyperoperation sequence and Graham's number on this page are additional lecture material.

<a id="pdf-page-187"></a>

## PDF page 187 — TREE and comparisons of very large numbers

The page records the qualitative comparison
\[
\mathrm{TREE}(3)\gg\text{Graham's number}.
\]
It also writes a much-smaller comparison with an iterated Ackermann expression, appearing as
\[
A^A(187\ldots)
\]
[the exponent/iteration notation and the complete argument are unclear in source].

A two-way vertical arrow links \(\mathrm{TREE}(3)\) to the general notation \(\mathrm{TREE}(n)\). The lower-right fragment “R & B” is retained [meaning unclear in source].

**Textbook cross-reference:** §6.3.2, printed pp. 182–183, discusses Ackermann growth. TREE and the displayed size comparisons are lecture context, not definitions or proofs supplied by this textbook section.

<a id="pdf-page-188"></a>

## PDF page 188 — Evaluation, substitution, and equivalent models

**Aexp is a recursive data type.** For example,
\[
x^2+1\equiv[[x*x]+1].
\]

**Evaluation.** Set \(x=n\), where \(n\in\mathbb Z\). The function has type
\[
\operatorname{eval}:\mathrm{Aexp}\times\mathbb Z\to\mathbb Z.
\]
Its base rules are
\[
\operatorname{eval}(x,n)=n,\qquad
\operatorname{eval}(k,n)=k.
\]
Its constructor rules are
\[
\operatorname{eval}([e_1+e_2],n)
=\operatorname{eval}(e_1,n)+\operatorname{eval}(e_2,n);
\]
\[
\operatorname{eval}([e_1*e_2],n)
=\operatorname{eval}(e_1,n)\operatorname{eval}(e_2,n);
\]
\[
\operatorname{eval}([-e],n)=-\operatorname{eval}(e,n).
\]

**Example:**
\[
\begin{aligned}
\operatorname{eval}(3+x^2,2)
&=\operatorname{eval}([3+[x*x]],2)\\
&=\operatorname{eval}(3,2)+\operatorname{eval}([x*x],2)\\
&=3+\operatorname{eval}(x,2)\operatorname{eval}(x,2)\\
&=3+(2\cdot2)=7.
\end{aligned}
\]

**Substitution.** Replace \(x\) in one expression by another expression. The initial example replaces \(x\) by \(3x\) in \(x^2+1\), yielding \(9x^2+1\).

The source uses the argument order
\[
\operatorname{subs}(f,e):\mathrm{Aexp}\times\mathrm{Aexp}\to\mathrm{Aexp},
\]
meaning “substitute \(f\) for every \(x\) in \(e\).” The base rules are
\[
\operatorname{subs}(f,x)=f,\qquad
\operatorname{subs}(f,k)=k.
\]
The constructor rules are
\[
\operatorname{subs}(f,[e_1+e_2])
=[\operatorname{subs}(f,e_1)+\operatorname{subs}(f,e_2)];
\]
\[
\operatorname{subs}(f,[e_1*e_2])
=[\operatorname{subs}(f,e_1)*\operatorname{subs}(f,e_2)];
\]
\[
\operatorname{subs}(f,[-e])=[-\operatorname{subs}(f,e)].
\]

**Examples and diagrams.**

- \(\operatorname{subs}(3x,x^2+1)=\operatorname{subs}([3*x],[[x*x]+1])\), giving \(9x^2+1\).
- \(\operatorname{eval}(\operatorname{subs}(3x,x(x-1)),2)
=\operatorname{eval}(x(x-1),\operatorname{eval}(3x,2))\).
- The first route is the **substitution model**: form \(3x(3x-1)\), then evaluate at \(x=2\).
- The second route is the **environment model**: evaluate \(3x\) at \(2\), obtaining \(6\), then evaluate \(x(x-1)\) at \(6\), obtaining \(6(6-1)\).
- Another isolated expression below is \(x(2x+1)\); its intended role is not stated.

The general assertion is that, for all \(e,f\in\mathrm{Aexp}\) and \(n\in\mathbb Z\),
\[
\boxed{\operatorname{eval}(\operatorname{subs}(f,e),n)
=\operatorname{eval}(e,\operatorname{eval}(f,n)).}
\]
The left side is labeled substitution model; the right side, environment model.

**Proof by structural induction on \(e\).**

For \(e=x\), both sides equal \(\operatorname{eval}(f,n)\). For \(e=k\), both sides equal \(k\).

For the sum case \(e=[e_1+e_2]\), assume for each component that
\[
\operatorname{eval}(\operatorname{subs}(f,e_i),n)
=\operatorname{eval}(e_i,\operatorname{eval}(f,n)).
\]
Then
\[
\begin{aligned}
\operatorname{eval}(\operatorname{subs}(f,[e_1+e_2]),n)
&=\operatorname{eval}([\operatorname{subs}(f,e_1)+\operatorname{subs}(f,e_2)],n)\\
&=\operatorname{eval}(\operatorname{subs}(f,e_1),n)
+\operatorname{eval}(\operatorname{subs}(f,e_2),n)\\
&=\operatorname{eval}(e_1,\operatorname{eval}(f,n))
+\operatorname{eval}(e_2,\operatorname{eval}(f,n))\\
&=\operatorname{eval}([e_1+e_2],\operatorname{eval}(f,n)).
\end{aligned}
\]
The handwritten proof ends after this sum case.

**Textbook clarification:** the product and negation cases follow by the same respective evaluation/substitution rules, replacing the final addition by multiplication or unary negation. See §6.4.1, “Evaluation and Substitution with Aexp's,” Definitions 6.4.2–6.4.3 and Theorem 6.4.4, printed pp. 184–188 (PDF pp. 192–196). The general identity and its proof are on printed pp. 187–188 (PDF pp. 195–196). The textbook writes \(\operatorname{subst}(f,e)\), with the **same argument order** as this page's \(\operatorname{subs}(f,e)\).

<a id="pdf-page-189"></a>

## PDF page 189 — Relations viewed as arrows

The page writes a relation as \(R:A\to B\) and draws several arrow diagrams. Some elements of \(A\) have no outgoing arrow, others have one, and others have more than one; elements of \(B\) can receive multiple arrows.

The annotations identify:

- **Function:** at most one outgoing arrow from each element of \(A\).
- **Total:** at least one outgoing arrow from each element of \(A\).
- **Surjective:** at least one incoming arrow at every element of \(B\).
- **Injective:** at most one incoming arrow at every element of \(B\).

Taken together, “function” and “total” give exactly one output for every input.

**Textbook cross-reference:** §4.4, “Binary Relations,” starts at printed p. 89 (PDF p. 97); §4.4.1, “Relation Diagrams,” printed pp. 90–91 (PDF pp. 98–99), gives the arrow representation and Definition 4.4.2 of the relation properties.

<a id="pdf-page-190"></a>

## PDF page 190 — A relation diagram and function properties

The sets shown are
\[
A=\{a,b,c,d,e\},\qquad B=\{1,2,3,4\}.
\]
Clearly visible arrows are \(a\to1\), \(d\to2\), and \(c\to4\). The drawing leaves \(b,e\) with no outgoing arrow and \(3\) with no incoming arrow. The labels to the right are “total,” “surjective,” and “injective \(f\)” [no clear final truth-value marks are attached].

**Clarification of the shown arrows:** they define an injective partial function, but the relation is not total on the displayed \(A\) and does not hit every element of the displayed \(B\).

**Textbook cross-reference:** §4.4.1, “Relation Diagrams,” and Definition 4.4.2, printed pp. 90–91 (PDF pp. 98–99), for the arrows and function properties. §4.5 is “Finite Cardinality,” beginning at printed p. 93 (PDF p. 101).

<a id="pdf-page-191"></a>

## PDF page 191 — Arrow definitions of relation properties

Let \(R:A\to B\) be a relation. The page lists the following definitions, understood at every point in the indicated set:

- \(R\) is a **function** if it has the \([\le 1\text{ arrow out}]\) property.
- \(R\) is **total** if it has the \([\ge 1\text{ arrow out}]\) property.
- \(R\) is **surjective** if it has the \([\ge 1\text{ arrow in}]\) property.
- \(R\) is **injective** if it has the \([\le 1\text{ arrow in}]\) property.
- The final handwritten line says “bijective if both \([\ge1\text{ arrow in}]\) and \([\le1\text{ arrow in}]\) hold.” Thus the written condition ensures exactly one incoming arrow at every point of \(B\), but omits a condition on outgoing arrows.

**Textbook clarification:** Definition 4.4.2 requires a bijection to have **both exactly one outgoing arrow at every domain point and exactly one incoming arrow at every codomain point**. The handwritten final line should therefore also include the function and total requirements. See §4.4.1, “Relation Diagrams,” printed pp. 90–91 (PDF pp. 98–99).

<a id="pdf-page-192"></a>

## PDF page 192 — Counting arrows in a surjective function

Consider a function \(R:A\to B\). A schematic diagram has a left oval labelled \(A\), a right oval labelled \(B\), and arrows entering the right-hand points. It illustrates the counting argument rather than giving named elements or a fully specified relation.

Because a function has at most one outgoing arrow per domain element,
\[
|A|\ge \#\text{arrows out}.
\]
If it is also a surjection, each codomain point has at least one incoming arrow, so
\[
\#\text{arrows in}\ge |B|.
\]
Every arrow is counted once at its start and once at its end. Combining the inequalities gives
\[
R\text{ is a surjective function }\Longrightarrow |A|\ge |B|.
\]
The last line abbreviates the conclusion as
\[
A\mathrel{\mathrm{surj}}B\Longrightarrow |A|\ge |B|.
\]

**Textbook clarification:** this numerical arrow-count argument is for **finite sets**. The notation \(A\mathrel{\mathrm{surj}}B\) means that some surjective function from \(A\) to \(B\) exists, rather than that every relation from \(A\) to \(B\) is surjective. See §4.5, printed pp. 93–94 (PDF pp. 101–102), Definition 4.5.2 and Lemma 4.5.3.

<a id="pdf-page-193"></a>

## PDF page 193 — Surj, inj, and bij notation

Let \(A,B\) be sets. The definitions are:
\[
A\mathrel{\mathrm{surj}}B
\quad\Longleftrightarrow\quad
\text{there exists a surjective function from }A\text{ to }B;
\]
\[
A\mathrel{\mathrm{inj}}B
\quad\Longleftrightarrow\quad
\text{there exists a total injective relation from }A\text{ to }B;
\]
\[
A\mathrel{\mathrm{bij}}B
\quad\Longleftrightarrow\quad
\text{there exists a bijection from }A\text{ to }B.
\]
The handwriting calls the middle map “total injective”; the word “total” has a crossing stroke but remains readable. No proof or example is added on this page.

**Textbook cross-reference:** Definition 4.5.2, §4.5, printed p. 94 (PDF p. 102). The textbook explicitly uses a total injective **relation** in the definition of \(\mathrm{inj}\); it need not satisfy the function property as part of that definition.

<a id="pdf-page-194"></a>

## PDF page 194 — Mapping rules for finite sets

**Lemma.** For finite sets \(A,B\),
\[
A\mathrel{\mathrm{surj}}B\Longleftrightarrow |A|\ge |B|;
\]
\[
A\mathrel{\mathrm{inj}}B\Longleftrightarrow |A|\le |B|;
\]
\[
A\mathrel{\mathrm{bij}}B\Longleftrightarrow |A|=|B|.
\]

**Example diagram.** A five-element set is placed above a two-element set. Using \(a_1,\ldots,a_5\) and \(b_1,b_2\) for the displayed indexed elements, the arrows show
\[
a_1\mapsto b_1,\qquad
a_2\mapsto b_2,\qquad
a_3,a_4,a_5\mapsto b_2.
\]
This is a total surjective function from the larger finite set onto the smaller one. The drawing supplies the construction; no separate proof of the three equivalences appears here.

**Textbook cross-reference:** Theorem 4.5.4, “Mapping Rules,” printed p. 95 (PDF p. 103). The preceding construction and Lemma 4.5.3 appear on printed pp. 93–94 (PDF pp. 101–102).

<a id="pdf-page-195"></a>

## PDF page 195 — Equal size of infinite sets and pairing functions

**Infinite sets.** Let \(A,B\) be sets. The page defines “\(A\) is of the same size as \(B\)” by the existence of a bijection:
\[
\exists R:A\to B\quad\text{such that }R\text{ is bijective}.
\]
The words “same size” are in quotation marks and the definition is bracketed in red.

Below it, \(\mathbb N\) and \(\mathbb Q\) are connected by a left-pointing arrow (from the \(\mathbb Q\) side toward \(\mathbb N\)); no mapping rule is written. The labels “pairing functions” and “Cantor's pairing” appear beneath it. A large unlabelled zigzag sweeps successive diagonal bands inside a roughly drawn pair of axes. It indicates a diagonal enumeration, but no grid coordinates or pairing formula are supplied.

The right margin lists the pairs
\[
(1,2),\qquad (2,4),\qquad (3,6).
\]
Their connection to the zigzag is not explained in the source.

**Textbook cross-reference:** §7.1, “Infinite Cardinality,” begins at printed p. 206 (PDF p. 214). It defines size comparison through mappings and discusses countable sets and diagonal enumeration. The source's mention of a named Cantor pairing function does not supply its explicit algebraic formula; none has been inserted here.

<a id="pdf-page-196"></a>

## PDF page 196 — Ice-cream selections encoded by bits

There are five available ice-cream flavours, labelled \(A,B,C,D,E\). How many ways are there to choose twelve ice creams when flavour multiplicities matter and order is disregarded?

The diagram uses a zero for an ice cream and a one as a separator between consecutive flavours. Its example is
\[
\underbrace{00000}*{A}\;1\;
\underbrace{00000}*{B}\;1\;
\underbrace{00}*{C}\;1\;
\underbrace{\phantom{00}}*{D}\;1\;
\underbrace{\phantom{00}}_{E}.
\]
Thus the flavour counts are \((5,5,2,0,0)\). Empty runs represent zero selections of that flavour. Red circles highlight the first three runs, and an oval spans the encoding up to the fourth separator.

Twelve zeros plus four ones form a **16-bit string with four ones**. The circled count is
\[
\binom{16}{4}.
\]
The general circled expression is
\[
\boxed{\binom{n+k-1}{k-1}},
\]
for \(n\) ice creams and \(k\) flavours.

**Textbook cross-reference:** §14.1 uses the analogous selection of flavoured donuts and its bit-sequence bijection, printed pp. 551–552 (PDF pp. 559–560). Corollaries 14.5.2–14.5.3, printed p. 563 (PDF p. 571), give the resulting count. Choosing the separator positions or the zero positions yields equal binomial coefficients.

<a id="pdf-page-197"></a>

## PDF page 197 — Mediant fractions and strictly smaller sets

**Stern–Brocot tree.** The top of the page displays
\[
\frac01,\qquad \frac11,\qquad \frac10,
\]
with arrows toward the label “Stern–Brocot tree.” Here \(1/0\) is a formal endpoint, rather than an ordinary rational number.

The displayed fraction construction is
\[
\frac mn,\ \frac{m'}{n'}
\quad\longmapsto\quad
\frac{m+m'}{n+n'}.
\]
The right margin again lists \((1,2),(2,4),(3,6)\); no accompanying rule explains these pairs.

**Size comparison.** “\(A\) is at least as big as \(B\)” is represented by
\[
A\mathrel{\mathrm{surj}}B.
\]
The red boxed definition is
\[
\boxed{A\mathrel{\mathrm{strict}}B
\quad\Longleftrightarrow\quad
\neg(A\mathrel{\mathrm{surj}}B).}
\]
For finite sets \(A,B\),
\[
A\mathrel{\mathrm{strict}}B\quad\Longleftrightarrow\quad |A|<|B|.
\]

**Proof.** Using the finite mapping rule,
\[
\begin{aligned}
A\mathrel{\mathrm{strict}}B
&\Longleftrightarrow \neg(A\mathrel{\mathrm{surj}}B)\\
&\Longleftrightarrow \neg(|A|\ge |B|)\\
&\Longleftrightarrow |A|<|B|.
\end{aligned}
\]

**Textbook cross-reference:** Definition 7.1.1 and Corollary 7.1.2, §7.1, printed p. 206 (PDF p. 214), match the definition and proof. The Stern–Brocot tree is not covered by this textbook passage; the notes give only its endpoint fractions and mediant construction here.

<a id="pdf-page-198"></a>

## PDF page 198 — Unordered flavour counts and ordered choices

Choose twelve ice creams when five flavours are available. The page repeats the separator encoding and writes the count
\[
\binom{16}{4}=1820\text{ ways}.
\]

The illustration has five labelled flavour blocks separated by four ones. It draws three zeros in each of the first four blocks, leaving the fifth empty:
\[
\underbrace{000}*{A}1\underbrace{000}*{B}1
\underbrace{000}*{C}1\underbrace{000}*{D}1
\underbrace{\phantom{000}}_{E}.
\]
Arrows point upward to the flavour labels. A second sketch has a sequence of choice slots, with “5” written above the first three slots to indicate five available choices at each step. The page writes
\[
5^{12}\sim 2\times10^8.
\]

**Textbook clarification:** \(5^{12}=244{,}140{,}625\) counts **ordered** sequences of twelve flavour choices, whereas \(1820\) counts flavour multiplicities with order disregarded. These are different objects, which explains the different counts. See §14.2.1, “The Product Rule,” printed pp. 552–553 (PDF pp. 560–561), and §14.5.2, printed p. 563 (PDF p. 571).

<a id="pdf-page-199"></a>

## PDF page 199 — Two ice creams from two flavours

Choose two ice creams when two flavours \(A,B\) are available. The two choice slots give
\[
2^2=4\text{ ordered ways}:
\qquad AA,\ AB,\ BA,\ BB.
\]
The source circles \(AA\) and \(BB\) separately and encloses \(AB,BA\) together, indicating that the latter two represent the same flavour multiplicities. It marks a resulting count of three:
\[
\binom31=3\text{ ways}.
\]
The equivalent expression \(\binom32\) is written below.

The lower-right sketch has three groups of short parallel strokes, separated by vertical bars, with a second row of circled and crossed-out letters underneath. Some arrows point up from rewritten letters to these groups. The exact overwritten letter labels and the final small expression are **[unclear in source]**; no additional numerical conclusion is legible there.

**Textbook clarification:** the unordered outcomes are exactly \((2,0),(1,1),(0,2)\), so the general formula \(\binom{n+k-1}{k-1}\) with \(n=k=2\) gives \(\binom31=3\). The grouping is not uniformly two-to-one: \(AA\) and \(BB\) each represent one ordered sequence, whereas the mixed outcome represents two. See §14.1 and Corollary 14.5.3, printed pp. 551–552 and 563 (PDF pp. 559–560 and 571).

<a id="pdf-page-200"></a>

## PDF page 200 — Counting rules, grid paths, and the pigeonhole principle

**Generalized product rule.** Three choice slots appear beneath the heading. The example count is
\[
5\times4\times3.
\]
No particular objects or restrictions for these slots are specified in the handwriting.

**Sum rule.** If \(A,B\) are disjoint,
\[
|A\cup B|=|A|+|B|.
\]

**Passwords of length 6, 7, or 8.** The initial letter set has 52 elements:
\[
F=\{a,b,c,\ldots,z,A,B,C,\ldots,Z\}.
\]
The set for the remaining positions is drawn as the 52-letter set together with the digits \(0,1,\ldots,9\), giving
\[
|R|=62.
\]
Valid passwords belong to
\[
(F\times R^5)\cup(F\times R^6)\cup(F\times R^7).
\]
Since these length classes are disjoint, their total number is
\[
|F||R|^5+|F||R|^6+|F||R|^7.
\]

**Division rule.** If a function \(f:A\to B\) is \(k\)-to-one,
\[
|A|=k|B|.
\]
Several circular seating diagrams label four people \(p_1,p_2,p_3,p_4\) around a circle and equate drawings that differ by rotation. A margin label says “4-to-1.” For \(n\) people, the written count is
\[
\frac{n!}{n}=(n-1)!.
\]
The notes describe the map as \(n\)-to-one.

**Subset rule.** A sketch splits \(n\) elements into a selected group of size \(k\) and a remaining group of size \(n-k\). The circled notation is
\[
\binom nk.
\]
The next sketch splits the elements into groups of sizes \(k_1,k_2,\ldots,k_m\), with
\[
n=k_1+k_2+\cdots+k_m,
\]
and writes the corresponding multinomial coefficient notation.

**Textbook clarification:** the explicit formulas for these displayed counts are
\[
\binom nk=\frac{n!}{k!(n-k)!},
\qquad
\binom{n}{k_1,k_2,\ldots,k_m}
=\frac{n!}{k_1!k_2!\cdots k_m!}.
\]
They are the Subset Rule and Subset Split Rule, §14.5.1 and §14.6.1, printed pp. 562–564 (PDF pp. 570–572).

**Grid paths.** An \(n\)-by-\(n\) square grid is drawn with start \(A\) at its upper-left corner and end \(B\) at its lower-right corner. The permitted directions are right and down, indicated by two arrows. A path has \(n\) right moves and \(n\) down moves, for \(2n\) moves total. The written count is
\[
\binom{2n}{n}.
\]
A smaller 2-by-2 grid is labelled with the count \(6\). A further grid appears near the next heading without an additional written path count.

**Pigeonhole principle.** First the page writes \(|P|>|H|\), for pigeons and holes. In function notation: if
\[
|A|>|B|,
\]
then every total function \(f:A\to B\) maps two different elements of \(A\) to the same element of \(B\). Here \(A\) is the set of pigeons, \(B\) the set of pigeonholes, and \(f\) assigns each pigeon to its hole.

**Generalized pigeonhole principle.** If
\[
|A|>k|B|,
\]
then a total function \(f:A\to B\) maps at least \(k+1\) distinct elements of \(A\) to the same element of \(B\).

**Hair-count example.** The source gives a population of Delhi of
\[
|A|=1,50,00,000=15{,}000{,}000.
\]
An initial hair annotation says “\(<10{,}000\) hair,” beside a bracket running from \(10{,}000\) to \(2,00,000\). Later it defines
\[
B=\{10{,}000,\ldots,1,60,000\}
\]
and writes \(|B|=1,50,000\). Let \(f\) map a person to the number of hairs on their head. The final implication is
\[
|A|>99|B|
\quad\Longrightarrow\quad
\text{100 people in Delhi have the same number of hairs.}
\]

**Textbook clarification:** the two upper hair bounds on this page disagree, and the initial “\(<10{,}000\)” does not agree with the later minimum of \(10{,}000\). The later inclusive range actually has \(160{,}000-10{,}000+1=150{,}001\) values; the inequality \(15{,}000{,}000>99\cdot150{,}001\) still holds. The conclusion of 100 people follows **if all people counted in \(A\) have hair counts in that later range**. The source does not justify that population assumption. The textbook's related example uses non-bald people in Boston and different numerical bounds; see §14.8.1, printed p. 574 (PDF p. 582).

**Textbook cross-references for the counting rules:** §14.2.3–14.2.4, printed pp. 554–555 (PDF pp. 562–563), for the sum rule and this password example; §14.3, printed pp. 555–558 (PDF pp. 563–566), for the generalized product rule; §14.4, printed pp. 559–561 (PDF pp. 567–569), for the division rule and circular seating; Rules 14.8.1–14.8.2, printed pp. 573–574 (PDF pp. 581–582), for the two pigeonhole principles.

<a id="pdf-page-201"></a>

## PDF page 201 — Subsets with the same sum

The heading is “Subset Sum Problem: NP-hard.” A preliminary sketch shows a list of numbers bracketed beside “+ve” and “−ve,” and another small sketch puts a plus sign and a division sign in separate brackets. No precise equation or decision problem is stated in those preliminary sketches.

The main example concerns **90 positive 25-digit numbers**, represented by a large bracketed list. It asks for two subsets with the same sum.

Let \(A\) be the collection of all subsets of the 90 numbers and let \(B\) contain the possible sums. The page gives
\[
|A|=2^{90}\approx1.24\times10^{27},
\]
and
\[
|B|=90\times10^{25}+1
\le0.901\times10^{27}.
\]
Thus
\[
|A|>|B|,
\]
so there are at least two different subsets with the same sum, by applying the pigeonhole principle to the map that sends a subset to its sum.

**Textbook cross-reference:** §14.8.2, “Subsets with the Same Sum,” printed pp. 574–575 (PDF pp. 582–583), gives exactly this 90-number argument. It uses the safe codomain \(B=\{0,1,\ldots,90\cdot10^{25}\}\); the sum of every subset lies there. The source does not list the actual 25-digit numbers on this page. Its NP-hard label is a separate complexity remark, rather than a proof that finding the particular colliding subsets is NP-hard.

<a id="pdf-page-202"></a>

## PDF page 202 — Inclusion–exclusion and combinatorial identities

**Two sets.** For disjoint \(A,B\), the sum rule gives
\[
|A\cup B|=|A|+|B|.
\]
In general,
\[
|A\cup B|=|A|+|B|-|A\cap B|.
\]

**Electrical engineering, mathematics, and physics.** Let \(E,M,P\) be the respective student sets. The written data are
\[
|E|=200,\qquad |M|=60,\qquad |P|=40.
\]
The counts for exactly the indicated pair of subjects are:

- Mathematics and electrical engineering: \(4\).
- Mathematics and physics: \(3\).
- Electrical engineering and physics: \(11\).
- All three subjects: \(2\).

Consequently,
\[
|E\cap M|=4+2=6,
\qquad |E\cap P|=11+2=13,
\qquad |P\cap M|=3+2=5.
\]
The inclusion–exclusion formula is
\[
\begin{aligned}
|E\cup M\cup P|
={}&|E|+|M|+|P|\\
&-|E\cap M|-|E\cap P|-|P\cap M|\\
&+|E\cap M\cap P|.
\end{aligned}
\]
The handwritten substitution is
\[
60+200+40-6-13-5+2.
\]
**Textbook clarification:** this expression equals \(278\). The counts labelled by a pair have been interpreted as **exactly** that pair, as required by the source's subsequent addition of the triple intersection.

**Permutation example: blocks 60, 04, and 42.** The source lists the ten distinct digits \(0,1,\ldots,9\) and asks for permutations containing at least one of the adjacent digit blocks \(60,04,42\). It illustrates a permutation such as \((1,7,2,6,9,5,4,3,8,0)\), then another with the block \(60\) circled.

Let \(P_{42},P_{60},P_{04}\) be the sets of digit permutations containing the indicated block. The target is
\[
|P_{42}\cup P_{60}\cup P_{04}|.
\]
Treating a required adjacent block as one object gives
\[
|P_{42}|=|P_{60}|=|P_{04}|=9!.
\]
The pairwise intersection counts written on the page are
\[
|P_{42}\cap P_{60}|=8!,\qquad
|P_{60}\cap P_{04}|=8!,\qquad
|P_{42}\cap P_{04}|=8!.
\]
The first example lists the eight objects
\[
(42,60,1,3,5,7,8,9).
\]
The second uses the merged block \(604\), listing
\[
(604,1,2,3,5,7,8,9).
\]
The triple intersection count is
\[
|P_{42}\cap P_{04}\cap P_{60}|=7!.
\]

**Textbook clarification:** the \(04\) and \(42\) requirements merge into \(042\), and all three requirements merge into \(6042\). These mergers explain the remaining \(8!\) and \(7!\) counts. Inclusion–exclusion therefore gives
\[
3\cdot9!-3\cdot8!+7!=972{,}720.
\]
The final total is not evaluated in the source.

**Integers divisible by 7 or 11.** Let \(A_7,A_{11}\) be the positive integers at most 1000 divisible by 7 and 11 respectively. Then
\[
\begin{aligned}
|A_7\cup A_{11}|
&=|A_7|+|A_{11}|-|A_7\cap A_{11}|\\
&=\left\lfloor\frac{1000}{7}\right\rfloor
+\left\lfloor\frac{1000}{11}\right\rfloor
-\left\lfloor\frac{1000}{7\cdot11}\right\rfloor\\
&=142+90-12=220.
\end{aligned}
\]

**General inclusion–exclusion theorem.** For finite sets \(S_1,\ldots,S_n\),
\[
\begin{aligned}
\left|\bigcup_{i=1}^nS_i\right|
={}&\sum_{i=1}^n|S_i|
-\sum_{1\le i<j\le n}|S_i\cap S_j|\\
&+\sum_{1\le i<j<k\le n}|S_i\cap S_j\cap S_k|
-\cdots\\
&+(-1)^{n-1}\left|\bigcap_{i=1}^nS_i\right|.
\end{aligned}
\]

**Proof by counting one element.** Suppose a particular element \(s\) belongs to \(r\ge1\) of the sets. The sum of single-set sizes counts it \(\binom r1\) times; the pairwise-intersection sum counts it \(\binom r2\) times; and so on. Its net count is
\[
\binom r1-\binom r2+\cdots+(-1)^{r+1}\binom rr=1,
\]
because
\[
\sum_{j=0}^r(-1)^j\binom rj=0,
\qquad \binom r0=1.
\]
An element outside every set is counted zero times. The source uses \(n\) locally for the number of sets containing \(s\); \(r\) here keeps that count distinct from the total number of sets.

**Other form: index sets.** With \(I\) a nonempty subset of \(\{1,\ldots,n\}\), the page rewrites the formula as
\[
\left|\bigcup_{j=1}^nS_j\right|
=\sum_{i=1}^n(-1)^{i+1}
\sum_{\substack{I\subseteq\{1,\ldots,n\}\\|I|=i}}
\left|\bigcap_{j\in I}S_j\right|.
\]
The heading calls this an “indicator set” form; the circled inner sum is over index subsets \(I\) of the stated size.

**Combinatorial proofs.** The circled symmetry identity is
\[
\binom nk=\binom n{n-k}.
\]
The next identity is
\[
\sum_{k=0}^n\binom nk\binom{2n}{n-k}=\binom{3n}{n}.
\]
The labels underneath give \(n\) apples and \(2n\) oranges. **Textbook clarification:** choosing \(n\) objects from the combined \(3n\) objects can be counted by fixing \(k\) apples and \(n-k\) oranges, then summing over \(k\).

**Pascal's identity.** The page writes
\[
\binom nk=\binom{n-1}{k-1}+\binom{n-1}k.
\]
On the left are the coefficient labels \(\binom00\), then \(\binom10,\binom11\), then \(\binom20,\binom21,\binom22\). On the right, branching lines show the first rows of Pascal's triangle:
\[
\begin{array}{ccccccc}
&&&1&&&\\
&&1&&1&&\\
&1&&2&&1&\\
1&&3&&3&&1.
\end{array}
\]
Each interior entry receives contributions from the two entries above it.

**Textbook cross-references:** §14.9, “Inclusion–Exclusion,” printed pp. 581–586 (PDF pp. 589–594), for the counting principle and element-count proof; §14.10, “Combinatorial Proofs,” printed pp. 587–591 (PDF pp. 595–599), for binomial identities and their combinatorial interpretation. The examples above follow the handwritten page; §14.9.3 also uses the digit blocks \(42,04,60\).

<a id="pdf-page-203"></a>

## PDF page 203 — Geometric sums and integral bounds

**Sums to consider.** The page opens with
\[
\sum_{k=1}^n\sqrt{k},
\qquad
\sum_{0\le k\le n}\lfloor\sqrt{k}\rfloor,
\]
with the second expression circled. The brackets around the square root indicate an integer-part operation, subsequently discussed under floor and ceiling on PDF page 205.

**Geometric sum.** Put
\[
S=1+x+x^2+\cdots+x^n.
\]
Then
\[
xS=x+x^2+x^3+\cdots+x^{n+1},
\]
and subtracting yields
\[
S=\frac{1-x^{n+1}}{1-x}.
\]
An arrow points to the infinite-series limit \(1/(1-x)\).

**Textbook clarification:** the finite formula assumes \(x\ne1\); at \(x=1\), \(S=n+1\). The infinite series converges to \(1/(1-x)\) for \(|x|<1\), a restriction absent from the handwritten arrow.

**Differentiating the sum.** The target is
\[
\sum_{i=1}^n i x^i=x+2x^2+3x^3+\cdots+nx^n.
\]
Differentiate the finite geometric sum and multiply by \(x\):
\[
\sum_{i=1}^n i x^i
=x\frac{d}{dx}\left(\sum_{i=0}^nx^i\right)
=x\frac{d}{dx}\left(\frac{1-x^{n+1}}{1-x}\right)
=\frac{x-(n+1)x^{n+1}+nx^{n+2}}{(1-x)^2}.
\]
**Textbook clarification:** the middle handwritten equality omits the factor \(x\) before the derivative of the fraction. The factor is required and is included explicitly above; the source's final numerator agrees with this corrected differentiation.

**Sum of the first \(n\) integers.** Write
\[
S=1+2+\cdots+n,
\qquad S=n+(n-1)+\cdots+1.
\]
Adding the two lines gives \(2S=n(n+1)\), hence
\[
S=\frac{n(n+1)}2.
\]

**Sum of squares.** The page guesses a cubic form
\[
\sum_{i=1}^ni^2=an^3+bn^2+cn+d.
\]
It lists the substitutions \(n=0,1,2,3\), including \(n=0\Rightarrow d=0\), and records
\[
a=\frac13,\qquad b=\frac12,\qquad c=\frac16,\qquad d=0.
\]
**Textbook clarification:** the four substitutions correspond to sums \(0,1,5,14\) and determine these coefficients. Guessing and fitting the polynomial discovers the formula; a separate proof, for example induction, establishes it for every \(n\). See §13.2, printed pp. 510–512 (PDF pp. 518–520).

**Square-root sum.** The source circles
\[
S=\sum_{i=1}^n\sqrt{i}
\]
and writes its order as \(O(n^{3/2})\).

**Monotone functions.** For \(f:\mathbb R^+\to\mathbb R^+\), and \(x>y\):

- Strictly increasing: \(f(x)>f(y)\). Red examples are \(2^x,\log x,\sqrt{x}\).
- Weakly increasing: \(f(x)\ge f(y)\). Red examples are \(\max(x,2)\) and a bracketed integer-rounding function of \(x\).
- Strictly decreasing: \(f(x)<f(y)\). Red examples are \(1/x,2^{-x}\).
- Weakly decreasing: \(f(x)\le f(y)\). The red example is a bracketed integer-rounding function of \(1/x\).

The floor/ceiling orientation of the two red bracketed examples is **[unclear in source]**. Either corresponding rounding operation preserves the indicated weak monotonicity. Also, the example \(\log x\) is increasing on \(x>0\), but takes negative values on \(0<x<1\); the stated positive codomain needs adjustment or a restricted domain for that example.

**Integral bound lemma.** Let
\[
S=\sum_{i=1}^nf(i),
\qquad I=\int_1^nf(x)\,dx.
\]
For a weakly increasing function, the green circled inequality is
\[
\boxed{I+f(1)\le S\le I+f(n).}
\]
Red inequality marks and the label “weakly decreasing” indicate that for a weakly decreasing function the endpoint terms reverse:
\[
I+f(n)\le S\le I+f(1).
\]
The diagram shows an increasing curve across integer positions \(1,2,3,\ldots,n\), rectangles below and above it, the first rectangle labelled \(f(1)\), red strips between rectangles and the curve, and the final rectangle enclosed in green. These areas explain why adding either endpoint term bounds the sum by the integral.

**Applying the lemma to \(\sqrt{x}\).**
\[
I=\int_1^n\sqrt{x}\,dx
=\frac23(n^{3/2}-1).
\]
Therefore
\[
\frac23(n^{3/2}-1)+1
\le S\le
\frac23(n^{3/2}-1)+\sqrt n,
\]
or, after simplifying,
\[
\boxed{\frac23n^{3/2}+\frac13
\le\sum_{i=1}^n\sqrt i
\le\frac23n^{3/2}+\sqrt n-\frac23.}
\]

**Harmonic numbers.** The \(n\)-th harmonic number is
\[
H_n=\sum_{k=1}^n\frac1k.
\]
The written bounds are
\[
\frac1n+\log n\le H_n\le\log n+1.
\]
Here the logarithm is the natural logarithm, arising from integrating \(1/x\).

**Textbook cross-references:** §13.1.2–13.1.6, printed pp. 505–510 (PDF pp. 513–518), for geometric sums and differentiation; §13.2, printed pp. 510–512 (PDF pp. 518–520), for sums of powers; Definition 13.3.1 and Theorem 13.3.2, §13.3, printed pp. 512–515 (PDF pp. 520–523), for monotonicity and integral bounds; §13.4, printed pp. 516–521 (PDF pp. 524–529), for harmonic numbers.

<a id="pdf-page-204"></a>

## PDF page 204 — Products, Stirling's formula, and double sums

**Turning products into sums.** For a positive-valued function \(f\), set
\[
P=\prod_{i=1}^nf(i).
\]
Then
\[
\log P=\sum_{i=1}^n\log f(i).
\]
The logarithm here is natural, as shown by the later exponentiation using \(e\).

**Factorial bounds.** Apply the product-to-sum idea to \(n!\):
\[
\log(n!)=\sum_{i=1}^n\log i.
\]
The comparison integral is \(\int_1^n\log x\,dx\). Using the integral bounds from the previous page,
\[
n\log n-n+1
\le\log(n!)
\le(n+1)\log n-n+1.
\]
Exponentiating gives the circled lower bound and indicated upper bound
\[
\boxed{\frac{n^n}{e^{n-1}}\le n!\le\frac{n^{n+1}}{e^{n-1}}.}
\]

**Stirling's approximation.** The source writes
\[
n!\sim\sqrt{2\pi n}\left(\frac ne\right)^n e^{\varepsilon(n)},
\qquad
\frac1{12n+1}\le\varepsilon(n)\le\frac1{12n}.
\]
**Textbook clarification:** with this bounded correction term, Theorem 13.5.1 states an **equality**
\[
n!=\sqrt{2\pi n}\left(\frac ne\right)^n e^{\varepsilon(n)}.
\]
As \(n\to\infty\), \(\varepsilon(n)\to0\), so the familiar approximation is \(n!\sim\sqrt{2\pi n}(n/e)^n\).

**Double sums and closed forms.** An initial sketch has two summation signs followed by an empty circled expression and the words “closed form”; no summand is specified there. The next displayed identity is
\[
\sum_{n=0}^{\infty}y^n\left(\sum_{i=0}^nx^i\right)
=\frac1{(1-y)(1-xy)}.
\]
**Textbook clarification:** as a numerical infinite sum, it is justified when \(|y|<1\) and \(|xy|<1\). Reordering gives
\[
\sum_{i=0}^{\infty}x^i\sum_{n=i}^{\infty}y^n
=\frac1{1-y}\sum_{i=0}^{\infty}(xy)^i
=\frac1{(1-y)(1-xy)}.
\]
These convergence conditions and intermediate steps are not supplied in the handwriting.

**Sum of harmonic numbers.** The page first writes the approximation
\[
\sum_{k=1}^nH_k\sim n\log n-n+1.
\]
It then obtains a closed form by changing the order of a triangular double sum:
\[
\begin{aligned}
\sum_{k=1}^nH_k
&=\sum_{k=1}^n\sum_{j=1}^k\frac1j\\
&=\sum_{j=1}^n\sum_{k=j}^n\frac1j\\
&=\sum_{j=1}^n\frac1j\sum_{k=j}^n1\\
&=\sum_{j=1}^n\frac{n-j+1}{j}\\
&=(n+1)\sum_{j=1}^n\frac1j-\sum_{j=1}^n\frac jj\\
&=\boxed{(n+1)H_n-n}.
\end{aligned}
\]
The diagram beside the derivation shows rows and columns indexed \(1,2,3,4,\ldots\), a diagonal boundary, and circled columns through the triangular region. It illustrates the same index pairs \(1\le j\le k\le n\) counted first by rows and then by columns.

**Textbook cross-reference:** §13.5, “Products,” and Theorem 13.5.1, printed pp. 522–524 (PDF pp. 530–532), for product logarithms, factorial bounds, and Stirling's formula; §13.6, “Double Trouble,” printed pp. 525–527 (PDF pp. 533–535), for changing the summation order and summing harmonic numbers. The initial approximation gives the leading asymptotic order, while the final identity is exact.

<a id="pdf-page-205"></a>

## PDF page 205 — Floor, ceiling, and integer comparisons

The page introduces floor \(\lfloor x\rfloor\), ceiling \(\lceil x\rceil\), and the notation \(x\bmod y\). It labels floor and ceiling explicitly but supplies no modulo definition on this page.

**Basic bounds.** For real \(x\),
\[
\lfloor x\rfloor\le x\le\lceil x\rceil,
\qquad
x-1<\lfloor x\rfloor,
\qquad
\lceil x\rceil<x+1.
\]
Combined,
\[
\boxed{x-1<\lfloor x\rfloor\le x\le\lceil x\rceil<x+1.}
\]

**Negation.**
\[
\lfloor-x\rfloor=-\lceil x\rceil,
\qquad
\lceil-x\rceil=-\lfloor x\rfloor.
\]

**Equivalent characterizations.** For \(n\in\mathbb Z\):
\[
\begin{array}{ll}
\text{(a)}&\lfloor x\rfloor=n\quad\Longleftrightarrow\quad n\le x<n+1;\\[2pt]
\text{(b)}&\lfloor x\rfloor=n\quad\Longleftrightarrow\quad x-1<n\le x;\\[2pt]
\text{(c)}&\lceil x\rceil=n\quad\Longleftrightarrow\quad n-1<x\le n;\\[2pt]
\text{(d)}&\lceil x\rceil=n\quad\Longleftrightarrow\quad x\le n<x+1.
\end{array}
\]

**Integer translation.** For \(x\in\mathbb R\) and \(n\in\mathbb Z\),
\[
\lfloor x+n\rfloor=\lfloor x\rfloor+n.
\]

**Comparisons with an integer.** Again for \(n\in\mathbb Z\),
\[
\begin{array}{ll}
\text{(e)}&x<n\quad\Longleftrightarrow\quad\lfloor x\rfloor<n;\\[2pt]
\text{(f)}&n<x\quad\Longleftrightarrow\quad n<\lceil x\rceil;\\[2pt]
\text{(g)}&x\le n\quad\Longleftrightarrow\quad\lceil x\rceil\le n;\\[2pt]
\text{(h)}&n\le x\quad\Longleftrightarrow\quad n\le\lfloor x\rfloor.
\end{array}
\]

**Diagram.** Coordinate axes and the line \(f(x)=x\) are drawn beside a parallel line. At several successive heights, green and red horizontal segments extend on opposite sides of the diagonal. The segments illustrate that integer rounding places a number between its neighbouring integer bounds, each less than one unit away. No further equation is attached to the extra parallel line.

**Textbook cross-reference:** Corollary 2.4.3, §2.4, printed p. 32 (PDF p. 40), describes floor as rounding down to the nearest integer. The identities here are direct consequences of the interval characterizations (a) and (c); the textbook does not give this complete eight-item list as a separate theorem.
