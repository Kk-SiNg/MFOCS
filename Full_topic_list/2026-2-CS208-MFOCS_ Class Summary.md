**Class 1: Lecture 1: 5/Oct/26:**  
Introductions.

Discussion of various open mathematical conjectures, such as the Goldbach conjecture, Collatz conjecture, Polya’s conjecture, why assigning true or false value to a proposition/predicate is nontrivial.

Why proof by sampling is not a valid proof technique.

Discussion on the matrix multiplication problem, Strassen’s algorithm, and some of the recent advances.

Discussion on Ramsey numbers.

Importance and relevance of attempting to solve hard problems in mathematics and the case of development of algebraic geometry while solving Fermat's last theorem.

A discussion of rumblings in mathematics at the start of the 20th century … Russell’s paradox, Russell and Whitehead’s efforts to formalize mathematics via the set theory: Principia Mathematica, and then Godel’s blow to it via the incompleteness theorem, Turing machine and its undecidability.

References to Doxiadis’ Logicomix and Hofstadter’s GEB.

**Class 2: Lecture 2: 6/Oct/26:**  
Discussion of two more commonly used, but invalid proof techniques: proof by bullying and proof by insulting.

Proof by cases and its illustration by computing R(3,3) and a discussion of extending the same technique to compute bigger diagonal Ramsey numbers.

Motivation for strong induction by discussing the proof of the existence part of the Prime factorization theorem.

Introduction to strong induction and the canonical structure of a strong induction proof. Comparisons with the ordinary induction.

**Class 3: Lecture 3: 7/Oct/26:**  
Strong induction proof that using 3 and 5 kgs weights, any weight \>= 8 kgs can be constructed.

Motivation for well-ordering principle based proof technique by discussing another way to prove the existence part of the Prime factorization theorem.

The formal definition of the well-ordering principle and the canonical structure of a well-ordering proof.

**Class 4: Lecture 4: 8/Oct/26:**  
Formal and a more detailed strong induction proof that using 3 and 5 kgs weights, any weight \>= 8 kgs can be constructed.

Illustration of the use of WOP to prove the formula for the sum of first n non-negative integers.

Discussion of the equivalence of ordinary induction, strong induction, and well-ordering principle based proofs … their respective pros and cons and illustrations of how a proof of one type can be converted to a proof of another type.

**Class 5: Tutorial 7: 12/Oct/26:**  
Tutorial on some more proof techniques.

**Class 6: Lecture 5: 13/Oct/26:**  
Introduction to recursive data types. Non-negative integers, character strings, binary trees, strings of parentheses, arithmetic expressions, and two-player complete information games, such as chess, as examples of recursive data types.

Non-negative integers as a RDT and the corresponding recursive definition of some functions defined over non-negative integers. Identifying ill-formed function definitions … introduction to Collatz conjecture and Ackermann function and the rate of its growth. Knuth’s arrow notation.

**Class 7: Lecture 6: 14/Oct/26:**  
Introduction to hyperoperations: from successor operation to addition to multiplication and exponentiation, tetration, pentation, and hexation. Graham’s number and lower bounds on TREE(3).

Introduction to structural induction: definition. Character strings as a recursive data type and recursive definitions of various functions defined over them. Using structural induction to prove some properties of character strings.

Arithmetic expressions as a recursive data type, Aexp: definition.

**Class 8: Lecture 7: 15/Oct/26:**  
Recursive definitions of evaluation and substitution functions defined over Aexp and examples of using those definitions to evaluate and substitute into an arithmetic expression, respectively.

The Substitution and Environment models of evaluating arithmetic expressions with substitutions, comparison of their respective pros and cons, and proof of their equivalence using structural induction.

**Class 9: Lecture 8: 21/Oct/26:**  
The arrow interpretation of binary relations that are total, function, surjective, injective, and bijective.

Lemma relating the existence of surjective function, total injective function, and a bijective function between two (finite) sets and their respective cardinalities. Generalizing this lemma for infinite sets.

Bijection between the set of non-negative integers and rationals: Cantor pairing function and Stern–Brocot tree.

Combinatorics: Bijection rule: establishing a correspondence between the number of ways to solve a problem and binary strings with certain properties and then counting the number of such binary strings to solve the original problem. Illustration of this method by establishing a correspondence between the number of ways to choose 12 ice-creams when 5 flavors are available and 16 bit strings with 4 1’s and then proving that the solution of the first problem is C(16,4) because that is the number of binary strings of length 16 with 4 1’s.

**Class 10: Lecture 9: 22/Oct/26:**  
Discussion on a doubt on the solution of last lecture’s Bijection rule example: An argument was given that the solution should be 5^12 because we have to select 12 ice-creams when each can be chosen from 5 given options. However, this is incorrect because the ice-cream ‘slots’ are indistinguishable so whether the first cream is of Flavor 1 and the second  of Flavor 2 or it is the other way, both are the same and count as one way because the order in which one or other flavor is chosen does not matter … what matters if a flavor is chosen at all and if yes, then how many times. If we do not count them so, then it leads to overcounting the number of ways of choosing ice-cream.

