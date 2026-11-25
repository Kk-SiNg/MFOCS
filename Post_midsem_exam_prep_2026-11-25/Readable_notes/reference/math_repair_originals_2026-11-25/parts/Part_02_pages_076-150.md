This part transcribes source PDF pages 076–150. Sparse continuation pages are retained. Source omissions and numerical errors are identified explicitly; supplementary reasoning is labelled separately.

<a id="pdf-page-076"></a>

## PDF page 076 — Continuation: an order on relations

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

For posets \((S,\preceq_1)\) and \((T,\preceq_2)\), a function \(f:S\to T\) is **order-reflecting** if

$$
\forall a,b\in S,\qquad
f(a)\preceq_2 f(b)\implies a\preceq_1 b.
$$

**Textbook cross-reference:** §9.7, Definition 9.7.1, printed p.339, provides the related concept of relation-preserving isomorphism. Order reflection is the backward implication of that relation equivalence.

<a id="pdf-page-080"></a>

## PDF page 080 — Order reflection implies injectivity

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

A set \(S\subseteq\mathbb R^n\) is **convex** if, for every \(x,y\in S\), the line segment joining \(x\) and \(y\) is entirely contained in \(S\).

**Diagrams.** A circular region contains several complete segments joining pairs of its points. A second region has an inward notch: a segment joining two points on opposite sides of the notch passes outside the region, whereas a lower segment remains inside. The latter region illustrates failure of convexity.

**Textbook cross-reference:** No matching treatment of convex sets/computational geometry was found in the supplied Lehman–Leighton–Meyer textbook. This is course-note material.

<a id="pdf-page-082"></a>

## PDF page 082 — Convexity characterized by line intersections

The notes give another characterization: \(S\subseteq\mathbb R^n\) is convex if, for any line \(\ell\) in \(\mathbb R^n\), the intersection \(\ell\cap S\) is a single, possibly empty, line segment.

**Diagrams.** A line through a circular region intersects it in one segment. A line across a region with a notch intersects it in separate pieces, so that region is not convex.

**Clarification of terminology:** Here “segment” describes an interval along the line; for general unbounded or open convex sets, the intersection can also be an unbounded or open interval. The literal source wording is “single (possibly empty) line segment.”

**Textbook cross-reference:** No matching computational-geometry section was found in the supplied textbook.

<a id="pdf-page-083"></a>

## PDF page 083 — Parametrizing a line segment

The segment joining points \(p\) and \(q\) is parametrized by

$$
rp+(1-r)q,\qquad r\in[0,1].
$$

The endpoint \(p\) corresponds to \(r=1\), and \(q\) corresponds to \(r=0\). The source diagram marks an intermediate point on the segment between them.

**Textbook cross-reference:** No matching computational-geometry section was found in the supplied textbook.

<a id="pdf-page-084"></a>

## PDF page 084 — Convex combinations

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

The page draws a segment with its two endpoints, followed by a triangle with an interior point. Beside the triangle it writes

$$
\sum_i r_i p_i,\qquad r_i=0.3,\quad i=1,2,3.
$$

**Source numerical error:** The three displayed coefficients \(0.3,0.3,0.3\) sum to \(0.9\), so they do not meet the normalization condition for a convex combination on page 084. The numerical values are retained exactly as written; the page does not supply corrected coefficients.

**Textbook cross-reference:** No matching computational-geometry section was found in the supplied textbook.

<a id="pdf-page-086"></a>

## PDF page 086 — Convex combinations stay in a convex set

If \(S\) is convex and \(p_1,\ldots,p_k\in S\subseteq\mathbb R^n\), then every convex combination of these points also belongs to \(S\).

The page marks the cases \(k=1\) and \(k=2\). Its diagram draws a segment wholly inside the region \(S\).

**Textbook cross-reference:** No matching computational-geometry section was found in the supplied textbook.

<a id="pdf-page-087"></a>

## PDF page 087 — Two sets of convex-combination coefficients

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

For \(P\subseteq\mathbb R^n\), the **convex hull of \(P\)** is the minimal convex set containing \(P\). The notes name this set \(C\).

