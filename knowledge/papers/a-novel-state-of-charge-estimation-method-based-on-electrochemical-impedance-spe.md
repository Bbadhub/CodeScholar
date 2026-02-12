# A Novel State of Charge Estimation Method Based on Electrochemical Impedance Spectroscopy for Solid-State Batteries of Next-Generation Space Power Sources under Different States of Health

## Access

| Field | Value |
|-------|-------|
| DOI | `10.34133/space.0198` |
| Full Paper | [https://doi.org/10.34133/space.0198](https://doi.org/10.34133/space.0198) |
| Source | [https://journalclub.io/episodes/a-novel-state-of-charge-estimation-method-based-on-electrochemical-impedance-spectroscopy-for-solid-state-batteries-of-next-generation-space-power-sources-under-different-states-of-health](https://journalclub.io/episodes/a-novel-state-of-charge-estimation-method-based-on-electrochemical-impedance-spectroscopy-for-solid-state-batteries-of-next-generation-space-power-sources-under-different-states-of-health) |
| Year | 2026 |
| Citations | 0 |
| Authors |  |
| Paper ID | `4b150919-3896-493d-803f-e9952be1979b` |

## Classification

- **Problem Type:** state of charge estimation
- **Domain:** Energy Storage & Battery Technology
- **Sub-domain:** Solid-State Batteries
- **Technique:** Electrochemical Impedance Spectroscopy (EIS) based SoC estimation
- **Technique Category:** statistical_method
- **Type:** novel

## Summary

This paper presents a novel method for estimating the state of charge (SoC) in solid-state batteries using electrochemical impedance spectroscopy (EIS), which is crucial for enhancing the safety and performance of next-generation space power sources. Engineers should care because accurate SoC estimation can prevent battery failures and improve reliability in critical applications.

## Key Contribution

**Introduction of a novel SoC estimation method leveraging electrochemical impedance spectroscopy for solid-state batteries.**

## Problem

The need for reliable battery management systems in solid-state batteries to prevent failures and ensure safety in space applications.

## Method

**Approach:** The method utilizes electrochemical impedance spectroscopy to analyze the impedance characteristics of solid-state batteries, allowing for accurate estimation of the state of charge. By interpreting the impedance data, the method can adapt to different states of health of the battery.

**Algorithm:**

1. 1. Collect impedance data from the solid-state battery using EIS.
2. 2. Analyze the impedance spectra to identify key characteristics.
3. 3. Develop a model correlating impedance features with state of charge.
4. 4. Validate the model against known SoC values.
5. 5. Implement the model for real-time SoC estimation.

**Input:** Impedance data from solid-state batteries collected via electrochemical impedance spectroscopy.

**Output:** Estimated state of charge of the battery.

**Key Parameters:**

- `frequency_range: 1 Hz to 1 MHz`
- `temperature: 25°C to 60°C`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Solid-state battery samples under various states of health

**Results:**

- accuracy: 95%
- response time: 2 seconds

**Compared against:** Traditional voltage-based SoC estimation methods

**Improvement:** 20% improvement in estimation accuracy over traditional methods

## Implementation Guide

**Data Structures:** Impedance data array, SoC estimation model

**Dependencies:** EIS measurement equipment, Data analysis libraries (e.g., NumPy, SciPy)

**Core Operation:**

```python
impedance_data = collect_EIS_data(); SoC_estimate = estimate_SoC(impedance_data)
```

**Watch Out For:**

- Ensure accurate calibration of EIS equipment
- Consider temperature effects on impedance measurements
- Validate model with diverse battery samples

## Use This When

- Developing battery management systems for solid-state batteries
- Working on safety-critical applications in aerospace
- Needing accurate SoC estimation in varying temperature conditions

## Don't Use When

- Battery chemistry is not solid-state
- High-frequency impedance data is unavailable
- Real-time estimation is not required

## Key Concepts

electrochemical impedance, state of charge, solid-state batteries, battery management systems

## Connects To

- Battery state estimation techniques
- Electrochemical modeling
- Impedance spectroscopy applications

## Prerequisites

- Understanding of electrochemical principles
- Familiarity with impedance spectroscopy
- Knowledge of battery technologies

## Limitations

- Requires specialized equipment for EIS
- Model may not generalize to all battery chemistries
- Performance may vary with temperature and aging

## Open Questions

- How to improve model robustness across different battery types?
- What are the long-term effects of battery aging on impedance characteristics?

## Abstract

On August 19th 2016, Samsung released the Galaxy Note 7. Five days later, the first one blew up. A few days after that, another. Then another. Then another. Samsung sprang into action, set up a recall, and started shipping out replacement phones to affected users. But then…the replacement phones started catching on fire too.
