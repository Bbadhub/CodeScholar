# Towards a global plastics treaty: Navigating policy preferences and economic interests

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1017/plc.2025.10030` |
| Full Paper | [https://doi.org/10.1017/plc.2025.10030](https://doi.org/10.1017/plc.2025.10030) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/c99baf71ed4bc7ea9c3acbbabf11bf29fff2da1d](https://www.semanticscholar.org/paper/c99baf71ed4bc7ea9c3acbbabf11bf29fff2da1d) |
| Source | [https://journalclub.io/episodes/towards-a-global-plastics-treaty-navigating-policy-preferences-and-economic-interests](https://journalclub.io/episodes/towards-a-global-plastics-treaty-navigating-policy-preferences-and-economic-interests) |
| Source | [https://www.semanticscholar.org/paper/c99baf71ed4bc7ea9c3acbbabf11bf29fff2da1d](https://www.semanticscholar.org/paper/c99baf71ed4bc7ea9c3acbbabf11bf29fff2da1d) |
| Year | 2026 |
| Citations | 1 |
| Authors | Elin Dreyer, Teis Hansen, Karl Holmberg, Lionel Kielhöfer, Tara Olsen, Johannes Stripple |
| Paper ID | `39e7ef9f-d6b2-4825-a297-a597cc9a5c98` |

## Classification

- **Problem Type:** policy analysis and negotiation dynamics
- **Domain:** Other
- **Sub-domain:** Environmental Policy
- **Technique:** Systematic Qualitative Content Analysis
- **Technique Category:** statistical_method
- **Type:** comparison

## Summary

The paper analyzes pre-session submissions from countries regarding a global treaty on plastic pollution, revealing diverse policy preferences and economic interests that could influence treaty negotiations. Engineers should care because understanding these dynamics can inform the development of effective policies and technologies to address plastic pollution.

## Key Contribution

**The identification of four distinct clusters of policy approaches among countries regarding plastic pollution measures.**

## Problem

The need for a legally binding international treaty to curb plastic pollution across its entire life cycle.

## Method

**Approach:** The method involves analyzing pre-session submissions from countries to identify proposed measures and priorities for a global plastics treaty. It employs systematic qualitative content analysis and cluster analysis to categorize submissions based on their policy preferences.

**Algorithm:**

1. 1. Collect pre-session submissions from countries.
2. 2. Code submissions based on proposed measures and targets.
3. 3. Perform cluster analysis using K-modes algorithm to categorize submissions.
4. 4. Analyze political-economic factors influencing clustering.
5. 5. Map the distribution of measures across the plastics value chain.

**Input:** Pre-session submissions from countries regarding plastic pollution measures.

**Output:** Categorized clusters of policy approaches and insights into political-economic factors.

**Key Parameters:**

- `K (number of clusters): 4`
- `Coding categories: regulatory measures, economic measures, soft measures, targets`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Pre-session submissions from 86 parties representing 174 states

**Results:**

- Number of proposed measures: 1,015 distinct measures
- Total codes for measures: 2,688

**Compared against:** Previous analyses of countries' positions in international negotiations

**Improvement:** Identified a more comprehensive understanding of policy preferences compared to previous studies.

## Implementation Guide

**Data Structures:** Submissions data structure for coding measures, Cluster assignments for analysis

**Dependencies:** Qualitative data analysis software (e.g., NVivo)

**Core Operation:**

```python
submissions = collect_submissions(); coded_data = code_submissions(submissions); clusters = cluster_analysis(coded_data, K=4);
```

**Watch Out For:**

- Be aware of potential biases in submissions due to coalition representations.
- Ensure the coding process is rigorous to avoid researcher bias.
- Recognize that the negotiation process is dynamic and submissions may not reflect current positions.

## Use This When

- You need to understand the diverse policy preferences of countries regarding environmental treaties.
- You are involved in developing strategies for international negotiations on plastic pollution.
- You want to analyze the impact of economic interests on environmental policy.

## Don't Use When

- You require a quantitative model for predicting environmental outcomes.
- You are looking for a specific algorithm for machine learning applications.
- You need immediate solutions for plastic waste management without policy considerations.

## Key Concepts

policy mix, cluster analysis, qualitative coding, international negotiations, plastic pollution, economic interests, regulatory measures

## Connects To

- K-means clustering
- Policy mix literature
- International environmental law
- Qualitative research methods
- Negotiation theory

## Prerequisites

- Understanding of qualitative research methods
- Familiarity with international environmental policy
- Knowledge of cluster analysis techniques

## Limitations

- Submissions represent a static snapshot of a dynamic negotiation process.
- Potential biases in submissions due to coalition dynamics.
- The analysis may not fully capture evolving positions of states.

## Open Questions

- How will the evolving political landscape affect future treaty negotiations?
- What specific measures will ultimately be included in the final treaty?

## Abstract

In August over 180 countries gathered in Geneva for what was known as INC-5.2: the resumed fifth session of the Intergovernmental Negotiating Committee on Plastic Pollution. The goal was to finalize a global treaty that would curb pollution across the full life cycle of plastic production and use.
