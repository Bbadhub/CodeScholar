# Predicting the RUL of Li-Ion Batteries in UAVs Using Machine Learning Techniques

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3390/computers13030064` |
| Full Paper | [https://doi.org/10.3390/computers13030064](https://doi.org/10.3390/computers13030064) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/f4c7d3bd285c32c536c6a454a130d0c493b70012](https://www.semanticscholar.org/paper/f4c7d3bd285c32c536c6a454a130d0c493b70012) |
| Source | [https://journalclub.io/episodes/predicting-the-rul-of-li-ion-batteries-in-uavs-using-machine-learning-techniques](https://journalclub.io/episodes/predicting-the-rul-of-li-ion-batteries-in-uavs-using-machine-learning-techniques) |
| Source | [https://www.semanticscholar.org/paper/f4c7d3bd285c32c536c6a454a130d0c493b70012](https://www.semanticscholar.org/paper/f4c7d3bd285c32c536c6a454a130d0c493b70012) |
| Year | 2026 |
| Citations | 11 |
| Authors | D. Andrioaia, V. Găitan, George Culea, I. Banu |
| Paper ID | `dff0b46c-3efe-4a89-abf1-c48b021ad488` |

## Classification

- **Problem Type:** regression analysis
- **Domain:** Machine Learning & AI
- **Sub-domain:** Predictive Maintenance
- **Technique:** Support Vector Machine for Regression (SVMR), Multiple Linear Regression (MLR), Random Forest (RF)
- **Technique Category:** regression_model
- **Type:** comparison

## Summary

This paper presents a machine learning approach to predict the Remaining Useful Life (RUL) of Li-Ion batteries used in UAVs, addressing the critical need for efficient battery management to prevent premature or delayed replacements. Engineers should care because accurate RUL predictions can significantly reduce operational costs and enhance safety in UAV operations.

## Key Contribution

**Development of a machine learning model to predict the RUL of Li-ion batteries specifically for UAV applications.**

## Problem

The need to accurately predict when Li-ion batteries in UAVs will reach the end of their useful life to optimize maintenance schedules and prevent operational failures.

## Method

**Approach:** The method involves collecting historical data from Li-ion batteries during charge/discharge cycles, preprocessing this data, and training machine learning models to learn the relationship between battery parameters and their RUL. The models predict the number of remaining cycles based on voltage, current, and capacity data.

**Algorithm:**

1. 1. Collect historical data from battery sensors during charge/discharge cycles.
2. 2. Preprocess the data (cleaning, scaling, feature extraction).
3. 3. Train the machine learning model using the preprocessed data.
4. 4. Predict the number of cycles elapsed and remaining capacity.
5. 5. Calculate RUL based on the predicted cycles and fault threshold.

**Input:** Voltage (U), Current (I), Discharged Capacity (C) at each cycle.

**Output:** Predicted number of remaining cycles and RUL.

**Key Parameters:**

- `SVMR: C = 0.1, kernel = poly, degree = 3.5, gamma = scale`
- `MLR: fit_intercept = True, copy_X = bool`
- `RF: n_estimators = 600, criterion = squared_error, random_state = 1`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Data from monitoring two Li-ion batteries over 1200 charge/discharge cycles.

**Results:**

- MAE (SVMR: 1.02, MLR: 67.21, RF: 1.53)
- MSE (SVMR: 51.02, MLR: 87.25, RF: 63.77)
- RMSE (SVMR: 7.14, MLR: 7614.10, RF: 7.98)
- R2 Score (SVMR: 0.99, MLR: 0.93, RF: 0.99)

**Compared against:** Comparison against standard regression methods.

**Improvement:** SVMR and RF achieved R2 scores of 0.99, indicating high accuracy.

## Implementation Guide

**Data Structures:** DataFrame for storing battery parameters, Arrays for input features and output labels

**Dependencies:** Python 3.6, TensorFlow, Pandas

**Core Operation:**

```python
model.fit(X_train, y_train); predictions = model.predict(X_test)
```

**Watch Out For:**

- Ensure data is cleaned and preprocessed before training.
- Monitor for overfitting, especially with complex models like RF.
- Adjust hyperparameters based on cross-validation results.

## Use This When

- You need to optimize battery replacement schedules for UAVs.
- You want to implement a predictive maintenance system for battery management.
- You have access to historical battery performance data.

## Don't Use When

- You require real-time predictions without historical data.
- You are working with battery types other than Li-ion.
- You need a solution that does not involve machine learning.

## Key Concepts

Remaining Useful Life, Li-Ion Batteries, Predictive Maintenance, Machine Learning, Regression Analysis

## Connects To

- Support Vector Machines
- Linear Regression
- Random Forest
- Predictive Maintenance Systems

## Prerequisites

- Understanding of machine learning concepts
- Familiarity with regression techniques
- Knowledge of battery performance metrics

## Limitations

- Model performance may vary with different battery chemistries.
- Requires sufficient historical data for training.
- May not generalize well to other applications without adaptation.

## Open Questions

- How can the model be adapted for different battery types?
- What additional features could improve prediction accuracy?

## Abstract

As lithium-ion batteries age they get worse and worse and eventually reach the end of their useful life. This is a big issue for companies who operate fleets of UAVs (drones). If they replace the batteries in their drones too early, they’re wasting money. If they replace them too late their missions and deliveries get compromised. So they need a way to predict exactly when a drone’s battery is going to reach the end of its useful life. This paper is using AI to do exactly that. Let's take a look.
