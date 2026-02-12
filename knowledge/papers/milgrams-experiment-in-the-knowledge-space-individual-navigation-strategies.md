# Milgram’s experiment in the knowledge space: individual navigation strategies

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1140/epjds/s13688-025-00558-6` |
| Full Paper | [https://doi.org/10.1140/epjds/s13688-025-00558-6](https://doi.org/10.1140/epjds/s13688-025-00558-6) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/21541eb6ed78c5c686f0ae3d3029ec8c5321cc0a](https://www.semanticscholar.org/paper/21541eb6ed78c5c686f0ae3d3029ec8c5321cc0a) |
| Source | [https://journalclub.io/episodes/milgrams-experiment-in-the-knowledge-space-individual-navigation-strategies](https://journalclub.io/episodes/milgrams-experiment-in-the-knowledge-space-individual-navigation-strategies) |
| Source | [https://www.semanticscholar.org/paper/21541eb6ed78c5c686f0ae3d3029ec8c5321cc0a](https://www.semanticscholar.org/paper/21541eb6ed78c5c686f0ae3d3029ec8c5321cc0a) |
| Year | 2026 |
| Citations | 1 |
| Authors | Manran Zhu, J. Kertész |
| Paper ID | `3dda8faa-a44b-404e-b94e-f2797a08b7e1` |

## Classification

- **Problem Type:** navigation strategy analysis
- **Domain:** Machine Learning & AI
- **Sub-domain:** Graph embedding, Navigation strategies
- **Technique:** DeepWalk
- **Technique Category:** statistical_method
- **Type:** adaptation

## Summary

This study explores individual navigation strategies in the knowledge space using a Wikipedia navigation game, revealing significant differences in how people navigate based on demographic factors. Engineers should care because understanding these strategies can inform the design of better information systems and enhance user experience in digital environments.

## Key Contribution

**Identification of hub-driven and proximity-driven navigation strategies in knowledge space based on individual differences.**

## Problem

The challenge of efficiently navigating through vast amounts of information online, particularly in knowledge networks like Wikipedia.

## Method

**Approach:** Participants navigated from one Wikipedia page to another using hyperlinks, and their navigation paths were analyzed to identify strategies. A graph embedding was trained on the Wikipedia network to quantify distances and hierarchical scores of articles.

**Algorithm:**

1. 1. Participants play the Wikipedia navigation game.
2. 2. Record the sequence of visited articles.
3. 3. Calculate the closeness score using cosine similarity.
4. 4. Calculate the hierarchical score based on in-degree and out-degree.
5. 5. Classify navigation paths as hub-driven or proximity-driven.
6. 6. Analyze the impact of demographic factors on navigation strategies.

**Input:** Participants' navigation paths on Wikipedia and demographic information.

**Output:** Classification of navigation strategies (hub-driven or proximity-driven) and performance metrics.

**Key Parameters:**

- `embedding_dimension: 64`
- `time_limit: 150 seconds (Speed-race game)`
- `max_clicks: 7 (Least-clicks game)`

**Complexity:** not stated

## Benchmarks

**Tested on:** English Wikipedia (20190820 Wiki Dump)

**Results:**

- time saved (seconds)
- steps saved

**Compared against:** Previous navigation studies on Wikipedia

**Improvement:** Hub-driven strategy improved performance in timed games, while proximity-driven strategy was less effective.

## Implementation Guide

**Data Structures:** Graph structure of Wikipedia articles, User navigation paths

**Dependencies:** DeepWalk implementation, Data processing libraries (e.g., NumPy, Pandas)

**Core Operation:**

```python
for each path in navigation_paths: calculate_hub_proximity_scores(path)
```

**Watch Out For:**

- Ensure accurate mapping of Wikipedia articles to their hierarchical scores.
- Consider demographic factors when analyzing navigation strategies.
- Account for potential biases in user navigation behavior.

## Use This When

- Designing educational tools that require efficient information retrieval.
- Creating user interfaces for knowledge-based applications.
- Analyzing user behavior in navigation-heavy applications.

## Don't Use When

- The application does not involve knowledge networks.
- Real-time navigation is not a priority.
- User demographics are not relevant to the navigation strategy.

## Key Concepts

graph embedding, navigation strategies, hub-driven, proximity-driven, Wikipedia navigation, individual differences

## Connects To

- social navigation theory
- information retrieval systems
- user experience design

## Prerequisites

- Understanding of graph theory
- Familiarity with navigation algorithms
- Knowledge of user behavior analysis

## Limitations

- Results may not generalize beyond Wikipedia
- Demographic factors may not capture all individual differences
- Limited to online navigation scenarios

## Open Questions

- How do different cultures influence navigation strategies?
- What are the implications for AI-driven navigation systems?

## Abstract

This study takes inspiration from Stanley Milgram’s famous “small world” experiment from the 1960s. In it, participants tried to get a letter to a stranger in another city by sending it only to people they knew personally (through their social network). Milgram wanted to measure how connected people actually were. The result, that it took about six handoffs on average, gave rise to the idea of “six degrees of separation.” In this study, the researchers moved that concept into the digital realm: instead of passing letters through friends-of-friends, participants had to navigate from one Wikipedia page to another using only links. What they discovered challenges how we think about both digital literacy and human cognition.
