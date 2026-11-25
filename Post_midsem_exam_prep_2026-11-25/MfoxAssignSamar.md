# CS208 — Problem Set Compendium

**Mathematical Foundations of Computer Science**  
**Seven assignments · Complete collection**

Source: [MfoxAssignSamar.pdf](../Study_material_after_mid_sems/MfoxAssignSamar.pdf).

This Markdown conversion contains all seven assignments and all 54 numbered questions. Mathematical notation is written in LaTeX. PDF page boundaries are identified below; repeated running headers, footers, and the watermark are omitted. The grading rubric is retained once and referenced where it appears in the source. Apparent source typos are preserved and explained in the conversion notes at the end.

## Front matter — PDF pages 1–2

PDF page 1 is the cover: “CS208 / Course Compendium”, “Problem Set Compendium”, “Seven assignments · Complete collection”, and “Mathematical Foundations of Computer Science”.

PDF page 2 contains the following contents table.

| Assignment | Topic | PDF starting page |
| --- | --- | --- |
| [1](#assignment-1) | Proofs & Induction | 3 |
| [2](#assignment-2) | Logic & Boolean Algebra | 5 |
| [3](#assignment-3) | Sets, Functions & Cardinality | 7 |
| [4](#assignment-4) | Strings, Recurrences & Counting | 8 |
| [5](#assignment-5) | Counting & Asymptotics | 9 |
| [6](#assignment-6) | Recurrences & Generating Functions | 10 |
| [7](#assignment-7) | Graphs & Order Relations | 12 |

<a id="grading-rubric"></a>
## Grading rubric

**Note:** Each question will be graded as per the following criteria:

- (a) 5 — Thorough understanding of the topic and conceptual clarity.
- (b) 4 — Adequate understanding of the topic and conceptual clarity.
- (c) 3 — Some understanding of the topic and conceptual clarity.
- (d) 2 or 1 — Poor understanding of the topic and messed up concepts.

This note appears at the start of Assignments 1–6. It does not appear at the start of Assignment 7.

<a id="assignment-1"></a>
## Assignment 1 — Proofs & Induction

**PDF page 3.** Mathematical Foundations of CS (CS208). The [grading rubric](#grading-rubric) applies as printed in the source.

<a id="a1-q1"></a>
### Question 1

Identify where the bug is in the following bogus proof.

**Bogus Claim:** If $a$ and $b$ are two equal real numbers, then $a=0$.

**Bogus Proof:**

$$
\begin{aligned}
a &= b \\
a^2 &= ab \\
a^2-b^2 &= ab-b^2 \\
(a-b)(a+b) &= (a-b)b \\
a+b &= b \\
a &= 0.
\end{aligned}
$$

<a id="a1-q2"></a>
### Question 2

It’s known that the Arithmetic Mean is at least as large as the Geometric Mean, namely,

$$
\frac{a+b}{2}\ge\sqrt{ab}
$$

for all nonnegative real numbers $a$ and $b$. A student came up with the following proof for this fact. Is it correct? If not, then what is your objection and how would you fix it?

**Purported Proof:**

$$
\begin{aligned}
\frac{a+b}{2} &\mathrel{\stackrel{?}{\ge}} \sqrt{ab} \\
a+b &\mathrel{\stackrel{?}{\ge}} 2\sqrt{ab} \\
a^2+2ab+b^2 &\mathrel{\stackrel{?}{\ge}} 4ab \\
a^2-2ab+b^2 &\mathrel{\stackrel{?}{\ge}} 0 \\
(a-b)^2 &\ge 0 \quad\text{which is known to be true.}
\end{aligned}
$$

<a id="a1-q3"></a>
### Question 3

Using proof by contradiction, prove that for any $n>0$, if $a^n$ is even, then $a$ is even.

<a id="a1-q4"></a>
### Question 4

Prove that $\log_4 6$ is irrational.

**PDF page 4 — Assignment 1 continued.**

<a id="a1-q5"></a>
### Question 5

Use Well Ordering Principle to prove that:

- (a) there is no solution over the positive integers to the equation $4a^3+2b^3=c^3$.
- (b) any integer greater than or equal to 8 can be represented as the sum of nonnegative integer multiples of 3 and 5.

<a id="a1-q6"></a>
### Question 6

Prove by induction on $n$ that

$$
1+r+r^2+\cdots+r^n=\frac{r^{n+1}-1}{r-1}
$$

for all $n\in\mathbb N$ and numbers $r\ne1$.

Remember to formally:

- (a) Declare proof by induction.
- (b) Identify the induction hypothesis $P(n)$.
- (c) Establish the base case.
- (d) Prove that $P(n)\implies P(n+1)$.
- (e) Conclude that $P(n)$ holds for all $n\ge1$.

as in the five part template.

<a id="a1-q7"></a>
### Question 7

The $n$-th Fibonacci number is defined by the equations:

$$
\begin{aligned}
F(0)&:=0,\\
F(1)&:=1,\\
F(n)&:=F(n-1)+F(n-2),\qquad n\ge2.
\end{aligned}
$$

Prove by induction that for all $n\ge1$,

$$
F(n-1)\cdot F(n+1)-F(n)^2=(-1)^n.
$$

<a id="a1-q8"></a>
### Question 8

You are given envelopes, numbered $0,1,\ldots,n-1$. Envelope 0 contains $2^0=1$ rupees. Envelope 1 contains $2^1=2$ rupees, …, and Envelope $n-1$ contains $2^{n-1}$ rupees. Let $P(n)$ be the assertion that:

> For all nonnegative integers $k<2^n$, there is a subset of the $n$ envelopes whose contents total to exactly $k$ rupees.

Prove by induction that $P(n)$ holds for all integers $n\ge1$.

<a id="assignment-2"></a>
## Assignment 2 — Logic & Boolean Algebra

**PDF page 5.** Mathematical Foundations of CS (CS208). The [grading rubric](#grading-rubric) applies as printed in the source.

<a id="a2-q1"></a>
### Question 1

A group of $n\ge1$ people can be divided into teams, each containing either 4 or 7 people. What are the possible values of $n$? Use strong induction to prove that your answer is correct.

<a id="a2-q2"></a>
### Question 2

Use strong induction to prove that $n\le3^{n/3}$ for every integer $n\ge0$.

<a id="a2-q3"></a>
### Question 3

From the following, choose correct negation of the statement: “The river is shallow or polluted.” Provide a justification of your choice.

- (a) It is false that the river is shallow or polluted.
- (b) The river is neither shallow nor polluted.
- (c) The river is deep and unpolluted.
- (d) The river is not shallow or not polluted.

<a id="a2-q4"></a>
### Question 4

Rewrite each of the following statements in the form “If A, then B.”

- (a) Healthy plant growth follows from sufficient water.
- (b) Increased availability of information is a necessary condition for further technological advances.
- (c) Errors were introduced only if there was a modification of the program.
- (d) Fuel savings implies good insulation or storm windows throughout.

<a id="a2-q5"></a>
### Question 5

Four machines, A, B, C, and D, are connected on a computer network. It is feared that a computer virus may have infected the network. Your security team makes the following statements:

- (a) If D is infected, then so is C.
- (b) If C is infected, then so is A.
- (c) If D is clean, then B is clean but C is infected.
- (d) If A is infected, then either B is infected or C is clean.

Assuming that these statements are all true, what can you conclude about infection of machines A, B, C, and D? Explain your reasoning.

<a id="a2-q6"></a>
### Question 6

Using propositional logic, prove that the statement

$$
A\land(B\to C)\land[(A\land B)\to(D\lor C)]\land B\to D
$$

is valid.

**PDF page 6 — Assignment 2 continued.**

<a id="a2-q7"></a>
### Question 7

Use a truth table to verify that $A\to(B\to C)\leftrightarrow(A\land B)\to C$ is valid.

<a id="a2-q8"></a>
### Question 8

Which of the following statements expresses the negation of “Everybody loves somebody sometime”? Justify your answer by first writing the predicate formula for the original statement and then negating it.

- (a) Everybody hates somebody sometime.
- (b) Somebody loves everybody all the time.
- (c) Everybody hates everybody all the time.
- (d) Somebody hates everybody all the time.

<a id="a2-q9"></a>
### Question 9

Consider the predicate formula $(\forall x)[P(x)\lor Q(x)]\to(\forall x)P(x)\lor(\forall x)Q(x)$. Is it valid?

<a id="a2-q10"></a>
### Question 10

Prove the following properties of propositional algebra. Justify each step.

- (a) $x+y'=x+(x'\cdot y+x\cdot y)'$.
- (b) $(x+y)'\cdot z+x'\cdot y\cdot z=x'\cdot z$.
- (c) $(x\cdot y')+(y\cdot z')+(z\cdot x')=(x'\cdot y)+(y'\cdot z)+(z'\cdot x)$.

<a id="assignment-3"></a>
## Assignment 3 — Sets, Functions & Cardinality

**PDF page 7.** Mathematical Foundations of CS (CS208). The [grading rubric](#grading-rubric) applies as printed in the source.

<a id="a3-q1"></a>
### Question 1

Prove $A\cup(B\cap C)=(A\cup B)\cap(A\cup C)$ for all sets $A$, $B$, and $C$, by using a chain of iff’s to show that $x\in A\cup(B\cap C)$ IFF $x\in(A\cup B)\cap(A\cup C)$ for all elements $x$.

<a id="a3-q2"></a>
### Question 2

Let $A$ and $B$ be sets. Prove that:

- (a) $\operatorname{pow}(A\cap B)=\operatorname{pow}(A)\cap\operatorname{pow}(B)$.
- (b) $(\operatorname{pow}(A)\cup\operatorname{pow}(B))\subseteq\operatorname{pow}(A\cup B)$.

<a id="a3-q3"></a>
### Question 3

Prove that for any sets $A$, $B$, $C$ and $D$, if the Cartesian products $A\times B$ and $C\times D$ are disjoint, then either $A$ and $C$ are disjoint or $B$ and $D$ are disjoint.

<a id="a3-q4"></a>
### Question 4

For each of the following real-valued functions on the real numbers, indicate whether it is a bijection, a surjection but not a bijection, an injection but not a bijection, or neither an injection nor a surjection.

- (a) $x\mapsto x^2$.
- (b) $x\mapsto x^3$.
- (c) $x\mapsto\sin x$.
- (d) $x\mapsto x\sin x$.
- (e) $x\mapsto e^x$.

<a id="a3-q5"></a>
### Question 5

Give an example of a relation $R$ that is a total injective function from a set $A$ to itself but is not a bijection.

<a id="a3-q6"></a>
### Question 6

Let $f:A\to B$ and $g:B\to C$ be function.

- (a) Prove that if the composition $g\circ f$ is a bijection, then $f$ is a total injection and $g$ is a surjection.
- (b) Show there is a total injection $f$ and a bijection, $g$, such that $g\circ f$ is not a bijection.

<a id="a3-q7"></a>
### Question 7

Let $X=\{a,b\}$. If $F:X\to X$, then list all partial functions $F$, all functions $F$, all injective functions $F$, and all surjective functions $F$.

<a id="a3-q8"></a>
### Question 8

Give an example of two uncountable sets $A$ and $B$ such that there is no bijection between them.

<a id="a3-q9"></a>
### Question 9

For each of the following sets, indicate whether it is finite, countably infinite, or uncountable. Justify your answers.

- (a) The set of even integers greater than $10^{100}$.
- (b) The power set of integer interval $[10,\ldots,10^{10}]$.
- (c) $U\cup D$, where $U$ is an uncountable set and $D$ be a countably infinite set.
- (d) $U-D$, where $U$ and $D$ are as in part (d).

<a id="assignment-4"></a>
## Assignment 4 — Strings, Recurrences & Counting

**PDF page 8.** Mathematical Foundations of CS (CS208). The [grading rubric](#grading-rubric) applies as printed in the source.

<a id="a4-q1"></a>
### Question 1

The *reversal* of a string is the string written backwards, for example, $\operatorname{rev}(abcd)=dcba$.

- (a) Give a simple recursive definition of $\operatorname{rev}(s)$ based on the recursive definition of $s\in A^\star$ and of concatenation operation discussed in the class.
- (b) Prove that $\operatorname{rev}(s\cdot t)=\operatorname{rev}(t)\cdot\operatorname{rev}(s)$ for all strings $s,t\in A^\star$. You may assume that concatenation is associative: $(r\cdot s)\cdot t=r\cdot(s\cdot t)$ for all strings $r,s,t\in A^\star$. If you are not convinced of associativity of concatenation, then you may prove it by structural induction on the recursive definition of string discussed in the class.

<a id="a4-q2"></a>
### Question 2

Provide simple recursive definitions of the following sets:

- (a) $S=\{2^k3^m5^n\in\mathbb N\mid k,m,n\in\mathbb N\}$.
- (b) $S=\{2^k3^{2k+m}5^{m+n}\in\mathbb N\mid k,m,n\in\mathbb N\}$.
- (c) $S=\{(a,b)\in\mathbb Z^2\mid(a-b)\text{ is a multiple of }3\}$.

<a id="a4-q3"></a>
### Question 3

Define the number $\#_c(s)$ of occurrences of the character $c\in A$ in the string $s$ recursively on the definition of $s\in A^\star$:

**Base case:** $\#_c(\lambda):=0$.

**Constructor case:**

$$
\#_c(\langle a,s\rangle)=
\begin{cases}
\#_c(s),&a\ne c,\\
1+\#_c(s),&a=c.
\end{cases}
$$

Prove by structural induction that for all $s,t\in A^\star$ and $c\in A$,

$$
\#_c(s\cdot t)=\#_c(s)+\#_c(t).
$$

<a id="a4-q4"></a>
### Question 4

Evaluate the sums

$$
S_n=\sum_{k=0}^n(-1)^{n-k},\qquad
T_n=\sum_{k=0}^n(-1)^{n-k}k,\qquad
U_n=\sum_{k=0}^n(-1)^{n-k}k^2
$$

by the perturbation method, assuming that $n\ge0$.

<a id="a4-q5"></a>
### Question 5

Evaluate the sum $\displaystyle\sum_{k=1}^n\frac{(-1)^k k}{4k^2-1}$.

<a id="a4-q6"></a>
### Question 6

Prove the Dirichlet box principle: if $n$ objects are put into $m$ boxes, some box must contain $\ge\lceil n/m\rceil$ objects, and some box must contain $\le\lfloor n/m\rfloor$.

<a id="a4-q7"></a>
### Question 7

Show that the expression

$$
\left\lceil\frac{2x+1}{2}\right\rceil
-\left\lceil\frac{2x+1}{4}\right\rceil
+\left\lfloor\frac{2x+1}{4}\right\rfloor
$$

is always either $\lfloor x\rfloor$ or $\lceil x\rceil$. In what circumstances does each case arise?

<a id="a4-q8"></a>
### Question 8

Prove or disprove: $\lfloor x\rfloor+\lfloor y\rfloor+\lfloor x+y\rfloor\le\lfloor2x\rfloor+\lfloor2y\rfloor$.

<a id="assignment-5"></a>
## Assignment 5 — Counting & Asymptotics

**PDF page 9.** Mathematical Foundations of CS (CS208). The [grading rubric](#grading-rubric) applies as printed in the source.

<a id="a5-q1"></a>
### Question 1

How many of the billion numbers in the integer interval $[1,\ldots,10^9]$ contain the digit 1?

<a id="a5-q2"></a>
### Question 2

There are 20 books arranged in a row on a shelf. Describe a bijection between ways of choosing 6 of these books so that no two adjacent books are selected, and 15-bit strings with exactly 6 ones.

<a id="a5-q3"></a>
### Question 3

How many ways are there to pick three distinct numbers from the integer interval $[1,\ldots,15]$ such that the sum of the numbers is divisible by three?

<a id="a5-q4"></a>
### Question 4

Suppose $2n+1$ numbers are selected from $\{1,2,\ldots,4n\}$. Using the Pigeonhole Principle, show that there must be two selected numbers whose difference is 2. Clearly indicate the pigeons, holes, and rules for assigning a pigeon to a hole.

<a id="a5-q5"></a>
### Question 5

Let $k_1,k_2,\ldots,k_{101}$ be a sequence of 101 integers. A sequence $k_{m+1},k_{m+2},\ldots,k_n$, where $0\le m<n\le101$ is called a subsequence. Prove that there is a subsequence whose elements sum to a number divisible by 100. (Hint: you may use Pigeonhole Principle.)

<a id="a5-q6"></a>
### Question 6

The working days in the next year can be numbered $1,2,3,\ldots,300$. I would like to avoid as many as possible.

- On even-numbered days, I’ll say I’m sick.
- On days that are a multiple of 3, I’ll say I was stuck in traffic.
- On days that are a multiple of 5, I’ll refuse to come out from under the blankets.

In total, how many work days will I avoid in the coming year? (Hint: you may use Inclusion-Exclusion Principle.)

<a id="a5-q7"></a>
### Question 7

Give a combinatorial proof (proof using combinatorial argument) for the identity:

$$
\sum_{r-0}^n\binom nr\binom m{k-r}=\binom{n+m}k.
$$

> Source notation: the printed lower summation limit is $r-0$. See the conversion notes.

<a id="a5-q8"></a>
### Question 8

Either prove or disprove each of the following statements:

- (a) $n!=O((n+1)!)$.
- (b) $(n+1)!=O(n!)$.
- (c) $n!=\Theta((n+1)!)$.

<a id="a5-q9"></a>
### Question 9

For each pair of functions below, indicate the smallest $c\in\mathbb Z^+$, and for that smallest $c$, the smallest $n_0\in\mathbb Z^+$, that would establish $f=O(g)$ as per the definition of “big-Oh” introduced in the class. If there is no such $c$, then write $\infty$.

- (a) $f(n)=\frac12n^2$, $g(n)=n$.
- (b) $f(n)=n$, $g(n)=n\ln n$.
- (c) $f(n)=2^n$, $g(n)=n^4\ln n$.
- (d) $f(n)=3\sin\left(\frac{\pi(n-1)}{100}\right)+2$, $g(n)=0.2$.

<a id="assignment-6"></a>
## Assignment 6 — Recurrences & Generating Functions

**PDF page 10.** Mathematical Foundations of CS (CS208). The [grading rubric](#grading-rubric) applies as printed in the source.

<a id="a6-q1"></a>
### Question 1

For the following divide-and-conquer recurrences, find a closed form expression for $T(n)$ using Plug-and-Chug method, and asymptotic bounds using Master Theorem and Akra-Bazzi formula. For each recurrence, $T(1)=1$ and $T(n)=\Theta(1)$ for all constant $n$. For Akra-Bazzi formula, state the value of $p$ you get for each recurrence and also state the values of the $a_i$, $b_i$, and $h_i(n)$ for each recurrence.

- (a) $T(n)=4T(\lfloor n/3\rfloor)+n^2$.
- (b) $T(n)=T(\lceil n/4\rceil)+T(\lfloor3n/4\rfloor)+n$.
- (c) $T(n)=2T(\lfloor n/4+\sqrt n\rfloor)+1$.

<a id="a6-q2"></a>
### Question 2

**(a)** Let

$$
S(x)=\frac{x^2+x}{(1-x)^3}.
$$

What is the coefficient of $x^n$ in the generating function series for $S(x)$?

**(b)** Explain why $S(x)/(1-x)$ is the generating function for the sums of squares. That is, the coefficient of $x^n$ in the series for $S(x)/(1-x)$ is $\sum_1^n k^2$.

**(c)** Use the above two parts to prove that

$$
\sum_1^n k^2=\frac{n(n+1)(2n+1)}6.
$$

<a id="a6-q3"></a>
### Question 3

Everyday in the life of Super Sam[^1] is a potential disaster:

- (a) Sam may or may not wear his t-shirt inside out.
- (b) Sam may or may not hurt his back while trying to jump down three steps on his office stairs.
- (c) Sam’s knee hits his coffee-table zero or more times.
- (d) Sam tells a joke on which no one but only him laughs and this happens an even number of times.

Let $T_n$ be the number of different combinations of $n$ mishaps Sam can suffer in one day. For example, $T_3=7$, because there are seven possible combinations of three mishaps.

- (a) Express the generating function $T(x)=T_0+T_1x+T_2x^2+\cdots$ as a quotient of polynomials.
- (b) Express $T(x)$ in terms of partial fractions.
- (c) Write a closed form expression for $T_n$.

[^1]: Any resemblance to any person known to you who spends a lot of time in front of blackboard is purely coincidental.

**PDF page 11 — Assignment 6 continued.**

<a id="a6-q4"></a>
### Question 4

Define the sequence $r_0,r_1,r_2,\ldots$ recursively by the rule that $r_0:=1$ and

$$
r_n:=7r_{n-1}+n+1,\qquad n>0.
$$

Let $R(x):=\sum_0^\infty r_nx^n$ be the generating function of this sequence. Express $R(x)$ as a quotient of polynomials or products of polynomials.

<a id="a6-q5"></a>
### Question 5

Satyam Shukla[^2] sends out a video that spreads like wildfire over ViralTube network. On the day of the release — call it day zero — and the day following — call it day one — the video does not receive any hits. However, starting with day two, the number of hits $r_n$ can be expressed as seven times the number of hits on the previous day, four times the number of hits the day before that, and the number of days that has passed since the release of the video plus one. So, for example on day 2, there will be $7\times0+4\times0+3=3$ hits.

- (a) Give a linear a recurrence for $r_n$.
- (b) Express the generating function $R(x):=\sum_0^\infty r_nx^n$ as a quotient of polynomials or products of polynomials.

[^2]: Any resemblance to any person known to you who shares photos and videos is purely coincidental.

<a id="assignment-7"></a>
## Assignment 7 — Graphs & Order Relations

**PDF page 12.** Mathematical Foundations of CS (CS208).

<a id="a7-q1"></a>
### Question 1

- (a) Prove that in any simple graph $G$ with at least two vertices, if $G$ is not connected, then $G'$ is connected. The graph $G'$ is called the complement of $G$ and is defined as a simple graph with the same number of vertices as $G$, where vertices $x-y$ are adjacent in $G'$ if and only if they are not adjacent in $G$.
- (b) Prove that a simple, connected graph with $n$ vertices has at least $n-1$ edges.
- (c) Using the results in parts (a) and (b), prove that a simple graph with $n$ vertices ($n\ge2$) and more than $C(n-1,2)$ edges is connected.

<a id="a7-q2"></a>
### Question 2

Five students are visiting seven professors (labeled A through G) for their project evaluations on the same day. The professors the five students must see are:

| Student | Professors |
| --- | --- |
| I | A, B, D |
| II | B, C, F |
| III | A, B, D, G |
| IV | E, G |
| V | D, E, F |

Each professor will be available to meet with students for one hour. What is the minimum number of time slots that must be used to set up the one-hour meetings so that no student has a conflict? What if Student III discovers that she does not need to see B and Student V discovers that he does not need to see D?

<a id="a7-q3"></a>
### Question 3

Consider a simple, complete graph with $n$ nodes. Testing for a Hamiltonian cycle by trial and error could be done by selecting a fixed starting node and then generating all possible paths from that node of length $n$.

- (a) How many paths of length $n$ are there if repetition of edges and nodes is allowed?
- (b) How many paths of length $n$ are there if repetition of edges and nodes is allowed but an edge may not be used twice in succession?
- (c) How many paths of length $n$ are there if nodes and edges cannot be repeated except for the starting node? (These are the Hamiltonian circuits.)
- (d) To solve the traveling salesman problem in a weighted graph, assume a fixed starting point at node 1 and generate all possible Hamiltonian cycles of length $n$ to find one with minimum weight. If it takes 0.000001 seconds to generate a single Hamiltonian cycle, how long will this process take in a simple, complete graph with 15 nodes?

<a id="a7-q4"></a>
### Question 4

Consider a simple and weighted graph $G=(V,E)$ with

$$
V=\{1,2,3,4,5,6,7,8\}
$$

$$
\begin{aligned}
E=\{&(1,2;3),(1,3;5),(1,5;8),(1,6;1),\\
&(2,3;2),(2,7;1),(3,4;1),(3,8;2),\\
&(4,5;4),(5,6;6),(5,8;1),(6,7;5),(7,8;1)\},
\end{aligned}
$$

where $(a,b;w)$ denotes an edge between nodes $a$ and $b$ with weight $w$. Construct an MST for this graph using the Prim’s algorithm as discussed in the class. Show step-by-step construction of the MST.

<a id="a7-q5"></a>
### Question 5

**(a)** Draw the Hasse diagram for each of the two partially ordered sets.

- (i) $S=\{1,2,3,5,6,10,15,30\}$, $xRy\leftrightarrow x\text{ divides }y$.
- (ii) $S=\operatorname{pow}(\{1,2,3\})$, $A\rho B\leftrightarrow A\subseteq B$.

**(b)** Let $(S,\rho)$ and $(T,\sigma)$ be two partially ordered sets. A relation $\mu$ on $S\times T$ is defined by

$$
(s_1,t_1)\mu(s_2,t_2)\leftrightarrow s_1\rho s_2\text{ and }t_1\sigma t_2.
$$

Show that $\mu$ is a partial ordering on $S\times T$.

## Conversion notes

- The source questions are reproduced rather than solved or silently repaired. In particular, Assignment 2 Question 6 prints a claim of validity ending in $\to D$; that statement is retained exactly, even though its validity should be checked during study.
- Assignment 3 Question 9(d) literally refers to “part (d)”. The apparent intended reference is part (c), where $U$ and $D$ are defined; the question above preserves the printed reference.
- Assignment 5 Question 7 visually prints $r-0$ below the summation symbol. This appears to be a typo for $r=0$, the usual lower limit in Vandermonde’s identity. The source notation is retained above so that the conversion does not hide the discrepancy.
- Assignment 6 uses shorthand limits such as $\sum_1^n k^2$ and $\sum_0^\infty r_nx^n$ without explicitly writing the index equality. They are retained as printed; the summation variables are $k$ and $n$, respectively.
- Formulas on PDF pages 4, 5, 8, 9, and 10 were checked against rendered source pages. This recovered superscripts, fractions, floor/ceiling brackets, and the numerator $x^2+x$ in Assignment 6 Question 2 that plain extraction can misplace.
