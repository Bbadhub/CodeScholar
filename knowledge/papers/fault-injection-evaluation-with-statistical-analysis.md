# Fault Injection Evaluation with Statistical Analysis

## Access

| Field | Value |
|-------|-------|
| DOI | `10.46586/tches.v2025.i4.215-253` |
| Full Paper | [https://doi.org/10.46586/tches.v2025.i4.215-253](https://doi.org/10.46586/tches.v2025.i4.215-253) |
| Source | [https://journalclub.io/episodes/fault-injection-evaluation-with-statistical-analysis](https://journalclub.io/episodes/fault-injection-evaluation-with-statistical-analysis) |
| Year | 2026 |
| Citations | 0 |
| Authors |  |
| Paper ID | `a891679e-e800-41c4-9b36-548f5784d6ca` |

## Classification

- **Problem Type:** fault injection evaluation
- **Domain:** Computer Security
- **Sub-domain:** Cryptographic Hardware Security
- **Technique:** FIESTA
- **Technique Category:** framework
- **Type:** novel

## Summary

The paper introduces FIESTA, an automated framework for evaluating the resistance of cryptographic hardware against fault injection attacks using a statistical approach. Engineers should care because FIESTA allows for the assessment of larger designs under realistic fault models, which is crucial for ensuring the security of hardware implementations in various applications.

## Key Contribution

**FIESTA is an open-source fault evaluation framework that employs a statistical approach to assess circuits within the general random fault model.**

## Problem

The need to verify the resistance of cryptographic hardware designs against fault injection attacks before fabrication.

## Method

**Approach:** FIESTA evaluates hardware circuits under the general random fault model by leveraging a non-exhaustive approach. It allows for the analysis of larger designs while maintaining a reasonable level of confidence in the results.

**Algorithm:**

1. 1. Define the circuit under test and its parameters.
2. 2. Specify the fault model and the probability distribution of faults.
3. 3. Generate a randomized subset of gates to be faulted based on the defined model.
4. 4. Simulate the circuit with the injected faults.
5. 5. Analyze the output to determine if the faults were effective.
6. 6. Report the success probability bounds based on the analysis.

**Input:** A circuit design represented in a suitable format (e.g., GDSII file) and a defined probability distribution for faults.

**Output:** Success probability bounds indicating the effectiveness of fault injection attacks on the circuit.

**Key Parameters:**

- `error_probability: α > 0`
- `fault_probability_distribution: user-defined based on the specific use case`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Various protected Advanced Encryption Standard (AES) cores

**Results:**

- success probability bounds: (µℓ, µu) = (14, 12)

**Compared against:** VERICA+, IronMask+

**Improvement:** FIESTA evaluates larger designs in less time compared to VERICA+ and IronMask+.

## Implementation Guide

**Data Structures:** Directed Acyclic Graph (DAG) for circuit representation, Sets for fault combinations

**Dependencies:** Python, GitHub repository for FIESTA

**Core Operation:**

```python
def evaluate_circuit(circuit, fault_model): inject_faults(circuit, fault_model); return analyze_output(circuit)
```

**Watch Out For:**

- Ensure the probability distribution for faults is accurately defined.
- Be aware of the error probability α when interpreting results.
- Consider the physical layout of the circuit when analyzing fault effects.

## Use This When

- Evaluating the security of large cryptographic hardware designs against fault injection attacks.
- Needing a framework that supports various adversary models for customized resistance analysis.
- Conducting pre-fabrication security assessments of hardware implementations.

## Don't Use When

- Working with very small circuits where exhaustive verification is feasible.
- When precise fault injection techniques are required that FIESTA does not support.
- If the application does not involve cryptographic hardware.

## Key Concepts

fault injection, cryptographic hardware, random fault model, statistical analysis, circuit evaluation, adversary models

## Connects To

- VERICA+
- IronMask+
- Statistical Fault Analysis (SFA)
- Differential Fault Analysis (DFA)
- Fault Sensitivity Analysis (FSA)

## Prerequisites

- Understanding of fault injection techniques and their implications.
- Familiarity with cryptographic hardware design.
- Knowledge of statistical analysis methods.

## Limitations

- FIESTA introduces an error probability α, which may affect the confidence in results.
- Requires user-defined probability distributions, which can be complex.
- Not exhaustive in terms of inputs or fault combinations, which may lead to imprecise results.

## Open Questions

- How can FIESTA be adapted to incorporate more precise fault models?
- What additional adversary models could enhance the framework's applicability?

## Abstract

Imagine that you're working on a new chip. It’s not a general-purpose processor, it’s built for a specific purpose and use case: cryptography. It accelerates encryption, decryption, and key generation directly in hardware, instead of relying on software routines (which are slower). If you can get this right, the use cases abound: everything from securing mobile payments, to protecting cloud servers, to safeguarding embedded devices and medical equipment, to securing the Internet of Things.
