# QUIC and TCP in unsafe networks: A comparative analysis

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1049/smc2.12083` |
| Full Paper | [https://doi.org/10.1049/smc2.12083](https://doi.org/10.1049/smc2.12083) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/c6bd7c6cd33a8fcd4b166b23a920dce63d5d1d48](https://www.semanticscholar.org/paper/c6bd7c6cd33a8fcd4b166b23a920dce63d5d1d48) |
| Source | [https://journalclub.io/episodes/quic-and-tcp-in-unsafe-networks-a-comparative-analysis](https://journalclub.io/episodes/quic-and-tcp-in-unsafe-networks-a-comparative-analysis) |
| Source | [https://www.semanticscholar.org/paper/c6bd7c6cd33a8fcd4b166b23a920dce63d5d1d48](https://www.semanticscholar.org/paper/c6bd7c6cd33a8fcd4b166b23a920dce63d5d1d48) |
| Year | 2026 |
| Citations | 4 |
| Authors | Andrew Simpson, Maitha Alshaali, Wanqing Tu, Muhammad Rizwan Asghar |
| Paper ID | `3eb0d40f-a0af-4fd5-881c-e8713fb23750` |

## Classification

- **Problem Type:** network protocol performance comparison
- **Domain:** Networking & Distributed Systems
- **Sub-domain:** Transport Layer Protocols
- **Technique:** QUIC
- **Technique Category:** protocol
- **Type:** novel

## Summary

This paper compares the performance and security features of QUIC and TCP in unsafe network environments, demonstrating that QUIC offers significant advantages in speed and efficiency. Engineers should care because QUIC's design allows for faster connections and better handling of multiple streams, which can enhance application performance in real-world scenarios.

## Key Contribution

**A comparative analysis highlighting QUIC's superior performance and security features over TCP in unsafe networks.**

## Problem

The need for faster and more secure data transmission protocols in unreliable network conditions motivated this work.

## Method

**Approach:** QUIC combines transport and application-layer functions to reduce latency and improve performance. It achieves this by multiplexing multiple streams over a single connection and minimizing handshake overhead, allowing for faster connection establishment and better adaptation to network conditions.

**Algorithm:**

1. 1. Initiate a QUIC connection using a single UDP packet.
2. 2. Perform a 0-RTT handshake if possible to establish the connection quickly.
3. 3. Multiplex multiple streams over the established connection.
4. 4. Implement built-in congestion control to adapt to network conditions.
5. 5. Handle incoming data streams without head-of-line blocking.
6. 6. Maintain connection migration capabilities for changing network environments.

**Input:** UDP packets containing QUIC connection initiation and data streams.

**Output:** Established QUIC connections with multiplexed streams and reduced latency.

**Key Parameters:**

- `max_streams: 100`
- `initial_rtt: 100ms`
- `congestion_control_algorithm: BBR`

**Complexity:** not stated

## Benchmarks

**Tested on:** Real-world network traffic simulations in unsafe environments.

**Results:**

- latency: 20ms reduction
- throughput: 30% increase

**Compared against:** Standard TCP implementations

**Improvement:** QUIC showed a 30% improvement in throughput and a 20ms reduction in latency compared to TCP.

## Implementation Guide

**Data Structures:** UDP socket, stream buffers, connection state management

**Dependencies:** QUIC libraries (e.g., ngtcp2, quiche), UDP networking stack

**Core Operation:**

```python
establish_quic_connection() { send_initial_packet(); if (0-RTT) { process_streams(); } }
```

**Watch Out For:**

- Ensure proper handling of connection migration to avoid data loss.
- Be aware of the limitations of 0-RTT handshakes in terms of security.
- Monitor for head-of-line blocking issues in multiplexed streams.

## Use This When

- Building applications that require low-latency data transmission.
- Developing services that need to handle multiple streams efficiently.
- Creating applications that operate in unreliable network conditions.

## Don't Use When

- Working in environments where TCP is mandated or required.
- Applications that do not require fast connection establishment.
- Scenarios where legacy support for TCP is critical.

## Key Concepts

UDP, multiplexing, congestion control, 0-RTT handshake, head-of-line blocking, connection migration

## Connects To

- TCP
- TLS
- HTTP/3
- UDP
- Congestion Control Algorithms

## Prerequisites

- Understanding of network protocols
- Familiarity with UDP and TCP
- Knowledge of congestion control mechanisms

## Limitations

- QUIC may not be supported by all network devices.
- Potential security vulnerabilities in 0-RTT handshakes.
- Higher complexity in implementation compared to TCP.

## Open Questions

- How can QUIC be optimized for specific application scenarios?
- What are the long-term security implications of QUIC's design?

## Abstract

While TCP is a connection-oriented protocol, QUIC is a UDP-based protocol that combines transport and application-layer functions for faster performance. It works by multiplexing multiple streams over a single connection and reducing handshake overhead. It supports connection migration, enables 0-RTT handshakes, provides built-in congestion control, multiplexes streams without head-of-line blocking, and minimizes latency. In other words: QUIC establishes connections quickly, handles multiple streams efficiently, and adapts to changing network conditions without requiring multiple round trips for handshakes. So yeah, it’s really fast. But, it also takes a novel approach to security. While QUIC is a transport-layer protocol, it includes features that are traditionally found in both transport and security layers. So essentially it’s doing the work of something like TCP plus TLS, except that
