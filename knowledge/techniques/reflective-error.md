# Reflective Error

**Reflective Error is a metric that assesses predictive performance with a focus on extreme events.**

**Category:** statistical_method  
**Maturity:** emerging

## How It Works

Reflective Error is derived from a weighted version of RMSE, which normalizes the error to facilitate comparisons across different scales. It emphasizes errors at extreme values by using a weighting function based on the empirical distribution of the target outputs. This allows for a more nuanced understanding of model performance, particularly in scenarios where extreme predictions are critical.

## Algorithm

**Input:** Predicted values and observed target values from regression models (arrays of floats).

**Output:** Reflective Error value (float) indicating the sensitivity of error to extremes.

**Steps:**

1. 1. Fit an empirical distribution to the target outputs.
2. 2. Define the reflective weighting function Ψ(y) based on the fitted distribution.
3. 3. Calculate the standard RMSE.
4. 4. Calculate the weighted RMSE using Ψ(y).
5. 5. Compute Reflective Error as the ratio of weighted RMSE to standard RMSE.
6. 6. Normalize the Reflective Error to a scale of 0 to 1.

**Core Operation:** `Reflective Error = Weighted RMSE / Standard RMSE`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `α` | 1 (default) | Tuning α affects the sensitivity of the weighting function. |
| `β` | 1 (default) | Tuning β influences the reflective loss function's behavior. |

## Complexity

- **Time:** O(n) for fitting the empirical distribution and calculating RMSE
- **Space:** O(n) for storing predicted and observed values
- **In practice:** Performance may vary based on the complexity of the empirical distribution fitting.

## Implementation

```python
def reflective_error(predictions: List[float], targets: List[float], alpha: float = 1, beta: float = 1) -> float:
    # Step 1: Fit empirical distribution
    distribution = fit_empirical_distribution(targets)
    # Step 2: Define weighting function
    weights = define_weighting_function(distribution, alpha, beta)
    # Step 3: Calculate RMSE
    rmse = calculate_rmse(predictions, targets)
    # Step 4: Calculate weighted RMSE
    weighted_rmse = calculate_weighted_rmse(predictions, targets, weights)
    # Step 5: Compute Reflective Error
    reflective_error = weighted_rmse / rmse
    # Step 6: Normalize
    return normalize(reflective_error)
```

## Common Mistakes

- Neglecting to fit the empirical distribution accurately.
- Using inappropriate values for α and β without tuning.
- Failing to interpret the Reflective Error in the context of extreme events.

## Use When

- Modeling environmental systems where extreme events are critical, such as flood prediction.
- Evaluating regression models where traditional metrics fail to capture performance at extremes.
- Optimizing machine learning models for applications sensitive to extreme predictions.

## Avoid When

- The dataset does not exhibit significant extremes or outliers.
- The model performance needs to be assessed uniformly across all data points without emphasis on extremes.
- Data is uniformly distributed with no significant variation in extremes.

## Tradeoffs

**Strengths:**

- Provides a better understanding of error distribution, particularly for extremes.
- Normalizes error for comparison across different scales.
- Emphasizes performance in critical scenarios where extremes matter.

**Weaknesses:**

- May not be suitable for datasets without significant extremes.
- Complexity in defining the empirical distribution accurately.
- Potential overemphasis on extremes can obscure overall model performance.

**Compared To:**

- **vs Root Mean Squared Error (RMSE):** Use Reflective Error when extremes are critical; RMSE is better for uniform performance assessment.

## Connects To

- Root Mean Squared Error (RMSE)
- Nash-Sutcliffe Efficiency (NSE)
- Quantile Regression
- Extreme Value Theory

## Evidence (Papers)

- **Reflective error: a metric for assessing predictive performance at extreme events** - [DOI](https://doi.org/10.1017/eds.2025.16)
