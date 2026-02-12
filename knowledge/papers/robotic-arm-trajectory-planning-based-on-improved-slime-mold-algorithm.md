# Robotic Arm Trajectory Planning Based on Improved Slime Mold Algorithm

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3390/machines13020079` |
| Full Paper | [https://doi.org/10.3390/machines13020079](https://doi.org/10.3390/machines13020079) |
| Source | [https://journalclub.io/episodes/robotic-arm-trajectory-planning-based-on-improved-slime-mold-algorithm](https://journalclub.io/episodes/robotic-arm-trajectory-planning-based-on-improved-slime-mold-algorithm) |
| Year | 2026 |
| Citations | 0 |
| Authors |  |
| Paper ID | `611bdb1e-e7bd-4b4f-be6d-03ce19813bd0` |

## Classification

- **Problem Type:** trajectory planning
- **Domain:** Robotics & Control Systems
- **Sub-domain:** Robotic arm trajectory optimization
- **Technique:** Improved Slime Mould Algorithm (ISMA)
- **Technique Category:** optimization_algorithm
- **Type:** novel

## Summary

The paper presents an improved Slime Mould Algorithm (ISMA) for robotic arm trajectory planning, addressing issues of vibration and wear during gripping operations. Engineers should care because this method optimizes movement time and reduces joint impacts, enhancing the longevity and efficiency of robotic arms in industrial applications.

## Key Contribution

**Introduction of an improved Slime Mould Algorithm for optimizing robotic arm trajectory planning with enhanced convergence and reduced impact forces.**

## Problem

The need to efficiently plan the motion trajectory of robotic arms in complex environments to minimize vibration and wear during operations.

## Method

**Approach:** The method constructs interpolation curves using seven non-uniform B-spline functions while optimizing time and impact force as objectives. The ISMA incorporates Bernoulli chaotic mapping for population diversity, adaptive feedback factors, and an improved artificial bee colony search strategy to enhance convergence.

**Algorithm:**

1. Initialize population using Bernoulli chaotic mapping.
2. Evaluate fitness of each individual in the population.
3. Update positions based on proximity to food and feedback factors.
4. Apply crossover operator to enhance diversity.
5. Use artificial bee colony strategy to guide search towards global optimum.
6. Optimize trajectory using B-spline interpolation.
7. Repeat until convergence criteria are met.

**Input:** Joint position and time series data for the robotic arm.

**Output:** Optimized trajectory for the robotic arm minimizing time and impact forces.

**Key Parameters:**

- `Kt (time coefficient): 0.4`
- `Kj (impact coefficient): 0.6`
- `Kp (penalty coefficient): 0.5`
- `Maximum iterations: 5000`
- `Adjustment factor k: 4`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Simulation data and real-machine experimental data

**Results:**

- Movement time reduction
- Joint impact minimization
- Vibration reduction

**Compared against:** Standard Slime Mould Algorithm (SMA), Butterfly Optimization Algorithm (BOA), Gray Wolf Algorithm (GWO), Sparrow Search Algorithm (SSA)

**Improvement:** Significant reduction in movement time and joint impacts compared to baseline algorithms.

## Implementation Guide

**Data Structures:** Array for joint positions, Matrix for B-spline control points

**Dependencies:** NumPy, SciPy, Matplotlib

**Core Operation:**

```python
initialize_population(); while not converged: evaluate_fitness(); update_positions(); apply_crossover(); optimize_trajectory();
```

**Watch Out For:**

- Ensure proper initialization of the population to avoid local optima.
- Carefully tune the feedback factor to balance exploration and exploitation.
- Monitor convergence criteria to prevent premature stopping.

## Use This When

- You need to optimize robotic arm movements in industrial applications.
- Minimizing vibration and wear during robotic operations is critical.
- You require a method that adapts to complex environments for trajectory planning.

## Don't Use When

- The robotic arm operates in a simple, predictable environment.
- Real-time trajectory adjustments are necessary.
- Computational resources are extremely limited.

## Key Concepts

Slime Mould Algorithm, B-spline interpolation, trajectory optimization, chaotic mapping, adaptive feedback, crossover operator

## Connects To

- Particle Swarm Optimization
- Cuckoo Search
- Artificial Bee Colony Algorithm

## Prerequisites

- Understanding of optimization algorithms
- Familiarity with B-spline curves
- Knowledge of robotic arm kinematics

## Limitations

- Performance may degrade in highly dynamic environments.
- Sensitivity to parameter tuning can affect results.
- Requires sufficient computational resources for large populations.

## Open Questions

- How can the algorithm be adapted for real-time trajectory adjustments?
- What are the effects of varying environmental conditions on optimization performance?

## Abstract

Use of the Slime Mold Algorithm (SMA) has exploded. It’s now used in scheduling and energy systems, in image processing and heavy machinery. You’ll see SMA references in papers on everything from network optimization to route optimization. And today we’re looking at a new paper that follows this trend. This time, the authors are applying the slime mold algorithm to robotic arm trajectory planning.