A separate reminder reads “a minimal set with property \(X\).”

**Example diagram.** For \(P=\{p_1,p_2\}\), the convex hull is the entire segment joining \(p_1\) and \(p_2\), not merely its endpoints.

**Textbook cross-reference:** No matching convex-hull section was found in the supplied textbook.

<a id="pdf-page-091"></a>

## PDF page 091 — Diagrams of convex hulls

The page gives geometric illustrations without a written proof:

- \(P=\{p_1,p_2,p_3\}\) is represented by the three vertices of a triangle; the entire triangular region is shaded.
- Four points form a quadrilateral inside a larger enclosing region. The smaller polygon illustrates the minimal convex region determined by those points.
- A filled rectangular region is drawn.
- A nonconvex, curved region is outlined in black, with a larger red convex outline and shading around it, illustrating filling the inward indentations.
- A second shaded triangle has an interior point in addition to its vertices; the extra interior point does not enlarge the triangular hull.

**Textbook cross-reference:** No matching convex-hull section was found in the supplied textbook.

<a id="pdf-page-092"></a>

## PDF page 092 — Minimal set and intersection definitions

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

The notation is \(P\subseteq\mathbb R^d\) and \(x\in\operatorname{Conv}(P)\).

**Diagram.** Several points lie on the boundary of a six-sided polygon, and several more lie inside it. An interior point is highlighted in red and joined by dotted segments toward other points of the configuration, illustrating a point expressed using a smaller selection of points.

No equation or proof is supplied on this page.

**Textbook cross-reference:** No matching convex-hull treatment was found in the supplied textbook.

<a id="pdf-page-098"></a>

## PDF page 098 — Unfinished convex-combination statement

The source contains the unfinished sentence:

> Given \(k\) points \(p_1,\ldots,p_k\) in a convex set \(S\), every …

The rest of the sentence is absent. It is retained as an unfinished fragment rather than replaced with a reconstructed assertion.

**Textbook cross-reference:** No matching convex-combination treatment was found in the supplied textbook.

<a id="pdf-page-099"></a>

## PDF page 099 — Reducing the number of nonzero coefficients

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

Let \(S\subseteq\mathbb R^d\) be convex and

$$
X=\{p_1,\ldots,p_k\}\subseteq S.
$$

**Exercise:** Show that every convex combination of points of \(X\) belongs to \(S\).

This repeats the earlier convex-combination lemma as a question. No proof is written on this page.

**Textbook cross-reference:** No matching convex-geometry section was found in the supplied textbook.

<a id="pdf-page-107"></a>

## PDF page 107 — Reduction lemma and Carathéodory's theorem

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

For a planar point set in \(\mathbb R^2\), the notes introduce **Graham scan** with these steps:

1. Find the point with the lowest \(y\)-coordinate; call it \(p\).
2. Sort all points by their angle with the \(x\)-axis.
3. Consider points from the sorted list in order.

The diagram marks consecutive positions \(i-1\), \(i\), and a next candidate. The page does not explicitly state the reference origin for the polar-angle sorting or give the complete turn-test rule.

**Textbook cross-reference:** No matching Graham-scan/computational-geometry section was found in the supplied textbook.

<a id="pdf-page-110"></a>

## PDF page 110 — Graham-scan point removals and turns

The page illustrates modifying candidate lists:

