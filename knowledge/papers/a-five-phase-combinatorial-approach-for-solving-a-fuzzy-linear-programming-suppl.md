# A five-phase combinatorial approach for solving a fuzzy linear programming supply chain production planning problem

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1080/23311916.2024.2334566` |
| Full Paper | [https://doi.org/10.1080/23311916.2024.2334566](https://doi.org/10.1080/23311916.2024.2334566) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/c89b9b2c90abb1ba5b4d5e851d807c2450cae5a5](https://www.semanticscholar.org/paper/c89b9b2c90abb1ba5b4d5e851d807c2450cae5a5) |
| Source | [https://journalclub.io/episodes/a-five-phase-combinatorial-approach-for-solving-a-fuzzy-linear-programming-supply-chain-production-planning-problem](https://journalclub.io/episodes/a-five-phase-combinatorial-approach-for-solving-a-fuzzy-linear-programming-supply-chain-production-planning-problem) |
| Source | [https://www.semanticscholar.org/paper/c89b9b2c90abb1ba5b4d5e851d807c2450cae5a5](https://www.semanticscholar.org/paper/c89b9b2c90abb1ba5b4d5e851d807c2450cae5a5) |
| Year | 2026 |
| Citations | 2 |
| Authors | Noppasorn Sutthibutr, N. Chiadamrong, K. Hiraishi, S. Thajchayapong |
| Paper ID | `d3bb7ee9-e1d8-4723-8f28-8f26e487ca8b` |

## Classification

- **Problem Type:** fuzzy linear programming
- **Domain:** Optimization & Operations Research
- **Sub-domain:** Fuzzy Linear Programming
- **Technique:** Five-phase combinatorial approach
- **Technique Category:** optimization_algorithm
- **Type:** novel

## Summary

The paper presents a five-phase combinatorial approach to enhance fuzzy linear programming for supply chain production planning. Engineers should care because this method improves decision-making under uncertainty by integrating multiple fuzzy concepts, leading to more robust and optimal solutions.

## Key Contribution

**A novel five-phase combinatorial method that integrates multiple fuzzy programming techniques to solve supply chain production planning problems more effectively.**

## Problem

The need for improved decision-making in supply chain production planning under uncertainty and fuzziness in data.

## Method

**Approach:** The method consists of five phases that integrate various fuzzy programming concepts to handle uncertainty in supply chain production planning. It combines Triangular Intuitionistic Fuzzy Numbers, Intuitionistic Fuzzy Linear Programming, Realistic Robust Programming, Chance-Constrained Programming, and Augmented Epsilon Constraint to generate optimal solutions.

**Algorithm:**

1. 1. Define the supply chain production planning problem with fuzzy parameters.
2. 2. Apply Triangular Intuitionistic Fuzzy Numbers to represent uncertainty.
3. 3. Formulate the problem using Intuitionistic Fuzzy Linear Programming.
4. 4. Incorporate Realistic Robust Programming to ensure solution robustness.
5. 5. Use Chance-Constrained Programming and Augmented Epsilon Constraint to derive Pareto-optimal solutions.

**Input:** Fuzzy parameters related to supply chain production, such as demand, supply, and costs represented as Triangular Intuitionistic Fuzzy Numbers.

**Output:** Pareto-optimal solutions for production planning that account for uncertainty and robustness.

**Key Parameters:**

- `fuzzy_parameter: TIFN values`
- `robustness_level: 0.1 to 0.5`
- `satisfaction_threshold: 0.7`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Synthetic supply chain data with fuzzy parameters

**Results:**

- Pareto-optimality, robustness level, satisfaction rate

**Compared against:** Traditional fuzzy linear programming methods

**Improvement:** Demonstrated improved robustness and optimality over traditional FLP methods.

## Implementation Guide

**Data Structures:** Fuzzy number representations, Linear programming models

**Dependencies:** Optimization libraries (e.g., SciPy, PuLP), Fuzzy logic libraries

**Core Operation:**

```python
solve_supply_chain(fuzzy_parameters): apply_five_phase_method(fuzzy_parameters)
```

**Watch Out For:**

- Ensure accurate representation of fuzzy parameters.
- Balance between robustness and optimality to avoid over-constraining.
- Validate results against real-world scenarios to ensure applicability.

## Use This When

- You need to make production planning decisions under uncertainty.
- Fuzzy parameters are involved in the decision-making process.
- Robustness in solutions is a critical requirement.

## Don't Use When

- The problem can be solved with traditional linear programming without fuzziness.
- High precision in parameters is required without uncertainty.
- The computational resources are extremely limited.

## Key Concepts

Fuzzy Linear Programming, Triangular Intuitionistic Fuzzy Numbers, Robust Programming, Chance-Constrained Programming, Pareto-optimal solutions

## Connects To

- Fuzzy Logic Systems
- Multi-Objective Optimization
- Robust Optimization Techniques

## Prerequisites

- Understanding of fuzzy logic and fuzzy numbers
- Basic knowledge of linear programming
- Familiarity with optimization techniques

## Limitations

- Complexity in accurately defining fuzzy parameters.
- Potential computational intensity due to multiple phases.
- May not be suitable for problems with precise data.

## Open Questions

- How can this approach be adapted for dynamic supply chain environments?
- What are the implications of different types of fuzzy representations on outcomes?

## Abstract

The authors argue that traditionally, you would solve this problem by gathering all your data then solving it as a fuzzy linear programming (FLP) problem. But, in this case, they say that’s not good enough. So this paper is introducing a new strategy that gets better results. It’s a five-phase combinatorial method that integrates five separate ideas: Triangular Intuitionistic Fuzzy Numbers (TIFN), Intuitionistic Fuzzy Linear Programming (IFLP), Realistic Robust Programming (RRP), Chance-Constrained Programming (CCP) and Augmented Epsilon Constraint (AUGMECON). Their argument is that this new system improves on FLP by allowing hesitation, ensuring robustness, considering both satisfaction and non-satisfaction levels, and generating Pareto-optimal solutions.
