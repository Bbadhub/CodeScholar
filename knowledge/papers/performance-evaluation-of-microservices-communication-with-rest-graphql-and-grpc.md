# Performance evaluation of microservices communication with REST, GraphQL, and gRPC

## Access

| Field | Value |
|-------|-------|
| DOI | `10.24425/ijet.2024.149562` |
| Full Paper | [https://doi.org/10.24425/ijet.2024.149562](https://doi.org/10.24425/ijet.2024.149562) |
| Source | [https://journalclub.io/episodes/performance-evaluation-of-microservices-communication-with-rest-graphql-and-grpc](https://journalclub.io/episodes/performance-evaluation-of-microservices-communication-with-rest-graphql-and-grpc) |
| Year | 2026 |
| Citations | 0 |
| Authors |  |
| Paper ID | `ae09d5ca-1e5e-4b84-8fe1-ca3ced82f581` |

## Classification

- **Problem Type:** microservices communication performance evaluation
- **Domain:** Software Engineering
- **Sub-domain:** Microservices Architecture
- **Technique:** Performance Evaluation Framework
- **Technique Category:** framework
- **Type:** comparison

## Summary

This paper evaluates the performance of microservices communication using REST, GraphQL, and gRPC, highlighting the strengths and weaknesses of each approach. Engineers should care because understanding these communication methods can significantly impact the efficiency and scalability of microservices architectures.

## Key Contribution

**A comparative analysis of REST, GraphQL, and gRPC performance in microservices communication.**

## Problem

The need to determine the most efficient communication protocol for microservices in distributed systems.

## Method

**Approach:** The method involves setting up microservices that communicate using REST, GraphQL, and gRPC. Performance metrics such as latency and throughput are measured under various load conditions to compare the efficiency of each protocol.

**Algorithm:**

1. 1. Set up microservices using REST, GraphQL, and gRPC.
2. 2. Define performance metrics to be evaluated (e.g., latency, throughput).
3. 3. Simulate various load conditions on the microservices.
4. 4. Measure and record the performance metrics for each communication method.
5. 5. Analyze the collected data to compare the performance of each protocol.
6. 6. Draw conclusions based on the performance results.

**Input:** Microservices architecture with implemented REST, GraphQL, and gRPC endpoints.

**Output:** Performance metrics including latency and throughput for each communication method.

**Key Parameters:**

- `load_conditions: varying levels of requests`
- `timeout_settings: configurable timeouts for requests`

**Complexity:** not stated

## Benchmarks

**Tested on:** Synthetic load tests simulating various user interactions.

**Results:**

- latency: measured in milliseconds
- throughput: requests per second

**Compared against:** Previous studies on microservices communication performance.

**Improvement:** not stated

## Implementation Guide

**Data Structures:** Service registry, Load balancer, Performance metrics collector

**Dependencies:** Microservices framework (e.g., Spring Boot, Express.js), gRPC library, GraphQL library

**Core Operation:**

```python
measure_performance(protocol): setup_microservice(protocol); simulate_load(); return collect_metrics();
```

**Watch Out For:**

- Ensure consistent load testing conditions
- Monitor network latency separately
- Consider the overhead of each protocol

## Use This When

- Evaluating communication protocols for new microservices
- Optimizing existing microservices architecture
- Deciding on a communication method for scalability

## Don't Use When

- When the application is monolithic
- If the performance metrics are not critical for the application
- In environments with minimal inter-service communication

## Key Concepts

microservices, REST, GraphQL, gRPC, performance metrics, latency, throughput

## Connects To

- Service Mesh
- API Gateway
- Load Balancing Techniques

## Prerequisites

- Understanding of microservices architecture
- Familiarity with REST, GraphQL, and gRPC
- Basic knowledge of performance testing

## Limitations

- Results may vary based on specific use cases
- Not all performance metrics are covered
- Experimental design may introduce biases

## Open Questions

- How do these protocols perform under extreme load conditions?
- What are the long-term maintenance implications of each protocol?

## Abstract

Now, if you’re like me: alarm bells are already ringing. These shootouts happen all the time, and in many cases the experimental design is seriously flawed. In my opinion, this paper is no exception. So rather than take this article at face value (and report their findings as fact), we’re going to take a more critical lens. I am going to present their research and their findings, but I’ll spend much more time than usual on history and context, and then I'll use that to inform counter-arguments to their analysis. This study is imperfect, but it’s not without value. They did unearth some interesting findings, I just don’t think those findings should be taken at face value; so we won’t. The way we'll get the most out of this paper is through a critical, interrogative lens, so let's do that.
