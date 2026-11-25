# Readable handwritten notes — Part 1, PDF pages 001–075

The transcription follows the source page order. It retains examples, proof steps and questions, including incomplete work. Additions explicitly headed **Textbook clarification** come from the supplied Lehman–Leighton–Meyer textbook; they are distinguished from the handwritten text.

<a id="pdf-page-001"></a>

## PDF page 001 — Sets and membership

A **set** is an unordered collection of objects. Membership is written $a\in A$; nonmembership is written $a\notin A$.

Examples:

- $A=$ the students in CS208.
- $A=\{a,b,c,d\}$.
- Standard number sets include $\mathbb N,\mathbb Q,\mathbb R,\mathbb C$.

For sets $A,B$, the page records both membership implications

$$a\in A\implies a\in B,\qquad b\in B\implies b\in A.$$

Together these describe sets having the same elements. The empty set is written $\varnothing$ or $\{\}$.

**Textbook cross-reference:** §4.1, Sets.

<a id="pdf-page-002"></a>

## PDF page 002 — Subsets, proper subsets and the universal set

The diagram shows a rectangle labelled $U$ containing three sets, two overlapping and one separate. $U$ is the surrounding universal set.

$A\subseteq B$ means that every member of $A$ is a member of $B$:

$$a\in A\implies a\in B.$$

The source also writes $A=B$ beneath this line, without a connecting statement. Equality would require the reverse inclusion as well; see the paired implications on page 001.

$A\subset B$ means that $A$ is a **proper subset** of $B$:

$$a\in A\implies a\in B,\qquad \exists b\in B\text{ such that }b\notin A.$$

The page records

$$\varnothing\subseteq A\subseteq U,\qquad A\subseteq A.$$

**Textbook cross-reference:** §4.1, Sets.

<a id="pdf-page-003"></a>

## PDF page 003 — Complement of a set

For a set $A$ inside a universal set $U$, its complement is

$$\overline A=\{a\in U\mid a\notin A\}.$$

Example: take $U=\mathbb N$ and let $A$ be the even natural numbers. The source leaves the line “$\overline A=$” blank as an exercise.

**Textbook clarification:** The complement in this example is the odd natural numbers, because complementation is taken relative to $U$. See §4.1, printed pp. 81–85.

<a id="pdf-page-004"></a>

## PDF page 004 — Ordered tuples and Cartesian products

An **ordered $n$-tuple** has the form $(m_1,m_2,\ldots,m_n)$. Two ordered tuples are equal precisely when corresponding entries agree:

$$
(m_1,\ldots,m_n)=(k_1,\ldots,k_n)
\quad\text{if }m_i=k_i\text{ for }i=1,\ldots,n.
$$

The **Cartesian product** of sets is

$$A\times B=\{(a,b)\mid a\in A,\ b\in B\}.$$

More generally,

$$
A_1\times\cdots\times A_n
=\{(a_1,\ldots,a_n)\mid a_i\in A_i\text{ for }i=1,\ldots,n\}.
$$

The symbols $m_1,\ldots,m_n$ appear beneath the factors at the bottom, but no further formula is written there.

**Textbook cross-reference:** §4.1 and §4.2, Sets and Sequences.

<a id="pdf-page-005"></a>

## PDF page 005 — Cartesian products as spaces and records

The first sketch is a two-ended line labelled $\mathbb R$, representing the real line. A parallelogram represents the plane, with the accompanying notation

$$\mathbb R\times\mathbb R=\mathbb R^2.$$

A second sketch is a table with columns **Name**, **Roll number**, and **Address**. It illustrates records containing several ordered fields. The rows are indicated only by dots; no particular records are specified.

**Textbook cross-reference:** §4.1–§4.2, Sets and Sequences.

<a id="pdf-page-006"></a>

## PDF page 006 — Functions, domain, codomain and image

For nonempty sets $A,B$, a **function** $f:A\to B$ assigns a unique element of $B$ to every element of $A$.

$A$ is the **domain** and $B$ is the **codomain**. The **range** consists of the values actually reached by the function.

The arrow sketch shows three domain elements: two map to one codomain element and the third maps to another. An additional codomain element lies outside the circled range. Thus a function may assign the same output to distinct inputs, and its range may be smaller than its codomain.

The page gives the example $f:\mathbb N\to\mathbb N$, with a square-function formula written as $f(a)=x^2$; the input-letter mismatch is retained here rather than silently treated as a new formula.

When $f(a)=b$, the page labels $a$ a **preimage** and $b$ an **image**.

**Textbook cross-reference:** §4.3, Functions.

<a id="pdf-page-007"></a>

## PDF page 007 — Injective functions

A function $f:A\to B$ is **injective**, or **one-to-one**, if no two distinct elements of $A$ map to the same element of $B$. Equivalently,

$$f(a)=f(b)\implies a=b.$$

Examples on the page:

- $f:\mathbb R\to\mathbb R$, $f(x)=x^2$: marked **not injective**.
- $f:\mathbb N\to\mathbb N$, $f(x)=x+1$: marked **injective**.
- $f:\mathbb R\to\mathbb R$, $f(x)=\sin x$: marked **not injective**.

The source notes $\mathbb N=\{0,1,\ldots\}$. Its final line writes $f:\mathbb R\to[-1,1]$ without repeating a formula or giving a conclusion.

**Textbook cross-reference:** §4.4.1, Definition 4.4.2, printed p. 91 (PDF p. 99), for injectivity; §4.5 and §7.1 for cardinality comparisons.

<a id="pdf-page-008"></a>

## PDF page 008 — Bijective functions

A function $f:A\to B$ is **bijective** if it is both injective and surjective.

Examples:

- $f:\mathbb R\to\mathbb R$, $f(x)=x$.
- $f:\mathbb R\to\mathbb R$, $f(x)=x^3$.
- $f:[-\pi/2,\pi/2]\to[-1,1]$, $f(x)=\sin x$.

The restricted sine function uses a different domain from the sine example on page 007.

**Textbook cross-reference:** §4.4.1, Definition 4.4.2, printed p. 91 (PDF p. 99), for function properties; §4.5 and §7.1 for cardinality comparisons.

<a id="pdf-page-009"></a>

## PDF page 009 — Inverse functions and necessary/sufficient conditions

If $f:A\to B$ is bijective, an inverse function $f^{-1}:B\to A$ is defined by

$$f^{-1}(b)=a\quad\text{such that }f(a)=b.$$

The source adds “$f^{-1}$ exists” without a further proof.

At the bottom it introduces the phrases “$P$ necessary [for] $Q$” and “$P$ sufficient [for] $Q$”. No implication formulas or examples are supplied on this page.

**Textbook cross-reference:** §4.4, Binary Relations, for inverse relations; §1.5 and §3.1.2 for implications.

<a id="pdf-page-010"></a>

## PDF page 010 — Surjective functions

A function $f:A\to B$ is **surjective**, or **onto**, if every element $b\in B$ has a preimage in $A$:

$$\forall b\in B\ \exists a\in A\text{ such that }f(a)=b.$$

**Textbook cross-reference:** §4.4.1, Definition 4.4.2, printed p. 91 (PDF p. 99), for function properties; §4.5 and §7.1 for cardinality comparisons.

<a id="pdf-page-011"></a>

## PDF page 011 — Comparing cardinalities using functions

Sets $A,B$ have the same **cardinality** if there exists a bijection between them. This is written $|A|=|B|$.

Example: $\{1,2,3\}$ and $\{a,b,c\}$ have the same cardinality.

The page records the comparisons:

$$
\begin{aligned}
\text{An injection }A\to B&\implies |A|\le|B|,\\
\text{A surjection }A\to B&\implies |A|\ge|B|.
\end{aligned}
$$

**Textbook cross-reference:** §4.5, printed p. 93 onward; §7.1, printed p. 206 onward.

<a id="pdf-page-012"></a>

## PDF page 012 — Equal cardinality of intervals

The page states

$$|[0,1]|=|[0,10]|.$$

It labels the intervals $A=[0,1]$ and $B=[0,10]$ and gives the bijection

$$f:A\to B,\qquad f(x)=10x.$$

The accompanying number-line sketch marks 0, an intermediate point labelled 2, and 10.

**Textbook cross-reference:** §7.1, Infinite Cardinality, printed p. 206 onward.

<a id="pdf-page-013"></a>

## PDF page 013 — Bijections between open intervals and the real line

The notes compare $(0,1)$ and $\mathbb R$. A chain of interval maps is indicated:

