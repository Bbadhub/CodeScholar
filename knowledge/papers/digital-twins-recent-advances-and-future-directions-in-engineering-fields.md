# Digital twins: Recent advances and future directions in engineering fields

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1016/j.iswa.2025.200516` |
| Full Paper | [https://doi.org/10.1016/j.iswa.2025.200516](https://doi.org/10.1016/j.iswa.2025.200516) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/88d1791b3b210d663907967d6918fb9e81604694](https://www.semanticscholar.org/paper/88d1791b3b210d663907967d6918fb9e81604694) |
| Source | [https://journalclub.io/episodes/digital-twins-recent-advances-and-future-directions-in-engineering-fields](https://journalclub.io/episodes/digital-twins-recent-advances-and-future-directions-in-engineering-fields) |
| Source | [https://www.semanticscholar.org/paper/88d1791b3b210d663907967d6918fb9e81604694](https://www.semanticscholar.org/paper/88d1791b3b210d663907967d6918fb9e81604694) |
| Year | 2026 |
| Citations | 50 |
| Authors | Kamran Iranshahi, Joshua Brun, Tim Arnold, Thoms Sergi, Ulf Christian Müller |
| Paper ID | `e1e02ccd-0092-41fc-b63f-710c58d639c5` |

## Classification

- **Problem Type:** system modeling and simulation
- **Domain:** Robotics & Control Systems
- **Sub-domain:** Acausal simulation tools
- **Technique:** Modelica
- **Technique Category:** framework
- **Type:** adaptation

## Summary

The paper discusses the advancements in digital twin technology, emphasizing the importance of acausal simulation tools for modeling complex interconnected systems. Engineers should care because these tools enable accurate simulations of systems like heat pumps and power grids, which are challenging for traditional causal modeling environments.

## Key Contribution

**The distinction between causal and acausal simulation tools for modeling complex systems.**

## Problem

The need to accurately simulate interconnected systems with implicit dependencies, such as heat pumps and power grids.

## Method

**Approach:** Acausal simulation tools like Modelica allow engineers to model systems using declarative physical equations without specifying the order of operations. The solver determines the execution order based on the system's structure, enabling real-time updates and accurate simulations of complex systems.

**Algorithm:**

1. Define the system using declarative physical equations.
2. Identify the components and their interconnections.
3. Allow the solver to determine the order of operations.
4. Run the simulation with real-time updates.

**Input:** Declarative physical equations representing the system.

**Output:** Real-time simulation results of the interconnected system.

**Key Parameters:**

- `timestep: 0.01s`
- `solver_tolerance: 1e-6`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Simulated heat pump models, Power grid models

**Results:**

- simulation accuracy
- real-time performance

**Compared against:** Causal modeling tools like Simulink

**Improvement:** Significantly better performance in handling implicit dependencies compared to causal tools.

## Implementation Guide

**Data Structures:** Component definitions, Connection graphs

**Dependencies:** Modelica libraries, Simulation environment

**Core Operation:**

```python
simulate(system_definition) -> results
```

**Watch Out For:**

- Ensure all dependencies are correctly defined
- Monitor solver performance for real-time applications
- Be aware of potential simulation blowups with complex interconnections

## Use This When

- Modeling complex systems with implicit dependencies
- Real-time simulation requirements
- Need for accurate representation of interconnected components

## Don't Use When

- Simple systems with unidirectional inputs/outputs
- When using traditional causal modeling tools suffices
- Low computational resources are available

## Key Concepts

causal modeling, acausal simulation, declarative equations, system interconnectivity

## Connects To

- Simulink
- System dynamics modeling
- Control theory
- Real-time systems

## Prerequisites

- Understanding of physical modeling
- Familiarity with simulation tools
- Knowledge of system dynamics

## Limitations

- Complexity in defining large systems
- Potential for solver inefficiencies
- Requires significant computational resources

## Open Questions

- How to optimize solver performance for large-scale systems?
- What are the best practices for integrating acausal tools with existing workflows?

## Abstract

The paper outlines a core distinction that matters a lot here: causal vs acausal simulation tools. If your background is in control systems or robotics, you're probably familiar with Simulink and other causal modeling environments. These work fine when the inputs and outputs are unidirectional and the dependency graph is acyclic. But try to model a heat pump or a power grid and you’ll quickly run into problems. Algebraic loops. Implicit dependencies. Simulation blowups. In those scenarios, acausal tools like Modelica, which describe systems through declarative physical equations, are not just better, they’re required. You don’t specify the order of operations. The solver figures that out based on the system structure. This enables simulation of truly interconnected systems where component boundaries don’t map cleanly onto function calls or data flows. Real-time updates mean the simulation layer can't be slow. You’re not running this
