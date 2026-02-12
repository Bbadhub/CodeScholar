# Hoarding knowledge or hoarding stress? Investigating the link between digital hoarding and cognitive failures among Chinese college students

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3389/fpsyg.2024.1518860` |
| Full Paper | [https://doi.org/10.3389/fpsyg.2024.1518860](https://doi.org/10.3389/fpsyg.2024.1518860) |
| Source | [https://journalclub.io/episodes/hoarding-knowledge-or-hoarding-stress-investigating-the-link-between-digital-hoarding-and-cognitive-failures-among-chinese-college-students](https://journalclub.io/episodes/hoarding-knowledge-or-hoarding-stress-investigating-the-link-between-digital-hoarding-and-cognitive-failures-among-chinese-college-students) |
| Year | 2026 |
| Citations | 0 |
| Authors |  |
| Paper ID | `faa37fb8-8264-4286-bfde-80029b8b96e2` |

## Classification

- **Problem Type:** behavioral analysis and cognitive psychology
- **Domain:** Human-Computer Interaction
- **Sub-domain:** Digital information management
- **Technique:** Moderated mediation model
- **Technique Category:** statistical_method
- **Type:** novel

## Summary

This study investigates the relationship between digital hoarding and cognitive failures among Chinese college students, revealing that digital hoarding leads to increased cognitive failures mediated by fatigue and moderated by mindfulness. Engineers should care because understanding these relationships can inform the design of digital tools that help users manage their digital content more effectively.

## Key Contribution

**The study empirically confirms the mediating role of fatigue and the moderating role of mindfulness in the relationship between digital hoarding and cognitive failures.**

## Problem

The increasing prevalence of digital hoarding among college students leads to cognitive failures, impacting their academic performance and mental health.

## Method

**Approach:** The method involves surveying participants to assess their levels of digital hoarding, fatigue, mindfulness, and cognitive failures. A moderated mediation model is constructed to analyze the relationships between these variables.

**Algorithm:**

1. 1. Recruit participants and administer surveys measuring digital hoarding, fatigue, mindfulness, and cognitive failures.
2. 2. Use SPSS to perform descriptive statistics and Pearson correlations.
3. 3. Apply Hayes' PROCESS macro (Model 4 and Model 8) to test mediation and moderation effects.
4. 4. Analyze regression coefficients and bootstrap confidence intervals to confirm hypotheses.

**Input:** Survey data from participants measuring digital hoarding, fatigue, mindfulness, and cognitive failures.

**Output:** Statistical analysis results indicating the relationships and effects among the variables.

**Key Parameters:**

- `sample_size: 801`
- `confidence_intervals: 95%`
- `bootstrap_resamples: 5000`

**Complexity:** not stated

## Benchmarks

**Tested on:** Survey responses from 801 Chinese college students

**Results:**

- Cognitive failures measured by CFQ, fatigue measured by Fatigue Assessment Scale, mindfulness measured by CAMM

**Compared against:** Previous studies on digital hoarding and cognitive failures

**Improvement:** The study shows that mindfulness significantly reduces the impact of digital hoarding on cognitive failures.

## Implementation Guide

**Data Structures:** Survey data structure for digital hoarding, fatigue, mindfulness, and cognitive failures

**Dependencies:** SPSS for statistical analysis, PROCESS macro for mediation analysis

**Core Operation:**

```python
results = PROCESS(data, model=8, bootstrap=5000)
```

**Watch Out For:**

- Ensure participant engagement to avoid common method bias.
- Control for demographic variables to improve model accuracy.
- Use appropriate scales with established reliability and validity.

## Use This When

- Designing applications to help users manage digital content effectively.
- Creating interventions to reduce cognitive overload in digital environments.
- Developing educational programs to promote mindfulness among students.

## Don't Use When

- Addressing non-digital forms of information management.
- When the target population does not exhibit digital hoarding behaviors.
- In contexts where cognitive failures are not a concern.

## Key Concepts

digital hoarding, cognitive failures, fatigue, mindfulness, moderated mediation model

## Connects To

- cognitive load theory
- behavioral economics
- digital well-being frameworks

## Prerequisites

- Understanding of statistical mediation and moderation
- Familiarity with survey design and analysis
- Knowledge of cognitive psychology principles

## Limitations

- Focus on a specific demographic (Chinese college students)
- Self-reported data may introduce bias
- Findings may not generalize to other populations

## Open Questions

- How can digital tools be designed to mitigate cognitive overload?
- What other factors influence the relationship between digital hoarding and cognitive failures?

## Abstract

On December 8th, 2022, the Google Chrome team announced “Memory Saver”: the browser’s new ability to free up RAM from unused tabs, so that it could be used in the tabs you’ve interacted with more recently. For most people, this was probably a non-event. For people like me, it was huge.
