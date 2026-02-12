# An evolutionary game theory analysis on the environmental impact of discharging Fukushima’s nuclear wastewater: International stakeholders and strategic dynamics

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1371/journal.pone.0317419` |
| Full Paper | [https://doi.org/10.1371/journal.pone.0317419](https://doi.org/10.1371/journal.pone.0317419) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/ad2ef6983ad4220b1a5eb662afb775629d15721c](https://www.semanticscholar.org/paper/ad2ef6983ad4220b1a5eb662afb775629d15721c) |
| Source | [https://journalclub.io/episodes/an-evolutionary-game-theory-analysis-on-the-environmental-impact-of-discharging-fukushimas-nuclear-wastewater-international-stakeholders-and-strategic-dynamics](https://journalclub.io/episodes/an-evolutionary-game-theory-analysis-on-the-environmental-impact-of-discharging-fukushimas-nuclear-wastewater-international-stakeholders-and-strategic-dynamics) |
| Source | [https://www.semanticscholar.org/paper/ad2ef6983ad4220b1a5eb662afb775629d15721c](https://www.semanticscholar.org/paper/ad2ef6983ad4220b1a5eb662afb775629d15721c) |
| Year | 2026 |
| Citations | 0 |
| Authors | Mingyang Li, Han Pengsihua, Songqing Zhao, Zejun Wang, Limin Yang, Tongjing Liu |
| Paper ID | `605cb6d3-b5ff-442f-8236-48a6e14f6c8a` |

## Classification

- **Problem Type:** multi-agent decision-making
- **Domain:** Optimization & Operations Research
- **Sub-domain:** Evolutionary Game Theory
- **Technique:** Evolutionary Game Theory Model
- **Technique Category:** statistical_method
- **Type:** novel

## Summary

This paper presents an evolutionary game theory model to analyze the strategic dynamics between Japan, other countries, and the Japan Fisheries Association regarding the discharge of Fukushima's nuclear wastewater. Engineers should care because this model provides insights into stakeholder interactions and decision-making processes that can inform policy and management strategies in environmental crises.

## Key Contribution

**The development of a tripartite evolutionary game model to analyze the strategic interactions among Japan, other countries, and the Japan Fisheries Association regarding nuclear wastewater discharge.**

## Problem

The need to manage the environmental impact and stakeholder responses to Japan's decision to discharge nuclear wastewater into the ocean.

## Method

**Approach:** The method models the decision-making processes of Japan, other countries, and the Japan Fisheries Association using evolutionary game theory. Each player adapts their strategies based on the outcomes of their decisions and the decisions of others over time.

**Algorithm:**

1. Define the players: Japan (J), other countries (C), and the Japanese Fisheries Association (F).
2. Establish the strategies available to each player (e.g., discharge or not for Japan, sanction or not for other countries).
3. Formulate the utility functions for each player based on their strategies and associated costs/benefits.
4. Derive the replicator dynamics equations for each player to model the evolution of strategies over time.
5. Simulate the model under various scenarios to analyze the stability and outcomes of different strategies.

**Input:** Probabilities of strategies (x for Japan, y for other countries, z for Fisheries Association), costs and benefits associated with each strategy.

**Output:** Evolutionarily stable strategies (ESS) and their expected utilities for each player.

**Key Parameters:**

- `x: Probability of Japan choosing to discharge (0 <= x <= 1)`
- `y: Probability of other countries choosing to sanction (0 <= y <= 1)`
- `z: Probability of Fisheries Association opposing discharge (0 <= z <= 1)`
- `CDJ: Cost of Japanese discharge`
- `CSJ: Cost of storing nuclear wastewater`
- `IJ: International image impact for Japan`
- `CIF: International image impact for Fisheries Association`
- `ERF: Revenue reduction for Fisheries Association due to discharge`
- `TRJ: Export tax revenue reduction for Japan due to discharge`
- `CSC: Additional cost for other countries to develop seafood products`

**Complexity:** Not stated

## Benchmarks

**Tested on:** International environmental reports, economic statistics related to nuclear wastewater discharge

**Results:**

- Expected utility values for each player, stability of strategies

**Compared against:** Previous models of stakeholder interactions without evolutionary dynamics

**Improvement:** Provides a more comprehensive understanding of strategic interactions compared to prior models.

## Implementation Guide

**Data Structures:** Payoff matrices for each stakeholder, Probability distributions for strategies

**Dependencies:** Python for simulations, NumPy for numerical calculations

**Core Operation:**

```python
while not converged: update strategies based on replicator dynamics equations
```

**Watch Out For:**

- Ensure accurate parameter values to reflect real-world scenarios
- Consider the impact of external factors not included in the model

## Use This When

- Modeling strategic interactions in environmental policy decisions.
- Analyzing multi-agent decision-making scenarios.
- Evaluating the impact of stakeholder strategies on environmental outcomes.

## Don't Use When

- The problem does not involve multiple stakeholders with conflicting interests.
- The decision-making process is based on perfect information and rationality.

## Key Concepts

Evolutionarily Stable Strategy, Replicator Dynamics, Stakeholder Interaction, Cost-Benefit Analysis

## Connects To

- Game Theory
- Multi-Agent Systems
- Environmental Economics

## Prerequisites

- Basic understanding of game theory concepts
- Familiarity with evolutionary dynamics
- Knowledge of environmental policy frameworks

## Limitations

- Assumes bounded rationality among stakeholders
- Does not account for political factors influencing decisions
- Focuses solely on economic perspectives

## Open Questions

- How can the model be adapted to include more stakeholders?
- What are the long-term implications of the strategies identified?

## Abstract

In classic game theory, players make rational decisions based on perfect information. But in real life, especially in complex environmental crises, information is limited, and rationality is bounded. That's where evolutionary game theory excels. It acknowledges that players don't instantly arrive at optimal strategies but rather adapt their approaches over time based on what they learn. The researchers created a model that gives each player two options: Japan can choose to either discharge the wastewater, or not. Other countries can choose to sanction Japan, or not. The JFA can choose to support the Japanese government, or not. Each choice carries costs and benefits. For Japan, discharging wastewater reduces storage costs but could damage their international image and lead to potential economic penalties. Other countries might gain political points by sanctioning Japan but doing so could disrupt valuable trade relationships. The JFA could
