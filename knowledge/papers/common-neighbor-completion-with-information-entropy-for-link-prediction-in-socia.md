# Common Neighbor Completion with Information Entropy for Link Prediction in Social Networks

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1007/s41019-024-00267-6` |
| Full Paper | [https://doi.org/10.1007/s41019-024-00267-6](https://doi.org/10.1007/s41019-024-00267-6) |
| Source | [https://journalclub.io/episodes/common-neighbor-completion-with-information-entropy-for-link-prediction-in-social-networks](https://journalclub.io/episodes/common-neighbor-completion-with-information-entropy-for-link-prediction-in-social-networks) |
| Year | 2026 |
| Citations | 0 |
| Authors |  |
| Paper ID | `a437fd0e-cb0a-4863-a35b-c9e9b3ad0320` |

## Classification

- **Problem Type:** link prediction
- **Domain:** Machine Learning & AI
- **Sub-domain:** Graph Neural Networks
- **Technique:** Common Neighbor Completion with Information Entropy (IECNC)
- **Technique Category:** neural_architecture
- **Type:** novel

## Summary

The paper presents a novel approach called Common Neighbor Completion with Information Entropy (IECNC) for link prediction in social networks, enhancing prediction accuracy by leveraging logical neighbor relationships and information entropy. Engineers should care because this method significantly improves the identification of hidden relationships, which is crucial for applications like social networking and recommendation systems.

## Key Contribution

**Introduction of IECNC, which integrates information entropy with a Message Passing Neural Network to enhance link prediction accuracy by considering common neighbor relationships.**

## Problem

The work addresses the challenge of predicting potential relationships in social networks, which are often incomplete and complex.

## Method

**Approach:** IECNC uses a Message Passing Neural Network (MPNN) to aggregate features from common neighbors and incorporates information entropy to quantify uncertainty in link predictions. The method enhances model expressiveness by focusing on logical relationships among neighbors.

**Algorithm:**

1. 1. Extract logical relationships of neighbors from the subgraph.
2. 2. Compute node features using MPNN.
3. 3. Calculate probabilities of common neighbors using softmax.
4. 4. Assess uncertainty using information entropy.
5. 5. Combine probabilities and entropy to predict links between nodes.

**Input:** Graph data represented as an adjacency matrix and node feature matrix.

**Output:** Predicted probabilities for potential links between node pairs.

**Key Parameters:**

- `learning_rate: 0.001`
- `number_of_layers: 3`
- `hidden_units_per_layer: 64`

**Complexity:** Not stated.

## Benchmarks

**Tested on:** Cora, Citeseer, Pubmed, twitch_RU, twitch_PT

**Results:**

- HITS@100

**Compared against:** Graph Autoencoders (GAE), Subgraph Embedding-based Link Prediction (SEAL), NEO-GNN, BUDDY

**Improvement:** Achieved leading HITS@100 scores, outperforming existing techniques.

## Implementation Guide

**Data Structures:** Adjacency matrix, Node feature matrix, Graph representation

**Dependencies:** PyTorch, NetworkX, NumPy

**Core Operation:**

```python
def predict_link(node_i, node_j): return sigmoid(aggregate_features(node_i, node_j) + compute_entropy(node_i, node_j))
```

**Watch Out For:**

- Ensure the graph data is preprocessed correctly to avoid missing edges.
- Monitor the learning rate to prevent overfitting.
- Be cautious with the choice of activation functions in MPNN.

## Use This When

- Building recommendation systems that suggest potential connections in social networks.
- Analyzing social network data to uncover hidden relationships.
- Developing applications that require accurate link predictions in incomplete graphs.

## Don't Use When

- The graph data is complete and well-structured.
- Real-time predictions are required with minimal latency.
- The relationships between nodes are static and do not evolve.

## Key Concepts

information entropy, link prediction, common neighbors, Message Passing Neural Network, graph incompleteness

## Connects To

- Graph Neural Networks
- Link Prediction Models
- Probabilistic Graph Models

## Prerequisites

- Understanding of graph theory
- Familiarity with neural networks
- Knowledge of information theory

## Limitations

- Performance may degrade with very large graphs due to computational complexity.
- Assumes that the relationships can be captured by common neighbors, which may not always be true.
- Requires careful tuning of parameters for optimal performance.

## Open Questions

- How can the model be adapted for dynamic graphs where relationships change over time?
- What are the implications of using different aggregation functions in MPNN?

## Abstract

Your job is to build a feature that suggests “people you may know”. When a user is browsing around they should see a little box somewhere on the site that lists the users we “think” they might actually already know, but haven’t yet connected with.
