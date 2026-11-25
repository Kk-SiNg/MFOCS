# CS208 (MFOCS) — End-Sem Study Plan & Checklist (Anchored to `Readable_notes.html`)

**Primary Source:** [Readable_notes.html](Post_midsem_exam_prep_2026-11-25/Readable_notes/Readable_notes.html) (and Markdown parts in [Readable_notes/parts/](Post_midsem_exam_prep_2026-11-25/Readable_notes/parts/) / [Page_index.md](Post_midsem_exam_prep_2026-11-25/Readable_notes/Page_index.md)) — covers what was taught in class across PDF pages **001–221**.

- **Phase 1 (Refresher — Pre-Midsem):** PDF pages **001–160**
- **Phase 2 (Core Post-Midsem):** PDF pages **161–221** *(use the `Pages 161–221` filter button in the HTML reader)*
- **Add-on Note:** Anything missing from `Readable_notes.html` (extra tutorial/assignment drills or unrecorded topics) will be appended later once the core flow is complete.

---

## Master Flow Tracker

### Phase 1: Pre-Midsem Refresher (Pages 001–160)

- [ ] **R1:** Sets, Functions, Cardinality & Countability (pp. 001–030, 036–048)
- [ ] **R2:** Binary Relations, Equivalence Relations & Posets (pp. 031–035, 049–080)
- [ ] **R3:** Computational Geometry & Bézier Curves (pp. 081–125, 136)
- [ ] **R4:** Logic, Rules of Inference & Basic Proof Techniques (pp. 126–160)

### Phase 2: Post-Midsem Curriculum (Pages 161–221)

- [ ] **Stage 1:** Proof Pitfalls, Proof by Cases, Strong Induction & Well-Ordering (pp. 161–174)
- [ ] **Stage 2:** Recursive Data Types, Fast-Growing Functions & Structural Induction (pp. 175–188)
- [ ] **Stage 3:** Arrow Relations, Explicit Bijections & Basic Counting Rules (pp. 189–200)
- [ ] **Stage 4:** Pigeonhole Principle, Inclusion–Exclusion & Combinatorial Proofs (pp. 200–202)
- [ ] **Stage 5:** Sums, Products, Stirling, Floor/Ceiling/Modulo & Iverson Brackets (pp. 203–208)
- [ ] **Stage 6:** Modelling Recurrences & Linear Recurrences (pp. 209–212)
- [ ] **Stage 7:** Divide-and-Conquer Recurrences — Akra–Bazzi & Master Theorem (pp. 213–214)
- [ ] **Stage 8:** Generating Functions & Formal Power Series (pp. 215–218)
- [ ] **Stage 9:** Graph Definitions, Isomorphism & Graph Coloring (pp. 219–221)

---

## Phase 1: Pre-Midsem Refresher (Pages 001–160)

### R1. Sets, Functions, Cardinality & Countability (`pp. 001–030`, `036–048`)

- [ ] **Sets & Products** (`pp. 001–005`): membership, equality, subsets ($\subseteq$ vs. $\subset$), complement $\overline{A}$, ordered $n$-tuples, Cartesian products $A_1 \times \dots \times A_n$
- [ ] **Functions & Invertibility** (`pp. 006–010`): domain, codomain, range, image/preimage; injective, surjective, bijective; inverse $f^{-1}$ exists iff bijective; necessary vs. sufficient phrasing
- [ ] **Comparing Cardinalities & Interval Bijections** (`pp. 011–014`, `036–048`):
  - [ ] Injection $\implies |A|\le|B|$, surjection $\implies |A|\ge|B|$, bijection $\implies |A|=|B|$
  - [ ] Scaling/linear maps: $[0,1]\to[0,10]$ ($10x$), $(0,1)\to(a,b)$ ($(1-x)a+xb$), $\mathbb{N}\to 2\mathbb{N}$ ($2x$)
  - [ ] Calculus/composition bijections: $(0,1)\to\mathbb{R}$ via $\tan(\pi x - \pi/2)$; $\mathbb{R}\to\mathbb{R}^+$ via $e^x$; $[0,1]\to\mathbb{R}$ by composition
  - [ ] Tutorial 1 chain shifts: $[0,1)\to(0,1)$, $(0,1]\to(0,1)$, $[0,1]\to(0,1)$ (two disjoint chains $1/2^n, 1/3^n$), $\mathbb{R}^+\to\mathbb{R}^+\cup\{0\}$, $[0,1]\cup(2,3]\to[0,1]$
