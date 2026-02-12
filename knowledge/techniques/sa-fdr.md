# SA-FDR

*Also known as: Simulated Annealing for Feature Discriminant Ratio*

**SA-FDR optimizes feature selection using simulated annealing to maximize the Fisher Discriminant Ratio.**

**Category:** optimization_algorithm  
**Maturity:** emerging

## How It Works

SA-FDR employs simulated annealing to explore various feature subsets in a dataset. It uses the Fisher Discriminant Ratio (FDR) as a measure of model quality, iteratively refining the feature subsets through probabilistic transitions. By allowing the acceptance of worse solutions, it helps escape local minima, ultimately converging on the best subset of features that enhances model performance.

## Algorithm

**Input:** Dataset with samples and features, specified number of features to select (k).

**Output:** Best subset of features that maximizes the FDR.

**Steps:**

1. Initialize replicas as binary vectors representing feature subsets.
2. Compute FDR values for each replica.
3. Iteratively propose changes to feature subsets and accept or reject based on the Metropolis rule.
4. Adjust the temperature to control the acceptance probability of worse solutions.
5. Repeat until convergence or a maximum number of iterations is reached.
6. Evaluate the final feature subsets using logistic regression and select the best one.

**Core Operation:** `output = maximize(FDR(features))`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `R` | 50 | Increases the diversity of feature subsets explored. |
| `βsteps` | 100 | Controls the granularity of temperature adjustments. |
| `NS` | 0.5 | Determines the number of sweeps for temperature adjustments. |
| `ε` | 0.7 | Affects the acceptance probability of worse solutions. |
| `kmax` | 30 | Limits the maximum number of features considered. |

## Complexity

- **Time:** Not explicitly stated.
- **Space:** Not explicitly stated.
- **In practice:** Performance may vary based on dataset size and feature dimensionality.

## Implementation

```python
def sa_fdr(data: np.ndarray, k: int) -> List[int]:
    # Initialize replicas
    replicas = initialize_replicas(data, k)
    # Compute initial FDR values
    fdr_values = compute_fdr(replicas)
    while not converged:
        # Propose changes to feature subsets
        propose_changes(replicas)
        # Accept or reject based on Metropolis rule
        accept_changes(replicas, fdr_values)
    return best_subset(replicas)
```

## Common Mistakes

- Not properly tuning the temperature parameters, leading to poor convergence.
- Failing to evaluate the final feature subsets adequately.
- Overlooking the importance of the initial replica configuration.

## Use When

- Working with high-dimensional datasets where feature selection is critical.
- Needing a balance between model interpretability and predictive performance.
- Facing challenges with overfitting due to irrelevant features.

## Avoid When

- The dataset is low-dimensional and feature selection is not necessary.
- Real-time performance is critical and computational resources are limited.

## Tradeoffs

**Strengths:**

- Effectively handles high-dimensional feature spaces.
- Balances exploration and exploitation through probabilistic transitions.
- Can escape local minima by accepting worse solutions.

**Weaknesses:**

- Computationally intensive, especially with large datasets.
- Performance may vary significantly based on parameter settings.
- Not suitable for low-dimensional datasets.

**Compared To:**

- **vs Recursive Feature Elimination (RFE):** Use SA-FDR for larger feature sets where RFE may be computationally prohibitive.
- **vs Lasso:** SA-FDR may achieve better performance with fewer features compared to Lasso.

## Connects To

- Feature Selection
- Simulated Annealing
- Fisher Discriminant Analysis
- Logistic Regression

## Evidence (Papers)

- **Optimized feature subset selection via simulated annealing** - [DOI](https://doi.org/10.1088/2632-2153/ae20ed)
