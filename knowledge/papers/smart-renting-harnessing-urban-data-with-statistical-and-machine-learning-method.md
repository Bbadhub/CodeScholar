# Smart Renting: Harnessing Urban Data with Statistical and Machine Learning Methods for Predicting Property Rental Prices from a Tenant’s Perspective

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3390/stats8010012` |
| Full Paper | [https://doi.org/10.3390/stats8010012](https://doi.org/10.3390/stats8010012) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/9960c6a38ff73ff0d2c4ef194a52833524b69a57](https://www.semanticscholar.org/paper/9960c6a38ff73ff0d2c4ef194a52833524b69a57) |
| Source | [https://journalclub.io/episodes/smart-renting-harnessing-urban-data-with-statistical-and-machine-learning-methods-for-predicting-property-rental-prices-from-a-tenants-perspective](https://journalclub.io/episodes/smart-renting-harnessing-urban-data-with-statistical-and-machine-learning-methods-for-predicting-property-rental-prices-from-a-tenants-perspective) |
| Source | [https://www.semanticscholar.org/paper/9960c6a38ff73ff0d2c4ef194a52833524b69a57](https://www.semanticscholar.org/paper/9960c6a38ff73ff0d2c4ef194a52833524b69a57) |
| Year | 2026 |
| Citations | 0 |
| Authors | Francisco Louzada, K. de Lacerda, P. H. Ferreira, Naomy Duarte Gomes |
| Paper ID | `2359f810-a031-4241-a0d0-c84d72047dd7` |

## Classification

- **Problem Type:** regression analysis for rental price prediction
- **Domain:** Machine Learning & AI
- **Sub-domain:** Regression Analysis
- **Technique:** XGBoost
- **Technique Category:** classification_model
- **Type:** novel

## Summary

This paper presents a machine learning framework for predicting rental prices in São Carlos, Brazil, using urban data. Engineers should care because it provides a practical application of ML techniques to a significant economic sector, enabling better decision-making for tenants and landlords.

## Key Contribution

**The development of a comprehensive machine learning model that accurately predicts rental prices based on various property attributes.**

## Problem

The lack of effective tools for estimating rental prices in the Brazilian market, particularly in the context of rising rental demand.

## Method

**Approach:** The method involves collecting rental property data, preprocessing it, and applying various machine learning models to predict rental prices. The best-performing model, XGBoost, captures complex relationships between property features and rental values.

**Algorithm:**

1. 1. Collect rental property data from a real estate website.
2. 2. Preprocess data: clean, encode categorical variables, and scale numerical variables.
3. 3. Split the dataset into training (80%) and testing (20%) sets.
4. 4. Apply various regression models including Linear Regression, SVR, Random Forest, XGBoost, KNN, and MLP.
5. 5. Use GridSearchCV for hyperparameter tuning with k-fold cross-validation.
6. 6. Evaluate models using metrics like MAE, MSE, RMSE, and R2.
7. 7. Select the best model based on performance metrics.

**Input:** Data frame containing property attributes: Type, Bedrooms, Bathrooms, Garages, Neighborhood, Suites, Furnished, and Rent_value.

**Output:** Predicted rental prices for the properties.

**Key Parameters:**

- `GridSearchCV: k-fold = 5`
- `XGBoost hyperparameters: not specified in detail`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Rental property data from Imobiliária Cardinali, São Carlos, Brazil (1166 rows, 8 columns)

**Results:**

- MAE: 517.77 BRL
- MSE: 910,429.47 BRL
- RMSE: 954.16 BRL
- R2: 0.74

**Compared against:** Linear Regression, SVR, Random Forest, KNN, MLP

**Improvement:** XGBoost outperformed other models with an R2 of 0.74.

## Implementation Guide

**Data Structures:** DataFrame for property attributes and rental prices

**Dependencies:** requests, Beautiful Soup, ScikitLearn, XGBoost, Matplotlib, statsmodels

**Core Operation:**

```python
model = XGBRegressor(); model.fit(X_train, y_train); predictions = model.predict(X_test)
```

**Watch Out For:**

- Ensure data is cleaned and preprocessed correctly before modeling.
- Be cautious of overfitting when tuning hyperparameters.
- Consider the impact of outliers on model performance.

## Use This When

- You need to predict rental prices based on property features.
- You want to develop a user-friendly platform for tenants and landlords.
- You are working in a market with limited rental price prediction tools.

## Don't Use When

- You require real-time price predictions with minimal data.
- You are dealing with a very small dataset.
- You need a model that interprets results in a straightforward manner.

## Key Concepts

Machine Learning, Regression Analysis, Data Preprocessing, Hyperparameter Tuning, Web Scraping, Feature Engineering

## Connects To

- Random Forest
- Support Vector Regression
- Linear Regression
- K-Nearest Neighbors
- Neural Networks

## Prerequisites

- Basic understanding of machine learning concepts
- Familiarity with Python programming
- Knowledge of regression analysis

## Limitations

- Model may struggle with extreme rental values due to limited data representation.
- The approach is specific to the São Carlos market and may not generalize well.
- Requires continuous data updates for accuracy.

## Open Questions

- How can the model be adapted for different geographical markets?
- What additional features could improve prediction accuracy?

## Abstract

In October 2025, Greystar, one of the largest property management firms in the US, agreed to pay 50 million dollars to settle accusations that it helped inflate rents through algorithmic collusion. Along with other landlords, Greystar had used RealPage’s rent-pricing system, an application that pooled non-public data from competing property owners and suggested coordinated rent adjustments. It analyzed demand, looked at competition and occupancy rates, then told landlords exactly how high the prices could go.
