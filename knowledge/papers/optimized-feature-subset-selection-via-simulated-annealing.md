# Optimized feature subset selection via simulated annealing

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1088/2632-2153/ae20ed` |
| Full Paper | [https://doi.org/10.1088/2632-2153/ae20ed](https://doi.org/10.1088/2632-2153/ae20ed) |
| Source | [https://journalclub.io/episodes/optimized-feature-subset-selection-via-simulated-annealing](https://journalclub.io/episodes/optimized-feature-subset-selection-via-simulated-annealing) |
| Year | 2026 |
| Citations | 0 |
| Authors |  |
| Paper ID | `1fa24136-2d77-4de7-b528-222db8f199a4` |

## Classification

- **Problem Type:** feature selection for classification models
- **Domain:** Machine Learning & AI
- **Sub-domain:** Feature Selection
- **Technique:** SA-FDR
- **Technique Category:** optimization_algorithm
- **Type:** novel

## Summary

The paper presents a novel algorithm, SA-FDR, for optimized feature subset selection using simulated annealing to maximize the Fisher Discriminant Ratio (FDR). This method is particularly valuable for engineers working with high-dimensional datasets, as it effectively identifies compact feature subsets while maintaining predictive accuracy.

## Key Contribution

**Introduction of the SA-FDR algorithm that utilizes simulated annealing for efficient feature selection in classification tasks.**

## Problem

The work addresses the challenge of selecting relevant features from high-dimensional datasets to improve model performance and interpretability.

## Method

**Approach:** The SA-FDR algorithm uses simulated annealing to explore feature subsets and optimize the Fisher Discriminant Ratio as a proxy for model quality. It iteratively refines feature subsets through probabilistic transitions, allowing for the acceptance of worse solutions to escape local minima.

**Algorithm:**

1. Initialize replicas as binary vectors representing feature subsets.
2. Compute FDR values for each replica.
3. Iteratively propose changes to feature subsets and accept or reject based on the Metropolis rule.
4. Adjust the temperature to control the acceptance probability of worse solutions.
5. Repeat until convergence or a maximum number of iterations is reached.
6. Evaluate the final feature subsets using logistic regression and select the best one.

**Input:** Dataset with samples and features, specified number of features to select (k).

**Output:** Best subset of features that maximizes the FDR.

**Key Parameters:**

- `R: number of replicas (e.g., 50)`
- `βsteps: number of temperature steps (e.g., 100)`
- `NS: number of sweeps (e.g., 0.5)`
- `ϵ: temperature step size (e.g., 0.7)`
- `kmax: maximum number of features to consider (e.g., 30)`

**Complexity:** Not stated.

## Benchmarks

**Tested on:** SPECTF Heart, Breast Cancer Wisconsin Diagnostic, Ozone Level Detection Eight Hours, Spambase, Predict Students’ Dropout and Academic Success, Taiwanese Bankruptcy Prediction, Madelon, Default of Credit Card Clients, Loan Default

**Results:**

- AUC: varies by dataset, e.g., Heart: 0.817, Cancer: 0.992, Loan Default: 0.712

**Compared against:** Recursive Feature Elimination (RFE), Lasso

**Improvement:** SA-FDR achieves better or comparable AUC values with fewer features than RFE and Lasso.

## Implementation Guide

**Data Structures:** Binary vectors for feature subsets, Matrices for within-class and between-class variance

**Dependencies:** NumPy for numerical operations, SciPy for optimization routines

**Core Operation:**

```python
Initialize replicas; compute FDR; propose changes; accept/reject based on Metropolis rule.
```

**Watch Out For:**

- Ensure proper initialization of replicas to avoid poor convergence.
- Monitor temperature adjustments to prevent premature convergence.
- Use diverse batches to avoid overfitting and ensure representative sampling.

## Use This When

- Working with high-dimensional datasets where feature selection is critical.
- Needing a balance between model interpretability and predictive performance.
- Facing challenges with overfitting due to irrelevant features.

## Don't Use When

- The dataset is low-dimensional and feature selection is not necessary.
- Real-time performance is critical and computational resources are limited.

## Key Concepts

feature selection, simulated annealing, Fisher Discriminant Ratio, logistic regression, combinatorial optimization

## Connects To

- Genetic Algorithms for feature selection
- Recursive Feature Elimination (RFE)
- Lasso regression for feature selection

## Prerequisites

- Understanding of logistic regression
- Familiarity with optimization algorithms
- Knowledge of feature selection techniques

## Limitations

- Assumes Gaussian distribution of features within classes.
- May require significant computational resources for large datasets.
- Performance may vary based on dataset characteristics.

## Open Questions

- How to optimize hyperparameters for runtime efficiency?
- Can the method be adapted for multi-class classification problems?

## Abstract

Imagine that you're a Data Scientist, working in the underwriting department at a bank. Your job is to build a model that can analyze batches of loan applications and predict which applicants in the batch (if any) are unusually likely to default on their loan.
