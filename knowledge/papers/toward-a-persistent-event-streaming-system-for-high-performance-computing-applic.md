# Toward a persistent event-streaming system for high-performance computing applications

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3389/fhpcp.2025.1638203` |
| Full Paper | [https://doi.org/10.3389/fhpcp.2025.1638203](https://doi.org/10.3389/fhpcp.2025.1638203) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/bdcd3e7f4891c34b40acf11773ddac316d93f764](https://www.semanticscholar.org/paper/bdcd3e7f4891c34b40acf11773ddac316d93f764) |
| Source | [https://journalclub.io/episodes/toward-a-persistent-event-streaming-system-for-high-performance-computing-applications](https://journalclub.io/episodes/toward-a-persistent-event-streaming-system-for-high-performance-computing-applications) |
| Source | [https://www.semanticscholar.org/paper/bdcd3e7f4891c34b40acf11773ddac316d93f764](https://www.semanticscholar.org/paper/bdcd3e7f4891c34b40acf11773ddac316d93f764) |
| Year | 2026 |
| Citations | 3 |
| Authors | Matthieu Dorier, Amal Gueroudji, Valérie Hayot-Sasson, H. Nguyen, Seth Ockerman, Renan Souza |
| Paper ID | `28fbfdd7-c5c7-4f52-9f4d-e63f480ef429` |

## Classification

- **Problem Type:** event-streaming for high-performance computing
- **Domain:** Software Engineering
- **Sub-domain:** Event-Driven Architectures
- **Technique:** Mofka
- **Technique Category:** framework
- **Type:** novel

## Summary

The paper introduces Mofka, a persistent event-streaming framework specifically designed for high-performance computing (HPC) applications, addressing the limitations of traditional parallel file systems. Engineers should care because Mofka significantly improves data handling and communication efficiency in complex HPC workflows, achieving up to 8× throughput improvement over existing solutions like Kafka and Redpanda.

## Key Contribution

**Mofka provides a high-performance, modular event-streaming framework tailored for HPC environments, leveraging advanced networking and data handling techniques.**

## Problem

HPC applications generate vast amounts of data that require efficient management and communication, which traditional file systems struggle to handle effectively.

## Method

**Approach:** Mofka divides events into metadata and data parts, optimizing the transfer of each. It uses RDMA for high-speed data transfers and supports large payloads, making it suitable for HPC workloads.

**Algorithm:**

1. 1. Producer creates a topic with a validator, partition selector, and serializer.
2. 2. Producer batches metadata and sends it to the partition manager.
3. 3. Partition manager redirects metadata to a log provider and RDMA handles for data to a storage provider.
4. 4. Consumer subscribes to partitions and receives metadata batches.
5. 5. Consumer uses a data selector to specify which data parts to retrieve.
6. 6. Data broker transfers the selected data directly to the consumer's memory.

**Input:** Events consisting of metadata (small, structured) and data (large, scientific payloads).

**Output:** Streamed events with metadata and selected data parts.

**Key Parameters:**

- `batch_size: 128`
- `number_of_threads: 4`

**Complexity:** not stated

## Benchmarks

**Tested on:** Argonne’s Polaris supercomputer, Oak Ridge’s Frontier supercomputer

**Results:**

- throughput: up to 8× improvement over Kafka and Redpanda

**Compared against:** Kafka, Redpanda

**Improvement:** 8× improvement in throughput in some scenarios

## Implementation Guide

**Data Structures:** topic handle, partition manager, log provider, data broker

**Dependencies:** Mochi suite components, RDMA-capable network

**Core Operation:**

```python
producer.push(metadata, data) to send events; consumer.pull() to retrieve events.
```

**Watch Out For:**

- Ensure proper configuration of validators and serializers for metadata.
- Monitor network usage to avoid bottlenecks with multiple NICs.
- Handle large payloads carefully to optimize memory usage.

## Use This When

- You need to manage large data streams in HPC applications.
- You require high throughput and low latency for data transfer in scientific workflows.
- You want to leverage advanced networking capabilities of HPC systems.

## Don't Use When

- Your application does not require persistence of data.
- You are working with small, structured messages typical in enterprise contexts.
- You need a solution that is not tailored for HPC environments.

## Key Concepts

event-driven architecture, persistent streaming, RDMA, HPC data management

## Connects To

- Kafka
- Redpanda
- Mochi suite
- HPC data services

## Prerequisites

- Understanding of event-driven architectures
- Familiarity with HPC systems
- Knowledge of RDMA networking

## Limitations

- Not suitable for applications requiring strict file consistency.
- May require significant configuration for optimal performance.
- Limited to environments that support the Mochi suite.

## Open Questions

- How can Mofka be extended to support more diverse data formats?
- What optimizations can be made for even larger-scale HPC applications?

## Abstract

You’ve undoubtedly heard of Kafka: the distributed streaming platform that lets you capture, process, and replay events. But what about Mofka? Have you heard of that? Probably not, because it just got invented. And this is the paper in which it's making its debut. So what is Mofka?
