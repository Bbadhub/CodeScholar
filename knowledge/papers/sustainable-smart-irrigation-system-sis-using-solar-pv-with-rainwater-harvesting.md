# Sustainable Smart Irrigation System (SIS) using solar PV with rainwater harvesting technique for indoor plants

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1371/journal.pone.0316911` |
| Full Paper | [https://doi.org/10.1371/journal.pone.0316911](https://doi.org/10.1371/journal.pone.0316911) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/f2b2fe0c4ce274e625a8a35cf4e0ad9ccce2d6ab](https://www.semanticscholar.org/paper/f2b2fe0c4ce274e625a8a35cf4e0ad9ccce2d6ab) |
| Source | [https://journalclub.io/episodes/sustainable-smart-irrigation-system-sis-using-solar-pv-with-rainwater-harvesting-technique-for-indoor-plants](https://journalclub.io/episodes/sustainable-smart-irrigation-system-sis-using-solar-pv-with-rainwater-harvesting-technique-for-indoor-plants) |
| Source | [https://www.semanticscholar.org/paper/f2b2fe0c4ce274e625a8a35cf4e0ad9ccce2d6ab](https://www.semanticscholar.org/paper/f2b2fe0c4ce274e625a8a35cf4e0ad9ccce2d6ab) |
| Year | 2026 |
| Citations | 5 |
| Authors | Syed Zahurul Islam, Muhammad Saufi Bin Kamarudin, Mohd Noor Abdullah, Mimi Mohaffyza, L. Sern, Mohammad Lutfi Othman |
| Paper ID | `fd0a9fb9-db41-46ed-a1c9-2fbdc175dbe7` |

## Classification

- **Problem Type:** automated irrigation system
- **Domain:** Robotics & Control Systems
- **Sub-domain:** Smart irrigation systems
- **Technique:** Sustainable Smart Irrigation System (SIS)
- **Technique Category:** framework
- **Type:** novel

## Summary

The paper presents a Sustainable Smart Irrigation System (SIS) that integrates solar photovoltaic (PV) technology and rainwater harvesting for indoor plant irrigation. Engineers should care because this system optimizes water usage and energy efficiency, addressing the challenges of manual watering and promoting sustainability.

## Key Contribution

**Integration of solar PV, rainwater harvesting, and IoT for an automated irrigation system.**

## Problem

The need for efficient and sustainable watering solutions for indoor plants due to the inconsistency and tediousness of manual watering.

## Method

**Approach:** The SIS uses a solar PV panel to power an Arduino-based system that controls soil moisture sensors and a water pump. The system collects rainwater and uses IoT technology to monitor soil moisture levels, adjusting irrigation schedules accordingly.

**Algorithm:**

1. 1. Measure soil moisture using the sensor.
2. 2. If moisture is below a threshold, activate the water pump.
3. 3. Use GSM to notify the user about the irrigation status.
4. 4. Collect rainwater and store it in a tank.
5. 5. Calculate daily water requirements based on plant needs.
6. 6. Optimize PV panel size based on energy consumption.
7. 7. Monitor system performance and adjust as necessary.

**Input:** Soil moisture data, rainfall data, energy consumption data.

**Output:** Irrigation status notifications, optimized irrigation schedules.

**Key Parameters:**

- `PV panel size: 30W`
- `Daily energy consumption: 22.71Wh`
- `GSM module for notifications`
- `Soil moisture threshold: calibrated based on sensor readings`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Rainwater collection data, soil moisture sensor data

**Results:**

- Water usage efficiency, CO2 emissions reduction: 14.97 kgCO2/year

**Compared against:** Manual watering methods

**Improvement:** Significant reduction in water usage and CO2 emissions compared to traditional methods.

## Implementation Guide

**Data Structures:** Arduino Uno, soil moisture sensor, ultrasonic sensor, GSM module, DC water pump

**Dependencies:** Arduino IDE, GSM library for Arduino

**Core Operation:**

```python
if soil_moisture < threshold: activate_pump() notify_user()
```

**Watch Out For:**

- Ensure GSM coverage is available for notifications.
- Calibrate soil moisture sensors accurately to avoid overwatering.
- Consider seasonal variations in rainfall for tank sizing.

## Use This When

- You need an automated irrigation solution for indoor plants.
- You want to reduce water usage and promote sustainability.
- You require remote monitoring of irrigation systems.

## Don't Use When

- The project requires high water demand that exceeds rainwater collection capacity.
- You need a system that operates without solar power.
- You are working in an area with unreliable GSM coverage.

## Key Concepts

solar PV, IoT, rainwater harvesting, soil moisture sensors, GSM communication, Arduino control

## Connects To

- IoT frameworks
- solar energy systems
- automated control systems

## Prerequisites

- Basic understanding of Arduino programming
- Knowledge of IoT concepts
- Familiarity with solar energy systems

## Limitations

- Dependent on weather conditions for rainwater collection.
- Limited by the capacity of the rainwater harvesting tank.
- Requires maintenance of solar panels and sensors.

## Open Questions

- How can the system be scaled for larger agricultural applications?
- What are the long-term effects of using this system on plant health?

## Abstract

First, the solar panel. The authors opted for a small one: at just 30W this monocrystalline photovoltaic panel was installed at a 15-degree tilt angle. This panel was chosen based on the energy requirements of all the other components in the system to optimize for efficiency. The authors analyzed the load of each system component: the Arduino Uno, soil moisture sensors, ultrasonic sensor, Global System for Mobile Communications (GSM) module, and DC water pump. They calculated a daily energy consumption of 22.71Wh and determined that with Malaysia's average sun-hours of 4.69 hours per day and accounting for a 50% buffer, they needed a minimum PV size of 7.26W. The 30W panel they chose provided ample headroom for operation even under suboptimal weather conditions. The power management system included a Maximum Power Point Tracker (MPPT) with a rated current of 7.8A, which optimizes the charging process by finding the ideal voltage-current point
