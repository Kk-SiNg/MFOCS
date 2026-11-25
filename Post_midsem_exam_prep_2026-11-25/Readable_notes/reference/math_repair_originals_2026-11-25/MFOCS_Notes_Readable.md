# CS208 MFOCS — Readable handwritten notes

**Coverage:** All 221 PDF pages transcribed.

Sources: [handwritten notes PDF](../../Study_material_after_mid_sems/MFOCS_Notes_Aug-Nov_2026.pdf) and [Lehman–Leighton–Meyer textbook](../../Study_material_after_mid_sems/MCS_Textbook_Lehman_Leighton_Meyer.pdf).

Use [the browser reader](Readable_notes.html) for rendered formulas and page search, or [the page index](Page_index.md) for navigation. PDF page numbers refer to the notes. Textbook PDF page number equals printed Arabic page number plus 8.

This is a visual transcription into readable prose and LaTeX. Definitions, examples, proof steps and meaningful diagram information are retained. Unfinished source exercises remain unfinished. Unclear handwriting and source qualifications are identified in place. Explicit textbook clarifications are distinguished from the handwritten content. Administrative annotations are retained without guessing their meaning.

<a id="pdf-page-001"></a>
## PDF page 001 — Sets and membership

[Original scan](source_pages/page_001.png)

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

[Original scan](source_pages/page_002.png)

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

[Original scan](source_pages/page_003.png)

For a set $A$ inside a universal set $U$, its complement is

$$\overline A=\{a\in U\mid a\notin A\}.$$

Example: take $U=\mathbb N$ and let $A$ be the even natural numbers. The source leaves the line “$\overline A=$” blank as an exercise.

**Textbook clarification:** The complement in this example is the odd natural numbers, because complementation is taken relative to $U$. See §4.1, printed pp. 81–85.

<a id="pdf-page-004"></a>
## PDF page 004 — Ordered tuples and Cartesian products

[Original scan](source_pages/page_004.png)

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

[Original scan](source_pages/page_005.png)

The first sketch is a two-ended line labelled $\mathbb R$, representing the real line. A parallelogram represents the plane, with the accompanying notation

$$\mathbb R\times\mathbb R=\mathbb R^2.$$

A second sketch is a table with columns **Name**, **Roll number**, and **Address**. It illustrates records containing several ordered fields. The rows are indicated only by dots; no particular records are specified.

**Textbook cross-reference:** §4.1–§4.2, Sets and Sequences.

<a id="pdf-page-006"></a>
## PDF page 006 — Functions, domain, codomain and image

[Original scan](source_pages/page_006.png)

For nonempty sets $A,B$, a **function** $f:A\to B$ assigns a unique element of $B$ to every element of $A$.

$A$ is the **domain** and $B$ is the **codomain**. The **range** consists of the values actually reached by the function.

The arrow sketch shows three domain elements: two map to one codomain element and the third maps to another. An additional codomain element lies outside the circled range. Thus a function may assign the same output to distinct inputs, and its range may be smaller than its codomain.

The page gives the example $f:\mathbb N\to\mathbb N$, with a square-function formula written as $f(a)=x^2$; the input-letter mismatch is retained here rather than silently treated as a new formula.

When $f(a)=b$, the page labels $a$ a **preimage** and $b$ an **image**.

**Textbook cross-reference:** §4.3, Functions.

<a id="pdf-page-007"></a>
## PDF page 007 — Injective functions

[Original scan](source_pages/page_007.png)

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

[Original scan](source_pages/page_008.png)

A function $f:A\to B$ is **bijective** if it is both injective and surjective.

Examples:

- $f:\mathbb R\to\mathbb R$, $f(x)=x$.
- $f:\mathbb R\to\mathbb R$, $f(x)=x^3$.
- $f:[-\pi/2,\pi/2]\to[-1,1]$, $f(x)=\sin x$.

The restricted sine function uses a different domain from the sine example on page 007.

**Textbook cross-reference:** §4.4.1, Definition 4.4.2, printed p. 91 (PDF p. 99), for function properties; §4.5 and §7.1 for cardinality comparisons.

<a id="pdf-page-009"></a>
## PDF page 009 — Inverse functions and necessary/sufficient conditions

[Original scan](source_pages/page_009.png)

If $f:A\to B$ is bijective, an inverse function $f^{-1}:B\to A$ is defined by

$$f^{-1}(b)=a\quad\text{such that }f(a)=b.$$

The source adds “$f^{-1}$ exists” without a further proof.

At the bottom it introduces the phrases “$P$ necessary [for] $Q$” and “$P$ sufficient [for] $Q$”. No implication formulas or examples are supplied on this page.

**Textbook cross-reference:** §4.4, Binary Relations, for inverse relations; §1.5 and §3.1.2 for implications.

<a id="pdf-page-010"></a>
## PDF page 010 — Surjective functions

[Original scan](source_pages/page_010.png)

A function $f:A\to B$ is **surjective**, or **onto**, if every element $b\in B$ has a preimage in $A$:

$$\forall b\in B\ \exists a\in A\text{ such that }f(a)=b.$$

**Textbook cross-reference:** §4.4.1, Definition 4.4.2, printed p. 91 (PDF p. 99), for function properties; §4.5 and §7.1 for cardinality comparisons.

<a id="pdf-page-011"></a>
## PDF page 011 — Comparing cardinalities using functions

[Original scan](source_pages/page_011.png)

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

[Original scan](source_pages/page_012.png)

The page states

$$|[0,1]|=|[0,10]|.$$

It labels the intervals $A=[0,1]$ and $B=[0,10]$ and gives the bijection

$$f:A\to B,\qquad f(x)=10x.$$

The accompanying number-line sketch marks 0, an intermediate point labelled 2, and 10.

**Textbook cross-reference:** §7.1, Infinite Cardinality, printed p. 206 onward.

<a id="pdf-page-013"></a>
## PDF page 013 — Bijections between open intervals and the real line

[Original scan](source_pages/page_013.png)

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

[Original scan](source_pages/page_014.png)

Let $A=\mathbb N$ and let $B$ be the even natural numbers. The page gives

$$f:A\to B,\qquad f(x)=2x.$$

This pairs each natural number with an even natural number.

The lower part of the page introduces a second pair of sets, $A=\mathbb R$ and $B=[-1,1]$, alongside a two-directional line sketch. No mapping formula or conclusion is written for this second example.

**Textbook cross-reference:** §7.1, Infinite Cardinality, printed p. 206 onward.

<a id="pdf-page-015"></a>
## PDF page 015 — Countable sets and their subsets

[Original scan](source_pages/page_015.png)

A set $X$ is **countable** if it is either finite or has the same cardinality as $\mathbb N$.

If $X$ is countable, then any subset of $X$ is also countable.

The sketch lists $x_1,x_2,x_3,\ldots$ and identifies selected elements with $y_1,y_2,\ldots$ from a subset $Y\subseteq X$. The first selected element is $x_1$ and the second shown is $x_3$, illustrating that one can retain selected entries from a listing of $X$.

**Textbook cross-reference:** §7.1.2, Countable Sets, printed pp. 209–210 (PDF pp. 217–218).

<a id="pdf-page-016"></a>
## PDF page 016 — Listing a Cartesian product of countable sets

[Original scan](source_pages/page_016.png)

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

[Original scan](source_pages/page_017.png)

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

[Original scan](source_pages/page_018.png)

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

[Original scan](source_pages/page_019.png)

The notes first recall $\mathbb Z\times\mathbb Z$.

For $A\times B\times C$, let $P=A\times B$. If $A,B$ are countable, $P$ is countable. Then $P\times C$ is countable when $C$ is countable. The page identifies this with $A\times B\times C$.

Repeating the argument gives the statement:

> The Cartesian product of finitely many countable sets is countable.

The source illustrates a finite list of factors as $A\times B\times C\times D\times E\times\cdots\times N$; the last $N$ is a factor label.

**Textbook cross-reference:** §7.1.2, Countable Sets, printed pp. 209–210 (PDF pp. 217–218).

<a id="pdf-page-020"></a>
## PDF page 020 — Finite unions of countable sets

[Original scan](source_pages/page_020.png)

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

[Original scan](source_pages/page_021.png)

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

[Original scan](source_pages/page_022.png)

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

[Original scan](source_pages/page_023.png)

An **enumeration** of a set is a complete, ordered listing of its elements.

The sketch labels the elements of a set $A$ by the natural numbers $1,2,3,4,\ldots$, producing a listing

$$a_1,a_2,a_3,\ldots.$$

The separate notes $\mathbb N$, $1,2,3,\ldots$, and $1\le2$ emphasize the ordering of the labels.

**Textbook cross-reference:** §7.1.2, Countable Sets, printed pp. 209–210 (PDF pp. 217–218).

<a id="pdf-page-024"></a>
## PDF page 024 — Finite sequences of natural numbers

[Original scan](source_pages/page_024.png)

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

[Original scan](source_pages/page_025.png)

This sparse page contains only the collection

$$\{(1,2),(2,1),(1,1),\ldots\}.$$

No additional definition, question, or conclusion is written. In particular, the order within a pair distinguishes $(1,2)$ from $(2,1)$.

**Textbook cross-reference:** §4.1–§4.2, Sets and Sequences, printed pp. 81–86.

<a id="pdf-page-026"></a>
## PDF page 026 — Finite subsets of the natural numbers

[Original scan](source_pages/page_026.png)

**Claim:** The set of all finite subsets of $\mathbb N$ is countable.

No proof is written on this page.

**Textbook cross-reference:** §4.1.3, Power Set, printed p. 83 (PDF p. 91); §7.1.2, Countable Sets, printed pp. 209–210 (PDF pp. 217–218).

<a id="pdf-page-027"></a>
## PDF page 027 — First diagonal argument for the power set

[Original scan](source_pages/page_027.png)

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

[Original scan](source_pages/page_028.png)

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

[Original scan](source_pages/page_029.png)

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

[Original scan](source_pages/page_030.png)

**Claim:** The set of real numbers $\mathbb R$ is uncountable.

The page proposes an injection $T\to\mathbb R$, where $T$ is the uncountable set of infinite 0–1 sequences from page 029. It illustrates a sequence

$$t=010001011\cdots$$

and maps it to a real with those digits after the point:

$$f(t)=0.t=0.010001011\cdots.$$

The notes also recall a map $(0,1)\to\mathbb R$ and compare $(0,1)$ with $[0,1]$.

**Textbook clarification:** For the displayed 0–1 digit construction, interpreting $0.t$ as a decimal expansion gives an injection: the permitted digits exclude the repeating-9 ambiguity. A binary interpretation needs care because some binary expansions are not unique. The source does not specify the base on this page. See §7.1.3, Corollary 7.1.15 and its decimal-expansion proof, printed pp. 212–213 (PDF pp. 220–221).

<a id="pdf-page-031"></a>
## PDF page 031 — Binary relations

[Original scan](source_pages/page_031.png)

For sets $A,B$, a **binary relation from $A$ to $B$** is a subset of $A\times B$. Its members are ordered pairs $(a,b)$ with $a\in A$ and $b\in B$.

Example: take $A=B=\mathbb N$ and include $(a,b)$ precisely when $a<b$.

The relation can be written $aRb$; the page also shows $a\sim b$ as alternative relation notation.

**Textbook cross-reference:** §4.4, Binary Relations, printed p. 89 onward.

<a id="pdf-page-032"></a>
## PDF page 032 — Relations on a set

[Original scan](source_pages/page_032.png)

For $A=\mathcal P(\mathbb N)$, consider the relation

$$aRb\quad\text{if }a\subseteq b.$$

A relation **on** $A$ relates members of $A$ to other members of $A$.

Another example is a relation on $\mathbb N$ defined by

$$aRb\quad\text{if }a\mid b.$$

**Textbook cross-reference:** §4.4, printed p. 89; §9.6, Partial Orders, printed p. 335 onward.

<a id="pdf-page-033"></a>
## PDF page 033 — Reflexive relations

[Original scan](source_pages/page_033.png)

A relation $R$ on a set $S$ is **reflexive** if

$$\forall a\in S,\quad aRa.$$

The middle of the page shows an example pair written $(\mathbb R^{[\text{unclear in source}]},R)$; the superscript and the relation's rule are not clearly specified there.

A clear example at the bottom is a relation on $\mathbb C$:

$$aRb\quad\text{if }|a|=|b|.$$

**Textbook cross-reference:** §9.11, Summary of Relational Properties, printed p. 343.

<a id="pdf-page-034"></a>
## PDF page 034 — Symmetric relations

[Original scan](source_pages/page_034.png)

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

[Original scan](source_pages/page_035.png)

A relation $R$ on $S$ is **antisymmetric** if

$$aRb\text{ and }bRa\implies a=b.$$

Examples on $\mathbb R$, both marked with a check:

