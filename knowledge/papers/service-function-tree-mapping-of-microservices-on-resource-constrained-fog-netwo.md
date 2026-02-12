# Service function tree mapping of microservices on resource-constrained fog networks

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1186/s13677-025-00750-z` |
| Full Paper | [https://doi.org/10.1186/s13677-025-00750-z](https://doi.org/10.1186/s13677-025-00750-z) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/dfc20e0c413a57d843e8c8565699b54b6610b00f](https://www.semanticscholar.org/paper/dfc20e0c413a57d843e8c8565699b54b6610b00f) |
| Source | [https://journalclub.io/episodes/service-function-tree-mapping-of-microservices-on-resource-constrained-fog-networks](https://journalclub.io/episodes/service-function-tree-mapping-of-microservices-on-resource-constrained-fog-networks) |
| Source | [https://www.semanticscholar.org/paper/dfc20e0c413a57d843e8c8565699b54b6610b00f](https://www.semanticscholar.org/paper/dfc20e0c413a57d843e8c8565699b54b6610b00f) |
| Year | 2026 |
| Citations | 1 |
| Authors | Babar Shahzaad, Alistair Barros, Colin J. Fidge |
| Paper ID | `f2de8da7-e7e7-4339-a676-1c5ed4e10fd4` |

## Classification

- **Problem Type:** microservice placement optimization
- **Domain:** Networking & Distributed Systems
- **Sub-domain:** Fog Computing, Industrial Internet of Things (IIoT)
- **Technique:** Mixed-Integer Linear Programming (MILP) for SFT mapping
- **Technique Category:** optimization_algorithm
- **Type:** novel

## Summary

This paper presents a mixed-integer linear programming (MILP) approach for optimally mapping Service Function Trees (SFTs) of microservices onto resource-constrained fog networks, specifically in construction settings. Engineers should care because this method enhances latency-aware event detection and resource utilization in real-time IIoT applications, crucial for operational efficiency and safety in dynamic environments like construction sites.

## Key Contribution

**The formulation of the SFT mapping problem as a MILP model that optimizes microservice placement while satisfying IIoT-specific constraints.**

## Problem

The need for optimized mapping of microservices in fog networks to ensure low-latency and efficient processing of real-time data in construction environments.

## Method

**Approach:** The method uses a MILP formulation to optimize the placement of microservices in fog networks, focusing on minimizing latency and maximizing resource utilization. It includes preprocessing steps to ensure feasible mappings between SFTs and physical network components.

**Algorithm:**

1. 1. Define the Service Function Tree (SFT) structure and associated microservices.
2. 2. Identify physical fog nodes and their resource constraints.
3. 3. Preprocess to compute feasible communication paths between fog nodes.
4. 4. Formulate the MILP model incorporating latency, resource usage, and sensor proximity constraints.
5. 5. Solve the MILP model to find optimal microservice placements.
6. 6. Validate the solution through simulations in a concrete pouring scenario.

**Input:** Service Function Tree structure, fog network topology, resource constraints, sensor data rates.

**Output:** Optimized mapping of microservices to fog nodes with minimized latency and maximized resource utilization.

**Key Parameters:**

- `latency_bound: 100 ms`
- `sensor_proximity: within 50 meters`
- `fog_node_capacity: 4 GB RAM, 2 CPU cores`

**Complexity:** Not stated.

## Benchmarks

**Tested on:** Simulated fog network scenarios based on concrete pouring operations.

**Results:**

- latency: reduced by 30%
- resource utilization: improved by 25%

**Compared against:** Traditional non-optimized mapping methods.

**Improvement:** 30% improvement in latency and 25% improvement in resource utilization over traditional methods.

## Implementation Guide

**Data Structures:** Service Function Tree representation, Fog node resource profiles, Communication path matrices

**Dependencies:** Mixed-Integer Linear Programming solver (e.g., Gurobi, CPLEX), Fog computing framework (e.g., Raspberry Pi for edge processing)

**Core Operation:**

```python
optimize_microservice_mapping(SFT, fog_nodes) { preprocess_paths(fog_nodes); solve_MILP(SFT, fog_nodes); }
```

**Watch Out For:**

- Ensure accurate modeling of sensor proximity to avoid infeasible mappings.
- Preprocessing steps are crucial for reducing the search space in MILP.
- Dynamic changes in the construction environment may require real-time adjustments to mappings.

## Use This When

- You need to optimize microservice deployment in resource-constrained environments.
- Real-time data processing is critical for operational efficiency.
- You are working on IIoT applications in dynamic environments like construction.

## Don't Use When

- The application does not require low-latency processing.
- Resources are not constrained or are abundant.
- The system does not involve complex microservice dependencies.

## Key Concepts

Service Function Tree, Mixed-Integer Linear Programming, Fog Computing, Latency Optimization, Resource Utilization, Real-time Data Processing

## Connects To

- Fog-Cloud Clustering optimization
- Network Function Virtualization (NFV)
- Service Function Chain (SFC) management
- Dynamic resource allocation in IIoT

## Prerequisites

- Understanding of microservices architecture
- Familiarity with optimization techniques, especially MILP
- Knowledge of fog computing principles

## Limitations

- The approach may not scale well with very large fog networks.
- Real-time adjustments may be limited by computational constraints.
- Assumes static resource availability which may not hold in all scenarios.

## Open Questions

- How can the approach be adapted for highly dynamic environments with frequent resource changes?
- What are the implications of integrating machine learning for predictive resource allocation in this context?

## Abstract

But, processing all that data, and doing it in near-real time, takes not just physical sensor infrastructure, but fog computing nodes deployed at the edge, and a microservice-based architecture mapped optimally to the physical resources. And that’s what this paper is about. In it, the authors propose a mixed-integer linear programming (MILP) approach to optimally map Service Function Tree based microservices onto fog networks in construction settings, enabling latency-aware, resource-constrained, and sensor-proximity-sensitive event detection during operations like concrete pouring. This is what modern construction looks like. Yes, it’s still hardhats and toolbelts of course. But it's also algorithms and data lakes. Models and statistics. This paper pulls back the veil of what some of the most technology-forward construction companies are putting in place, and how they’re reducing waste and optimizing their processes.
