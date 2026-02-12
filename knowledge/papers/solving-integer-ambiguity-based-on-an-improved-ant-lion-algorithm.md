# Solving Integer Ambiguity Based on an Improved Ant Lion Algorithm

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3390/s25041212` |
| Full Paper | [https://doi.org/10.3390/s25041212](https://doi.org/10.3390/s25041212) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/3614f6ce6c8431b6c663bb4f10c2362efd0c8d7a](https://www.semanticscholar.org/paper/3614f6ce6c8431b6c663bb4f10c2362efd0c8d7a) |
| Source | [https://journalclub.io/episodes/solving-integer-ambiguity-based-on-an-improved-ant-lion-algorithm](https://journalclub.io/episodes/solving-integer-ambiguity-based-on-an-improved-ant-lion-algorithm) |
| Source | [https://www.semanticscholar.org/paper/3614f6ce6c8431b6c663bb4f10c2362efd0c8d7a](https://www.semanticscholar.org/paper/3614f6ce6c8431b6c663bb4f10c2362efd0c8d7a) |
| Year | 2026 |
| Citations | 0 |
| Authors | Wuzheng Guo, Yuanfa Ji, Xiyan Sun, Xizi Jia |
| Paper ID | `22884074-2962-4599-8bf2-9379bc68e36e` |

## Classification

- **Problem Type:** integer ambiguity resolution
- **Domain:** Machine Learning & AI
- **Sub-domain:** Optimization Algorithms
- **Technique:** Simulated Annealing Ant Lion Optimizer (SAALO)
- **Technique Category:** optimization_algorithm
- **Type:** novel

## Summary

The paper presents an enhanced Simulated Annealing Ant Lion Optimizer (SAALO) designed to efficiently resolve integer ambiguities in GNSS applications, achieving a success rate exceeding 98% in high-dimensional scenarios. Engineers should care because this algorithm improves the speed and reliability of high-precision positioning systems.

## Key Contribution

**Introduction of the SAALO algorithm that significantly enhances the efficiency of integer ambiguity resolution in GNSS applications.**

## Problem

The challenge of resolving integer ambiguities in GNSS carrier phase observations to achieve high-precision positioning results.

## Method

**Approach:** The SAALO algorithm combines the Ant Lion Optimization strategy with simulated annealing to enhance the search for integer ambiguities. It optimizes the random wandering function of ants using a roulette selection method to improve convergence and escape local optima.

**Algorithm:**

1. Initialize ants and ant lions randomly in the solution space.
2. Calculate the trap size for each ant lion based on the current iteration.
3. Ants wander randomly within the trap of their chosen ant lion.
4. Update the position of ants based on their random wandering and the best ant lion.
5. Select the best ant lion as the elite solution.
6. Apply simulated annealing to determine if the new ant lion position should be accepted.

**Input:** Carrier phase observations from GNSS systems.

**Output:** Resolved integer ambiguities for high-precision positioning.

**Key Parameters:**

- `max_iterations: 1000`
- `population_size: 50`
- `initial_temperature: 100`
- `cooling_rate: 0.95`

**Complexity:** Not stated.

## Benchmarks

**Tested on:** 6-dimensional and 12-dimensional integer ambiguity scenarios, short- and medium-baseline scenarios using a single-frequency GPS system.

**Results:**

- solution success rate: >98%
- average solution time: 0.0496 s faster than LAMBDA, 0.01 s faster than M-LAMBDA

**Compared against:** Ant Lion Optimization Algorithm (ALO), LAMBDA algorithm, M-LAMBDA algorithm

**Improvement:** 5.2% higher success rate compared to LAMBDA algorithm.

## Implementation Guide

**Data Structures:** Arrays for storing positions of ants and ant lions, Matrices for covariance and transformation

**Dependencies:** NumPy for numerical computations, SciPy for optimization routines

**Core Operation:**

```python
Initialize ants and ant lions; while not converged: update positions based on traps; apply simulated annealing.
```

**Watch Out For:**

- Ensure proper initialization of parameters to avoid premature convergence.
- Monitor the cooling rate in simulated annealing to balance exploration and exploitation.
- Be cautious of the fitness function scaling to prevent bias in selection.

## Use This When

- You need to resolve integer ambiguities in GNSS applications.
- You require high-precision positioning with a success rate above 98%.
- You are dealing with high-dimensional optimization problems.

## Don't Use When

- The problem space is small and can be solved with simpler methods.
- Real-time processing is critical and cannot accommodate the algorithm's complexity.
- You need guaranteed optimal solutions without the risk of local optima.

## Key Concepts

integer ambiguity, GNSS, optimization, simulated annealing, Ant Lion Optimization, high-dimensional search, fitness function

## Connects To

- Genetic Algorithms
- Particle Swarm Optimization
- Ant Colony Optimization
- Simulated Annealing

## Prerequisites

- Understanding of optimization algorithms
- Familiarity with GNSS systems
- Knowledge of integer programming

## Limitations

- Computationally intensive for very high-dimensional problems
- Performance may degrade with poor parameter tuning
- Requires careful handling of local optima.

## Open Questions

- How can the algorithm be adapted for real-time applications?
- What are the effects of varying the cooling rate on performance?

## Abstract

On October 4th, 1957, the Soviet Union launched Sputnik: the first satellite ever put into orbit. This, to put it bluntly, scared the crap out of the Americans and propelled the U.S. into the space race. In the days and weeks after launch, the U.S. became obsessed with tracking Sputnik's movements. Where is it now? Ok, how about now? And now? In order to track it, they used Doppler shift measurements. Radio receivers on the ground would listen to Sputnik’s beeping signal, and analyze how its frequency changed as it moved. The resulting measurements allowed engineers to calculate its exact orbit and predict its future positions. The U.S. got quite good at this, and this led to a realization. If we can track a satellite in space with ground-based measurements, then the converse is also true. If we had multiple satellites in space at one time, then we could use them to track objects on Earth. Within four months
