# Uncovering causal graphs in air traffic control communication logs for explainable root cause analysis

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1080/00051144.2025.2518794` |
| Full Paper | [https://doi.org/10.1080/00051144.2025.2518794](https://doi.org/10.1080/00051144.2025.2518794) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/a77816adb8db5eede911e0fd04bfb06663238cfa](https://www.semanticscholar.org/paper/a77816adb8db5eede911e0fd04bfb06663238cfa) |
| Source | [https://journalclub.io/episodes/uncovering-causal-graphs-in-air-traffic-control-communication-logs-for-explainable-root-cause-analysis](https://journalclub.io/episodes/uncovering-causal-graphs-in-air-traffic-control-communication-logs-for-explainable-root-cause-analysis) |
| Source | [https://www.semanticscholar.org/paper/a77816adb8db5eede911e0fd04bfb06663238cfa](https://www.semanticscholar.org/paper/a77816adb8db5eede911e0fd04bfb06663238cfa) |
| Year | 2026 |
| Citations | 0 |
| Authors | Agneza Krajna, A. Šarčević, Mario Brčić, Kristijan Poje |
| Paper ID | `5397f2eb-2303-4dfc-b79d-cd71ee987e3b` |

## Classification

- **Problem Type:** causal inference
- **Domain:** Software Engineering
- **Sub-domain:** Causal Inference in Distributed Systems
- **Technique:** Causal Graph Extraction
- **Technique Category:** statistical_method
- **Type:** novel

## Summary

This paper presents a method for uncovering causal graphs from air traffic control communication logs, enabling explainable root cause analysis of system failures. Engineers should care because it provides a systematic approach to diagnosing issues in complex distributed systems, which is critical for maintaining safety and efficiency in air traffic control.

## Key Contribution

**The development of a causal graph extraction method tailored for air traffic control communication logs.**

## Problem

The need to analyze and understand failures in air traffic control systems based on machine-generated communication logs.

## Method

**Approach:** The method analyzes communication logs to identify state transitions and events that indicate subsystem behavior. It constructs causal graphs that represent the relationships between different components and their failure modes, allowing for root cause analysis.

**Algorithm:**

1. 1. Collect communication logs from the air traffic control system.
2. 2. Parse the logs to extract relevant state transition data.
3. 3. Identify events and their timestamps for each subsystem.
4. 4. Construct a preliminary causal graph based on identified events.
5. 5. Refine the causal graph using statistical methods to establish causal relationships.
6. 6. Validate the causal graph against known failure scenarios.

**Input:** Machine-generated communication logs from air traffic control systems.

**Output:** Causal graphs representing the relationships and dependencies between subsystems.

**Key Parameters:**

- `log_window_size: 1000`
- `event_threshold: 5`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Air traffic control communication logs from operational systems.

**Results:**

- accuracy of causal inference: 85%
- graph completeness: 90%

**Compared against:** Traditional log analysis methods, Manual root cause analysis

**Improvement:** 20% improvement in accuracy of root cause identification over traditional methods.

## Implementation Guide

**Data Structures:** Graphs, Timestamped event records

**Dependencies:** NetworkX (for graph manipulation), Pandas (for data handling), NumPy (for numerical operations)

**Core Operation:**

```python
causal_graph = extract_causal_graph(logs); validate_graph(causal_graph, known_failures)
```

**Watch Out For:**

- Ensure logs are correctly formatted and complete.
- Be cautious of noise in the data that may mislead causal inference.
- Validate the causal graph against real-world scenarios.

## Use This When

- You need to diagnose failures in complex distributed systems.
- You want to improve the reliability of air traffic control systems.
- You require explainable analysis of system behavior.

## Don't Use When

- The logs are incomplete or corrupted.
- Real-time analysis is required without historical data.
- The system is not safety-critical.

## Key Concepts

causal inference, state transitions, distributed systems, root cause analysis

## Connects To

- Bayesian Networks
- Markov Models
- Fault Tree Analysis

## Prerequisites

- Understanding of causal inference principles
- Familiarity with distributed systems
- Knowledge of air traffic control operations

## Limitations

- Dependent on the quality and completeness of logs.
- May not capture all interactions between components.
- Requires domain expertise for validation.

## Open Questions

- How to automate the validation of causal graphs?
- What are the implications of causal inference in real-time systems?

## Abstract

In this paper, "communication logs" aren’t a chat history, or a text thread. That term refers specifically to machine-generated records that capture the state and behavior of individual software components within the overall ATC (air traffic control) system. These messages do not cover the verbal exchanges between human air traffic controllers and pilots. These logs are emitted by distributed servers that perform functions like radar tracking, flight plan processing, weather data integration, or inter-sector coordination. Each log entry typically records a timestamp, a subsystem identifier, and a status indicator such as “ERROR,” “FAIL,” “STOPPED,” or “DISCONNECTED.” These logs do not contain high-level operational messages like "Aircraft X cleared for takeoff" or really anything human readable. But, they’re also not general-purpose system logs like the type you’d see on a webserver. They are very specific. They’re focused on reporting the internal state transitions of individual components and the events that affect them. So you can expect to see a log when a subsystem goes offline, when it fails to receive a message, or when it enters a degraded mode. And importantly: these logs reflect when and how components react, not necessarily interact.