$$
(0,1)\longrightarrow(-\pi/2,\pi/2)
\xrightarrow{\tan}(-\infty,\infty).
$$

The tangent sketch is an increasing curve through the origin, with domain endpoints $-\pi/2$ and $\pi/2$ marked on the horizontal axis.

The page also writes $(0,1)\to(a,b)$ and $(a,b)\to(c,d)$. For the first of these it supplies

$$f(x)=(1-x)a+xb.$$

No formula for the second map is supplied.

**Textbook cross-reference:** §7.1, Infinite Cardinality, printed p. 206 onward.

<a id="pdf-page-014"></a>

## PDF page 014 — Naturals, even naturals and another interval example

Let $A=\mathbb N$ and let $B$ be the even natural numbers. The page gives

$$f:A\to B,\qquad f(x)=2x.$$

This pairs each natural number with an even natural number.

The lower part of the page introduces a second pair of sets, $A=\mathbb R$ and $B=[-1,1]$, alongside a two-directional line sketch. No mapping formula or conclusion is written for this second example.

**Textbook cross-reference:** §7.1, Infinite Cardinality, printed p. 206 onward.

<a id="pdf-page-015"></a>

## PDF page 015 — Countable sets and their subsets

A set $X$ is **countable** if it is either finite or has the same cardinality as $\mathbb N$.

If $X$ is countable, then any subset of $X$ is also countable.

The sketch lists $x_1,x_2,x_3,\ldots$ and identifies selected elements with $y_1,y_2,\ldots$ from a subset $Y\subseteq X$. The first selected element is $x_1$ and the second shown is $x_3$, illustrating that one can retain selected entries from a listing of $X$.

**Textbook cross-reference:** §7.1.2, Countable Sets, printed pp. 209–210 (PDF pp. 217–218).

<a id="pdf-page-016"></a>

## PDF page 016 — Listing a Cartesian product of countable sets

Let $X,Y$ be countable, with listings

$$X=\{x_1,x_2,x_3,\ldots\},\qquad Y=\{y_1,y_2,y_3,\ldots\}.$$

The page begins an array for $X\times Y$:

$$
\begin{array}{cccc}
(x_1,y_1)&(x_1,y_2)&(x_1,y_3)&\cdots\\
(x_2,y_1)&\cdots&&
\end{array}
$$

It writes $\mathbb N$ and the numbers 1, 2, 3 above the first row, beginning a discussion of how to list the pairs. The diagonal enumeration is drawn on the next page.

**Textbook cross-reference:** §7.1.2, Countable Sets, printed pp. 209–210 (PDF pp. 217–218).

<a id="pdf-page-017"></a>

## PDF page 017 — Diagonal enumeration of pairs

The diagram has horizontal coordinates $x_1,x_2,x_3,x_4,\ldots$ and vertical coordinates $y_1,y_2,y_3,y_4,\ldots$. Grid points represent pairs in $X\times Y$.

The visible numbering visits:

| Number | Pair |
| --- | --- |
| 1 | $(x_1,y_1)$ |
| 2 | $(x_2,y_1)$ |
| 3 | $(x_1,y_2)$ |
| 4 | $(x_3,y_1)$ |
| 5 | $(x_2,y_2)$ |
| 6 | $(x_1,y_3)$ |

The curves then continue across successive diagonals. Each diagonal has finitely many points, so the drawing illustrates a listing in which every grid point is eventually visited.

**Textbook cross-reference:** §7.1.2, Countable Sets, printed pp. 209–210 (PDF pp. 217–218).

<a id="pdf-page-018"></a>

## PDF page 018 — Countability of rational numbers

The page lists these countable sets and constructions:

- $\mathbb N$.
- If $A,B$ are countable, then $A\times B$ is countable.
- $\mathbb Q$ is countable.

It represents rationals using integer pairs $(p,q)$ with $p\in\mathbb Z$, $q\in\mathbb Z$, $q\ne0$, and writes

$$
(p_1,q_1)\equiv(p_2,q_2)
\quad\text{if }p_1q_2=p_2q_1.
$$

The last line is $\mathbb Q\subseteq\mathbb Z\times\mathbb Z$.

**Textbook clarification:** Rational numbers are represented by fractions $p/q$; different pairs may represent the same rational, as the cross-multiplication condition indicates. Thus the final containment is shorthand for a representation, not a literal identification of every rational with every representing pair. Countability follows by listing integer pairs and removing duplicate fractions. See §7.1.2, Corollary 7.1.10, printed p. 210 (PDF p. 218).

<a id="pdf-page-019"></a>

## PDF page 019 — Finite products of countable sets

The notes first recall $\mathbb Z\times\mathbb Z$.

For $A\times B\times C$, let $P=A\times B$. If $A,B$ are countable, $P$ is countable. Then $P\times C$ is countable when $C$ is countable. The page identifies this with $A\times B\times C$.

Repeating the argument gives the statement:

> The Cartesian product of finitely many countable sets is countable.

The source illustrates a finite list of factors as $A\times B\times C\times D\times E\times\cdots\times N$; the last $N$ is a factor label.

**Textbook cross-reference:** §7.1.2, Countable Sets, printed pp. 209–210 (PDF pp. 217–218).

<a id="pdf-page-020"></a>

## PDF page 020 — Finite unions of countable sets

**Claim:** Any finite union of countable sets is countable.

Let the countable sets be $A,B,C,\ldots,M$, and write

$$S=A\cup B\cup C\cup\cdots\cup M.$$

The proof setup lists their elements in rows:

$$
\begin{aligned}
A&=\{a_1,a_2,a_3,\ldots\},\\
B&=\{b_1,b_2,b_3,\ldots\},\\
C&=\{c_1,c_2,c_3,\ldots\},\\
&\ \vdots\\
M&=\{m_1,m_2,m_3,\ldots\}.
\end{aligned}
$$

The enumeration continues on the next page.

**Textbook cross-reference:** §7.1.2, Countable Sets, printed pp. 209–210 (PDF pp. 217–218).

<a id="pdf-page-021"></a>

## PDF page 021 — Countable unions by a diagonal listing

The page now considers $A_1,A_2,A_3,\ldots$, with rows

$$
\begin{array}{cccc}
A_1:&a_{11}&a_{12}&a_{13}&\cdots\\
A_2:&a_{21}&a_{22}&a_{23}&\cdots\\
A_3:&a_{31}&a_{32}&a_{33}&\cdots\\
&\vdots&&&
\end{array}
$$

Diagonal strokes traverse this array. The drawing extends the finite-union discussion to a countable family: list entries diagonal by diagonal, omitting repetitions when an element appears in several sets.

**Textbook cross-reference:** §7.1.2, Countable Sets, printed pp. 209–210 (PDF pp. 217–218).

<a id="pdf-page-022"></a>

## PDF page 022 — Comparing a union and a product

The page writes $A\times B$, $A\cup B$, and the proposed inequality

$$|A\cup B|\le|A\times B|.$$

It then records

$$|A|\le|A\times B|$$

and illustrates the map

$$a_i\longmapsto(a_i,b_1).$$

Lists $a_1,a_2,\ldots$ and $b_1,b_2,\ldots$ appear next to this construction.

**Textbook clarification:** The displayed map assumes $B$ has an element $b_1$, and it gives an injection from $A$ into $A\times B$. The union/product inequality has no hypotheses written on this page and is not true for arbitrary sets: two disjoint singleton sets have union size 2 and product size 1. Cardinality comparisons should therefore be checked through an actual injection. See §4.5, printed pp. 93–96, and §7.1, printed pp. 206–210.

<a id="pdf-page-023"></a>

## PDF page 023 — Enumeration

An **enumeration** of a set is a complete, ordered listing of its elements.

The sketch labels the elements of a set $A$ by the natural numbers $1,2,3,4,\ldots$, producing a listing

$$a_1,a_2,a_3,\ldots.$$

The separate notes $\mathbb N$, $1,2,3,\ldots$, and $1\le2$ emphasize the ordering of the labels.

**Textbook cross-reference:** §7.1.2, Countable Sets, printed pp. 209–210 (PDF pp. 217–218).

<a id="pdf-page-024"></a>

## PDF page 024 — Finite sequences of natural numbers

**Claim:** The set of all finite-length sequences of natural numbers is countable.

The proof outline separates sequences into successive length classes, labelled “seq 1”, “seq 2”, “seq 3”, …, and invokes a **countable union of countable sets**. Each fixed-length class is a finite Cartesian product of copies of $\mathbb N$.

