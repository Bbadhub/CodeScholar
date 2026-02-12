# Real-time monitoring of water quality dynamics using low-cost sensor networks in Lagos lagoon

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1017/wat.2025.10006` |
| Full Paper | [https://doi.org/10.1017/wat.2025.10006](https://doi.org/10.1017/wat.2025.10006) |
| Source | [https://journalclub.io/episodes/real-time-monitoring-of-water-quality-dynamics-using-low-cost-sensor-networks-in-lagos-lagoon](https://journalclub.io/episodes/real-time-monitoring-of-water-quality-dynamics-using-low-cost-sensor-networks-in-lagos-lagoon) |
| Year | 2026 |
| Citations | 0 |
| Authors |  |
| Paper ID | `72f0d379-993f-4120-a76e-e948fb70fa4f` |

## Classification

- **Problem Type:** environmental monitoring
- **Domain:** Environmental Monitoring
- **Sub-domain:** Sensor Networks, Machine Learning in Ecology
- **Technique:** AI-driven multi-sensor data logging system
- **Technique Category:** framework
- **Type:** novel

## Summary

The study presents a low-cost multi-sensor network for real-time monitoring of water quality and biodiversity in Lagos Lagoon, utilizing Raspberry Pi technology. Engineers should care because it demonstrates a practical, scalable solution for environmental monitoring in resource-constrained settings, integrating AI for species identification.

## Key Contribution

**Development of a cost-effective, AI-driven multi-sensor system for continuous aquatic ecosystem monitoring.**

## Problem

The degradation of water quality and loss of aquatic biodiversity in Lagos Lagoon due to pollution and climate change necessitated a reliable monitoring solution.

## Method

**Approach:** The method involves integrating temperature sensors, hydrophones, and cameras into a Raspberry Pi-based system for real-time data collection. Data is processed and stored locally, with remote access enabled for monitoring.

**Algorithm:**

1. 1. Assemble Raspberry Pi with sensors (temperature, microphone, camera).
2. 2. Calibrate sensors for accurate measurements.
3. 3. Deploy sensors in aquatic environments.
4. 4. Collect data on temperature, sound, and images.
5. 5. Process data using AI algorithms for species identification.
6. 6. Store data locally and enable remote access for monitoring.

**Input:** Environmental data from temperature sensors (DS18B20), hydrophones, and camera images.

**Output:** Real-time logs of temperature, acoustic data, and images of aquatic life.

**Key Parameters:**

- `learning_rate: 0.001`
- `batch_size: 32`
- `epochs: 20`
- `sensor_depth: 1m`

**Complexity:** not stated

## Benchmarks

**Tested on:** 31 species visual dataset (8791 training images, 2751 validation images, 1760 testing images), Acoustic datasets from hydrophones

**Results:**

- accuracy: 0.2604 (final validation accuracy)
- training loss: 2.8122 (final training loss)
- validation loss: 2.5765 (final validation loss)

**Compared against:** Commercial-grade sensors for temperature and acoustic monitoring

**Improvement:** Demonstrated capability to monitor aquatic conditions effectively despite challenges.

## Implementation Guide

**Data Structures:** Raspberry Pi GPIO for sensor interfacing, CSV format for data logging

**Dependencies:** Python libraries for data processing (e.g., NumPy, OpenCV), RealVNC for remote access, Machine learning libraries (e.g., TensorFlow, Keras)

**Core Operation:**

```python
data = read_sensors(); process_data(data); if species_detected: log_data(data)
```

**Watch Out For:**

- Ensure waterproofing of the sensor enclosure.
- Calibrate sensors before deployment to avoid inaccuracies.
- Monitor battery life to ensure continuous operation.

## Use This When

- You need a low-cost solution for environmental monitoring.
- Real-time data collection is essential for aquatic ecosystems.
- You want to integrate AI for species identification in ecological studies.

## Don't Use When

- High precision is required beyond the capabilities of low-cost sensors.
- Real-time underwater data transmission is critical beyond 10 cm depth.
- You need a solution for environments with high signal attenuation.

## Key Concepts

Raspberry Pi, Multi-sensor integration, AI species identification, Real-time data logging, Environmental monitoring, Acoustic analysis, Image processing

## Connects To

- IoT sensor networks
- Machine learning for ecological data
- Remote monitoring systems

## Prerequisites

- Basic understanding of Raspberry Pi and GPIO interfacing
- Familiarity with machine learning concepts
- Knowledge of environmental monitoring techniques

## Limitations

- Signal attenuation limits real-time data transmission underwater.
- Image quality affected by water turbidity.
- Requires further optimization for AI models.

## Open Questions

- How can the system be improved for deeper underwater monitoring?
- What advanced image processing techniques can enhance data quality?

## Abstract

The authors have come up with a field-ready sensor network that can collect, process, and store environmental data autonomously. It’s really nothing more than a Raspberry Pi, a waterproof housing, and a whole lot of ingenuity. But what it’s capable of is impressive. It can measure temperature, it can record underwater sound, and it can capture images of aquatic life without commercial-grade hardware.
