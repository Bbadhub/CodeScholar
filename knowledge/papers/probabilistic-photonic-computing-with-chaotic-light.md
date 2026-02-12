# Probabilistic photonic computing with chaotic light

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1038/s41467-024-54931-6` |
| Full Paper | [https://doi.org/10.1038/s41467-024-54931-6](https://doi.org/10.1038/s41467-024-54931-6) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/aa92309c0880d82a9631c1936204dfa4b552f3b3](https://www.semanticscholar.org/paper/aa92309c0880d82a9631c1936204dfa4b552f3b3) |
| Source | [https://journalclub.io/episodes/probabilistic-photonic-computing-with-chaotic-light](https://journalclub.io/episodes/probabilistic-photonic-computing-with-chaotic-light) |
| Source | [https://www.semanticscholar.org/paper/aa92309c0880d82a9631c1936204dfa4b552f3b3](https://www.semanticscholar.org/paper/aa92309c0880d82a9631c1936204dfa4b552f3b3) |
| Year | 2026 |
| Citations | 29 |
| Authors | Frank Brückerhoff-Plückelmann, Hendrik Borras, Bernhard Klein, Akhil Varri, Marlon Becker, Jelle Dijkstra |
| Paper ID | `2e98edd2-4c05-4ab4-a5b1-715253062605` |

## Classification

- **Problem Type:** probabilistic computing
- **Domain:** Machine Learning & AI
- **Sub-domain:** Bayesian Neural Networks
- **Technique:** Photonic Probabilistic Computing
- **Technique Category:** framework
- **Type:** novel

## Summary

The paper presents a novel approach to probabilistic photonic computing using chaotic light to enable high-speed computations and uncertainty quantification in Bayesian neural networks. Engineers should care because this method allows for faster processing and better handling of uncertainty compared to traditional electronic computing methods.

## Key Contribution

**Introduction of a photonic architecture that utilizes chaotic light for probabilistic computation and uncertainty quantification in neural networks.**

## Problem

The need for efficient computation of probabilistic models and uncertainty quantification in artificial neural networks motivated this work.

## Method

**Approach:** The method employs chaotic light as an entropy source to perform probabilistic computations in a photonic crossbar array. It enables parallel sampling and efficient encoding of probabilistic information for Bayesian neural networks.

**Algorithm:**

1. 1. Generate chaotic light using amplified spontaneous emission.
2. 2. Split and delay the light to create independent optical signals.
3. 3. Encode input distributions onto the optical carrier using electro-optic modulators.
4. 4. Perform matrix-vector multiplications in the photonic crossbar array using non-volatile phase change material.
5. 5. Demultiplex the output signal to sample from the probability density functions in parallel.

**Input:** Encoded distributions of input data represented as optical signals.

**Output:** Probability density functions representing the results of probabilistic computations.

**Key Parameters:**

- `symbol_rate: 17.6 GBaud`
- `optical_bandwidth: several THz`
- `transmission_coefficient: 0.6 (for GST cell)`

**Complexity:** not stated

## Benchmarks

**Tested on:** MNIST

**Results:**

- accuracy: >99%
- Mutual Information (MI) for OOD detection

**Compared against:** Deterministic ANNs, Maximum Predicted Softmax Probability, MaxLogit, Energy-based methods

**Improvement:** Significantly better uncertainty quantification compared to deterministic methods.

## Implementation Guide

**Data Structures:** photonic crossbar array, chaotic light source, electro-optic modulators, phase change material (GST)

**Dependencies:** Optical components for chaotic light generation, Electro-optic modulators, Photonic crossbar architecture

**Core Operation:**

```python
chaotic_light = generate_chaotic_light(); input_distribution = encode_input(chaotic_light); output_distribution = photonic_crossbar(input_distribution); sample_output(output_distribution);
```

**Watch Out For:**

- Ensure the chaotic light source is stable and properly calibrated.
- Be aware of the limitations of electronic noise in the readout circuit.
- Understand the implications of using non-volatile phase change materials.

## Use This When

- You need to perform high-speed probabilistic computations.
- Uncertainty quantification is critical for your application.
- You are working with incomplete or noisy data.

## Don't Use When

- Deterministic computations are sufficient for your needs.
- You require a traditional electronic computing architecture.
- Low latency is more critical than handling uncertainty.

## Key Concepts

chaotic light, Bayesian inference, photonic crossbar, probabilistic neural networks, uncertainty quantification, in-memory computing, Monte Carlo methods

## Connects To

- Bayesian Neural Networks
- Monte Carlo methods
- Optical computing architectures
- In-memory computing techniques

## Prerequisites

- Basic understanding of photonics and optical systems.
- Familiarity with Bayesian inference and probabilistic models.
- Knowledge of neural network architectures.

## Limitations

- Complexity of integrating optical components.
- Potential electronic noise affecting output.
- Dependence on the stability of chaotic light generation.

## Open Questions

- How can this approach be scaled for larger datasets?
- What are the implications of using different chaotic light sources?

## Abstract

Optical computers are fundamentally different from traditional electronic computers. In essence, they use photons (light) rather than electrons to process and transmit information. This shift in medium leads to several critical distinctions in how components operate and interact. Recall that at the heart of traditional computers is the transistor, a semiconductor device that controls the flow of electrons to perform logical operations and amplify signals. In contrast, optical computers leverage optical transistors (or similar photonic components) that control and manipulate light. Unlike electronic transistors, which rely on voltage or current, optical transistors operate through phenomena such as nonlinear optical effects, where one light beam can modulate another. This enables optical components to switch signals at speeds closer to the speed of light, significantly faster than the electron mobility in silicon