Illustrative sequences are written as

$$
(1,3,10,10^{10},9,\ldots),\qquad(2,4,8,15,\ldots).
$$

The trailing dots indicate unspecified further entries; no lengths are assigned to these two examples.

**Textbook cross-reference:** §4.2, Sequences, printed p. 86; §7.1.2, Countable Sets, printed pp. 209–210 (PDF pp. 217–218).

<a id="pdf-page-025"></a>

## PDF page 025 — A short collection-of-pairs example

This sparse page contains only the collection

$$\{(1,2),(2,1),(1,1),\ldots\}.$$

No additional definition, question, or conclusion is written. In particular, the order within a pair distinguishes $(1,2)$ from $(2,1)$.

**Textbook cross-reference:** §4.1–§4.2, Sets and Sequences, printed pp. 81–86.

<a id="pdf-page-026"></a>

## PDF page 026 — Finite subsets of the natural numbers

**Claim:** The set of all finite subsets of $\mathbb N$ is countable.

No proof is written on this page.

**Textbook cross-reference:** §4.1.3, Power Set, printed p. 83 (PDF p. 91); §7.1.2, Countable Sets, printed pp. 209–210 (PDF pp. 217–218).

<a id="pdf-page-027"></a>

## PDF page 027 — First diagonal argument for the power set

The page considers $\mathcal P(\mathbb N)$ and says to suppose it is countable. Its proposed listing pairs subsets and natural-number labels:

$$S_1\leftrightarrow1,\qquad S_2\leftrightarrow2,\qquad S_3\leftrightarrow3,\ldots.$$

For a natural-number label $n$ paired with a subset $S$, call $n$ **labelled** if $n\in S$ and **unlabelled** otherwise.

Let $B$ be the set of unlabelled numbers. Since the assumed listing contains every subset of $\mathbb N$, $B$ must itself have a label $b\in\mathbb N$.

The page marks both alternatives as contradictory:

1. $b$ is labelled.
2. $b$ is unlabelled.

The argument is repeated more explicitly on page 028.

**Textbook cross-reference:** §7.1.3, Power Sets Are Strictly Bigger, Theorem 7.1.11 and Corollary 7.1.12, printed p. 211 (PDF p. 219).

<a id="pdf-page-028"></a>

## PDF page 028 — The power set is uncountable

**Claim:** $\mathcal P(\mathbb N)$ is uncountable.

Assume, for contradiction, that $\mathcal P(\mathbb N)$ is countable and has a listing $S_1,S_2,S_3,\ldots$ paired with $1,2,3,\ldots$.

For the subset $S_i$ paired with the natural number $n=i$:

- If $n\in S_i$, call $n$ **labelled**.
- Otherwise, call $n$ **unlabelled**.

Let $B$ be the set of unlabelled numbers. In the assumed listing, $B=S_b$ for some label $b$.

Both cases lead to contradiction:

- If $b$ is labelled, then $b\in S_b=B$, even though $B$ consists of unlabelled numbers.
- If $b$ is unlabelled, then $b\notin S_b=B$, but by the definition of $B$, an unlabelled $b$ belongs to $B$.

Therefore the assumed complete listing cannot exist.

**Textbook cross-reference:** §7.1.3, Power Sets Are Strictly Bigger, Theorem 7.1.11 and Corollary 7.1.12, printed p. 211 (PDF p. 219).

<a id="pdf-page-029"></a>

## PDF page 029 — Infinite binary sequences are uncountable

Let $T$ be the set of infinite sequences of 0s and 1s. The claim is that $T$ is uncountable.

Assume $T$ is countable and list its sequences as rows. The visible beginning of the array is:

$$
\begin{array}{c|cccccccc}
s_1&0&1&0&0&0&1&1&1&\cdots\\
s_2&1&0&1&1&0&1&0&1&\cdots\\
s_3&0&0&1&1&0&0&1&1&\cdots\\
\vdots&&&&&&&&&\\
s_i&\cdots&&&&&1&&&\cdots
\end{array}
$$

The last schematic row emphasizes its diagonal digit rather than fixing a column number in the displayed finite portion.

Construct a sequence $b$ by flipping the diagonal entries. Its illustrated beginning is $1,1,0,\ldots$, and when the $i$-th diagonal entry is 1, the corresponding entry of $b$ is 0. Thus $b$ differs from row $s_i$ in position $i$, for every $i$. It cannot appear in the supposedly complete listing.

**Textbook cross-reference:** §7.1.3, Corollary 7.1.13, printed p. 211 (PDF p. 219); §7.1.4, Diagonal Argument, printed pp. 214–215 (PDF pp. 222–223).

<a id="pdf-page-030"></a>

## PDF page 030 — From infinite digit sequences to real numbers

**Claim:** The set of real numbers $\mathbb R$ is uncountable.

The page proposes an injection $T\to\mathbb R$, where $T$ is the uncountable set of infinite 0–1 sequences from page 029. It illustrates a sequence

$$t=010001011\cdots$$

and maps it to a real with those digits after the point:

$$f(t)=0.t=0.010001011\cdots.$$

The notes also recall a map $(0,1)\to\mathbb R$ and compare $(0,1)$ with $[0,1]$.

**Textbook clarification:** For the displayed 0–1 digit construction, interpreting $0.t$ as a decimal expansion gives an injection: the permitted digits exclude the repeating-9 ambiguity. A binary interpretation needs care because some binary expansions are not unique. The source does not specify the base on this page. See §7.1.3, Corollary 7.1.15 and its decimal-expansion proof, printed pp. 212–213 (PDF pp. 220–221).

<a id="pdf-page-031"></a>

## PDF page 031 — Binary relations

For sets $A,B$, a **binary relation from $A$ to $B$** is a subset of $A\times B$. Its members are ordered pairs $(a,b)$ with $a\in A$ and $b\in B$.

Example: take $A=B=\mathbb N$ and include $(a,b)$ precisely when $a<b$.

The relation can be written $aRb$; the page also shows $a\sim b$ as alternative relation notation.

**Textbook cross-reference:** §4.4, Binary Relations, printed p. 89 onward.

<a id="pdf-page-032"></a>

## PDF page 032 — Relations on a set

For $A=\mathcal P(\mathbb N)$, consider the relation

$$aRb\quad\text{if }a\subseteq b.$$

A relation **on** $A$ relates members of $A$ to other members of $A$.

Another example is a relation on $\mathbb N$ defined by

$$aRb\quad\text{if }a\mid b.$$

**Textbook cross-reference:** §4.4, printed p. 89; §9.6, Partial Orders, printed p. 335 onward.

<a id="pdf-page-033"></a>

## PDF page 033 — Reflexive relations

A relation $R$ on a set $S$ is **reflexive** if

$$\forall a\in S,\quad aRa.$$

The middle of the page shows an example pair written $(\mathbb R^{[\text{unclear in source}]},R)$; the superscript and the relation's rule are not clearly specified there.

A clear example at the bottom is a relation on $\mathbb C$:

$$aRb\quad\text{if }|a|=|b|.$$

**Textbook cross-reference:** §9.11, Summary of Relational Properties, printed p. 343.

<a id="pdf-page-034"></a>

## PDF page 034 — Symmetric relations

A relation $R$ on $S$ is **symmetric** if, for all $a,b\in S$,

$$aRb\implies bRa.$$

The page introduces $S=\{a,b,c,d\}$ and several small relation examples:

- $R=\{(a,b),(b,a)\}$.
- An additional pair $(b,c)$ is written beneath this first example.
- A second displayed relation is $R=\{(a,b),(b,c),(a,c)\}$.

No explicit verdicts are written beside these finite examples.

The right-hand example is a relation on $\mathbb R^2$ defined by orthogonality:

$$aRb\quad\text{if }\langle a,b\rangle=0.$$

**Textbook cross-reference:** §9.11, Summary of Relational Properties, printed p. 343.

<a id="pdf-page-035"></a>

## PDF page 035 — Antisymmetric relations

A relation $R$ on $S$ is **antisymmetric** if

$$aRb\text{ and }bRa\implies a=b.$$

Examples on $\mathbb R$, both marked with a check:

- $aRb$ if $a=b+1$.
- $aRb$ if $a<b$.

**Textbook cross-reference:** §9.6, Partial Orders, printed p. 335 onward; §9.11, printed p. 343.

<a id="pdf-page-036"></a>

## PDF page 036 — Tutorial 1: a bijection from a half-open to an open interval

