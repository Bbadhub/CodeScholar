# Discovering effective policies for land-use planning with neuroevolution

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1017/eds.2025.18` |
| Full Paper | [https://doi.org/10.1017/eds.2025.18](https://doi.org/10.1017/eds.2025.18) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/4ad65e48051ddb9c698050d9a62af1456398490a](https://www.semanticscholar.org/paper/4ad65e48051ddb9c698050d9a62af1456398490a) |
| Source | [https://journalclub.io/episodes/discovering-effective-policies-for-land-use-planning-with-neuroevolution](https://journalclub.io/episodes/discovering-effective-policies-for-land-use-planning-with-neuroevolution) |
| Source | [https://www.semanticscholar.org/paper/4ad65e48051ddb9c698050d9a62af1456398490a](https://www.semanticscholar.org/paper/4ad65e48051ddb9c698050d9a62af1456398490a) |
| Year | 2026 |
| Citations | 1 |
| Authors | Daniel Young, Olivier Francon, Elliot Meyerson, C. Schwingshackl, Jacob Bieker, Hugo Cunha |
| Paper ID | `f919a7c7-703c-4426-8a85-0eccd3ba56f0` |

## Classification

- **Problem Type:** multi-objective optimization
- **Domain:** Machine Learning & AI
- **Sub-domain:** Evolutionary optimization
- **Technique:** Evolutionary Surrogate-assisted Prescription (ESP)
- **Technique Category:** optimization_algorithm
- **Type:** novel

## Summary

The paper presents a system that discovers effective land-use policies by predicting emissions from land-use changes and evolving better policies through neuroevolution. Engineers should care because this approach provides a scalable method to optimize land-use decisions, which can significantly impact climate change mitigation efforts.

## Key Contribution

**The introduction of an evolutionary surrogate-assisted prescription method for optimizing land-use planning policies.**

## Problem

The need to optimize land-use patterns to minimize carbon emissions while maintaining ecosystem services.

## Method

**Approach:** The method learns a surrogate model to predict emissions from historical land-use changes, which is then used in an evolutionary search to discover optimal land-use policies. This results in a Pareto front of solutions that balance carbon impact and land-use change.

**Algorithm:**

1. 1. Collect historical data on land-use changes and associated emissions.
2. 2. Train a surrogate model to predict emissions based on land-use changes.
3. 3. Initialize a population of candidate policies (neural networks).
4. 4. Evaluate each candidate using the surrogate model to predict outcomes.
5. 5. Select the best-performing candidates based on their predicted outcomes.
6. 6. Apply crossover and mutation to generate new candidates.
7. 7. Repeat steps 4-6 until convergence or a stopping criterion is met.

**Input:** Historical land-use data, including latitude, longitude, area, year, and current land use percentages.

**Output:** A Pareto front of optimal land-use policies that minimize emissions and land-use change.

**Key Parameters:**

- `population_size: 100`
- `mutation_rate: 0.01`
- `crossover_rate: 0.7`
- `learning_rate: 0.001`

**Complexity:** Not stated.

## Benchmarks

**Tested on:** Land-Use Harmonization dataset (LUH2), Bookkeeping model of Land-Use Emissions (BLUE)

**Results:**

- ELUC (emissions from land-use change)
- percentage of land changed

**Compared against:** Multi-objective linear programming, Multi-criteria decision-making (MCDM), Causal machine learning approaches

**Improvement:** The proposed method generates a Pareto front that effectively balances carbon impact and land-use change, outperforming traditional methods.

## Implementation Guide

**Data Structures:** Neural network for prescriptive model, Dataframe for historical land-use data

**Dependencies:** scikit-learn, PyTorch

**Core Operation:**

```python
for each candidate in population: evaluate(candidate) using surrogate_model; select_best_candidates(); crossover_and_mutate();
```

**Watch Out For:**

- Ensure the surrogate model is well-trained to avoid poor policy recommendations.
- Be cautious of overfitting when training on historical data.
- Consider the computational cost of evaluating the surrogate model.

## Use This When

- You need to optimize land-use decisions to minimize carbon emissions.
- You want to explore trade-offs between environmental impact and land-use change.
- You are working on climate change mitigation strategies.

## Don't Use When

- The land-use decisions are highly localized and require fine-grained data.
- You need real-time decision-making without the ability to train models.
- The problem does not involve multiple conflicting objectives.

## Key Concepts

neuroevolution, surrogate modeling, Pareto optimization, land-use planning, carbon emissions, evolutionary algorithms

## Connects To

- Genetic algorithms
- Reinforcement learning
- Multi-objective optimization techniques

## Prerequisites

- Understanding of evolutionary algorithms
- Familiarity with surrogate modeling
- Knowledge of multi-objective optimization

## Limitations

- The approach may not generalize well to highly localized land-use scenarios.
- The resolution of input data may limit the effectiveness of recommendations.
- The method relies on historical data, which may not capture future conditions accurately.

## Open Questions

- How can the model be adapted for real-time decision-making?
- What additional objectives could be incorporated to enhance policy recommendations?

## Abstract

The point isn’t to test effective land-use policies, it’s to discover them. Their system learns to predict emissions from land-use changes, then uses that predictor as a surrogate to evolve better policies through neuroevolution. What makes this particularly interesting is how it scales.
