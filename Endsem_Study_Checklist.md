# CS208 (MFOCS) — Post-Midsem End-Sem Study Flow & Checklist

> **Pre-Midsem Boundary (Already Covered in `Study_material_before_mid_sems/cs208.pdf`):**
> Sets, tuples, Cartesian products, basic functions & countability ($\mathbb{Q}$ vs $\mathbb{R}, \mathcal{P}(\mathbb{N})$), binary relations, equivalence relations & partitions, posets & order-preserving/reflecting maps, computational geometry (convexity, convex hull, Carathéodory's theorem, Bézier curves), propositional & predicate logic, and basic proof techniques (direct, contraposition, contradiction, ordinary induction).
>
> **Post-Midsem Scope (This Checklist):**
> Built from `Full_topic_list/2026-2-CS208-MFOCS_ Class Summary.md` (Classes 1–22, Oct 5 – Nov 12, 2026), extended with Lecture 20–21 handwritten notes in `Study_material_after_mid_sems/MFOCS_Notes_Aug-Nov_2026.pdf` (Nov 17–18, 2026, where Class 23 was left blank in the summary), and cross-referenced with `MCS_Textbook_Lehman_Leighton_Meyer.pdf`, `Tutorial_8`, `Tutorial_9`, `Tutorial_10` (Oct 12 tutorial), and `MfoxAssignSamar.pdf`.

---

## Overall Study Flow

1. **Module 1: Advanced Induction & Well-Ordering** *(Picks up directly from pre-midsem Ordinary Induction)*
2. **Module 2: Recursive Data Types & Structural Induction** *(Generalizes induction from $\mathbb{N}$ to strings, trees, expressions)*
3. **Module 3: Cardinality Extensions & Combinatorics** *(Bijective counting, rules of counting, Pigeonhole, Inclusion–Exclusion)*
4. **Module 4: Integer Functions, Sums, Products & Asymptotics** *(Algebraic & analytic toolkit needed before recurrences)*
5. **Module 5: Recurrence Relations** *(Plug-and-chug, linear recurrences, Akra–Bazzi & Master Theorem)*
6. **Module 6: Generating Functions** *(Unifies Combinatorics from Module 3 and Linear Recurrences from Module 5)*
7. **Module 7: Graph Theory & Graph Coloring** *(Nov 17–18 lectures + verify Assignment 7 extras)*

---

## Progress Tracker

- [ ] **Module 1:** Advanced Induction & Well-Ordering
- [ ] **Module 2:** Recursive Data Types & Structural Induction
- [ ] **Module 3:** Cardinality Extensions & Combinatorics
- [ ] **Module 4:** Integer Functions, Sums, Products & Asymptotics
- [ ] **Module 5:** Recurrence Relations
- [ ] **Module 6:** Generating Functions
- [ ] **Module 7:** Graph Theory & Graph Coloring

---

## Module 1: Advanced Induction & Well-Ordering

*Sources: Lectures 1–4 (Oct 5–8), Tutorial 7 (Oct 12, image in `Tutorial_10/`), Notes pp. 161–174, Textbook Ch. 1, 2, 5, `MfoxAssignSamar.pdf` Assignment 1*

- [ ] **Proof Pitfalls & Mathematical Context (Light Review)**
  - [ ] Invalid proof techniques: proof by sampling, proof by bullying, proof by insulting (identify bugs in bogus proofs)
  - [ ] Proof by cases — illustrated via Ramsey number $R(3,3) = 6$ and extending to larger diagonal Ramsey numbers
  - [ ] Conceptual context (no heavy memorization): open conjectures (Goldbach, Collatz, Pólya), Strassen's matrix multiplication, Russell's paradox, Gödel's incompleteness, Turing undecidability
- [ ] **Strong Induction**
  - [ ] Canonical structure of a strong induction proof (base case(s), strong hypothesis $\forall j \le k, P(j)$, inductive step)
  - [ ] Comparison with ordinary induction (when strong induction is cleaner/necessary)
  - [ ] Example: Existence of prime factorization for all integers $n \ge 2$
  - [ ] Example: Constructing any weight $n \ge 8$ kg using $3$ kg and $5$ kg weights (formal multi-base-case proof)
- [ ] **Well-Ordering Principle (WOP)**
  - [ ] Formal statement of WOP and canonical proof template (assume nonempty set $C$ of counterexamples $\implies$ take least element $m \in C \implies$ derive contradiction)
  - [ ] Example: Existence of prime factorization via WOP
  - [ ] Example: Sum of first $n$ non-negative integers via WOP
  - [ ] Example: Non-existence of positive integer solutions to Diophantine equations (e.g., $4a^3 + 2b^3 = c^3$)
- [ ] **Equivalence of Ordinary Induction, Strong Induction & WOP**
  - [ ] Understand why all three proof methods are logically equivalent
  - [ ] Convert a WOP proof into an induction/strong induction proof (and vice versa)
  - [ ] **Practice:** `Tutorial_10` (Oct 12 Tutorial 1/7) Q1–Q6; `MfoxAssignSamar.pdf` Assignment 1 Q1–Q8

---

## Module 2: Recursive Data Types & Structural Induction

*Sources: Lectures 5–7 (Oct 13–15), Tutorial 8 Q1–Q3 (Nov 2), Notes pp. 175–188, Textbook Ch. 6, `MfoxAssignSamar.pdf` Assignment 4 Q1–Q3*

- [ ] **Recursive Data Types (RDTs)**
  - [ ] Structure of an RDT: base case(s) + constructor case(s)
  - [ ] Standard examples: non-negative integers $\mathbb{N}$, character strings $A^*$, binary trees, matched parentheses strings, arithmetic expressions, two-player complete-information games
  - [ ] Writing recursive definitions for sets (e.g., $\{2^k 3^m 5^n\}$, $\{(a,b) \in \mathbb{Z}^2 \mid 3 \mid (a-b)\}$)
- [ ] **Recursive Functions & Fast-Growing Hierarchies**
  - [ ] Defining recursive functions over $\mathbb{N}$ and spotting ill-formed / non-terminating definitions (e.g., Collatz-like definitions)
  - [ ] **Ackermann function**: recursive definition and super-primitive-recursive growth rate
  - [ ] **Hyperoperations & Knuth's up-arrow notation**: successor $\to$ addition $\to$ multiplication $\to$ exponentiation $\to$ tetration $\to$ pentation $\to$ hexation
  - [ ] Conceptual awareness: Graham's number and lower bounds on $\text{TREE}(3)$
- [ ] **Structural Induction**
  - [ ] Formal definition and template of structural induction over an RDT
  - [ ] Character strings $A^*$ as an RDT: length, concatenation $s \cdot t$, reversal $\text{rev}(s)$, character count $\#_c(s)$
  - [ ] Proofs via structural induction: $\text{rev}(s \cdot t) = \text{rev}(t) \cdot \text{rev}(s)$, $\#_c(s \cdot t) = \#_c(s) + \#_c(t)$, associativity of concatenation
- [ ] **Arithmetic Expressions (`Aexp`) & Evaluation Models**
  - [ ] Recursive definition of `Aexp` (variables, constants, $+$, $*$, unary $-$)
  - [ ] Recursive definitions of `eval` and substitution `subst` over `Aexp`
  - [ ] **Substitution model vs. Environment model** of evaluation (pros, cons, trace examples)
  - [ ] Equivalence proof between Substitution and Environment models using structural induction
  - [ ] **Practice:** `Tutorial_8` Q1–Q3; `MfoxAssignSamar.pdf` Assignment 4 Q1–Q3

---

## Module 3: Cardinality Extensions & Combinatorics

*Sources: Lectures 8–10 (Oct 21–26), Tutorial 8 Q4–Q9 (Nov 2), Notes pp. 189–202, Textbook Ch. 7.1 & Ch. 14, `MfoxAssignSamar.pdf` Assignment 5 Q1–Q7*

- [ ] **Cardinality Bridge (From Pre-Midsem `cs208.pdf` L2–L5)**
  - [ ] Arrow interpretation of binary relations: total, function, injective, surjective, bijective
  - [ ] Mapping Lemma relating $|A|$ and $|B|$ via surjections, total injections, and bijections (finite & infinite sets)
  - [ ] Explicit bijections $\mathbb{N} \leftrightarrow \mathbb{Q}$: **Cantor pairing function** and **Stern–Brocot tree**
- [ ] **Fundamental Counting Principles**
  - [ ] **Bijection Rule**: translating a problem to bit strings / canonical objects (e.g., 12 ice-creams from 5 flavors $\leftrightarrow$ 16-bit strings with four 1s $\implies \binom{16}{4}$)
  - [ ] Recognizing overcounting pitfalls (distinct vs. indistinguishable slots — why $5^{12}$ fails for unordered ice-cream scoops; distinct vs. indistinguishable meals)
  - [ ] **Sum Rule** (for disjoint sets)
  - [ ] **Product Rule** & **Generalized Product Rule** (e.g., passwords of length 6–8, grid paths)
  - [ ] **Division Rule** ($k$-to-$1$ functions; e.g., circular seating of $n$ people around a round table)
- [ ] **Binomial, Multinomial & Combinatorial Proofs**
  - [ ] Binomial coefficients $\binom{n}{k}$, Binomial Theorem, Pascal's identity & Pascal's triangle
  - [ ] Multinomial coefficients $\binom{n}{k_1, k_2, \dots, k_m}$ and Multinomial Theorem
  - [ ] **Combinatorial proofs** (double counting / story proofs — e.g., symmetry $\binom{n}{r}=\binom{n}{n-r}$, Vandermonde's identity)
- [ ] **Pigeonhole Principle**
  - [ ] Standard Pigeonhole Principle & Generalized Pigeonhole Principle ($\ge \lceil n/m \rceil$ and $\le \lfloor n/m \rfloor$ Dirichlet box principle)
  - [ ] Classic applications: subset-sum with equal sums, hairs-on-heads, pairs differing by $2$, contiguous subsequence divisible by $100$
- [ ] **Inclusion–Exclusion Principle**
  - [ ] Formula for 2, 3, and $n$ sets ($|\bigcup_{i=1}^n S_i|$) and indicator-set / binomial-sum proof
  - [ ] Applications: divisibility counts, forbidden digit/pattern counts (e.g., integers in $[1, 10^9]$ containing digit 1, avoiding patterns `60`, `04`, `42`)
  - [ ] **Practice:** `Tutorial_8` Q4–Q9; `MfoxAssignSamar.pdf` Assignment 4 Q6 & Assignment 5 Q1–Q7

---

## Module 4: Integer Functions, Sums, Products & Asymptotics

*Sources: Lectures 11–13 (Oct 27–29), Notes pp. 203–208, Textbook Ch. 13, `MfoxAssignSamar.pdf` Assignment 4 Q4–Q8 & Assignment 5 Q8–Q9*

- [ ] **Integer Functions (`floor`, `ceil`, `mod`)**
  - [ ] Definitions of $\lfloor x \rfloor$, $\lceil x \rceil$, fractional part $\{x\} = x - \lfloor x \rfloor$, and $x \bmod y = x - y\lfloor x/y \rfloor$ (including negative $x$ or $y$)
  - [ ] Core inequalities & identities: $\lfloor -x \rfloor = -\lceil x \rceil$, $\lfloor x+n \rfloor = \lfloor x \rfloor + n$ ($n \in \mathbb{Z}$), characterizations ($n \le x < n+1$), bit-length $\lfloor \lg n \rfloor + 1 = \lceil \lg(n+1) \rceil$
  - [ ] Nested floor/ceiling identities: $\lfloor \sqrt{\lfloor x \rfloor} \rfloor = \lfloor \sqrt{x} \rfloor$, $\lceil \sqrt{\lceil x \rceil} \rceil = \lceil \sqrt{x} \rceil$, $\lfloor f(x) \rfloor = \lfloor f(\lfloor x \rfloor) \rfloor$ criterion, $\lfloor (x+m)/n \rfloor = \lfloor (\lfloor x \rfloor + m)/n \rfloor$
- [ ] **Evaluating & Bounding Series Sums**
  - [ ] **Perturbation method** for closed-form sums (geometric series, $\sum i x^i$, $\sum (-1)^{n-k} k^2$)
  - [ ] **Integral Method** for upper & lower bounds on weakly increasing / weakly decreasing functions
  - [ ] Example: Upper and lower bounds on $\sum_{i=1}^n \sqrt{i} = \Theta(n^{3/2})$
  - [ ] **Harmonic numbers** $H_n = \sum_{k=1}^n \frac{1}{k}$ and bounds $\frac{1}{n} + \ln n \le H_n \le \ln n + 1$
  - [ ] **Multiple sums & swapping summation order** (e.g., $\sum_{k=1}^n H_k = (n+1)H_n - n$)
- [ ] **Iverson's Bracket**
  - [ ] Definition $[P]$ ($1$ if $P$ is true, $0$ otherwise) and manipulating summation limits
  - [ ] Computing exact closed form for $\sum_{0 \le k < n} \lfloor \sqrt{k} \rfloor$
  - [ ] Using $\sum \lfloor \sqrt{k} \rfloor$ to get a tighter lower bound on $\sum \sqrt{k}$ than the Integral Method
- [ ] **Products & Factorial Bounds**
  - [ ] Converting products to sums via logarithms: $\ln\left(\prod f(i)\right) = \sum \ln f(i)$
  - [ ] Bounding $n!$ via integral of $\ln x$ and **Stirling's approximation** ($n! \sim \sqrt{2\pi n}(n/e)^n$, error bounds)
- [ ] **Asymptotic Notation** *(Appears in Lecture 16, Textbook Ch. 13.7, and `MfoxAssignSamar.pdf` Assignment 5 Q8–Q9)*
  - [ ] Formal definitions of $O(g)$, $\Omega(g)$, $\Theta(g)$, and $\sim$ (asymptotic equivalence)
  - [ ] Finding witnesses $(c, n_0)$ to prove $f = O(g)$ and disproving false asymptotic claims (e.g., $(n+1)!$ vs $n!$)
  - [ ] **Practice:** `MfoxAssignSamar.pdf` Assignment 4 Q4, Q5, Q7, Q8 & Assignment 5 Q8, Q9

---

## Module 5: Recurrence Relations

*Sources: Lectures 14–16 (Nov 3–5), Tutorial 9 Q1 (Nov 12), Notes pp. 209–214, Textbook Ch. 21, `MfoxAssignSamar.pdf` Assignment 6 Q1*

- [ ] **Formulating & Solving Basic Recurrences**
  - [ ] Translating recursive algorithms/problems into recurrences + induction verification
  - [ ] **Josephus problem**: recurrence $J(1)=1, J(2n)=2J(n)-1, J(2n+1)=2J(n)+1$ and closed form $J(2^m+\ell) = 2\ell + 1$
  - [ ] **Guess-and-Verify** method (pattern spotting $\to$ proof by induction) — Tower of Hanoi ($T_n = 2T_{n-1}+1$)
  - [ ] **Expansion / Plug-and-Chug** method — Merge Sort ($T_n = 2T_{n/2} + n - 1$) and general divide-and-conquer recurrences
- [ ] **Linear Recurrences**
  - [ ] **Homogeneous linear recurrences**: characteristic polynomial, distinct roots (Fibonacci & Binet's formula), repeated roots of multiplicity $k$ ($r^n, nr^n, \dots, n^{k-1}r^n$)
  - [ ] **Inhomogeneous linear recurrences**: general solution = homogeneous + particular solution
  - [ ] Method of undetermined coefficients for particular solutions ($g(n) = c$, polynomial, exponential $a^n$; modified Tower of Hanoi where move cost depends on disk size)
- [ ] **Divide-and-Conquer Recurrences**
  - [ ] **Akra–Bazzi Theorem & Formula**:
    - Form $T(x) = \sum_{i=1}^k a_i T(b_i x + h_i(x)) + g(x)$ (verify $a_i > 0$, $b_i \in (0,1)$, $|h_i(x)| = O(x/\log^2 x)$, growth condition on $g$)
    - Solve $\sum_{i=1}^k a_i b_i^p = 1$ for $p$ and evaluate $T(n) = \Theta\left(n^p\left(1 + \int_1^n \frac{g(u)}{u^{p+1}}\,du\right)\right)$
    - Why boundary conditions and $\lfloor \cdot \rfloor / \lceil \cdot \rceil$ perturbations $h_i(n)$ don't affect asymptotic bounds
  - [ ] **Master Theorem** as a special-case corollary of Akra–Bazzi (all 3 cases)
  - [ ] **Big Picture**: comparing how the number of subproblems vs. subproblem size affects linear & divide-and-conquer asymptotic behavior
  - [ ] **Practice:** `Tutorial_9` Q1(a)–(c); `MfoxAssignSamar.pdf` Assignment 6 Q1(a)–(c)

---

## Module 6: Generating Functions

*Sources: Lectures 17–19 (Nov 9–11), Tutorial 9 Q2–Q5 (Nov 12), Notes pp. 215–218, Textbook Ch. 15, `MfoxAssignSamar.pdf` Assignment 6 Q2–Q5*

- [ ] **Ordinary Generating Functions (OGFs) Basics**
  - [ ] Sequence $(a_0, a_1, \dots) \leftrightarrow F(x) = \sum_{n=0}^\infty a_n x^n$ and coefficient extractor $[x^n]F(x)$
  - [ ] Core closed-form identities: $\frac{1}{1-x}$, $\frac{1}{1-ax}$, $\frac{1}{(1-x)^2}$, $\frac{1}{(1-x)^k} = \sum \binom{n+k-1}{n} x^n$, $(1+x)^m$, finite sums $\frac{1-x^{k+1}}{1-x}$, even/odd powers $\frac{1}{1-x^2}$
  - [ ] Prefix-sum trick: if $A(x)$ generates $(a_n)$, then $\frac{A(x)}{1-x}$ generates $\left(\sum_{k=0}^n a_k\right)$
- [ ] **Convolution Rule & Counting Applications**
  - [ ] Product of GFs = convolution: $[x^n](A(x)B(x)) = \sum_{k=0}^n a_k b_{n-k}$
  - [ ] Modeling constrained selection problems (e.g., 87 ice-creams / "Super Sam's mishaps" with parity, multiple, and upper-bound constraints)
  - [ ] Deriving the Binomial Theorem via convolution / product of $(1+x)$ factors
- [ ] **Partial Fractions Decomposition**
  - [ ] Expressing rational OGFs $P(x)/Q(x)$ as sums of partial fractions
  - [ ] Handling distinct roots $\frac{c_i}{1-\alpha_i x}$ and repeated roots $\frac{c}{(1-\alpha x)^r}$ to extract closed-form $[x^n]$
- [ ] **Solving Linear Recurrences via Generating Functions**
  - [ ] Homogeneous recurrences (e.g., Fibonacci sequence)
  - [ ] Non-homogeneous recurrences (e.g., Tower of Hanoi after establishing $T_n = 2T_{n-1}+1$ via upper & lower bounds; ViralTube / $r_n = 7r_{n-1} + n + 1$)
- [ ] **Formal Power Series (Ring of Power Series)**
  - [ ] Treating generating functions algebraically even when coefficients diverge (e.g., $n!$ and $n \cdot n!$)
  - [ ] Deriving iterative identities (e.g., $n! = 1 + \sum_{i=1}^n (i-1)(i-1)!$) via power-series manipulation
  - [ ] **Practice:** `Tutorial_9` Q2–Q5; `MfoxAssignSamar.pdf` Assignment 6 Q2–Q5

---

## Module 7: Graph Theory & Graph Coloring

*Sources: Lectures 20–21 in `MFOCS_Notes_Aug-Nov_2026.pdf` (Nov 17–18, pp. 219–221 — Class 23 was blank in `Class Summary.md`), Textbook Ch. 11 (and Ch. 9.6/9.9), `MfoxAssignSamar.pdf` Assignment 7*

### Part A: Directly Covered in Nov 17–18 Lecture Notes (pp. 219–221)

- [ ] **Graph Fundamentals & Degrees**
  - [ ] Undirected simple graphs vs. directed graphs; $G = (V, E)$, $|V| \ge 1$, $|E| \ge 0$, adjacent vertices, $\deg(v)$
  - [ ] Average degree across two partitions $X, Y$: $\text{avg deg}(X) = \frac{|Y|}{|X|} \text{avg deg}(Y)$
  - [ ] **Handshaking Theorem**: $\sum_{v \in V(G)} \deg(v) = 2|E(G)|$ (and parity corollary)
- [ ] **Standard Graph Families & Isomorphism**
  - [ ] Complete graph $K_n$ ($|E| = \binom{n}{2} = \frac{n(n-1)}{2}$), path/line graph, cycle graph $C_n$
  - [ ] **Graph Isomorphism**: definition ($\exists$ bijection $f: V(G) \to V(H)$ preserving adjacency), proving isomorphism is an equivalence relation, checking/disproving isomorphism (e.g., $C_5$ vs. 5-pointed star)
- [ ] **Graph Coloring & Bipartite Graphs**
  - [ ] $k$-colorable graphs and **chromatic number** $\chi(G)$
  - [ ] Key chromatic numbers: $\chi(C_{\text{even}}) = 2$, $\chi(C_{\text{odd}}) = 3$, $\chi(K_n) = n$
  - [ ] **Bipartite graphs**: definition and $\chi(G) = 2$ (for bipartite graphs with at least one edge)
  - [ ] Computational hardness note: $k$-coloring / SAT as NP-complete; distributed & online graph coloring
  - [ ] **Degree-Bound Coloring Theorem**: Any graph with maximum degree $\Delta \le n$ is $(n+1)$-colorable — **proof by induction on the number of vertices $|V|$**

### Part B: Additional Topics in `MfoxAssignSamar.pdf` Assignment 7 *(Confirm if taught in classes after Nov 18)*

- [ ] **Connectivity & Graph Complements** (`Assignment 7` Q1)
  - [ ] Graph complement $G'$; proving if $G$ is disconnected then $G'$ is connected
  - [ ] Connected graph on $n$ vertices has $\ge n-1$ edges; $> \binom{n-1}{2}$ edges implies $G$ is connected
- [ ] **Graph Coloring Scheduling Application** (`Assignment 7` Q2)
  - [ ] Modeling conflict graphs and finding minimum time slots via $\chi(G)$
- [ ] **Walks, Paths & Hamiltonian Cycles** (`Assignment 7` Q3)
  - [ ] Counting length-$n$ walks/paths in $K_n$ (with repetition, no consecutive edge reuse, Hamiltonian cycles) & TSP brute-force timing
- [ ] **Weighted Graphs & Prim's MST** (`Assignment 7` Q4)
  - [ ] Step-by-step Minimum Spanning Tree construction using Prim's algorithm
- [ ] **Order Relations & Hasse Diagrams (Pre-Midsem Extension)** (`Assignment 7` Q5; Textbook Ch. 9.6, 9.9)
  - [ ] Drawing Hasse diagrams for posets (divisibility, power-set inclusion)
  - [ ] Proving product order $\mu$ on $S \times T$ is a partial order

---

## Final Pre-Exam Consolidation Pass

- [ ] Re-solve all problems from `Tutorial_10` (Oct 12), `Tutorial_8` (Nov 2), and `Tutorial_9` (Nov 12) without notes
- [ ] Work through `MfoxAssignSamar.pdf` Assignments 1, 4, 5, 6, and relevant parts of Assignment 7 under timed conditions
- [ ] Review proof templates side-by-side: Ordinary Induction vs. Strong Induction vs. WOP vs. Structural Induction
- [ ] Review formula sheet: Integer functions, Harmonic & integral bounds, Akra–Bazzi / Master Theorem, core OGF series & partial fractions, Handshaking & coloring bounds
