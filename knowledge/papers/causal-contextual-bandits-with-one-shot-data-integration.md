# Causal contextual bandits with one-shot data integration

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3389/frai.2024.1346700` |
| Full Paper | [https://doi.org/10.3389/frai.2024.1346700](https://doi.org/10.3389/frai.2024.1346700) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/bfe46d03f9fbbd26ded58c5be8390d6534449f17](https://www.semanticscholar.org/paper/bfe46d03f9fbbd26ded58c5be8390d6534449f17) |
| Source | [https://journalclub.io/episodes/causal-contextual-bandits-with-one-shot-data-integration](https://journalclub.io/episodes/causal-contextual-bandits-with-one-shot-data-integration) |
| Source | [https://www.semanticscholar.org/paper/bfe46d03f9fbbd26ded58c5be8390d6534449f17](https://www.semanticscholar.org/paper/bfe46d03f9fbbd26ded58c5be8390d6534449f17) |
| Year | 2026 |
| Citations | 1 |
| Authors | Chandrasekar Subramanian, Balaraman Ravindran |
| Paper ID | `a02f8b55-52c8-4f81-a39b-40e1947e2526` |

## Classification

- **Problem Type:** sequential decision-making
- **Domain:** Machine Learning & AI
- **Sub-domain:** Causal Inference, Bandit Algorithms
- **Technique:** CoBA (Causal contextual Bandits with One-shot data integration)
- **Technique Category:** optimization_algorithm
- **Type:** novel

## Summary

The paper presents a novel approach to causal contextual bandits that allows for one-shot data integration, enabling agents to perform multiple targeted experiments simultaneously within a budget. This method is crucial for applications like software experimentation and marketing, where quick and informed decision-making is essential.

## Key Contribution

**Introduction of a causal contextual bandit framework that integrates causal side information and allows for one-shot data acquisition.**

## Problem

The need for efficient decision-making in environments where multiple actions can be tested simultaneously, such as software product experimentation and marketing strategies.

## Method

**Approach:** The method involves maintaining beliefs about conditional probability distributions and selecting samples for multiple context-action pairs to minimize an entropy-like measure under budget constraints. The agent integrates the acquired data to update its policy.

**Algorithm:**

1. Initialize beliefs about CPDs using logged offline data.
2. Specify the number of samples required for each context-action pair.
3. Calculate costs associated with acquiring those samples.
4. Ensure total cost does not exceed the budget.
5. Integrate acquired samples to update beliefs.
6. Learn a policy based on updated beliefs.
7. Evaluate the learned policy and measure regret.

**Input:** Logged offline data consisting of context-action-reward tuples.

**Output:** A learned policy mapping contexts to actions.

**Key Parameters:**

- `budget: B (total cost for acquiring samples)`
- `cost function: β(x, cA, Nx,cA)`
- `number of samples: Nx,cA for each (x, cA)`

**Complexity:** Not stated.

## Benchmarks

**Tested on:** Synthetic data, Real-world inspired dataset

**Results:**

- Regret: O(s(MC/mB - ǫ) ln(MXMC/δ))

**Compared against:** Standard contextual bandit algorithms

**Improvement:** Algorithm outperformed baselines in all experiments.

## Implementation Guide

**Data Structures:** Causal graph representation, Data structures for storing context-action-reward tuples

**Dependencies:** scipy.optimize (for optimization tasks)

**Core Operation:**

```python
policy = learn_policy(logged_data, causal_graph); samples = acquire_samples(policy, budget); update_beliefs(samples);
```

**Watch Out For:**

- Ensure the budget is correctly calculated to avoid overspending.
- Be cautious of information leakage when selecting samples.
- Validate the causal graph to ensure accurate modeling.

## Use This When

- You need to conduct multiple experiments simultaneously within a budget.
- You have causal side information that can inform decision-making.
- You want to minimize regret in a sequential decision-making context.

## Don't Use When

- The environment does not allow for one-shot data acquisition.
- You lack causal side information.
- The cost of acquiring samples is prohibitively high.

## Key Concepts

Causal inference, Contextual bandits, Entropy measure, Targeted interventions, Fairness in algorithms

## Connects To

- Multi-armed bandits
- Active learning
- Reinforcement learning
- Causal inference frameworks

## Prerequisites

- Understanding of causal graphs
- Familiarity with bandit algorithms
- Knowledge of optimization techniques

## Limitations

- Assumes no unobserved confounders.
- Performance may degrade with high costs for sample acquisition.
- Requires accurate causal graph representation.

## Open Questions

- How to generalize the approach to more complex causal structures?
- What are the implications of varying budget constraints on performance?

## Abstract

When you’re playing a slot-machine, you’re making a series of choices based on the information and feedback you’re receiving from the interface. Each pull of the lever represents a decision to act, based on the outcome of previous plays. Over time, you start to gather information about potential rewards, and you must decide whether to continue playing, stop, or change strategies. You are effectively balancing the uncertainty of future rewards against the results you’ve been observing. This is called a sequential decision-making problem, and it is very similar to many other decisions that you, (or another person, or a business, or an autonomous-car) need to make all the time. In many aspects of life, you're taking actions, observing outcomes, and making choices that (ideally) optimize your results over time.
