# FPGA-Based Realization of Intelligent Escalator Controller Using Artificial Neural Network

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1155/jece/7567924` |
| Full Paper | [https://doi.org/10.1155/jece/7567924](https://doi.org/10.1155/jece/7567924) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/4fbc1e0cd74ed787bbba1f35da1d034dd8787b74](https://www.semanticscholar.org/paper/4fbc1e0cd74ed787bbba1f35da1d034dd8787b74) |
| Source | [https://journalclub.io/episodes/fpga-based-realization-of-intelligent-escalator-controller-using-artificial-neural-network](https://journalclub.io/episodes/fpga-based-realization-of-intelligent-escalator-controller-using-artificial-neural-network) |
| Source | [https://www.semanticscholar.org/paper/4fbc1e0cd74ed787bbba1f35da1d034dd8787b74](https://www.semanticscholar.org/paper/4fbc1e0cd74ed787bbba1f35da1d034dd8787b74) |
| Year | 2026 |
| Citations | 2 |
| Authors | A. Saeed, S. A. Gitaffa, Reem I. Dawai |
| Paper ID | `fa8ef7d1-0f94-4bde-90f1-edd1b87767c5` |

## Classification

- **Problem Type:** real-time control systems
- **Domain:** Robotics & Control Systems
- **Sub-domain:** Embedded systems
- **Technique:** Feed-Forward Neural Network
- **Technique Category:** neural_architecture
- **Type:** novel

## Summary

The paper presents a real-time escalator controller implemented on an FPGA using a feed-forward neural network, eliminating the need for an operating system or microcontroller. Engineers should care because this approach allows for efficient hardware-level control of escalators, enhancing responsiveness and reliability.

## Key Contribution

**Development of an FPGA-based intelligent escalator controller using a feed-forward neural network without an operating system.**

## Problem

The need for a responsive and reliable escalator control system that operates without traditional computing resources.

## Method

**Approach:** The method involves a feed-forward neural network that processes binary signals from infrared sensors to determine the occupancy of escalator steps. The network consists of an input layer, a hidden layer with a specific activation function, and outputs that control the escalator's operation.

**Algorithm:**

1. 1. Initialize the neural network with 4 input neurons and 10 hidden neurons.
2. 2. Connect the input neurons to the hidden layer using weights.
3. 3. Feed the binary signals from the infrared sensors into the input layer.
4. 4. Apply the satlins activation function to the hidden layer neurons.
5. 5. Generate output signals based on the hidden layer's activations.
6. 6. Control the escalator's operation based on the output signals.

**Input:** Four binary signals from infrared sensors indicating occupancy of escalator steps.

**Output:** Control signals for the escalator's operation.

**Key Parameters:**

- `hidden_layer_size: 10`
- `activation_function: satlins`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Prototype escalator with infrared sensors

**Results:**

- Response time, accuracy of occupancy detection

**Compared against:** Traditional microcontroller-based escalator controllers

**Improvement:** Not stated

## Implementation Guide

**Data Structures:** Neural network architecture, Weight matrices

**Dependencies:** FPGA development tools, Neural network libraries for FPGA

**Core Operation:**

```python
output = satlins(weights * input)
```

**Watch Out For:**

- Ensure proper weight initialization
- Monitor for overfitting in the neural network
- Test the system under various occupancy scenarios

## Use This When

- Building real-time control systems without an OS
- Implementing hardware-level control for escalators
- Developing efficient embedded systems

## Don't Use When

- Need for complex processing beyond simple control
- When using existing microcontroller solutions is more feasible
- In scenarios requiring extensive software libraries

## Key Concepts

FPGA, neural networks, real-time control, embedded systems

## Connects To

- FPGA programming
- Neural network optimization
- Real-time embedded systems

## Prerequisites

- Basic understanding of neural networks
- Familiarity with FPGA architecture
- Knowledge of real-time systems

## Limitations

- Limited to simple control tasks
- Requires specific hardware setup
- Not suitable for complex decision-making

## Open Questions

- How to scale the system for larger escalators?
- What are the implications of using different activation functions?

## Abstract

the problem they are solving is narrow but not trivial: build a real-time controller with no operating system. No microcontroller. Just a feed-forward neural net burned into silicon. Let’s walk through the structure of the neural network they built to handle the task. The input to the network consists of four binary signals. Each corresponds to one of the four stair-steps in the prototype escalator. These are hard-wired signals coming from discrete infrared sensors mounted at each step. Each signal is either high (occupied) or low (empty), giving us a total input space of 16 unique combinations. These four binary inputs feed directly into the input layer of the neural network. The input layer consists of 4 neurons. These feed into a single hidden layer containing 10 neurons. The hidden layer uses the satlins activation function, a symmetric saturated linear function with output constrained between -1 and +1. Satlins behaves similarly to tansig or
