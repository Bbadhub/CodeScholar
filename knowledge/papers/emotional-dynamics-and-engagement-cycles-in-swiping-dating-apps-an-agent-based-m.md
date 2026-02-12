# Emotional dynamics and engagement cycles in swiping dating apps: An agent-based modeling approach

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1016/j.chbr.2025.100775` |
| Full Paper | [https://doi.org/10.1016/j.chbr.2025.100775](https://doi.org/10.1016/j.chbr.2025.100775) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/c2cb3e736e3ea7455b342971be2728b262f33a4a](https://www.semanticscholar.org/paper/c2cb3e736e3ea7455b342971be2728b262f33a4a) |
| Source | [https://journalclub.io/episodes/emotional-dynamics-and-engagement-cycles-in-swiping-dating-apps-an-agent-based-modeling-approach](https://journalclub.io/episodes/emotional-dynamics-and-engagement-cycles-in-swiping-dating-apps-an-agent-based-modeling-approach) |
| Source | [https://www.semanticscholar.org/paper/c2cb3e736e3ea7455b342971be2728b262f33a4a](https://www.semanticscholar.org/paper/c2cb3e736e3ea7455b342971be2728b262f33a4a) |
| Year | 2026 |
| Citations | 0 |
| Authors | Herald Cela, Michael Vogrin, Thomas Schmickl, Guilherme Wood |
| Paper ID | `68586615-0498-40b1-86f3-edf60db13021` |

## Classification

- **Problem Type:** user engagement modeling
- **Domain:** Human-Computer Interaction
- **Sub-domain:** User engagement modeling
- **Technique:** Agent-based modeling
- **Technique Category:** framework
- **Type:** novel

## Summary

This paper presents an agent-based modeling approach to understand emotional dynamics and engagement cycles in swiping dating apps, highlighting the impact of rapid implicit rejection on user behavior. Engineers should care because this model can inform the design of more user-friendly dating applications that mitigate negative emotional effects.

## Key Contribution

**An agent-based model that simulates user interactions and emotional responses in swiping dating apps.**

## Problem

The need to understand how rapid implicit rejection in swiping dating apps affects user emotions and engagement.

## Method

**Approach:** The method involves creating agents that represent users in a swiping dating app environment. These agents interact based on emotional states influenced by rejection and acceptance, allowing for the simulation of engagement cycles over time.

**Algorithm:**

1. 1. Initialize a population of user agents with emotional states.
2. 2. Simulate swiping interactions where agents evaluate potential matches.
3. 3. Update emotional states based on acceptance or rejection outcomes.
4. 4. Record engagement metrics over multiple cycles.
5. 5. Analyze the impact of rejection frequency on overall user satisfaction.

**Input:** Initial parameters for user agents, including emotional state distributions and rejection rates.

**Output:** Simulation results showing engagement metrics and emotional dynamics over time.

**Key Parameters:**

- `initial_emotional_state: normal`
- `rejection_rate: 0.5`
- `evaluation_time: 2 seconds`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Synthetic user interaction data generated based on typical swiping behaviors.

**Results:**

- user engagement rate, emotional distress level

**Compared against:** Traditional user engagement models without implicit rejection consideration.

**Improvement:** Demonstrated improved understanding of user emotional dynamics compared to baseline models.

## Implementation Guide

**Data Structures:** Agent class to represent users, emotional state variables, interaction history logs

**Dependencies:** NetLogo or AnyLogic for agent-based modeling simulation

**Core Operation:**

```python
for each agent in population: evaluate_match(); update_emotional_state(); log_engagement();
```

**Watch Out For:**

- Ensure emotional state transitions are realistic and based on psychological research.
- Avoid overfitting the model to synthetic data without real-world validation.

## Use This When

- Designing user interfaces for dating apps to enhance user experience.
- Studying the psychological effects of rapid rejection in digital environments.
- Developing algorithms to optimize user engagement in social applications.

## Don't Use When

- Building applications that do not involve user interactions or emotional responses.
- When the focus is on explicit rather than implicit user feedback.
- In scenarios where user behavior is not influenced by emotional states.

## Key Concepts

agent-based modeling, user engagement, emotional dynamics, implicit rejection

## Connects To

- User behavior modeling
- Emotional AI
- Social network analysis

## Prerequisites

- Basic understanding of agent-based modeling
- Familiarity with user engagement metrics
- Knowledge of emotional psychology

## Limitations

- Model may not capture all real-world complexities of human emotions.
- Assumes uniformity in user responses to rejection.
- Dependent on the accuracy of initial parameter settings.

## Open Questions

- How can this model be adapted for different types of social applications?
- What are the long-term effects of using swiping apps on user mental health?

## Abstract

The core idea here is that ‘swiping apps’ expose users to high volumes of what the authors call “subtle/implicit rejection". Unlike face-to-face dating scenarios where rejection might be rarer and more explicit, swiping apps deliver rejection constantly but ambiguously. Previous research has shown that rejection is psychologically distressing (as you’d expect). But swiping apps turn up the velocity. You get rejected, then immediately have to evaluate someone else, then potentially face more rejection, all within a few seconds.
