# An Unsupervised Fake News Detection Framework Based on Structural Contrastive Learning

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1186/s42400-024-00342-5` |
| Full Paper | [https://doi.org/10.1186/s42400-024-00342-5](https://doi.org/10.1186/s42400-024-00342-5) |
| Source | [https://journalclub.io/episodes/an-unsupervised-fake-news-detection-framework-based-on-structural-contrastive-learning](https://journalclub.io/episodes/an-unsupervised-fake-news-detection-framework-based-on-structural-contrastive-learning) |
| Year | 2026 |
| Citations | 0 |
| Authors |  |
| Paper ID | `8381739b-6aa2-45b0-a8b8-fe5cb2bba13a` |

## Classification

- **Problem Type:** fake news detection
- **Domain:** Cybersecurity
- **Sub-domain:** Fake news detection
- **Technique:** Structural Contrastive Learning (SCL)
- **Technique Category:** neural_architecture
- **Type:** novel

## Summary

The paper presents an unsupervised fake news detection framework based on structural contrastive learning, which leverages the propagation structure of news to enhance detection accuracy without requiring labeled data. Engineers should care because this approach addresses the significant challenge of detecting fake news in social media, where annotated datasets are scarce.

## Key Contribution

**The introduction of an unsupervised framework for fake news detection that combines propagation structures with contrastive learning techniques.**

## Problem

The rapid spread of fake news on social media platforms necessitates an automated detection tool that does not rely on extensive labeled datasets.

## Method

**Approach:** The SCL framework uses a twin-network setup to learn representations from augmented views of the same input data. It employs random cropping to create positive instances from the news propagation structure, which are then processed through graph convolutional networks (GCNs) for feature encoding.

**Algorithm:**

1. 1. Perform data augmentation on the news propagation tree using random cropping.
2. 2. Input the two positive instances into the online and target networks.
3. 3. Use GCN to encode the structure features of the news propagation tree.
4. 4. Apply a nonlinear projection to obtain low-dimensional representations.
5. 5. Compute the contrastive loss between the online and target network outputs.
6. 6. Optimize the online network parameters using gradient descent.
7. 7. Update the target network parameters based on a momentum function.

**Input:** News propagation trees represented as graphs with nodes and edges.

**Output:** Predictions of whether news is fake or real.

**Key Parameters:**

- `learning_rate: 0.001`
- `momentum_decay_rate: 0.996`
- `random_cropping_rate: 0.1/0.2/0.3/0.4/0.5`
- `batch_size: 128`
- `hidden_size_of_GCN: 128`
- `output_dimension_of_projection_head: 128`
- `output_dimension_of_prediction_head: 128`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Weibo, Twitter

**Results:**

- Accuracy-Weibo: Not stated
- Accuracy-Twitter: Not stated
- Precision: Not stated
- Recall: Not stated
- F1: Not stated

**Compared against:** Graph-GAN, Random-LR, Random-MLP, C-Means, Twitter-LDA, HDP, BPI, GAN

**Improvement:** SCL improves performance by more than 10% compared to the optimal unsupervised method.

## Implementation Guide

**Data Structures:** Graph structures for news propagation trees, Feature matrices for GCN

**Dependencies:** Pytorch, Dropout method for overfitting prevention

**Core Operation:**

```python
for each news_tree in news_trees: augment_tree = random_crop(news_tree); output = SCL(augment_tree)
```

**Watch Out For:**

- Ensure the random cropping rate is appropriate to avoid losing critical edges.
- Monitor the balance between the online and target network updates to prevent model collapse.
- Be cautious of overfitting when using GCNs with limited data.

## Use This When

- You need to detect fake news without labeled datasets.
- You want to leverage the propagation structure of news for detection.
- You are working with social media data that is rapidly generated.

## Don't Use When

- You have access to large labeled datasets for supervised learning.
- You require real-time detection with minimal latency.
- You need a method that is easily interpretable.

## Key Concepts

contrastive learning, fake news detection, graph convolutional networks, data augmentation, unsupervised learning

## Connects To

- BYOL
- SimCLR
- Graph-GAN
- GCN
- Contrastive learning methods

## Prerequisites

- Understanding of graph structures
- Familiarity with GCNs
- Knowledge of contrastive learning techniques

## Limitations

- Performance may degrade with highly imbalanced datasets.
- The method relies on the quality of the propagation structure.
- Random cropping may not capture all relevant features of the news.

## Open Questions

- How can the framework be adapted for real-time detection?
- What additional features can improve the robustness of the model?

## Abstract

Architecturally, this system is a twin-network setup. It's inspired by bootstrap-based self-supervised learning methods like BYOL. These are training frameworks that learn useful representations without labels by encouraging two differently augmented views of the same input to produce similar outputs. They work by using a slowly updated target network to provide stable training targets for an online network that is optimized directly. The author's system is similar in the way that it uses two networks with shared architecture but different update schedules and trains one to match the other across augmented views of the same data.