- [ ] **Countability & Diagonalization** (`pp. 015–030`):
  - [ ] Subsets of countable sets are countable
  - [ ] Diagonal enumeration of $X\times Y$, $\mathbb{Q}$, finite products, and countable unions of countable sets
  - [ ] Finite sequences and finite subsets of $\mathbb{N}$ are countable
  - [ ] Uncountability via contradiction/diagonalization: $\mathcal{P}(\mathbb{N})$ (labelled vs. unlabelled), infinite binary sequences $\{0,1\}^\mathbb{N}$, and $\mathbb{R}$ ($t \mapsto 0.t$ decimal injection)

### R2. Binary Relations, Equivalence Relations & Posets (`pp. 031–035`, `049–080`)

- [ ] **Relation Properties** (`pp. 031–035`, `049`): $R \subseteq A \times B$, reflexive, symmetric, antisymmetric, transitive (plus counterexamples like $\|x-y\|<1$, consecutive integers, orthogonality)
- [ ] **Equivalence Relations & Partitions** (`pp. 050–071`):
  - [ ] Equivalence classes $[a]$, congruence mod 5, geometric norm examples ($\|x\|=\|y\|$, $|x|_1=|y|_1$)
  - [ ] Fundamental equivalence: $aRb \iff [a]=[b] \iff [a]\cap[b]\neq\emptyset$, and partition $\leftrightarrow$ equivalence relation correspondence
- [ ] **Partial Orders & Refinement Poset** (`pp. 052–054`, `059`, `072–080`):
  - [ ] Poset axioms (reflexive, antisymmetric, transitive): $(\mathbb{Z}^+, \mid)$, $(\mathcal{P}(S),\subseteq)$, infinite binary sequences
  - [ ] Finer relation ($R_1 \sim R_2$ iff $aR_1b \implies aR_2b$) forms a poset $(M, \sim)$ on equivalence relations
  - [ ] Comparable elements vs. total orders (chains)
  - [ ] Order-preserving (monotone) maps & composition; order-reflecting maps imply injectivity (`p. 080`)

### R3. Computational Geometry & Bézier Curves (`pp. 081–125`, `136`)

- [ ] **Convex Sets & Convex Hulls** (`pp. 081–096`): line-segment vs. line-intersection convexity, $rp+(1-r)q$, convex combinations stay in convex sets, 3 equivalent definitions of $\text{Conv}(S)$
- [ ] **Carathéodory's Theorem** (`pp. 097–108`): Reduction lemma ($d$ points for conic combinations) and Carathéodory ($d+1$ points for convex combinations via lifting $(x,1)\in\mathbb{R}^{d+1}$)
- [ ] **Planar Hulls, Minkowski Sums & Rigid Motions** (`pp. 109–118`, `136`): Graham scan (left-turn determinant), gift-wrapping, Minkowski sum $A\oplus B$, distance-preserving maps and rotations about fixed point
- [ ] **Parametric & Bézier Curves** (`pp. 119–125`): circle/3D curves, monomial vs. Bernstein basis, control-point weighted sums, tangent vectors

### R4. Logic, Inference & Proof Techniques (`pp. 126–160`)

