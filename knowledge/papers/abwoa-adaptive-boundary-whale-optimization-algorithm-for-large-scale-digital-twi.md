# ABWOA: adaptive boundary whale optimization algorithm for large-scale digital twin network construction

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1186/s13677-024-00667-z` |
| Full Paper | [https://doi.org/10.1186/s13677-024-00667-z](https://doi.org/10.1186/s13677-024-00667-z) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/70ddf0966d2b9a283cd1337ff8b345c29e342574](https://www.semanticscholar.org/paper/70ddf0966d2b9a283cd1337ff8b345c29e342574) |
| Source | [https://journalclub.io/episodes/abwoa-adaptive-boundary-whale-optimization-algorithm-for-large-scale-digital-twin-network-construction](https://journalclub.io/episodes/abwoa-adaptive-boundary-whale-optimization-algorithm-for-large-scale-digital-twin-network-construction) |
| Source | [https://www.semanticscholar.org/paper/70ddf0966d2b9a283cd1337ff8b345c29e342574](https://www.semanticscholar.org/paper/70ddf0966d2b9a283cd1337ff8b345c29e342574) |
| Year | 2026 |
| Citations | 2 |
| Authors | Hao Feng, Kun Cao, Gan Huang, Hao Liu |
| Paper ID | `93afb47e-02a8-4e02-a608-abb700937535` |

## Classification

- **Problem Type:** multi-dimensional bin packing problem
- **Domain:** Networking & Distributed Systems
- **Sub-domain:** Digital Twin Networks
- **Technique:** Adaptive Boundary Whale Optimization Algorithm (ABWOA)
- **Technique Category:** optimization_algorithm
- **Type:** novel

## Summary

The paper presents the Adaptive Boundary Whale Optimization Algorithm (ABWOA) for efficiently constructing large-scale Digital Twin Networks (DTN). Engineers should care because it provides a novel approach to optimize the mapping of physical networks onto digital infrastructures, improving operational efficiency and reducing costs.

## Key Contribution

**Introduction of the Adaptive Boundary Whale Optimization Algorithm (ABWOA) for digital twin network construction, enhancing solution efficiency and quality.**

## Problem

The challenge of efficiently mapping physical network entities onto a distributed digital twin network infrastructure to minimize operational costs and enhance performance.

## Method

**Approach:** ABWOA enhances the traditional Whale Optimization Algorithm by dynamically adjusting search boundaries during the optimization process. This allows for improved convergence speed and solution quality in high-dimensional problems.

**Algorithm:**

1. Initialize a population of potential solutions (construction schemes).
2. Evaluate the fitness of each solution based on the number of DTNI nodes used.
3. Update positions of solutions using the shrinking encircling mechanism, spiral updating mechanism, and prey exploration mechanism.
4. Apply the Augmented Lagrangian Method for constraint handling to ensure valid solutions.
5. Dynamically adjust search boundaries based on current optimal solutions.
6. Repeat until convergence criteria are met.

**Input:** Data representing the physical network, including nodes, links, and their resource requirements (CPU, memory, bandwidth).

**Output:** An optimized mapping of physical network entities to DTNI nodes, minimizing the number of servers used.

**Key Parameters:**

- `population_size: 100`
- `max_iterations: 1000`
- `penalty_coefficient: 1.0`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Various network scales for digital twin network construction

**Results:**

- solution quality, convergence speed, time cost

**Compared against:** Genetic Algorithm, Particle Swarm Optimization, Artificial Bee Colony, Differential Evolution Algorithm, Moth Search Algorithm, Original Whale Optimization Algorithm

**Improvement:** ABWOA outperformed other algorithms in terms of solution quality and convergence speed.

## Implementation Guide

**Data Structures:** Graph representation for physical network and DTNI, Matrix for population of solutions

**Dependencies:** NumPy for numerical operations, SciPy for optimization routines

**Core Operation:**

```python
for each solution in population: evaluate_fitness(solution); update_positions(); apply_constraints();
```

**Watch Out For:**

- Ensure valid solutions to avoid penalties affecting performance.
- Monitor convergence to prevent premature stopping.
- Adjust parameters based on specific network characteristics.

## Use This When

- You need to optimize the mapping of physical networks to digital infrastructures.
- Working on large-scale distributed systems requiring efficient resource allocation.
- You are facing high-dimensional optimization problems in network construction.

## Don't Use When

- The problem size is small and can be solved with simpler algorithms.
- Real-time constraints are critical and require faster heuristics.
- The problem does not involve resource constraints.

## Key Concepts

Digital Twin Network, Whale Optimization Algorithm, Multi-dimensional Bin Packing, Augmented Lagrangian Method

## Connects To

- Genetic Algorithms
- Particle Swarm Optimization
- Differential Evolution
- Augmented Lagrangian Method

## Prerequisites

- Understanding of optimization algorithms
- Familiarity with digital twin technology
- Knowledge of resource allocation problems

## Limitations

- May struggle with extremely high-dimensional problems beyond certain thresholds.
- Performance may vary based on the specific characteristics of the network being modeled.
- Requires careful tuning of parameters for optimal performance.

## Open Questions

- How can ABWOA be adapted for real-time optimization in dynamic networks?
- What are the impacts of varying network topologies on the performance of ABWOA?

## Abstract

What do bees, ants, moths, bats, fish, birds and whales have in common? Give up? They all have optimization algorithms named in their honor. And today’s article is focusing on a new variant of that last one: whale optimization. In this paper it’s being used to solve a mapping problem for something called a Digital Twin Network (DTN). But the authors didn’t just solve that problem the one way, no. They actually solved it seven different ways, with seven algorithms, and then benchmarked them against each other. That gives us the opportunity to spend today’s episode taking a stroll through algorithm land. We’re going to ground ourselves in the problem-space very briefly, then spend the rest of the time learning about seven different algorithms. How they work, their strengths and weaknesses, and which one ended up being the best fit for the DTN problem. Let’s jump into it
