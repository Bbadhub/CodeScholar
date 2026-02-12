# Advancing Pediatric Growth Assessment with Machine Learning: Overcoming Challenges in Early Diagnosis and Monitoring

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3390/children12030317` |
| Full Paper | [https://doi.org/10.3390/children12030317](https://doi.org/10.3390/children12030317) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/267bae1a08ee664d5cd5d9bda7a5af5dd781a053](https://www.semanticscholar.org/paper/267bae1a08ee664d5cd5d9bda7a5af5dd781a053) |
| Source | [https://journalclub.io/episodes/advancing-pediatric-growth-assessment-with-machine-learning-overcoming-challenges-in-early-diagnosis-and-monitoring](https://journalclub.io/episodes/advancing-pediatric-growth-assessment-with-machine-learning-overcoming-challenges-in-early-diagnosis-and-monitoring) |
| Source | [https://www.semanticscholar.org/paper/267bae1a08ee664d5cd5d9bda7a5af5dd781a053](https://www.semanticscholar.org/paper/267bae1a08ee664d5cd5d9bda7a5af5dd781a053) |
| Year | 2026 |
| Citations | 3 |
| Authors | Mauro Rodriguez-Marin, L. G. Orozco-Alatorre |
| Paper ID | `20370390-7fca-4143-aa1f-d5baa9996dff` |

## Classification

- **Problem Type:** binary classification
- **Domain:** Machine Learning & AI
- **Sub-domain:** Logistic Regression
- **Technique:** Logistic Regression
- **Technique Category:** statistical_method
- **Type:** novel

## Summary

This paper presents a logistic regression model to enhance pediatric growth assessment, improving diagnostic precision and timeliness for identifying growth disorders. Engineers should care because it provides a practical, interpretable, and efficient method for automating pediatric growth monitoring in clinical settings.

## Key Contribution

**Development of a logistic regression model for pediatric growth assessment that significantly improves diagnostic accuracy and operational efficiency.**

## Problem

The need for accurate and timely assessment of pediatric growth to diagnose and monitor growth disorders effectively.

## Method

**Approach:** The method uses logistic regression to analyze biometric and demographic data to predict the probability of appropriate height versus short stature in children. It incorporates data preprocessing techniques such as cleaning, imputation, and feature selection to enhance model performance.

**Algorithm:**

1. 1. Collect biometric and demographic data from children aged 6 to 13.
2. 2. Preprocess the data: clean, impute missing values, and select relevant features.
3. 3. Develop a logistic regression model using R.
4. 4. Train the model on the dataset.
5. 5. Evaluate the model using performance metrics such as accuracy, sensitivity, and ROC curve.
6. 6. Adjust parameters based on cross-validation results.
7. 7. Deploy the model for clinical use.

**Input:** Biometric and demographic data including age, height, and growth patterns.

**Output:** Probability of appropriate height or short stature (binary outcome).

**Key Parameters:**

- `learning_rate: not specified`
- `max_iterations: not specified`
- `cross_validation_folds: k-fold (number not specified)`

**Complexity:** not stated

## Benchmarks

**Tested on:** Real-world data from public institutions, including Stanford Medicine Children’s Health.

**Results:**

- accuracy: 94.65%
- sensitivity: 91.03%
- AUC: 0.96

**Compared against:** Traditional pediatric growth assessment methods.

**Improvement:** Significantly improved identification of growth anomalies compared to conventional assessment methods.

## Implementation Guide

**Data Structures:** Data frame for storing biometric and demographic data.

**Dependencies:** R programming language, R libraries for logistic regression and data preprocessing.

**Core Operation:**

```python
model = glm(outcome ~ predictors, family = binomial, data = dataset)
```

**Watch Out For:**

- Ensure proper data cleaning and imputation to avoid biases.
- Be cautious of multicollinearity among predictor variables.
- Validate the model with external datasets to ensure generalizability.

## Use This When

- You need a transparent and interpretable model for clinical decision-making.
- You are working with small to medium-sized datasets.
- Real-time processing and resource efficiency are required in healthcare environments.

## Don't Use When

- You require complex non-linear relationships that logistic regression cannot model.
- You have a large dataset that may benefit from more complex models.
- Interpretability is not a priority for your application.

## Key Concepts

logistic regression, pediatric growth, machine learning, binary classification, predictive modeling

## Connects To

- Random Forest
- Neural Networks
- Support Vector Machines
- Feature Selection Techniques

## Prerequisites

- Understanding of logistic regression
- Basic knowledge of R programming
- Familiarity with data preprocessing techniques

## Limitations

- Limited to linear relationships between predictors and the outcome.
- Sensitive to outliers in the dataset.
- Requires prior imputation for missing data.

## Open Questions

- How can hybrid models combining logistic regression with other ML techniques enhance predictive performance?
- What are the best practices for ensuring data privacy and security in pediatric healthcare applications?

## Abstract

Logistic regression is a statistical technique used to predict the probability of a binary outcome (like yes/no, disease/no-disease, pass/fail, or in our case today appropriate-height/short-stature). It’s easiest to understand what this is, by understanding what it’s not. It’s not linear regression. Linear regression assumes that the relationship between input and output is straight and continuous.