- [ ] **Propositional Logic** (`pp. 126–133`): propositions, $\neg,\land,\lor,\oplus,\Rightarrow,\Leftrightarrow$, converse/contrapositive/inverse, compound expressions
- [ ] **Arguments, Validity & Inference** (`pp. 134–146`): valid vs. sound arguments, satisfiability, inference rules (modus ponens, chaining, De Morgan, etc.) & step-by-step derivations
- [ ] **Predicate Logic** (`pp. 147–150`): predicates, $\forall,\exists$, De Morgan's laws for quantifiers, witness-based existential proofs
- [ ] **Core Proof Techniques** (`pp. 151–160`):
  - [ ] Direct proof (parity, product of squares)
  - [ ] Contraposition ($3n+2$ odd $\implies n$ odd)
  - [ ] Contradiction ($a\le\sqrt{n}$ or $b\le\sqrt{n}$, $\sqrt{2}$ irrational)
  - [ ] Ordinary mathematical induction ($P(1)$ + $P(k)\Rightarrow P(k+1)$, sum formulas, $2^n < n!$, faulty same-color balls induction failing at $k=1$)

---

## Phase 2: Post-Midsem Curriculum (Pages 161–221)

### Stage 1. Proof by Cases, Strong Induction & Well-Ordering (`pp. 161–174`)

- [ ] Proof pitfalls (sampling, bullying, insulting comments) (`p. 161`)
- [ ] Proof by cases & Ramsey numbers ($R(3,3)=6$ proof and larger Ramsey numbers) (`pp. 162–163`)
- [ ] Strong induction vs. ordinary induction (`pp. 164–166`)
- [ ] Prime factorization existence by strong induction (`p. 165`) and $3\text{ kg}/5\text{ kg}$ weights $\ge 8\text{ kg}$ (`pp. 167–168`, `172–173`)
- [ ] Well-Ordering Principle (WOP) template: prime factorization (`pp. 169–171`) and sum formula (`p. 174`)
- [ ] Equivalence of ordinary induction, strong induction, and WOP (`p. 174`)

### Stage 2. Recursive Data Types & Structural Induction (`pp. 175–188`)

- [ ] Recursive objects: base cases + constructors (`p. 175`)
- [ ] Well-defined vs. ill-formed recursions on $\mathbb{N}$ (missing base case, growing args, overlapping cases, Collatz) (`pp. 176–177`)
- [ ] Fast-growing functions & context: Ackermann function (`p. 178`), repeated operations, tetration, pentation, Knuth arrows, hyperoperations, Graham's number, $\text{TREE}(3)$ (`pp. 179–180`, `186–187`)
- [ ] Recursive strings $A^*$ and formal structural induction (`pp. 181–183`) + length of concatenated strings (`p. 184`)
- [ ] Arithmetic expressions (`Aexp`): recursive definition, `eval`, `subs`, substitution vs. environment models & equivalence (`pp. 185`, `188`)

### Stage 3. Arrow Relations, Explicit Bijections & Counting Rules (`pp. 189–200`)

- [ ] Relations as arrow diagrams: total, function, injective, surjective, bijective (`pp. 189–191`)
- [ ] Mapping rules for finite sets (`surj`, `inj`, `bij`) & cardinality of infinite sets (`pp. 192–195`, `197`)
- [ ] Enumerating $\mathbb{Q}$: Cantor pairing function (`p. 195`) and Stern–Brocot mediant fractions (`p. 197`)
- [ ] Bijection rule & stars-and-bars: 12 ice-creams from 5 flavours ($\binom{16}{4}$) vs. ordered $5^{12}$ (`pp. 196`, `198–199`)
- [ ] Counting rules (sum, product, generalized product, division / $k$-to-1), grid paths (`p. 200`)

### Stage 4. Pigeonhole, Inclusion–Exclusion & Combinatorial Proofs (`pp. 200–202`)

