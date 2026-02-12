# Macroswarm: A field-based compositional framework for swarm programming

## Access

| Field | Value |
|-------|-------|
| DOI | `10.46298/LMCS-21(3:13)2025` |
| Full Paper | [https://doi.org/10.46298/LMCS-21(3:13)2025](https://doi.org/10.46298/LMCS-21(3:13)2025) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/70a51786800a322c48e2b4d726c349e72908d307](https://www.semanticscholar.org/paper/70a51786800a322c48e2b4d726c349e72908d307) |
| Source | [https://journalclub.io/episodes/macroswarm-a-field-based-compositional-framework-for-swarm-programming](https://journalclub.io/episodes/macroswarm-a-field-based-compositional-framework-for-swarm-programming) |
| Source | [https://www.semanticscholar.org/paper/70a51786800a322c48e2b4d726c349e72908d307](https://www.semanticscholar.org/paper/70a51786800a322c48e2b4d726c349e72908d307) |
| Year | 2026 |
| Citations | 17 |
| Authors | G. Aguzzi, Roberto Casadei, Mirko Viroli |
| Paper ID | `87a9402b-b1ca-4f20-ba69-d2e466b4553c` |

## Classification

- **Problem Type:** swarm programming
- **Domain:** Software Engineering
- **Sub-domain:** Swarm Programming
- **Technique:** MacroSwarm
- **Technique Category:** framework
- **Type:** novel

## Summary

MacroSwarm is a field-based compositional framework for swarm programming that enables the design and implementation of complex swarm behaviors through reusable functional blocks. Engineers should care because it provides a formal API for programming decentralized swarm behaviors, ensuring robustness and resilience in dynamic environments.

## Key Contribution

**The design and implementation of MacroSwarm, a framework that formalizes swarm programming with self-stabilization properties for resilience.**

## Problem

The need for effective design and implementation methods for coordinating computation and action within groups of simple agents to achieve complex global goals.

## Method

**Approach:** MacroSwarm models swarm behavior as an augmented event structure, where each device performs a sense-compute-interact loop. This allows for decentralized coordination and the expression of swarm behaviors as pure functions.

**Algorithm:**

1. 1. Each device senses the environment and gathers messages from neighbors.
2. 2. The device computes new values based on the sensed data.
3. 3. The device decides on actions and interacts by sending messages and performing actuations.
4. 4. This process is repeated in a loop for all devices in the swarm.

**Input:** Sensor data from the environment and messages from neighboring devices.

**Output:** Actuation commands and updated state information for each device.

**Key Parameters:**

- `message_expiration_threshold: configurable based on application needs`
- `sensing_interval: configurable, typically in milliseconds`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Simulated environments for flocking, pattern formation, and collective decision-making.

**Results:**

- Robustness under adversarial conditions, self-stabilization properties.

**Compared against:** Existing swarm programming frameworks and methods.

**Improvement:** Demonstrated resilience and robustness in dynamic environments compared to traditional methods.

## Implementation Guide

**Data Structures:** Event structures, Sensing fields, Actuation fields

**Dependencies:** ScaFi framework, Scala programming language

**Core Operation:**

```python
for device in swarm: sense(); compute(); interact();
```

**Watch Out For:**

- Ensure proper configuration of message expiration thresholds.
- Monitor the sensing interval to balance responsiveness and resource usage.

## Use This When

- Designing decentralized systems with multiple interacting agents.
- Implementing complex swarm behaviors like flocking or pattern formation.
- Developing applications that require resilience to environmental changes.

## Don't Use When

- When centralized control is preferred for simplicity.
- For applications with very low resource constraints where overhead is critical.

## Key Concepts

self-stabilization, field-based coordination, aggregate computing, decentralized control, compositionality, swarm behavior blocks

## Connects To

- Aggregate computing
- Field calculus
- Decentralized control systems
- Self-organizing systems

## Prerequisites

- Understanding of decentralized algorithms
- Familiarity with swarm intelligence concepts
- Basic knowledge of functional programming

## Limitations

- Performance may degrade with very large swarms due to communication overhead.
- Requires a proper understanding of the underlying ScaFi framework for effective implementation.

## Open Questions

- How can MacroSwarm be extended to support more complex swarm behaviors?
- What are the implications of varying network topologies on swarm performance?

## Abstract

The system models the swarm as what researchers call an augmented event structure, where each event represents a round of three sub-events in a loop: sense-compute-interact. This loop is performed by a specific device at a specific point in time and space. In fact, it’s performed by every device, all at once. Each device: senses the environment, gathers messages from neighbors, computes new values and decides on actions, then interacts by sending messages and performing actuations.
