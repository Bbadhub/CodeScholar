# Fast autoscaling algorithm for cost optimization of container clusters

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1186/s13677-025-00748-7` |
| Full Paper | [https://doi.org/10.1186/s13677-025-00748-7](https://doi.org/10.1186/s13677-025-00748-7) |
| Source | [https://journalclub.io/episodes/fast-autoscaling-algorithm-for-cost-optimization-of-container-clusters](https://journalclub.io/episodes/fast-autoscaling-algorithm-for-cost-optimization-of-container-clusters) |
| Year | 2026 |
| Citations | 0 |
| Authors |  |
| Paper ID | `6a1ec9fe-62ca-47ac-a78c-d68c07467733` |

## Classification

- **Problem Type:** resource allocation optimization
- **Domain:** Cloud Computing
- **Sub-domain:** Container orchestration
- **Technique:** Fast Container to Machine Allocator (FCMA)
- **Technique Category:** optimization_algorithm
- **Type:** novel

## Summary

The paper presents the Fast Container to Machine Allocator (FCMA), an algorithm designed to optimize the allocation of containers and virtual machines in cloud environments to minimize deployment costs while ensuring timely autoscaling. Engineers should care because FCMA significantly reduces solving time compared to traditional Integer Linear Programming (ILP) models, making it suitable for real-time applications.

## Key Contribution

**Development of the FCMA algorithm for fast and cost-effective resource allocation in container clusters.**

## Problem

The challenge of efficiently allocating containers and virtual machines in cloud environments to meet variable workloads without exceeding time and memory limits.

## Method

**Approach:** FCMA calculates the optimal allocation of containers and VMs based on workload predictions to minimize costs. It operates by reducing the problem size and combining ILP methods with heuristics to achieve near-optimal solutions quickly.

**Algorithm:**

1. 1. Define the workload for each application in requests per second.
2. 2. Identify available instance classes and their resources (CPU, memory, price).
3. 3. Formulate a partial ILP problem to determine initial allocations.
4. 4. Aggregate nodes based on resource requirements.
5. 5. Allocate containers to nodes based on performance and cost.
6. 6. Aggregate containers to optimize resource usage.

**Input:** Workload data (requests per second), instance class specifications (CPU cores, memory, price), container class requirements.

**Output:** Number of VMs and containers allocated for each application, along with their respective resources.

**Key Parameters:**

- `workload: requests per second (rps)`
- `instance_classes: number of available instance classes`
- `containers: number of container classes`
- `cores: CPU cores required per container`
- `memory: memory required per container (GB)`
- `price: cost per hour of instance classes ($/h)`

**Complexity:** Not stated.

## Benchmarks

**Tested on:** Synthetic workloads representing various application demands.

**Results:**

- Solving time reduction: average of two orders of magnitude faster than ILP; Cost-effectiveness: comparable to ILP solutions.

**Compared against:** Conlloovia (previous ILP model), First Fit by Core (FFC), First Fit by Price (FFP) heuristics.

**Improvement:** FCMA shows an average solving time reduction of two orders of magnitude compared to Conlloovia.

## Implementation Guide

**Data Structures:** Arrays for instance classes, containers, and their resource requirements., Graphs for representing container-to-machine assignments.

**Dependencies:** Python libraries for optimization (e.g., PuLP, SciPy), Kubernetes for deployment.

**Core Operation:**

```python
for each application: allocate_resources(workload, instance_classes, containers)
```

**Watch Out For:**

- Ensure accurate workload predictions to avoid under or over-provisioning.
- Monitor the performance of containers to adjust allocations dynamically.
- Be aware of the trade-offs between cost and fault tolerance.

## Use This When

- You need to optimize resource allocation in a cloud environment with variable workloads.
- Real-time autoscaling decisions are critical for maintaining service levels.
- You want to minimize costs associated with deploying containers and VMs.

## Don't Use When

- The workload is predictable and does not require dynamic scaling.
- You have a very small number of containers and VMs, making the problem trivial.
- You require absolute optimality over speed in resource allocation.

## Key Concepts

autoscaling, resource allocation, cost optimization, container orchestration, virtual machines, cloud computing, heuristics, ILP

## Connects To

- Integer Linear Programming (ILP)
- Heuristic optimization methods
- Kubernetes autoscalers
- Cloud resource management frameworks

## Prerequisites

- Understanding of cloud computing concepts
- Familiarity with container orchestration
- Basic knowledge of optimization techniques

## Limitations

- FCMA is primarily focused on CPU-bound applications and may not perform well for memory or I/O intensive workloads.
- The algorithm's performance may degrade with extremely large problem sizes or highly variable workloads.
- Secondary objectives may conflict with primary cost minimization goals.

## Open Questions

- How can FCMA be adapted for memory-bound or I/O-bound applications?
- What additional heuristics can be integrated to further improve allocation efficiency?

## Abstract

Here’s the issue: ILP has a scaling ceiling. As the number of container classes, VM types, and applications increases, the size of the optimization problem explodes. Each container can fit in multiple VMs. Each VM can host multiple container combinations. And when you allow for both horizontal and vertical scaling, the variable count rapidly outpaces what most solvers can handle in real time. Even with carefully engineered simplifications, these systems eventually break down. In larger deployments, or in clusters with short scheduling windows, the solver either fails to converge or exceeds memory limits. So that’s the problem facing these researchers. Even if your workload forecasts are perfect, and your autoscaler has a rich inventory of resource types to choose from, you still have to solve the container-to-machine assignment problem in a matter of seconds. If you can’t, your autoscaler can’t act in time. That means wasted capacity, missed SLAs
