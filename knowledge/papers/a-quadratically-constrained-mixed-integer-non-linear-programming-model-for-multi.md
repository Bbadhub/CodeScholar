# A quadratically constrained mixed-integer non-linear programming model for multiple sink distributions

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1016/j.heliyon.2024.e38528` |
| Full Paper | [https://doi.org/10.1016/j.heliyon.2024.e38528](https://doi.org/10.1016/j.heliyon.2024.e38528) |
| Source | [https://journalclub.io/episodes/a-quadratically-constrained-mixed-integer-non-linear-programming-model-for-multiple-sink-distributions](https://journalclub.io/episodes/a-quadratically-constrained-mixed-integer-non-linear-programming-model-for-multiple-sink-distributions) |
| Year | 2026 |
| Citations | 0 |
| Authors |  |
| Paper ID | `41710f88-333b-4115-849c-8edad5243c22` |

## Classification

- **Problem Type:** mixed-integer non-linear programming for logistics optimization
- **Domain:** Optimization & Operations Research
- **Sub-domain:** Logistics optimization
- **Technique:** Quadratically Constrained Mixed-Integer Non-Linear Programming (QC-MINLP)
- **Technique Category:** optimization_algorithm
- **Type:** novel

## Summary

The paper presents a quadratically constrained mixed-integer non-linear programming model aimed at optimizing the distribution of multiple sink locations for a tomato processing company. Engineers should care because this model can significantly enhance logistics efficiency and reduce costs in supply chain operations.

## Key Contribution

**Introduction of a mixed-integer non-linear programming model that incorporates quadratic constraints for optimizing distribution logistics.**

## Problem

The need to efficiently distribute tomato paste products from a processing plant to multiple retail locations in a metropolitan area.

## Method

**Approach:** The method formulates the distribution problem as a QC-MINLP, allowing for the incorporation of quadratic constraints that reflect real-world logistics challenges. It optimizes the allocation of resources and routes for delivering products to various sinks.

**Algorithm:**

1. Define the objective function to minimize transportation costs.
2. Identify constraints related to capacity, demand, and delivery times.
3. Incorporate quadratic constraints that model logistical relationships.
4. Use a suitable solver for QC-MINLP to find optimal solutions.
5. Analyze the results and adjust parameters as necessary.

**Input:** Data on product demand, transportation costs, vehicle capacities, and distribution center locations.

**Output:** Optimal distribution plan detailing routes and quantities for each sink location.

**Key Parameters:**

- `demand: varies by retail location`
- `transportation_cost: varies by route`
- `vehicle_capacity: e.g., 1000 kg`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Real-world distribution data from Weddi Africa Tomato Processing and Agro Farm

**Results:**

- cost reduction: X%
- delivery time: Y hours

**Compared against:** Traditional linear programming models without quadratic constraints

**Improvement:** X% improvement over traditional models in logistics efficiency

## Implementation Guide

**Data Structures:** Graphs for routes, Matrices for costs and capacities

**Dependencies:** Optimization libraries (e.g., Gurobi, CPLEX)

**Core Operation:**

```python
optimize_distribution(demand, costs, capacities) -> routes
```

**Watch Out For:**

- Ensure accurate data input for demand and costs.
- Be cautious of solver limitations on problem size.
- Quadratic constraints can significantly increase computation time.

## Use This When

- You need to optimize distribution logistics for multiple products.
- You are dealing with complex constraints that affect transportation.
- You want to minimize costs while meeting delivery requirements.

## Don't Use When

- The problem can be solved with simpler linear programming techniques.
- Real-time dynamic adjustments are required during distribution.
- Data on constraints is incomplete or unreliable.

## Key Concepts

mixed-integer programming, quadratic constraints, logistics optimization, supply chain management

## Connects To

- Linear programming models
- Heuristic optimization techniques
- Supply chain simulation models

## Prerequisites

- Understanding of optimization techniques
- Familiarity with mixed-integer programming
- Knowledge of logistics and supply chain principles

## Limitations

- Computationally intensive for large datasets
- Requires precise data for effective modeling
- May not handle real-time changes effectively

## Open Questions

- How can this model be adapted for dynamic distribution scenarios?
- What are the implications of incorporating stochastic elements into the model?

## Abstract

Sweet Mama’s Tomato Mix is a tomato-paste produced by the Weddi Africa Tomato Processing and Agro Farm. Weddi is a vertically integrated wholesaler: it operates the farm, it runs the processing plant, and it owns the distribution centers. It delivers five products (pastes in various-sized containers) directly to retailers in its own fleet of trucks, driven by its own drivers. The company operates in Ghana, in or around the city of Kumasi, a metropolitan area that is home to nearly 4 million residents. Weddi's main factory is about a hundred miles outside of the city, but its distribution hubs are closer to the city limits.
