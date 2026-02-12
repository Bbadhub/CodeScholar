# Prediction of IPO performance from prospectus using multinomial logistic regression, a machine learning model

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3934/dsfe.2025006` |
| Full Paper | [https://doi.org/10.3934/dsfe.2025006](https://doi.org/10.3934/dsfe.2025006) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/35896c0ae1639edcf746515f2a99ce26cc664730](https://www.semanticscholar.org/paper/35896c0ae1639edcf746515f2a99ce26cc664730) |
| Source | [https://journalclub.io/episodes/prediction-of-ipo-performance-from-prospectus-using-multinomial-logistic-regression-a-machine-learning-model](https://journalclub.io/episodes/prediction-of-ipo-performance-from-prospectus-using-multinomial-logistic-regression-a-machine-learning-model) |
| Source | [https://www.semanticscholar.org/paper/35896c0ae1639edcf746515f2a99ce26cc664730](https://www.semanticscholar.org/paper/35896c0ae1639edcf746515f2a99ce26cc664730) |
| Year | 2026 |
| Citations | 1 |
| Authors | M. Alahmadi, Mustafa Tahsin Yilmaz |
| Paper ID | `848687d4-4111-478e-856a-7cec4e016597` |

## Classification

- **Problem Type:** classification
- **Domain:** Finance
- **Sub-domain:** Financial prediction models
- **Technique:** Multinomial Logistic Regression (MLR)
- **Technique Category:** classification_model
- **Type:** novel

## Summary

This paper presents a method for predicting the performance of initial public offerings (IPOs) using multinomial logistic regression (MLR) based on financial indicators extracted from prospectuses. Engineers should care because this approach can enhance investment decision-making by providing a more accurate prediction of IPO outcomes.

## Key Contribution

**The innovative application of multinomial logistic regression to predict IPO performance based on detailed prospectus data.**

## Problem

The challenge of accurately predicting the performance of IPOs based on various financial indicators and prospectus characteristics.

## Method

**Approach:** The method uses MLR to classify IPO performance into three categories: BELOW AVERAGE, AVERAGE, and ABOVE AVERAGE. It leverages financial ratios and prospectus characteristics as independent variables to predict the class of IPO performance.

**Algorithm:**

1. 1. Collect and preprocess data from prospectuses.
2. 2. Split data into training (90%) and testing (10%) sets.
3. 3. Normalize the training data.
4. 4. Train the MLR model using the training data.
5. 5. Calculate class probabilities using the trained model.
6. 6. Assign labels based on a predetermined threshold.
7. 7. Evaluate model performance using metrics like accuracy, recall, precision, and F1 score.

**Input:** Data from IPO prospectuses including financial ratios and prospectus characteristics.

**Output:** Predicted class of IPO performance: BELOW AVERAGE (0), AVERAGE (1), ABOVE AVERAGE (2).

**Key Parameters:**

- `learning_rate: 0.01`
- `threshold: 0.5`

**Complexity:** Not stated.

## Benchmarks

**Tested on:** Data from 55 IPOs in the Saudi stock market from 2010 to 2022.

**Results:**

- accuracy: 71.4%
- AUC: 0.71

**Compared against:** Other machine learning algorithms (not specified)

**Improvement:** MLR model showed higher accuracy compared to other machine learning algorithms.

## Implementation Guide

**Data Structures:** DataFrame for storing prospectus data, Arrays for feature vectors

**Dependencies:** Python, NumPy, Pandas, Scikit-learn

**Core Operation:**

```python
model.fit(X_train, y_train) to train the MLR model; predictions = model.predict(X_test) to classify IPO performance.
```

**Watch Out For:**

- Ensure data is cleaned and preprocessed to avoid skewed results.
- Watch for multicollinearity among independent variables.
- Be cautious of overfitting with a small dataset.

## Use This When

- You need to predict the performance of IPOs based on financial data.
- You have access to detailed prospectus information for companies going public.
- You want to classify outcomes into multiple categories rather than binary.

## Don't Use When

- The dataset is too small to train a reliable model.
- You require real-time predictions and cannot afford preprocessing time.
- The IPOs have unique characteristics that cannot be generalized.

## Key Concepts

multinomial logistic regression, IPO performance prediction, financial ratios, prospectus analysis

## Connects To

- Logistic Regression
- Random Forest
- Support Vector Machines
- Feature Selection Techniques

## Prerequisites

- Understanding of logistic regression
- Familiarity with financial ratios
- Knowledge of data preprocessing techniques

## Limitations

- Model performance may vary with different datasets.
- Limited to the features extracted from prospectuses.
- May not account for external market factors influencing IPO performance.

## Open Questions

- How can the model be adapted for different markets or regions?
- What additional features could improve prediction accuracy?

## Abstract

When a company goes public, the “offer” price is set through a combination of underwriter analysis, market conditions, negotiation, and more. After a lot of back and forth, all the stakeholders (and potential buyers) eventually reach what feels like a good number.
