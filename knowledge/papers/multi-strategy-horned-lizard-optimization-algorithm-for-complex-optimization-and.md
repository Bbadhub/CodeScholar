# Multi strategy Horned Lizard Optimization Algorithm for complex optimization and advanced feature selection problems

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1186/s40537-025-01205-7` |
| Full Paper | [https://doi.org/10.1186/s40537-025-01205-7](https://doi.org/10.1186/s40537-025-01205-7) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/b22fdb2a1f495bf4d3259fde836b437797c9a99c](https://www.semanticscholar.org/paper/b22fdb2a1f495bf4d3259fde836b437797c9a99c) |
| Source | [https://journalclub.io/episodes/multi-strategy-horned-lizard-optimization-algorithm-for-complex-optimization-and-advanced-feature-selection-problems](https://journalclub.io/episodes/multi-strategy-horned-lizard-optimization-algorithm-for-complex-optimization-and-advanced-feature-selection-problems) |
| Source | [https://www.semanticscholar.org/paper/b22fdb2a1f495bf4d3259fde836b437797c9a99c](https://www.semanticscholar.org/paper/b22fdb2a1f495bf4d3259fde836b437797c9a99c) |
| Year | 2026 |
| Citations | 2 |
| Authors | Marwa M. Emam, Mosa E. Hosney, Reham R. Mostafa, Essam H. Houssein |
| Paper ID | `296e06f6-86b5-4a21-903f-b89d5ae07a9d` |

## Classification

- **Problem Type:** multi-objective optimization
- **Domain:** Machine Learning & AI
- **Sub-domain:** Feature Selection
- **Technique:** Multi-strategy Horned Lizard Optimization Algorithm (mHLOA)
- **Technique Category:** optimization_algorithm
- **Type:** novel

## Summary

The Multi-strategy Horned Lizard Optimization Algorithm (mHLOA) enhances the original Horned Lizard Optimization Algorithm (HLOA) by integrating a Local Escaping Operator, Orthogonal Learning, and RIME-based diversification to improve convergence and escape local optima. Engineers should care because mHLOA effectively addresses complex optimization and advanced feature selection problems, particularly in high-dimensional datasets.

## Key Contribution

**Introduction of mHLOA, which significantly improves the performance of feature selection and complex optimization tasks over traditional HLOA.**

## Problem

The need to select a minimal yet highly informative subset of features from large datasets to maximize classification accuracy.

## Method

**Approach:** mHLOA combines multiple strategies to enhance the search efficiency of the original HLOA. It employs a Local Escaping Operator to maintain population diversity, Orthogonal Learning to refine the search process, and a RIME diversification mechanism to improve exploration capabilities.

**Algorithm:**

1. Initialize population of solutions.
2. Evaluate fitness of each solution using a fitness function.
3. Apply Local Escaping Operator to allow solutions to escape local optima.
4. Use Orthogonal Learning to refine the search process.
5. Implement RIME diversification to enhance exploration.
6. Update the best solution found.
7. Repeat until convergence criteria are met.

**Input:** A dataset with features and corresponding labels for classification tasks.

**Output:** A reduced set of features that maximizes classification accuracy.

**Key Parameters:**

- `population_size: 100`
- `max_iterations: 1000`
- `local_escape_rate: 0.1`
- `orthogonal_learning_factor: 0.5`

**Complexity:** Not stated.

## Benchmarks

**Tested on:** 14 standard datasets from the UCI Machine Learning Repository, 12 complex benchmark functions from the CEC’22 test suite

**Results:**

- classification accuracy: superior to state-of-the-art algorithms
- feature reduction: reduced feature subset size while maintaining accuracy

**Compared against:** GWO, WOA, HHO, GJO, HGS, RIME, original HLOA

**Improvement:** mHLOA consistently outperformed baseline algorithms in terms of accuracy and feature selection efficiency.

## Implementation Guide

**Data Structures:** Array for population of solutions, Matrix for feature subsets, List for fitness values

**Dependencies:** NumPy, SciPy, Pandas

**Core Operation:**

```python
for each solution in population: evaluate_fitness(solution); apply_local_escaping(solution);
```

**Watch Out For:**

- Ensure proper initialization of population to avoid premature convergence.
- Monitor the balance between exploration and exploitation to prevent getting stuck in local optima.
- Adjust parameters based on the specific dataset characteristics.

## Use This When

- Dealing with high-dimensional datasets in classification tasks.
- Needing to improve the performance of existing feature selection methods.
- Working on complex optimization problems requiring robust solutions.

## Don't Use When

- The dataset is small and does not require feature selection.
- Real-time processing is critical and cannot afford the computational overhead.
- The problem domain does not involve optimization.

## Key Concepts

feature selection, metaheuristic algorithms, local optima, multi-objective optimization, population diversity, exploration-exploitation balance

## Connects To

- Particle Swarm Optimization (PSO)
- Genetic Algorithms (GA)
- Ant Colony Optimization (ACO)

## Prerequisites

- Understanding of metaheuristic optimization techniques.
- Familiarity with feature selection methods.
- Knowledge of classification algorithms.

## Limitations

- Performance may degrade on very small datasets.
- Computationally intensive for extremely high-dimensional datasets.
- May require fine-tuning of parameters for optimal performance.

## Open Questions

- How can mHLOA be adapted for unsupervised feature selection?
- What are the effects of different parameter settings on the performance of mHLOA?

## Abstract

The horned lizard is such an odd specimen that it has inspired its own optimization algorithm. Aptly named the Horned Lizard Optimization algorithm (HLOA). And in today's paper, the authors try to improve on it. Their version, called the Multi-strategy Horned Lizard Optimization Algorithm (mHLOA), adds a Local Escaping Operator, Orthogonal Learning, and RIME-based diversification in an attempt to escape local optima and improve convergence. On today’s episode we’ll walk through how traditional HLOA works, its shortcomings, and what mHLOA does differently. Let’s jump in. First, let's talk about the types of problems that HLOA is designed to solve. Let's say you have a massive dataset with hundreds of features, and you want to build a predictive model. For example, you have a dataset of customer shopping habits and you want a model that can predict which products someone is likely to buy next.
