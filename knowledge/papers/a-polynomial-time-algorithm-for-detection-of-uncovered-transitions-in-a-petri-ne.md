# A Polynomial-Time Algorithm for Detection of Uncovered Transitions in a Petri Net-Based Concurrent System

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3390/app15020680` |
| Full Paper | [https://doi.org/10.3390/app15020680](https://doi.org/10.3390/app15020680) |
| Source | [https://journalclub.io/episodes/a-polynomial-time-algorithm-for-detection-of-uncovered-transitions-in-a-petri-net-based-concurrent-system](https://journalclub.io/episodes/a-polynomial-time-algorithm-for-detection-of-uncovered-transitions-in-a-petri-net-based-concurrent-system) |
| Year | 2026 |
| Citations | 0 |
| Authors |  |
| Paper ID | `0f424b3b-41ec-49ed-8f64-e47c8df4ec2d` |

## Classification

- **Problem Type:** verification of concurrent systems
- **Domain:** Software Engineering
- **Sub-domain:** Petri nets and concurrent systems
- **Technique:** Polynomial-Time Algorithm for Detection of Uncovered Transitions
- **Technique Category:** algorithm
- **Type:** novel

## Summary

This paper presents a polynomial-time algorithm for detecting uncovered transitions in Petri net-based concurrent systems, significantly improving the efficiency of verification processes. Engineers should care because it allows for timely identification of potential issues in complex systems, enhancing reliability and performance during the design phase.

## Key Contribution

**A novel polynomial-time algorithm for detecting uncovered transitions in Petri nets, improving verification efficiency.**

## Problem

The need for efficient verification methods in large and complex Petri net-based concurrent systems to ensure correctness and reliability.

## Method

**Approach:** The method transforms the incidence matrix of a Petri net into its reduced row echelon form (RREF) and then identifies uncovered transitions by examining the properties of the RREF. It checks for transitions that cannot form a proper t-invariant based on the nonnegative entries in the rows.

**Algorithm:**

1. Input the incidence matrix of the Petri net.
2. Transpose the incidence matrix.
3. Transform the transposed matrix into RREF.
4. For each row in RREF, check for uncovered transitions by examining nonnegative entries.
5. Identify transitions that cannot form a proper t-invariant.
6. Return the set of uncovered transitions.

**Input:** Incidence matrix of a Petri net-based concurrent system.

**Output:** Set of uncovered transitions in the Petri net.

**Complexity:** O(|P|²|T|) time, O(|P|) space

## Benchmarks

**Tested on:** 386 test modules including real-life concurrent systems, cyber-physical systems, and manufacturing systems.

**Results:**

- Run-time efficiency and correctness of results.

**Compared against:** Martínez–Silva method, PIPE tool.

**Improvement:** The proposed algorithm computed results for all tested cases, while both baselines failed to deliver results for all models within one hour.

## Implementation Guide

**Data Structures:** Incidence matrix, Reduced row echelon form matrix

**Dependencies:** Linear algebra libraries for matrix operations (e.g., NumPy in Python)

**Core Operation:**

```python
uncoveredTransitions = compute_uncovered_transitions(incidence_matrix)
```

**Watch Out For:**

- Ensure the incidence matrix is correctly formatted before input.
- Watch for numerical stability when performing matrix operations.
- Be aware of the limitations of the RREF method in terms of interpretability.

## Use This When

- You need to verify complex Petri net-based concurrent systems efficiently.
- You are in the early design stages and need quick feedback on potential issues.
- You are dealing with large-scale systems where traditional methods are computationally infeasible.

## Don't Use When

- The Petri net model is simple and can be verified using existing methods without performance concerns.
- You require exhaustive analysis of all possible states rather than focusing on uncovered transitions.
- The system does not utilize Petri nets for modeling.

## Key Concepts

Petri nets, transition invariants, RREF, uncovered transitions, concurrent systems, verification

## Connects To

- Matrix operations
- Linear algebra techniques
- State space exploration
- Reachability graph analysis

## Prerequisites

- Understanding of Petri nets
- Familiarity with linear algebra
- Knowledge of concurrent systems

## Limitations

- The algorithm may not provide insights into all qualitative properties of the system.
- Performance may vary based on the structure of the incidence matrix.
- It focuses solely on uncovered transitions, potentially missing other verification aspects.

## Open Questions

- How can this algorithm be extended to analyze qualitative properties of Petri nets?
- What are the implications of uncovered transitions on system performance and reliability?

## Abstract

When the algorithm gets called you need to pass it an incidence matrix, which is just the mathematical version of the diagram I described earlier. It starts by just initializing an empty list. This is where it’s going to store any uncovered transitions that it finds. Next, it flips (transposes) the rows and columns of the incidence matrix. This is just to prepare it for the next steps, which involve analyzing the transitions mathematically. Now, the algorithm reworks the transposed matrix into something called Reduced Row Echelon Form (RREF). This is a cleaned-up version where patterns in the data become much clearer. It involves reorganizing and simplifying the rows to highlight key features. With the RREF in hand, it then looks at each row (representing places in the system) to find transitions that
