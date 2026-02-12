# Trustworthy and reliable computing using untrusted and unreliable quantum hardware

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3389/fcomp.2024.1431788` |
| Full Paper | [https://doi.org/10.3389/fcomp.2024.1431788](https://doi.org/10.3389/fcomp.2024.1431788) |
| Source | [https://journalclub.io/episodes/trustworthy-and-reliable-computing-using-untrusted-and-unreliable-quantum-hardware](https://journalclub.io/episodes/trustworthy-and-reliable-computing-using-untrusted-and-unreliable-quantum-hardware) |
| Year | 2026 |
| Citations | 0 |
| Authors |  |
| Paper ID | `60e6836f-91f3-4426-b158-ea362cbde486` |

## Classification

- **Problem Type:** quantum computing security
- **Domain:** Quantum Computing
- **Sub-domain:** Quantum Security
- **Technique:** Intelligent Run-Adaptive Shot Distribution
- **Technique Category:** framework
- **Type:** novel

## Summary

The paper presents a method for achieving trustworthy and reliable quantum computing using untrusted and unreliable quantum hardware by modeling adversarial tampering and proposing an equitable distribution of quantum shots across different hardware options. Engineers should care because this approach can significantly improve the reliability of quantum computations, especially in critical applications where tampering could lead to sub-optimal solutions.

## Key Contribution

**Proposed an intelligent run-adaptive shot distribution heuristic to mitigate adversarial tampering in quantum computing.**

## Problem

The need for reliable quantum computing solutions in the presence of potentially tampered results from untrusted quantum hardware providers.

## Method

**Approach:** The method involves distributing quantum shots across multiple hardware options to mitigate the effects of adversarial tampering. An intelligent heuristic is used to adaptively allocate more shots to reliable hardware based on temporal variations in hardware quality.

**Algorithm:**

1. 1. Identify available quantum hardware options.
2. 2. Distribute total shots across these hardware options.
3. 3. Execute quantum programs on each hardware option.
4. 4. Collect results and analyze probability distributions.
5. 5. Adjust shot distribution based on observed hardware performance.
6. 6. Combine results to form a final probability distribution of solutions.

**Input:** Quantum programs and the number of total shots to be executed.

**Output:** Probability distribution of the solution space after combining results from different hardware.

**Key Parameters:**

- `total_shots: 1000`
- `tampering_coefficient: 0.1 to 0.5`

**Complexity:** Not stated.

## Benchmarks

**Tested on:** IBM's fake backends for quantum simulations

**Results:**

- Performance Metric (PM)
- Total Variational Distance (TVD)

**Compared against:** Single hardware execution without shot distribution

**Improvement:** Achieved up to ≈190X improvement for pure quantum workloads and ≈2.5X for hybrid-classical algorithms.

## Implementation Guide

**Data Structures:** Arrays for storing shot results, Data structures for probability distributions

**Dependencies:** IBM Qiskit

**Core Operation:**

```python
results = combine_results(distribute_shots(hardware_options, total_shots))
```

**Watch Out For:**

- Ensure accurate measurement of hardware performance to avoid misallocation of shots.
- Monitor temporal variations in hardware quality continuously.

## Use This When

- You need to run quantum algorithms on unreliable hardware.
- You are working with critical applications where tampering could lead to significant consequences.
- You want to improve the reliability of quantum computations in a mixed hardware environment.

## Don't Use When

- You have access to fully trusted and reliable quantum hardware.
- The application does not require high reliability in quantum results.

## Key Concepts

quantum hardware, adversarial tampering, shot distribution, quantum algorithms, QAOA, hybrid quantum-classical

## Connects To

- Quantum Approximate Optimization Algorithm (QAOA)
- Variational Quantum Eigensolver (VQE)
- Ensemble of Diverse Mappings (EDM)

## Prerequisites

- Basic understanding of quantum computing
- Familiarity with quantum algorithms
- Knowledge of cloud-based quantum services

## Limitations

- The method relies on the assumption that some hardware is trusted.
- Performance may vary significantly based on the quality of the available hardware.
- The approach may not be effective if all hardware options are untrusted.

## Open Questions

- How to optimally determine the split boundary for shot distribution?
- What metrics should be used to evaluate the effectiveness of the defense against tampering?

## Abstract

Right now, in 2024, writing programs for quantum computers feels like you’re writing code for IBM mainframes in the 1960s. Here’s what it's like: You write your code. You find a vendor with an available quantum computer that has a compiler compatible with your code. You send your code to that vendor in the hopes that they will compile and run your code sometime soon. You wait and you wait and you wait (for minutes or hours or days) You eventually get a readout back of the result of your program and/or your errors. The whole process is like stepping into a time machine!...And not in a good way.
