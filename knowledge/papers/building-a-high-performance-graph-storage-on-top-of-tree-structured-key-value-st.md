# Building a High-Performance Graph Storage on Top of Tree-Structured Key-Value Stores

## Access

| Field | Value |
|-------|-------|
| DOI | `10.26599/BDMA.2023.9020015` |
| Full Paper | [https://doi.org/10.26599/BDMA.2023.9020015](https://doi.org/10.26599/BDMA.2023.9020015) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/cc918ebb17475034417465c74624933d90c1f333](https://www.semanticscholar.org/paper/cc918ebb17475034417465c74624933d90c1f333) |
| Source | [https://journalclub.io/episodes/building-a-high-performance-graph-storage-on-top-of-tree-structured-key-value-stores](https://journalclub.io/episodes/building-a-high-performance-graph-storage-on-top-of-tree-structured-key-value-stores) |
| Source | [https://www.semanticscholar.org/paper/cc918ebb17475034417465c74624933d90c1f333](https://www.semanticscholar.org/paper/cc918ebb17475034417465c74624933d90c1f333) |
| Year | 2026 |
| Citations | 3 |
| Authors | Heng Lin, Zhiyong Wang, Shipeng Qi, Xiaowei Zhu, Chuntao Hong, Wenguang Chen |
| Paper ID | `ec950773-60fa-452f-85db-447b9851c729` |

## Classification

- **Problem Type:** graph storage optimization
- **Domain:** Software Engineering
- **Sub-domain:** Graph Databases
- **Technique:** TuGraph
- **Technique Category:** framework
- **Type:** novel

## Summary

The paper presents TuGraph, a high-performance graph database built on tree-structured key-value stores, focusing on optimizing storage layout and query performance. Engineers should care because it significantly outperforms existing Graph Database Management Systems (GDBMS) in various benchmarks, particularly in scenarios involving complex graph queries.

## Key Contribution

**Development of TuGraph, a graph database that optimizes storage layout on tree-structured key-value stores for improved performance.**

## Problem

The need for efficient storage and querying of graph data in applications such as social networks, financial risk assessment, and data lineage tracking.

## Method

**Approach:** TuGraph employs a two-layer architecture consisting of a Property Graph storage layer and a key-value storage layer. It optimizes the packing of graph topology and properties to enhance read and write performance, particularly for multi-hop queries.

**Algorithm:**

1. 1. Analyze common access patterns in graph queries.
2. 2. Choose a tree-structured key-value store (LMDB) based on performance benchmarks.
3. 3. Pack graph topology and properties into key-value pairs using adaptive mapping.
4. 4. Implement a concurrent writer to handle multiple write operations efficiently.
5. 5. Optimize read and write operations based on locality and access patterns.

**Input:** Graph data in property graph model format, including vertices and edges with associated properties.

**Output:** Efficiently stored graph data that supports high-performance querying.

**Key Parameters:**

- `threshold_size: 2 KB for mixed mapping, 4 KB for split mapping`
- `read_to_write_ratio: 20:1`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Linked Data Benchmark Council (LDBC) Social Network Benchmark (SNB)

**Results:**

- micro-benchmark performance
- macro-benchmark performance

**Compared against:** Existing GDBMS like Neo4j and TigerGraph

**Improvement:** Significant performance improvements over existing GDBMS, specific values not stated.

## Implementation Guide

**Data Structures:** Property Graph structure, Key-Value pairs for vertices and edges

**Dependencies:** LMDB, Lucene for full-text indexing

**Core Operation:**

```python
def add_edge(src, dst, properties): if not detect_cycle(src, dst): store_edge(src, dst, properties)
```

**Watch Out For:**

- Ensure that the threshold size for adaptive mapping is appropriately set to balance performance.
- Be aware of the limitations of LMDB's single writer when designing for high write loads.

## Use This When

- Building applications that require efficient graph data storage and querying.
- Handling complex multi-hop graph queries in real-time.
- Developing systems that need to support high read-to-write ratios.

## Don't Use When

- When the application requires extensive write operations that exceed the capabilities of a single writer.
- In scenarios where graph data is not the primary focus or is relatively simple.

## Key Concepts

property graph model, adaptive mapping, concurrent writing, key-value storage

## Connects To

- RocksDB
- Neo4j
- TigerGraph
- B+ tree data structures

## Prerequisites

- Understanding of graph data models
- Familiarity with key-value stores
- Knowledge of concurrent programming

## Limitations

- Single writer limitation in LMDB may hinder performance under heavy write loads.
- Performance may degrade if graph data exceeds memory capacity.
- Complexity in managing adaptive mapping and ensuring efficient data access.

## Open Questions

- How can the concurrent writing capabilities be further enhanced?
- What are the implications of using different key-value stores on performance?

## Abstract

Imagine it’s the early 2000s, and you’re working as a Software Engineer at one of the budding social networks of the time. It could be a Facebook, a MySpace, a Friendster, a Twitter, etc. What makes your work special is that you’re part of what’s increasingly being known as “Web 2.0.” Gone are the days of static websites and individual user experiences. This is the dawn of the dynamic web and shared experiences. Social experiences. Your company is not just storing data about users and their individual flows through the application, but also how each user is interacting with each other user. You have new concepts that describe this. For the first time, you have things like “following” and “follower.” You have “friends,” you have “groups” and social circles. You have relationships.
