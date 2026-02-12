# AE+SINDy-C

**AE+SINDy-C combines autoencoders and Sparse Identification of Nonlinear Dynamics with Control for efficient learning and control of high-dimensional systems.**

**Category:** optimization_algorithm  
**Maturity:** emerging

## How It Works

The AE+SINDy-C framework leverages autoencoders to compress the state and action spaces into lower-dimensional latent representations. By applying the SINDy-C algorithm in this latent space, it predicts future states while minimizing reconstruction and SINDy losses. This approach allows for effective control of complex systems with fewer interactions, making it suitable for scenarios where data is limited.

## Algorithm

**Input:** Current state and control input, both represented in high-dimensional space.

**Output:** Predicted next state in the observation space.

**Steps:**

1. 1. Encode the observed state and control input using separate encoder networks.
2. 2. Apply the SINDy-C algorithm in the latent space to predict the next state.
3. 3. Decode the predicted state back to the observation space.
4. 4. Compute the reconstruction loss and SINDy loss.
5. 5. Optimize the model parameters to minimize the combined loss.

**Core Operation:** `output = decode(SINDy-C(latent_state, latent_control))`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `NLat_x` | dimension size | Increases or decreases the capacity of state representation. |
| `NLat_u` | dimension size | Increases or decreases the capacity of control representation. |
| `λ1, λ2, λ3` | regularization parameters | Adjusts the trade-off between fitting the data and model complexity. |

## Complexity

- **Time:** Not stated
- **Space:** Not stated
- **In practice:** Performance may vary based on the dimensionality of the input data and the architecture of the autoencoders.

## Implementation

```python
def ae_sindy_c(state: np.ndarray, control: np.ndarray) -> np.ndarray:
    latent_state = encoder_state(state)
    latent_control = encoder_control(control)
    predicted_latent_state = sindy_c(latent_state, latent_control)
    return decoder(predicted_latent_state)
```

## Common Mistakes

- Neglecting to tune the latent dimensions for optimal performance.
- Overfitting the model by using inappropriate regularization parameters.
- Failing to validate the model on unseen data before deployment.

## Use When

- Controlling high-dimensional nonlinear systems with limited data.
- Needing interpretable models for safety-critical applications.
- Reducing the computational cost of simulations in control tasks.

## Avoid When

- The system dynamics are fully observable and low-dimensional.
- Real-time performance is critical and cannot accommodate the training time.
- The application does not require interpretability.

## Tradeoffs

**Strengths:**

- Improves sample efficiency in learning dynamics.
- Provides interpretable models suitable for critical applications.
- Reduces computational costs in control tasks.

**Weaknesses:**

- May not perform well in fully observable low-dimensional systems.
- Training time can be significant, affecting real-time applications.
- Interpretability may not be necessary for all applications.

**Compared To:**

- **vs Traditional SINDy:** Use AE+SINDy-C when dealing with high-dimensional data; traditional SINDy is better for simpler systems.

## Connects To

- Autoencoders
- Sparse Identification of Nonlinear Dynamics (SINDy)
- Model Predictive Control (MPC)
- Dimensionality Reduction Techniques

## Evidence (Papers)

- **Interpretable and efficient data-driven discovery and control of distributed systems** [2 citations] - [DOI](https://doi.org/10.1017/dce.2025.10027)
