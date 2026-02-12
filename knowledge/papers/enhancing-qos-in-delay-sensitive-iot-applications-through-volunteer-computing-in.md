# Enhancing QoS in Delay-Sensitive IoT Applications through Volunteer Computing in Fog Environments

## Access

| Field | Value |
|-------|-------|
| DOI | `10.33889/IJMEMS.2024.9.6.072` |
| Full Paper | [https://doi.org/10.33889/IJMEMS.2024.9.6.072](https://doi.org/10.33889/IJMEMS.2024.9.6.072) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/f70b823d8dac7c73e2bab769b9d5c40372270c5d](https://www.semanticscholar.org/paper/f70b823d8dac7c73e2bab769b9d5c40372270c5d) |
| Source | [https://journalclub.io/episodes/enhancing-qos-in-delay-sensitive-iot-applications-through-volunteer-computing-in-fog-environments](https://journalclub.io/episodes/enhancing-qos-in-delay-sensitive-iot-applications-through-volunteer-computing-in-fog-environments) |
| Source | [https://www.semanticscholar.org/paper/f70b823d8dac7c73e2bab769b9d5c40372270c5d](https://www.semanticscholar.org/paper/f70b823d8dac7c73e2bab769b9d5c40372270c5d) |
| Year | 2026 |
| Citations | 0 |
| Authors | M. Rani, Kalpna Guleria, S. Panda |
| Paper ID | `339376b4-2ef6-4a18-844b-055f606b24e1` |

## Classification

- **Problem Type:** task scheduling
- **Domain:** Networking & Distributed Systems
- **Sub-domain:** Volunteer Computing, Fog Computing
- **Technique:** Min-CCV and Min-V
- **Technique Category:** scheduling_algorithm
- **Type:** novel

## Summary

The paper presents two heuristic algorithms, Min-CCV and Min-V, aimed at enhancing Quality of Service (QoS) in delay-sensitive IoT applications by optimizing task scheduling in volunteer computing systems within fog environments. Engineers should care because these algorithms significantly improve network performance and reduce costs associated with computational and communicational tasks.

## Key Contribution

**Introduction of Min-CCV and Min-V algorithms for efficient task scheduling in volunteer computing systems to enhance QoS.**

## Problem

The need to optimize task scheduling in heterogeneous volunteer computing environments to improve QoS for delay-sensitive IoT applications.

## Method

**Approach:** The proposed algorithms Min-CCV and Min-V prioritize tasks based on their deadlines and costs associated with violations, effectively scheduling them across fog and cloud nodes. This dynamic allocation aims to minimize computational, communicational, and violational costs while maximizing QoS.

**Algorithm:**

1. 1. Receive task requests from IoT devices.
2. 2. Calculate task attributes including memory requirements, input/output sizes, and QoS requirements.
3. 3. Prioritize tasks based on deadlines and violation costs.
4. 4. Allocate tasks to appropriate fog or cloud nodes based on resource availability.
5. 5. Execute tasks and monitor performance metrics.
6. 6. Adjust allocations dynamically based on real-time resource utilization.

**Input:** Task requests from IoT devices including attributes like memory requirement, input/output file sizes, and QoS requirements.

**Output:** Allocated tasks to fog and cloud nodes with improved QoS metrics.

**Key Parameters:**

- `deadline: specific time by which a task must be completed`
- `cost_violation: penalty for not meeting task deadlines`
- `memory_requirement: varies by task`
- `input_output_sizes: varies by task`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Simulated task requests in a volunteer computing environment

**Results:**

- Deadline satisfaction rate: approximately 99.5%
- Cost reduction: 15 to 53% compared to existing methods

**Compared against:** Generic-based algorithms for task scheduling

**Improvement:** Significant improvement in deadline satisfaction and cost efficiency over existing methods.

## Implementation Guide

**Data Structures:** Task request queue, Resource availability matrix, Task allocation matrix

**Dependencies:** iFogSim for simulation, Python for algorithm implementation

**Core Operation:**

```python
for task in task_requests: allocate_task(task, fog_nodes, cloud_nodes)
```

**Watch Out For:**

- Ensure accurate measurement of task attributes to avoid misallocation.
- Monitor resource availability in real-time to adapt to changing conditions.
- Consider the overhead of communication costs when scheduling tasks.

## Use This When

- You need to optimize task scheduling for IoT applications with strict latency requirements.
- You are working in a heterogeneous computing environment with varying resource capabilities.
- Cost efficiency is a priority in your computing resource allocation.

## Don't Use When

- Tasks have uniform requirements and do not vary in priority or resource needs.
- The computing environment is entirely homogeneous with no variability in resource capabilities.
- Real-time processing is not critical for the application.

## Key Concepts

Volunteer computing, Quality of Service, Task scheduling, Fog computing, Cost efficiency

## Connects To

- Cloud computing frameworks
- Task scheduling algorithms in distributed systems
- Resource management techniques in IoT

## Prerequisites

- Understanding of task scheduling concepts
- Knowledge of fog and cloud computing architectures
- Familiarity with QoS metrics and their importance in IoT applications

## Limitations

- The algorithms may not perform well in completely homogeneous environments.
- Dynamic resource availability can complicate scheduling decisions.
- The focus on cost and QoS may overlook other important factors like energy efficiency.

## Open Questions

- How can these algorithms be adapted for real-time processing tasks?
- What additional metrics can be incorporated to further enhance QoS in volunteer computing?

## Abstract

Imagine for a second that you are an IoT device. You’re a smart watch, or a smart speaker, or a smart lamp, or a smart fridge. Either way you’re smart, you’ve got a processor onboard, and you can handle a lot of the computational workload yourself. But for some tasks, there are just so many calculations to do (so quickly) that your onboard chip isn’t up to the job. For those kinds of workloads, you offload the processing to a remote server, let that machine do the heavy lifting, and then return the result. But there’s a problem. When it comes to choosing the type of server that you send your workload to, you are spoiled for choice. You’ve got three main classes of options: Cloud Servers, Edge Servers, and Fog Nodes.
