# Stochastic Resetting

**Stochastic Resetting enhances SGD by allowing model parameters to reset to a previous state, mitigating the effects of label noise during training.**

**Category:** optimization_algorithm  
**Maturity:** emerging

## How It Works

Stochastic Resetting integrates a mechanism into the Stochastic Gradient Descent (SGD) process where model parameters can revert to a checkpoint with a certain probability. This approach helps avoid overfitting to corrupted data by revisiting earlier, potentially more accurate states of the model. By doing so, it improves generalization performance, especially in the presence of label noise in the training dataset.

## Algorithm

**Input:** Corrupted training set D̃tr, validation set Dval, reset probability r, threshold T.

**Output:** Updated model parameters θ after training.

**Steps:**

1. Initialize model parameters θ0 and set iteration t = 0.
2. For each iteration t, sample a mini-batch Bt from the corrupted training set.
3. Update parameters θt using the SGD update rule.
4. With probability r, reset θt to a checkpoint θc.
5. Evaluate the model on the validation set and update the best checkpoint θbest if necessary.
6. If no improvement is seen for T iterations, update the checkpoint θc to θbest.

**Core Operation:** `θt = θt-1 - learning_rate * ∇L(Bt, θt-1)`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `learning_rate` | 0.01 | Affects the speed of convergence; too high may lead to instability. |
| `reset_probability` | r (0 < r < 1) | Higher values increase the likelihood of reverting to earlier states, which can help mitigate overfitting. |
| `threshold` | T (e.g., 1000 iterations) | Determines how long to wait before updating the checkpoint; longer thresholds may lead to slower adaptation. |

## Complexity

- **Time:** O(n * m) where n is the number of iterations and m is the size of the mini-batch.
- **Space:** O(k) where k is the number of checkpoints stored.
- **In practice:** Performance may vary based on the dataset and the degree of label noise present.

## Implementation

```python
def stochastic_resetting(train_data: np.ndarray, val_data: np.ndarray, learning_rate: float, reset_prob: float, threshold: int) -> np.ndarray:
    initialize_parameters()
    best_checkpoint = current_parameters
    for t in range(max_iterations):
        mini_batch = sample_mini_batch(train_data)
        update_parameters(mini_batch, learning_rate)
        if np.random.rand() < reset_prob:
            current_parameters = best_checkpoint
        if validation_improvement(val_data):
            best_checkpoint = current_parameters
        if no_improvement_for(threshold):
            update_checkpoint(best_checkpoint)
    return current_parameters
```

## Common Mistakes

- Not tuning the reset probability, leading to suboptimal performance.
- Failing to update the checkpoint appropriately, which can cause loss of better model states.
- Ignoring the effects of label noise on the dataset, which can mislead the training process.

## Use When

- Training DNNs on datasets with known label noise.
- Seeking to improve generalization performance in supervised learning tasks.
- Experiencing overfitting issues during model training.

## Avoid When

- The dataset is clean and free from label noise.
- Real-time training is required without interruptions.
- The computational resources are extremely limited.

## Tradeoffs

**Strengths:**

- Improves generalization performance in the presence of label noise.
- Helps prevent overfitting by revisiting better model states.
- Can lead to better validation metrics compared to standard SGD.

**Weaknesses:**

- May introduce additional computational overhead due to checkpoint management.
- Not effective on clean datasets, potentially wasting resources.
- Could slow down training if reset probability is too high.

**Compared To:**

- **vs Standard SGD:** Use Stochastic Resetting when dealing with noisy labels; otherwise, standard SGD may suffice.

## Connects To

- Stochastic Gradient Descent
- Dropout
- Batch Normalization
- Early Stopping

## Evidence (Papers)

- **Stochastic resetting mitigates latent gradient bias of SGD from label noise** [5 citations] - [DOI](https://doi.org/10.1088/2632-2153/adbc46)
