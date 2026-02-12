# Association between shift work and brain age gap: a neuroimaging study using MRI-based brain age prediction algorithms

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3389/fnagi.2025.1650497` |
| Full Paper | [https://doi.org/10.3389/fnagi.2025.1650497](https://doi.org/10.3389/fnagi.2025.1650497) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/d3847a10a50cea8f696c204ad8d0d11dc86c51c0](https://www.semanticscholar.org/paper/d3847a10a50cea8f696c204ad8d0d11dc86c51c0) |
| Source | [https://journalclub.io/episodes/association-between-shift-work-and-brain-age-gap-a-neuroimaging-study-using-mri-based-brain-age-prediction-algorithms](https://journalclub.io/episodes/association-between-shift-work-and-brain-age-gap-a-neuroimaging-study-using-mri-based-brain-age-prediction-algorithms) |
| Source | [https://www.semanticscholar.org/paper/d3847a10a50cea8f696c204ad8d0d11dc86c51c0](https://www.semanticscholar.org/paper/d3847a10a50cea8f696c204ad8d0d11dc86c51c0) |
| Year | 2026 |
| Citations | 0 |
| Authors | Youjin Kim, Joon Yul Choi, Evgeny Petrovskiy, W. Lee |
| Paper ID | `5fb6a514-4170-4533-a65f-da9120574486` |

## Classification

- **Problem Type:** brain age prediction
- **Domain:** Machine Learning & AI
- **Sub-domain:** Neuroimaging
- **Technique:** Brain age prediction algorithms
- **Technique Category:** statistical_method
- **Type:** comparison

## Summary

This study investigates the association between shift work and brain aging by calculating the brain age gap (BAG) using MRI-based brain age prediction algorithms. Engineers should care because it provides insights into how occupational factors may influence brain health, which could inform the development of health monitoring tools.

## Key Contribution

**The study demonstrates that shift work is associated with accelerated brain aging as measured by the brain age gap (BAG).**

## Problem

The real-world problem motivating this work is the need to understand how shift work affects brain health and aging.

## Method

**Approach:** The method involves training machine learning models on MRI scans to predict brain age, then calculating the brain age gap (BAG) as the difference between predicted brain age and chronological age. The study uses multiple models to assess the impact of shift work on BAG.

**Algorithm:**

1. 1. Collect structural MRI data from participants.
2. 2. Preprocess MRI images using FreeSurfer and FSL.
3. 3. Apply seven brain age prediction models to estimate brain age.
4. 4. Calculate BAG as the difference between predicted brain age and chronological age.
5. 5. Perform statistical analyses (ANCOVA) to compare BAG between shift workers and non-shift workers.

**Input:** Structural MRI scans (T1-weighted and T2-weighted images).

**Output:** Predicted brain age and brain age gap (BAG).

**Key Parameters:**

- `repetition_time_T1: 1970 ms`
- `echo_time_T1: 2.84 ms`
- `inversion_time_T1: 991 ms`
- `flip_angle_T1: 9 degrees`
- `voxel_size_T1: 0.5 mm x 0.5 mm x 1 mm`
- `repetition_time_T2: 3200 ms`
- `echo_time_T2: 509 ms`
- `flip_angle_T2: 120 degrees`
- `voxel_size_T2: 0.5 mm x 0.5 mm x 1 mm`

**Complexity:** Not stated.

## Benchmarks

**Tested on:** MRI scans from 113 healthcare workers (33 shift workers, 80 fixed daytime workers).

**Results:**

- R2 for pyment: 0.79
- R2 for DenseNet: 0.69
- R2 for brainageR: 0.66
- MAE for pyment: 4.75
- MAE for DenseNet: 4.92
- MAE for brainageR: 10.37

**Compared against:** Comparison against fixed daytime workers' BAG values.

**Improvement:** Shift workers exhibited significantly higher BAG than non-shift workers (p < 0.05).

## Implementation Guide

**Data Structures:** MRI image arrays, Data frames for participant demographics, Statistical models for analysis

**Dependencies:** FreeSurfer 7.4, FSL 6.0, R version 4.4.3, SAS version 9.4

**Core Operation:**

```python
predicted_age = model.predict(MRI_data); BAG = predicted_age - chronological_age;
```

**Watch Out For:**

- Ensure MRI images are of high quality to avoid bias.
- Be cautious of overfitting when using multiple models.
- Adjust for covariates appropriately to avoid confounding results.

## Use This When

- You need to assess the impact of occupational factors on brain health.
- You are developing health monitoring tools based on neuroimaging data.
- You want to explore the relationship between lifestyle factors and cognitive decline.

## Don't Use When

- You require real-time brain age predictions without extensive preprocessing.
- You are working with a dataset that lacks sufficient MRI quality.
- You need a method that does not rely on machine learning.

## Key Concepts

brain age gap, MRI, machine learning, neuroimaging, shift work, brain aging, statistical analysis

## Connects To

- Brain age prediction models
- Neuroimaging techniques
- Machine learning for health monitoring

## Prerequisites

- Understanding of MRI data processing
- Familiarity with machine learning algorithms
- Knowledge of statistical analysis methods

## Limitations

- Limited sample size may affect generalizability.
- Potential biases in self-reported shift work data.
- The study design is cross-sectional, limiting causal inference.

## Open Questions

- What are the long-term effects of shift work on brain health?
- How can we improve the interpretability of deep learning models in neuroimaging?

## Abstract

First, let's talk about what these researchers were actually measuring. The brain age “gap” is the difference between your chronological age and your "predicted brain age" based on MRI scans. Researchers train machine learning models on brain scans from thousands of healthy people. These models learn to predict someone's age just by looking at their brain structure. When you feed a new brain scan into these models, they spit out a predicted age. So, if the model says your brain looks 45 but you're only 40, you have a brain age gap of five years.
