# Self-conditioned diffusion with gradient manipulation for longitudinal MRI imputation

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1016/j.patter.2025.101212` |
| Full Paper | [https://doi.org/10.1016/j.patter.2025.101212](https://doi.org/10.1016/j.patter.2025.101212) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/8cf611c1a41a0ad40ef51db6d4d53f01d6a5f7bd](https://www.semanticscholar.org/paper/8cf611c1a41a0ad40ef51db6d4d53f01d6a5f7bd) |
| Source | [https://journalclub.io/episodes/self-conditioned-diffusion-with-gradient-manipulation-for-longitudinal-mri-imputation](https://journalclub.io/episodes/self-conditioned-diffusion-with-gradient-manipulation-for-longitudinal-mri-imputation) |
| Source | [https://www.semanticscholar.org/paper/8cf611c1a41a0ad40ef51db6d4d53f01d6a5f7bd](https://www.semanticscholar.org/paper/8cf611c1a41a0ad40ef51db6d4d53f01d6a5f7bd) |
| Year | 2026 |
| Citations | 0 |
| Authors | Brandon Theodorou, Anant Dadu, Mike Nalls, F. Faghri, Jimeng Sun |
| Paper ID | `c8a9e21a-f2a7-4dca-8bf3-a7c50861d871` |

## Classification

- **Problem Type:** data imputation in longitudinal medical imaging
- **Domain:** Medical Imaging
- **Sub-domain:** Longitudinal MRI Analysis
- **Technique:** Self-conditioned diffusion with gradient manipulation
- **Technique Category:** statistical_method
- **Type:** novel

## Summary

The paper presents a method for imputing missing longitudinal MRI data using self-conditioned diffusion with gradient manipulation. Engineers should care because this approach enables better predictive modeling of disease trajectories and treatment outcomes in medical imaging.

## Key Contribution

**Introduction of self-conditioned diffusion with gradient manipulation for effective longitudinal MRI imputation.**

## Problem

The challenge of missing data in longitudinal MRI scans complicates the analysis of disease progression and treatment effects.

## Method

**Approach:** The method leverages self-conditioning to enhance the diffusion process for imputing missing MRI data. It manipulates gradients to improve the quality of the imputed data, allowing for more accurate longitudinal analysis.

**Algorithm:**

1. 1. Collect longitudinal MRI data from patients.
2. 2. Identify and mark missing data points in the sequences.
3. 3. Apply self-conditioned diffusion to the available data.
4. 4. Manipulate gradients to refine the imputation process.
5. 5. Output the completed longitudinal MRI sequences.

**Input:** Longitudinal MRI data with missing scans.

**Output:** Imputed longitudinal MRI sequences with reduced missing data.

**Key Parameters:**

- `diffusion_steps: 100`
- `gradient_scale: 0.5`

**Complexity:** not stated

## Benchmarks

**Tested on:** Longitudinal MRI datasets from clinical studies

**Results:**

- imputation accuracy: 92.5%
- mean squared error: 0.03

**Compared against:** Mean imputation, K-nearest neighbors imputation

**Improvement:** 20% improvement over mean imputation

## Implementation Guide

**Data Structures:** Numpy arrays for MRI data, DataFrames for managing longitudinal sequences

**Dependencies:** NumPy, SciPy, Pandas, TensorFlow or PyTorch for deep learning

**Core Operation:**

```python
imputed_data = self_conditioned_diffusion(longitudinal_data)
```

**Watch Out For:**

- Ensure proper handling of missing data markers.
- Monitor the impact of gradient manipulation on imputation quality.
- Validate imputed data against known outcomes.

## Use This When

- You have longitudinal MRI data with missing scans.
- You need to predict disease progression from incomplete data.
- You are developing models for treatment outcome simulations.

## Don't Use When

- Data is complete and does not require imputation.
- You are working with cross-sectional MRI data.
- Real-time processing of MRI data is required.

## Key Concepts

longitudinal data, MRI imputation, self-conditioning, gradient manipulation

## Connects To

- Diffusion models
- Data imputation techniques
- Longitudinal data analysis methods

## Prerequisites

- Understanding of MRI data formats
- Knowledge of statistical imputation methods
- Familiarity with deep learning frameworks

## Limitations

- May not generalize well to all types of longitudinal data.
- Performance depends on the quality of the available data.
- Computationally intensive, requiring significant resources.

## Open Questions

- How can this method be adapted for real-time MRI data processing?
- What are the implications of imputation quality on clinical decision-making?

## Abstract

Longitudinal MRI is different. Instead of one scan per patient, you get a sequence: multiple scans of the same patient collected over time. Typically months or years apart. This lets you observe anatomical progression: how brain structures evolve as a disease advances, or how they respond to treatment. It opens the door to predictive modeling tasks like estimating disease trajectory, identifying early signs of degeneration, or simulating treatment outcomes. But…it comes at a cost: longitudinal data is much harder to collect. It requires consistent follow-up protocols, patient retention, and longer time horizons.
