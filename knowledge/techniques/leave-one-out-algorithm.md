# Leave-one-out algorithm

**The leave-one-out algorithm quantifies the contribution of individual treatment comparisons in network meta-analysis.**

**Category:** statistical_method  
**Maturity:** emerging

## How It Works

This algorithm iteratively excludes each treatment comparison from a network meta-analysis (CNMA) to assess its impact on the overall estimates. By recomputing the variances of the component effects without each comparison, it calculates how much each comparison contributes to the precision of the estimates. The results are normalized to create a contribution matrix that indicates the relative importance of each comparison.

## Algorithm

**Input:** Data representing treatment comparisons and their effects, structured in a network format.

**Output:** A normalized contribution matrix indicating the percentage contribution of each comparison to the precision of component estimates.

**Steps:**

1. 1. Conduct a CNMA for the full network to estimate all component effects and their variances.
2. 2. For each direct comparison, conduct a CNMA without that comparison and recompute all component effects and their variances.
3. 3. Calculate precision leverage for each comparison based on the change in variance when excluded.
4. 4. Normalize the precision leverage values to create a contribution matrix.

**Core Operation:** `Contribution = (Vfull,j - V−i,j) / Vfull,j`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `n` | number of distinct components | Affects the complexity and size of the contribution matrix. |
| `k` | number of edges (comparisons) | Influences the number of iterations and computations required. |
| `Vfull,j` | variance of component effect estimates from full network | Serves as a baseline for calculating contribution. |
| `V−i,j` | variance of component effect estimates after excluding comparison i | Determines the impact of excluding a comparison. |

## Complexity

- **Time:** Not explicitly stated
- **Space:** Not explicitly stated
- **In practice:** Performance may vary based on the number of comparisons and components in the network.

## Implementation

```python
def leave_one_out_analysis(data: List[Comparison]) -> ContributionMatrix:
    full_effects, full_variances = conduct_cnma(data)
    contribution_matrix = []
    for comparison in data:
        reduced_data = exclude_comparison(data, comparison)
        effects, variances = conduct_cnma(reduced_data)
        precision_leverage = calculate_precision_leverage(full_variances, variances)
        contribution_matrix.append(normalize(precision_leverage))
    return contribution_matrix
```

## Common Mistakes

- Failing to properly normalize the precision leverage values.
- Not accounting for overlapping components in the treatment comparisons.
- Assuming linearity without validating the assumptions of the model.

## Use When

- You need to analyze the contribution of individual treatment comparisons in complex interventions.
- You are working with multicomponent treatment data and need to disentangle effects.
- You require a robust method to enhance the interpretability of CNMA results.

## Avoid When

- The treatment comparisons do not exhibit overlapping components.
- You are dealing with simple pairwise meta-analysis without complex interactions.
- The assumptions of linear additivity and identifiability are violated.

## Tradeoffs

**Strengths:**

- Provides a detailed understanding of individual contributions to overall estimates.
- Enhances the interpretability of complex treatment networks.
- Improves precision in contribution analysis compared to traditional methods.

**Weaknesses:**

- Computationally intensive for large networks with many comparisons.
- May not be applicable for simple pairwise analyses.
- Assumes linear relationships which may not hold in all cases.

**Compared To:**

- **vs Traditional network meta-analysis methods:** Use leave-one-out for more precise contribution analysis.

## Connects To

- Network meta-analysis (NMA)
- Bayesian meta-analysis
- Meta-regression
- Sensitivity analysis

## Evidence (Papers)

- **A leave-one-out algorithm for contribution analysis in component network meta-analysis** [3 citations] - [DOI](https://doi.org/10.1186/s12874-025-02619-w)