**Tutorial 1, question 1.** Compare $[0,1)$, where $0\le x<1$, with $(0,1)$, where $0<x<1$.

The displayed function is

$$
f(x)=
\begin{cases}
1/2,&x=0,\\
1/2^{n+1},&x=1/2^n,\quad n=1,2,\ldots,\\
x,&\text{otherwise}.
\end{cases}
$$

A boxed chain starts with $0,1/2,1/4,1/8,\ldots$ and shifts the powers of two to the next entry. The first output in that small sketch looks like “1” with no denominator; **[unclear in source]**. The large formula clearly states $f(0)=1/2$.

For injectivity, the note says that no two elements have the same image.

For surjectivity, it begins with $y\in(0,1)$ and the case

$$y=1/2^{n+1}\quad\Longrightarrow\quad f(1/2^n)=y.$$

The special first image $1/2$ comes from $x=0$ in the displayed function. The remaining values are unchanged.

**Textbook cross-reference:** §7.1, Infinite Cardinality, printed pp. 206–210; §4.5, Finite Cardinality, printed p. 93 onward.

<a id="pdf-page-037"></a>

## PDF page 037 — Tutorial 1: the other half-open interval

**Question 2.** Let $A=(0,1]$ and $B=(0,1)$.

The page proposes

$$
f(x)=
\begin{cases}
1/2,&x=1,\\
1/2^{n+1},&x=1/2^n,\quad n=0,1,2,\ldots,\\
x,&\text{otherwise}.
\end{cases}
$$

The two stated cases agree at $x=1$ when $n=0$, so that overlap does not assign conflicting outputs.

An auxiliary two-column sketch writes the entries $0,1,2,3,4,5$ on the left and $0,2,3,4,5$ on the right. It connects equal entries except for the omitted left-hand 1; no further caption explains this separate sketch.

**Textbook cross-reference:** §7.1, Infinite Cardinality, printed pp. 206–210.

<a id="pdf-page-038"></a>

## PDF page 038 — Tutorial 1: a closed interval and two disjoint chains

**Question 3.** Construct a map $[0,1]\to(0,1)$.

The sketches use two chains:

$$
0\longmapsto1/3\longmapsto1/9\longmapsto\cdots,
\qquad
1\longmapsto1/2\longmapsto1/4\longmapsto\cdots.
$$

The displayed rules are

$$
f(x)=
\begin{cases}
1/2,&x=1,\\
1/3,&x=0,\\
1/2^{n+1},&x=1/2^n,\quad n=1,2,3,\ldots,\\
1/3^{n+1},&x=1/3^n,\quad n=1,2,3,\ldots.
\end{cases}
$$

The page labels these **disjoint chains**. It does not write an otherwise clause at the bottom of this formula.

**Textbook clarification:** To make the displayed construction a function on all of $[0,1]$, retain $f(x)=x$ at every point outside the two chains, as in the preceding tutorial constructions. The chain entries have no collisions, and every target value is either shifted from a predecessor or unchanged. This uses the bijection definition in §4.4.1, Definition 4.4.2, printed p. 91 (PDF p. 99), and the infinite-cardinality discussion in §7.1, printed pp. 206–210.

<a id="pdf-page-039"></a>

## PDF page 039 — Checking the closed-interval construction

For a target $y\in(0,1)$, the notes record the two chain cases:

$$
y=1/2^{n+1}\quad\Longrightarrow\quad f(1/2^n)=y,
$$

$$
y=1/3^{n+1}\quad\Longrightarrow\quad f(1/3^n)=y.
$$

The source concludes

$$|[0,1]|=|(0,1)|.$$

The endpoints of the shifted chains are handled by the special values $f(1)=1/2$ and $f(0)=1/3$ given on page 038.

**Textbook cross-reference:** §7.1, Infinite Cardinality, printed pp. 206–210.

<a id="pdf-page-040"></a>

## PDF page 040 — Tutorial 1: the real line and positive reals

**Question 4.** Compare $\mathbb R^+$ and $\mathbb R$. The page proposes

$$f:\mathbb R\to\mathbb R^+,\qquad f(x)=e^x.$$

It notes $e^x>0$ and $e^0=1$. An increasing-curve sketch accompanies the exponential example. A separate sketch labelled $f(x)=x^2$ shows a parabola crossed by a horizontal line, illustrating repeated outputs for the square function.

The injectivity calculation is

$$
f(a)=f(b)
\quad\Longrightarrow\quad
\ln(e^a)=\ln(e^b)
\quad\Longrightarrow\quad a=b.
$$

The example continues on the next page.

**Textbook cross-reference:** §7.1, Infinite Cardinality, printed pp. 206–210; §4.4.1, Definition 4.4.2, printed p. 91 (PDF p. 99), for the bijection criterion.

<a id="pdf-page-041"></a>

## PDF page 041 — Surjectivity of the exponential map

Continue the map $f:\mathbb R\to\mathbb R^+$, $f(x)=e^x$ from page 040. For any $y>0$, solve

$$y=e^x\quad\Longrightarrow\quad x=\log y.$$

Then

$$f(x)=e^x=e^{\log y}=y.$$

Thus every positive real number has a preimage. Together with the injectivity calculation on page 040, this gives a bijection. The right margin writes both directions $\mathbb R\to\mathbb R^+$ and $\mathbb R^+\to\mathbb R$, with the inverse indicated by $\log x$.

**Textbook cross-reference:** §4.4, Binary Relations (function properties), printed pp. 89–92 (PDF pp. 97–100); §7.1, Infinite Cardinality, printed pp. 206–210 (PDF pp. 214–218).

<a id="pdf-page-042"></a>

## PDF page 042 — Adding zero to the positive reals

**Tutorial question 5.** Compare $\mathbb R^+$ and $\mathbb R^+\cup\{0\}$. The displayed function has domain $\mathbb R^+$ and is

$$
f(x)=
\begin{cases}
0,&x=1,\\
\dfrac1{n-1},&x=\dfrac1n,\quad n=2,3,4,\ldots,\\
x,&\text{otherwise}.
\end{cases}
$$

For injectivity, the source describes the sequence

$$1,\frac12,\frac13,\frac14,\ldots$$

as getting mapped to

$$0,1,\frac12,\frac13,\ldots.$$

Each point outside that sequence maps to itself. A right-hand sketch compares the positive integers $1,2,3,4,5,6$ with a list having an extra circled zero at the top.

The left margin sketches the reverse-direction chain $0\mapsto1$, $1\mapsto1/2$, $1/2\mapsto1/3$, $1/3\mapsto1/4$. This is the inverse direction of the displayed function.

**Textbook cross-reference:** §7.1.1, Infinity Is Different, especially Lemma 7.1.7 on adding an element to an infinite set, printed pp. 208–209 (PDF pp. 216–217).

<a id="pdf-page-043"></a>

## PDF page 043 — Checking that the extra zero is reached

For $y\in\mathbb R^+\cup\{0\}$, the notes list the special targets:

$$y=0:\qquad f(1)=0,$$

$$y=1:\qquad f\!\left(\frac12\right)=1.$$

For a target $y=1/n$, the source writes

$$f\!\left(\frac1{n-1}\right)=\frac1n.$$

**Source correction / textbook clarification:** This last line reverses the chain on page 042. For the function actually displayed there, the correct preimage is

$$f\!\left(\frac1{n+1}\right)=\frac1n\qquad(n\ge1).$$

All remaining positive reals map to themselves. The boxed conclusion is

$$|\mathbb R^+|=|\mathbb R^+\cup\{0\}|.$$

An upper-right oval contains the isolated annotation “S24072 @ [unclear in source]”; it does not state a mathematical condition.

**Textbook cross-reference:** §7.1.1, Infinity Is Different, printed pp. 208–209 (PDF pp. 216–217); §4.4, printed pp. 89–92 (PDF pp. 97–100), for surjectivity.

<a id="pdf-page-044"></a>

## PDF page 044 — Mapping two intervals into one interval

**Tutorial question 6.** Compare

$$[0,1]\cup(2,3]\qquad\text{and}\qquad[0,1].$$

The interval diagram splits the target into the disjoint pieces

$$\left[0,\frac12\right]\quad\text{and}\quad\left(\frac12,1\right].$$

Map the first domain interval by

$$f(x)=\frac x2\qquad(x\in[0,1]).$$

The examples are $0\mapsto0$, $1\mapsto1/2$, $1/2\mapsto1/4$, and continuation of the halving chain.

