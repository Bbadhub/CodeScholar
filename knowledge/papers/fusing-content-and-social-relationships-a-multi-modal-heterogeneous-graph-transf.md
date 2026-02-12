# Fusing content and social relationships: a multi-modal heterogeneous graph transformer approach for social bot detection

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1140/epjds/s13688-025-00583-5` |
| Full Paper | [https://doi.org/10.1140/epjds/s13688-025-00583-5](https://doi.org/10.1140/epjds/s13688-025-00583-5) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/7f460c87499d7baa27e74fdb3e341a34773c79ef](https://www.semanticscholar.org/paper/7f460c87499d7baa27e74fdb3e341a34773c79ef) |
| Source | [https://journalclub.io/episodes/fusing-content-and-social-relationships-a-multi-modal-heterogeneous-graph-transformer-approach-for-social-bot-detection](https://journalclub.io/episodes/fusing-content-and-social-relationships-a-multi-modal-heterogeneous-graph-transformer-approach-for-social-bot-detection) |
| Source | [https://www.semanticscholar.org/paper/7f460c87499d7baa27e74fdb3e341a34773c79ef](https://www.semanticscholar.org/paper/7f460c87499d7baa27e74fdb3e341a34773c79ef) |
| Year | 2026 |
| Citations | 1 |
| Authors | Jianhong Luo, Chaoqi Jin |
| Paper ID | `93c746c0-f95b-4f42-a09c-b104389e9cdd` |

## Classification

- **Problem Type:** social bot detection
- **Domain:** Cybersecurity
- **Sub-domain:** Social bot detection
- **Technique:** MM-HGT-Bot
- **Technique Category:** framework
- **Type:** novel

## Summary

The paper presents MM-HGT-Bot, a multi-modal framework for detecting social bots by integrating user-generated content with social relationships through a Heterogeneous Graph Transformer. Engineers should care because it offers a robust method to identify complex bot behaviors that traditional methods struggle to detect.

## Key Contribution

**The introduction of a theoretically-informed relational modeling approach that distinguishes between information source selection and potential influence in social networks.**

## Problem

The increasing prevalence of social bots on online platforms, which can manipulate public opinion and disrupt social stability.

## Method

**Approach:** MM-HGT-Bot constructs a heterogeneous graph that encodes users, their relationships, and their tweets. It employs a Heterogeneous Graph Transformer to learn distinct patterns from these relationships and fuses them with content-based representations.

**Algorithm:**

1. 1. Encode user features (numerical, categorical, and description-based).
2. 2. Process the textual content of recent tweets using Doc2vec to create tweet representations.
3. 3. Compute attention scores for tweets based on user features.
4. 4. Aggregate tweet representations using attention scores to create content-aware user representations.
5. 5. Use a fusion gate to combine user features and content-aware representations.
6. 6. Apply the Heterogeneous Graph Transformer to learn relationship-based representations.
7. 7. Classify users as bots or humans based on the combined representations.

**Input:** User metadata, user tweets, and social network relationships.

**Output:** Classification of users as either social bots or human accounts.

**Key Parameters:**

- `learning_rate: 0.001`
- `batch_size: 32`
- `num_epochs: 100`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Cresci-15, Twibot-20

**Results:**

- accuracy
- F1-score

**Compared against:** BotRGCN, RGT, traditional ML classifiers

**Improvement:** MM-HGT-Bot consistently outperforms state-of-the-art baselines.

## Implementation Guide

**Data Structures:** Heterogeneous graph structure, user feature vectors, tweet feature vectors

**Dependencies:** PyTorch, Doc2vec library, Heterogeneous Graph Transformer implementation

**Core Operation:**

```python
user_features = encode_user_features(users); tweet_representations = process_tweets(tweets); combined_representation = fuse(user_features, tweet_representations); classify(combined_representation)
```

**Watch Out For:**

- Ensure proper normalization of numerical features.
- Be cautious with the attention mechanism to avoid overfitting.
- Monitor the balance between user features and content features during fusion.

## Use This When

- You need to detect social bots in social media platforms.
- You want to analyze the interplay between user content and social relationships.
- You require a robust model that integrates multiple data modalities.

## Don't Use When

- You are working with a dataset that lacks rich relational information.
- You need a quick solution without extensive feature engineering.
- You are focused solely on user attributes without considering content.

## Key Concepts

Heterogeneous Graph Transformer, social network theory, multi-modal learning, attention mechanism

## Connects To

- Graph Neural Networks
- Deep Learning for NLP
- Social Network Analysis

## Prerequisites

- Understanding of graph theory
- Familiarity with deep learning frameworks
- Knowledge of social network dynamics

## Limitations

- Requires substantial computational resources for large graphs.
- Performance may degrade with noisy or incomplete data.
- Complexity in tuning hyperparameters for optimal performance.

## Open Questions

- How can the model be adapted for real-time bot detection?
- What additional features could enhance the detection accuracy?

## Abstract

On July 5th 1993, a cartoon drawn by Peter Steiner was published in The New Yorker. In it, two dogs are sitting at a desk in front of a computer. One dog turns to the other and says a now iconic line:"On the Internet, nobody knows you're a dog."
