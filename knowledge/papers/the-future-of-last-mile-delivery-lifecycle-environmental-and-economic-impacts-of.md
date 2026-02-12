# The Future of Last-Mile Delivery: Lifecycle Environmental and Economic Impacts of Drone-Truck Parallel Systems

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3390/drones9010054` |
| Full Paper | [https://doi.org/10.3390/drones9010054](https://doi.org/10.3390/drones9010054) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/a23c6b00c745068889512b91fdaee4f1831fbc38](https://www.semanticscholar.org/paper/a23c6b00c745068889512b91fdaee4f1831fbc38) |
| Source | [https://journalclub.io/episodes/the-future-of-last-mile-delivery-lifecycle-environmental-and-economic-impacts-of-drone-truck-parallel-systems](https://journalclub.io/episodes/the-future-of-last-mile-delivery-lifecycle-environmental-and-economic-impacts-of-drone-truck-parallel-systems) |
| Source | [https://www.semanticscholar.org/paper/a23c6b00c745068889512b91fdaee4f1831fbc38](https://www.semanticscholar.org/paper/a23c6b00c745068889512b91fdaee4f1831fbc38) |
| Year | 2026 |
| Citations | 14 |
| Authors | Danwen Bao, Yu Yan, Yuhan Li, Jiajun Chu |
| Paper ID | `2f599bb6-9265-4364-a267-88a4acd41f49` |

## Classification

- **Problem Type:** multi-objective optimization
- **Domain:** Logistics & Transportation
- **Sub-domain:** Drone delivery systems
- **Technique:** Parallel Drone Scheduling Traveling Salesman Problem (PDSTSP)
- **Technique Category:** optimization_algorithm
- **Type:** novel

## Summary

This paper investigates the Parallel Drone Scheduling Traveling Salesman Problem (PDSTSP) to evaluate the environmental and economic sustainability of a collaborative drone-truck delivery system. It provides a mathematical model to optimize delivery operations, showing significant reductions in carbon emissions and costs compared to traditional delivery methods.

## Key Contribution

**Development of a mathematical model for optimizing drone-truck delivery operations that integrates environmental and economic assessments.**

## Problem

The need for efficient last-mile delivery solutions that minimize environmental impact and operational costs.

## Method

**Approach:** The method optimizes the delivery routes for a fleet of drones and trucks operating in parallel. It minimizes the total completion time while considering environmental impacts through Life Cycle Assessment (LCA) and economic performance through Life Cycle Cost Analysis (LCCA).

**Algorithm:**

1. Define the set of nodes representing the depot and customer locations.
2. Categorize customers into those served by trucks and those that can be served by either drones or trucks.
3. Formulate the problem as a Mixed-Integer Linear Programming (MILP) model.
4. Set constraints for load capacities, travel distances, and operational parameters.
5. Optimize the delivery routes to minimize total completion time.
6. Perform sensitivity analysis on factors like delivery density and traffic conditions.

**Input:** Set of customer locations, demand weights, vehicle capacities, and operational parameters.

**Output:** Optimized delivery routes for drones and trucks, total completion time, and environmental/economic impact metrics.

**Key Parameters:**

- `drone_capacity: 2.5 kg`
- `truck_capacity: 1300 kg`
- `annual_operation_days: 300`
- `daily_operation_hours: 8`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Simulated delivery scenarios with varying customer densities and traffic conditions.

**Results:**

- carbon emissions reduction: ~20%
- cost reduction: 20-30% compared to fuel truck fleet

**Compared against:** Traditional truck-only delivery systems

**Improvement:** 20% reduction in carbon emissions and 20-30% cost reduction compared to fuel truck fleet.

## Implementation Guide

**Data Structures:** Graph representation of delivery nodes, Binary variables for route selection

**Dependencies:** Optimization libraries (e.g., PuLP, Gurobi) for MILP

**Core Operation:**

```python
minimize total_completion_time; optimize routes for trucks and drones based on customer demands;
```

**Watch Out For:**

- Ensure accurate modeling of drone and truck capacities.
- Consider regulatory constraints for drone operations.
- Account for real-world traffic conditions in simulations.

## Use This When

- Implementing last-mile delivery solutions in urban areas with high demand density.
- Seeking to reduce operational costs and environmental impacts in logistics.
- Integrating drone technology into existing delivery systems.

## Don't Use When

- Delivering large, heavy parcels that exceed drone capacity.
- Operating in areas with strict regulations against drone usage.
- When delivery time windows are critical and cannot be accommodated.

## Key Concepts

Life Cycle Assessment, Life Cycle Cost Analysis, Mixed-Integer Linear Programming, sensitivity analysis

## Connects To

- Traveling Salesman Problem (TSP)
- Flying Sidekick Traveling Salesman Problem (FSTSP)
- Multi-Objective Genetic Algorithm (MOGA)

## Prerequisites

- Understanding of optimization techniques.
- Familiarity with drone logistics and operational constraints.
- Knowledge of environmental impact assessment methods.

## Limitations

- Limited to scenarios where drones can operate legally.
- Assumes constant speeds for vehicles, which may not reflect real-world conditions.
- Does not account for customer-specific delivery time requirements.

## Open Questions

- How can the model be adapted for varying customer demand patterns?
- What are the long-term economic impacts of widespread drone adoption in logistics?

## Abstract

​The Traveling Salesman Problem (TSP) is a classic optimization challenge. There’s a set of points (locations), and a “salesman” (or in this case, a delivery vehicle) who must visit each point once, and then return to the starting point. And he must do all this in the shortest total distance. On the surface, it seems fairly straightforward. You might assume that with enough computational power, you could just check all the options fairly quickly. But you can’t. The complexity of TSP grows exponentially as the number of points increases. The number of total possibilities is the factorial of one-less than the number of points. So with just a handful of destinations, it’s feasible to calculate every possible route and choose the shortest one. But, as the number of points grows, the solutions can’t be built incrementally, so there is a combinatorial explosion. This is what we call NP-Hard
