# Enhancing Data Security Through VLSM Subnetting and TCP/IP Model in an ENT

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3390/app142310968` |
| Full Paper | [https://doi.org/10.3390/app142310968](https://doi.org/10.3390/app142310968) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/526b29c31f3e31ec73b00ea046a4ac3482d39ad2](https://www.semanticscholar.org/paper/526b29c31f3e31ec73b00ea046a4ac3482d39ad2) |
| Source | [https://journalclub.io/episodes/enhancing-data-security-through-vlsm-subnetting-and-tcpip-model-in-an-ent](https://journalclub.io/episodes/enhancing-data-security-through-vlsm-subnetting-and-tcpip-model-in-an-ent) |
| Source | [https://www.semanticscholar.org/paper/526b29c31f3e31ec73b00ea046a4ac3482d39ad2](https://www.semanticscholar.org/paper/526b29c31f3e31ec73b00ea046a4ac3482d39ad2) |
| Year | 2026 |
| Citations | 1 |
| Authors | Caxton Okoh, Waba Nasali Theophilus, Paul Dawkins, Sebamalai Paheerathan |
| Paper ID | `e7fada58-d559-460a-bf35-6c6838de7c13` |

## Classification

- **Problem Type:** network security and optimization
- **Domain:** Networking & Distributed Systems
- **Sub-domain:** Network Security and Design
- **Technique:** Enhanced Network Topology (ENT)
- **Technique Category:** networking framework
- **Type:** novel

## Summary

The paper presents an Enhanced Network Topology (ENT) that integrates Variable Length Subnet Mask (VLSM) subnetting and the updated TCP/IP model to improve data security and performance in traditional corporate networks. Engineers should care because this approach modernizes legacy systems, making them more resilient against cyber threats while optimizing resource allocation.

## Key Contribution

**The introduction of an Enhanced Network Topology (ENT) that utilizes VLSM and an updated TCP/IP model for improved data security and network performance.**

## Problem

The need to secure data transmission and optimize resource allocation in legacy corporate networks.

## Method

**Approach:** The method involves designing a hierarchical network topology that incorporates VLSM for efficient IP address allocation and the updated TCP/IP model for secure data transmission. The ENT is simulated using Cisco Packet Tracer to analyze packet transfer and connections.

**Algorithm:**

1. Identify the host requirements for each subnet.
2. Determine the class of IP subnet based on the required number of hosts.
3. Identify the host bits for each subnet using the formula 2^n - 2.
4. Allocate IP addresses and subnet masks based on the identified host bits.
5. Simulate the network design in Cisco Packet Tracer.

**Input:** Network requirements including the number of hosts per location and existing network infrastructure.

**Output:** A simulated network topology with optimized IP address allocation and enhanced security protocols.

**Key Parameters:**

- `CIDR: /24 for the main network`
- `Subnet A: /25 for 120 hosts`
- `Subnet B: /27 for 30 hosts`
- `Subnet C: /26 for 60 hosts`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Cisco Packet Tracer simulation results

**Results:**

- Packet transfer efficiency
- Network security protocols effectiveness

**Compared against:** Traditional network configurations without VLSM

**Improvement:** Demonstrated improved security and performance metrics over traditional configurations.

## Implementation Guide

**Data Structures:** Subnetting tables, Routing tables, Network device configurations

**Dependencies:** Cisco Packet Tracer, Networking hardware (routers, switches)

**Core Operation:**

```python
for each subnet in network: allocate IP addresses based on VLSM; configure routing protocols; simulate in Cisco Packet Tracer.
```

**Watch Out For:**

- Ensure correct subnet mask allocation to avoid IP conflicts.
- Monitor for misconfigurations that could expose the network to threats.
- Validate simulation results against expected performance metrics.

## Use This When

- Modernizing legacy corporate networks to improve security.
- Designing networks for IoT or SCADA systems requiring secure data transmission.
- Optimizing IP address allocation in large enterprise networks.

## Don't Use When

- Working with small networks where traditional subnetting suffices.
- In environments where existing cloud solutions provide adequate security.
- When simplicity and minimal configuration are prioritized over security.

## Key Concepts

VLSM, TCP/IP model, network topology, routing protocols, IPSec, DHCP, network simulation

## Connects To

- CIDR
- Routing Information Protocol (RIP)
- Enhanced Interior Gateway Routing Protocol (EIGRP)
- Open Shortest Path First (OSPF)
- Internet Protocol Security (IPSec)

## Prerequisites

- Understanding of subnetting
- Familiarity with TCP/IP model
- Knowledge of routing protocols

## Limitations

- Complexity in configuration for large networks.
- Potential for misconfiguration leading to security vulnerabilities.
- Dependence on Cisco Packet Tracer for simulation.

## Open Questions

- How can this approach be adapted for real-time network monitoring?
- What are the implications of using this model in cloud-based environments?

## Abstract

If you’ve gotten used to creating VPCs on AWS or GCP, (or VNets on Azure), then you’ve probably become pretty spoiled. All those configuration options, and knobs and dials. The CIDR blocks and subnets and masks. All that comes out of the box when you’re working in the cloud. But if you’re administering a traditional corporate network for an enterprise, the picture is probably very different. These kinds of legacy systems don’t provide nearly the functionality that you might want and need to support the company’s growing demands. And that’s where this paper comes in. The authors are proposing what they’re calling an ENT: An Enhanced Network Topology that makes a number of changes all-at-once to quickly modernize older networks.