- $aRb$ if $a=b+1$.
- $aRb$ if $a<b$.

**Textbook cross-reference:** §9.6, Partial Orders, printed p. 335 onward; §9.11, printed p. 343.

<a id="pdf-page-036"></a>
## PDF page 036 — Tutorial 1: a bijection from a half-open to an open interval

[Original scan](source_pages/page_036.png)

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

[Original scan](source_pages/page_037.png)

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

[Original scan](source_pages/page_038.png)

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

[Original scan](source_pages/page_039.png)

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

[Original scan](source_pages/page_040.png)

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

[Original scan](source_pages/page_041.png)

Continue the map $f:\mathbb R\to\mathbb R^+$, $f(x)=e^x$ from page 040. For any $y>0$, solve

$$y=e^x\quad\Longrightarrow\quad x=\log y.$$

Then

$$f(x)=e^x=e^{\log y}=y.$$

Thus every positive real number has a preimage. Together with the injectivity calculation on page 040, this gives a bijection. The right margin writes both directions $\mathbb R\to\mathbb R^+$ and $\mathbb R^+\to\mathbb R$, with the inverse indicated by $\log x$.

**Textbook cross-reference:** §4.4, Binary Relations (function properties), printed pp. 89–92 (PDF pp. 97–100); §7.1, Infinite Cardinality, printed pp. 206–210 (PDF pp. 214–218).

<a id="pdf-page-042"></a>
## PDF page 042 — Adding zero to the positive reals

[Original scan](source_pages/page_042.png)

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

[Original scan](source_pages/page_043.png)

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

[Original scan](source_pages/page_044.png)

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

[Original scan](source_pages/page_045.png)

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

[Original scan](source_pages/page_046.png)

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

[Original scan](source_pages/page_047.png)

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

[Original scan](source_pages/page_048.png)

**Tutorial question 8.** Compare $[0,1]$ and $\mathbb R$. The page starts with the composition notation $f(g(x))$.

From question 3, the notes recall

$$|[0,1]|=|(0,1)|.$$

From question 7, they recall

$$|(0,1)|=|\mathbb R|.$$

Since the composition of two bijections is a bijection, the source concludes that $g\circ f$ is a bijection, where $f$ maps the closed interval to the open interval and $g$ maps the open interval to the real line. The starting $f(g(x))$ uses the opposite symbol order; the domains determine the intended composition.

**Textbook cross-reference:** §7.1, Lemma 7.1.3, printed pp. 206–207 (PDF pp. 214–215), for transitivity of equal cardinality; Problem 4.19(b), printed p. 105 (PDF p. 113), asks for the composition-of-bijections result.

<a id="pdf-page-049"></a>
## PDF page 049 — Transitive relations

[Original scan](source_pages/page_049.png)

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

[Original scan](source_pages/page_050.png)

A relation $R$ on $A$ is an **equivalence relation** if $R$ is reflexive, symmetric, and transitive.

One example has $A$ equal to the set of all triangles in $\mathbb R^2$, with

$$a\sim b\quad\text{if triangle }a\text{ is similar to triangle }b.$$

Another construction begins with a function $f:X\to Y$. Define a relation on $X$ by

$$a\sim b\quad\text{if }f(a)=f(b),\qquad a,b\in X.$$

The page denotes the resulting pair by $(X,\sim)$.

**Textbook cross-reference:** §9.10, Equivalence Relations, printed pp. 341–342 (PDF pp. 349–350), particularly the relation defined by equality of the values of a function; §9.11, printed p. 343 (PDF p. 351).

<a id="pdf-page-051"></a>
## PDF page 051 — Examples to check for equivalence

[Original scan](source_pages/page_051.png)

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

[Original scan](source_pages/page_052.png)

A relation $R$ on a set $A$ is a **partial order** if it is reflexive, antisymmetric, and transitive. The pair $(A,R)$ is called a **poset**.

The example is $(\mathbb Z,\le)$. Its antisymmetry condition is illustrated by

$$a\le b\text{ and }b\le a\quad\Longrightarrow\quad a=b.$$

**Textbook cross-reference:** §9.6.3, Weak Partial Orders, printed pp. 337–338 (PDF pp. 345–346), especially Definitions 9.6.12–9.6.13.

<a id="pdf-page-053"></a>
## PDF page 053 — Divisibility and inclusion as proposed orders

[Original scan](source_pages/page_053.png)

The first proposed example is $(\mathbb Z,\mid)$, with $a\mid b$. The source writes

$$a\mid b\text{ and }b\mid a\quad\Longrightarrow\quad a=b.$$

**Source correction / textbook clarification:** On all of $\mathbb Z$, this implication is false: $1\mid-1$ and $-1\mid1$, but $1\ne-1$. Divisibility is a partial order on the **positive integers**, where mutual divisibility does imply equality. This follows from divisibility in §8.1, printed pp. 243–247 (PDF pp. 251–255), together with antisymmetry in §9.6.3, printed p. 338 (PDF p. 346).

The second example starts with an arbitrary set $S$ and gives

$$\bigl(\mathcal P(S),\subseteq\bigr),$$

the power set ordered by set inclusion.

**Textbook cross-reference:** §8.1, Divisibility, printed pp. 243–247 (PDF pp. 251–255); §9.6.3, printed pp. 337–338 (PDF pp. 345–346); §9.7, Representing Partial Orders by Set Containment, printed p. 339 (PDF p. 347).

<a id="pdf-page-054"></a>
## PDF page 054 — Comparing infinite binary sequences

[Original scan](source_pages/page_054.png)

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

[Original scan](source_pages/page_055.png)

Let $R$ be an equivalence relation on a set $A$. For $a\in A$, its **equivalence class** is

$$[a]=\{b\in A\mid aRb\}.$$