- A list containing \(p,A,B,C,D\), with \(C\) crossed out.
- A later list containing \(p,A,B,C,D',p\), with \(B\) and \(C\) crossed out.

The point diagram places \(p\) at the bottom, \(A\) and \(B\) on the right, \(C\) and \(D\) farther left, and \(D'\) above. Dotted candidate connections show why intermediate points may be removed while forming the hull.

A separate diagram compares the directions \(A\to B\) and \(A\to C\), illustrating the turn between consecutive candidate edges. The exact deletion test is not written on the page.

**Textbook cross-reference:** No matching Graham-scan section was found in the supplied textbook.

<a id="pdf-page-111"></a>

## PDF page 111 — Gift-wrapping algorithm

The underlined heading is **“Gift wrapping algo.”**

Beneath it are several unlabelled points and a faint broken vertical line. No algorithmic steps, equations, or complexity bound are written on this page.

**Textbook cross-reference:** No matching gift-wrapping/convex-hull algorithm section was found in the supplied textbook.

<a id="pdf-page-112"></a>

## PDF page 112 — Minkowski sum

For \(A,B\subseteq\mathbb R^n\), the page defines

$$
A\oplus B=\{a+b\mid a\in A,\ b\in B\}.
$$

**Diagrams.** \(A\) is drawn as a horizontal segment and \(B\) as a vertical segment. A coordinate sketch shows these directions, and a shaded rectangle illustrates their Minkowski sum.

**Textbook cross-reference:** No matching Minkowski-sum section was found in the supplied textbook.

<a id="pdf-page-113"></a>

## PDF page 113 — Minkowski-sum example to consider

The page draws \(A\) as a circular region with radius marked \(r\), and \(B\) as a horizontal segment marked \(0.5\). It then writes

$$
A\oplus B
$$

without drawing the resulting set or supplying a calculation.

**Textbook cross-reference:** No matching Minkowski-sum section was found in the supplied textbook.

<a id="pdf-page-114"></a>

## PDF page 114 — Rigid motions and a set-sum diagram

A rigid motion in \(\mathbb R^n\) is denoted by \((A,b)\), with arrows identifying \(A\) as the rotation part and \(b\) as the translation part. Its displayed map is

$$
x\longmapsto Ax+b.
$$

The page also draws a small filled circular set labelled \(A\), a larger circular boundary labelled \(B\), and an annular shaded set beside \(A\oplus B\).

**Notation warning:** The set \(A\) in the Minkowski-sum drawing and the matrix \(A\) in the rigid-motion formula use the same letter for different objects.

**Textbook cross-reference:** No matching rigid-motion/Minkowski-sum section was found in the supplied textbook.

<a id="pdf-page-115"></a>

## PDF page 115 — Rigid motions preserve distance

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

The page represents a plane curve by

$$
c(t)=(x(t),y(t)),
\qquad t\in[0,1].
$$

**Diagrams.** A closed oval has a marked point on its boundary. A separate green, curved path has short tick marks at successive positions. Another sketch shows two coordinate graphs; \(x(t)\) is written above the path, and the lower horizontal axis is labelled \(x\). These drawings accompany the idea of describing a curve through its coordinate functions. A small handwritten annotation immediately after the coordinate pair is [unclear in source].

**Textbook cross-reference:** No matching treatment of parametric curves was found in the supplied textbook.

<a id="pdf-page-120"></a>

## PDF page 120 — Circle parametrization and a curve in three dimensions

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

The page writes the family

$$
\{1,t,t^2,t^3,\ldots,t^n\}.
$$

Below it is an unlabelled smooth curve with one crest and one trough. No coefficient formula or additional claim is written on this page.

**Textbook cross-reference:** No matching polynomial-curve construction section was found in the supplied textbook.

<a id="pdf-page-122"></a>

## PDF page 122 — Bézier curves: coordinate representation

The heading is **“Bezier curves.”** The curve is represented by

$$
c(t)=(x(t),y(t)).
$$

**Diagram.** Coordinate axes are drawn with a diagonal vector starting at the origin and pointing into the first quadrant, illustrating a position vector for a point on the curve. No control-point or blending-function formula is given until the next page.

**Textbook cross-reference:** No matching Bézier-curve section was found in the supplied textbook.

<a id="pdf-page-123"></a>

## PDF page 123 — Bézier curve as a weighted sum of control points

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

The page lists these examples:

- **“This statement is false.”** A large cross is drawn beside it.
- \(1+1=2\), marked as a proposition and assigned a propositional label \(P\).
- **“Today is Monday,”** assigned label \(P\).
- **“All Mondays are pleasant,”** assigned label \(Q\).

The underlined final heading is **“Propositional variables.”** The letter \(P\) is reused for two separate examples.

**Textbook clarification:** The definition in §1.1, printed p.5 (textbook PDF p.13), requires a statement to be either true or false and excludes statements whose truth varies with circumstance. Thus “Today is Monday” requires a specified day/context to have a fixed truth value. The cross beside the self-referential first sentence records that it does not receive a consistent classical truth value. §3.1, printed p.42 (PDF p.50), explains using \(P,Q\) as variables for propositions.

<a id="pdf-page-128"></a>

## PDF page 128 — Negation

Under **“Connectives,”** the page takes a proposition \(p\) and forms its negation \(\neg p\).

The source uses \(0\) for false and \(1\) for true:

| \(p\) | \(\neg p\) |
|---|---|
| 0 | 1 |
| 1 | 0 |

**Textbook cross-reference:** §3.1.1, **“NOT, AND, and OR,”** printed p.42 (textbook PDF p.50), gives the negation truth table with \(T,F\) in place of \(1,0\).

<a id="pdf-page-129"></a>

## PDF page 129 — Conjunction, disjunction, and exclusive OR

The page names **conjunction** \(p\land q\) and **disjunction** \(p\lor q\), and adds a truth-table column for exclusive OR \(p\oplus q\):

| \(p\) | \(q\) | \(p\land q\) | \(p\lor q\) | \(p\oplus q\) |
| --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 1 |
| 1 | 1 | 1 | 1 | 0 |

**Textbook cross-reference:** §3.1.1, printed pp.42–43 (textbook PDF pp.50–51), gives AND, inclusive OR, and XOR with the same truth values.

<a id="pdf-page-130"></a>

## PDF page 130 — Implication and its contrapositive

The heading **“Conditional statements”** lists

$$
p\Rightarrow q,\qquad p\Leftrightarrow q.
$$

The truth table on this page concerns implication and its contrapositive:

| \(p\) | \(q\) | \(p\Rightarrow q\) | \(\neg q\Rightarrow\neg p\) |
| --- | --- | --- | --- |
| 0 | 0 | 1 | 1 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 1 | 1 | 1 |

The two final columns agree in every row.

**Textbook cross-reference:** §3.1.2, **“IMPLIES,”** printed pp.43–45 (textbook PDF pp.51–53), defines implication. §3.3.1, **“Implications and Contrapositives,”** printed pp.48–49 (PDF pp.56–57), gives the same comparison and identifies the equivalent contrapositive. The listed biconditional is defined in §3.1.3, printed p.45 (PDF p.53).

<a id="pdf-page-131"></a>

## PDF page 131 — A conditional-language example and biconditional truth table

The source illustrates \(p\Rightarrow q\) with the Hindi statement

> जल है तो कल है।

This says, “If there is water, there is a tomorrow/future.” The water clause is labelled \(p\), and the future clause \(q\).

It separately writes \(\neg p\Rightarrow\neg q\) beside

> जल नहीं तो कल नहीं।

This says, “If there is no water, there is no tomorrow/future.”

The lower part gives the biconditional table:

| \(p\) | \(q\) | \(p\Leftrightarrow q\) |
| --- | --- | --- |
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

**Textbook clarification:** The second conditional is the **inverse** of the first; the contrapositive studied on [PDF page 130](#pdf-page-130) is \(\neg q\Rightarrow\neg p\). They should not be substituted for one another. See §3.3.1, printed pp.48–49 (textbook PDF pp.56–57), for implication/contrapositive equivalence. §1.4.1, printed p.10 (PDF p.18), explicitly gives an unsound “Non-Rule” that tries to infer \(P\Rightarrow Q\) from \(\neg P\Rightarrow\neg Q\). The biconditional table matches §3.1.3, printed p.45 (PDF p.53).

<a id="pdf-page-132"></a>

## PDF page 132 — Syntax for forming compound propositions

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

The heading is **“Compound propositions.”** The formula, written twice, is

$$
\bigl((\neg p\land q)\lor r\bigr)\Rightarrow s.
$$

Its parentheses first group \(\neg p\land q\), then the disjunction with \(r\), before applying the implication to \(s\). No truth table or simplification is supplied on this page.

**Textbook cross-reference:** §3.1, printed pp.42–45 (textbook PDF pp.50–53), supplies the connective meanings; §3.2.1, **“Truth Table Calculation,”** printed pp.46–47 (PDF pp.54–55), illustrates evaluating compound expressions.

<a id="pdf-page-134"></a>

## PDF page 134 — Premises and conclusion of an argument

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

The page draws:

- A circular set \(A\), with its centre marked and radius \(r=1\).
- A horizontal segment \(B\), with length \(\ell=0.5\).
- The notation \(A\oplus B\), beside a small shaded rounded region.

This returns to the set-sum example from [PDF page 113](#pdf-page-113). No equation for the resulting boundary, placement of the segment endpoints, or explicit statement of whether \(A\) is the circle or the filled disk is written on this page.

**Textbook cross-reference:** No matching Minkowski-sum section was found in the supplied textbook. Here \(\oplus\) denotes a sum of sets, whereas [PDF page 129](#pdf-page-129) uses the same symbol for exclusive OR.

<a id="pdf-page-137"></a>

## PDF page 137 — Expressing argument validity as an implication

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

Seven circled premise/conclusion patterns appear on the page. The names below identify the standard rules represented by the handwritten formulas.

| Pattern | Premise(s) | Conclusion |
| --- | --- | --- |
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

An argument is said to be **sound** if it is **valid** and its **premises are true**.

The boxed shorthand is

$$
\text{premises}\Rightarrow\text{conclusion}.
$$

The definition adds the truth of the premises to the validity condition from [PDF page 135](#pdf-page-135).

**Textbook cross-reference:** §1.4.1, **“Logical Deductions,”** printed p.10 (textbook PDF p.18), discusses sound inference rules and explains why starting from true axioms and applying sound rules yields true conclusions. §3.3.2, printed p.50 (PDF p.58), defines validity for formulas. The notes' phrase “sound argument” additionally specifies that the actual premises are true.

<a id="pdf-page-142"></a>

## PDF page 142 — A satisfiability example

Under the heading **“Satisfiability,”** the page boxes the formula

$$
\bigl((p\land q)\lor\neg r\bigr)\Rightarrow q.
$$

There is a small annotation beneath the box [unclear in source]. No truth assignment, truth table, or verdict is written on the page.

**Textbook clarification:** §3.3.2, **“Validity and Satisfiability,”** printed p.50 (textbook PDF p.58), defines a satisfiable formula as one true for at least one truth assignment. The displayed formula is satisfiable: any assignment with \(q=1\) makes the implication true. It is not valid: with \(p=q=r=0\), the antecedent is true and the consequent false. These evaluations use §3.1.1–3.1.2, printed pp.42–43 (PDF pp.50–51); the assignments are added clarification rather than handwritten solutions.

<a id="pdf-page-143"></a>

## PDF page 143 — Further inference patterns involving implications and equivalence

The page gives eight premise/conclusion patterns:

| No. | Premise(s) | Conclusion |
| --- | --- | --- |
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

The circled claim is

$$
p\Rightarrow q,\quad p\land r\ \vdash\ q\land r.
$$

The proof is written in six steps:

| Step | Formula | Reason in the notes |
| --- | --- | --- |
| 1 | \(p\land r\) | Premise |
| 2 | \(r\) | \(p\land r\vdash r\) |
| 3 | \(p\) | \(p\land r\vdash p\) |
| 4 | \(p\Rightarrow q\) | Premise |
| 5 | \(q\) | From steps 3 and 4 |
| 6 | \(q\land r\) | From steps 2 and 5 |

**Textbook cross-reference:** §1.4.1, printed p.10 (textbook PDF p.18), gives modus ponens, used at step 5, and requires each deduction to identify the earlier facts used. §3.1.1, printed p.42 (PDF p.50), gives the conjunction truth table supporting extraction in steps 2–3 and conjunction formation in step 6.

<a id="pdf-page-145"></a>

## PDF page 145 — Derivation using contraposition and implication chaining

**Premises:**

$$
p\Rightarrow q,\qquad
\neg p\Rightarrow r,\qquad
r\Rightarrow s.
$$

**Conclusion:** \(\neg q\Rightarrow s\).

The source proof proceeds as follows:

| Step | Formula | Justification |
| --- | --- | --- |
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
| --- | --- | --- |
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
