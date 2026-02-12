# A predictive model for stunting among children under the age of three

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3389/fped.2024.1441714` |
| Full Paper | [https://doi.org/10.3389/fped.2024.1441714](https://doi.org/10.3389/fped.2024.1441714) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/30ddbe54e349b5a041c4e7fdc50bb85b13bb7dd4](https://www.semanticscholar.org/paper/30ddbe54e349b5a041c4e7fdc50bb85b13bb7dd4) |
| Source | [https://journalclub.io/episodes/a-predictive-model-for-stunting-among-children-under-the-age-of-three](https://journalclub.io/episodes/a-predictive-model-for-stunting-among-children-under-the-age-of-three) |
| Source | [https://www.semanticscholar.org/paper/30ddbe54e349b5a041c4e7fdc50bb85b13bb7dd4](https://www.semanticscholar.org/paper/30ddbe54e349b5a041c4e7fdc50bb85b13bb7dd4) |
| Year | 2026 |
| Citations | 2 |
| Authors | Yuxiang Xiong, Xuhuai Hu, Jindan Cao, Li Shang, Ben Niu |
| Paper ID | `18d77a58-7841-4daa-9998-ce3cad48367d` |

## Classification

- **Problem Type:** predictive modeling for health outcomes
- **Domain:** Machine Learning & AI
- **Sub-domain:** Predictive modeling
- **Technique:** LASSO regression and logistic regression
- **Technique Category:** statistical_method
- **Type:** novel

## Summary

The paper presents a predictive model for stunting among children under three years of age, utilizing a combination of LASSO regression and logistic regression to identify key risk factors. Engineers should care because this model can inform early interventions for childhood growth impairments, potentially improving health outcomes.

## Key Contribution

**Development of a nomogram-based predictive model for childhood stunting using LASSO and logistic regression techniques.**

## Problem

The need to identify risk factors for stunting in children to enable early intervention and improve health outcomes.

## Method

**Approach:** The method involves using LASSO regression to select significant predictors from a dataset of children under three years old, followed by logistic regression to construct a predictive model. A nomogram is created to visualize the risk factors and their contributions to stunting.

**Algorithm:**

1. 1. Collect data on children under three years old, including risk factors.
2. 2. Split the dataset into training (80%) and validation (20%) sets.
3. 3. Apply LASSO regression on the training set to identify significant predictors.
4. 4. Use logistic regression to model the relationship between predictors and stunting.
5. 5. Create a nomogram based on the logistic regression results.
6. 6. Validate the model using the validation set and assess performance metrics.

**Input:** Data on children including age, gender, parental education, feeding patterns, and health status.

**Output:** A nomogram predicting the risk of stunting in children under three years old.

**Key Parameters:**

- `lambda (LASSO regularization parameter): optimal value determined through cross-validation`
- `training-validation split ratio: 80:20`

**Complexity:** not stated

## Benchmarks

**Tested on:** 9,581 children under three years old from Shenzhen, China

**Results:**

- AUC: 0.678 (training set), 0.734 (validation set)
- Calibration plots and DCA for clinical validity

**Compared against:** Standard logistic regression without LASSO feature selection

**Improvement:** The model showed improved predictive accuracy over standard methods.

## Implementation Guide

**Data Structures:** DataFrame for storing child health data, Nomogram structure for visualization

**Dependencies:** R programming language, rms package for nomogram creation

**Core Operation:**

```python
model = logistic_regression(LASSO(data))
```

**Watch Out For:**

- Ensure data quality and completeness to avoid bias.
- Carefully tune the LASSO parameter to avoid overfitting.
- Validate the model on an independent dataset to assess generalizability.

## Use This When

- You need to predict health outcomes based on multiple risk factors.
- Working on interventions for childhood health issues.
- Developing tools for clinicians to assess developmental risks in children.

## Don't Use When

- Data is limited or not representative of the target population.
- The problem does not involve multiple predictors or risk factors.
- Real-time predictions are required without prior model training.

## Key Concepts

LASSO regression, logistic regression, nomogram, predictive modeling, child health assessment

## Connects To

- Logistic regression
- Machine learning for health predictions
- Statistical modeling techniques

## Prerequisites

- Understanding of regression analysis
- Familiarity with predictive modeling concepts
- Basic knowledge of child health metrics

## Limitations

- Model may not generalize to populations outside of Shenzhen, China.
- Dependent on the quality of input data and risk factor selection.
- Does not account for unmeasured confounding variables.

## Open Questions

- How can the model be adapted for different cultural contexts?
- What additional risk factors could improve the model's predictive power?

## Abstract

Worldwide, approximately 1/5th of children under the age of five suffer from some sort of physical growth-impairment. That figure has improved virtually every year for decades, but there’s still a lot of work left to do. Growth-impairment has traditionally been viewed strictly as a function of malnutrition, but there is an increasing awareness that there are a multitude of other factors that correlate strongly with growth-impairment. Identifying these risk factors could help clinicians intervene earlier and more effectively. In this research the authors attempt to build a predictive model for growth-impairment: a model that can analyze other household and familial risk factors, and inform medical professionals of any elevated risk.
