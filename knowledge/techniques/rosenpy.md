# RosenPy

**RosenPy is a framework for building complex-valued neural networks using complex numbers for weights and activations.**

**Category:** neural_architecture  
**Maturity:** emerging

## How It Works

RosenPy allows users to define complex-valued neural network architectures, initializing weights and activations as complex numbers. The framework supports forward propagation using complex arithmetic, enabling the computation of loss and backpropagation for weight updates. This approach leverages the unique properties of complex numbers, making it suitable for specific applications like signal processing and telecommunications.

## Algorithm

**Input:** Data formatted as complex numbers, typically in the form of arrays or tensors.

**Output:** Predictions or classifications also represented as complex numbers.

**Steps:**

1. 1. Define the architecture of the complex-valued neural network.
2. 2. Initialize weights as complex numbers.
3. 3. Forward propagate inputs through the network using complex arithmetic.
4. 4. Compute loss based on the output and target values.
5. 5. Backpropagate the loss to update weights.
6. 6. Repeat for a specified number of epochs.

**Core Operation:** `output = complex_activation(weights · inputs)`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `learning_rate` | 0.001 | A higher learning rate may speed up training but can lead to instability. |
| `num_epochs` | 100 | More epochs can improve accuracy but increase training time. |
| `batch_size` | 32 | Larger batch sizes can stabilize training but require more memory. |

## Complexity

- **Time:** Not explicitly stated
- **Space:** Not explicitly stated
- **In practice:** Performance may vary based on the complexity of the network and the size of the input data.

## Implementation

```python
def train_complex_nn(data: List[complex], labels: List[complex], learning_rate: float = 0.001, num_epochs: int = 100, batch_size: int = 32) -> None:
    model = define_complex_architecture()
    for epoch in range(num_epochs):
        for batch in get_batches(data, batch_size):
            outputs = forward_propagate(model, batch)
            loss = compute_loss(outputs, labels)
            backpropagate(model, loss)
            update_weights(model, learning_rate)
```

## Common Mistakes

- Neglecting to properly initialize complex weights.
- Overlooking the need for complex arithmetic in forward propagation.
- Failing to adjust learning rates for complex-valued computations.

## Use When

- Building neural networks for signal processing tasks.
- Working with datasets that naturally involve complex numbers.
- Exploring advanced neural network architectures that require complex-valued computations.

## Avoid When

- The problem domain does not involve complex numbers.
- Simple tasks that can be solved with standard real-valued neural networks.
- When computational resources are extremely limited.

## Tradeoffs

**Strengths:**

- Utilizes the unique properties of complex numbers for specific applications.
- Can potentially improve performance in signal processing tasks.
- Allows for more expressive neural network architectures.

**Weaknesses:**

- Limited applicability to problems that do not involve complex numbers.
- Increased computational complexity compared to real-valued networks.
- May require more resources and expertise to implement effectively.

**Compared To:**

- **vs Standard real-valued neural networks:** Use RosenPy for tasks involving complex numbers; otherwise, standard networks are simpler.

## Connects To

- Complex-valued neural networks
- Signal processing techniques
- Telecommunications modeling
- Advanced neural network architectures

## Evidence (Papers)

- **RosenPy: An open source Python framework for complex-valued neural networks** [2 citations] - [DOI](https://doi.org/10.1016/j.softx.2024.101925)
