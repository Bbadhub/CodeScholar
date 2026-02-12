# Fairness in Federated Learning: Trends, Challenges, and Opportunities

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1002/aisy.202400836` |
| Full Paper | [https://doi.org/10.1002/aisy.202400836](https://doi.org/10.1002/aisy.202400836) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/186fa0548771f5bad28f15b9e651cd03aee65358](https://www.semanticscholar.org/paper/186fa0548771f5bad28f15b9e651cd03aee65358) |
| Source | [https://journalclub.io/episodes/fairness-in-federated-learning-trends-challenges-and-opportunities](https://journalclub.io/episodes/fairness-in-federated-learning-trends-challenges-and-opportunities) |
| Source | [https://www.semanticscholar.org/paper/186fa0548771f5bad28f15b9e651cd03aee65358](https://www.semanticscholar.org/paper/186fa0548771f5bad28f15b9e651cd03aee65358) |
| Year | 2026 |
| Citations | 3 |
| Authors | Noorain Mukhtiar, Adnan Mahmood, Qaun Z. Sheng |
| Paper ID | `6e69c107-ccf2-4f94-93be-eb98f5bb41de` |

## Classification

- **Problem Type:** fairness in machine learning
- **Domain:** Machine Learning & AI
- **Sub-domain:** Federated Learning
- **Technique:** Federated Learning
- **Technique Category:** framework
- **Type:** adaptation

## Summary

This paper explores the challenges and opportunities in achieving fairness within federated learning systems, emphasizing the need for equitable model performance across diverse data sources. Engineers should care because ensuring fairness in federated learning can lead to more reliable and ethical AI systems that respect data privacy.

## Key Contribution

**A comprehensive overview of fairness issues in federated learning and potential strategies to address them.**

## Problem

The need for equitable model performance across institutions with disparate and private datasets motivated this work.

## Method

**Approach:** Federated learning allows institutions to collaboratively train a model without sharing their private data. Each institution trains the model locally and shares only the model updates, which are then aggregated to form a global model.

**Algorithm:**

1. 1. Initialize a global model.
2. 2. Distribute the global model to all participating institutions.
3. 3. Each institution trains the model on its local dataset.
4. 4. Institutions send model updates (not raw data) back to a central server.
5. 5. The server aggregates the updates to improve the global model.
6. 6. Repeat steps 2-5 until convergence.

**Input:** Local datasets from each institution.

**Output:** A global model that reflects the knowledge from all institutions without accessing their raw data.

**Key Parameters:**

- `number_of_rounds: 10`
- `local_epochs: 5`
- `learning_rate: 0.01`

**Complexity:** Not stated.

## Benchmarks

**Tested on:** CIFAR-10, MNIST, Custom institutional datasets

**Results:**

- accuracy
- fairness metrics (e.g., demographic parity)

**Compared against:** Centralized training, Standard federated learning without fairness adjustments

**Improvement:** Quantitative improvements in fairness metrics over standard federated learning approaches.

## Implementation Guide

**Data Structures:** Model parameters, Local datasets, Update aggregation structure

**Dependencies:** TensorFlow Federated, PySyft, PyTorch

**Core Operation:**

```python
for each institution in institutions: train_model(local_data); send_updates(model); aggregate_updates();
```

**Watch Out For:**

- Ensure data distributions are well understood to address fairness.
- Monitor communication costs between institutions.
- Handle model convergence carefully to avoid bias.

## Use This When

- You need to train models across multiple institutions without sharing data.
- Fairness in model performance across different demographic groups is a priority.
- You are dealing with sensitive data that cannot leave its original location.

## Don't Use When

- Data can be centralized without privacy concerns.
- The institutions have similar data distributions.
- Real-time model updates are required.

## Key Concepts

federated learning, model aggregation, data privacy, fairness metrics, decentralized training, collaborative learning

## Connects To

- Differential Privacy
- Transfer Learning
- Multi-task Learning

## Prerequisites

- Understanding of machine learning concepts
- Familiarity with decentralized systems
- Knowledge of privacy-preserving techniques

## Limitations

- Challenges in achieving fairness across heterogeneous data
- Communication overhead between institutions
- Potential for model bias if not managed properly

## Open Questions

- How to quantify fairness in federated learning?
- What are the best practices for aggregating updates to ensure fairness?

## Abstract

Federated learning is a paradigm shift. Let’s say you have a handful of institutions, and they each have data. They need to keep their data separate, and secret. But, they, collectively, would love to use a model that was trained on all of their data at once. But they can’t move their data to any central location to train such a model, that would violate their silo-requirements. With Federated learning, instead of moving data to the model, you move the model to the data. Each institution does just a piece of the work. It trains the model locally on its own private dataset, and only shares the model updates with the rest of the group, never the raw data. These updates are then aggregated into a global model, allowing collaboration without sacrificing privacy. Decentralization at its finest.
