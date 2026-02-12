# HIPR: Hardware IP Protection through Low-Overhead Fine-Grain Redaction

## Access

| Field | Value |
|-------|-------|
| DOI | `10.46586/tches.v2025.i3.781-805` |
| Full Paper | [https://doi.org/10.46586/tches.v2025.i3.781-805](https://doi.org/10.46586/tches.v2025.i3.781-805) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/ae73aaf5a21daf4288c3a9cc8711159d985b1ca1](https://www.semanticscholar.org/paper/ae73aaf5a21daf4288c3a9cc8711159d985b1ca1) |
| Source | [https://journalclub.io/episodes/hipr-hardware-ip-protection-through-low-overhead-fine-grain-redaction](https://journalclub.io/episodes/hipr-hardware-ip-protection-through-low-overhead-fine-grain-redaction) |
| Source | [https://www.semanticscholar.org/paper/ae73aaf5a21daf4288c3a9cc8711159d985b1ca1](https://www.semanticscholar.org/paper/ae73aaf5a21daf4288c3a9cc8711159d985b1ca1) |
| Year | 2026 |
| Citations | 2 |
| Authors | Aritra Dasgupta, Sudipta Paria, S. Bhunia |
| Paper ID | `e175629e-581c-47d0-90f1-c7f3d28fbfeb` |

## Classification

- **Problem Type:** hardware IP protection
- **Domain:** Cybersecurity
- **Sub-domain:** Hardware IP Protection
- **Technique:** HIPR
- **Technique Category:** framework
- **Type:** novel

## Summary

HIPR is a novel fine-grain redaction methodology designed to protect hardware intellectual property (IP) from confidentiality and integrity attacks in the semiconductor industry. It significantly reduces overhead costs compared to existing redaction techniques while maintaining robust security, making it suitable for real-world applications.

## Key Contribution

**Introduction of a low-overhead fine-grain redaction methodology for hardware IP protection that is robust and scalable.**

## Problem

The globalization of the semiconductor supply chain has made hardware IP vulnerable to piracy, cloning, and malicious alterations.

## Method

**Approach:** HIPR identifies security-critical logic cones in a hardware design and replaces them with a configurable fabric that can only be programmed with a protected bitstream. It employs multiple optimization steps to reduce overhead while ensuring security.

**Algorithm:**

1. Create a hypergraph from the original netlist.
2. Sort the hypergraph topologically.
3. Identify critical edges based on a removal cost function.
4. Redact Boolean logic using Configurable Look-Up Tables (CLUTs).
5. Redact sequential logic using Configurable Sequential Blocks (CSBs).
6. Redact interconnect logic using Configurable Programmable Interconnects (CPIs).
7. Generate the configuration bitstream for the redacted components.
8. Optimize the bitstream for size without compromising security.

**Input:** Original netlist (RTL or gate-level design files).

**Output:** Redacted netlist and compacted configuration bitstream.

**Key Parameters:**

- `Tcrit: configurable threshold for critical logic identification (default: 0)`
- `gamma_min_size: minimum size for random LUTs`
- `gamma_max_size: maximum size for random LUTs`
- `gamma_x_max: maximum percentage of FFs to redact using CSBs`
- `gamma_y_max: maximum percentage of sequential logic to redact`

**Complexity:** Not stated.

## Benchmarks

**Tested on:** Open-source benchmarks used for evaluation.

**Results:**

- Area overhead reduction: 1 to 2 orders of magnitude compared to state-of-the-art techniques.

**Compared against:** Existing coarse-grain and fine-grain redaction techniques.

**Improvement:** 1 to 2 orders of magnitude reduction in area overhead.

## Implementation Guide

**Data Structures:** Hypergraph representation of the netlist., Lists for CLUTs, CSBs, and CPIs.

**Dependencies:** Custom-designed standard cells for CLUTs, CSBs, and CPIs.

**Core Operation:**

```python
Nmod, cfg_bitstreamcompact = HIPR(N, θ, γ)
```

**Watch Out For:**

- Ensure that the configurable fabric is designed to minimize overhead.
- Be cautious of the security implications of the generated bitstream.
- Monitor the performance impact of redaction on the overall design.

## Use This When

- You need to protect hardware IP in a zero-trust manufacturing environment.
- You require a scalable solution for hardware IP redaction with minimal overhead.
- You want to integrate redaction techniques into existing EDA tool flows.

## Don't Use When

- The design does not involve sensitive hardware IP.
- You are working with very small designs where overhead is not a concern.
- You require a solution that does not involve reconfigurable fabrics.

## Key Concepts

fine-grain redaction, configurable fabric, security-critical logic, interconnect randomization

## Connects To

- LUT-based obfuscation
- eFPGA-based redaction
- logic locking techniques

## Prerequisites

- Understanding of hardware design flows
- Familiarity with EDA tools
- Knowledge of security threats in hardware IP

## Limitations

- Potential vulnerability to advanced structural attacks.
- Requires custom design of standard cells for optimal performance.
- Overhead optimization may not be suitable for all designs.

## Open Questions

- How can HIPR be adapted for different types of hardware designs?
- What additional security measures can be integrated with HIPR?

## Abstract

You see, if you’re in the semiconductor industry, you more than likely have a global supply chain. Sure, your designs are perfected over here, but only with help from consultants who are from somewhere else. And the fabrication happens in a third place, using machines from fourth place…and the packaging happens in a fifth place…then of course the testing and assembly happen somewhere else entirely. So no: locking down your IP doesn’t mean just giving your team Yubikeys and calling it a day. Your intellectual property is passing through dozens of hands, and being seen by hundreds of eyes. Chips are complex, and a successful product launch is partially the result of the work of thousands of people who you’ll never meet and have no access to.