- [ ] Pigeonhole Principle: hairs-on-heads example (`p. 200`) and subsets with the same sum (`p. 201`)
- [ ] Inclusion–Exclusion Principle: 2–3 set examples, divisibility, $n$-set formula and indicator proof (`p. 202`)
- [ ] Combinatorial proofs & binomial identities (symmetry, Vandermonde-style identity, Pascal's identity/triangle) (`p. 202`)

### Stage 5. Sums, Products, Integer Functions & Iverson Brackets (`pp. 203–208`)

- [ ] Geometric sums, $\sum i x^i$, polynomial-fit sums, integral bounds ($\sum\sqrt{i}$), harmonic numbers $H_n$ (`p. 203`)
- [ ] Products via logarithms, factorial bounds, Stirling's formula, and double sums ($\sum_{k=1}^n H_k$) (`p. 204`)
- [ ] Floor $\lfloor x \rfloor$, ceiling $\lceil x \rceil$, fractional part $\{x\}$: interval characterizations, negation, nested floor/ceiling identities (`pp. 205–206`)
- [ ] Modulo arithmetic $x \bmod y$ including negative signs (`pp. 206–207`)
- [ ] Iverson brackets $[P]$: rewriting bounds, nested log-sum example, closed form for $\sum \lfloor \sqrt{k} \rfloor$ & tighter lower bound on $\sum \sqrt{k}$ (`pp. 207–208`)

### Stage 6. Modelling Recurrences & Linear Recurrences (`pp. 209–212`)

- [ ] Josephus problem recurrences & closed form; Tower of Hanoi and Merge Sort via guess-and-verify / plug-and-chug (`pp. 209–210`)
- [ ] Homogeneous linear recurrences: characteristic polynomial, distinct roots (Fibonacci / Binet's formula), repeated roots (`p. 211`)
- [ ] Nonhomogeneous linear recurrences: homogeneous + particular solution & particular-solution guesses (`pp. 212–213`)

### Stage 7. Divide-and-Conquer Recurrences (`pp. 213–214`)

- [ ] Akra–Bazzi formula & conditions ($a_i, b_i, h_i(n), g(n)$, solving $\sum a_i b_i^p = 1$, integral formula) (`pp. 213–214`)
- [ ] Floor/ceiling perturbation invariance, Master theorem as a corollary, and recurrence growth big picture (`p. 214`)

### Stage 8. Generating Functions & Formal Power Series (`pp. 215–218`)

- [ ] Ordinary generating functions (OGFs), modeling constrained selections, and convolution / product rule (`pp. 215–216`)
- [ ] Rational generating functions, ice-cream calculation, partial fractions (distinct & repeated roots), and deriving the binomial theorem (`pp. 216–217`)
- [ ] Solving linear recurrences via OGFs (Fibonacci, Tower of Hanoi) and formal factorial power series ($n! = 1 + \sum_{i=1}^n (i-1)(i-1)!$) (`p. 218`)

### Stage 9. Graph Definitions, Isomorphism & Graph Coloring (`pp. 219–221`)

- [ ] Undirected simple graphs vs. directed graphs, adjacency, vertex degrees, Handshaking theorem, bipartite average-degree relation (`p. 219`)
- [ ] Standard graphs ($K_n$, path/"line" graph, cycle $C_n$) and Graph Isomorphism (equivalence relation, bijection preserving edges) (`p. 219`)
- [ ] Assessment/book notes (`p. 220`)
- [ ] Proper vertex coloring, $k$-colorability, chromatic number $\chi(G)$ ($C_{\text{even}}$, $C_{\text{odd}}$, $K_n$, bipartite graphs) (`p. 221`)
- [ ] SAT / complexity remarks and inductive proof of $\chi(G) \le \Delta(G) + 1$ (`p. 221`)

---

## Later Add-Ons *(If Needed After Core Flow)*

- [ ] Verify whether any unrecorded topics, Assignment 4–7 extras, or Tutorial 7–9 drills need to be appended after completing Stages 1–9.
