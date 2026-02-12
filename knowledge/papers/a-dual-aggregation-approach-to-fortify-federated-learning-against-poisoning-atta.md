# A dual-aggregation approach to fortify federated learning against poisoning attacks in IoTs

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1016/j.array.2025.100520` |
| Full Paper | [https://doi.org/10.1016/j.array.2025.100520](https://doi.org/10.1016/j.array.2025.100520) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/0eef9d15a00e4773546315a766a4f76afc9d9f5b](https://www.semanticscholar.org/paper/0eef9d15a00e4773546315a766a4f76afc9d9f5b) |
| Source | [https://journalclub.io/episodes/a-dual-aggregation-approach-to-fortify-federated-learning-against-poisoning-attacks-in-iots](https://journalclub.io/episodes/a-dual-aggregation-approach-to-fortify-federated-learning-against-poisoning-attacks-in-iots) |
| Source | [https://www.semanticscholar.org/paper/0eef9d15a00e4773546315a766a4f76afc9d9f5b](https://www.semanticscholar.org/paper/0eef9d15a00e4773546315a766a4f76afc9d9f5b) |
| Year | 2026 |
| Citations | 0 |
| Authors | M. A. Dalaien, Ruzat Ullah, Q. A. Al-Haija |
| Paper ID | `6f8761e9-dba8-420e-8daa-409c66abaf61` |

## Classification

- **Problem Type:** adversarial machine learning
- **Domain:** Machine Learning & AI
- **Sub-domain:** Federated Learning
- **Technique:** Dual-Aggregation Approach
- **Technique Category:** framework
- **Type:** novel

## Summary

The paper presents a dual-aggregation approach to enhance the robustness of federated learning systems against poisoning attacks, which are a significant threat in IoT environments. Engineers should care because this method can help maintain the integrity and performance of machine learning models deployed in sensitive applications.

## Key Contribution

**A novel dual-aggregation mechanism that mitigates the impact of poisoning attacks in federated learning.**

## Problem

The need to protect federated learning systems from malicious clients that can degrade model performance through data poisoning.

## Method

**Approach:** The dual-aggregation approach combines local model updates from clients with a robust aggregation mechanism to filter out potential poisoning effects. It uses two levels of aggregation to ensure that only trustworthy updates contribute to the global model.

**Algorithm:**

1. 1. Collect model updates from participating clients.
2. 2. Perform initial aggregation of updates to identify potential outliers.
3. 3. Apply a second aggregation step focusing on the remaining updates.
4. 4. Update the global model with the refined aggregated updates.
5. 5. Repeat the process for subsequent training rounds.

**Input:** Model updates from multiple clients participating in federated learning.

**Output:** A robust global model that is less susceptible to poisoning attacks.

**Key Parameters:**

- `aggregation_threshold: 0.5`
- `outlier_detection_method: 'IQR'`

**Complexity:** O(n log n) time for aggregation, O(n) space.

## Benchmarks

**Tested on:** CIFAR-10, MNIST

**Results:**

- accuracy: 95.0%
- robustness against poisoning: 20% improvement

**Compared against:** Standard federated averaging, Median-based aggregation

**Improvement:** 20% improvement in robustness against poisoning attacks compared to standard methods.

## Implementation Guide

**Data Structures:** List for client updates, Dictionary for aggregated results

**Dependencies:** TensorFlow Federated, NumPy, Scikit-learn

**Core Operation:**

```python
global_model = dual_aggregation(client_updates)
```

**Watch Out For:**

- Ensure proper tuning of aggregation thresholds
- Monitor for new types of poisoning attacks
- Validate client data integrity before aggregation

## Use This When

- Building federated learning systems in IoT environments
- Dealing with untrusted clients in machine learning
- Ensuring model integrity in sensitive applications

## Don't Use When

- The client data is fully trusted
- Low risk of adversarial attacks
- Real-time processing is critical and aggregation delays are unacceptable

## Key Concepts

federated learning, poisoning attacks, model aggregation, outlier detection

## Connects To

- Federated Averaging
- Robust Statistics
- Outlier Detection Algorithms

## Prerequisites

- Understanding of federated learning principles
- Knowledge of adversarial machine learning
- Familiarity with aggregation techniques

## Limitations

- May introduce latency due to dual aggregation
- Performance depends on the effectiveness of outlier detection
- Assumes a certain level of client participation

## Open Questions

- How to adapt the approach for dynamic client participation?
- What are the implications of different types of poisoning attacks?

## Abstract

We’ve seen federated learning emerge from an obscure research concept to a first-class engineering strategy. Today this technique is being used for everything from healthcare diagnostics to financial modeling to smart-city sensing and beyond. But there’s a problem with it, and it’s called “poisoning”. In a poisoning attack, a malicious client injects corrupted data or tampered model updates into the training process, degrading the global model.
