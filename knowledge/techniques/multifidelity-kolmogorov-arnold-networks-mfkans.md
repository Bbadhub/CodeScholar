# Multifidelity Kolmogorov-Arnold Networks (MFKANs)

**MFKANs leverage low-fidelity data to enhance predictions using a small set of high-fidelity data.**

**Category:** neural_architecture  
**Maturity:** emerging

## How It Works

MFKANs consist of three components: a low-fidelity Kolmogorov-Arnold Network (KAN) for initial predictions, a linear KAN to capture linear correlations, and a nonlinear KAN for adjustments. The low-fidelity KAN is pretrained and its weights are frozen, allowing the linear and nonlinear KANs to learn from the high-fidelity data. The outputs from both KANs are combined to produce refined high-fidelity predictions.

## Algorithm

**Input:** Low-fidelity dataset {(xi, fL(xi))} and high-fidelity dataset {(xj, fH(xj))}

**Output:** Predictions for high-fidelity data based on the learned correlations.

**Steps:**

1. 1. Pretrain the low-fidelity KAN using low-fidelity data.
2. 2. Freeze the weights of the low-fidelity KAN.
3. 3. Train the linear KAN to learn the linear correlation between low-fidelity predictions and high-fidelity data.
4. 4. Train the nonlinear KAN to learn the nonlinear correction.
5. 5. Combine outputs from the linear and nonlinear KANs to produce high-fidelity predictions.
6. 6. Optimize the loss function that includes penalties for overfitting.

**Core Operation:** `output = linear_KAN(low_fidelity_output) + nonlinear_KAN(low_fidelity_output)`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `learning_rate` | 0.001 | Affects the speed of convergence during training. |
| `penalization_weight (w)` | 0 or 1 | Controls the strength of the overfitting penalty. |
| `n (for penalization term)` | typically 4 | Determines the order of the penalization term. |
| `number of epochs` | preselected maximum | Sets the maximum training iterations without early stopping. |

## Complexity

- **Time:** Not stated
- **Space:** Not stated
- **In practice:** Performance may vary based on the complexity of the datasets used.

## Implementation

```python
def mfkan(low_fidelity_data: List[Tuple], high_fidelity_data: List[Tuple]) -> List:
    low_fidelity_kan = pretrain_low_fidelity_kan(low_fidelity_data)
    freeze_weights(low_fidelity_kan)
    linear_kan = train_linear_kan(low_fidelity_kan, high_fidelity_data)
    nonlinear_kan = train_nonlinear_kan(low_fidelity_kan, high_fidelity_data)
    return combine_outputs(linear_kan, nonlinear_kan)
```

## Common Mistakes

- Neglecting to freeze the weights of the low-fidelity KAN after pretraining.
- Overfitting the linear or nonlinear KANs due to insufficient high-fidelity data.
- Failing to properly tune the penalization weight, leading to poor generalization.

## Use When

- You have limited high-fidelity data but abundant low-fidelity data.
- You need to model complex functions with interpretable results.
- You want to reduce the cost of data collection in scientific applications.

## Avoid When

- You have sufficient high-fidelity data available.
- The relationship between low-fidelity and high-fidelity data is not expected to be strongly correlated.
- You require real-time predictions with minimal computational overhead.

## Tradeoffs

**Strengths:**

- Effectively combines low-fidelity and high-fidelity data.
- Captures complex correlations with fewer parameters than traditional methods.
- Provides interpretable results through its architecture.

**Weaknesses:**

- Performance heavily relies on the correlation between low and high-fidelity data.
- May not perform well with purely high-fidelity datasets.
- Training can be computationally intensive depending on the architecture.

**Compared To:**

- **vs Single-fidelity KANs:** Use MFKANs when low-fidelity data is abundant and high-fidelity data is scarce.
- **vs Multifidelity MLPs:** MFKANs are preferable for capturing complex correlations with fewer parameters.

## Connects To

- Kolmogorov-Arnold Networks (KANs)
- Multifidelity Learning
- Neural Networks
- Regression Analysis

## Evidence (Papers)

- **Multifidelity Kolmogorov-Arnold networks** - [DOI](https://doi.org/10.1088/2632-2153/adf702)
