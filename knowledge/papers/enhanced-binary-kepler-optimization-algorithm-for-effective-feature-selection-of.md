# Enhanced Binary Kepler Optimization Algorithm for effective feature selection of supervised learning classification

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1186/s40537-025-01125-6` |
| Full Paper | [https://doi.org/10.1186/s40537-025-01125-6](https://doi.org/10.1186/s40537-025-01125-6) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/1e67a36aff33c25e2595a9c95f36d39b6674be21](https://www.semanticscholar.org/paper/1e67a36aff33c25e2595a9c95f36d39b6674be21) |
| Source | [https://journalclub.io/episodes/enhanced-binary-kepler-optimization-algorithm-for-effective-feature-selection-of-supervised-learning-classification](https://journalclub.io/episodes/enhanced-binary-kepler-optimization-algorithm-for-effective-feature-selection-of-supervised-learning-classification) |
| Source | [https://www.semanticscholar.org/paper/1e67a36aff33c25e2595a9c95f36d39b6674be21](https://www.semanticscholar.org/paper/1e67a36aff33c25e2595a9c95f36d39b6674be21) |
| Year | 2026 |
| Citations | 2 |
| Authors | A. A. El-Mageed, A. Abohany, Khalid M. Hosny |
| Paper ID | `d7dc2e10-7b88-4387-ad4e-9d39a10b9696` |

## Classification

- **Problem Type:** feature selection for supervised learning classification
- **Domain:** Machine Learning & AI
- **Sub-domain:** Feature Selection
- **Technique:** Enhanced Binary Kepler Optimization Algorithm (BKOA-MUT)
- **Technique Category:** optimization_algorithm
- **Type:** novel

## Summary

The Enhanced Binary Kepler Optimization Algorithm (BKOA-MUT) improves feature selection in supervised learning by integrating Kepler's planetary motion laws with Differential Evolution mutation strategies. Engineers should care because it offers a robust and efficient method for selecting optimal feature subsets, enhancing classification accuracy while reducing computational costs.

## Key Contribution

**The introduction of BKOA-MUT, which combines Kepler's laws with DE mutation strategies for effective feature selection.**

## Problem

The challenge of identifying relevant features from high-dimensional datasets to improve classification accuracy and reduce computational costs.

## Method

**Approach:** BKOA-MUT simulates planetary motion to guide candidate solutions through the search space, balancing exploration and exploitation. It integrates DE/rand and DE/best mutation strategies to enhance search capabilities and reduce premature convergence.

**Algorithm:**

1. Initialize a population of candidate solutions (planets) randomly in the feature space.
2. Evaluate the fitness of each candidate solution based on classification accuracy.
3. Update the position and velocity of each candidate solution using Kepler's laws.
4. Apply DE/rand and DE/best mutation strategies to enhance the search process.
5. Select the best candidate solutions as the new population.
6. Repeat the evaluation and update steps until convergence criteria are met.

**Input:** A dataset with labeled features for supervised learning.

**Output:** A reduced subset of features that maximizes classification accuracy.

**Key Parameters:**

- `population_size: 100`
- `max_iterations: 1000`
- `mutation_factor: 0.5`
- `crossover_rate: 0.9`

**Complexity:** Not stated.

## Benchmarks

**Tested on:** 25 UCI benchmarks including three large-scale datasets with over 1000 attributes.

**Results:**

- accuracy: significant improvements over existing MHAs
- feature reduction: effective reduction in the number of features selected

**Compared against:** Recent Meta-heuristic Algorithms (MHAs)

**Improvement:** Statistically significant enhancements validated using the Wilcoxon rank-sum test.

## Implementation Guide

**Data Structures:** Array for candidate solutions, Matrix for feature subsets, Fitness evaluation function

**Dependencies:** NumPy for numerical operations, SciPy for optimization routines, scikit-learn for machine learning models

**Core Operation:**

```python
for each planet in population: evaluate_fitness(planet); update_position(planet); apply_mutation(planet);
```

**Watch Out For:**

- Ensure proper tuning of mutation factor and crossover rate to avoid premature convergence.
- Monitor the balance between exploration and exploitation to maintain diversity in the population.
- Validate results with statistical tests to confirm improvements.

## Use This When

- You need to select features from high-dimensional datasets for classification tasks.
- You want to improve the accuracy of machine learning models while reducing computational costs.
- You are facing challenges with traditional feature selection methods in terms of scalability.

## Don't Use When

- The dataset is small and does not require complex feature selection.
- Real-time processing is critical and cannot accommodate the computational overhead of the algorithm.
- You need a deterministic solution rather than a probabilistic one.

## Key Concepts

feature selection, Kepler Optimization Algorithm, Differential Evolution, meta-heuristic algorithms, classification accuracy, high-dimensional datasets

## Connects To

- Differential Evolution
- Genetic Algorithms
- Particle Swarm Optimization
- Gravitational Search Algorithm
- Feature Selection Techniques

## Prerequisites

- Understanding of meta-heuristic optimization techniques.
- Familiarity with feature selection methods.
- Knowledge of machine learning classification algorithms.

## Limitations

- May struggle with very high-dimensional datasets beyond its designed capacity.
- Performance can vary based on the choice of parameters and dataset characteristics.
- Requires careful tuning to avoid local optima.

## Open Questions

- How can BKOA-MUT be adapted for real-time feature selection tasks?
- What are the effects of varying population sizes on the algorithm's performance?

## Abstract

Many metaheuristics draw their metaphors from nature. Some pretend to be bees. Some pretend to be wolves. This one pretends to be a planet. The Kepler Optimization Algorithm (KOA) already existed prior to this paper. It’s a physics-inspired method that simulates planetary motion as a way to guide candidate solutions through the search space. Specifically, it’s built around Kepler’s three laws of orbital mechanics (which describe how the planets orbit around the sun). The key idea is that each solution is treated as a "planet" orbiting around the current global best, which acts as the "sun." The metaphor isn’t just for show. Each of the algorithm’s internal update rules (its position, velocity, eccentricity, gravitational pull) maps directly to a component of Keplerian physics. These constructs define how solutions evolve over time. Each candidate solution starts as a point in the search space with a randomly initialized
