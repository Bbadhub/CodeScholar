# Developing a tourism circuit around a brownfield destination: a framework based on analytic hierarchy process and weighted Shapley value

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1080/29966892.2025.2459401` |
| Full Paper | [https://doi.org/10.1080/29966892.2025.2459401](https://doi.org/10.1080/29966892.2025.2459401) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/5fbc426803e43afa8c7b93d431f5f9eff7c19eeb](https://www.semanticscholar.org/paper/5fbc426803e43afa8c7b93d431f5f9eff7c19eeb) |
| Source | [https://journalclub.io/episodes/developing-a-tourism-circuit-around-a-brownfield-destination-a-framework-based-on-analytic-hierarchy-process-and-weighted-shapley-value](https://journalclub.io/episodes/developing-a-tourism-circuit-around-a-brownfield-destination-a-framework-based-on-analytic-hierarchy-process-and-weighted-shapley-value) |
| Source | [https://www.semanticscholar.org/paper/5fbc426803e43afa8c7b93d431f5f9eff7c19eeb](https://www.semanticscholar.org/paper/5fbc426803e43afa8c7b93d431f5f9eff7c19eeb) |
| Year | 2026 |
| Citations | 0 |
| Authors | S. Sivanandham, S. Srivatsa Srinivas, Ananya Jain |
| Paper ID | `7ef3d4da-dfb9-42d3-864d-9196add712c5` |

## Classification

- **Problem Type:** multi-criteria decision analysis, cooperative game theory
- **Domain:** Optimization & Operations Research
- **Sub-domain:** Tourism Management
- **Technique:** Analytic Hierarchy Process and Weighted Shapley Value
- **Technique Category:** optimization_algorithm
- **Type:** novel

## Summary

The authors developed a framework to create tourism circuits that encourage longer stays and equitable economic benefits across multiple locations. Engineers should care because this approach can enhance local economies and improve tourist experiences in underdeveloped areas.

## Key Contribution

**A two-step mathematical framework combining multi-criteria decision analysis and cooperative game theory for tourism circuit development.**

## Problem

The challenge of distributing tourist visits and economic benefits across multiple culturally significant sites in a region.

## Method

**Approach:** The method involves two main steps: first, using multi-criteria decision analysis to identify and prioritize strategies that can extend tourist stays. Second, applying cooperative game theory to allocate government subsidies effectively among underdeveloped tourist sites to manage increased demand.

**Algorithm:**

1. 1. Identify criteria for evaluating tourism sites.
2. 2. Use Analytic Hierarchy Process to prioritize these criteria.
3. 3. Assess potential strategies for extending tourist stays.
4. 4. Apply Weighted Shapley Value to determine subsidy distribution.
5. 5. Implement the recommended strategies.
6. 6. Monitor and evaluate the impact on tourist distribution and economic benefits.

**Input:** Data on tourist preferences, site characteristics, and economic metrics.

**Output:** A prioritized list of strategies and a subsidy allocation plan for tourism sites.

**Key Parameters:**

- `criteria_weights: varies based on stakeholder input`
- `subsidy_amount: determined by government budget`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Tourism data from Ramanathapuram district, Tamil Nadu, India

**Results:**

- Visitor stay duration, economic impact measures

**Compared against:** Current tourism distribution models

**Improvement:** Expected increase in visitor distribution and economic benefits across sites.

## Implementation Guide

**Data Structures:** Priority matrix for criteria evaluation, Game theory models for subsidy allocation

**Dependencies:** Analytic Hierarchy Process libraries, Game theory frameworks

**Core Operation:**

```python
prioritize_sites = AHP(criteria_data); subsidies = WeightedShapleyValue(site_data, prioritize_sites)
```

**Watch Out For:**

- Ensure accurate data collection on tourist preferences.
- Stakeholder input is crucial for weighting criteria.
- Monitor the impact of implemented strategies continuously.

## Use This When

- Developing tourism strategies in underdeveloped areas.
- Seeking to balance economic benefits across multiple locations.
- Implementing government subsidies for tourism development.

## Don't Use When

- Tourism sites are already well-distributed and economically balanced.
- Lack of data on tourist preferences or site characteristics.
- Immediate short-term tourism boosts are needed.

## Key Concepts

multi-criteria decision analysis, cooperative game theory, tourism circuit, economic distribution

## Connects To

- Analytic Hierarchy Process
- Shapley Value
- Tourism Management Frameworks
- Economic Impact Analysis

## Prerequisites

- Understanding of multi-criteria decision analysis
- Familiarity with cooperative game theory
- Knowledge of tourism economics

## Limitations

- Dependent on accurate and comprehensive data.
- May not account for all external factors affecting tourism.
- Implementation may require significant stakeholder coordination.

## Open Questions

- How can this framework be adapted for different cultural contexts?
- What are the long-term impacts on local economies post-implementation?

## Abstract

The authors have developed a framework for creating tourism “circuits” that extend visitor stays and distribute economic benefits across multiple locations. Instead of showing-up and leaving, this framework encourages tourists to explore nearby sites, spend more time in the area, and engage with a wider range of local experiences. The impact is a longer stay, higher spending, and more balanced growth across the region. The research comes from the Ramanathapuram district in Tamil Nadu, India, where nearly 23 million tourists visit each year and head to the famous religious sites. The problem is, only just-over 300,000 make it to the other culturally significant temples and landmarks in the same district. The authors’ solution is a two-step mathematical framework: first, they use multi-criteria decision analysis to prioritize strategies for extending tourist stays, then they apply cooperative game theory to determine how government subsidies should be allocated across underdeveloped sites to handle increased visitor demand.
