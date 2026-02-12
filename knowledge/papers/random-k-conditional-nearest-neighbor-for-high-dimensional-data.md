# Random k conditional nearest neighbor for high-dimensional data

## Access

| Field | Value |
|-------|-------|
| DOI | `10.7717/peerj-cs.2497` |
| Full Paper | [https://doi.org/10.7717/peerj-cs.2497](https://doi.org/10.7717/peerj-cs.2497) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/de2abb6e0817f95db9f6b5fac13af9137366fa51](https://www.semanticscholar.org/paper/de2abb6e0817f95db9f6b5fac13af9137366fa51) |
| Source | [https://journalclub.io/episodes/random-k-conditional-nearest-neighbor-for-high-dimensional-data](https://journalclub.io/episodes/random-k-conditional-nearest-neighbor-for-high-dimensional-data) |
| Source | [https://www.semanticscholar.org/paper/de2abb6e0817f95db9f6b5fac13af9137366fa51](https://www.semanticscholar.org/paper/de2abb6e0817f95db9f6b5fac13af9137366fa51) |
| Year | 2026 |
| Citations | 7 |
| Authors | Jiaxuan Lu, Hyukjun Gweon |
| Paper ID | `e6ba547d-e032-4e5a-9ab2-af082a33b173` |

## Classification

- **Problem Type:** classification
- **Domain:** Machine Learning & AI
- **Sub-domain:** k-Nearest Neighbors
- **Technique:** Random k Conditional Nearest Neighbor (RkCNN)
- **Technique Category:** classification_model
- **Type:** novel

## Summary

The paper introduces the Random k Conditional Nearest Neighbor (RkCNN) method, an enhancement of the k-Nearest Neighbors (kNN) algorithm designed to improve classification performance in high-dimensional data by aggregating multiple kCNN classifiers built on random feature subsets. Engineers should care because this method addresses the challenges posed by noisy features and the curse of dimensionality, making it applicable in various domains such as gene expression analysis.

## Key Contribution

**The introduction of RkCNN, which combines multiple kCNN classifiers from random feature subsets and weights them based on their informativeness for improved classification accuracy.**

## Problem

The work is motivated by the need to improve classification accuracy in high-dimensional datasets that often contain many irrelevant features.

## Method

**Approach:** RkCNN constructs multiple kCNN classifiers using random subsets of features and aggregates their predictions based on a separation score that quantifies the informativeness of each subset. The final classification is determined by the weighted average of the class probabilities from the selected classifiers.

**Algorithm:**

1. 1. For each of the h random feature subsets, sample m features from the feature space.
2. 2. Calculate the separation score for each feature subset.
3. 3. Sort the separation scores in descending order.
4. 4. Select the top r feature subsets based on their separation scores.
5. 5. Construct a kCNN model for each of the top r subsets.
6. 6. Calculate the predicted probabilities for each class from each kCNN model.
7. 7. Aggregate the probabilities using weighted averaging based on the separation scores.

**Input:** Feature matrix X of size n x q, where n is the number of instances and q is the number of features.

**Output:** Predicted class probabilities for a new instance.

**Key Parameters:**

- `k: number of nearest neighbors (recommended small value, e.g., 1)`
- `m: number of features in each random subset (recommended small to moderate value, e.g., 10-20)`
- `r: number of contributing subsets (recommended larger value, e.g., 200)`
- `h: total number of random feature subsets (h should be greater than or equal to r, e.g., h = r, 2r, ..., 10r)`

**Complexity:** Not stated.

## Benchmarks

**Tested on:** Gene expression datasets

**Results:**

- Classification accuracy

**Compared against:** Standard kNN, kCNN

**Improvement:** RkCNN shows improved predictive classification performance compared to traditional kNN methods, particularly in high-dimensional settings.

## Implementation Guide

**Data Structures:** Feature matrix (numpy array), List of separation scores

**Dependencies:** NumPy, scikit-learn

**Core Operation:**

```python
for j in range(h): sample_features = random.sample(features, m); score = calculate_separation_score(sample_features); ...
```

**Watch Out For:**

- Ensure that the number of features m is not too large to avoid redundancy.
- Monitor the balance between r and h to optimize performance without excessive computation.
- Be cautious of overfitting when using too many contributing subsets.

## Use This When

- You have a high-dimensional dataset with many irrelevant features.
- You need to improve classification accuracy in noisy environments.
- You want to leverage ensemble methods for better model robustness.

## Don't Use When

- The dataset has a low number of features and instances.
- Real-time classification is critical and computational resources are limited.
- You require a simple, interpretable model without ensemble complexity.

## Key Concepts

k-Nearest Neighbors, High-dimensional data, Ensemble methods, Separation score, Random feature subsets, Classification performance

## Connects To

- k-Nearest Neighbors (kNN)
- k Conditional Nearest Neighbor (kCNN)
- Bagging methods
- Random Forests
- Feature selection techniques

## Prerequisites

- Understanding of k-Nearest Neighbors algorithm.
- Familiarity with ensemble learning concepts.
- Knowledge of high-dimensional data challenges.

## Limitations

- Performance may degrade with extremely high-dimensional datasets if too many irrelevant features are present.
- Computational cost increases with larger values of r and h.
- Requires careful tuning of parameters for optimal performance.

## Open Questions

- How can RkCNN be adapted for real-time classification tasks?
- What are the optimal strategies for feature selection in different domains?

## Abstract

Today’s paper is about advancements in an algorithm called k-Nearest Neighbors. If you’ve listened to some of our Machine-Learning episodes, you’ve undoubtedly heard that term before. k-Nearest Neighbors (or kNN for short) is everywhere, and is used for everything. Why? Because it’s simple and it's effective. It’s not necessarily always the best tool for the job (and later we’re going to see how these authors are trying to modify it to be better at more things), but it is pretty good at a lot of use-cases. That’s why you’ll see kNNs used in ecology, in linguistics, in sports analytics, and even in archaeology. So before we get into this paper, let’s talk about kNN for a while. How does it work? What do “distances in feature space” even mean? And why is this algorithm so good at calculating them? Let’s get into it.
