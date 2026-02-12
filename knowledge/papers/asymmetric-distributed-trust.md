# Asymmetric Distributed Trust

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1007/s00446-024-00469-1` |
| Full Paper | [https://doi.org/10.1007/s00446-024-00469-1](https://doi.org/10.1007/s00446-024-00469-1) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/757e2fdd0f938f9ea6b14bfe74cf764f4aade768](https://www.semanticscholar.org/paper/757e2fdd0f938f9ea6b14bfe74cf764f4aade768) |
| Source | [https://journalclub.io/episodes/asymmetric-distributed-trust](https://journalclub.io/episodes/asymmetric-distributed-trust) |
| Source | [https://www.semanticscholar.org/paper/757e2fdd0f938f9ea6b14bfe74cf764f4aade768](https://www.semanticscholar.org/paper/757e2fdd0f938f9ea6b14bfe74cf764f4aade768) |
| Year | 2026 |
| Citations | 45 |
| Authors | C. Cachin, Björn Tackmann |
| Paper ID | `7d058599-1968-431e-9ff1-e09e756f151f` |

## Classification

- **Problem Type:** Byzantine fault tolerance in distributed systems
- **Domain:** Networking & Distributed Systems
- **Sub-domain:** Byzantine fault tolerance
- **Technique:** Asymmetric Byzantine Quorum Systems
- **Technique Category:** framework
- **Type:** novel

## Summary

The paper introduces asymmetric Byzantine quorum systems that allow processes in a distributed system to have subjective trust assumptions, enabling protocols for reliable broadcasts, shared memory, and consensus under Byzantine faults. Engineers should care because this approach enhances the flexibility and robustness of distributed systems by accommodating varying trust levels among nodes.

## Key Contribution

**Introduction of asymmetric Byzantine quorum systems that generalize traditional symmetric quorum systems to model subjective trust.**

## Problem

The need for distributed systems to maintain consensus and functionality even when some nodes are faulty or malicious.

## Method

**Approach:** The method formalizes asymmetric Byzantine quorum systems where each process can define its own trust assumptions about other processes. It introduces protocols for shared memory, reliable broadcasts, and consensus that leverage these asymmetric quorums.

**Algorithm:**

1. 1. Define a fail-prone system for each process based on its trust assumptions.
2. 2. Construct local quorum systems for each process that satisfy consistency and availability conditions.
3. 3. Implement protocols for shared memory and broadcast using the defined quorums.
4. 4. Extend a randomized binary consensus protocol to work with asymmetric trust.
5. 5. Ensure that safety is guaranteed for wise processes and liveness depends on the presence of a sufficient number of wise processes.

**Input:** A set of processes with defined trust assumptions and communication links.

**Output:** Consensus decisions, reliable broadcasts, and shared memory states.

**Key Parameters:**

- `n: number of processes`
- `f: maximum number of faulty processes (typically f < n/3 for traditional systems)`
- `local_quorum_size: varies based on trust assumptions`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Simulated distributed systems with varying numbers of processes and fault scenarios.

**Results:**

- Safety and liveness guarantees, message complexity, time complexity.

**Compared against:** Traditional symmetric Byzantine quorum systems.

**Improvement:** The protocols ensure safety for wise processes and improve liveness conditions compared to traditional models.

## Implementation Guide

**Data Structures:** Process set, quorum sets, message queues

**Dependencies:** Distributed computing libraries, consensus libraries

**Core Operation:**

```python
for each process p in P: define local_quorum(p) based on trust assumptions; implement consensus using local_quorum.
```

**Watch Out For:**

- Ensure that local quorum definitions are consistent across processes.
- Watch for scenarios where naive processes may block progress.
- Test thoroughly under various fault conditions to validate safety and liveness.

## Use This When

- Building decentralized applications that require flexible trust models.
- Implementing consensus protocols in permissioned blockchain systems.
- Designing distributed systems where nodes may have different trust levels.

## Don't Use When

- The system requires uniform trust assumptions across all nodes.
- Performance is critical and the overhead of asymmetric trust is unacceptable.
- The application domain does not involve Byzantine faults.

## Key Concepts

Byzantine fault tolerance, quorum systems, subjective trust, distributed consensus, asynchronous protocols

## Connects To

- Federated Byzantine quorum systems (FBQS)
- Traditional Byzantine quorum systems
- Consensus algorithms like PBFT and HotStuff

## Prerequisites

- Understanding of Byzantine fault tolerance concepts
- Familiarity with distributed systems and consensus protocols
- Knowledge of quorum systems and their properties

## Limitations

- Safety guarantees are only provided for wise processes.
- Liveness depends on the presence of a sufficient number of wise processes.
- Increased complexity in protocol design compared to symmetric models.

## Open Questions

- How to optimize the performance of protocols under asymmetric trust?
- What are the implications of asymmetric trust in larger, more complex distributed systems?

## Abstract

If you've worked on a distributed system before, you might have encountered the concept of Byzantine fault tolerance (BFT). It’s the ability of a decentralized network to function and continue to reach consensus even after some nodes fail. It also works if those nodes are acting maliciously, or for some other reason can’t be trusted at the moment. It involves something called Byzantine quorum systems, where you need agreement from a certain number of nodes (but not all the nodes) before you trust a decision.
