# A Rule-Based Method for Enhancing Burst Tolerance in Stateful Microservices

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3390/electronics14142752` |
| Full Paper | [https://doi.org/10.3390/electronics14142752](https://doi.org/10.3390/electronics14142752) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/59436d594e77f04497767d074fc4ed9c10d5ed7b](https://www.semanticscholar.org/paper/59436d594e77f04497767d074fc4ed9c10d5ed7b) |
| Source | [https://journalclub.io/episodes/a-rule-based-method-for-enhancing-burst-tolerance-in-stateful-microservices](https://journalclub.io/episodes/a-rule-based-method-for-enhancing-burst-tolerance-in-stateful-microservices) |
| Source | [https://www.semanticscholar.org/paper/59436d594e77f04497767d074fc4ed9c10d5ed7b](https://www.semanticscholar.org/paper/59436d594e77f04497767d074fc4ed9c10d5ed7b) |
| Year | 2026 |
| Citations | 0 |
| Authors | Kestutis Pakrijauskas, D. Mažeika |
| Paper ID | `dc441cd0-613f-4d15-8cb9-799056db76bd` |

## Classification

- **Problem Type:** burst workload management in stateful microservices
- **Domain:** Software Engineering
- **Sub-domain:** Microservices Architecture
- **Technique:** Rule-Based Burst Tolerance Method
- **Technique Category:** framework
- **Type:** novel

## Summary

The paper presents a rule-based method to enhance burst tolerance in stateful microservices by combining write-scaling and load balancing to distribute workloads across multiple nodes. Engineers should care because this approach reduces failure rates and extends operational time under burst conditions, thereby preserving application availability.

## Key Contribution

**A novel rule-based method for managing burst workloads in stateful microservices through workload distribution and vertical scaling.**

## Problem

Stateful microservices struggle to maintain performance during sudden workload bursts, leading to potential service-level objective (SLO) breaches.

## Method

**Approach:** The method monitors memory usage on stateful microservice nodes and redistributes workloads when memory utilization exceeds a threshold. It vertically scales a node to handle increased demand while balancing the load across remaining nodes.

**Algorithm:**

1. Monitor memory usage on the primary node.
2. If memory exceeds the threshold, disallow new connections to the overloaded node.
3. Direct new connections to a secondary node.
4. Initiate vertical scaling on the overloaded node.
5. Balance the load between remaining nodes based on memory utilization.
6. Transfer existing connections to the newly scaled node once ready.

**Input:** Memory utilization metrics from stateful microservice nodes.

**Output:** Redistributed workloads and scaled nodes ready to handle burst requests.

**Key Parameters:**

- `memory_threshold: 85-95%`
- `memory_increase: 10-25%`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Synthetic dataset generated using Yahoo! Cloud Serving Benchmark (YCSB) with 100,000 records.

**Results:**

- Operational time under burst, number of failed requests.

**Compared against:** Out-of-the-box functionality of MySQL Galera cluster.

**Improvement:** The proposed method sustains burst load for nearly twice as long while reducing failure rates.

## Implementation Guide

**Data Structures:** Database cluster setup for Multi-Primary replication, Connection pool for low-latency connections, Proxy layer for request routing

**Dependencies:** Kubernetes, MySQL Galera Cluster, ProxySQL

**Core Operation:**

```python
if memory_usage > threshold: disallow_connections(primary_node); scale_up(secondary_node); balance_load(nodes);
```

**Watch Out For:**

- Ensure proper configuration of the database proxy to handle connection routing.
- Monitor memory usage accurately to avoid premature scaling.
- Test the system under various burst scenarios to validate performance.

## Use This When

- Handling unpredictable spikes in user activity.
- Managing resource allocation in cloud-based microservices.
- Ensuring high availability during burst workloads.

## Don't Use When

- Predictable workloads that do not require dynamic scaling.
- When historical data is available for accurate workload prediction.
- In environments where resource overprovisioning is acceptable.

## Key Concepts

stateful microservices, burst workload, load balancing, vertical scaling, resource management, SLOs, database proxy

## Connects To

- Kubernetes orchestration techniques
- Load balancing algorithms
- Multi-Primary database architectures

## Prerequisites

- Understanding of microservices architecture
- Knowledge of database management systems
- Familiarity with Kubernetes and container orchestration

## Limitations

- Requires a minimum of three nodes in the cluster.
- Dependent on accurate memory utilization metrics.
- May not perform well under extreme resource constraints.

## Open Questions

- How can this method be optimized with machine learning predictions?
- What are the impacts of different database architectures on burst tolerance?

## Abstract

Stateful microservices hold onto session-related data. So ensuring consistent performance means more intensive and fine-grained resource management. When subjected to bursts, they must continue to process incoming requests, manage data caching, and maintain user session integrity. A failure anywhere in this chain can lead to performance bottlenecks, increased latency, and ultimately, a failure to meet service-level objectives (SLOs). So how do people normally handle this? Well, a common approach is simply to overprovision your resources. Spin up more than you need now, and ideally more than you’d need even in a reasonable burst. By having additional resources on standby, you’re raising the likelihood that you’ll be able to handle peak loads when they come. Now obviously, this approach has its costs. Maintaining idle resources impacts operating expenses and increases the carbon footprint of your system. And that’s even the case when the system is underutilized. Having it sit idle doesn’t mean it isn’t burning through power and racking up the charges.
