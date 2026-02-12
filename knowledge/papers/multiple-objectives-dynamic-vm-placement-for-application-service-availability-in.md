# Multiple objectives dynamic VM placement for application service availability in cloud networks

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1186/s13677-024-00610-2` |
| Full Paper | [https://doi.org/10.1186/s13677-024-00610-2](https://doi.org/10.1186/s13677-024-00610-2) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/29da7e58ec7b02d99d764cf601f868736341307e](https://www.semanticscholar.org/paper/29da7e58ec7b02d99d764cf601f868736341307e) |
| Source | [https://journalclub.io/episodes/multiple-objectives-dynamic-vm-placement-for-application-service-availability-in-cloud-networks](https://journalclub.io/episodes/multiple-objectives-dynamic-vm-placement-for-application-service-availability-in-cloud-networks) |
| Source | [https://www.semanticscholar.org/paper/29da7e58ec7b02d99d764cf601f868736341307e](https://www.semanticscholar.org/paper/29da7e58ec7b02d99d764cf601f868736341307e) |
| Year | 2026 |
| Citations | 10 |
| Authors | Yanal Alahmad, Anjali Agarwal |
| Paper ID | `85a3fb2e-bf89-438f-9e01-08206c00a9a0` |

## Classification

- **Problem Type:** multi-objective optimization
- **Domain:** Cloud Computing
- **Sub-domain:** Virtual Machine Placement
- **Technique:** MoVPAAC
- **Technique Category:** framework
- **Type:** novel

## Summary

The paper presents the MoVPAAC framework, which addresses the NP-hard problem of dynamic VM placement in cloud computing by optimizing for multiple objectives such as power consumption, resource waste, and application availability. Engineers should care because this framework enhances service availability and resource utilization, which are critical for cloud service providers.

## Key Contribution

**Introduction of the MoVPAAC framework for dynamic VM placement that integrates multiple optimization goals to ensure high application availability in cloud environments.**

## Problem

The need to allocate virtual machines in a way that minimizes resource waste and power consumption while maximizing application availability and responsiveness in cloud networks.

## Method

**Approach:** The MoVPAAC framework uses an integer nonlinear programming (INLP) model to optimize dynamic VM placement based on multiple objectives. It employs an Ant Colony heuristic algorithm for solving the INLP model and a deep learning method for predicting application task failures.

**Algorithm:**

1. 1. Define the application service availability requirements.
2. 2. Model the dynamic VM placement problem as an INLP with multiple objectives.
3. 3. Use the Ant Colony heuristic to find optimal VM placements.
4. 4. Implement a deep learning model to predict task failures.
5. 5. Adjust VM placements based on predicted failures to ensure high availability.
6. 6. Monitor resource utilization and adjust placements dynamically.

**Input:** Application service requirements, server availability, resource capacities, and historical failure data.

**Output:** Optimized VM placement strategy that meets availability requirements while minimizing power consumption and resource waste.

**Key Parameters:**

- `availability_requirement: 0.9`
- `power_consumption: minimized`
- `resource_waste: minimized`

**Complexity:** NP-hard

## Benchmarks

**Tested on:** Simulated cloud environment with varying workloads and availability requirements.

**Results:**

- Power consumption, resource utilization, application availability

**Compared against:** Existing VM placement algorithms from the literature

**Improvement:** The proposed solution outperformed baseline algorithms in terms of application admission rates, power consumption reduction, and CPU/RAM utilization.

## Implementation Guide

**Data Structures:** Graphs for representing server and VM relationships, Matrices for resource allocation

**Dependencies:** Optimization libraries (e.g., CPLEX), Deep learning frameworks (e.g., TensorFlow, PyTorch)

**Core Operation:**

```python
optimize_vm_placement(app_requirements, server_data): return MoVPAAC(app_requirements, server_data)
```

**Watch Out For:**

- Ensure accurate prediction of task failures to avoid unnecessary migrations.
- Monitor resource utilization continuously to adapt placements dynamically.
- Be aware of the computational overhead of the INLP model.

## Use This When

- You need to optimize VM placement for multiple objectives in a cloud environment.
- You are facing challenges with application availability and resource utilization.
- You require a proactive approach to manage VM failures and ensure service continuity.

## Don't Use When

- The application does not have strict availability requirements.
- You are working in a static VM placement scenario.
- The overhead of implementing a complex framework is not justified.

## Key Concepts

Dynamic VM placement, Integer nonlinear programming, Ant Colony optimization, Deep learning for failure prediction

## Connects To

- Integer Linear Programming (ILP)
- Ant Colony Optimization (ACO)
- Deep Learning for Predictive Analytics

## Prerequisites

- Understanding of optimization techniques
- Familiarity with cloud computing architectures
- Knowledge of machine learning for predictive modeling

## Limitations

- The framework may require significant computational resources for large-scale deployments.
- Accuracy of failure predictions can impact overall performance.
- The approach is tailored for cloud environments and may not generalize to other contexts.

## Open Questions

- How can the framework be adapted for different cloud service models?
- What additional objectives could be integrated into the optimization model?

## Abstract

If you’ve been around computer science for a while you’ve undoubtedly heard of the Bin-Packing problem. While it's surely difficult, imagine how much worse it would be if you had to optimize for several variables at the same time. That’s the situation faced by high volume SaaS companies who are trying to allocate Virtual Machines (or containers) onto their bare metal compute. They’re not just trying to minimize resource waste and cost, they need to balance power consumption, failure rates, application responsiveness, uptime, and more. Doing that is NP-hard and incredibly complex. In this paper the authors conceive an elegant solution: A framework called MoVPAAC.