Combinatorics: Sum rule for disjoint sets, product rule for distinct and indistinguishable objects, generalized product rule, division rule: k-to-1 functions, and examples illustrating their uses, such as:

- counting the number of ways of selecting food items when the same, say 5, food options are available for three distinct meals in a day: breakfast, lunch, and dinner (this number is 5^3) and the number of ways of selecting food items when the same 5 options are available for three (indistinguishable) meals in a day (this number is C(7,4))  
- counting the number of ways creating distinct passwords of length 6 to 8 characters, when the first character must be a letter and remaining ones a letter or a digit  
- counting the number of unique ways of seating n people around a round table  
- counting the number of unique paths from the top left corner of an n x n square grid to the bottom right corner when only the right and down moves are allowed

Binomial and multinomial coefficients and the corresponding theorems, pigeonhole and generalized pigeonhole principles and examples of their uses in the subset sum problem and the hairs on heads problem..

**Class 11: Lecture 10: 26/Oct/26:**  
Inclusion-exclusion principle, its proof, and discussion of examples illustrating its use.

Proving combinatorial identities using combinatorial arguments. Pascal’s triangle.

**Class 12: Lecture 11: 27/Oct/26:**  
Evaluating series sums and products and computing upper and lower bounds on them. Sum of square-roots of first n non-negative integers: computing upper and lower bounds. Harmonic numbers. Multiple sums and changing the order of the summation technique: sum of first n Harmonic numbers.

**Class 13: Lecture 12: 28/Oct/26:**  
Integers functions: ceil, floor, and mod. Discussion of their definitions, properties, and examples of their use.

**Class 14: Lecture 13: 29/Oct/26:**  
Iverson’s bracket and illustration of its use in computing closed form for series sums. Sum of floors of square-roots of first n non-negative integers and using the result to provide a tighter lower bound to the sum of square-roots of first n non-negative integers compared to what is obtained using the technique in Lecture 11\.

**Class 15: Tutorial 8: 2/Nov/26:**  
Tutorial on structural induction, recursive function definitions, counting rules, the pigeonhole principle, the inclusion-exclusion principle, combinatorial arguments, and integer functions.

**Class 16: Lecture 14: 3/Nov/26:**  
Introduction to recurrence relations. Josephus problem and its recurrences. Recursive algorithms, recurrence relations, and induction. Guess-and-verify (finding patterns in a sequence of numbers) and expansion/plug-and-chug (finding patterns in a sequence of expressions) methods of solving recurrences and their illustrations in solving the recurrences for Tower of Hanoi and Merge sort, respectively.

**Class 17: Lecture 15: 4/Nov/26:**  
Linear recurrences. Solving homogenous linear recurrences and its illustration in solving the Fibonacci recurrence. Solving inhomogeneous linear recurrences, homogenous and particular solutions, and its illustration in solving the modified Tower of Hanoi problem (where effort in moving a disk depends on its size.)

**Class 18: Lecture 16: 5/Nov/26:**  
Divide-and-conquer recurrences. Akra-Bazzi formula and Akra-Bazzi theorem ([paper link](https://link.springer.com/article/10.1023/A:1018373005182)) and their illustration in solving Merge sort recurrence. Discussion on boundary conditions and floor/ceiling operations having no effect on the asymptotic behaviour of divide-and-conquer recurrences. Master theorem as a corollary of Akra-Bazzi theorem.

Big picture for recurrences: effects of the size and number of subproblems on asymptotic behaviour of linear and divide-and-conquer recurrences.

**Class 19: Lecture 17: 9/Nov/26:**  
Surprise quiz on a “weird” counting problem to demonstrate the use of generating functions.

Introduction to generating functions as mathematical tools to convert problems about sequences to problems about algebra. Illustration of solving some simple counting problems using generating functions.

**Class 20: Lecture 18: 10/Nov/26:**  
Product of generating functions and the convolution rule. Solving counting problems with the convolution rule and its illustration via solving various counting problems, including deriving the binomial theorem and solving the “weird” counting problem of Class 19’s surprise quiz.

Generating functions as a quotient of polynomials and expressing them as a sum of partial fractions with “simple” power series. Partial fractions with distinct and repeated roots.

**Class 21: Lecture 19: 11/Nov/26:**  
Using generating functions to solve homogeneous and non-homogeneous linear recurrences and their respective illustrations using the Fibonacci and Towers of Hanoi recurrences. Establishing the Towers of Hanoi recurrence via equating a lower and an upper bound. Generating functions for series with ‘diverging’ coefficients, such as n\! and n\*n\!, and using those to establish an iterative identity for n\!

**Class 22: Tutorial 9: 12/Nov/26:**  
Tutorial on solving recurrences, specially the linear and divide-and-conquer recurrences, and using generating functions for solving counting problems and linear recurrences.

**Class 23: Lecture 20: 17/Nov/26:**  
