# Improving Performance of Key–Value Stores for High-Performance Storage Devices

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3390/app14177538` |
| Full Paper | [https://doi.org/10.3390/app14177538](https://doi.org/10.3390/app14177538) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/7dc272b2a127bb1eae5d02852f1fe8f2f6597ecf](https://www.semanticscholar.org/paper/7dc272b2a127bb1eae5d02852f1fe8f2f6597ecf) |
| Source | [https://journalclub.io/episodes/improving-performance-of-keyvalue-stores-for-high-performance-storage-devices](https://journalclub.io/episodes/improving-performance-of-keyvalue-stores-for-high-performance-storage-devices) |
| Source | [https://www.semanticscholar.org/paper/7dc272b2a127bb1eae5d02852f1fe8f2f6597ecf](https://www.semanticscholar.org/paper/7dc272b2a127bb1eae5d02852f1fe8f2f6597ecf) |
| Year | 2026 |
| Citations | 0 |
| Authors | Sunggon Kim, Hwajung Kim |
| Paper ID | `13ca2116-c3e3-4d75-9c5c-de84fd912469` |

## Classification

- **Problem Type:** I/O performance optimization in key-value stores
- **Domain:** Software Engineering
- **Sub-domain:** Key-Value Stores
- **Technique:** Multi-threaded compaction operation
- **Technique Category:** optimization_algorithm
- **Type:** novel

## Summary

The authors analyze the performance of key-value stores (KV stores) like RocksDB on high-performance storage devices and propose a multi-threaded compaction operation to improve I/O performance. This work is crucial for engineers looking to optimize database performance on modern hardware, as it reveals significant performance gaps and provides a solution to leverage multi-core CPUs effectively.

## Key Contribution

**Introduction of a multi-threaded compaction operation that utilizes idle threads to enhance I/O performance in key-value stores.**

## Problem

The performance of existing key-value stores is significantly below the potential of high-performance storage devices due to inefficient I/O operations.

## Method

**Approach:** The method involves analyzing the I/O operations of RocksDB and identifying bottlenecks caused by coarse-grained locking mechanisms. By enabling idle threads to participate in I/O operations, the proposed scheme parallelizes the compaction process, thus improving overall performance.

**Algorithm:**

1. Identify target files for compaction.
2. Allocate a temporary read buffer.
3. Engage idle threads to read target files into the read buffer.
4. Sort and merge the data from the read buffer.
5. Write the output files back to storage.

**Input:** Key-value pairs stored in RocksDB, with a focus on the files involved in the compaction process.

**Output:** Improved I/O performance metrics for the KV store.

**Key Parameters:**

- `max_background_flushes: 1`
- `max_background_compactions: 1, 2, 4`
- `threads: 1 (default), 2, 4, 8, 16`

**Complexity:** Not stated

## Benchmarks

**Tested on:** db_bench benchmark with fillrandom workload

**Results:**

- Throughput (MB/s)

**Compared against:** Standard RocksDB implementation without multi-threaded compaction

**Improvement:** Up to 16% improvement in performance over the standard RocksDB implementation.

## Implementation Guide

**Data Structures:** ReadQueue (global data structure for managing files to read)

**Dependencies:** RocksDB version 5.13, Linux kernel 4.17.0, ext4 file system

**Core Operation:**

```python
while not queue.is_empty(): select_file_to_prefetch(); read_file_into_buffer();
```

**Watch Out For:**

- Ensure proper locking mechanisms to avoid race conditions when accessing the ReadQueue.
- Monitor thread contention to prevent performance degradation with too many threads.
- Test performance with varying numbers of threads to find the optimal configuration.

## Use This When

- You need to optimize the performance of a key-value store on multi-core CPUs.
- You are working with high-performance storage devices like NVMe SSDs.
- You want to reduce I/O stalls caused by background operations in RocksDB.

## Don't Use When

- Your application does not require high-performance I/O operations.
- You are using a single-core CPU or low-performance storage devices.
- The overhead of managing multiple threads outweighs the performance benefits.

## Key Concepts

key-value stores, I/O operations, multi-threading, compaction, RocksDB, NVMe SSD

## Connects To

- FASTER (concurrent key-value store)
- IceFS (optimized file system)
- SpanFS (journaling file system optimization)
- MAX (multi-core-friendly log-structured file system)

## Prerequisites

- Understanding of key-value store architectures.
- Familiarity with multi-threading concepts.
- Knowledge of I/O operations and performance metrics.

## Limitations

- The proposed scheme may not be effective for single-threaded workloads.
- Performance gains may vary based on the specific hardware configuration.
- Increased complexity in managing multiple threads may introduce new bugs.

## Open Questions

- How can the proposed scheme be adapted for other types of databases?
- What are the long-term effects of multi-threading on data consistency in KV stores?

## Abstract

We all know that key-value stores are fast. They're fast at reading, they're fast at writing. The question is, could they be faster? Is it theoretically possible that there is still, to this day, a significant gap between their potential maximum, and their realized performance? Today's authors say yes, there is. In this paper they started with a host machine, and they analyzed the performance of the host's underlying storage hardware (NVMe SSD), to determine (at the lowest level) how fast data could actually be fetched-from and written-to disk. Then they setup a key-value store (RocksDB) on that host, then benchmarked reads and writes of that DB against the host's raw performance. Now what you'd expect to see is a little performance hit, explainable by the presence of the database application itself. It needs to run business logic, and that logic takes a little time. Understandable. But what the authors actually found was a far more significant
