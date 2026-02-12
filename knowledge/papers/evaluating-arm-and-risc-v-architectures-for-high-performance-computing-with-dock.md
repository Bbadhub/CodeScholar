# Evaluating ARM and RISC-V Architectures for High-Performance Computing with Docker and Kubernetes

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3390/electronics13173494` |
| Full Paper | [https://doi.org/10.3390/electronics13173494](https://doi.org/10.3390/electronics13173494) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/07ce97a177120e6383fc3d5ba5dd526971bbecca](https://www.semanticscholar.org/paper/07ce97a177120e6383fc3d5ba5dd526971bbecca) |
| Source | [https://journalclub.io/episodes/evaluating-arm-and-risc-v-architectures-for-high-performance-computing-with-docker-and-kubernetes](https://journalclub.io/episodes/evaluating-arm-and-risc-v-architectures-for-high-performance-computing-with-docker-and-kubernetes) |
| Source | [https://www.semanticscholar.org/paper/07ce97a177120e6383fc3d5ba5dd526971bbecca](https://www.semanticscholar.org/paper/07ce97a177120e6383fc3d5ba5dd526971bbecca) |
| Year | 2026 |
| Citations | 10 |
| Authors | Vedran Dakić, Leo Mršić, Zdravko Kunić, Goran Đambić |
| Paper ID | `983186a2-73cb-42f5-b8fc-330e93b7dc6c` |

## Classification

- **Problem Type:** high-performance computing evaluation
- **Domain:** Computer Architecture
- **Sub-domain:** High-Performance Computing, Containerization
- **Technique:** Performance Evaluation of ARM and RISC-V Architectures
- **Technique Category:** evaluation_method
- **Type:** comparison

## Summary

This paper evaluates the performance of ARM and RISC-V architectures in high-performance computing (HPC) environments, particularly focusing on their integration with Docker and Kubernetes. Engineers should care because the findings highlight ARM's superior performance and ease of use in HPC workloads compared to RISC-V, which faces integration challenges.

## Key Contribution

**The paper provides a comparative analysis of ARM and RISC-V architectures for HPC, emphasizing the practical implications of their integration with containerization technologies.**

## Problem

The need for efficient and scalable computing solutions in scientific research and other computationally intensive fields motivated this work.

## Method

**Approach:** The method involves setting up high-performance computing environments using ARM and RISC-V architectures integrated with Docker and Kubernetes. Performance metrics such as scalability and efficiency are then measured and compared across both architectures.

**Algorithm:**

1. 1. Set up Docker containers for both ARM and RISC-V architectures.
2. 2. Deploy Kubernetes clusters to manage the containers.
3. 3. Run benchmark tests to evaluate performance metrics.
4. 4. Collect data on processing speed, resource utilization, and scalability.
5. 5. Analyze the results to compare ARM and RISC-V performance.

**Input:** Docker images configured for ARM and RISC-V architectures.

**Output:** Performance metrics including processing speed, resource utilization, and scalability results.

**Key Parameters:**

- `docker_image_size: 500MB`
- `kubernetes_node_count: 5`
- `benchmark_duration: 60 minutes`

**Complexity:** not stated

## Benchmarks

**Tested on:** Synthetic HPC workloads designed for benchmarking

**Results:**

- Processing speed, resource utilization, scalability

**Compared against:** x86 architecture performance metrics

**Improvement:** ARM showed better performance and scalability compared to RISC-V, though specific percentage improvements were not quantified.

## Implementation Guide

**Data Structures:** Docker containers, Kubernetes clusters

**Dependencies:** Docker, Kubernetes, Benchmarking tools (e.g., HPCG, STREAM)

**Core Operation:**

```python
deploy_application(architecture='ARM/RISC-V', container='docker_image')
```

**Watch Out For:**

- Ensure compatibility of Docker images with the target architecture.
- Monitor resource utilization closely to avoid bottlenecks.
- Be aware of the integration challenges when using RISC-V with Kubernetes.

## Use This When

- You need to deploy HPC applications in a containerized environment.
- You are evaluating different architectures for energy efficiency in computing.
- You require a scalable solution for scientific computing workloads.

## Don't Use When

- You need maximum compatibility with existing x86 software ecosystems.
- You require a highly customizable architecture without integration complexity.
- You are working in an environment where RISC-V's current limitations are a critical factor.

## Key Concepts

HPC, ARM architecture, RISC-V architecture, Docker, Kubernetes, containerization, performance evaluation

## Connects To

- Docker Swarm for container orchestration
- Kubernetes for managing containerized applications
- Benchmarking frameworks for HPC evaluation

## Prerequisites

- Understanding of containerization technologies
- Familiarity with high-performance computing concepts
- Knowledge of ARM and RISC-V architectures

## Limitations

- RISC-V integration with Kubernetes is complex and less mature than ARM.
- Performance may vary significantly based on specific workloads.
- ARM's proprietary nature may limit customization compared to RISC-V.

## Open Questions

- What optimizations can be made to improve RISC-V's integration with container technologies?
- How can ARM and RISC-V architectures be further enhanced for specific HPC applications?

## Abstract

In 2020, Apple revealed the first release in their “M” series of computers, their foray into designing and building their own chips. No longer would they depend on Intel's processors to power their machines; the future of Apple would be vertically-integrated chip development. And it all started with The M1. While most of the headlines of the time were about the sheer processing power of the computer, many articles buried the real lead. The incredible part of the announcement was less about Apple bringing chip-manufacturing in-house, and more about the fact that they had switched from x86 to ARM. This wasn’t just a coup d’etat for ARM, it was a win for RISC: The Reduced Instruction Set Computer architecture.
