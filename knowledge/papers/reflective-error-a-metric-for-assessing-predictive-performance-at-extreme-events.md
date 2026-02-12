# Reflective error: a metric for assessing predictive performance at extreme events

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1017/eds.2025.16` |
| Full Paper | [https://doi.org/10.1017/eds.2025.16](https://doi.org/10.1017/eds.2025.16) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/c33acb980799fe551bab562e160029a9f966af51](https://www.semanticscholar.org/paper/c33acb980799fe551bab562e160029a9f966af51) |
| Source | [https://journalclub.io/episodes/reflective-error-a-metric-for-assessing-predictive-performance-at-extreme-events](https://journalclub.io/episodes/reflective-error-a-metric-for-assessing-predictive-performance-at-extreme-events) |
| Source | [https://www.semanticscholar.org/paper/c33acb980799fe551bab562e160029a9f966af51](https://www.semanticscholar.org/paper/c33acb980799fe551bab562e160029a9f966af51) |
| Year | 2026 |
| Citations | 0 |
| Authors | R. E. Rouse, Henry Moss, Scott Hosking, Allan McRobie, Emily Shuckburgh |
| Paper ID | `a25e5141-4798-4856-b505-e6e158334bc0` |

## Classification

- **Problem Type:** error metric evaluation for regression models
- **Domain:** Machine Learning & AI
- **Sub-domain:** error metrics for regression models
- **Technique:** Reflective Error
- **Technique Category:** statistical_method
- **Type:** novel

## Summary

The paper introduces a new error metric called Reflective Error (RE) designed to assess predictive performance specifically at extreme events, addressing the limitations of traditional metrics like RMSE and R-squared. Engineers should care because this metric allows for better evaluation and optimization of models in applications where extreme predictions are critical, such as flood forecasting.

## Key Contribution

**The introduction of the Reflective Error metric that quantifies model performance sensitivity to extreme values in regression tasks.**

## Problem

Existing error metrics fail to adequately assess model performance in predicting extreme events, which are crucial in fields like environmental modeling.

## Method

**Approach:** Reflective Error is derived from the weighted form of RMSE, normalizing it to allow comparison across different scales. It uses a weighting function based on the empirical distribution of the target outputs to emphasize errors at extremes over routine data.

**Algorithm:**

1. 1. Fit an empirical distribution to the target outputs.
2. 2. Define the reflective weighting function Ψ(y) based on the fitted distribution.
3. 3. Calculate the standard RMSE.
4. 4. Calculate the weighted RMSE using Ψ(y).
5. 5. Compute Reflective Error as the ratio of weighted RMSE to standard RMSE.
6. 6. Normalize the Reflective Error to a scale of 0 to 1.

**Input:** Predicted values and observed target values from regression models.

**Output:** Reflective Error value indicating the distribution of error sensitivity to extremes.

**Key Parameters:**

- `α: 1 (default), β: 1 (default) for the weighting function`
- `α and β can be tuned for the reflective loss function, with typical values found to be 0.5 ≤ α ≤ 5 and 0.5 ≤ β - α ≤ 1.`

**Complexity:** Not stated.

## Benchmarks

**Tested on:** Synthetic normally distributed dataset, Real-world hydrological data from the River Avon and River Exe

**Results:**

- RMSE: 9.35 m³/s for River Avon, 2.68 m³/s for River Exe
- NSE: 0.87 for River Avon, 0.75 for River Exe
- RE: 0.92 for River Avon, 0.95 for River Exe

**Compared against:** Root Mean Squared Error (RMSE), Nash-Sutcliffe Efficiency (NSE)

**Improvement:** Reflective Error provides a better understanding of error distribution, particularly for extremes, which is not captured by RMSE or NSE.

## Implementation Guide

**Data Structures:** Arrays or lists for predicted and observed values., Data structures to hold the fitted probability distribution.

**Dependencies:** NumPy for numerical operations, SciPy for statistical functions and fitting distributions

**Core Operation:**

```python
RE = sum((y_i - y_hat_i)^2 * Ψ(y_i)) / sum((y_i - y_hat_i)^2)
```

**Watch Out For:**

- Ensure the empirical distribution is accurately fitted to avoid misleading RE values.
- Be cautious with the choice of α and β in the reflective loss function to maintain model performance.
- The RE metric is undefined if total error is 0 or ∞.

## Use This When

- Modeling environmental systems where extreme events are critical, such as flood prediction.
- Evaluating regression models where traditional metrics fail to capture performance at extremes.
- Optimizing machine learning models for applications sensitive to extreme predictions.

## Don't Use When

- The dataset does not exhibit significant extremes or outliers.
- The model performance needs to be assessed uniformly across all data points without emphasis on extremes.
- Data is uniformly distributed with no significant variation in extremes.

## Key Concepts

error metrics, extreme values, weighted RMSE, empirical distribution, reflective weighting function

## Connects To

- Root Mean Squared Error (RMSE)
- Nash-Sutcliffe Efficiency (NSE)
- Extreme Value Theory
- Weighted Loss Functions in Neural Networks

## Prerequisites

- Understanding of regression analysis and error metrics.
- Familiarity with empirical distribution fitting.
- Knowledge of machine learning model evaluation.

## Limitations

- Reflective Error does not quantify the magnitude of error, only its distribution.
- May not perform well on datasets without significant extremes.
- Requires careful tuning of parameters for optimal performance.

## Open Questions

- How can Reflective Error be adapted for discrete probability distributions?
- What are the best practices for selecting α and β in various applications?

## Abstract

If you're evaluating a regression model, especially in environmental modeling or scientific computing, you’re probably reaching for root mean squared error (RMSE), or maybe R-squared. These are the default metrics. They’re implemented in every major ML library. They're what you log during training, what you use in your plots, and what you hand over to stakeholders as a measure of how “good" the model is. But, as I mentioned above, there's a blind spot. RMSE tells you the magnitude of your model’s average deviation, but it’s insensitive to where those deviations occur in the distribution. Whether your model is consistently off in the tails, or only makes small errors in the mode, RMSE will often return the same score. That’s a problem if your application actually cares about getting the extremes right. Take flood prediction, for example. Missing the routine streamflow by a few percent is tolerable. Missing the flood crest by the same
