# Dynamic scheduling strategies for cloud-based load balancing in parallel and distributed systems

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1186/s13677-025-00757-6` |
| Full Paper | [https://doi.org/10.1186/s13677-025-00757-6](https://doi.org/10.1186/s13677-025-00757-6) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/30a8085aa722b775b5b0e1de4c6a39e9c8049bf7](https://www.semanticscholar.org/paper/30a8085aa722b775b5b0e1de4c6a39e9c8049bf7) |
| Source | [https://journalclub.io/episodes/dynamic-scheduling-strategies-for-cloud-based-load-balancing-in-parallel-and-distributed-systems](https://journalclub.io/episodes/dynamic-scheduling-strategies-for-cloud-based-load-balancing-in-parallel-and-distributed-systems) |
| Source | [https://www.semanticscholar.org/paper/30a8085aa722b775b5b0e1de4c6a39e9c8049bf7](https://www.semanticscholar.org/paper/30a8085aa722b775b5b0e1de4c6a39e9c8049bf7) |
| Year | 2026 |
| Citations | 2 |
| Authors | Nasser S. Albalawi |
| Paper ID | `5edc36fd-267f-4942-bb16-0afc8566dca9` |

## Classification

- **Problem Type:** dynamic load balancing and task scheduling in cloud computing
- **Domain:** Cloud Computing
- **Sub-domain:** Load Balancing and Resource Management
- **Technique:** Round-Robin Allocation with Sunflower Whale Optimization (RRA-SWO)
- **Technique Category:** optimization_algorithm
- **Type:** novel

## Summary

The paper presents a comprehensive dynamic scheduling approach for load balancing in cloud-based parallel and distributed systems, utilizing a combination of optimization techniques to enhance resource allocation and task scheduling. Engineers should care because it addresses critical issues of resource underutilization and performance degradation in cloud environments.

## Key Contribution

**Introduction of a novel integration of Round-Robin Allocation with Sunflower Whale Optimization (RRA-SWO) for effective load balancing in cloud systems.**

## Problem

The work is motivated by the need to optimize resource utilization and performance in cloud environments facing dynamic workloads and potential bottlenecks.

## Method

**Approach:** The method involves detecting overloaded virtual machine hosts (VMHs), making decisions on VM migrations, and dynamically balancing loads using a combination of RRA-SWO for allocation and Hybrid Ant Genetic Algorithm (HAGA) for scheduling. Continuous monitoring and adjustment are performed using Least Response Time (LRT) and Harmony Search Algorithm with Linear Regression (LR-HSA).

**Algorithm:**

1. 1. Detect overloaded VMHs.
2. 2. Use RRA-SWO to allocate VMs to underutilized VMHs.
3. 3. Schedule tasks using HAGA.
4. 4. Monitor load using LRT.
5. 5. Predict workload changes using LR-HSA.
6. 6. Adjust resources dynamically based on predictions.
7. 7. Implement Least Recently Used (LRU) for task rescheduling.

**Input:** Current load data from VMHs, task requirements, and resource availability.

**Output:** Optimally balanced load distribution across VMHs and scheduled tasks.

**Key Parameters:**

- `learning_rate: 0.01`
- `population_size: 100`
- `migration_threshold: 70%`

**Complexity:** Not stated

## Benchmarks

**Tested on:** CloudSim simulation environment

**Results:**

- Packet Delivery Ratio: 98%
- Average Response Time: 65 seconds
- Task Success Rate: 95%
- Memory Utilization Rate: 80%
- Throughput: 97%

**Compared against:** Existing load balancing algorithms without dynamic scheduling

**Improvement:** Substantial enhancements in performance metrics compared to baseline methods.

## Implementation Guide

**Data Structures:** Priority queues for task scheduling, Graphs for VM dependencies, Arrays for load metrics

**Dependencies:** CloudSim, NetBeans 12.3, Optimization libraries for RRA-SWO and HAGA

**Core Operation:**

```python
for each VM in overloaded_VM_list: allocate_VM(VM, underutilized_VM); schedule_tasks(VM);
```

**Watch Out For:**

- Ensure accurate load monitoring to avoid false positives in VM migration.
- Be cautious of the overhead introduced by frequent VM migrations.
- Test the system under various load conditions to validate performance.

## Use This When

- You need to optimize resource utilization in a cloud environment.
- You are facing performance degradation due to overloaded virtual machines.
- You require real-time load monitoring and adjustment in distributed systems.

## Don't Use When

- The system has static workloads with predictable resource requirements.
- You are working in a non-cloud environment.
- The overhead of dynamic scheduling outweighs the benefits.

## Key Concepts

dynamic scheduling, load balancing, resource allocation, task scheduling, cloud computing, optimization algorithms

## Connects To

- Ant Colony Optimization (ACO)
- Genetic Algorithms (GA)
- Harmony Search Algorithm
- Reinforcement Learning for dynamic scheduling
- Deep Learning for load prediction

## Prerequisites

- Understanding of cloud computing architectures
- Familiarity with optimization algorithms
- Knowledge of task scheduling principles

## Limitations

- Performance may degrade under extremely high loads.
- Complexity in implementation due to multiple algorithms.
- Potential overhead from dynamic monitoring and adjustments.

## Open Questions

- How can the approach be adapted for edge computing environments?
- What are the implications of using this method in hybrid cloud scenarios?

## Abstract

If you’re running a large cluster of interconnected cloud services, a systemic failure probably won’t start with a ‘crash’. There will be no loud explosion or dramatic boom. Not at the early stages of the problem anyway. Initially, all you’ll hear is a faint whine. One node, struggling to keep its head above water. It could be a webserver, or a database, or a queue, or a cache, or a block store…whatever your bottleneck (the weakest part of your system) happens to be. You’ll notice it hiccuping, and sweating. You’ll see its performance slowly degrading, and becoming less predictable, as the machine, little by little, gets completely overwhelmed. Then finally, minutes, or hours, or weeks later, it goes down. Taking who-knows-what with it along the way.
