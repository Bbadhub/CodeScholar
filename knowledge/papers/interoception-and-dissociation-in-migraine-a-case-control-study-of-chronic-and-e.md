# Interoception and dissociation in migraine: a case-control study of chronic and episodic subtypes

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3389/fneur.2025.1643260` |
| Full Paper | [https://doi.org/10.3389/fneur.2025.1643260](https://doi.org/10.3389/fneur.2025.1643260) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/8325ff14c4ef9e413b026d7fa9a81321c6e787a4](https://www.semanticscholar.org/paper/8325ff14c4ef9e413b026d7fa9a81321c6e787a4) |
| Source | [https://journalclub.io/episodes/interoception-and-dissociation-in-migraine-a-case-control-study-of-chronic-and-episodic-subtypes](https://journalclub.io/episodes/interoception-and-dissociation-in-migraine-a-case-control-study-of-chronic-and-episodic-subtypes) |
| Source | [https://www.semanticscholar.org/paper/8325ff14c4ef9e413b026d7fa9a81321c6e787a4](https://www.semanticscholar.org/paper/8325ff14c4ef9e413b026d7fa9a81321c6e787a4) |
| Year | 2026 |
| Citations | 3 |
| Authors | Akihiro Koreki, Vilomi Bhatia, Anne-Marie Logan, Usman Khan, M. Onaya, Sarah N Garfinkel |
| Paper ID | `c6ec92f7-cf43-489d-9394-17c658e12f0e` |

## Classification

- **Problem Type:** interoceptive prediction error analysis
- **Domain:** Bioinformatics & Health
- **Sub-domain:** Neurology, Pain Management
- **Technique:** Interoceptive Trait Prediction Error (ITPE) and Interoceptive State Prediction Error (ISPE)
- **Technique Category:** statistical_method
- **Type:** novel

## Summary

This study investigates interoceptive abnormalities in individuals with chronic and episodic migraine, revealing significant differences in interoceptive accuracy and dissociation levels compared to control subjects. Engineers should care because these findings could inform the development of diagnostic tools or therapeutic interventions targeting interoceptive processing in migraine patients.

## Key Contribution

**The study identifies and quantifies interoceptive prediction errors in migraine patients, highlighting their potential role in the chronification of migraine.**

## Problem

Understanding the mechanisms underlying chronic migraine and its co-morbidities, particularly related to interoception and dissociation.

## Method

**Approach:** The method involves assessing interoceptive accuracy through heartbeat tracking and discrimination tasks, alongside self-report questionnaires to evaluate dissociation. The discrepancies between subjective beliefs and objective performance are quantified as ITPE and ISPE.

**Algorithm:**

1. 1. Recruit participants and classify them into migraine and control groups.
2. 2. Conduct heartbeat tracking and discrimination tasks to measure interoceptive accuracy.
3. 3. Administer self-report questionnaires to assess interoceptive sensibility and dissociation.
4. 4. Calculate ITPE as the difference between interoceptive sensibility and accuracy.
5. 5. Calculate ISPE based on trial-by-trial performance and confidence ratings.
6. 6. Analyze the data using statistical methods to compare groups.

**Input:** Participants' heartbeat data from tracking and discrimination tasks, self-report questionnaire responses.

**Output:** Quantified interoceptive accuracy, ITPE, ISPE, and dissociation scores.

**Key Parameters:**

- `HTT: Heartbeat Tracking Task`
- `HDT: Heartbeat Discrimination Task`
- `SDQ: Somatoform Dissociation Questionnaire`
- `MDI: Multiscale Dissociation Inventory`
- `BAI: Beck’s Anxiety Inventory`
- `BDI: Beck’s Depression Inventory`

**Complexity:** Not stated

## Benchmarks

**Tested on:** 49 participants (26 migraine patients, 23 control subjects)

**Results:**

- Interoceptive accuracy for HTT: 0.50 (migraine) vs. 0.78 (control)
- Interoceptive sensibility: 110 (migraine) vs. 39 (control)
- ITPE for HTT: 1.08 (migraine) vs. -1.16 (control)
- ITPE for HDT: 0.87 (migraine) vs. -0.62 (control)
- ISPE: 2.30 (chronic migraine) vs. 1.75 (episodic migraine)

**Compared against:** Control group without migraine

**Improvement:** Significant differences in interoceptive accuracy and prediction errors, with p-values < 0.001.

## Implementation Guide

**Data Structures:** Data structures for storing participant responses and task performance metrics., Statistical models for analyzing interoceptive prediction errors.

**Dependencies:** Statistical analysis libraries (e.g., R, Python's SciPy), Data collection tools for heartbeat tracking and questionnaires.

**Core Operation:**

```python
calculate_ITPE(sensibility, accuracy) = sensibility - accuracy
```

**Watch Out For:**

- Ensure accurate measurement of heartbeats to avoid data discrepancies.
- Be cautious of participant bias in self-report questionnaires.

## Use This When

- Developing diagnostic tools for migraine based on interoceptive processing.
- Creating therapeutic interventions targeting interoceptive abnormalities.
- Researching the relationship between chronic pain and cognitive processes.

## Don't Use When

- Addressing acute migraine attacks without considering interoceptive factors.
- When the focus is solely on pharmacological treatments without behavioral or cognitive assessments.

## Key Concepts

interoception, dissociation, predictive coding, interoceptive accuracy, interoceptive prediction error, chronic migraine, episodic migraine

## Connects To

- Predictive coding models in neuroscience
- Functional neurological disorders
- Chronic pain management strategies

## Prerequisites

- Understanding of interoception and its role in neurology.
- Familiarity with statistical methods for analyzing psychological data.
- Knowledge of migraine classification and assessment.

## Limitations

- Small sample size may limit generalizability.
- Potential confounding factors not fully controlled.
- Reliance on self-report measures may introduce bias.

## Open Questions

- How do interoceptive abnormalities evolve over time in migraine patients?
- What are the underlying neural mechanisms driving these interoceptive prediction errors?

## Abstract

The ‘prediction error’ concept is crucial to understanding today's research, so let's unpack it. Your brain is a prediction machine, it’s constantly generating expectations about incoming sensory information based on past experience. When you walk up stairs, your brain predicts that your heart rate will increase and you'll feel slightly out of breath. When these predictions match the actual signals from your body, everything feels normal. But when there's a mismatch between prediction and reality, you get a prediction error signal that helps your brain update its models. There are two types of interoceptive prediction errors that we can measure.