Map the second domain interval by

$$f(x)=\frac{x-1}{2}\qquad(x\in(2,3]).$$

The endpoint calculation writes $2\mapsto1/2$ and $3\mapsto(3-1)/2=1$. Here $2$ is an excluded endpoint, so $1/2$ is excluded from the second image interval. The formula is repeated in the right margin.

**Textbook cross-reference:** §4.3, Functions, printed pp. 87–88 (PDF pp. 95–96); §4.4, printed pp. 89–92 (PDF pp. 97–100); §7.1, printed pp. 206–210 (PDF pp. 214–218).

<a id="pdf-page-045"></a>

## PDF page 045 — The piecewise interval bijection

The displayed map is

$$
f(x)=
\begin{cases}
\dfrac x2,&x\in[0,1],\\
\dfrac{x-1}{2},&x\in(2,3].
\end{cases}
$$

The source's top line writes $f:[0,1]\cup[2,3]\to[0,1]$, although the second case and preceding page use $(2,3]$. The intended domain is $[0,1]\cup(2,3]$; including $2$ in the second piece would give the same output $1/2$ as $x=1$.

The note calls these “2 disjoint functions” and marks injection with a check. Each formula is injective on its own interval, and their images $[0,1/2]$ and $(1/2,1]$ are disjoint.

For the first surjectivity case, let $0\le y\le1/2$. From

$$y=\frac x2$$

obtain $x=2y\in[0,1]$. The source does not write the second target case.

**Textbook clarification:** For $1/2<y\le1$, choose $x=2y+1\in(2,3]$; then $(x-1)/2=y$. Thus the piecewise map is also surjective, using the criterion in Definition 4.4.2, printed p. 91 (PDF p. 99).

**Textbook cross-reference:** §4.4, Binary Relations, printed pp. 89–92 (PDF pp. 97–100); §7.1, Infinite Cardinality, printed pp. 206–210 (PDF pp. 214–218).

<a id="pdf-page-046"></a>

## PDF page 046 — A tangent bijection from an open interval to the real line

**Tutorial question 7.** Compare $(0,1)$ and $\mathbb R=(-\infty,\infty)$. The construction passes through the intervals

$$(0,1)\ \longrightarrow\ (0,\pi)\ \longrightarrow\ \left(-\frac\pi2,\frac\pi2\right)\ \xrightarrow{\tan}\ \mathbb R.$$

The circled function is

$$f(x)=\tan\left(\pi x-\frac\pi2\right).$$

The top-right shorthand “$\tan x=(-\pi/2,\pi/2)$” indicates the chosen **domain interval** for tangent, rather than an equality between a function value and an interval.

At the left endpoint the notes write $0^+$, $\pi x-\pi/2=-\pi/2$, and $-\infty$; at the right endpoint they write $1^-$, $\pi x-\pi/2=\pi/2$, and $+\infty$.

**Clarification of the endpoint notation:** These statements describe limits:

$$\lim_{x\to0^+}f(x)=-\infty,\qquad \lim_{x\to1^-}f(x)=+\infty.$$

The endpoint values are not part of the domain. This calculus fact supports the bijection exercise; the textbook cross-reference supplies the definitions of bijection and equal cardinality rather than a tangent-function proof.

**Textbook cross-reference:** §4.4, Definition 4.4.2, printed p. 91 (PDF p. 99); §7.1, Infinite Cardinality, printed pp. 206–210 (PDF pp. 214–218).

<a id="pdf-page-047"></a>

## PDF page 047 — Checking the tangent map

An increasing tangent-shaped graph is crossed by horizontal lines, with a check beside it. The injectivity heading is represented by the underlined assumption $f(a)=f(b)$; no algebraic continuation is written.

For **surjectivity**, take $y\in\mathbb R$ and let

$$x=\frac1\pi\left(\tan^{-1}(y)+\frac\pi2\right).$$

Since

$$\tan^{-1}(y)\in\left(-\frac\pi2,\frac\pi2\right),$$

we have $x\in(0,1)$. The source circles the conclusion $f(x)=y$.

**Textbook clarification:** Injectivity follows because tangent is strictly increasing on $(-\pi/2,\pi/2)$ and $x\mapsto\pi x-\pi/2$ is strictly increasing. For the displayed preimage,

$$f(x)=\tan\bigl(\tan^{-1}(y)\bigr)=y.$$

These are the injectivity and surjectivity conditions from Definition 4.4.2, printed p. 91 (PDF p. 99).

**Textbook cross-reference:** §4.4, printed pp. 89–92 (PDF pp. 97–100); §7.1, printed pp. 206–210 (PDF pp. 214–218).

<a id="pdf-page-048"></a>

## PDF page 048 — Composing bijections to map a closed interval onto the real line

**Tutorial question 8.** Compare $[0,1]$ and $\mathbb R$. The page starts with the composition notation $f(g(x))$.

From question 3, the notes recall

$$|[0,1]|=|(0,1)|.$$

From question 7, they recall

$$|(0,1)|=|\mathbb R|.$$

Since the composition of two bijections is a bijection, the source concludes that $g\circ f$ is a bijection, where $f$ maps the closed interval to the open interval and $g$ maps the open interval to the real line. The starting $f(g(x))$ uses the opposite symbol order; the domains determine the intended composition.

**Textbook cross-reference:** §7.1, Lemma 7.1.3, printed pp. 206–207 (PDF pp. 214–215), for transitivity of equal cardinality; Problem 4.19(b), printed p. 105 (PDF p. 113), asks for the composition-of-bijections result.

<a id="pdf-page-049"></a>

## PDF page 049 — Transitive relations

A relation $R$ on a set $A$ is **transitive** if, for every $a,b,c\in A$,

$$aRb\text{ and }bRc\quad\Longrightarrow\quad aRc.$$

For $(\mathbb Z,<)$, the example is

$$a<b,\ b<c\quad\Longrightarrow\quad a<c.$$

The bottom of the page gives a three-element set (the third handwritten label is **[unclear in source]**, apparently $c$ in light of the following pairs) and

$$R=\{(a,b),(b,c)\}.$$

No verdict is explicitly written beside this finite example.

**Textbook clarification:** If $A=\{a,b,c\}$ with distinct labels, this $R$ is not transitive: $(a,b)$ and $(b,c)$ are present but $(a,c)$ is absent. Compare §9.11, printed p. 343 (PDF p. 351).

**Textbook cross-reference:** §9.6, Partial Orders, printed pp. 335–338 (PDF pp. 343–346); §9.11, Summary of Relational Properties, printed p. 343 (PDF p. 351).

<a id="pdf-page-050"></a>

## PDF page 050 — Equivalence relations and equality of function values

A relation $R$ on $A$ is an **equivalence relation** if $R$ is reflexive, symmetric, and transitive.

One example has $A$ equal to the set of all triangles in $\mathbb R^2$, with

$$a\sim b\quad\text{if triangle }a\text{ is similar to triangle }b.$$

Another construction begins with a function $f:X\to Y$. Define a relation on $X$ by

$$a\sim b\quad\text{if }f(a)=f(b),\qquad a,b\in X.$$

The page denotes the resulting pair by $(X,\sim)$.

**Textbook cross-reference:** §9.10, Equivalence Relations, printed pp. 341–342 (PDF pp. 349–350), particularly the relation defined by equality of the values of a function; §9.11, printed p. 343 (PDF p. 351).

<a id="pdf-page-051"></a>

## PDF page 051 — Examples to check for equivalence

The page lists four relations:

1. On $\mathbb Z$, define $aRb$ if $a=b$ or $a=-b$.
2. On $\mathbb R$, define $aRb$ if $a-b$ is an integer.
3. Fix an integer $m>0$. On $\mathbb Z$, define $a\sim b$ if $a-b$ is divisible by $m$.
4. Fix $\varepsilon\in\mathbb R$ with $\varepsilon>0$. On $\mathbb R$, define $a\sim b$ if $|a-b|\le\varepsilon$.

No individual verdict or proof is written on this page.

**Textbook clarification:** The first three relations are equivalence relations. The first is equality of the values of $f(a)=|a|$; the second is equality of the fractional parts of real numbers; the third is congruence modulo $m$. The fourth is reflexive and symmetric but fails transitivity: $0\sim\varepsilon$ and $\varepsilon\sim2\varepsilon$, while $0\not\sim2\varepsilon$. These checks use Definition 9.10.1 and the function-value construction in Definition 9.10.2, printed pp. 341–342 (PDF pp. 349–350).

