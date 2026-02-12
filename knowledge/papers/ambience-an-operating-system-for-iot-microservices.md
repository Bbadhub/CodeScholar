# Ambience: an operating system for IoT microservices

## Access

| Field | Value |
|-------|-------|
| DOI | `10.55056/jec.786` |
| Full Paper | [https://doi.org/10.55056/jec.786](https://doi.org/10.55056/jec.786) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/14bd71dbdc373172d0b9bae354dd085fab38574f](https://www.semanticscholar.org/paper/14bd71dbdc373172d0b9bae354dd085fab38574f) |
| Source | [https://journalclub.io/episodes/ambience-an-operating-system-for-iot-microservices](https://journalclub.io/episodes/ambience-an-operating-system-for-iot-microservices) |
| Source | [https://www.semanticscholar.org/paper/14bd71dbdc373172d0b9bae354dd085fab38574f](https://www.semanticscholar.org/paper/14bd71dbdc373172d0b9bae354dd085fab38574f) |
| Year | 2026 |
| Citations | 3 |
| Authors | F. Bakir, Sierra Wang, Tyler Ekaireb, Jack Pearson, C. Krintz, Rich Wolski |
| Paper ID | `24efc9aa-a26b-4665-97b3-a11b7ca11e1a` |

## Classification

- **Problem Type:** operating system design for IoT microservices
- **Domain:** Software Engineering
- **Sub-domain:** Operating Systems for IoT
- **Technique:** Ambience
- **Technique Category:** framework
- **Type:** novel

## Summary

Ambience is a novel operating system designed specifically for IoT microservices, addressing the challenges of heterogeneity and resource constraints in IoT environments. Engineers should care because it enables efficient deployment and management of microservices across a wide range of hardware, from microcontrollers to servers.

## Key Contribution

**Ambience provides a unified operating system abstraction for IoT microservices that optimizes resource usage and performance across diverse hardware platforms.**

## Problem

The need for a common operating system that can efficiently manage microservices across a wide range of resource-constrained IoT devices and traditional cloud infrastructure.

## Method

**Approach:** Ambience operates by providing a set of abstractions that allow microservices to be deployed flexibly across various hardware platforms. It utilizes deployment-time determination of isolation boundaries, asynchronous computational models, and typed system calls to optimize performance.

**Algorithm:**

1. 1. Define microservices with strongly typed interfaces using an interface definition language (IDL).
2. 2. Create deployment manifests that specify service dependencies, network topologies, and security isolation groups.
3. 3. Compile custom kernel images for each target node based on the deployment manifest.
4. 4. Assign microservices to groups for shared address space or isolation based on deployment requirements.
5. 5. Utilize zero-copy IPC for communication within groups and RPC for communication between groups.

**Input:** Deployment manifests written in a Domain Specific Language (DSL) embedded in Python, defining services, dependencies, and network configurations.

**Output:** Custom kernel images for each node that instantiate the specified microservices and their configurations.

**Key Parameters:**

- `service_instance: {name: 'detection', service: tf_lite_detection}`
- `network: {udp-internet: 4898}`
- `group: {name: 'camera_group', services: ['detection', 'camera']}`

**Complexity:** Not stated

## Benchmarks

**Tested on:** End-to-end IoT application for wildlife monitoring

**Results:**

- Throughput: hundreds of thousands of requests per second
- Latency: lower per-request latencies compared to Tock

**Compared against:** Linux operating system, Azure IoT platform, Tock embedded operating system

**Improvement:** Ambience achieves one to three orders of magnitude better efficiency compared to Linux and Azure IoT, and up to 7x greater throughput than Tock.

## Implementation Guide

**Data Structures:** Deployment manifests, Service groups, Custom kernel images

**Dependencies:** Python for writing deployment manifests, Ambience framework for deployment

**Core Operation:**

```python
compile_and_deploy(manifest): create_kernel_image(manifest) -> deploy_to_nodes(kernel_image)
```

**Watch Out For:**

- Ensure that service dependencies are correctly defined in the manifest to avoid runtime errors.
- Be cautious of resource constraints on microcontrollers when defining service groups.
- Avoid hardcoding isolation decisions; leverage Ambience's deployment-time flexibility.

## Use This When

- Building IoT applications that require efficient resource management across heterogeneous devices.
- Developing microservices that need to be deployed on both low-resource microcontrollers and high-performance servers.
- Needing a flexible isolation model for microservices that can adapt at deployment time.

## Don't Use When

- Developing applications that require POSIX compatibility.
- When a general-purpose operating system is needed for non-IoT applications.
- In scenarios where existing middleware solutions are sufficient.

## Key Concepts

microservices, typed interfaces, asynchronous communication, deployment manifests, resource optimization, capability-based access control

## Connects To

- Kubernetes
- Serverless computing
- Unikernels
- Tock operating system

## Prerequisites

- Understanding of microservices architecture
- Familiarity with operating system concepts
- Knowledge of IoT device constraints

## Limitations

- Not a general-purpose OS; lacks POSIX compatibility
- May require specific hardware support for optimal performance
- Complexity in defining deployment manifests for large applications

## Open Questions

- How can Ambience be extended to support more complex security models?
- What are the implications of using Ambience in highly dynamic IoT environments?

## Abstract

Why embark on any of this at all? What problem are they actually solving? What unmet need is there that they’re trying to fill? The first thing to know is that we're not talking about microservices running on big servers or the public cloud (AWS, GCP, etc.). We're talking about microservices running in highly resource-constrained environments, specifically IoT devices. This could be a smart thermostat, a wearable health tracker, a factory floor sensor, or a wildlife monitoring system. Either way, don't think of the playing field as a big hulky processors with a ton of horsepower and memory. It's the opposite of that.
