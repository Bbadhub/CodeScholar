# Scoop

**Scoop is an optimization algorithm designed to enhance the training of models for profiling attacks against higher-order masking in cryptographic implementations.**

**Category:** optimization_algorithm  
**Maturity:** emerging

## How It Works

Scoop leverages second-order derivatives of the loss function to navigate the loss landscape more effectively, which helps in overcoming low-gradient areas that can hinder optimization. It employs sparse mirror descent to utilize the intrinsic sparsity of information present in side-channel attack traces. This combination allows for more efficient training, particularly in scenarios where traditional methods struggle with plateau effects.

## Algorithm

**Input:** Training data consisting of traces and corresponding secret values.

**Output:** Trained model parameters that minimize the loss function.

**Steps:**

1. Initialize model parameters using a distribution (e.g., Kaiming uniform).
2. Compute the loss function based on the model's predictions.
3. Calculate the gradient and Hessian of the loss function.
4. Update model parameters using the second-order optimization rule.
5. Incorporate sparse mirror descent to enhance performance.
6. Repeat until convergence or a set number of iterations.

**Core Operation:** `model_parameters = model_parameters - learning_rate * (gradient + Hessian * model_parameters)`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `learning_rate` | 0.001 | A higher learning rate may speed up convergence but risks overshooting minima. |
| `batch_size` | 32 | Larger batch sizes can stabilize training but may require more memory. |
| `number_of_iterations` | 1000 | Increasing iterations can lead to better convergence but may also increase training time. |

## Complexity

- **Time:** Not explicitly stated, but generally higher than first-order methods due to Hessian calculations.
- **Space:** Not explicitly stated, but requires storage for Hessian and gradients.
- **In practice:** Real-world performance may vary based on the specific characteristics of the dataset and model architecture.

## Implementation

```python
def scoop_optimization(data: np.ndarray, labels: np.ndarray, learning_rate: float = 0.001, batch_size: int = 32, iterations: int = 1000) -> np.ndarray:
    parameters = initialize_parameters()
    for i in range(iterations):
        loss = compute_loss(parameters, data, labels)
        gradient, hessian = compute_gradients(loss)
        parameters -= learning_rate * (gradient + hessian @ parameters)
        if convergence_criteria_met():
            break
    return parameters
```

## Common Mistakes

- Neglecting to properly initialize parameters, which can lead to poor convergence.
- Using an inappropriate learning rate that either slows down training or causes divergence.
- Failing to account for the sparsity of the data, which can lead to inefficient training.

## Use When

- You need to optimize deep learning models for profiling attacks against cryptographic implementations.
- You are facing challenges with the plateau effect in optimization during training.
- You require a more efficient method for training models on small datasets typical in side-channel analysis.

## Avoid When

- The problem does not involve deep learning or profiling attacks.
- You are working with large-scale datasets where traditional optimization methods suffice.
- The application does not require handling of higher-order masking schemes.

## Tradeoffs

**Strengths:**

- Effectively reduces plateau length in optimization.
- Utilizes second-order information for better convergence.
- Adapts well to small datasets typical in side-channel analysis.

**Weaknesses:**

- Higher computational cost due to Hessian calculations.
- May not perform well on large-scale datasets.
- Complexity in implementation compared to first-order methods.

**Compared To:**

- **vs Standard SGD:** Use Scoop when facing plateau effects; otherwise, SGD may suffice.
- **vs Adam:** Scoop may outperform Adam in specific scenarios involving higher-order masking.

## Connects To

- Stochastic Gradient Descent (SGD)
- Adam Optimizer
- Higher-Order Optimization Methods
- Sparse Mirror Descent
- Cryptographic Profiling Techniques

## Evidence (Papers)

- **Scoop: An Optimization Algorithm for Profiling Attacks against Higher-Order Masking** - [DOI](https://doi.org/10.46586/tches.v2025.i3.56-80)
