# The Fog Node Location Problem

## Access

| Field | Value |
|-------|-------|
| DOI | `10.19153/cleiej.27.3.2` |
| Full Paper | [https://doi.org/10.19153/cleiej.27.3.2](https://doi.org/10.19153/cleiej.27.3.2) |
| Source | [https://journalclub.io/episodes/the-fog-node-location-problem](https://journalclub.io/episodes/the-fog-node-location-problem) |
| Year | 2026 |
| Citations | 0 |
| Authors |  |
| Paper ID | `aee91ef4-c5fc-4cfe-a806-cfd5cce7839a` |

## Classification

- **Problem Type:** facility location optimization
- **Domain:** Networking & Distributed Systems
- **Sub-domain:** Fog computing
- **Technique:** UAV Fog Node Location algorithm
- **Technique Category:** optimization_algorithm
- **Type:** novel

## Summary

The paper addresses the Fog Node Location Problem, focusing on optimizing the placement of fog nodes to meet variable end-user demands while minimizing costs, energy consumption, and latency. Engineers should care because this research provides practical algorithms and models that can enhance the performance of IoT systems by strategically deploying fog computing resources.

## Key Contribution

**Introduction of multi-objective mixed-integer linear programming (MILP) models and heuristic algorithms for optimizing fog node locations and capacities.**

## Problem

The need for efficient placement of fog nodes to reduce latency and improve service for IoT devices with strict latency requirements.

## Method

**Approach:** The method involves formulating the fog node location problem as a multi-objective optimization problem using MILP. It optimizes the placement of both fixed and mobile fog nodes (UAVs) based on user demands and operational constraints.

**Algorithm:**

1. Define candidate locations for fog nodes.
2. Model workload demands at each location over time.
3. Formulate the optimization problem using MILP with objectives for workload maximization and cost minimization.
4. Implement the UAV Fog Node Location algorithm to identify underutilized fixed nodes for replacement by UAVs.
5. Simulate the deployment and evaluate performance metrics.

**Input:** Candidate locations for fog nodes, workload demands at each location over time, cost and capacity of fixed servers and UAVs.

**Output:** Optimal locations for fog nodes, number of servers at each location, UAV deployment plan, and workload served.

**Key Parameters:**

- `CS: cost of a single fixed server`
- `CU: cost of a UAV carrying a mobile server`
- `KS: capacity of a single fixed server`
- `KU: capacity of a UAV mobile server`
- `C: available budget`
- `E: total battery capacity of a UAV`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Telecom Italia data, OpenCellId project data

**Results:**

- acceptance ratio of requests
- energy consumption of end-user devices
- number of requests processed

**Compared against:** Previous facility location algorithms

**Improvement:** Up to 40% reduction in energy consumption compared to scenarios with a single fog node.

## Implementation Guide

**Data Structures:** Graphs for candidate locations, Arrays for workload demands, Matrices for server capacities

**Dependencies:** Gurobi Optimizer, Python

**Core Operation:**

```python
for each candidate location l: optimize workload served wlt using MILP model; deploy UAVs where fixed servers are underutilized.
```

**Watch Out For:**

- Ensure accurate modeling of energy consumption for UAVs.
- Consider the trade-off between cost and performance when deploying UAVs.
- Monitor the operational time of UAVs to avoid battery depletion.

## Use This When

- Designing IoT systems with strict latency requirements.
- Deploying fog computing resources in urban environments.
- Optimizing resource allocation in smart cities.

## Don't Use When

- Latency requirements are not critical.
- Fixed infrastructure is sufficient without mobility.
- Cost constraints are not a concern.

## Key Concepts

fog computing, UAV deployment, multi-objective optimization, mixed-integer linear programming

## Connects To

- Facility location problems
- Energy-efficient computing
- UAV trajectory optimization

## Prerequisites

- Understanding of optimization techniques
- Familiarity with linear programming
- Knowledge of fog computing principles

## Limitations

- Scalability issues with large problem instances.
- Assumes fixed costs for UAVs and servers may not reflect real-world variability.
- Limited operational time for UAVs due to battery constraints.

## Open Questions

- How to further improve the scalability of the proposed algorithms?
- What are the implications of varying UAV costs on deployment strategies?

## Abstract

If you find yourself working with IoT devices, you’ll probably spend a lot of time thinking about light. No matter how elegantly you program your device, and no matter how cleanly you construct the backend, the interactions between your device and its server will only ever be as quick and responsive as light allows. Light travels at around 300,000 kilometers per second. That's around 186 miles per millisecond. So for tasks that require a round-trip to the server, the ultimate latency and lagginess of your device has nothing to do with your programming abilities; it has to do with how physically far the IoT device is from the nearest data center. Let's say you're building a device with strict latency requirements, and you want a roundtrip baseline of 6 milliseconds. If that’s the case, your server can’t be more than around 560 miles away from the device. Any further and light won’t have enough time to get to the server and come back.
