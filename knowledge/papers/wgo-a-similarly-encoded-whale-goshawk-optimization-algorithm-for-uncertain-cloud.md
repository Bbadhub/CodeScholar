# WGO: a similarly encoded whale-goshawk optimization algorithm for uncertain cloud manufacturing service composition

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1007/s43684-025-00089-x` |
| Full Paper | [https://doi.org/10.1007/s43684-025-00089-x](https://doi.org/10.1007/s43684-025-00089-x) |
| Source | [https://journalclub.io/episodes/wgo-a-similarly-encoded-whale-goshawk-optimization-algorithm-for-uncertain-cloud-manufacturing-service-composition](https://journalclub.io/episodes/wgo-a-similarly-encoded-whale-goshawk-optimization-algorithm-for-uncertain-cloud-manufacturing-service-composition) |
| Year | 2026 |
| Citations | 0 |
| Authors |  |
| Paper ID | `329ac4f1-f5a2-43c1-93ce-030569831057` |

## Classification

- **Problem Type:** service composition optimization
- **Domain:** Cloud Manufacturing
- **Sub-domain:** Service Composition
- **Technique:** Whale-Goshawk Optimization Algorithm (WGO)
- **Technique Category:** optimization_algorithm
- **Type:** novel

## Summary

The paper presents the Whale-Goshawk Optimization Algorithm (WGO), which enhances service composition in uncertain cloud manufacturing environments by integrating a novel similar integer coding method and combining the Whale Optimization Algorithm (WOA) with the Northern Goshawk Optimization Algorithm (NGO). Engineers should care because this approach improves the efficiency and effectiveness of service selection under uncertainty, a common challenge in cloud manufacturing.

## Key Contribution

**Introduction of the Whale-Goshawk Optimization Algorithm (WGO) that combines WOA and NGO with a novel similar integer coding method for improved service composition in uncertain environments.**

## Problem

The work addresses the challenge of optimizing service composition in cloud manufacturing, where uncertainties in service states and environments complicate traditional QoS-based methods.

## Method

**Approach:** WGO operates in two stages: a global search using a similar integer coding method to identify potential service combinations, followed by a local search that refines these combinations based on service similarity. The algorithm utilizes cosine similarity to group services with similar QoS attributes, enhancing the search for optimal solutions.

**Algorithm:**

1. 1. Decompose the user request into subtasks.
2. 2. Construct a candidate service set (CSS) for each subtask.
3. 3. Apply similar integer coding to the CSS based on QoS similarity.
4. 4. Perform a global search using WOA to identify promising service combinations.
5. 5. Execute a local search using NGO to refine the identified combinations.
6. 6. Evaluate the service combinations based on user-defined QoS preferences.
7. 7. Return the optimal service composition.

**Input:** User request for service composition, including QoS preferences and task requirements.

**Output:** Optimal service composition that maximizes QoS attributes according to user preferences.

**Key Parameters:**

- `cosine_similarity_threshold: 0.6`
- `γ: 0.3`
- `max_iterations: T (not specified)`

**Complexity:** Not stated.

## Benchmarks

**Tested on:** Not specified in the provided text.

**Results:**

- QoS attributes, execution time, cost, reliability.

**Compared against:** Traditional QoS-based service composition methods.

**Improvement:** Experimental results demonstrate effectiveness, but specific improvement percentages are not stated.

## Implementation Guide

**Data Structures:** Service repository, Candidate service set (CSS), Similar service set (SS)

**Dependencies:** NumPy for numerical operations, SciPy for cosine similarity calculations

**Core Operation:**

```python
services = similar_integer_coding(candidate_services); optimal_services = WGO(services);
```

**Watch Out For:**

- Ensure the cosine similarity threshold is appropriate for your service set.
- Monitor the balance between global and local search to avoid local optima.
- Be cautious of the computational cost when dealing with large service repositories.

## Use This When

- You need to optimize service composition in a cloud manufacturing environment with uncertain service states.
- You have a large repository of services with varying QoS attributes and need to group similar services.
- You require a flexible optimization algorithm that can adapt to dynamic service conditions.

## Don't Use When

- The service repository is small and stable, where simpler methods may suffice.
- Real-time processing is critical and cannot accommodate the algorithm's computational overhead.
- You need guaranteed optimal solutions rather than near-optimal solutions.

## Key Concepts

similar integer coding, cosine similarity, global search, local search, cloud manufacturing, service composition

## Connects To

- Whale Optimization Algorithm (WOA)
- Northern Goshawk Optimization Algorithm (NGO)
- Genetic Algorithms
- Ant Colony Optimization
- Particle Swarm Optimization

## Prerequisites

- Understanding of QoS metrics
- Familiarity with optimization algorithms
- Knowledge of cloud manufacturing concepts

## Limitations

- Performance may degrade with very large service repositories
- Sensitivity to the choice of similarity threshold
- Assumes service QoS attributes are accurately measurable

## Open Questions

- How can the algorithm be adapted for real-time service composition?
- What are the implications of varying QoS metrics on the optimization process?

## Abstract

Similar Integer Coding incorporates an awareness of service similarity. Instead of treating each service as an entirely distinct option, this approach groups services with comparable QoS attributes into clusters before assigning integer codes. These clusters are formed based on a similarity measure, specifically cosine similarity, which evaluates how close two services are in terms of key performance metrics. Cosine similarity is a mathematical technique that measures the angle between two vectors in a multi-dimensional space, rather than their absolute distance. In the context of service composition, each service can be represented as a vector of its QoS attributes, where each attribute (execution time, cost, reliability) corresponds to a dimension. The cosine similarity score between two services is computed as the dot product of their vectors divided by the product of their magnitudes, resulting in a value between -1 and 1. A similarity
