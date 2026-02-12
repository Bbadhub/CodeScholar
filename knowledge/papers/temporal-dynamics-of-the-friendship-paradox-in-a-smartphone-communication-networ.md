# Temporal dynamics of the friendship paradox in a smartphone communication network

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1007/s41109-025-00710-1` |
| Full Paper | [https://doi.org/10.1007/s41109-025-00710-1](https://doi.org/10.1007/s41109-025-00710-1) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/24caf4c033afb1c2a27073a1bea38d0a8df65a59](https://www.semanticscholar.org/paper/24caf4c033afb1c2a27073a1bea38d0a8df65a59) |
| Source | [https://journalclub.io/episodes/temporal-dynamics-of-the-friendship-paradox-in-a-smartphone-communication-network](https://journalclub.io/episodes/temporal-dynamics-of-the-friendship-paradox-in-a-smartphone-communication-network) |
| Source | [https://www.semanticscholar.org/paper/24caf4c033afb1c2a27073a1bea38d0a8df65a59](https://www.semanticscholar.org/paper/24caf4c033afb1c2a27073a1bea38d0a8df65a59) |
| Year | 2026 |
| Citations | 1 |
| Authors | Cheng Wang, Omar Lizardo, David S. Hachen |
| Paper ID | `29e4f77b-866f-41bf-a9d5-7b4d9643a29d` |

## Classification

- **Problem Type:** social network analysis, temporal dynamics, friendship paradox
- **Domain:** Social Network Analysis
- **Sub-domain:** Temporal Dynamics of Social Networks
- **Technique:** Friendship Index
- **Technique Category:** statistical_method
- **Type:** novel

## Summary

This study investigates the temporal dynamics of the friendship paradox using smartphone communication data from over 600 students. Engineers should care because understanding this phenomenon can inform the design of social networks and interventions that mitigate distorted social perceptions.

## Key Contribution

**The introduction of a dynamic friendship index that tracks the evolution of the friendship paradox over time.**

## Problem

The friendship paradox leads individuals to misjudge social norms based on the degree disparity between themselves and their friends.

## Method

**Approach:** The method calculates a dynamic friendship index that measures the ratio of the average degree of an individual's friends to their own degree over time. This allows for tracking how the friendship paradox evolves as the network develops.

**Algorithm:**

1. 1. Collect smartphone communication data over a specified period.
2. 2. Construct undirected networks daily based on interactions.
3. 3. Calculate the degree of each node (individual) in the network.
4. 4. Compute the average degree of each individual's friends.
5. 5. Calculate the friendship index for each individual at each time point.
6. 6. Analyze the temporal changes in the friendship index.

**Input:** Smartphone communication records detailing interactions among individuals.

**Output:** Dynamic friendship index values for each individual over time.

**Key Parameters:**

- `time_period: 119 days`
- `number_of_participants: 692`
- `communication_records: over 60 million`

**Complexity:** Not stated

## Benchmarks

**Tested on:** NetHealth dataset from 692 undergraduate students at the University of Notre Dame

**Results:**

- friendship index
- degree of individuals
- average degree of alters

**Compared against:** Static friendship index from previous studies

**Improvement:** The dynamic friendship index provides a more nuanced understanding of the friendship paradox compared to static measures.

## Implementation Guide

**Data Structures:** Graph representation of individuals and their connections, Data structures for storing communication records

**Dependencies:** NetworkX (for network analysis), Pandas (for data manipulation), NumPy (for numerical calculations)

**Core Operation:**

```python
for each day in time_period: construct_network(data); calculate_friendship_index(network);
```

**Watch Out For:**

- Ensure data privacy and ethical considerations when collecting communication data.
- Account for missing data in communication records.
- Be cautious of biases in self-reported friendship data.

## Use This When

- Designing social networks that aim to mitigate distorted perceptions of social norms.
- Analyzing communication patterns in educational or workplace settings.
- Studying the influence of highly connected individuals on group behavior.

## Don't Use When

- The network is static and does not evolve over time.
- Data on individual interactions is not available.
- The focus is solely on individual behaviors without considering network effects.

## Key Concepts

friendship paradox, dynamic networks, social norms, degree disparity

## Connects To

- Social network analysis techniques
- Graph theory
- Temporal data analysis

## Prerequisites

- Understanding of graph theory
- Familiarity with social network analysis
- Basic statistical methods

## Limitations

- The study is limited to a specific demographic (undergraduate students).
- Results may not generalize to other types of social networks.
- The reliance on self-reported data may introduce biases.

## Open Questions

- How do different types of social networks influence the friendship paradox?
- What interventions can effectively mitigate the effects of the friendship paradox?

## Abstract

In his book The Tipping Point, Malcolm Gladwell describes the three types of people you need to get a movement or a phenomenon to “tip.” That is, to get it to break out of a subculture and into the mainstream. Mavens, who accumulate and share knowledge. Salesmen, who persuade and influence others. Connectors, who know lots of people and link different social groups together. That last group, connectors, is what we're talking about today. Imagine that you and all your friends are "nodes" in a graph. If you have a friendship with someone, that friendship itself is an "edge" connecting you two. As you zoom out from the graph you see an interconnected web of friendships and friend-groups. Now imagine that, out of a few hundred nodes, there are a couple nodes with far more edges leading towards them. For every friendship you have, they might have 10. These are the connectors. The social butterflies. The popular kids. We call them high-degree nodes. The virtue of their extreme connectedness means that their very existence creates a statistical phenomenon called the Friendship Paradox.