The example returns to triangles under similarity, denoted $(\Delta\text{'s},\sim)$. If $a$ is equilateral, the page asks

$$[a]=\ ?$$

**Textbook clarification:** In this example, $[a]$ consists of all equilateral triangles: every triangle similar to an equilateral triangle is equilateral, and all equilateral triangles are similar. This applies the definition of an equivalence class in §9.10.1, printed p. 342 (PDF p. 350).

At the bottom, a separate sketch labelled $a$ depicts a triangle with a right-angle marker and tiny angle labels **[unclear in source]**. This sketch does not depict an equilateral triangle; the source does not explain how it relates to the preceding example.

**Textbook cross-reference:** §9.10.1, Equivalence Classes, Definition 9.10.3, printed p. 342 (PDF p. 350).

<a id="pdf-page-056"></a>
## PDF page 056 — Congruence classes modulo five

[Original scan](source_pages/page_056.png)

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

[Original scan](source_pages/page_057.png)

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

[Original scan](source_pages/page_058.png)

A rectangular diagram of $A$ is divided into five regions labelled

$$[a],\ [b],\ [c],\ [d],\ [e].$$

Each region represents a different equivalence class, and the classes fill the set without overlap. Below it are the words “congruence modulo $m$” and the pairs

$$(\mathbb Z,=)\qquad\text{and}\qquad(\mathbb Z,\sim),$$

with $a\sim b$ written under the second pair. No further relation rule is supplied here beyond the preceding congruence example.

**Textbook clarification:** Equality gives the singleton classes $[a]=\{a\}$. Congruence modulo $m$ groups integers by their remainders, so its classes are larger. Both are partitions of $\mathbb Z$, by Theorem 9.10.4, printed p. 343 (PDF p. 351).

**Textbook cross-reference:** §9.10.1, printed pp. 342–343 (PDF pp. 350–351).

<a id="pdf-page-059"></a>
## PDF page 059 — Finer relations and partition refinement

[Original scan](source_pages/page_059.png)

Consider $(S,R_1)$ and $(S,R_2)$. The source defines $R_1$ to be **finer than** $R_2$ if

$$\forall a,b\in S,\qquad aR_1b\ \Longrightarrow\ aR_2b.$$

It also writes the generic logical form $p\Rightarrow q$.

The large diagram shows one set $S$ with several systems of boundaries, drawn in green, yellow, and dashed red. They illustrate partitions with different amounts of subdivision. A smaller diagram shows $S$ split into three regions containing points.

**Textbook clarification:** In the equivalence-relation setting, $R_1$ is finer than $R_2$ precisely when each $R_1$-class lies inside an $R_2$-class. As sets of ordered pairs, this is $R_1\subseteq R_2$. The textbook explains equivalence classes as partition blocks in §9.10.1, printed pp. 342–343 (PDF pp. 350–351); the particular terminology “finer” is supplied by the lecture notes.

**Textbook cross-reference:** §4.4, Binary Relations, printed p. 89 (PDF p. 97); §9.10.1, printed pp. 342–343 (PDF pp. 350–351).

<a id="pdf-page-060"></a>
## PDF page 060 — Partitions and the relation they induce

[Original scan](source_pages/page_060.png)

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

[Original scan](source_pages/page_061.png)

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

[Original scan](source_pages/page_062.png)

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

[Original scan](source_pages/page_063.png)

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

[Original scan](source_pages/page_064.png)

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

[Original scan](source_pages/page_065.png)

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

[Original scan](source_pages/page_066.png)

Under the heading **Antisymmetry**, the notes consider

$$x\sim y,\qquad y\sim x,\qquad y=x.$$

The equality $\|y\|=\|x\|$ is circled, and the vectors

$$(0,1)\qquad\text{and}\qquad(1,0)$$

are written as the test pair. A large arrow points from them toward the proposed conclusion $y=x$.

**Textbook clarification:** Both vectors have norm one, so they are related in both directions, but they are distinct. Thus the proposed antisymmetry implication fails. The relation is an equivalence relation, but it is not a partial order. Compare antisymmetry and weak partial orders in §9.6.3, printed p. 338 (PDF p. 346), and equivalence relations in §9.10, printed pp. 341–342 (PDF pp. 349–350).

**Textbook cross-reference:** §9.6.3, printed p. 338 (PDF p. 346); §9.10, printed pp. 341–342 (PDF pp. 349–350).

<a id="pdf-page-067"></a>
## PDF page 067 — Equality of the sum-of-absolute-values norm

[Original scan](source_pages/page_067.png)

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

[Original scan](source_pages/page_068.png)

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

[Original scan](source_pages/page_069.png)

**Question 4.** On $\mathbb R$, define

$$x\sim y\quad\text{if }x^2-y^2=1.$$

For **reflexivity**, test $x\sim x$:

$$x^2-x^2=0\ne1.$$

Thus the relation is not reflexive. The source supplies no further property checks on this page.

**Textbook clarification:** Failure of reflexivity already rules out both an equivalence relation and a weak partial order, by Definitions 9.10.1 and 9.6.13.

**Textbook cross-reference:** §9.6.3, printed p. 338 (PDF p. 346); §9.10, printed p. 341 (PDF p. 349).

<a id="pdf-page-070"></a>
## PDF page 070 — Two subsets whose intersection has one element

[Original scan](source_pages/page_070.png)

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

[Original scan](source_pages/page_071.png)

**Question 6.** On $\mathbb Z$, define

$$x\sim y\quad\text{if }y-x=1.$$

For the reflexivity test $x\sim x$, the page writes

$$x-x\ne1.$$

Since $x-x=0$, the relation is not reflexive. No further checks are written here.

**Textbook clarification:** This excludes both an equivalence relation and a weak partial order, whose definitions require reflexivity.

**Textbook cross-reference:** §9.6.3, printed p. 338 (PDF p. 346); §9.10, printed p. 341 (PDF p. 349).

<a id="pdf-page-072"></a>
## PDF page 072 — A diagram comparing finer and coarser subdivisions

[Original scan](source_pages/page_072.png)

The page writes $R_1\sim R_2$ above two grid-like diagrams. The left drawing has more horizontal and vertical dividing lines, with a small oval in one region. The right drawing has fewer dividing lines and larger regions.

There is no formula or definition of $\sim$ on this page. Read with pages 059 and 073, it illustrates **refinement**: the finer subdivision has smaller blocks, and each small block lies in a block of the coarser subdivision.

**Textbook cross-reference:** §9.10.1, Equivalence Classes, printed pp. 342–343 (PDF pp. 350–351), for relations viewed as partitions. The refinement terminology is defined in the lecture notes on page 059.

<a id="pdf-page-073"></a>
## PDF page 073 — Ordering the set of equivalence relations by refinement

[Original scan](source_pages/page_073.png)

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

[Original scan](source_pages/page_074.png)

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

[Original scan](source_pages/page_075.png)

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

<a id="pdf-page-076"></a>
## PDF page 076 — Continuation: an order on relations

[Original scan](source_pages/page_076.png)

The page contains only the two underlined notations

$$
(M,\sim), \qquad R_1\sim R_2.
$$

**Continuation/context from PDF pages 073–075:** \(M\) is the set of all equivalence relations on one fixed set \(S\). The relation \(R_1\sim R_2\) means that \(R_1\) is **finer** than \(R_2\):

$$
\forall a,b\in S,\qquad aR_1b\Rightarrow aR_2b,
$$

or equivalently \(R_1\subseteq R_2\) when the relations are viewed as sets of ordered pairs. Pages 073–075 establish reflexivity, antisymmetry, and transitivity, so \((M,\sim)\) is a poset. Here \(\sim\) is the handwritten **order symbol**, rather than a claim that the elements of \(M\) form an equivalence class. The context is supplied by the preceding source pages; it is not repeated on page 076 itself.

**Textbook cross-reference:** §9.6, weak partial orders, printed pp.337–338 (textbook PDF pp.345–346), supplies the general framework.

<a id="pdf-page-077"></a>
## PDF page 077 — Comparable elements and total orders

[Original scan](source_pages/page_077.png)

Elements \(a,b\) of a poset \((S,\preceq)\) are **comparable** if either

$$
a\preceq b \quad\text{or}\quad b\preceq a.
$$

If all elements of \((S,\preceq)\) are comparable, the order is called a **total order** or **chain**.

Examples on the page:

- \((\mathbb Z,\le)\).
- \((\mathcal P(S),\subseteq)\), with two subsets \(S_1,S_2\) drawn inside \(S\). The drawing of disjoint, nonempty subsets illustrates that neither \(S_1\subseteq S_2\) nor \(S_2\subseteq S_1\) need hold. Thus a power-set order is generally not total.

**Textbook cross-reference:** §9.8, Definition 9.8.1, printed p.340. The textbook uses “linear order” and explains the terminology difference between a total order and a total relation.

<a id="pdf-page-078"></a>
## PDF page 078 — Order-preserving maps and composition

[Original scan](source_pages/page_078.png)

Let \((S,\preceq_1)\) and \((T,\preceq_2)\) be posets. A function \(f:S\to T\) is **order-preserving**, or **monotone**, if

$$
\forall a,b\in S,\qquad
a\preceq_1 b \implies f(a)\preceq_2 f(b).
$$

**Lemma written in the notes.** Given posets
\((S,\preceq_1)\), \((T,\preceq_2)\), and \((W,\preceq_3)\), and monotone maps

$$
S\xrightarrow{f}T\xrightarrow{g}W,
$$

the composition \(g\circ f\) is also monotone.

The source records the lemma and arrow diagram but does not supply further proof steps on this page.

**Textbook cross-reference:** §9.7, Definition 9.7.1, printed p.339, discusses maps preserving a relation. That definition requires a bijection preserving the relation in both directions for isomorphism; the present definition requires only the forward implication.

<a id="pdf-page-079"></a>
## PDF page 079 — Order-reflecting maps

[Original scan](source_pages/page_079.png)

For posets \((S,\preceq_1)\) and \((T,\preceq_2)\), a function \(f:S\to T\) is **order-reflecting** if

$$
\forall a,b\in S,\qquad
f(a)\preceq_2 f(b)\implies a\preceq_1 b.
$$

**Textbook cross-reference:** §9.7, Definition 9.7.1, printed p.339, provides the related concept of relation-preserving isomorphism. Order reflection is the backward implication of that relation equivalence.

<a id="pdf-page-080"></a>
## PDF page 080 — Order reflection implies injectivity

[Original scan](source_pages/page_080.png)

**Claim.** If \(f:S\to T\) is order-reflecting between posets, then \(f\) is injective.

The proof in the notes follows the implication chain

$$
\begin{aligned}
f(a)=f(b)
&\implies f(a)\preceq_2 f(b)
       \text{ and }f(b)\preceq_2 f(a)\\
&\implies a\preceq_1 b
       \text{ and }b\preceq_1 a\\
&\implies a=b.
\end{aligned}
$$

Here \(a,b\in S\). The first step uses reflexivity of the target order, the second uses order reflection, and the last uses antisymmetry of the source order.

**Textbook cross-reference:** §9.6.3, Definitions 9.6.12–9.6.13, printed p.338, states antisymmetry and the axioms of a weak partial order; §9.7, printed p.339, gives the related relation-preserving-map framework.

<a id="pdf-page-081"></a>
## PDF page 081 — Computational geometry: convex sets

[Original scan](source_pages/page_081.png)

A set \(S\subseteq\mathbb R^n\) is **convex** if, for every \(x,y\in S\), the line segment joining \(x\) and \(y\) is entirely contained in \(S\).

**Diagrams.** A circular region contains several complete segments joining pairs of its points. A second region has an inward notch: a segment joining two points on opposite sides of the notch passes outside the region, whereas a lower segment remains inside. The latter region illustrates failure of convexity.

**Textbook cross-reference:** No matching treatment of convex sets/computational geometry was found in the supplied Lehman–Leighton–Meyer textbook. This is course-note material.

<a id="pdf-page-082"></a>
## PDF page 082 — Convexity characterized by line intersections

[Original scan](source_pages/page_082.png)

The notes give another characterization: \(S\subseteq\mathbb R^n\) is convex if, for any line \(\ell\) in \(\mathbb R^n\), the intersection \(\ell\cap S\) is a single, possibly empty, line segment.

**Diagrams.** A line through a circular region intersects it in one segment. A line across a region with a notch intersects it in separate pieces, so that region is not convex.

**Clarification of terminology:** Here “segment” describes an interval along the line; for general unbounded or open convex sets, the intersection can also be an unbounded or open interval. The literal source wording is “single (possibly empty) line segment.”

**Textbook cross-reference:** No matching computational-geometry section was found in the supplied textbook.

<a id="pdf-page-083"></a>
## PDF page 083 — Parametrizing a line segment

[Original scan](source_pages/page_083.png)

The segment joining points \(p\) and \(q\) is parametrized by

$$
rp+(1-r)q,\qquad r\in[0,1].
$$

The endpoint \(p\) corresponds to \(r=1\), and \(q\) corresponds to \(r=0\). The source diagram marks an intermediate point on the segment between them.

**Textbook cross-reference:** No matching computational-geometry section was found in the supplied textbook.

<a id="pdf-page-084"></a>
## PDF page 084 — Convex combinations

[Original scan](source_pages/page_084.png)

Given points \(p_1,\ldots,p_k\in\mathbb R^n\), take \(k\) nonnegative real numbers \(r_1,\ldots,r_k\) such that

$$
\sum_{i=1}^k r_i=1.
$$

Their **convex combination** is the point

$$
p=\sum_{i=1}^k r_i p_i.
$$

The page repeats the same conditions using coefficients \(s_1,\ldots,s_k\ge0\), with \(\sum_i s_i=1\), and the resulting sum \(\sum_i s_i p_i\).

**Textbook cross-reference:** No matching computational-geometry section was found in the supplied textbook.

<a id="pdf-page-085"></a>
## PDF page 085 — Segment and triangle examples

[Original scan](source_pages/page_085.png)

The page draws a segment with its two endpoints, followed by a triangle with an interior point. Beside the triangle it writes

$$
\sum_i r_i p_i,\qquad r_i=0.3,\quad i=1,2,3.
$$

**Source numerical error:** The three displayed coefficients \(0.3,0.3,0.3\) sum to \(0.9\), so they do not meet the normalization condition for a convex combination on page 084. The numerical values are retained exactly as written; the page does not supply corrected coefficients.

**Textbook cross-reference:** No matching computational-geometry section was found in the supplied textbook.

<a id="pdf-page-086"></a>
## PDF page 086 — Convex combinations stay in a convex set

[Original scan](source_pages/page_086.png)

If \(S\) is convex and \(p_1,\ldots,p_k\in S\subseteq\mathbb R^n\), then every convex combination of these points also belongs to \(S\).

The page marks the cases \(k=1\) and \(k=2\). Its diagram draws a segment wholly inside the region \(S\).

**Textbook cross-reference:** No matching computational-geometry section was found in the supplied textbook.

<a id="pdf-page-087"></a>
## PDF page 087 — Two sets of convex-combination coefficients

[Original scan](source_pages/page_087.png)

For points \(p_1,\ldots,p_k\in\mathbb R^n\), the notes record two convex combinations:

$$
\begin{aligned}
r_i&\in\mathbb R^+\cup\{0\},&
\sum_i r_i&=1,&
p&=\sum_i r_i p_i,\\
s_i&\in\mathbb R^+\cup\{0\},&
\sum_i s_i&=1,&
s&=\sum_i s_i p_i.
\end{aligned}
$$

Both coefficient families are nonnegative and normalized. No further conclusion is written on this page.

**Textbook cross-reference:** No matching computational-geometry section was found in the supplied textbook.

<a id="pdf-page-088"></a>
## PDF page 088 — Induction proof for convex combinations

[Original scan](source_pages/page_088.png)

**Claim repeated.** If \(S\) is convex and \(p_1,\ldots,p_k\in S\), every convex combination of those points belongs to \(S\).

The proof is by induction on \(k\). Assume the result for \(k\), and consider \(k+1\) points of \(S\). Write

$$
x=\sum_{i=1}^{k+1}r_i p_i,\qquad
r_i\ge0,\qquad
\sum_{i=1}^{k+1}r_i=1.
$$

Then

$$
\begin{aligned}
x
&=\sum_{i=1}^{k}r_i p_i+r_{k+1}p_{k+1}\\
&=\sum_{i=1}^{k}r_i p_i+
\left(1-\sum_{i=1}^{k}r_i\right)p_{k+1}.
\end{aligned}
$$

The induction step continues on the next page.

**Textbook cross-reference:** Ch.5, induction, printed pp.115–129, supports the proof method. The convex-geometry claim itself is not treated in the supplied textbook.

<a id="pdf-page-089"></a>
## PDF page 089 — Normalizing the first \(k\) coefficients

[Original scan](source_pages/page_089.png)

The previous expression is rearranged as

$$
x=
\left(\sum_{i=1}^{k}r_i\right)
\left(\sum_{i=1}^{k}
\frac{r_i}{\sum_{j=1}^{k}r_j}p_i\right)
+
\left(1-\sum_{i=1}^{k}r_i\right)p_{k+1}.
$$

The boxed inner sum is named \(y\); the notes state \(y\in S\) by the induction hypothesis. Defining

$$
r=\sum_{j=1}^{k}r_j,
$$

gives

$$
x=ry+(1-r)p_{k+1}.
$$

The page marks this as completion of the lemma: it is a convex combination of two points in \(S\).

**Source proof gap:** The displayed normalization divides by \(r\), so it applies when \(r>0\). The endpoint case \(r=0\) is not handled explicitly on the page.

**Textbook cross-reference:** Ch.5, printed pp.115–129, for induction; no matching convex-geometry section.

<a id="pdf-page-090"></a>
## PDF page 090 — Convex hull as a minimal convex superset

[Original scan](source_pages/page_090.png)

For \(P\subseteq\mathbb R^n\), the **convex hull of \(P\)** is the minimal convex set containing \(P\). The notes name this set \(C\).

A separate reminder reads “a minimal set with property \(X\).”

**Example diagram.** For \(P=\{p_1,p_2\}\), the convex hull is the entire segment joining \(p_1\) and \(p_2\), not merely its endpoints.

**Textbook cross-reference:** No matching convex-hull section was found in the supplied textbook.

<a id="pdf-page-091"></a>
## PDF page 091 — Diagrams of convex hulls

[Original scan](source_pages/page_091.png)

The page gives geometric illustrations without a written proof:

- \(P=\{p_1,p_2,p_3\}\) is represented by the three vertices of a triangle; the entire triangular region is shaded.
- Four points form a quadrilateral inside a larger enclosing region. The smaller polygon illustrates the minimal convex region determined by those points.
- A filled rectangular region is drawn.
- A nonconvex, curved region is outlined in black, with a larger red convex outline and shading around it, illustrating filling the inward indentations.
- A second shaded triangle has an interior point in addition to its vertices; the extra interior point does not enlarge the triangular hull.

**Textbook cross-reference:** No matching convex-hull section was found in the supplied textbook.

<a id="pdf-page-092"></a>
## PDF page 092 — Minimal set and intersection definitions

[Original scan](source_pages/page_092.png)

Two definitions are listed:

1. The minimal convex set containing \(P\).
2. The intersection of all convex sets containing \(P\).

The notes label these \(M\) and \(I\), respectively. Let \(\mathcal S\) denote the family of all convex sets containing \(P\). For \(S_1,S_2\in\mathcal S\), the notes state that \(S_1\cap S_2\) is convex and contains \(P\).

They also record

$$
M\in\mathcal S,\qquad
M\cap S_i=M
\quad\text{for all }S_i\in\mathcal S.
$$

The second identity is the containment property needed to identify the minimal set with the intersection.

**Textbook cross-reference:** §7.2, sets and their operations, printed p.212 onward, supplies the set-intersection language; convexity is course-specific.

<a id="pdf-page-093"></a>
## PDF page 093 — The minimality argument

[Original scan](source_pages/page_093.png)

Let \(M\) be a minimal convex set containing \(P\), and let \(S_1\) be another convex set containing \(P\). Define

$$
Y=M\cap S_1.
$$

Then \(Y\) is convex and contains \(P\), because both intersected sets have these properties. The page records

$$
Y\subseteq M,\qquad \text{[unclear in source: the next comparison with \(M\)]},
\qquad\Longrightarrow Y=M.
$$

The intended role of the comparison is the minimality of \(M\): \(Y\) cannot be a proper convex subset still containing \(P\).

**Textbook cross-reference:** §7.2, printed p.212 onward, for intersection and subset notation. The minimal-convex-set argument is course-specific.

<a id="pdf-page-094"></a>
## PDF page 094 — Intersections of convex sets are convex

[Original scan](source_pages/page_094.png)

**Claim.** If \(C_1,C_2\) are convex, then \(C_1\cap C_2\) is convex.

Take \(p_1,p_2\in C_1\cap C_2\). Then both points belong to \(C_1\) and both belong to \(C_2\). Convexity therefore gives

$$
\overline{p_1p_2}\subseteq C_1
\quad\text{and}\quad
\overline{p_1p_2}\subseteq C_2.
$$

Thus

$$
\overline{p_1p_2}\subseteq C_1\cap C_2,
$$

as required.

**Textbook cross-reference:** §7.2, printed p.212 onward, for intersections. The geometric argument is not in the supplied textbook.

<a id="pdf-page-095"></a>
## PDF page 095 — Convex hull and all convex combinations

[Original scan](source_pages/page_095.png)

Let \(Z\) be the set of all convex combinations of points of \(P\), and let \(M\) be the minimal convex set containing \(P\).

The goal is

$$
M=Z.
$$

The page states that \(Z\) is a convex set containing \(P\), and records

$$
Z\cap M=M\implies M\subseteq Z.
$$

It also writes the other required inclusion,

$$
Z\subseteq M.
$$

The justification is continued in subsequent pages.

**Textbook cross-reference:** §7.2, printed p.212 onward, for equality proved by two inclusions. The convex-hull result is course-specific.

<a id="pdf-page-096"></a>
## PDF page 096 — Three equivalent convex-hull descriptions

[Original scan](source_pages/page_096.png)

The notes collect the descriptions:

- \(M\): the **unique** minimal convex set containing \(P\).
- The intersection of all convex sets containing \(P\).
- \(X\): the set of all convex combinations of points of \(P\).

Both inclusions are checked:

$$
M\subseteq X,\qquad X\subseteq M.
$$

Beside the second inclusion, the page recalls the earlier lemma: if \(S\) is convex and \(P=\{p_1,\ldots,p_k\}\subseteq S\), the convex combinations of these points belong to \(S\).

**Textbook cross-reference:** §7.2, printed p.212 onward, for the two-inclusion method and set operations; no matching convex-hull treatment.

<a id="pdf-page-097"></a>
## PDF page 097 — A point inside a finite-point convex hull

[Original scan](source_pages/page_097.png)

The notation is \(P\subseteq\mathbb R^d\) and \(x\in\operatorname{Conv}(P)\).

**Diagram.** Several points lie on the boundary of a six-sided polygon, and several more lie inside it. An interior point is highlighted in red and joined by dotted segments toward other points of the configuration, illustrating a point expressed using a smaller selection of points.

No equation or proof is supplied on this page.

**Textbook cross-reference:** No matching convex-hull treatment was found in the supplied textbook.

<a id="pdf-page-098"></a>
## PDF page 098 — Unfinished convex-combination statement

[Original scan](source_pages/page_098.png)

The source contains the unfinished sentence:

> Given \(k\) points \(p_1,\ldots,p_k\) in a convex set \(S\), every …

The rest of the sentence is absent. It is retained as an unfinished fragment rather than replaced with a reconstructed assertion.

**Textbook cross-reference:** No matching convex-combination treatment was found in the supplied textbook.

<a id="pdf-page-099"></a>
## PDF page 099 — Reducing the number of nonzero coefficients

[Original scan](source_pages/page_099.png)

**Lemma as written.** Given \(S=\{q_1,\ldots,q_N\}\subseteq\mathbb R^d\), for every \(x\in\operatorname{Conv}(S)\) there exist nonnegative real coefficients \(w_1,\ldots,w_N\) such that

$$
x=\sum_{n=1}^{N}w_nq_n
$$

and at most \(d\) coefficients are nonzero.

**Distinction in the source statement:** This representation does not state that the new coefficients sum to \(1\). It is a nonnegative linear-combination reduction; it is not yet the normalized \(d+1\)-point convex-combination theorem.

The proof focuses on \(N=d+1\), fixes \(N\), and uses an induction hypothesis for the dimension. For the step, it writes

$$
x=\sum_{n=1}^{k+1}r_nq_n,\qquad
\sum_n r_n=1,\qquad r_n\ge0.
$$

If a coefficient is zero, the reduction is already achieved, so the remaining argument assumes none is zero.

**Textbook cross-reference:** Ch.5, printed pp.115–129, for induction. The coefficient-reduction lemma is course-specific.

<a id="pdf-page-100"></a>
## PDF page 100 — The linearly dependent case

[Original scan](source_pages/page_100.png)

The first case assumes \(q_1,\ldots,q_k\in\mathbb R^k\) are linearly dependent, so

$$
\dim\operatorname{span}\{q_1,\ldots,q_k\}<k.
$$

The source says to use the induction hypothesis in the lower-dimensional space, written as \(\mathbb R^{k-1}\). It records the normalized representation

$$
\sum_{n=1}^{k}
\frac{w_n}{\sum_{j=1}^{k}w_j}q_n
=\sum_{i=1}^{k-1}\alpha_iq_i.
$$

Rescaling gives

$$
x=\sum_{n=1}^{k}w_nq_n
=
\left(\sum_{j=1}^{k}w_j\right)
\left(\sum_{i=1}^{k-1}\alpha_iq_i\right).
$$

This page uses \(x\) for the subtotal involving the first \(k\) vectors. The full combination also includes \(q_{k+1}\), as restored explicitly on page 105.

**Source convention:** The lower-dimensional span is being represented in coordinates; it need not literally equal the displayed coordinate subspace.

**Textbook cross-reference:** Ch.5, printed pp.115–129, for the induction method; no matching geometric coefficient-reduction theorem.

<a id="pdf-page-101"></a>
## PDF page 101 — The linearly independent case and coefficient adjustment

[Original scan](source_pages/page_101.png)

If \(\{q_1,\ldots,q_k\}\) is linearly independent, it spans \(\mathbb R^k\). Therefore

$$
q_{k+1}=\sum_{n=1}^{k}u_nq_n
$$

for some real \(u_1,\ldots,u_k\).

For any real \(\theta\),

$$
\begin{aligned}
q_{k+1}
&=(1-\theta)q_{k+1}+\theta q_{k+1}\\
&=(1-\theta)q_{k+1}
+\theta\sum_{n=1}^{k}u_nq_n.
\end{aligned}
$$

Substituting this into \(x\) gives

$$
\begin{aligned}
x
&=\sum_{n=1}^{k}w_nq_n
+w_{k+1}(1-\theta)q_{k+1}
+w_{k+1}\theta\sum_{n=1}^{k}u_nq_n\\
&=\sum_{n=1}^{k}
(w_n+\theta w_{k+1}u_n)q_n
+(1-\theta)w_{k+1}q_{k+1}.
\end{aligned}
$$

The adjusted coefficients are underlined in the source. Their choice is developed later.

**Textbook cross-reference:** No matching coefficient-adjustment/convex-geometry treatment was found in the supplied textbook.

<a id="pdf-page-102"></a>
## PDF page 102 — The reduction lemma and one-dimensional basis case

[Original scan](source_pages/page_102.png)

The boxed claim specializes to

$$
S=\{q_1,\ldots,q_{d+1}\}\subseteq\mathbb R^d,\qquad
x\in\operatorname{Conv}(S).
$$

There exist \(w_i\ge0\) with

$$
x=\sum_{i=1}^{d+1}w_iq_i
$$

such that at most \(d\) coefficients are positive: at least one is zero.

**Basis step, \(d=1\).** The page draws \(q_1,x,q_2\) on the real line, with \(x\) between the other two, and writes

$$
x=w_1q_1+w_2q_2,
$$

crossing out the \(w_2q_2\) term to illustrate eliminating a coefficient. No value of the replacement coefficient is computed.

As on page 099, the reduced nonnegative coefficients need not sum to \(1\).

**Textbook cross-reference:** Ch.5, printed pp.115–129, for induction and basis cases; no matching geometry theorem.

<a id="pdf-page-103"></a>
## PDF page 103 — Dimension-induction setup

[Original scan](source_pages/page_103.png)

Assume the statement for \(k\) points in \(\mathbb R^{k-1}\), and prove it for \(k+1\) points in \(\mathbb R^k\).

For

$$
S=\{q_1,\ldots,q_{k+1}\},\qquad x\in\operatorname{Conv}(S),
$$

there are coefficients \(u_i\ge0\) such that

$$
x=\sum_{i=1}^{k+1}u_iq_i,\qquad
\sum_i u_i=1.
$$

Suppose none of the \(u_i\) is zero; otherwise a term has already been eliminated. The page then singles out the first \(k\) vectors \(\{q_1,\ldots,q_k\}\).

**Textbook cross-reference:** Ch.5, printed pp.115–129, for the induction framework; the geometric result is course-specific.

<a id="pdf-page-104"></a>
## PDF page 104 — Rescaling a lower-dimensional representation

[Original scan](source_pages/page_104.png)

**Case 1:** \(\{q_1,\ldots,q_k\}\) is linearly dependent. This page writes its span dimension as \(k-1\); the earlier page states the more general inequality \(<k\).

Define

$$
y=\sum_{i=1}^{k}
\frac{u_i}{\sum_{j=1}^{k}u_j}q_i.
$$

Using the induction hypothesis, the page rewrites this as

$$
y=\sum_{i=1}^{k-1}r_iq_i,\qquad r_i\ge0,
$$

and notes that one coefficient is zero, relabelled as \(r_k=0\).

Let

$$
\overline u=\sum_{j=1}^{k}u_j.
$$

Then

$$
\sum_{i=1}^{k}u_iq_i
=\overline u\sum_{i=1}^{k-1}r_iq_i.
$$

**Textbook cross-reference:** Ch.5, printed pp.115–129, for induction; no matching geometry theorem.

<a id="pdf-page-105"></a>
## PDF page 105 — Completing the dependent-case substitution

[Original scan](source_pages/page_105.png)

The original combination is

$$
x=\sum_{i=1}^{k}u_iq_i+u_{k+1}q_{k+1}.
$$

Substituting page 104's reduced subtotal gives

$$
x=\sum_{i=1}^{k-1}\overline u\,r_iq_i
+u_{k+1}q_{k+1}.
$$

The resulting coefficient list is

$$
\{\overline u\,r_1,\overline u\,r_2,\ldots,
\overline u\,r_{k-1},u_{k+1}\}.
$$

Thus one of the original \(k+1\) terms has been removed.

**Textbook cross-reference:** Ch.5, printed pp.115–129, for the induction argument; no matching geometry theorem.

<a id="pdf-page-106"></a>
## PDF page 106 — A convex-combination exercise

[Original scan](source_pages/page_106.png)

Let \(S\subseteq\mathbb R^d\) be convex and

$$
X=\{p_1,\ldots,p_k\}\subseteq S.
$$

**Exercise:** Show that every convex combination of points of \(X\) belongs to \(S\).

This repeats the earlier convex-combination lemma as a question. No proof is written on this page.

**Textbook cross-reference:** No matching convex-geometry section was found in the supplied textbook.

<a id="pdf-page-107"></a>
## PDF page 107 — Reduction lemma and Carathéodory's theorem

[Original scan](source_pages/page_107.png)

The boxed **lemma** states: for

$$
S=\{q_1,\ldots,q_N\}\subseteq\mathbb R^d,\qquad
x\in\operatorname{Conv}(S),
$$

there exist nonnegative coefficients \(w_1,\ldots,w_N\) such that

$$
x=\sum_{i=1}^{N}w_iq_i,
$$

and at most \(d\) coefficients are nonzero. This lemma does not require normalization of the new coefficients.

The following **theorem** states: \(x\) is a **convex combination of at most \(d+1\) points of \(S\)**. This is the normalized statement commonly called Carathéodory's theorem.

**Textbook cross-reference:** No matching Carathéodory/convex-hull section was found in the supplied textbook.

<a id="pdf-page-108"></a>
## PDF page 108 — Lifting to one higher dimension

[Original scan](source_pages/page_108.png)

Identify \(\mathbb R^d\) with the following subset of \(\mathbb R^{d+1}\):

$$
\{p\in\mathbb R^{d+1}\mid p_{d+1}=1\}.
$$

Under this embedding,

$$
S\longmapsto
\overline S=\{(q_i,1)\mid q_i\in S\}
\subseteq\mathbb R^{d+1}.
$$

If \(x\in\operatorname{Conv}(S)\), then
\((x,1)\in\operatorname{Conv}(\overline S)\). Apply the reduction lemma in dimension \(d+1\): there are \(w_i\ge0\) such that

$$
(x,1)=\sum_{i=1}^{N}w_i(q_i,1),
$$

with at most \(d+1\) nonzero coefficients. Comparing coordinates gives

$$
x=\sum_i w_iq_i,\qquad
\sum_i w_i=1.
$$

Thus the representation is a convex combination using at most \(d+1\) original points.

**Textbook cross-reference:** No matching convex-geometry/lifting theorem was found in the supplied textbook.

<a id="pdf-page-109"></a>
## PDF page 109 — Graham scan in the plane

[Original scan](source_pages/page_109.png)

For a planar point set in \(\mathbb R^2\), the notes introduce **Graham scan** with these steps:

1. Find the point with the lowest \(y\)-coordinate; call it \(p\).
2. Sort all points by their angle with the \(x\)-axis.
3. Consider points from the sorted list in order.

The diagram marks consecutive positions \(i-1\), \(i\), and a next candidate. The page does not explicitly state the reference origin for the polar-angle sorting or give the complete turn-test rule.

**Textbook cross-reference:** No matching Graham-scan/computational-geometry section was found in the supplied textbook.

<a id="pdf-page-110"></a>
## PDF page 110 — Graham-scan point removals and turns

[Original scan](source_pages/page_110.png)

The page illustrates modifying candidate lists:

- A list containing \(p,A,B,C,D\), with \(C\) crossed out.
- A later list containing \(p,A,B,C,D',p\), with \(B\) and \(C\) crossed out.

The point diagram places \(p\) at the bottom, \(A\) and \(B\) on the right, \(C\) and \(D\) farther left, and \(D'\) above. Dotted candidate connections show why intermediate points may be removed while forming the hull.

A separate diagram compares the directions \(A\to B\) and \(A\to C\), illustrating the turn between consecutive candidate edges. The exact deletion test is not written on the page.

**Textbook cross-reference:** No matching Graham-scan section was found in the supplied textbook.

<a id="pdf-page-111"></a>
## PDF page 111 — Gift-wrapping algorithm

[Original scan](source_pages/page_111.png)

The underlined heading is **“Gift wrapping algo.”**

Beneath it are several unlabelled points and a faint broken vertical line. No algorithmic steps, equations, or complexity bound are written on this page.

**Textbook cross-reference:** No matching gift-wrapping/convex-hull algorithm section was found in the supplied textbook.

<a id="pdf-page-112"></a>
## PDF page 112 — Minkowski sum

[Original scan](source_pages/page_112.png)

For \(A,B\subseteq\mathbb R^n\), the page defines

$$
A\oplus B=\{a+b\mid a\in A,\ b\in B\}.
$$

**Diagrams.** \(A\) is drawn as a horizontal segment and \(B\) as a vertical segment. A coordinate sketch shows these directions, and a shaded rectangle illustrates their Minkowski sum.

**Textbook cross-reference:** No matching Minkowski-sum section was found in the supplied textbook.

<a id="pdf-page-113"></a>
## PDF page 113 — Minkowski-sum example to consider

[Original scan](source_pages/page_113.png)

The page draws \(A\) as a circular region with radius marked \(r\), and \(B\) as a horizontal segment marked \(0.5\). It then writes

$$
A\oplus B
$$

without drawing the resulting set or supplying a calculation.

**Textbook cross-reference:** No matching Minkowski-sum section was found in the supplied textbook.

<a id="pdf-page-114"></a>
## PDF page 114 — Rigid motions and a set-sum diagram

[Original scan](source_pages/page_114.png)

A rigid motion in \(\mathbb R^n\) is denoted by \((A,b)\), with arrows identifying \(A\) as the rotation part and \(b\) as the translation part. Its displayed map is

$$
x\longmapsto Ax+b.
$$

The page also draws a small filled circular set labelled \(A\), a larger circular boundary labelled \(B\), and an annular shaded set beside \(A\oplus B\).

**Notation warning:** The set \(A\) in the Minkowski-sum drawing and the matrix \(A\) in the rigid-motion formula use the same letter for different objects.

**Textbook cross-reference:** No matching rigid-motion/Minkowski-sum section was found in the supplied textbook.

<a id="pdf-page-115"></a>
## PDF page 115 — Rigid motions preserve distance

[Original scan](source_pages/page_115.png)

The page repeats the rigid-motion notation \((A,b)\) and map

$$
f(x)=Ax+b.
$$

Its defining distance property is

$$
\|x_1-x_2\|
=\|f(x_1)-f(x_2)\|,
\qquad
\forall x_1,x_2\in\mathbb R^n.
$$

No derivation or matrix condition is written on this page.

**Textbook cross-reference:** No matching rigid-motion section was found in the supplied textbook.

<a id="pdf-page-116"></a>
## PDF page 116 — Rotation about a specified point

[Original scan](source_pages/page_116.png)

In \(\mathbb R^2\), a rigid motion \((A,b)\) acts by

$$
x\longmapsto A(x)+b.
$$

To rotate about a point \(x_0\), the displayed map is

$$
x\longmapsto A(x-x_0)+x_0,
$$

where

$$
A=\begin{pmatrix}
\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta
\end{pmatrix}.
$$

**Diagram.** Coordinate axes and a point \(x_0\) away from the origin accompany the formula. The point is the centre about which the rotation is performed.

**Textbook cross-reference:** No matching rigid-motion or planar-rotation section was found in the supplied textbook.

<a id="pdf-page-117"></a>
## PDF page 117 — Fixed point of a nonidentity planar rotation

[Original scan](source_pages/page_117.png)

The proof separates two cases for \(f(x)=Ax+b\):

- If \(A=I\), then \((A,b)\) is a **pure translation**.
- If \(A\ne I\), with \(A\) the planar rotation matrix, seek a fixed point \(x_0\).

The fixed-point equation gives

$$
Ax_0+b=x_0,
\qquad
(A-I)x_0=-b.
$$

The notes state that \(A-I\) is invertible for a nonzero rotation angle and therefore write

$$
x_0=-(A-I)^{-1}b.
$$

The rotation matrix is again

$$
A=\begin{pmatrix}
\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta
\end{pmatrix}.
$$

**Source qualification:** The page writes the angle condition as \(\theta\ne0\). Since rotation angles are periodic, this means a nonidentity rotation: \(\theta\not\equiv0\pmod{2\pi}\). The argument concerns the displayed rotation matrix; it does not discuss reflections.

**Textbook cross-reference:** No matching classification of planar rigid motions was found in the supplied textbook.

<a id="pdf-page-118"></a>
## PDF page 118 — Expressing the rigid motion as rotation about its fixed point

[Original scan](source_pages/page_118.png)

Continuing with the fixed point from [PDF page 117](#pdf-page-117), the page is headed **“Rotate about \(x_0\).”** It calculates

$$
\begin{aligned}
x&\longmapsto A(x-x_0)+x_0\\
&=Ax-Ax_0+Ax_0+b\\
&=Ax+b.
\end{aligned}
$$

The cancellation uses \(x_0=Ax_0+b\). Thus the rigid motion \((A,b)\) has the rotation-about-\(x_0\) form above.

**Textbook cross-reference:** No matching rigid-motion section was found in the supplied textbook.

<a id="pdf-page-119"></a>
## PDF page 119 — Parametric description of a plane curve

[Original scan](source_pages/page_119.png)

The page represents a plane curve by

$$
c(t)=(x(t),y(t)),
\qquad t\in[0,1].
$$

**Diagrams.** A closed oval has a marked point on its boundary. A separate green, curved path has short tick marks at successive positions. Another sketch shows two coordinate graphs; \(x(t)\) is written above the path, and the lower horizontal axis is labelled \(x\). These drawings accompany the idea of describing a curve through its coordinate functions. A small handwritten annotation immediately after the coordinate pair is [unclear in source].

**Textbook cross-reference:** No matching treatment of parametric curves was found in the supplied textbook.

<a id="pdf-page-120"></a>
## PDF page 120 — Circle parametrization and a curve in three dimensions

[Original scan](source_pages/page_120.png)

For a circle, the page gives

$$
c(t)=(\cos t,\sin t),
\qquad t\in[0,2\pi].
$$

A circle sketch appears beside this formula.

For a space curve, the coordinate representation is

$$
c(t)=(x(t),y(t),z(t)),
\qquad t\in[a,b).
$$

The source draws an open winding curve beside the second formula. Its parameter interval is written with a square opening bracket and a rounded closing bracket.

**Textbook cross-reference:** No matching parametrized-circle or space-curve section was found in the supplied textbook.

<a id="pdf-page-121"></a>
## PDF page 121 — Monomials for polynomial curves

[Original scan](source_pages/page_121.png)

The page writes the family

$$
\{1,t,t^2,t^3,\ldots,t^n\}.
$$

Below it is an unlabelled smooth curve with one crest and one trough. No coefficient formula or additional claim is written on this page.

**Textbook cross-reference:** No matching polynomial-curve construction section was found in the supplied textbook.

<a id="pdf-page-122"></a>
## PDF page 122 — Bézier curves: coordinate representation

[Original scan](source_pages/page_122.png)

The heading is **“Bezier curves.”** The curve is represented by

$$
c(t)=(x(t),y(t)).
$$

**Diagram.** Coordinate axes are drawn with a diagonal vector starting at the origin and pointing into the first quadrant, illustrating a position vector for a point on the curve. No control-point or blending-function formula is given until the next page.

**Textbook cross-reference:** No matching Bézier-curve section was found in the supplied textbook.

<a id="pdf-page-123"></a>
## PDF page 123 — Bézier curve as a weighted sum of control points

[Original scan](source_pages/page_123.png)

The emphasized formula is

$$
c(t)=\sum_{i=0}^{n}P_i\,\theta_{i,n}(t),
\qquad P_i\in\mathbb R^2.
$$

The scalar functions \(\theta_{i,n}(t)\) are indexed by

$$
i=0,1,2,\ldots,n.
$$

The points are written in coordinate-column form:

$$
P_0=\begin{pmatrix}P_{0,x}\\P_{0,y}\end{pmatrix},\quad
P_1=\begin{pmatrix}P_{1,x}\\P_{1,y}\end{pmatrix},\quad
P_2=\begin{pmatrix}P_{2,x}\\P_{2,y}\end{pmatrix},\quad\ldots,\quad
P_n=\begin{pmatrix}P_{n,x}\\P_{n,y}\end{pmatrix}.
$$

The handwritten symbol for the blending functions is rendered as \(\theta\). No explicit formula for these functions is given on this page.

**Textbook cross-reference:** No matching Bézier-curve or control-point section was found in the supplied textbook.

<a id="pdf-page-124"></a>
## PDF page 124 — Polynomial coefficients and change of basis

[Original scan](source_pages/page_124.png)

The page repeats the monomial family

$$
\{1,t,t^2,\ldots,t^n\}
$$

and writes a polynomial curve in the form

$$
c(t)=a_0\cdot1+a_1t+a_2t^2+\cdots+a_nt^n.
$$

It then compares two coordinate descriptions in \(\mathbb R^{n+1}\): one using \(\{v_0,v_1,\ldots,v_n\}\), with coefficient vector \(\alpha\), and one using the standard coordinate directions \(\{i,j,k,\ldots\}\), with coefficient vector \(\beta\). The displayed conversion is

$$
\alpha=M\beta.
$$

The matrix \(M\) is circled, but its entries and the exact convention for the two bases are not supplied.

**Textbook cross-reference:** No matching linear-algebra change-of-basis section was found in the supplied textbook.

<a id="pdf-page-125"></a>
## PDF page 125 — Binomial theorem and tangent vectors to a curve

[Original scan](source_pages/page_125.png)

The binomial expansion is written as

$$
(a+b)^n=\sum_{i=0}^{n}\binom ni a^i b^{n-i}.
$$

The curve notation is repeated:

$$
c(t)=(x(t),y(t)),\qquad t\in I.
$$

The derivative notation \(c'(t)\) appears below it.

**Diagram.** A winding curve has several arrows drawn tangent to it: one points up and right near the first crest, one rightward along a nearly horizontal portion, and one upward along a steep portion. The drawing illustrates tangent directions at different parameter values; no coordinate formula for the derivative is written on this page.

**Textbook cross-reference:** §14.6.3, **“The Binomial Theorem,”** Theorem 14.6.4, printed p.566 (textbook PDF p.574), gives the same expansion with the exponents indexed in the opposite order. The supplied textbook does not cover tangent vectors to parametric curves.

<a id="pdf-page-126"></a>
## PDF page 126 — Logic and the definition of a proposition

[Original scan](source_pages/page_126.png)

The headings are **“Logic”** and **“Propositional logic.”**

A **proposition** is a statement which may be assigned a truth value of **true** or **false**, but not both.

The arithmetic examples at the bottom are

$$
1+1=2,\qquad 1+1=3.
$$

At the lower right is an incomplete algebraic fragment beginning \(x^3-x^2\); its remaining marks are [unclear in source]. It is not written as a complete sentence or equation.

**Textbook cross-reference:** §1.1, **“Propositions,”** printed p.5 (textbook PDF p.13), defines propositions and gives true and false arithmetic examples. §3.1, printed p.42 (PDF p.50), introduces propositional/Boolean variables.

<a id="pdf-page-127"></a>
## PDF page 127 — Propositions, self-reference, and propositional variables

[Original scan](source_pages/page_127.png)

The page lists these examples:

- **“This statement is false.”** A large cross is drawn beside it.
- \(1+1=2\), marked as a proposition and assigned a propositional label \(P\).
- **“Today is Monday,”** assigned label \(P\).
- **“All Mondays are pleasant,”** assigned label \(Q\).

The underlined final heading is **“Propositional variables.”** The letter \(P\) is reused for two separate examples.

**Textbook clarification:** The definition in §1.1, printed p.5 (textbook PDF p.13), requires a statement to be either true or false and excludes statements whose truth varies with circumstance. Thus “Today is Monday” requires a specified day/context to have a fixed truth value. The cross beside the self-referential first sentence records that it does not receive a consistent classical truth value. §3.1, printed p.42 (PDF p.50), explains using \(P,Q\) as variables for propositions.

<a id="pdf-page-128"></a>
## PDF page 128 — Negation

[Original scan](source_pages/page_128.png)

Under **“Connectives,”** the page takes a proposition \(p\) and forms its negation \(\neg p\).

The source uses \(0\) for false and \(1\) for true:

| \(p\) | \(\neg p\) |
|---|---|
| 0 | 1 |
| 1 | 0 |

**Textbook cross-reference:** §3.1.1, **“NOT, AND, and OR,”** printed p.42 (textbook PDF p.50), gives the negation truth table with \(T,F\) in place of \(1,0\).

<a id="pdf-page-129"></a>
## PDF page 129 — Conjunction, disjunction, and exclusive OR

[Original scan](source_pages/page_129.png)

The page names **conjunction** \(p\land q\) and **disjunction** \(p\lor q\), and adds a truth-table column for exclusive OR \(p\oplus q\):

| \(p\) | \(q\) | \(p\land q\) | \(p\lor q\) | \(p\oplus q\) |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 1 |
| 1 | 1 | 1 | 1 | 0 |

**Textbook cross-reference:** §3.1.1, printed pp.42–43 (textbook PDF pp.50–51), gives AND, inclusive OR, and XOR with the same truth values.

<a id="pdf-page-130"></a>
## PDF page 130 — Implication and its contrapositive

[Original scan](source_pages/page_130.png)

The heading **“Conditional statements”** lists

$$
p\Rightarrow q,\qquad p\Leftrightarrow q.
$$

The truth table on this page concerns implication and its contrapositive:

| \(p\) | \(q\) | \(p\Rightarrow q\) | \(\neg q\Rightarrow\neg p\) |
|---|---|---|---|
| 0 | 0 | 1 | 1 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 1 | 1 | 1 |

The two final columns agree in every row.

**Textbook cross-reference:** §3.1.2, **“IMPLIES,”** printed pp.43–45 (textbook PDF pp.51–53), defines implication. §3.3.1, **“Implications and Contrapositives,”** printed pp.48–49 (PDF pp.56–57), gives the same comparison and identifies the equivalent contrapositive. The listed biconditional is defined in §3.1.3, printed p.45 (PDF p.53).

<a id="pdf-page-131"></a>
## PDF page 131 — A conditional-language example and biconditional truth table

[Original scan](source_pages/page_131.png)

The source illustrates \(p\Rightarrow q\) with the Hindi statement

> जल है तो कल है।

This says, “If there is water, there is a tomorrow/future.” The water clause is labelled \(p\), and the future clause \(q\).

It separately writes \(\neg p\Rightarrow\neg q\) beside

> जल नहीं तो कल नहीं।

This says, “If there is no water, there is no tomorrow/future.”

The lower part gives the biconditional table:

| \(p\) | \(q\) | \(p\Leftrightarrow q\) |
|---|---|---|
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

**Textbook clarification:** The second conditional is the **inverse** of the first; the contrapositive studied on [PDF page 130](#pdf-page-130) is \(\neg q\Rightarrow\neg p\). They should not be substituted for one another. See §3.3.1, printed pp.48–49 (textbook PDF pp.56–57), for implication/contrapositive equivalence. §1.4.1, printed p.10 (PDF p.18), explicitly gives an unsound “Non-Rule” that tries to infer \(P\Rightarrow Q\) from \(\neg P\Rightarrow\neg Q\). The biconditional table matches §3.1.3, printed p.45 (PDF p.53).

<a id="pdf-page-132"></a>
## PDF page 132 — Syntax for forming compound propositions

[Original scan](source_pages/page_132.png)

Under **“Syntax”** and **“Sentences,”** the page gives sample formulas

$$
p\Rightarrow q,\qquad (p\land q)\lor r.
$$

The boxed rule says: if \(p,q\) are propositions, then

$$
\neg p,\quad p\lor q,\quad p\land q,\quad p\oplus q,\quad
p\Rightarrow q,\quad p\Leftrightarrow q
$$

are all propositions.

**Textbook cross-reference:** §3.1, printed pp.42–45 (textbook PDF pp.50–53), describes forming propositions with the listed connectives and gives their truth tables.

<a id="pdf-page-133"></a>
## PDF page 133 — A nested compound proposition

[Original scan](source_pages/page_133.png)

The heading is **“Compound propositions.”** The formula, written twice, is

$$
\bigl((\neg p\land q)\lor r\bigr)\Rightarrow s.
$$

Its parentheses first group \(\neg p\land q\), then the disjunction with \(r\), before applying the implication to \(s\). No truth table or simplification is supplied on this page.

**Textbook cross-reference:** §3.1, printed pp.42–45 (textbook PDF pp.50–53), supplies the connective meanings; §3.2.1, **“Truth Table Calculation,”** printed pp.46–47 (PDF pp.54–55), illustrates evaluating compound expressions.

<a id="pdf-page-134"></a>
## PDF page 134 — Premises and conclusion of an argument

[Original scan](source_pages/page_134.png)

An **inference/argument** has two parts:

1. **Premises:** one or more propositions.
2. **Conclusion:** one proposition.

The example is

$$
\begin{array}{ll}
1.&p\Rightarrow q\\
2.&p\\\hline
\text{Conclusion:}&q.
\end{array}
$$

The page also writes the conjunction of the premises,

$$
(p\Rightarrow q)\land p,
$$

beside the conclusion \(q\).

**Textbook cross-reference:** §1.4.1, **“Logical Deductions,”** printed p.10 (textbook PDF p.18), names this inference **modus ponens** and explains the soundness requirement for an inference rule.

<a id="pdf-page-135"></a>
## PDF page 135 — Definition of a valid argument

[Original scan](source_pages/page_135.png)

An argument is **valid** if it is not possible for the conclusion to be false when all the premises are true.

The page expresses this as

$$
\text{premises}\Rightarrow\text{conclusion}
\quad\text{is true}.
$$

Here “premises” means their conjunction, as illustrated on [PDF page 134](#pdf-page-134), and the definition requires the implication to hold for every assignment of truth values.

**Textbook cross-reference:** §1.4.1, printed p.10 (textbook PDF p.18), defines soundness as forbidding true premises with a false conclusion. §3.3.2, **“Validity and Satisfiability,”** printed p.50 (PDF p.58), defines a valid formula as one true for every truth assignment.

<a id="pdf-page-136"></a>
## PDF page 136 — Return to a Minkowski-sum sketch

[Original scan](source_pages/page_136.png)

The page draws:

- A circular set \(A\), with its centre marked and radius \(r=1\).
- A horizontal segment \(B\), with length \(\ell=0.5\).
- The notation \(A\oplus B\), beside a small shaded rounded region.

This returns to the set-sum example from [PDF page 113](#pdf-page-113). No equation for the resulting boundary, placement of the segment endpoints, or explicit statement of whether \(A\) is the circle or the filled disk is written on this page.

**Textbook cross-reference:** No matching Minkowski-sum section was found in the supplied textbook. Here \(\oplus\) denotes a sum of sets, whereas [PDF page 129](#pdf-page-129) uses the same symbol for exclusive OR.

<a id="pdf-page-137"></a>
## PDF page 137 — Expressing argument validity as an implication

[Original scan](source_pages/page_137.png)

The page repeats that an argument has a **list of premises** and a **conclusion**.

One boxed example is

$$
\frac{p\Rightarrow q,\ p}{q}.
$$

It is accompanied by

$$
((p\Rightarrow q)\land p)\vdash q
$$

and the boxed implication

$$
\bigl((p\Rightarrow q)\land p\bigr)\Rightarrow q.
$$

The criterion written below is: **“premises \(\Rightarrow\) conclusion is true.”** Together with [PDF page 135](#pdf-page-135), this means true under every truth assignment.

A second boxed argument at the upper right is

$$
\frac{p\Rightarrow q,\ q}{p}.
$$

**Textbook clarification:** The first rule is modus ponens (§1.4.1, printed p.10; textbook PDF p.18). The second argument is invalid: with \(p=0,q=1\), both its premises are true and its conclusion is false. This follows from the implication table in §3.1.2, printed p.43 (PDF p.51), and the soundness criterion in §1.4.1. The source does not write out this counterexample.

<a id="pdf-page-138"></a>
## PDF page 138 — Seven inference patterns

[Original scan](source_pages/page_138.png)

Seven circled premise/conclusion patterns appear on the page. The names below identify the standard rules represented by the handwritten formulas.

| Pattern | Premise(s) | Conclusion |
|---|---|---|
| Modus tollens | \(p\Rightarrow q,\ \neg q\) | \(\neg p\) |
| Chaining implications | \(p\Rightarrow q,\ q\Rightarrow r\) | \(p\Rightarrow r\) |
| Disjunctive syllogism | \(p\lor q,\ \neg p\) | \(q\) |
| Addition | \(p\) | \(p\lor q\) |
| Simplification | \(p\land q\) | \(p\) |
| De Morgan pattern for AND | \(\neg(p\land q)\) | \(\neg p\lor\neg q\) |
| De Morgan pattern for OR | \(\neg(p\lor q)\) | \(\neg p\land\neg q\) |

**Textbook cross-reference:** §1.4.1, printed p.10 (textbook PDF p.18), presents the chaining rule and the general soundness criterion. §3.1.1–3.1.2, printed pp.42–43 (PDF pp.50–51), provides the connective truth tables for checking the first five patterns. §3.4.2, **“Proving Equivalences,”** printed p.53 (PDF p.61), states De Morgan's laws, equations (3.11)–(3.12), as equivalences and therefore supports both directions of the last two patterns.

<a id="pdf-page-139"></a>
## PDF page 139 — General implication for an argument with many premises

[Original scan](source_pages/page_139.png)

The source displays an argument with premises \(p_1,p_2,\ldots,p_n\) and conclusion \(q\):

$$
\frac{p_1,\ p_2,\ \ldots,\ p_n}{q}.
$$

Its boxed formula is

$$
(p_1\land p_2\land\cdots\land p_n)\Rightarrow q.
$$

Braces label the conjunction on the left as **premises** and \(q\) as the **conclusion**. The phrase “premises \(\Rightarrow\) conclusion” is repeated below.

**Textbook cross-reference:** §1.4.1, printed p.10 (textbook PDF p.18), gives the rule's soundness requirement. §3.3.2, printed p.50 (PDF p.58), gives the always-true criterion for a valid formula. Together these match the validity test using the displayed implication.

<a id="pdf-page-140"></a>
## PDF page 140 — Two argument examples and a short derivation

[Original scan](source_pages/page_140.png)

The argument on the left is written as

$$
\frac{p\land q,\ r,\ s\lor T,\ \neg T,\ u\lor\neg r}{\neg r}.
$$

Here the capital \(T\) is retained as the propositional variable used in the source.

The argument on the right is

$$
\frac{p\Rightarrow q,\ p\land r}{q\land r}.
$$

Under it, the handwritten derivation lists

$$
\begin{array}{l}
p\land r\\
p\\
p\Rightarrow q\\
q\\
r\\\hline
q\land r.
\end{array}
$$

**Textbook clarification:** The right-hand derivation extracts \(p,r\) from \(p\land r\), uses modus ponens to obtain \(q\), and then forms \(q\land r\). See §3.1.1, printed p.42 (textbook PDF p.50), for conjunction and §1.4.1, printed p.10 (PDF p.18), for modus ponens. The left-hand argument is invalid: assign \(p=q=r=s=u=1\) and \(T=0\). All five premises are then true while \(\neg r\) is false. This counterexample uses the connective tables in §3.1.1, printed pp.42–43 (PDF pp.50–51), and the validity criterion in §3.3.2, printed p.50 (PDF p.58); it is added here because the source supplies no verdict or counterexample for the left-hand argument.

<a id="pdf-page-141"></a>
## PDF page 141 — Sound arguments

[Original scan](source_pages/page_141.png)

An argument is said to be **sound** if it is **valid** and its **premises are true**.

The boxed shorthand is

$$
\text{premises}\Rightarrow\text{conclusion}.
$$

The definition adds the truth of the premises to the validity condition from [PDF page 135](#pdf-page-135).

**Textbook cross-reference:** §1.4.1, **“Logical Deductions,”** printed p.10 (textbook PDF p.18), discusses sound inference rules and explains why starting from true axioms and applying sound rules yields true conclusions. §3.3.2, printed p.50 (PDF p.58), defines validity for formulas. The notes' phrase “sound argument” additionally specifies that the actual premises are true.

<a id="pdf-page-142"></a>
## PDF page 142 — A satisfiability example

[Original scan](source_pages/page_142.png)

Under the heading **“Satisfiability,”** the page boxes the formula

$$
\bigl((p\land q)\lor\neg r\bigr)\Rightarrow q.
$$

There is a small annotation beneath the box [unclear in source]. No truth assignment, truth table, or verdict is written on the page.

**Textbook clarification:** §3.3.2, **“Validity and Satisfiability,”** printed p.50 (textbook PDF p.58), defines a satisfiable formula as one true for at least one truth assignment. The displayed formula is satisfiable: any assignment with \(q=1\) makes the implication true. It is not valid: with \(p=q=r=0\), the antecedent is true and the consequent false. These evaluations use §3.1.1–3.1.2, printed pp.42–43 (PDF pp.50–51); the assignments are added clarification rather than handwritten solutions.

<a id="pdf-page-143"></a>
## PDF page 143 — Further inference patterns involving implications and equivalence

[Original scan](source_pages/page_143.png)

The page gives eight premise/conclusion patterns:

| No. | Premise(s) | Conclusion |
|---|---|---|
| 1 | \(p\lor q,\ \neg p\lor r\) | \(q\lor r\) |
| 2 | \(p\Rightarrow q,\ q\Rightarrow p\) | \(p\Leftrightarrow q\) |
| 3 | \(p\Leftrightarrow q,\ q\) | \(p\) |
| 4 | \(p\Leftrightarrow q,\ \neg q\) | \(\neg p\) |
| 5 | \(p\Leftrightarrow q,\ p\lor q\) | \(p\land q\) |
| 6 | \(p\Leftrightarrow q,\ \neg p\lor\neg q\) | \(\neg p\land\neg q\) |
| 7 | \(p\Rightarrow q\) | \(p\Rightarrow(p\land q)\) |
| 8 | \(p\Rightarrow q,\ r\Rightarrow q,\ p\lor r\) | \(q\) |

At the bottom it repeats the general argument formula, using \(c\) for the conclusion:

$$
(p_1\land p_2\land\cdots\land p_n)\Rightarrow c.
$$

**Textbook cross-reference:** §3.1.1–3.1.3, printed pp.42–45 (textbook PDF pp.50–53), provides the truth tables needed to check these patterns. §3.3.1, printed p.49 (PDF p.57), explicitly identifies the conjunction of the two opposite implications with the biconditional, matching pattern 2. §1.4.1, printed p.10 (PDF p.18), gives the general criterion for sound inference rules; the source supplies no individual proofs on this page.

<a id="pdf-page-144"></a>
## PDF page 144 — Detailed derivation of a conjunction conclusion

[Original scan](source_pages/page_144.png)

The circled claim is

$$
p\Rightarrow q,\quad p\land r\ \vdash\ q\land r.
$$

The proof is written in six steps:

| Step | Formula | Reason in the notes |
|---|---|---|
| 1 | \(p\land r\) | Premise |
| 2 | \(r\) | \(p\land r\vdash r\) |
| 3 | \(p\) | \(p\land r\vdash p\) |
| 4 | \(p\Rightarrow q\) | Premise |
| 5 | \(q\) | From steps 3 and 4 |
| 6 | \(q\land r\) | From steps 2 and 5 |

**Textbook cross-reference:** §1.4.1, printed p.10 (textbook PDF p.18), gives modus ponens, used at step 5, and requires each deduction to identify the earlier facts used. §3.1.1, printed p.42 (PDF p.50), gives the conjunction truth table supporting extraction in steps 2–3 and conjunction formation in step 6.

<a id="pdf-page-145"></a>
## PDF page 145 — Derivation using contraposition and implication chaining

[Original scan](source_pages/page_145.png)

**Premises:**

$$
p\Rightarrow q,\qquad
\neg p\Rightarrow r,\qquad
r\Rightarrow s.
$$

**Conclusion:** \(\neg q\Rightarrow s\).

The source proof proceeds as follows:

| Step | Formula | Justification |
|---|---|---|
| 1 | \(p\Rightarrow q\) | Premise |
| 2 | \(\neg q\Rightarrow\neg p\) | Contrapositive of step 1; written as \(p\Rightarrow q\vdash\neg q\Rightarrow\neg p\) |
| 3 | \(\neg p\Rightarrow r\) | Premise |
| 4 | \(\neg q\Rightarrow r\) | From steps 2 and 3 |
| 5 | \(r\Rightarrow s\) | Premise |
| 6 | \(\neg q\Rightarrow s\) | Chain steps 4 and 5 |

**Source qualification:** The final handwritten step reference after “from 4 &” resembles a circled 1 [unclear in source]. Step 5 is the premise needed for the displayed conclusion; the table makes this dependency explicit.

**Textbook clarification:** The final justification is restored using the chaining rule in §1.4.1, printed p.10 (textbook PDF p.18). Contraposition is justified by §3.3.1, printed pp.48–49 (PDF pp.56–57). These establish the complete six-step argument even where the final source reference is unclear.

<a id="pdf-page-146"></a>
## PDF page 146 — An argument to derive t

[Original scan](source_pages/page_146.png)

**Premises:**

$$
\neg p\land q,\qquad
r\Rightarrow p,\qquad
\neg r\Rightarrow s,\qquad
s\Rightarrow t.
$$

**Conclusion:** \(t\).

The source states the argument without writing proof steps.

**Textbook clarification:** A derivation is: extract \(\neg p\) from \(\neg p\land q\); use \(r\Rightarrow p\) and \(\neg p\) to infer \(\neg r\); then use \(\neg r\Rightarrow s\) to obtain \(s\), and \(s\Rightarrow t\) to obtain \(t\). The conjunction step follows §3.1.1, printed p.42 (textbook PDF p.50); contraposition follows §3.3.1, printed pp.48–49 (PDF pp.56–57); the two final steps use modus ponens in §1.4.1, printed p.10 (PDF p.18). These proof steps are added clarification.

<a id="pdf-page-147"></a>
## PDF page 147 — Predicates and substitution examples

[Original scan](source_pages/page_147.png)

Under **“Predicate logic,”** the notes say that **predicates are propositions with variables**.

The one-variable example is

$$
P(x):\quad x=1.
$$

The page states

$$
P(0)\text{ is false},\qquad P(1)\text{ is true}.
$$

The two-variable example is

$$
Q(x,y):\quad x=y+1.
$$

Its evaluations are

$$
Q(1,0)\text{ is true}\quad(\checkmark),\qquad
Q(1,1)\text{ is false}\quad(\times).
$$

**Textbook cross-reference:** §1.2, **“Predicates,”** printed p.8 (textbook PDF p.16), defines a predicate as a proposition whose truth depends on variables and illustrates substitution. Chapter 3 §3.6, printed p.56 onward (PDF p.64 onward), develops formulas with predicates and quantifiers.

<a id="pdf-page-148"></a>
## PDF page 148 — Universal and existential quantifiers

[Original scan](source_pages/page_148.png)

The page defines the readings

$$
\forall x\,P(x):\quad P(x)\text{ holds for all values of }x,
$$

and

$$
\exists x\,P(x):\quad P(x)\text{ holds for at least one value of }x.
$$

The first boxed example is

$$
\forall x\in\mathbb Z,\quad x+1>x,
$$

with a check mark.

The second boxed example is

$$
\exists x\in\mathbb R,\quad x^2>x.
$$

Overlapping cross and check marks appear beside this example, so the final handwritten verdict is not unambiguous.

**Textbook clarification:** §3.6.1, **“Quantifiers,”** printed pp.56–58 (textbook PDF pp.64–66), gives the universal and existential meanings. The first example is true; the second is also true, since the witness \(x=2\) gives \(4>2\). The witness is added here to resolve the ambiguous marks in the source. §3.6.4, printed p.59 (PDF p.67), explains the domain of discourse, which must be fixed when interpreting quantifiers.

<a id="pdf-page-149"></a>
## PDF page 149 — Negating quantifiers

[Original scan](source_pages/page_149.png)

The page states the two equivalences

$$
\neg\bigl(\exists x\,P(x)\bigr)
\equiv
\forall x\,\neg P(x),
$$

and

$$
\neg\bigl(\forall x\,P(x)\bigr)
\equiv
\exists x\,\neg P(x).
$$

**Diagram.** A rounded rectangle labelled \(X\) contains several small marks representing elements of the domain. No individual element or predicate subset is labelled.

**Textbook cross-reference:** §3.6.5, **“Negating Quantifiers,”** printed pp.59–60 (textbook PDF pp.67–68), gives these exact equivalences as equations (3.19)–(3.20): moving negation across a quantifier switches universal and existential quantification.

<a id="pdf-page-150"></a>
## PDF page 150 — A predicate-logic argument using one existential witness

[Original scan](source_pages/page_150.png)

**Premises:**

$$
\exists x\,\bigl(C(x)\land\neg B(x)\bigr),\qquad
\forall x\,\bigl(C(x)\Rightarrow P(x)\bigr).
$$

**Conclusion:**

$$
\exists x\,\bigl(P(x)\land\neg B(x)\bigr).
$$

The handwritten proof has nine steps:

| Step | Formula | Reason in the notes |
|---|---|---|
| 1 | \(\exists x(C(x)\land\neg B(x))\) | Premise |
| 2 | \(C(a)\land\neg B(a)\) | “\(x=a\) in 1” |
| 3 | \(C(a)\) | From step 2 |
| 4 | \(\forall x(C(x)\Rightarrow P(x))\) | Premise |
| 5 | \(C(a)\Rightarrow P(a)\) | “\(x=a\) in 4” |
| 6 | \(P(a)\) | From steps 5 and 3 |
| 7 | \(\neg B(a)\) | From step 2 |
| 8 | \(P(a)\land\neg B(a)\) | Conjoin the two obtained statements |
| 9 | \(\exists x(P(x)\land\neg B(x))\) | “\(x=a\)” |

**Textbook clarification:** At step 2, \(a\) must name a witness provided by the existential premise; it is not an arbitrary domain element. The universal premise in step 4 applies to that same witness, producing step 5. Steps 6–8 use modus ponens and conjunction, and step 9 asserts existence using the witness already obtained. See §3.6.1, printed pp.56–58 (textbook PDF pp.64–66), for the quantifier meanings; §3.6.4, printed p.59 (PDF p.67), for the common domain; §1.4.1, printed p.10 (PDF p.18), for modus ponens; and §3.1.1, printed p.42 (PDF p.50), for conjunction. The witness explanation expands the source's shorthand while retaining its nine-step proof.

<a id="pdf-page-151"></a>
## PDF page 151 — Direct proof and parity definitions

[Original scan](source_pages/page_151.png)

**Proof techniques: direct proof.** To prove an implication (p\Rightarrow q), start from (p) and derive (q).

An integer (n) is **even** if there is a (k\in\mathbb Z) such that (n=2k=2k+0). It is **odd** if there is a (k\in\mathbb Z) such that (n=2k+1).

**Textbook cross-reference:** §1.5, “Proving an Implication,” printed pp. 11–12 (PDF pp. 19–20).

<a id="pdf-page-152"></a>
## PDF page 152 — The square of an odd integer is odd

[Original scan](source_pages/page_152.png)

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

[Original scan](source_pages/page_153.png)

**Claim.** If (m,n) are perfect squares, then (mn) is a perfect square.

Write (m=i^2) and (n=j^2) for some (i,j\in\mathbb Z). Therefore
\[
mn=i^2j^2=(ij)^2.
\]
Since (ij\in\mathbb Z), this is a perfect square.

**Textbook cross-reference:** §1.5, printed pp. 11–12, for direct proof from the definitions.

<a id="pdf-page-154"></a>
## PDF page 154 — Proof by contraposition

[Original scan](source_pages/page_154.png)

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

[Original scan](source_pages/page_155.png)

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

[Original scan](source_pages/page_156.png)

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

[Original scan](source_pages/page_157.png)

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

[Original scan](source_pages/page_158.png)

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

[Original scan](source_pages/page_159.png)

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

[Original scan](source_pages/page_160.png)

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

[Original scan](source_pages/page_161.png)

The handwritten page lists:

- “Proof by sampling” — crossed out.
- “Proof by bullying” — crossed out.
- “Proof by insulting” — checked [the final method name is unclear in source; it may be a humorous expression rather than a formal method].

**Textbook cross-reference:** §1.9, “Good Proofs in Practice,” printed pp. 17–19 (PDF pp. 25–27), gives related guidance about what constitutes a proof. The three expressions above are source comments, not textbook methods.

<a id="pdf-page-162"></a>
## PDF page 162 — Proof by cases and a Ramsey example

[Original scan](source_pages/page_162.png)

**Proof by cases.** The diagrams show a complete graph on four vertices (a square with its diagonals), a complete graph on five vertices (a pentagon with diagonals), and a six-vertex cycle outline. In the five-vertex picture, the five perimeter edges are blue and the five diagonal edges are red.

The stated Ramsey number is
\[
R(3,3)=6,
\]
with the annotation “monochromatic clique.”

**Textbook clarification:** \(R(3,3)=6\) means that every red/blue coloring of all edges of \(K_6\) contains a triangle whose three edges have the same color, while an appropriate coloring of \(K_5\) has none. The rightmost sketch only shows the perimeter of six vertices; the complete graph requires all pairwise edges. See §1.7, “Proof by Cases,” printed pp. 15–16 (PDF pp. 23–24).

<a id="pdf-page-163"></a>
## PDF page 163 — Additional Ramsey numbers

[Original scan](source_pages/page_163.png)

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

[Original scan](source_pages/page_164.png)

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

[Original scan](source_pages/page_165.png)

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

[Original scan](source_pages/page_166.png)

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

[Original scan](source_pages/page_167.png)

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

[Original scan](source_pages/page_168.png)

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

[Original scan](source_pages/page_169.png)

**Prime factorization.** Let \(P(n)\) mean “a prime factorization of \(n\) exists.” The source mentions \(\mathbb Z_{\ge0}\) and \(\mathbb N\) alongside the notation.

Form the set of counterexamples:
\[
C=\{n:P(n)\text{ does not hold}\}.
\]
Assume \(C\) is a nonempty set of nonnegative integers. By the **well-ordering principle (WOP)**, \(C\) has a smallest element.

**Textbook clarification:** for this property the domain should be integers \(n\ge2\) (or include \(1\) using the empty product); \(0\) is not a product of primes. This domain restriction is essential to the counterexample argument. See §2.3, “Factoring into Primes,” printed p. 30 (PDF p. 38), for this well-ordering argument, and §5.2, printed pp. 124–126 (PDF pp. 132–134), for strong induction.

<a id="pdf-page-170"></a>
## PDF page 170 — The smallest-counterexample argument

[Original scan](source_pages/page_170.png)

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

[Original scan](source_pages/page_171.png)

**Well-ordering principle (WOP).** Given a predicate \(P(n)\), define
\[
C=\{n:P(n)\text{ is not true}\}.
\]
Assume \(C\) is nonempty, and use WOP to choose its smallest element \(n_0\in C\). The aim is to derive that \(P(n_0)\) is true, contradicting \(n_0\in C\).

The last handwritten line reads “\(n<n_0\) — \(P(n)\) is not true.” **Source correction:** minimality of the counterexample gives the reverse: \(P(n)\) is true for every eligible \(n<n_0\). The line \(P(n_0)\) “true,” above it, is the contradiction the argument is meant to establish.

**Textbook cross-reference:** §2.2, “Template for Well Ordering Proofs,” printed pp. 28–29 (PDF pp. 36–37).

<a id="pdf-page-172"></a>
## PDF page 172 — Strong-induction proof for three/five kilogram weights

[Original scan](source_pages/page_172.png)

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

[Original scan](source_pages/page_173.png)

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

[Original scan](source_pages/page_174.png)

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

[Original scan](source_pages/page_175.png)

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

[Original scan](source_pages/page_176.png)

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

[Original scan](source_pages/page_177.png)

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

[Original scan](source_pages/page_178.png)

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

[Original scan](source_pages/page_179.png)

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

[Original scan](source_pages/page_180.png)

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

[Original scan](source_pages/page_181.png)

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

[Original scan](source_pages/page_182.png)

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

[Original scan](source_pages/page_183.png)

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

[Original scan](source_pages/page_184.png)

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

[Original scan](source_pages/page_185.png)

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

[Original scan](source_pages/page_186.png)

The heading is **hexation**, illustrated by four up-arrows. The page defines a sequence using the following indexing:
\[
g_0=3\uparrow\uparrow\uparrow\uparrow3
\]
(four arrows),
\[
g_1=3\underbrace{\uparrow\cdots\uparrow}_{g_0\text{ arrows}}3,
\qquad
g_2=3\underbrace{\uparrow\cdots\uparrow}_{g_1\text{ arrows}}3,
\]
and, at the last step,
\[
g_{63}=3\underbrace{\uparrow\cdots\uparrow}_{g_{62}\text{ arrows}}3.
\]
An arrow labels \(g_{63}\) as **Graham's number**. “HYPEROPERATIONS” is written in red at the bottom.

**Textbook cross-reference:** §6.3, printed pp. 180–183, provides recursive-function context; the hyperoperation sequence and Graham's number on this page are additional lecture material.

<a id="pdf-page-187"></a>
## PDF page 187 — TREE and comparisons of very large numbers

[Original scan](source_pages/page_187.png)

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

[Original scan](source_pages/page_188.png)

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

[Original scan](source_pages/page_189.png)

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

[Original scan](source_pages/page_190.png)

The sets shown are
\[
A=\{a,b,c,d,e\},\qquad B=\{1,2,3,4\}.
\]
Clearly visible arrows are \(a\to1\), \(d\to2\), and \(c\to4\). The drawing leaves \(b,e\) with no outgoing arrow and \(3\) with no incoming arrow. The labels to the right are “total,” “surjective,” and “injective \(f\)” [no clear final truth-value marks are attached].

**Clarification of the shown arrows:** they define an injective partial function, but the relation is not total on the displayed \(A\) and does not hit every element of the displayed \(B\).

**Textbook cross-reference:** §4.4.1, “Relation Diagrams,” and Definition 4.4.2, printed pp. 90–91 (PDF pp. 98–99), for the arrows and function properties. §4.5 is “Finite Cardinality,” beginning at printed p. 93 (PDF p. 101).

<a id="pdf-page-191"></a>
## PDF page 191 — Arrow definitions of relation properties

[Original scan](source_pages/page_191.png)

Let \(R:A\to B\) be a relation. The page lists the following definitions, understood at every point in the indicated set:

- \(R\) is a **function** if it has the \([\le 1\text{ arrow out}]\) property.
- \(R\) is **total** if it has the \([\ge 1\text{ arrow out}]\) property.
- \(R\) is **surjective** if it has the \([\ge 1\text{ arrow in}]\) property.
- \(R\) is **injective** if it has the \([\le 1\text{ arrow in}]\) property.
- The final handwritten line says “bijective if both \([\ge1\text{ arrow in}]\) and \([\le1\text{ arrow in}]\) hold.” Thus the written condition ensures exactly one incoming arrow at every point of \(B\), but omits a condition on outgoing arrows.

**Textbook clarification:** Definition 4.4.2 requires a bijection to have **both exactly one outgoing arrow at every domain point and exactly one incoming arrow at every codomain point**. The handwritten final line should therefore also include the function and total requirements. See §4.4.1, “Relation Diagrams,” printed pp. 90–91 (PDF pp. 98–99).

<a id="pdf-page-192"></a>
## PDF page 192 — Counting arrows in a surjective function

[Original scan](source_pages/page_192.png)

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

[Original scan](source_pages/page_193.png)

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

[Original scan](source_pages/page_194.png)

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

[Original scan](source_pages/page_195.png)

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

[Original scan](source_pages/page_196.png)

There are five available ice-cream flavours, labelled \(A,B,C,D,E\). How many ways are there to choose twelve ice creams when flavour multiplicities matter and order is disregarded?

The diagram uses a zero for an ice cream and a one as a separator between consecutive flavours. Its example is
\[
\underbrace{00000}_{A}\;1\;
\underbrace{00000}_{B}\;1\;
\underbrace{00}_{C}\;1\;
\underbrace{\phantom{00}}_{D}\;1\;
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

[Original scan](source_pages/page_197.png)

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

[Original scan](source_pages/page_198.png)

Choose twelve ice creams when five flavours are available. The page repeats the separator encoding and writes the count
\[
\binom{16}{4}=1820\text{ ways}.
\]

The illustration has five labelled flavour blocks separated by four ones. It draws three zeros in each of the first four blocks, leaving the fifth empty:
\[
\underbrace{000}_{A}1\underbrace{000}_{B}1
\underbrace{000}_{C}1\underbrace{000}_{D}1
\underbrace{\phantom{000}}_{E}.
\]
Arrows point upward to the flavour labels. A second sketch has a sequence of choice slots, with “5” written above the first three slots to indicate five available choices at each step. The page writes
\[
5^{12}\sim 2\times10^8.
\]

**Textbook clarification:** \(5^{12}=244{,}140{,}625\) counts **ordered** sequences of twelve flavour choices, whereas \(1820\) counts flavour multiplicities with order disregarded. These are different objects, which explains the different counts. See §14.2.1, “The Product Rule,” printed pp. 552–553 (PDF pp. 560–561), and §14.5.2, printed p. 563 (PDF p. 571).

<a id="pdf-page-199"></a>
## PDF page 199 — Two ice creams from two flavours

[Original scan](source_pages/page_199.png)

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

[Original scan](source_pages/page_200.png)

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

[Original scan](source_pages/page_201.png)

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

[Original scan](source_pages/page_202.png)

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

[Original scan](source_pages/page_203.png)

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

[Original scan](source_pages/page_204.png)

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

[Original scan](source_pages/page_205.png)

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

<a id="pdf-page-206"></a>
## PDF page 206 — Fractional parts, nested floors/ceilings and modulo

[Original scan](source_pages/page_206.png)

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

[Original scan](source_pages/page_207.png)

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

[Original scan](source_pages/page_208.png)

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

[Original scan](source_pages/page_209.png)

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

[Original scan](source_pages/page_210.png)

**Textbook cross-reference:** §21.2, printed pp. 870–873 (PDF pp. 878–881).

Use $T_1=0$. Setting $k=\lg n$ gives $T_{n/2^k}=T_1$, so

$$
T_n=nT_1+n\lg n-n+1
=\boxed{n\lg n-n+1}.
$$

This exact solution uses the power-of-two input-size assumption from the preceding page.

<a id="pdf-page-211"></a>
## PDF page 211 — Homogeneous linear recurrences and characteristic roots

[Original scan](source_pages/page_211.png)

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

[Original scan](source_pages/page_212.png)

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

[Original scan](source_pages/page_213.png)

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

[Original scan](source_pages/page_214.png)

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
|---|---|---|
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

[Original scan](source_pages/page_215.png)

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

[Original scan](source_pages/page_216.png)

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

[Original scan](source_pages/page_217.png)

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

[Original scan](source_pages/page_218.png)

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

[Original scan](source_pages/page_219.png)

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

[Original scan](source_pages/page_220.png)

This page contains reference and administrative notes rather than a new mathematical topic.

- Rosen — “Discrete Math”.
- Epp — the book-title line is left blank.
- Gersting — “Math Structures for CS”.
- Hein — “Discrete Structures”.

The lower half contains “40% — 10% + 50%”, the numbers “35” and “55”, and a further “40 50” annotation. **Source qualification:** their association with particular assessment components is not specified clearly enough to reconstruct a grading scheme. These are transcribed as written, not treated as an authoritative current marks distribution.

<a id="pdf-page-221"></a>
## PDF page 221 — Graph coloring and the maximum-degree bound

[Original scan](source_pages/page_221.png)

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
