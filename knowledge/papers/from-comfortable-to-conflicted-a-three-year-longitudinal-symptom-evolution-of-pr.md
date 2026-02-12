# From comfortable to conflicted: a three-year longitudinal symptom evolution of problematic Internet use among junior high school students

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3389/fpsyt.2025.1635911` |
| Full Paper | [https://doi.org/10.3389/fpsyt.2025.1635911](https://doi.org/10.3389/fpsyt.2025.1635911) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/99e9353da3c3a0e61a1b15d30dd6522c43ade011](https://www.semanticscholar.org/paper/99e9353da3c3a0e61a1b15d30dd6522c43ade011) |
| Source | [https://journalclub.io/episodes/from-comfortable-to-conflicted-a-three-year-longitudinal-symptom-evolution-of-problematic-internet-use-among-junior-high-school-students](https://journalclub.io/episodes/from-comfortable-to-conflicted-a-three-year-longitudinal-symptom-evolution-of-problematic-internet-use-among-junior-high-school-students) |
| Source | [https://www.semanticscholar.org/paper/99e9353da3c3a0e61a1b15d30dd6522c43ade011](https://www.semanticscholar.org/paper/99e9353da3c3a0e61a1b15d30dd6522c43ade011) |
| Year | 2026 |
| Citations | 0 |
| Authors | Yanjun Kang, Xun Feng, Tong Zhang, Kexin Yin, Peng Wang |
| Paper ID | `df8749fc-acbf-461b-b4e8-78851f1f8528` |

## Classification

- **Problem Type:** longitudinal symptom evolution analysis
- **Domain:** Psychology & Behavioral Science
- **Sub-domain:** Network Analysis in Mental Health
- **Technique:** Network Analysis
- **Technique Category:** statistical_method
- **Type:** novel

## Summary

The study utilized network analysis to investigate the evolution of symptoms related to problematic Internet use (PIU) among junior high school students over three years. Engineers should care because this approach provides insights into the relationships between symptoms, which can inform the development of targeted interventions for PIU.

## Key Contribution

**The application of network analysis to longitudinally track and analyze the evolution of PIU symptoms among adolescents.**

## Problem

The increasing prevalence of problematic Internet use among adolescents and the need for effective prevention and intervention strategies.

## Method

**Approach:** The method involves constructing a network where symptoms of PIU are represented as nodes and the relationships between them as edges. The strength of these relationships is analyzed over time to identify core symptoms and their evolution.

**Algorithm:**

1. 1. Collect longitudinal data on PIU symptoms using the Problematic Internet Use Scale.
2. 2. Construct a Gaussian graphical model (GGM) for each time point to visualize symptom relationships.
3. 3. Calculate centrality measures for each symptom to identify core symptoms.
4. 4. Perform network comparison tests across different time points to analyze changes in symptom relationships.

**Input:** Data collected from the Problematic Internet Use Scale (PIUS-a) across four assessments.

**Output:** Network visualizations and centrality metrics indicating the evolution of PIU symptoms.

**Key Parameters:**

- `number_of_assessments: 4`
- `sample_size: 302`
- `alpha: 0.05 (for statistical significance)`
- `confidence_interval: 95%`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Problematic Internet Use Scale (PIUS-a) data from 302 junior high school students

**Results:**

- centrality measures (strength, closeness, betweenness)
- correlation coefficients between symptoms

**Compared against:** Previous studies on PIU without longitudinal network analysis

**Improvement:** Identified core symptoms and their evolution over time, providing a dynamic understanding of PIU.

## Implementation Guide

**Data Structures:** Graphs for network representation, Data frames for symptom scores

**Dependencies:** R programming language, qgraph package, bootnet package, mice package

**Core Operation:**

```python
network = construct_network(symptom_data); centrality = calculate_centrality(network); visualize(network)
```

**Watch Out For:**

- Ensure data is normally distributed before applying Gaussian graphical models.
- Be cautious of missing data; use multiple imputation to handle it effectively.
- Interpret centrality measures carefully, as they can vary with network structure.

## Use This When

- You need to analyze the relationships between symptoms of a behavioral issue over time.
- You are developing interventions for adolescents based on symptom evolution.
- You want to visualize complex relationships in psychological data.

## Don't Use When

- You require a quick, one-time assessment of symptoms without longitudinal tracking.
- You are working with a population that does not exhibit significant behavioral changes over time.

## Key Concepts

network analysis, problematic Internet use, longitudinal study, centrality measures, Gaussian graphical model

## Connects To

- Gaussian Graphical Models
- Centrality Measures in Networks
- Longitudinal Data Analysis Techniques

## Prerequisites

- Basic understanding of network theory
- Familiarity with psychological assessment tools
- Knowledge of statistical analysis methods

## Limitations

- Findings may not generalize to populations outside of junior high school students.
- The study does not account for external factors influencing PIU.
- Longitudinal data collection can be resource-intensive.

## Open Questions

- How do external factors (e.g., social environment) influence the evolution of PIU symptoms?
- What specific interventions are most effective at different stages of symptom evolution?

## Abstract

They used a technique called network analysis to map out how different symptoms of problematic Internet use relate to each other and change over time. On today's episode, we'll explore how they tracked symptom evolution, what they discovered about ‘comfort’ and ‘conflict’, and what this means for preventing and treating Internet dependency in young people. Let’s dive in.
