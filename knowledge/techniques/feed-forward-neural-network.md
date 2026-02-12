# Feed-Forward Neural Network

*Also known as: FFNN, Feedforward Neural Network*

**A feed-forward neural network processes inputs through layers to produce outputs without feedback loops.**

**Category:** neural_architecture  
**Maturity:** proven

## How It Works

A feed-forward neural network consists of an input layer, one or more hidden layers, and an output layer. Data flows in one direction from input to output, with each layer applying weights and activation functions to transform the data. The network learns by adjusting these weights based on the error of its predictions during training, allowing it to generalize from the training data to make predictions on new data.

## Algorithm

**Input:** Binary signals from sensors (e.g., shape: [4])

**Output:** Control signals for the system (e.g., shape: [1])

**Steps:**

1. 1. Initialize the neural network with a specified number of input and hidden neurons.
2. 2. Connect the input neurons to the hidden layer using weights.
3. 3. Feed input data into the input layer.
4. 4. Apply an activation function to the hidden layer neurons.
5. 5. Generate output signals based on the hidden layer's activations.
6. 6. Use output signals to perform the desired task.

**Core Operation:** `output = activation_function(weights · input)`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `hidden_layer_size` | 10 | Increasing size can improve learning capacity but may lead to overfitting. |
| `activation_function` | satlins | Different functions can affect the network's ability to learn complex patterns. |

## Complexity

- **Time:** O(n * m * p) where n is the number of inputs, m is the number of hidden neurons, and p is the number of outputs.
- **Space:** O(m + p) for storing weights and activations.
- **In practice:** Performance can vary based on the architecture and the complexity of the task.

## Implementation

```python
def feed_forward_nn(input: List[float]) -> List[float]:
    hidden_layer = apply_activation(weights_hidden @ input)
    output = weights_output @ hidden_layer
    return output
```

## Common Mistakes

- Not normalizing input data, leading to poor performance.
- Choosing inappropriate activation functions for the task.
- Failing to properly initialize weights, which can hinder learning.

## Use When

- Building real-time control systems without an OS
- Implementing hardware-level control for escalators
- Developing efficient embedded systems

## Avoid When

- Need for complex processing beyond simple control
- When using existing microcontroller solutions is more feasible
- In scenarios requiring extensive software libraries

## Tradeoffs

**Strengths:**

- Simple architecture that is easy to implement.
- Effective for a wide range of tasks.
- Fast inference time due to the lack of feedback loops.

**Weaknesses:**

- Limited to problems that can be solved with a single pass of data.
- Can struggle with complex patterns requiring memory of past inputs.
- Prone to overfitting with too many hidden neurons.

**Compared To:**

- **vs Recurrent Neural Network:** Use RNNs for tasks requiring memory of previous inputs, like time series.

## Connects To

- Convolutional Neural Network
- Recurrent Neural Network
- Support Vector Machine
- Decision Trees

## Evidence (Papers)

- **FPGA-Based Realization of Intelligent Escalator Controller Using Artificial Neural Network** [2 citations] - [DOI](https://doi.org/10.1155/jece/7567924)
