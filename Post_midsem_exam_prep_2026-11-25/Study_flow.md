# CS208 MFOCS: post-midsem study flow

Start with the short prerequisite refresh, then follow the numbered stages. The order puts the tools needed for a topic before that topic: induction before recursive structures, counting and bounds before recurrences, and recurrences before generating functions.

Use [Checklist.md](Checklist.md) to track individual concepts and practice. The complete assignment PDF has been converted to [MfoxAssignSamar.md](MfoxAssignSamar.md), including the assignments that overlap pre-midsem material.

## Scope and sources

The [class summary](../Full_topic_list/2026-2-CS208-MFOCS_%20Class%20Summary.md) records substantive content for Lectures 1–19 and Tutorials 7–9, dated 5 October–12 November 2026. Its Lecture 20 entry on 17 November is blank. The [handwritten notes](../Study_material_after_mid_sems/MFOCS_Notes_Aug-Nov_2026.pdf), PDF pp. 219 and 221, directly establish graph fundamentals and coloring. Those pages do not show dates. Assignment 7 supplies the additional graph/order applications listed in Stage 10.

The [pre-midsem PDF](../Study_material_before_mid_sems/cs208.pdf) already covers sets, functions, cardinality/countability, relations, equivalence classes, partial/total orders, convexity and convex hulls, Carathéodory's theorem, logic, direct proof, contraposition, contradiction, and ordinary induction. We will refresh these when needed. The new explicit bijection constructions and graph/order assignment exercises remain in the plan.

## Learning order

| Stage | Topics we will cover | Why here / completion target |
|---|---|---|
| 0. Prerequisite refresh | Ordinary induction; logic and proof methods; functions, bijections and cardinality; basic posets | Recall the definitions and write a valid induction proof. |
| 1. Stronger proof methods | Proof by cases; Ramsey example; strong induction; well-ordering principle; equivalence of the three induction/WOP methods | Prove prime-factorization existence and the 3 kg/5 kg weight example using the appropriate template. |
| 2. Recursive structures | Recursive data types and functions; structural induction; strings, trees and brackets; `Aexp`, evaluation and substitution; substitution/environment models; fast-growing-function context | Write recursive definitions and prove a string property and the evaluation-model equivalence. |
| 3. Bijections and counting | Arrow interpretation of relations; Cantor pairing; Stern–Brocot tree; bijection, sum, product and division rules; distinguishability; stars and bars; binomial/multinomial coefficients and theorems | Model counting problems without overcounting. |
| 4. Counting proofs | Pigeonhole and generalized pigeonhole; inclusion–exclusion and its proof; combinatorial arguments; Pascal's triangle | Identify the pigeons/holes and intersections; prove an identity by counting two ways. |
| 5. Integer functions, sums and bounds | Floor, ceiling, modulo; summation/product methods; harmonic numbers; swapping summation order; Iverson brackets; square-root sums; factorial bounds; asymptotic notation | Evaluate or bound a sum and justify an asymptotic claim with the definition. |
| 6. Recurrence foundations and linear recurrences | Modelling and initial conditions; Josephus; guess-and-verify; expansion; Hanoi and merge sort; homogeneous and nonhomogeneous linear recurrences; characteristic roots and particular solutions | Obtain a solution and verify it against the recurrence and initial conditions. |
| 7. Divide-and-conquer recurrences | Akra–Bazzi formula/theorem; Master theorem as a corollary; boundary and floor/ceiling effects; number and size of subproblems | Choose an applicable theorem, check its hypotheses, and derive the bound. |
| 8. Generating functions | Ordinary generating functions; coefficient extraction; counting models; products/convolution; partial fractions with distinct/repeated roots; solving recurrences; formal power series and factorial identities | Turn a counting problem or recurrence into algebra and recover its coefficients. |
| 9. Graphs and coloring | Graph definitions and degrees; handshaking; standard graphs; isomorphism; bipartite graphs; chromatic number; degree-bound coloring proof | State definitions precisely and prove the basic degree/coloring results. |
| 10. Graph and order assignment applications | Complements/connectivity and edge bounds; conflict scheduling; walks and Hamiltonian circuits; TSP enumeration; weighted graphs and Prim's MST; Hasse diagrams and product orders | Complete Assignment 7; order definitions are a pre-midsem refresh. |
| 11. Exam consolidation | Mixed proofs, counting, sums, recurrence/GF problems and graph exercises; formula/proof-template recall | Solve a mixed set without notes, then correct and re-solve errors. |

### Brief mathematical context

Alongside Stages 1–2, cover the introductory discussions: Goldbach, Collatz and Pólya conjectures; proof pitfalls; matrix multiplication and Strassen's algorithm; Ramsey numbers; Fermat's last theorem and algebraic geometry; Russell's paradox, *Principia Mathematica*, Gödel incompleteness and Turing undecidability; Ackermann, Knuth arrows, hyperoperations, Graham's number and TREE(3). Aim to explain the ideas and why they appeared in class. The class summary does not specify detailed technical proofs for these discussions.

## Practice map

Question links point to the complete converted compendium. They are exercises, not a solutions file.

