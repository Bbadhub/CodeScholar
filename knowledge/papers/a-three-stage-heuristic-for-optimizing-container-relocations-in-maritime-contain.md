# A Three-Stage Heuristic For Optimizing Container Relocations In Maritime Container Terminals

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3846/transport.2024.21668` |
| Full Paper | [https://doi.org/10.3846/transport.2024.21668](https://doi.org/10.3846/transport.2024.21668) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/ede647b21c3cedf183059f877e0cb7db68e752f6](https://www.semanticscholar.org/paper/ede647b21c3cedf183059f877e0cb7db68e752f6) |
| Source | [https://journalclub.io/episodes/a-three-stage-heuristic-for-optimizing-container-relocations-in-maritime-container-terminals](https://journalclub.io/episodes/a-three-stage-heuristic-for-optimizing-container-relocations-in-maritime-container-terminals) |
| Source | [https://www.semanticscholar.org/paper/ede647b21c3cedf183059f877e0cb7db68e752f6](https://www.semanticscholar.org/paper/ede647b21c3cedf183059f877e0cb7db68e752f6) |
| Year | 2026 |
| Citations | 0 |
| Authors | Qianwen Zhu, Bo Jin |
| Paper ID | `cc93ae08-b804-490c-bbeb-273dbf755a41` |

## Classification

- **Problem Type:** container relocation optimization
- **Domain:** Optimization & Operations Research
- **Sub-domain:** Logistics optimization
- **Technique:** Three-Stage Heuristic (3SH)
- **Technique Category:** optimization_algorithm
- **Type:** novel

## Summary

The paper presents a Three-Stage Heuristic (3SH) for optimizing container relocations in maritime container terminals, addressing the NP-hard Container Relocation Problem (CRP). Engineers should care because this approach significantly reduces the number of relocation operations, leading to cost savings in terminal operations.

## Key Contribution

**The introduction of a three-stage heuristic that optimizes the relocation of multiple blocking containers simultaneously, outperforming existing methods.**

## Problem

The need to minimize relocation operations in maritime container terminals to improve efficiency and reduce operational costs.

## Method

**Approach:** The 3SH method operates in three stages: first, it assigns blocking containers to stacks without causing additional relocations; second, it completes the assignment for remaining containers that will cause relocations; and third, it adjusts the assignments to further optimize the arrangement.

**Algorithm:**

1. 1. Identify blocking containers above the target container.
2. 2. In the first stage, assign containers to stacks without causing additional relocations.
3. 3. In the second stage, assign remaining containers using an enhanced Virtual Relocation Index (VRI).
4. 4. In the last stage, adjust assignments to optimize the relocation of blocking containers.

**Input:** Data on container stacks, their heights, and the priority of containers for retrieval.

**Output:** An optimized arrangement of containers in stacks that minimizes the number of relocations.

**Key Parameters:**

- `S: number of stacks`
- `H: maximum height limit`
- `N: number of containers`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Instances from Wu & Ting (2010), Instances from Caserta et al. (2011), Instances from Zhu et al. (2012)

**Results:**

- Average number of relocations
- Average computation time in milliseconds

**Compared against:** Min-Max heuristic by Caserta et al. (2012), PR4 heuristic by Zhu et al. (2012), Chain heuristic by Jovanovic & Voß (2014), VRH by Ting & Wu (2017)

**Improvement:** 3SH outperformed existing heuristics, winning 35 out of 48 groups in tests.

## Implementation Guide

**Data Structures:** Stacks to represent container storage, Priority queues for managing container retrieval order

**Dependencies:** Java for implementation of the heuristic, Libraries for numerical computations (if needed)

**Core Operation:**

```python
for each blocking container c: assign destination stack based on VRI; adjust assignments in last stage.
```

**Watch Out For:**

- Ensure LIFO constraints are respected during relocations.
- Monitor the impact of each relocation on future retrievals.

## Use This When

- Optimizing container retrieval in maritime terminals with high container volumes.
- Reducing operational costs associated with container relocations.
- Improving efficiency in logistics and supply chain management.

## Don't Use When

- Dealing with small-scale instances where traditional heuristics perform adequately.
- When real-time decision-making is required and computational time is critical.

## Key Concepts

blocking containers, LIFO constraint, priority values, Virtual Relocation Index (VRI)

## Connects To

- Integer programming formulations for CRP
- Branch-and-bound algorithms for optimization
- Other heuristics like genetic algorithms and ant colony optimization

## Prerequisites

- Understanding of optimization problems
- Familiarity with heuristic algorithms
- Knowledge of logistics and container management systems

## Limitations

- Performance may degrade on small-scale instances.
- Complexity increases with the number of containers and stacks.

## Open Questions

- How can the heuristic be adapted for real-time decision-making?
- What are the implications of varying stack heights and container priorities?

## Abstract

Every stack is a LIFO queue (last-in-first-out), so there’s only one solution, right? Wrong. It’s more complicated than that. Here’s why. And this is what makes it NP-Hard: Each container that is in the way of the container you want to reach is called a “blocking” container. Every time you move a blocking container, you have to decide where to put it, and that decision has consequences for future retrievals. Not only does each stack have height limitations, but the placement of that container on another stack can either make future retrievals easier or harder depending on the sequence of container requests that come later. If you move a container to a stack where it blocks another container that will be needed soon, you’ve effectively created an additional retrieval problem for yourself.
