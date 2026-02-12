# A Scalable Real-Time SDN-Based MQTT Framework for Industrial Applications

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1109/OJIES.2024.3373232` |
| Full Paper | [https://doi.org/10.1109/OJIES.2024.3373232](https://doi.org/10.1109/OJIES.2024.3373232) |
| Source | [https://journalclub.io/episodes/a-scalable-real-time-sdn-based-mqtt-framework-for-industrial-applications](https://journalclub.io/episodes/a-scalable-real-time-sdn-based-mqtt-framework-for-industrial-applications) |
| Year | 2026 |
| Citations | 0 |
| Authors |  |
| Paper ID | `91da88ed-e9d8-4eb2-a198-4bb922590028` |

## Classification

- **Problem Type:** real-time communication in industrial IoT
- **Domain:** Networking & Distributed Systems
- **Sub-domain:** Industrial Internet of Things (IIoT), Software-Defined Networking (SDN), MQTT
- **Technique:** RT-MQTT and MRT-MQTT
- **Technique Category:** framework
- **Type:** novel

## Summary

This paper presents a scalable framework that integrates Software-Defined Networking (SDN) with the Message Queuing Telemetry Transport (MQTT) protocol to enhance real-time communication in industrial applications. Engineers should care because it addresses the critical need for timeliness and reliability in the rapidly evolving landscape of Industry 4.0 and the Industrial Internet of Things (IIoT).

## Key Contribution

**The development of a real-time MQTT extension (RT-MQTT) integrated with SDN for improved network management and real-time performance.**

## Problem

The need for reliable and timely communication in complex industrial environments with numerous heterogeneous devices.

## Method

**Approach:** The method integrates SDN with MQTT to allow applications to specify real-time requirements, which are then enforced by the SDN controller through network reservations. The framework uses multicast to efficiently propagate MQTT traffic across multiple edge networks.

**Algorithm:**

1. 1. Define real-time requirements using MQTT User Properties.
2. 2. Intercept MQTT traffic with a Network Manager.
3. 3. Extract real-time information from the intercepted traffic.
4. 4. Instruct the SDN controller to create network reservations based on the extracted information.
5. 5. Deploy multicast across selected brokers to propagate MQTT traffic.
6. 6. Monitor and adjust network reservations as needed.

**Input:** MQTT messages with specified real-time requirements in User Properties.

**Output:** Real-time MQTT communication with guaranteed latency and reliability across the network.

**Key Parameters:**

- `QoS levels: 0, 1, 2`
- `Latency requirements: application-specific (not specified in the paper)`
- `Network reservation parameters: application-specific (not specified in the paper)`

**Complexity:** Not stated.

## Benchmarks

**Tested on:** Emulation experiments conducted in industrial scenarios.

**Results:**

- Latency reduction compared to standard MQTT and DM-MQTT.

**Compared against:** Standard MQTT, Direct Multicast-MQTT (DM-MQTT)

**Improvement:** Demonstrated superior performance in latency reduction over MQTT and DM-MQTT.

## Implementation Guide

**Data Structures:** MQTT message structure, SDN flow tables, Network reservation data structures

**Dependencies:** MQTT broker (v5.0), SDN controller (OpenFlow compatible)

**Core Operation:**

```python
def handle_mqtt_message(message): extract_real_time_requirements(message); instruct_sdn_controller(); propagate_multicast();
```

**Watch Out For:**

- Ensure compatibility between MQTT version and SDN controller.
- Monitor network performance to adjust reservations dynamically.
- Be aware of potential overhead introduced by real-time extensions.

## Use This When

- You need to ensure real-time communication in industrial IoT applications.
- You are working with heterogeneous devices that require dynamic network management.
- You want to reduce latency in MQTT communications across multiple edge networks.

## Don't Use When

- The application does not require real-time guarantees.
- You are working in a static network environment with no need for dynamic reconfiguration.
- The overhead of integrating SDN is not justified for your use case.

## Key Concepts

SDN, MQTT, real-time communication, multicast, resource management, IIoT, network reservations

## Connects To

- MQTT-SN
- OpenQoS
- DM-MQTT
- MI-SDN
- SDN-based QoS frameworks

## Prerequisites

- Understanding of MQTT protocol
- Familiarity with SDN concepts
- Knowledge of real-time systems

## Limitations

- Not explicitly designed for non-real-time applications
- Potential overhead from real-time processing
- Requires specific network configurations for optimal performance

## Open Questions

- How can security be integrated without compromising real-time performance?
- What are the scalability limits of the proposed framework in larger industrial settings?

## Abstract

Let’s say you and I are Oompa Loompas in a chocolate factory. We have various jobs, and we do all the meaningful work, while the crazy guy in the hat gets all the credit. But that’s fine, it’s what we signed up for. Your job is to take caramel squares and dip them in chocolate. Then you hand them to me. I sprinkle a little salt on top and carefully wrap each chocolate-covered caramel in a cellophane wrapper, twist the ends, and then place that carefully in a box lined with tissue paper. You dip, I wrap.
