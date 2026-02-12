# Modeling supply chain risk events by considering their contributing events: a systematic literature review

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1080/17517575.2025.2472303` |
| Full Paper | [https://doi.org/10.1080/17517575.2025.2472303](https://doi.org/10.1080/17517575.2025.2472303) |
| Source | [https://journalclub.io/episodes/modeling-supply-chain-risk-events-by-considering-their-contributing-events-a-systematic-literature-review](https://journalclub.io/episodes/modeling-supply-chain-risk-events-by-considering-their-contributing-events-a-systematic-literature-review) |
| Year | 2026 |
| Citations | 0 |
| Authors |  |
| Paper ID | `137b432b-8797-4fea-bee0-e5f75c2cb864` |

## Classification

- **Problem Type:** supply chain risk modeling
- **Domain:** Optimization & Operations Research
- **Sub-domain:** Supply Chain Management
- **Technique:** Contributing Events Framework
- **Technique Category:** framework
- **Type:** novel

## Summary

This paper reviews the modeling of supply chain risk events by identifying and analyzing contributing events that lead to disruptions. Engineers should care because understanding these upstream conditions can improve risk management strategies and enhance supply chain resilience.

## Key Contribution

**A systematic framework for modeling supply chain risk events by considering their contributing events.**

## Problem

The need to understand how upstream conditions contribute to supply chain disruptions.

## Method

**Approach:** The method involves identifying contributing events that lead to risk events in supply chains. By systematically analyzing these upstream conditions, the framework aims to provide a more comprehensive understanding of risk dynamics.

**Algorithm:**

1. 1. Identify potential risk events in the supply chain.
2. 2. Gather data on historical disruptions and their contributing events.
3. 3. Analyze the relationships between contributing events and risk events.
4. 4. Develop a model that incorporates these relationships.
5. 5. Validate the model with real-world data.
6. 6. Use the model to predict potential disruptions.

**Input:** Historical data on supply chain disruptions and contributing events.

**Output:** A predictive model that identifies potential risk events based on contributing factors.

**Key Parameters:**

- `data_source: historical disruption data`
- `analysis_method: statistical correlation`

**Complexity:** not stated

## Benchmarks

**Tested on:** Historical supply chain disruption data from various industries.

**Results:**

- accuracy of predictions, reduction in disruption impact

**Compared against:** Traditional risk assessment models that do not consider contributing events.

**Improvement:** Expected to provide more accurate predictions than traditional models.

## Implementation Guide

**Data Structures:** Graphs to represent relationships between events, Databases for storing historical data

**Dependencies:** Data analysis libraries (e.g., Pandas, NumPy), Statistical modeling tools (e.g., R, Python's StatsModels)

**Core Operation:**

```python
model = create_model(historical_data); predictions = model.predict(new_data)
```

**Watch Out For:**

- Ensure data quality and completeness.
- Be cautious of overfitting the model to historical data.
- Consider external factors that may not be captured in the data.

## Use This When

- You need to model complex supply chain disruptions.
- You want to improve risk management strategies.
- You are analyzing historical supply chain data.

## Don't Use When

- The supply chain is simple with few variables.
- Real-time decision-making is required without historical data.
- Immediate responses to disruptions are needed.

## Key Concepts

risk events, contributing events, supply chain resilience, predictive modeling

## Connects To

- Risk assessment frameworks
- Predictive analytics
- Supply chain optimization techniques

## Prerequisites

- Understanding of supply chain dynamics
- Familiarity with statistical modeling
- Knowledge of data analysis techniques

## Limitations

- May require extensive historical data.
- Complexity in accurately identifying contributing events.
- Potential for model bias based on data selection.

## Open Questions

- How to effectively quantify the impact of contributing events?
- What are the best practices for real-time risk assessment?

## Abstract

Supply chain disruptions don’t happen in isolation. They ripple. Some are triggered internally (like forecasting errors), others come from outside (like geopolitical conflict or natural disasters). But, importantly, most disruptions don’t start at the moment they become visible. They build slowly, unevenly, from smaller incidents. A missed quality check, a delayed customs clearance, a misread weather forecast. These are called contributing events, upstream conditions that increase the likelihood of downstream risk. The disruption itself is called the risk event, the early tremors are the contributors. And that distinction (between root conditions and final outcomes) is exactly where many current models fall short.
