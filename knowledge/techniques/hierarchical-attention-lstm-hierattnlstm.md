# Hierarchical Attention LSTM (HierAttnLSTM)

**HierAttnLSTM is a neural network model designed for spatial-temporal traffic forecasting using a hierarchical attention mechanism.**

**Category:** neural_architecture  
**Maturity:** emerging

## How It Works

HierAttnLSTM processes traffic data through multiple layers of LSTM units, capturing both short-term fluctuations and long-term trends. It employs attention pooling to weigh the importance of hidden and cell states from lower layers before passing them to higher layers. This hierarchical structure allows the model to effectively learn complex patterns in traffic data across different time scales.

## Algorithm

**Input:** Traffic state data including speed, density, volume, and travel time (shape: [batch_size, time_steps, features])

**Output:** Predicted traffic states for all corridors over a specified time horizon (shape: [batch_size, output_size])

**Steps:**

1. Initialize LSTM layers with input traffic data.
2. For each time step, compute hidden and cell states using LSTM equations.
3. Apply affine transformations to hidden and cell states.
4. Compute attention weights using softmax on transformed states.
5. Pool hidden states and cell states using attention weights.
6. Feed pooled states into the upper layer LSTM.
7. Repeat for multiple layers to capture hierarchical features.
8. Output final predictions through a fully connected layer.

**Core Operation:** `output = fully_connected_layer(pooled_states)`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `number_of_layers` | 3 | Increasing layers may capture more complex patterns but can lead to overfitting. |
| `window_size` | 5 | Larger window sizes can capture longer trends but may increase computational complexity. |
| `learning_rate` | 0.001 | Higher learning rates can speed up training but may lead to instability. |
| `batch_size` | 64 | Larger batch sizes can improve training speed but may require more memory. |

## Complexity

- **Time:** O(n * m * p)
- **Space:** O(n * m)
- **In practice:** Performance can vary significantly based on the size of the dataset and the complexity of the traffic patterns.

## Implementation

```python
def hierarchical_attention_lstm(data: np.ndarray) -> np.ndarray:
    lstm_layers = initialize_lstm_layers(data)
    for time_step in range(data.shape[1]):
        hidden_states, cell_states = compute_lstm_states(lstm_layers, data[:, time_step])
        attention_weights = compute_attention_weights(hidden_states)
        pooled_states = pool_states(hidden_states, cell_states, attention_weights)
        lstm_layers = feed_to_upper_layer(lstm_layers, pooled_states)
    return output_final_predictions(lstm_layers)
```

## Common Mistakes

- Neglecting to tune hyperparameters like learning rate and batch size.
- Using insufficient training data leading to overfitting.
- Failing to preprocess input data adequately for temporal patterns.

## Use When

- You need to predict traffic states across multiple corridors.
- You want to capture both short-term and long-term traffic patterns.
- You are dealing with complex spatial-temporal data.

## Avoid When

- The dataset is too small or lacks temporal granularity.
- Real-time prediction is not critical.
- You require a simpler model without hierarchical complexity.

## Tradeoffs

**Strengths:**

- Captures complex spatial-temporal dependencies effectively.
- Improves prediction accuracy over traditional LSTM models.
- Hierarchical structure allows for multi-scale learning.

**Weaknesses:**

- Increased computational complexity compared to simpler models.
- Requires larger datasets for effective training.
- May be prone to overfitting if not properly regularized.

**Compared To:**

- **vs Traditional LSTM:** Use HierAttnLSTM for complex patterns; use LSTM for simpler tasks.
- **vs Graph Neural Networks:** Use HierAttnLSTM for temporal data; use GNNs for spatial relationships.

## Connects To

- LSTM
- Attention Mechanisms
- Graph Neural Networks
- Temporal Convolutional Networks

## Evidence (Papers)

- **Network level spatial temporal traffic forecasting with Hierarchical Attention LSTM** [8 citations] - [DOI](https://doi.org/10.48130/dts-0024-0021)
