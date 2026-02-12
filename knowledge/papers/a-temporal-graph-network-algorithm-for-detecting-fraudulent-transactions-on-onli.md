# A Temporal Graph Network Algorithm for Detecting Fraudulent Transactions on Online Payment Platforms

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3390/a17120552` |
| Full Paper | [https://doi.org/10.3390/a17120552](https://doi.org/10.3390/a17120552) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/ff6c5af42fca3483c3994631f8d82b553571d2c9](https://www.semanticscholar.org/paper/ff6c5af42fca3483c3994631f8d82b553571d2c9) |
| Source | [https://journalclub.io/episodes/a-temporal-graph-network-algorithm-for-detecting-fraudulent-transactions-on-online-payment-platforms](https://journalclub.io/episodes/a-temporal-graph-network-algorithm-for-detecting-fraudulent-transactions-on-online-payment-platforms) |
| Source | [https://www.semanticscholar.org/paper/ff6c5af42fca3483c3994631f8d82b553571d2c9](https://www.semanticscholar.org/paper/ff6c5af42fca3483c3994631f8d82b553571d2c9) |
| Year | 2026 |
| Citations | 4 |
| Authors | Diego Saldaña-Ulloa, Guillermo De Ita Luna, J. R. Marcial-Romero |
| Paper ID | `304b739d-92f3-4daa-bb5e-19bfa22abd45` |

## Classification

- **Problem Type:** fraud detection
- **Domain:** Cybersecurity
- **Sub-domain:** Fraud detection
- **Technique:** Temporal Graph Network (TGN)
- **Technique Category:** neural_architecture
- **Type:** novel

## Summary

The paper presents a Temporal Graph Network (TGN) algorithm designed to detect fraudulent transactions on online payment platforms by modeling transactions as dynamic event-based temporal graphs. Engineers should care because this approach leverages temporal interactions to improve fraud detection accuracy, particularly in high-fraud regions like Latin America.

## Key Contribution

**Introduction of an Event-Based Temporal Graph (ETG) approach for fraud detection using a Temporal Graph Network (TGN).**

## Problem

The work addresses the real-world problem of increasing fraudulent transactions on online payment platforms, particularly in Latin America, which has the highest fraud rate globally.

## Method

**Approach:** The method utilizes an Event-Based Temporal Graph (ETG) to represent transactions as a dynamic graph where vertices and edges evolve over time based on transaction events. The TGN processes these graphs using a message-passing mechanism to classify transactions as fraudulent or legitimate.

**Algorithm:**

1. 1. Initialize memory states and raw messages.
2. 2. For each epoch, iterate through batches of events in the training set.
3. 3. Compute messages based on the current state.
4. 4. Aggregate messages from neighboring vertices.
5. 5. Update memory states with aggregated messages.
6. 6. Compute embeddings for the vertices involved in the transaction.
7. 7. Apply a sigmoid function to predict the class of the transaction.
8. 8. Calculate the weighted cross-entropy loss and update model parameters.

**Input:** Event-Based Temporal Graph (ETG) containing vertices, edges, and timestamps of transactions.

**Output:** Predicted class labels for transactions (fraudulent or normal) along with evaluation metrics like F1 score and AUC.

**Key Parameters:**

- `train_ratio: 0.7`
- `validation_ratio: 0.15`
- `test_ratio: 0.15`
- `n_epochs: 100`

**Complexity:** Not stated.

## Benchmarks

**Tested on:** Real transaction data from an online payment platform in Latin America.

**Results:**

- F1 score
- AUC

**Compared against:** Traditional machine learning algorithms like decision trees and neural networks.

**Improvement:** The paper demonstrates that integrating more interaction events into the graph improves detection metrics significantly, though specific percentage improvements are not quantified.

## Implementation Guide

**Data Structures:** Graph data structure for ETG, Memory states for message passing

**Dependencies:** PyTorch, NetworkX, NumPy

**Core Operation:**

```python
for each batch (u, v, e, t) in GEtrain: mem = msg(mem_raw); mem = agg(mem); states = update(mem, states); y = sigmoid(emb(u, t));
```

**Watch Out For:**

- Ensure that the input data is properly formatted as an ETG.
- Monitor for class imbalance in the dataset and apply class weighting if necessary.
- Be cautious of overfitting, especially with a complex model and limited data.

## Use This When

- You need to detect fraudulent transactions in a dynamic environment.
- You have access to time-stamped transaction data.
- You want to leverage the relationships between different entities involved in transactions.

## Don't Use When

- You are working with static transaction data without temporal information.
- You require real-time processing with extremely low latency.
- You have a very small dataset that cannot effectively train a neural network.

## Key Concepts

Temporal Graphs, Event-Based Temporal Graphs, Message Passing, Graph Neural Networks, Fraud Detection, Dynamic Graphs

## Connects To

- Graph Convolutional Networks (GCN)
- Recurrent Neural Networks (RNN)
- Attention Mechanisms
- Dynamic Graphs
- Temporal Data Analysis

## Prerequisites

- Understanding of Graph Neural Networks
- Familiarity with temporal data processing
- Knowledge of fraud detection techniques

## Limitations

- The approach may not perform well with static data.
- Requires a significant amount of labeled data for effective training.
- Performance may vary based on the quality of the input graph structure.

## Open Questions

- How can the model be adapted for real-time fraud detection?
- What additional features could further enhance detection accuracy?

## Abstract

Temporal Graph Networks (TGNs) extend GNNs by incorporating time-sensitive interactions into the graph structure. Unlike static graphs, which capture a frozen view of relationships, temporal graphs model how relationships evolve over time. TGNs process sequences of time-stamped events, making them well-suited for dynamic environments like online payment systems where transactions occur continuously. Each time a relevant event happens—such as a credit card being linked to a device or a payment being made—TGNs update their understanding of the network state. TGNs rely on event-based temporal graphs (ETGs) rather than snapshot-based graphs. Snapshot-based graphs divide
