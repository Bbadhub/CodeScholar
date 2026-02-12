# Internet of Paint (IoP): Design, Challenges, Applications and Future Directions

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1109/ACCESS.2025.3539121` |
| Full Paper | [https://doi.org/10.1109/ACCESS.2025.3539121](https://doi.org/10.1109/ACCESS.2025.3539121) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/39977bd92247ac7b0824b53cc5b026b7086f8d65](https://www.semanticscholar.org/paper/39977bd92247ac7b0824b53cc5b026b7086f8d65) |
| Source | [https://journalclub.io/episodes/internet-of-paint-iop-design-challenges-applications-and-future-directions](https://journalclub.io/episodes/internet-of-paint-iop-design-challenges-applications-and-future-directions) |
| Source | [https://www.semanticscholar.org/paper/39977bd92247ac7b0824b53cc5b026b7086f8d65](https://www.semanticscholar.org/paper/39977bd92247ac7b0824b53cc5b026b7086f8d65) |
| Year | 2026 |
| Citations | 0 |
| Authors | Lasantha Thakshila Wedage, Mehmet Can Vuran, Bernard Butler, Christos Argyropoulos, S. Balasubramaniam |
| Paper ID | `199f0e67-d7b3-440b-b59a-d929c826a598` |

## Classification

- **Problem Type:** wireless communication channel capacity analysis
- **Domain:** Networking & Distributed Systems
- **Sub-domain:** Terahertz communication
- **Technique:** Channel capacity analysis for THz transceivers
- **Technique Category:** statistical_method
- **Type:** novel

## Summary

The paper presents a channel capacity analysis for THz transceivers embedded in paint, demonstrating the potential for high-frequency communication through painted surfaces. Engineers should care because this approach could enable novel applications in wireless communication and IoT devices using everyday materials.

## Key Contribution

**The analysis of channel capacity for THz transceivers in paint, highlighting the impact of sub-band division on communication efficiency.**

## Problem

The need for effective communication methods in environments where traditional wireless signals may be obstructed or interfered with.

## Method

**Approach:** The method involves dividing the total bandwidth of THz frequencies into narrow sub-bands to calculate individual capacities, which are then aggregated to determine overall channel capacity. This approach helps mitigate interference from non-white molecular noise.

**Algorithm:**

1. 1. Define the total bandwidth available for THz communication.
2. 2. Divide the bandwidth into narrow sub-bands.
3. 3. Calculate the capacity of each sub-band.
4. 4. Aggregate the capacities of all sub-bands to get the overall channel capacity.
5. 5. Model the impact of different transceiver burial depths.
6. 6. Analyze the results to determine optimal configurations.

**Input:** Total bandwidth of THz frequencies and characteristics of the paint layer.

**Output:** Overall channel capacity in bits per second.

**Key Parameters:**

- `bandwidth: [specific range]`
- `paint_thickness: 2 mm`
- `transceiver_depths: [0.5 mm, 1 mm, 1.95 mm]`

**Complexity:** Not stated.

## Benchmarks

**Tested on:** Simulation data from THz transceiver models in painted environments.

**Results:**

- Channel capacity in bits per second.

**Compared against:** Traditional wireless communication methods without paint.

**Improvement:** Not stated.

## Implementation Guide

**Data Structures:** Arrays for sub-band capacities, Data structures for modeling paint properties

**Dependencies:** Simulation software for THz communication analysis

**Core Operation:**

```python
def calculate_channel_capacity(bandwidth, paint_thickness): ...
```

**Watch Out For:**

- Ensure accurate modeling of paint properties for realistic results.
- Consider environmental factors that may affect THz signal propagation.
- Validate simulation results against real-world measurements.

## Use This When

- Designing communication systems in environments with potential signal interference.
- Exploring novel applications for IoT devices using everyday materials.
- Evaluating the performance of THz communication technologies.

## Don't Use When

- Working in environments where traditional wireless signals are sufficient.
- When low-frequency communication is required.
- In scenarios where paint thickness cannot be controlled.

## Key Concepts

channel capacity, THz transceivers, sub-band division, molecular noise, communication efficiency

## Connects To

- Terahertz communication systems
- Wireless sensor networks
- Signal processing techniques for noise mitigation

## Prerequisites

- Understanding of wireless communication principles
- Familiarity with THz frequency characteristics
- Knowledge of signal processing techniques

## Limitations

- Results may vary significantly with different paint types.
- Limited to specific frequency ranges and environmental conditions.
- Requires precise control over transceiver placement.

## Open Questions

- What are the practical limits of THz communication through various materials?
- How can this approach be scaled for larger networks?

## Abstract

The researchers performed a channel capacity analysis, a test to determine the theoretical maximum rate at which information can be transmitted, measured in bits per second. To calculate the overall channel capacity for THz transceivers in paint, the total bandwidth is divided into narrow sub-bands, and their individual capacities are aggregated. This is possible due to the high frequency selectivity at THz frequencies; in other words, the system is capable of responding to specific frequencies while ignoring others. The division into sub-bands is also helpful to mitigate potential interference from non-white molecular noise, which varies across the frequency spectrum. In the simulation, they used a 2 mm thick layer of “Titanium white” paint; this is thicker than most paint layers and was used to represent a worst-case scenario. They then modeled three different transceiver burial depths, 0.5 mm, 1 mm, and 1.95 mm and checked
