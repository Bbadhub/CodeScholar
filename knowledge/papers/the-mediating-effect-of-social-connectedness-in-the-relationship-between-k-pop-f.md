# The Mediating Effect of Social Connectedness in the Relationship Between K-Pop Fandom Identity and Mental Health

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1177/21582440251369989` |
| Full Paper | [https://doi.org/10.1177/21582440251369989](https://doi.org/10.1177/21582440251369989) |
| Source | [https://journalclub.io/episodes/the-mediating-effect-of-social-connectedness-in-the-relationship-between-k-pop-fandom-identity-and-mental-health](https://journalclub.io/episodes/the-mediating-effect-of-social-connectedness-in-the-relationship-between-k-pop-fandom-identity-and-mental-health) |
| Year | 2026 |
| Citations | 0 |
| Authors |  |
| Paper ID | `66307554-2c34-4008-a052-e5bf15a7ea98` |

## Classification

- **Problem Type:** social network analysis, mental health assessment
- **Domain:** Human-Computer Interaction
- **Sub-domain:** Community engagement platforms
- **Technique:** Social Connectedness Mediating Model
- **Technique Category:** statistical_method
- **Type:** novel

## Summary

This paper investigates the impact of K-Pop fandom identity on mental health, specifically focusing on happiness and life satisfaction. Engineers should care because understanding these social dynamics can inform the design of applications that enhance community engagement and mental well-being.

## Key Contribution

**The identification of social connectedness as a mediating factor between K-Pop fandom identity and mental health outcomes.**

## Problem

The real-world problem is understanding how fandom identities influence mental health and the role of social connections in this relationship.

## Method

**Approach:** The method involves analyzing survey data from K-Pop fans to assess their fandom identity, social connectedness, and mental health indicators. Statistical models are used to determine the mediating effect of social connectedness on the relationship between fandom identity and mental health.

**Algorithm:**

1. 1. Collect survey data from K-Pop fans regarding their fandom identity, social connections, and mental health.
2. 2. Preprocess the data to ensure quality and completeness.
3. 3. Apply statistical analysis to identify correlations between fandom identity and mental health.
4. 4. Use mediation analysis to evaluate the role of social connectedness.
5. 5. Interpret results to understand the impact of social connections on mental health outcomes.

**Input:** Survey data including fandom identity metrics, social connectedness scores, and mental health indicators.

**Output:** Statistical results indicating the strength and significance of the mediating effect of social connectedness.

**Key Parameters:**

- `sample_size: 200`
- `confidence_level: 0.95`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Surveys from K-Pop fandom communities

**Results:**

- happiness score, life satisfaction score, depression scale

**Compared against:** Previous studies on fandom impact on mental health

**Improvement:** Not stated

## Implementation Guide

**Data Structures:** DataFrames for survey data, Statistical models for analysis

**Dependencies:** pandas, statsmodels, scikit-learn

**Core Operation:**

```python
results = mediation_analysis(survey_data, 'fandom_identity', 'mental_health', 'social_connectedness')
```

**Watch Out For:**

- Ensure survey questions are clear and unbiased
- Account for confounding variables in analysis
- Validate the sample size for statistical significance

## Use This When

- Building applications for fan communities
- Designing mental health support tools
- Conducting research on social dynamics in fandoms

## Don't Use When

- Analyzing non-fandom related social interactions
- When data on social connections is unavailable
- In contexts where fandom identity is not relevant

## Key Concepts

social connectedness, fandom identity, mental health, mediation analysis

## Connects To

- Social Network Analysis
- Community Detection Algorithms
- Mental Health Assessment Tools

## Prerequisites

- Basic statistics
- Understanding of mediation analysis
- Knowledge of survey design

## Limitations

- Findings may not generalize beyond K-Pop fandom
- Self-reported data may introduce bias
- Causality cannot be definitively established

## Open Questions

- How do different fandoms compare in terms of mental health impact?
- What other factors influence the relationship between fandom identity and mental health?

## Abstract

Does identifying as part of a K-Pop fandom make people feel happier and more satisfied with their lives? Does it help shield them from depression? And if those effects exist, are they explained by the social connections fans form with one another, or is some other psychological mechanism at work?
