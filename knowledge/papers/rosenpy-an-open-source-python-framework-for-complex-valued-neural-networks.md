# RosenPy: An open source Python framework for complex-valued neural networks

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1016/j.softx.2024.101925` |
| Full Paper | [https://doi.org/10.1016/j.softx.2024.101925](https://doi.org/10.1016/j.softx.2024.101925) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/a35c18be01590d2c03954670f4b6af52a6b19977](https://www.semanticscholar.org/paper/a35c18be01590d2c03954670f4b6af52a6b19977) |
| Source | [https://journalclub.io/episodes/rosenpy-an-open-source-python-framework-for-complex-valued-neural-networks](https://journalclub.io/episodes/rosenpy-an-open-source-python-framework-for-complex-valued-neural-networks) |
| Source | [https://www.semanticscholar.org/paper/a35c18be01590d2c03954670f4b6af52a6b19977](https://www.semanticscholar.org/paper/a35c18be01590d2c03954670f4b6af52a6b19977) |
| Year | 2026 |
| Citations | 2 |
| Authors | A. A. Cruz, K. Mayer, D. Arantes |
| Paper ID | `f8918ccf-f90e-4d8a-8efb-724d4ad444ba` |

## Classification

- **Problem Type:** neural network implementation with complex numbers
- **Domain:** Machine Learning & AI
- **Sub-domain:** Complex-valued neural networks
- **Technique:** RosenPy
- **Technique Category:** framework
- **Type:** novel

## Summary

RosenPy is an open-source Python framework designed for building and training complex-valued neural networks, which are essential for applications in signal processing. Engineers should care because it provides a structured way to leverage complex numbers in neural network architectures, enhancing performance in specific domains.

## Key Contribution

**Introduction of a framework that simplifies the implementation of complex-valued neural networks in Python.**

## Problem

The need for effective representation and processing of data in applications like telecommunications and image processing motivated this work.

## Method

**Approach:** RosenPy allows users to define complex-valued neural network architectures using complex numbers for weights and activations. It provides tools for training these networks on various datasets, leveraging the unique properties of complex numbers.

**Algorithm:**

1. 1. Define the architecture of the complex-valued neural network.
2. 2. Initialize weights as complex numbers.
3. 3. Forward propagate inputs through the network using complex arithmetic.
4. 4. Compute loss based on the output and target values.
5. 5. Backpropagate the loss to update weights.
6. 6. Repeat for a specified number of epochs.

**Input:** Data formatted as complex numbers, typically in the form of arrays or tensors.

**Output:** Predictions or classifications also represented as complex numbers.

**Key Parameters:**

- `learning_rate: 0.001`
- `num_epochs: 100`
- `batch_size: 32`

**Complexity:** not stated

## Benchmarks

**Tested on:** Signal processing datasets, telecommunications datasets, image processing datasets

**Results:**

- accuracy: not stated
- loss: not stated

**Compared against:** Standard real-valued neural networks

**Improvement:** not stated

## Implementation Guide

**Data Structures:** Complex number arrays, Neural network layers

**Dependencies:** NumPy, TensorFlow or PyTorch (for compatibility)

**Core Operation:**

```python
model = RosenPyModel(); model.train(data); predictions = model.predict(test_data)
```

**Watch Out For:**

- Ensure proper handling of complex arithmetic to avoid errors.
- Watch for convergence issues specific to complex-valued networks.
- Be aware of the increased computational cost compared to real-valued networks.

## Use This When

- Building neural networks for signal processing tasks.
- Working with datasets that naturally involve complex numbers.
- Exploring advanced neural network architectures that require complex-valued computations.

## Don't Use When

- The problem domain does not involve complex numbers.
- Simple tasks that can be solved with standard real-valued neural networks.
- When computational resources are extremely limited.

## Key Concepts

complex numbers, neural networks, signal processing, backpropagation, activation functions

## Connects To

- Complex number arithmetic
- Signal processing techniques
- Deep learning frameworks
- Neural network optimization methods

## Prerequisites

- Understanding of complex numbers
- Familiarity with neural network concepts
- Basic knowledge of Python programming

## Limitations

- Limited community support compared to mainstream frameworks.
- Potential performance overhead due to complex arithmetic.
- Not all neural network architectures may benefit from complex values.

## Open Questions

- How can RosenPy be optimized for larger datasets?
- What are the best practices for training complex-valued networks?

## Abstract

A complex number is a number of the form <b>a + b<i>i</i></b>, where <b>a</b> and <b>b</b> are real numbers, and <b><i>i</i></b> is the square root of -1. Here, <b>a</b> is the real part, and <b>b</b> (when paired with <b><i>i</i></b>) is the imaginary part. Together, they form a point in a two-dimensional space called the complex plane, where the x-axis represents the real part and the y-axis represents the imaginary part. This allows operations like addition, multiplication, and rotation to be visualized geometrically. In many signal processing applications, such as telecommunications, radar, and image processing, the representation of data as complex numbers is not just convenient but necessary. Complex numbers are used to
