# Edge Computing Architecture for the Management of Underwater Cultural Heritage

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3390/jmse12122250` |
| Full Paper | [https://doi.org/10.3390/jmse12122250](https://doi.org/10.3390/jmse12122250) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/b6a9030f0065347237b82a74155fae77aa0e2dac](https://www.semanticscholar.org/paper/b6a9030f0065347237b82a74155fae77aa0e2dac) |
| Source | [https://journalclub.io/episodes/edge-computing-architecture-for-the-management-of-underwater-cultural-heritage](https://journalclub.io/episodes/edge-computing-architecture-for-the-management-of-underwater-cultural-heritage) |
| Source | [https://www.semanticscholar.org/paper/b6a9030f0065347237b82a74155fae77aa0e2dac](https://www.semanticscholar.org/paper/b6a9030f0065347237b82a74155fae77aa0e2dac) |
| Year | 2026 |
| Citations | 0 |
| Authors | Jorge Herrera-Santos, Marta Plaza-Hernández, Sebastián López-Flórez, Vladimir Djapic, Javier Prieto Tejedor, Emilio Santiago Corchado-Rodríguez |
| Paper ID | `27366dbe-86c9-4bfb-8e06-7c53b89f8eec` |

## Classification

- **Problem Type:** real-time monitoring and management of underwater cultural heritage
- **Domain:** Machine Learning & AI
- **Sub-domain:** Edge Computing, Internet of Underwater Things
- **Technique:** Edge Computing Architecture for Underwater Cultural Heritage Management
- **Technique Category:** framework
- **Type:** novel

## Summary

The paper presents an edge computing architecture designed for the management of underwater cultural heritage (UCH), addressing the unique challenges posed by underwater environments. Engineers should care because this platform enhances real-time monitoring and management of UCH, improving responsiveness and reliability in remote maritime areas.

## Key Contribution

**An innovative platform integrating edge computing and the Internet of Underwater Things (IoUT) for real-time monitoring and management of underwater cultural heritage.**

## Problem

The need to protect and manage underwater cultural heritage sites, which face threats from environmental changes and inadequate conservation technologies.

## Method

**Approach:** The method involves deploying edge nodes on buoys near underwater cultural heritage sites to process data locally, reducing reliance on cloud connectivity. The architecture integrates acoustic communication and LoRa technology for robust data transmission and real-time risk assessment using AI models.

**Algorithm:**

1. 1. Deploy sensors in the underwater environment to collect data.
2. 2. Transmit data to edge nodes on buoys using acoustic communication.
3. 3. Process and filter data at the edge nodes to identify critical information.
4. 4. Cache important data until cloud connectivity is available.
5. 5. Send processed metadata to the cloud for further analysis and storage.
6. 6. Utilize AI models for real-time risk assessment based on processed data.

**Input:** Data from underwater sensors measuring environmental parameters (temperature, pressure, salinity, etc.)

**Output:** Processed metadata and real-time alerts regarding the status of underwater cultural heritage sites.

**Key Parameters:**

- `battery_life: 48 hours`
- `data_transmission_interval: 10 minutes`
- `LoRa_range: up to 10 km`
- `acoustic_communication_range: variable based on conditions`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Environmental data from underwater sensors, Historical data from public databases

**Results:**

- Real-time monitoring accuracy
- Response time to environmental changes

**Compared against:** Traditional cloud-based monitoring systems

**Improvement:** Significantly improved responsiveness and reduced data transmission costs compared to traditional methods.

## Implementation Guide

**Data Structures:** Sensor networks, Edge nodes on buoys, Communication protocols for acoustic and LoRa

**Dependencies:** Acoustic communication libraries, LoRa communication modules, AI frameworks for risk assessment

**Core Operation:**

```python
for each sensor in underwater network: data = collect_data(sensor); process_data(data); send_to_edge_node(data);
```

**Watch Out For:**

- Ensure battery systems are reliable for long-term deployments.
- Monitor for signal attenuation in underwater environments.
- Consider environmental factors that may affect sensor accuracy.

## Use This When

- Monitoring underwater cultural heritage sites with limited cloud connectivity.
- Implementing real-time risk assessment for environmental changes affecting submerged artifacts.
- Deploying sensor networks in remote maritime areas.

## Don't Use When

- High-bandwidth data transmission is consistently available.
- Real-time processing is not critical for the application.
- The underwater environment is not a factor.

## Key Concepts

edge computing, IoUT, acoustic communication, real-time monitoring, risk assessment, environmental parameters, data caching

## Connects To

- IoT frameworks for underwater applications
- AI models for environmental monitoring
- Acoustic communication technologies

## Prerequisites

- Understanding of edge computing principles
- Familiarity with underwater sensor technologies
- Knowledge of acoustic communication methods

## Limitations

- Signal attenuation in water limits communication range.
- Dependence on battery life for sensor nodes.
- Challenges in maintaining equipment in harsh underwater conditions.

## Open Questions

- How can the system be scaled for larger underwater sites?
- What additional sensors could enhance monitoring capabilities?

## Abstract

Your mission is to travel to a new site and install sensors, monitoring, and edge nodes as usual. But there’s a catch. This cultural heritage site… is underwater. It’s not a dig-site or a cave, it’s an ancient shipwreck. So now you’ve got some thinking to do. How does the heritage-site being underwater change what you need to build? What’s the same, and what’s different? Let’s walk through it. There are five key differences: 1. There’s no power in the middle of the ocean. 2. Radio signals attenuate in water. 3. GPS is ineffective under water. 4. Not only is everything going to get wet, but pressure is high, temps are cold and saltwater corrodes everything. 5. Connectivity to the cloud will be possible, but limited. You’re no longer working in vanilla IoT. This is IoUT, the Internet of Underwater Things.
