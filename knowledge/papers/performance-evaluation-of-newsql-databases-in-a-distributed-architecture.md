# Performance Evaluation of NewSQL Databases in a Distributed Architecture

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1109/ACCESS.2025.3529740` |
| Full Paper | [https://doi.org/10.1109/ACCESS.2025.3529740](https://doi.org/10.1109/ACCESS.2025.3529740) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/eb2498d0fd475efcc5f20a58ff5b6c0bbb20f77e](https://www.semanticscholar.org/paper/eb2498d0fd475efcc5f20a58ff5b6c0bbb20f77e) |
| Source | [https://journalclub.io/episodes/performance-evaluation-of-newsql-databases-in-a-distributed-architecture](https://journalclub.io/episodes/performance-evaluation-of-newsql-databases-in-a-distributed-architecture) |
| Source | [https://www.semanticscholar.org/paper/eb2498d0fd475efcc5f20a58ff5b6c0bbb20f77e](https://www.semanticscholar.org/paper/eb2498d0fd475efcc5f20a58ff5b6c0bbb20f77e) |
| Year | 2026 |
| Citations | 2 |
| Authors | Zhiyao Zhang, Alan Megargel, Lingxiao Jiang |
| Paper ID | `638be2d9-9e6a-484e-9161-a13de14c126b` |

## Classification

- **Problem Type:** distributed database consistency
- **Domain:** Database Systems
- **Sub-domain:** NewSQL databases
- **Technique:** NewSQL performance evaluation
- **Technique Category:** framework
- **Type:** comparison

## Summary

This paper evaluates the performance of NewSQL databases within distributed architectures, highlighting their ability to maintain ACID compliance while achieving scalability. Engineers should care because NewSQL offers a solution for applications requiring strong consistency without sacrificing performance.

## Key Contribution

**A comprehensive performance evaluation of NewSQL databases in distributed environments, demonstrating their advantages over NoSQL systems.**

## Problem

The need for reliable, consistent data in distributed systems that often sacrifice consistency for performance.

## Method

**Approach:** The method involves benchmarking various NewSQL databases under distributed conditions to assess their performance metrics while maintaining ACID properties. This includes measuring latency, throughput, and consistency levels across different workloads.

**Algorithm:**

1. 1. Select a set of NewSQL databases for evaluation.
2. 2. Define a range of distributed workloads simulating real-world applications.
3. 3. Measure performance metrics such as latency and throughput under each workload.
4. 4. Analyze the consistency guarantees provided by each database during the tests.
5. 5. Compare results against traditional relational and NoSQL databases.

**Input:** Distributed workloads simulating various application scenarios.

**Output:** Performance metrics including latency, throughput, and consistency levels.

**Key Parameters:**

- `workload_type: transactional, analytical`
- `node_count: 3-10`
- `data_size: 1GB-10TB`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Synthetic workloads designed to mimic real-world applications

**Results:**

- latency: measured in milliseconds
- throughput: transactions per second
- consistency: ACID compliance levels

**Compared against:** Traditional relational databases, NoSQL databases

**Improvement:** Demonstrated improved consistency and performance metrics compared to NoSQL systems.

## Implementation Guide

**Data Structures:** Distributed transaction logs, Performance metrics storage

**Dependencies:** Database management systems (NewSQL), Benchmarking tools (e.g., YCSB, SysBench)

**Core Operation:**

```python
for each database in NewSQL_databases: measure_performance(workload)
```

**Watch Out For:**

- Ensure proper configuration of database nodes for accurate results
- Be aware of network latency affecting performance measurements
- Consider the impact of varying workloads on consistency guarantees

## Use This When

- Building applications requiring strong consistency in distributed environments
- Evaluating database options for high-performance transactional systems
- Migrating from traditional databases to more scalable solutions

## Don't Use When

- Applications that can tolerate eventual consistency
- Use cases focused solely on high availability without strict consistency
- Small-scale applications where simplicity is prioritized over performance

## Key Concepts

ACID compliance, distributed transactions, performance benchmarking, scalability, latency, throughput

## Connects To

- ACID properties
- NoSQL databases
- Distributed systems
- Performance benchmarking frameworks
- Database scalability techniques

## Prerequisites

- Understanding of database architectures
- Familiarity with ACID vs BASE models
- Knowledge of distributed systems principles

## Limitations

- Performance may vary significantly based on workload type
- Not all NewSQL databases are created equal in terms of performance
- Limited real-world case studies compared to NoSQL

## Open Questions

- How do NewSQL databases perform under extreme load conditions?
- What are the long-term implications of using NewSQL in rapidly evolving application environments?

## Abstract

Where NewSQL diverges from NoSQL is in its treatment of consistency. NoSQL databases were developed to solve the scalability limitations of relational databases. Most of them accomplish this by relaxing strict consistency guarantees in favor of availability, partitioning, and performance. Rather than focusing on ACID, they often follow a model called BASE: Basically Available, Soft state, Eventually consistent. BASE allows nodes in a distributed system to return slightly outdated data in exchange for lower latency and higher throughput. While this works well for applications like social media feeds and real-time analytics, it presents serious challenges for use cases that require precise, immediate consistency. NewSQL avoids these pitfalls by maintaining ACID compliance, ensuring that distributed transactions are just as reliable as those in a traditional relational