**Textbook cross-reference:** §9.10, printed pp. 341–342 (PDF pp. 349–350); §8.6, Modular Arithmetic, printed pp. 263–264 (PDF pp. 271–272).

<a id="pdf-page-052"></a>

## PDF page 052 — Partial orders and posets

A relation $R$ on a set $A$ is a **partial order** if it is reflexive, antisymmetric, and transitive. The pair $(A,R)$ is called a **poset**.

The example is $(\mathbb Z,\le)$. Its antisymmetry condition is illustrated by

$$a\le b\text{ and }b\le a\quad\Longrightarrow\quad a=b.$$

**Textbook cross-reference:** §9.6.3, Weak Partial Orders, printed pp. 337–338 (PDF pp. 345–346), especially Definitions 9.6.12–9.6.13.

<a id="pdf-page-053"></a>

## PDF page 053 — Divisibility and inclusion as proposed orders

The first proposed example is $(\mathbb Z,\mid)$, with $a\mid b$. The source writes

$$a\mid b\text{ and }b\mid a\quad\Longrightarrow\quad a=b.$$

**Source correction / textbook clarification:** On all of $\mathbb Z$, this implication is false: $1\mid-1$ and $-1\mid1$, but $1\ne-1$. Divisibility is a partial order on the **positive integers**, where mutual divisibility does imply equality. This follows from divisibility in §8.1, printed pp. 243–247 (PDF pp. 251–255), together with antisymmetry in §9.6.3, printed p. 338 (PDF p. 346).

The second example starts with an arbitrary set $S$ and gives

$$\bigl(\mathcal P(S),\subseteq\bigr),$$

the power set ordered by set inclusion.

**Textbook cross-reference:** §8.1, Divisibility, printed pp. 243–247 (PDF pp. 251–255); §9.6.3, printed pp. 337–338 (PDF pp. 345–346); §9.7, Representing Partial Orders by Set Containment, printed p. 339 (PDF p. 347).

<a id="pdf-page-054"></a>

## PDF page 054 — Comparing infinite binary sequences

Let $T$ be the set of all infinite sequences of zeros and ones. For $a,b\in T$, the page writes the comparison alternatives

$$a\le b\qquad\text{or}\qquad b\le a.$$

The upper-right sketch begins with the sequences

$$010\ldots\qquad\text{and}\qquad111\ldots,$$

and points to the first entries. The lower-right sketch labels

$$a=0110\ldots,\qquad b=0101\ldots,$$

and points to the third entry of $b$, where $a$ has $1$ and $b$ has $0$. At the fourth entry the inequality goes in the opposite direction.

**Textbook clarification:** The order rule is not explicitly defined on this page. Interpreting the diagrams as the coordinatewise order,

$$a\le b\quad\Longleftrightarrow\quad a_i\le b_i\text{ for every coordinate }i,$$

the second pair is incomparable: neither $a\le b$ nor $b\le a$ holds. This is the product-order idea in §9.9, printed pp. 340–341 (PDF pp. 348–349). The written “or” can therefore be read as a comparability test, rather than a property established for every pair in $T$.

**Textbook cross-reference:** §9.8, Linear Orders, printed p. 340 (PDF p. 348); §9.9, Product Orders, printed pp. 340–341 (PDF pp. 348–349).

<a id="pdf-page-055"></a>

## PDF page 055 — Equivalence classes

Let $R$ be an equivalence relation on a set $A$. For $a\in A$, its **equivalence class** is

$$[a]=\{b\in A\mid aRb\}.$$