Practice is selected by question content rather than assignment title: Assignment 2 Q1–Q2 are strong induction even though its contents-page label is “Logic & Boolean Algebra.” Its later questions and Assignment 3 mainly refresh pre-midsem topics. Final consolidation includes the selected Assignment 1 questions, Assignment 2 Q1–Q2 and Assignments 4–7.

| Stage | Assignment practice | Other class material |
|---|---|---|
| 1 | [Assignment 1](MfoxAssignSamar.md#assignment-1), especially [Q5](MfoxAssignSamar.md#a1-q5) for WOP; [A2 Q1](MfoxAssignSamar.md#a2-q1) and [Q2](MfoxAssignSamar.md#a2-q2) for strong induction; ordinary-proof items are refresh | Tutorial 7, 12 October, stored in `Tutorial_10` |
| 2 | [A4 Q1](MfoxAssignSamar.md#a4-q1), [Q2](MfoxAssignSamar.md#a4-q2), [Q3](MfoxAssignSamar.md#a4-q3) | Tutorial 8 Q1–Q3 |
| 3 | [A5 Q2](MfoxAssignSamar.md#a5-q2), [Q3](MfoxAssignSamar.md#a5-q3), plus the class counting examples | Tutorial 8 Q4–Q6 |
| 4 | [A4 Q6](MfoxAssignSamar.md#a4-q6); [A5 Q1](MfoxAssignSamar.md#a5-q1), [Q4](MfoxAssignSamar.md#a5-q4), [Q5](MfoxAssignSamar.md#a5-q5), [Q6](MfoxAssignSamar.md#a5-q6), [Q7](MfoxAssignSamar.md#a5-q7) | Tutorial 8 Q7–Q9 |
| 5 | [A4 Q4](MfoxAssignSamar.md#a4-q4), [Q5](MfoxAssignSamar.md#a4-q5), [Q7](MfoxAssignSamar.md#a4-q7), [Q8](MfoxAssignSamar.md#a4-q8); [A5 Q8](MfoxAssignSamar.md#a5-q8), [Q9](MfoxAssignSamar.md#a5-q9) | Lecture integer-function and sum/bound examples |
| 6–7 | [A6 Q1](MfoxAssignSamar.md#a6-q1), plus Josephus, Fibonacci, Hanoi and merge-sort lecture examples | Tutorial 9 Q1 |
| 8 | [A6 Q2](MfoxAssignSamar.md#a6-q2), [Q3](MfoxAssignSamar.md#a6-q3), [Q4](MfoxAssignSamar.md#a6-q4), [Q5](MfoxAssignSamar.md#a6-q5) | Tutorial 9 Q2–Q5 and the lecture quiz |
| 9–10 | [Assignment 7](MfoxAssignSamar.md#assignment-7) Q1–Q5 | Handwritten notes PDF pp. 219 and 221 |

Tutorial directory numbers differ from the class-summary tutorial numbers. These sheets were checked by their printed headings and dates:

- [12 October sheet](../Tutorial_10/WhatsApp%20Image%202026-11-23%20at%2012.35.02%20%283%29.jpeg): printed **Tutorial 1**, corresponding by date to summary **Tutorial 7**; Q1–Q6.
- [Tutorial 8, 2 November](../Tutorial_8/WhatsApp%20Image%202026-11-23%20at%2012.35.02%20%282%29.jpeg): Q1–Q9.
- [Tutorial 9, 12 November, page 1](../Tutorial_9/WhatsApp%20Image%202026-11-23%20at%2012.35.02.jpeg): Q1–Q4; [page 2](../Tutorial_9/WhatsApp%20Image%202026-11-23%20at%2012.35.02%20%281%29.jpeg): Q5.

## Textbook reading map

Use the supplied [Lehman–Leighton–Meyer textbook](../Study_material_after_mid_sems/MCS_Textbook_Lehman_Leighton_Meyer.pdf) for the relevant sections, rather than reading its entire syllabus. In this PDF, an Arabic printed page number corresponds to PDF page number **printed page + 8**.

| Stages | Relevant textbook sections | Printed starting pages |
|---|---|---|
| 1 | §1.7 proof by cases; Ch. 2 WOP; §5.2–5.3 strong induction and equivalence | 15; 27; 124–129 |
| 2 | §6.1–6.4 recursive definitions, structural induction, matched brackets, recursive functions, arithmetic expressions | 173–183 |
| 3–4 | §7.1 cardinality bridge; Ch. 14 cardinality/counting rules | 206; 551 |
| 5 | Ch. 13 sums and asymptotics | 503 |
| 6–7 | §21.1–21.5 recurrences | 867–888 |
| 8 | §15.1–15.5 generating functions and formal power series | 627–643 |
| 9–10 | §11.1–11.5, §11.7–11.10 selected graph topics; §9.6 and §9.9 order refresh | 393–424; 335; 340 |

The class notes/assignments supply course-specific material, including Cantor pairing, Stern–Brocot, integer functions, Josephus and Prim's algorithm. A relevant textbook chapter is supplementary reading, not evidence that every topic in that chapter was taught.

## How we will work through a stage

1. Learn the definitions, statement and conditions of each result.
2. Work through the class example and its reasoning.
3. Solve the linked assignment/tutorial problems independently.
4. Record mistakes, re-solve them, and mark the checklist only when you can explain the concept and use it without notes.

No fixed calendar is assumed because an exam date and daily study time have not been supplied.
