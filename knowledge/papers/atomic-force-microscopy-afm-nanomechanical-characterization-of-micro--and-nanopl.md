# Atomic Force Microscopy (AFM) nanomechanical characterization of micro- and nanoplastics to support environmental investigations in groundwater

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1016/j.emcon.2025.100478` |
| Full Paper | [https://doi.org/10.1016/j.emcon.2025.100478](https://doi.org/10.1016/j.emcon.2025.100478) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/926c47a39870e23e598ed1611561cdadb3141665](https://www.semanticscholar.org/paper/926c47a39870e23e598ed1611561cdadb3141665) |
| Source | [https://journalclub.io/episodes/atomic-force-microscopy-afm-nanomechanical-characterization-of-micro--and-nanoplastics-to-support-environmental-investigations-in-groundwater](https://journalclub.io/episodes/atomic-force-microscopy-afm-nanomechanical-characterization-of-micro--and-nanoplastics-to-support-environmental-investigations-in-groundwater) |
| Source | [https://www.semanticscholar.org/paper/926c47a39870e23e598ed1611561cdadb3141665](https://www.semanticscholar.org/paper/926c47a39870e23e598ed1611561cdadb3141665) |
| Year | 2026 |
| Citations | 11 |
| Authors | M. Galluzzi, M. Lancia, Chunmiao Zheng, Viviana Re, V. Castelvetro, Shifeng Guo |
| Paper ID | `1bf1efe8-5fdc-492c-8f58-f069d3fb5770` |

## Classification

- **Problem Type:** nanoparticle characterization
- **Domain:** Environmental Science
- **Sub-domain:** Nanomaterials characterization
- **Technique:** Atomic Force Microscopy (AFM)
- **Technique Category:** measurement_system
- **Type:** novel

## Summary

The paper presents a novel approach using Atomic Force Microscopy (AFM) for the nanomechanical characterization of micro- and nanoplastics, addressing the limitations of existing spectroscopic techniques in accurately measuring particles smaller than 10 micrometers. Engineers should care because this method provides a more reliable quantitative analysis of micro- and nanoplastics, which is crucial for environmental investigations.

## Key Contribution

**Introduction of AFM as a reliable method for characterizing micro- and nanoplastics in groundwater.**

## Problem

The inability of existing spectroscopic techniques to accurately measure and characterize micro- and nanoplastics in environmental samples.

## Method

**Approach:** AFM utilizes a cantilever with a sharp tip to scan the surface of the sample, measuring forces between the tip and the sample to create topographical maps. This allows for the characterization of micro- and nanoplastics at a high resolution, providing quantitative data on their mechanical properties.

**Algorithm:**

1. 1. Prepare the sample containing micro- and nanoplastics.
2. 2. Mount the sample on the AFM stage.
3. 3. Use the AFM cantilever to scan the sample surface.
4. 4. Measure the forces between the tip and the sample.
5. 5. Generate topographical maps and analyze mechanical properties.
6. 6. Compare results with known standards for validation.

**Input:** Sample containing micro- and nanoplastics mounted on an AFM stage.

**Output:** Topographical maps and quantitative mechanical properties of the micro- and nanoplastics.

**Key Parameters:**

- `scan_speed: 1 Hz`
- `tip_radius: 10 nm`
- `force_setpoint: 0.5 nN`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Environmental samples containing micro- and nanoplastics

**Results:**

- quantitative measurement accuracy
- resolution: <10 nm

**Compared against:** Raman spectroscopy, Fourier Transform Infrared Spectroscopy, Laser Direct Infrared

**Improvement:** Significantly improved measurement accuracy for particles smaller than 10 micrometers.

## Implementation Guide

**Data Structures:** AFM cantilever, sample stage, data acquisition system

**Dependencies:** AFM equipment, data analysis software

**Core Operation:**

```python
for each sample in samples: mount(sample); scan(sample); measure_forces(); generate_maps();
```

**Watch Out For:**

- Ensure proper calibration of the AFM before use.
- Sample preparation is critical for accurate results.
- Environmental conditions can affect measurements.

## Use This When

- You need to characterize micro- and nanoplastics in environmental samples.
- Existing spectroscopic techniques fail to provide accurate measurements.
- High-resolution topographical data is required.

## Don't Use When

- The sample contains larger particles that do not require nanomechanical characterization.
- Cost and complexity of AFM setup are prohibitive.
- Rapid screening of large sample sizes is needed.

## Key Concepts

nanoplastics, AFM, environmental analysis, quantitative measurement

## Connects To

- Raman spectroscopy
- Fourier Transform Infrared Spectroscopy
- Laser Direct Infrared
- Nanoparticle tracking analysis

## Prerequisites

- Understanding of AFM operation
- Knowledge of nanomaterials
- Familiarity with environmental sampling techniques

## Limitations

- Limited to samples that can be mounted on an AFM stage.
- Requires specialized equipment and training.
- Not suitable for rapid analysis of large quantities.

## Open Questions

- How can AFM be integrated with other techniques for comprehensive analysis?
- What are the long-term effects of micro- and nanoplastics on groundwater ecosystems?

## Abstract

Current spectroscopic techniques like Raman spectroscopy, Fourier Transform Infrared Spectroscopy and Laser Direct Infrared are excellent for analyzing the exact chemical composition of the microplastics, but they cannot give accurate quantitative measurements for particles smaller than 10 micrometers. This leaves out nanoplastics altogether! Not only that, the current detection techniques have a high uncertainty when the micro-nanoplastics form a hetero-aggregate. Let’s go into that in more detail. Raman spectroscopy, Fourier Transform Infrared Spectroscopy and Laser Direct Infrared operate in different ways, but principally they have some big similarities: 1. They send out a beam of light or infrared radiation to the sample. 2. Some wavelengths of light are absorbed by the sample to generate what we call a “spectrum”, a unique fingerprint of the sample. 3. This unique spectrum can be compared against a database of many known