The example returns to triangles under similarity, denoted $(\Delta\text{'s},\sim)$. If $a$ is equilateral, the page asks

$$[a]=\ ?$$

**Textbook clarification:** In this example, $[a]$ consists of all equilateral triangles: every triangle similar to an equilateral triangle is equilateral, and all equilateral triangles are similar. This applies the definition of an equivalence class in §9.10.1, printed p. 342 (PDF p. 350).

At the bottom, a separate sketch labelled $a$ depicts a triangle with a right-angle marker and tiny angle labels **[unclear in source]**. This sketch does not depict an equilateral triangle; the source does not explain how it relates to the preceding example.

**Textbook cross-reference:** §9.10.1, Equivalence Classes, Definition 9.10.3, printed p. 342 (PDF p. 350).

<a id="pdf-page-056"></a>
## PDF page 056 — Congruence classes modulo five

Congruence modulo $m$ is a relation on $\mathbb Z$:

$$a\sim b\quad\text{if }m\mid(a-b).$$

For $m=5$, the page writes

$$[0]=\{\ldots,-10,-5,0,5,10,15,\ldots\},$$

$$[1]=\{\ldots,-9,-4,1,6,11,\ldots\}.$$

The labels $[5]$ and $[10]$ are placed above entries in the first class, indicating $[5]=[10]=[0]$. The page also lists $[2]$, $[3]$, $[4]$, and $[5]$, but does not fill in the first three of these sets. It records the general fact

$$a\in[a].$$

**Textbook clarification:** The other three distinct residue classes are

$$[2]=\{\ldots,-8,-3,2,7,12,\ldots\},$$
$$[3]=\{\ldots,-7,-2,3,8,13,\ldots\},$$
$$[4]=\{\ldots,-6,-1,4,9,14,\ldots\}.$$

There are exactly five classes, and $[5]$ repeats $[0]$. Compare the textbook's congruence-modulo-five partition in §9.10.1, printed pp. 342–343 (PDF pp. 350–351).

**Textbook cross-reference:** §8.6, Modular Arithmetic, printed pp. 263–264 (PDF pp. 271–272); §9.10.1, printed pp. 342–343 (PDF pp. 350–351).

<a id="pdf-page-057"></a>
## PDF page 057 — Three equivalent descriptions of belonging to one class

For an equivalence relation $R$ on $A$, the following statements are equivalent:

1. $aRb$.
2. $[a]=[b]$.
3. $[a]\cap[b]\ne\varnothing$.

The written proof establishes (3) $\Rightarrow$ (1). If the intersection is nonempty, there exists $c\in A$ such that

$$c\in[a]\quad\text{and}\quad c\in[b].$$

By the class definition,

$$aRc\quad\text{and}\quad bRc.$$

By symmetry, $cRb$; hence $aRc$ and $cRb$. Transitivity gives $aRb$.

**Textbook clarification:** For (1) $\Rightarrow$ (2), if $x\in[a]$, then $aRx$ and $bRa$ by symmetry of $aRb$, so $bRx$ by transitivity. Thus $[a]\subseteq[b]$; exchanging $a$ and $b$ gives the reverse inclusion. For (2) $\Rightarrow$ (3), reflexivity gives $a\in[a]=[b]$, so the common class is nonempty. These complete the correspondence underlying Theorem 9.10.4, printed p. 343 (PDF p. 351).

**Textbook cross-reference:** §9.10.1, Equivalence Classes, printed pp. 342–343 (PDF pp. 350–351); Theorem 9.10.4, printed p. 343 (PDF p. 351).

<a id="pdf-page-058"></a>
## PDF page 058 — A set decomposed into equivalence classes

A rectangular diagram of $A$ is divided into five regions labelled

$$[a],\ [b],\ [c],\ [d],\ [e].$$

Each region represents a different equivalence class, and the classes fill the set without overlap. Below it are the words “congruence modulo $m$” and the pairs

$$(\mathbb Z,=)\qquad\text{and}\qquad(\mathbb Z,\sim),$$

with $a\sim b$ written under the second pair. No further relation rule is supplied here beyond the preceding congruence example.

**Textbook clarification:** Equality gives the singleton classes $[a]=\{a\}$. Congruence modulo $m$ groups integers by their remainders, so its classes are larger. Both are partitions of $\mathbb Z$, by Theorem 9.10.4, printed p. 343 (PDF p. 351).

**Textbook cross-reference:** §9.10.1, printed pp. 342–343 (PDF pp. 350–351).

<a id="pdf-page-059"></a>
## PDF page 059 — Finer relations and partition refinement

Consider $(S,R_1)$ and $(S,R_2)$. The source defines $R_1$ to be **finer than** $R_2$ if

$$\forall a,b\in S,\qquad aR_1b\ \Longrightarrow\ aR_2b.$$

It also writes the generic logical form $p\Rightarrow q$.

The large diagram shows one set $S$ with several systems of boundaries, drawn in green, yellow, and dashed red. They illustrate partitions with different amounts of subdivision. A smaller diagram shows $S$ split into three regions containing points.

**Textbook clarification:** In the equivalence-relation setting, $R_1$ is finer than $R_2$ precisely when each $R_1$-class lies inside an $R_2$-class. As sets of ordered pairs, this is $R_1\subseteq R_2$. The textbook explains equivalence classes as partition blocks in §9.10.1, printed pp. 342–343 (PDF pp. 350–351); the particular terminology “finer” is supplied by the lecture notes.

**Textbook cross-reference:** §4.4, Binary Relations, printed p. 89 (PDF p. 97); §9.10.1, printed pp. 342–343 (PDF pp. 350–351).

<a id="pdf-page-060"></a>
## PDF page 060 — Partitions and the relation they induce

A **partition** of $S$ is a family of subsets $\{S_i\}$ satisfying

$$\bigcup_i S_i=S$$

and pairwise disjointness. The source writes $S_i\cap S_j=\varnothing$ followed by “$\forall i,j$”.

**Source correction / textbook clarification:** Disjointness applies when $i\ne j$; each block must also be nonempty. For $i=j$, $S_i\cap S_i=S_i$, so requiring that intersection to be empty would force every block to be empty. These are the partition conditions in Definition 9.5.6, printed p. 333 (PDF p. 341).

The page then lists $S_1,S_2,S_3,\ldots,S_n$ and starts a relation as a set of pairs,

$$R=\{(a,b),(a,a),(b,b),\ldots\}.$$

The bottom-right diagram divides $S$ into four blocks containing points. It indicates that pairs are included when both points belong to the same block; the general formula is not yet written on this page.

**Textbook cross-reference:** §9.5, Definition 9.5.6 (partition), printed p. 333 (PDF p. 341); §9.10.1, printed pp. 342–343 (PDF pp. 350–351), for the correspondence with equivalence relations.

<a id="pdf-page-061"></a>
## PDF page 061 — A finite relation written from three blocks

The partition diagram has the blocks

$$\{a,b,c\},\qquad\{d,e\},\qquad\{f,g\}.$$

The source writes the complete induced relation:

$$
\begin{aligned}
R=\{& (a,a),(b,b),(c,c),\\
& (a,b),(b,c),(c,a),\\
& (b,a),(c,b),(a,c),\\
& (d,d),(e,e),(d,e),(e,d),\\
& (f,f),(g,g),(f,g),(g,f)\}.
\end{aligned}
$$

Thus every ordered pair within a block is included, and no pair between different blocks is included.

**Textbook cross-reference:** §9.10.1, Equivalence Classes, printed pp. 342–343 (PDF pp. 350–351), for the equivalence relation induced by a partition.

<a id="pdf-page-062"></a>
## PDF page 062 — Points within distance one: reflexivity and symmetry

**Question 1.** On $\mathbb R^2$, define

$$x\sim y\quad\text{if }\|x-y\|<1,\qquad x,y\in\mathbb R^2.$$

For **reflexivity**,

$$\|x-x\|=0<1.$$

For **symmetry**, start with $x\sim y$, so $\|x-y\|<1$. The calculation uses

$$\|y-x\|=\|-(x-y)\|=\|x-y\|<1,$$

and hence $y\sim x$. The page also writes the relation notation $xRy$, $yRx$ under this argument. Some intermediate inequalities abbreviate the norm bars, but the relation's top definition clearly uses the norm.

**Textbook cross-reference:** §9.10, Definition 9.10.1, printed pp. 341–342 (PDF pp. 349–350); §9.11, Summary of Relational Properties, printed p. 343 (PDF p. 351).

<a id="pdf-page-063"></a>
## PDF page 063 — Points within distance one: failure of transitivity

The transitivity test asks whether $x\sim y$ and $y\sim z$ imply $x\sim z$. Choose

$$x=(0,0),\qquad y=\left(\frac34,0\right),\qquad z=\left(\frac32,0\right).$$

The first two comparisons are marked with checks, and the page marks the overall transitivity claim as false. A small coordinate-axis sketch shows points and the segment between nearby points.

**Textbook clarification:** The distances are

$$\|x-y\|=\frac34<1,\qquad\|y-z\|=\frac34<1,$$

but

$$\|x-z\|=\frac32>1.$$

Thus $x\sim y$ and $y\sim z$, while $x\not\sim z$. The relation is reflexive and symmetric, but is not an equivalence relation. This is the transitivity criterion in §9.11, printed p. 343 (PDF p. 351).

**Textbook cross-reference:** §9.10, printed pp. 341–342 (PDF pp. 349–350); §9.11, printed p. 343 (PDF p. 351).

<a id="pdf-page-064"></a>
## PDF page 064 — Equality of norms as an equivalence relation

**Question 2.** On $\mathbb R^2$, define

$$x\sim y\quad\text{if }\|x\|=\|y\|.$$

The source gives three shorthand equality checks:

$$x=x;\qquad x=y\ \Longrightarrow\ y=x;\qquad x=y,\ y=z\ \Longrightarrow\ x=z.$$

Here these checks apply to the **norm values**. More explicitly,

$$\|x\|=\|x\|,$$
$$\|x\|=\|y\|\ \Longrightarrow\ \|y\|=\|x\|,$$
$$\|x\|=\|y\|,\ \|y\|=\|z\|\ \Longrightarrow\ \|x\|=\|z\|.$$

Below a dividing line, $[x]$ is described as the set of all points $y\in\mathbb R^2$ that are related to $x$, namely those satisfying $\|x\|=\|y\|$.

**Textbook cross-reference:** §9.10, Definition 9.10.2, printed p. 342 (PDF p. 350): use the function $f(x)=\|x\|$; §9.10.1, Definition 9.10.3, on the same page, for its classes.

<a id="pdf-page-065"></a>
## PDF page 065 — The classes are circles centered at the origin

The page draws a circle centered at the intersection of coordinate axes. It lists representative points for several norm values:

- Norm $0$: $(0,0)$.
- Norm $1$: $(0,1)$, $(1,0)$, $(-1,0)$.
- Norm $2$: $(0,2)$, $(-2,0)$.

The source labels these lists $[0]$, $[1]$, and $[2]$, and includes the calculation

$$\sqrt{0^2+1^2}=1.$$

**Notation clarification:** The domain consists of vectors, so the scalar labels here name the **radius** of a class. For example, “$[1]$” means the class of any vector with norm one. The listed points are examples, not a complete list of the circle.

The displayed class definition, repeated and boxed, is

$$[x]=\{y\in\mathbb R^2\mid x\sim y\}
=\{y\in\mathbb R^2\mid\|x\|=\|y\|\}.$$

**Textbook clarification:** For $x\ne(0,0)$ this is the entire circle of radius $\|x\|$ centered at the origin. For $x=(0,0)$, it is the singleton $\{(0,0)\}$. This specializes Definition 9.10.3, printed p. 342 (PDF p. 350).

**Textbook cross-reference:** §9.10–§9.10.1, printed p. 342 (PDF p. 350).

<a id="pdf-page-066"></a>
## PDF page 066 — Equal norms do not give antisymmetry

Under the heading **Antisymmetry**, the notes consider

$$x\sim y,\qquad y\sim x,\qquad y=x.$$

The equality $\|y\|=\|x\|$ is circled, and the vectors

$$(0,1)\qquad\text{and}\qquad(1,0)$$

are written as the test pair. A large arrow points from them toward the proposed conclusion $y=x$.

**Textbook clarification:** Both vectors have norm one, so they are related in both directions, but they are distinct. Thus the proposed antisymmetry implication fails. The relation is an equivalence relation, but it is not a partial order. Compare antisymmetry and weak partial orders in §9.6.3, printed p. 338 (PDF p. 346), and equivalence relations in §9.10, printed pp. 341–342 (PDF pp. 349–350).

**Textbook cross-reference:** §9.6.3, printed p. 338 (PDF p. 346); §9.10, printed pp. 341–342 (PDF pp. 349–350).

<a id="pdf-page-067"></a>
## PDF page 067 — Equality of the sum-of-absolute-values norm

**Question 3.** On $\mathbb R^3$, define $x\sim y$ if $|x|=|y|$, where the page defines

$$|x|=|x_1|+|x_2|+|x_3|.$$

This is the $\ell_1$ norm; writing it as $\|x\|_1$ distinguishes the vector norm from scalar absolute value.

The source checks reflexivity by $x\sim x$. It illustrates symmetry using the shorthand $x=y$, $y=x$, and transitivity using $|x|=|y|$ and $|y|=|z|$. As in question 2, these are equalities of the norm values.

The class definition is

$$[x]=\{y\in\mathbb R^3\mid x\sim y\}.$$

A small axis sketch contains a point. Beneath the class formula is an unfinished or crossed-out norm calculation, whose final value is **[unclear in source]**.

**Textbook clarification:** Taking $f(x)=|x_1|+|x_2|+|x_3|$, the relation is equality of function values, so it is an equivalence relation. Its class is

$$[x]=\left\{y\in\mathbb R^3\;\middle|\;|y_1|+|y_2|+|y_3|=|x_1|+|x_2|+|x_3|\right\}.$$

This applies Definition 9.10.2 and the class definition in §9.10.1, printed p. 342 (PDF p. 350).

**Textbook cross-reference:** §9.10–§9.10.1, printed p. 342 (PDF p. 350).

<a id="pdf-page-068"></a>
## PDF page 068 — Verdict on the three-dimensional norm example

The page gives the example vectors

$$(1,0,0),\qquad(-1,0,0),\qquad\ldots$$

inside norm bars. It labels their common class $[1]$, with further entries left as dashes. Both vectors have $\ell_1$ norm one, so the scalar label again stands for the norm value.

The final verdicts are:

- **Equivalence relation:** check.
- **Classes:** check.
- **Poset:** marked false.

**Textbook clarification:** The two listed vectors are distinct but related in both directions, which supplies the counterexample to antisymmetry. The entire norm-one class is $\{y\in\mathbb R^3:|y_1|+|y_2|+|y_3|=1\}$, as determined on page 067.

**Textbook cross-reference:** §9.6.3, printed p. 338 (PDF p. 346); §9.10–§9.10.1, printed p. 342 (PDF p. 350).

<a id="pdf-page-069"></a>
## PDF page 069 — A difference-of-squares relation

**Question 4.** On $\mathbb R$, define

$$x\sim y\quad\text{if }x^2-y^2=1.$$

For **reflexivity**, test $x\sim x$:

$$x^2-x^2=0\ne1.$$

Thus the relation is not reflexive. The source supplies no further property checks on this page.

**Textbook clarification:** Failure of reflexivity already rules out both an equivalence relation and a weak partial order, by Definitions 9.10.1 and 9.6.13.

**Textbook cross-reference:** §9.6.3, printed p. 338 (PDF p. 346); §9.10, printed p. 341 (PDF p. 349).

<a id="pdf-page-070"></a>
## PDF page 070 — Two subsets whose intersection has one element

**Question 5.** On $\mathcal P(S)$, define

$$x\sim y\quad\text{if }|x\cap y|=1.$$

For $S=\{1,2\}$, the power set is written as

$$\mathcal P(S)=\{\varnothing,\{1\},\{2\},\{1,2\}\}.$$

The page tests reflexivity by asking for

$$|x\cap x|=1.$$

This line has both a check-like mark and a false mark nearby. An isolated $\varnothing$ is also marked false on the right.

**Textbook clarification:** Since $x\cap x=x$, the condition holds only when $x$ is a singleton. It fails for $x=\varnothing$ and for $x=\{1,2\}$. Consequently the relation on the whole power set is not reflexive. The marks can be understood as distinguishing the singleton cases from the failed cases.

**Textbook cross-reference:** §4.1, Sets, printed pp. 81–85 (PDF pp. 89–93), for power sets and intersection; §9.11, Summary of Relational Properties, printed p. 343 (PDF p. 351).

<a id="pdf-page-071"></a>
## PDF page 071 — Consecutive integers as a relation

**Question 6.** On $\mathbb Z$, define

$$x\sim y\quad\text{if }y-x=1.$$

For the reflexivity test $x\sim x$, the page writes

$$x-x\ne1.$$

Since $x-x=0$, the relation is not reflexive. No further checks are written here.

**Textbook clarification:** This excludes both an equivalence relation and a weak partial order, whose definitions require reflexivity.

**Textbook cross-reference:** §9.6.3, printed p. 338 (PDF p. 346); §9.10, printed p. 341 (PDF p. 349).

<a id="pdf-page-072"></a>
## PDF page 072 — A diagram comparing finer and coarser subdivisions

The page writes $R_1\sim R_2$ above two grid-like diagrams. The left drawing has more horizontal and vertical dividing lines, with a small oval in one region. The right drawing has fewer dividing lines and larger regions.

There is no formula or definition of $\sim$ on this page. Read with pages 059 and 073, it illustrates **refinement**: the finer subdivision has smaller blocks, and each small block lies in a block of the coarser subdivision.

**Textbook cross-reference:** §9.10.1, Equivalence Classes, printed pp. 342–343 (PDF pp. 350–351), for relations viewed as partitions. The refinement terminology is defined in the lecture notes on page 059.

<a id="pdf-page-073"></a>
## PDF page 073 — Ordering the set of equivalence relations by refinement

**Question 7.** Fix a set $S$, and let

$$M=\{R\mid R\text{ is an equivalence relation on }S\}.$$

Define a relation $\sim$ on $M$ by “finer than”:

$$R_1\sim R_2\quad\Longleftrightarrow\quad
\forall a,b\in S,\quad aR_1b\ \Longrightarrow\ aR_2b.$$

The page circles $(M,\sim)$ and boxes the implication $aR_1b\Rightarrow aR_2b$. Thus $\sim$ here compares **relations**, rather than comparing elements of $S$.

For **reflexivity**, take $R\in M$. Then $R\sim R$, because

$$aRb\quad\Longrightarrow\quad aRb.$$

The note says that every equation implies itself.

**Textbook clarification:** Regard each $R\in M$ as its set of ordered pairs in $S\times S$. Then $R_1\sim R_2$ is exactly $R_1\subseteq R_2$. This is set inclusion restricted to the family $M$, so the partial-order results apply. Compare §9.6.3, printed pp. 337–338 (PDF pp. 345–346), and §9.7, printed p. 339 (PDF p. 347).

**Textbook cross-reference:** §4.4, Binary Relations, printed p. 89 (PDF p. 97); §9.6.3, printed pp. 337–338 (PDF pp. 345–346); §9.10.1, printed pp. 342–343 (PDF pp. 350–351).

<a id="pdf-page-074"></a>
## PDF page 074 — Antisymmetry of refinement

Assume

$$R_1\sim R_2\qquad\text{and}\qquad R_2\sim R_1.$$

The first assumption says

$$aR_1b\quad\Longrightarrow\quad aR_2b,$$

and the second says

$$aR_2b\quad\Longrightarrow\quad aR_1b.$$

Therefore, for every $a,b\in S$,

$$aR_1b\quad\Longleftrightarrow\quad aR_2b.$$

The source explains: for every pair $(a,b)$, $R_1$ contains the pair if and only if $R_2$ contains it. Hence the two relations contain exactly the same ordered pairs, so $R_1=R_2$. This establishes antisymmetry of the refinement relation on $M$.

**Textbook cross-reference:** §4.4, Definition 4.4.1, printed p. 89 (PDF p. 97); §9.6.3, Definition 9.6.12, printed p. 338 (PDF p. 346).

<a id="pdf-page-075"></a>
## PDF page 075 — Transitivity of refinement and the resulting poset

Assume

$$R_1\sim R_2\qquad\text{and}\qquad R_2\sim R_3.$$

To show $R_1\sim R_3$, the source writes the two implications

$$aR_1b\quad\Longrightarrow\quad aR_2b\tag{1}$$

and

$$aR_2b\quad\Longrightarrow\quad aR_3b.\tag{2}$$

From (1) and (2),

$$aR_1b\quad\Longrightarrow\quad aR_3b.$$

Therefore $R_1\sim R_3$, proving transitivity.

Together, pages 073–075 establish reflexivity, antisymmetry, and transitivity, so $(M,\sim)$ is a poset. In this notation:

- $S$ is the fixed underlying set.
- $M$ is the set of **all equivalence relations on $S$**.
- $R_1,R_2,R_3$ are elements of $M$.
- $R_1\sim R_2$ means $R_1$ is **finer than** $R_2$, equivalently $R_1\subseteq R_2$ as sets of ordered pairs.

The next PDF page continues this conclusion.

**Textbook cross-reference:** §9.6.3, Weak Partial Orders, Definitions 9.6.12–9.6.13, printed p. 338 (PDF p. 346); §9.7, Representing Partial Orders by Set Containment, printed p. 339 (PDF p. 347).
