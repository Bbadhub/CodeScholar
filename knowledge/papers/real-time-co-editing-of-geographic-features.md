# Real-Time Co-Editing of Geographic Features

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3390/ijgi13120441` |
| Full Paper | [https://doi.org/10.3390/ijgi13120441](https://doi.org/10.3390/ijgi13120441) |
| Source | [https://journalclub.io/episodes/real-time-co-editing-of-geographic-features](https://journalclub.io/episodes/real-time-co-editing-of-geographic-features) |
| Year | 2026 |
| Citations | 0 |
| Authors |  |
| Paper ID | `99f2d431-cf27-4ba4-9c40-809e746433d5` |

## Classification

- **Problem Type:** real-time geospatial data co-editing
- **Domain:** Software Engineering
- **Sub-domain:** Geospatial Data Management
- **Technique:** Tentative Operations
- **Technique Category:** conflict-free replicated data types
- **Type:** novel

## Summary

The paper presents a web-based real-time co-editing system for geospatial features using Conflict-Free Replicated Data Types (CRDTs), enabling multiple users to edit geospatial data simultaneously without conflicts. Engineers should care because this approach allows for seamless collaboration in dynamic environments like disaster response, where real-time updates are critical.

## Key Contribution

**Introduction of a novel operation generation technique called 'tentative operations' for CRDTs in geospatial co-editing.**

## Problem

The need for multiple users to collaboratively edit geospatial data in real-time without manual conflict resolution.

## Method

**Approach:** The method uses CRDTs to allow users to edit local copies of geospatial data, which are then merged in real-time using a conflict resolution mechanism. The 'tentative operations' technique generates operations based on the most recent session-wide state to minimize concurrency issues.

**Algorithm:**

1. 1. User performs an edit on their local copy of the geospatial data.
2. 2. Generate a new CRDT element representing the edit.
3. 3. Insert the new element into the local CRDT data structure.
4. 4. Transmit the new element to all other sites.
5. 5. Each site integrates the new element into their local data structure based on the originLeft parameter.
6. 6. Resolve any conflicts using the CRDT's conflict resolution strategies.

**Input:** Geospatial data in the form of linear geometries represented as ordered sets of points.

**Output:** A synchronized state of geospatial data across multiple users' local copies, conflict-free.

**Key Parameters:**

- `max_concurrent_users: 10`
- `update_frequency: 100ms`
- `geometry_type: linear`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Synthetic geospatial data with varying complexity

**Results:**

- Latency: <100ms
- Conflict resolution success rate: 95%

**Compared against:** Traditional optimistic concurrency control methods

**Improvement:** Significant reduction in conflict resolution time compared to traditional methods.

## Implementation Guide

**Data Structures:** CRDT data structure, Ordered set of points

**Dependencies:** YJS or Automerge for CRDT implementation, OpenLayers for geospatial visualization

**Core Operation:**

```python
new_element = generate_CRDT_element(edit); insert_into_local_structure(new_element); transmit_to_sites(new_element);
```

**Watch Out For:**

- Ensure all sites are synchronized before applying edits.
- Handle network latency to avoid conflicts during high concurrency.

## Use This When

- Building applications for real-time collaborative mapping.
- Developing systems for emergency response requiring live data updates.
- Creating tools for crowdsourced geographic information systems.

## Don't Use When

- Working with static geospatial data that does not require real-time updates.
- In scenarios with very low user concurrency (e.g., single-user applications).

## Key Concepts

CRDT, strong eventual consistency, tentative operations, geospatial editing

## Connects To

- Operational Transformation
- NoSQL databases
- WebSocket for real-time communication

## Prerequisites

- Understanding of CRDTs
- Familiarity with geospatial data structures
- Knowledge of JavaScript

## Limitations

- Performance may degrade with very high concurrency
- Complexity in handling higher-level geospatial operations

## Open Questions

- How to optimize CRDTs for more complex geospatial features?
- What are the best practices for integrating CRDTs with existing GIS systems?

## Abstract

There are two broad categories of CRDTs: state-based and operation-based. In state-based CRDTs, each replica periodically shares its entire state with others, and a merge function is used to combine different states into a unified, conflict-free version. The merge function is designed to be idempotent (meaning that applying it multiple times has the same effect as applying it once), associative (meaning that the order of merging does not matter), and commutative (merging in different sequences leads to the same result). Operation-based CRDTs, in contrast, rely on propagating individual operations rather than entire states. Each operation is designed to be deterministic and to produce the same effect across all replicas, provided that it is delivered in causal order. This reduces the amount of data that needs to be transmitted. So in practice, operation-based CRDTs are
