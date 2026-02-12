# Application of Forced Oscillation Technique in Assessing Pulmonary Fibrosis in Hermansky-Pudlak Syndrome

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3390/arm92060040` |
| Full Paper | [https://doi.org/10.3390/arm92060040](https://doi.org/10.3390/arm92060040) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/4bb061049f4ce7ce3061f9df423d521b223c1a89](https://www.semanticscholar.org/paper/4bb061049f4ce7ce3061f9df423d521b223c1a89) |
| Source | [https://journalclub.io/episodes/application-of-forced-oscillation-technique-in-assessing-pulmonary-fibrosis-in-hermansky-pudlak-syndrome](https://journalclub.io/episodes/application-of-forced-oscillation-technique-in-assessing-pulmonary-fibrosis-in-hermansky-pudlak-syndrome) |
| Source | [https://www.semanticscholar.org/paper/4bb061049f4ce7ce3061f9df423d521b223c1a89](https://www.semanticscholar.org/paper/4bb061049f4ce7ce3061f9df423d521b223c1a89) |
| Year | 2026 |
| Citations | 0 |
| Authors | Wilfredo De Jesús-Rojas, Luis Reyes-Peña, José Muñiz-Hernández, R. Mena-Ventura, Gabriel Camareno-Soto, G. Rosario-Ortiz |
| Paper ID | `7fb3eee3-5958-4684-9753-5436de9e68b2` |

## Classification

- **Problem Type:** medical diagnosis and monitoring
- **Domain:** Bioinformatics & Health
- **Sub-domain:** Pulmonary disease assessment
- **Technique:** Forced Oscillation Technique (FOT)
- **Technique Category:** detection_system
- **Type:** novel

## Summary

The paper evaluates the Forced Oscillation Technique (FOT) as a non-invasive tool for assessing pulmonary fibrosis in patients with Hermansky-Pudlak Syndrome (HPS). This technique shows promise for early detection and monitoring of pulmonary fibrosis, which is crucial for improving patient outcomes.

## Key Contribution

**The study demonstrates that FOT can effectively measure changes in pulmonary resistance and reactance correlating with the severity of pulmonary fibrosis in HPS patients.**

## Problem

The need for early detection and monitoring of pulmonary fibrosis in patients with Hermansky-Pudlak Syndrome, which is often not captured by standard clinical techniques.

## Method

**Approach:** The FOT uses external pulse vibrations to measure the flow response of the respiratory tract during normal breathing. It quantifies respiratory impedance (Zrs), which is divided into resistance (Rrs) and reactance (Xrs) at multiple frequencies.

**Algorithm:**

1. 1. Set up the Resmon™Pro V3 device for FOT measurements.
2. 2. Instruct the patient to breathe normally while the device emits oscillatory signals.
3. 3. Measure the flow response of the respiratory tract to the oscillations.
4. 4. Calculate Rrs and Xrs from the measured flow and pressure data.
5. 5. Analyze the results to assess the severity of pulmonary fibrosis.

**Input:** Normal breathing data from patients with Hermansky-Pudlak Syndrome.

**Output:** Values of respiratory resistance (Rrs) and reactance (Xrs) at frequencies of 5, 11, and 19 Hz.

**Key Parameters:**

- `frequency: 5 Hz, 11 Hz, 19 Hz`
- `device: Resmon™Pro V3`

**Complexity:** not stated

## Benchmarks

**Tested on:** Five adult patients with Hermansky-Pudlak Syndrome (HPS)

**Results:**

- Rrs: measured in cmH2O/(s/L)
- Xrs: measured in cmH2O/(s/L)
- FEV1: forced expired volume in 1 s, median values ranged from 39% to 70% of predicted

**Compared against:** Standard spirometry measurements

**Improvement:** FOT detected changes in pulmonary function earlier than standard spirometry.

## Implementation Guide

**Data Structures:** Patient respiratory data, FOT measurement results

**Dependencies:** Resmon™Pro V3 device

**Core Operation:**

```python
Rrs, Xrs = FOT.measure(patient_breathing_data)
```

**Watch Out For:**

- Ensure patient compliance during the measurement process.
- Interpret results in the context of clinical symptoms and HRCT findings.
- Consider variations in normal values based on patient demographics.

## Use This When

- Monitoring patients with Hermansky-Pudlak Syndrome for pulmonary fibrosis.
- Assessing lung function in patients unable to perform standard spirometry.
- Early detection of lung function deterioration in interstitial lung diseases.

## Don't Use When

- Patients with normal lung function without risk factors for pulmonary fibrosis.
- In cases where spirometry can be performed reliably.
- When immediate invasive diagnostic procedures are required.

## Key Concepts

respiratory impedance, pulmonary fibrosis, non-invasive measurement, oscillometry

## Connects To

- Spirometry for lung function testing
- High-resolution computed tomography (HRCT) for imaging
- Impulse oscillometry for lung function assessment

## Prerequisites

- Understanding of respiratory physiology
- Familiarity with pulmonary function testing
- Knowledge of Hermansky-Pudlak Syndrome and its implications

## Limitations

- Limited to specific patient populations (e.g., HPS patients).
- Requires specialized equipment and training.
- May not be applicable for all types of pulmonary diseases.

## Open Questions

- How does FOT compare with other non-invasive techniques in broader populations?
- What are the long-term implications of using FOT for monitoring pulmonary fibrosis?

## Abstract

Hermansky-Pudlak Syndrome (HPS) is a rare hereditary condition characterized by genetic mutations impacting Lysosome Related Organelles (LRO). One of the deadliest manifestations of HPS is the development of scarring in the lung tissue called pulmonary fibrosis. Early detection can significantly improve a patient’s quality of life, but many of the early warning signs don't present themselves to the standard clinical technique. Are there other, more specialized tools that might help here? In today's episode, we'll look at research that evaluates a specialized clinical tool called the Forced Oscillation Technique (FOT) as a promising early detection tool for pulmonary fibrosis. We’ll explore pulmonary fibrosis in HPS, how it is clinically diagnosed and why the current methods need an overhaul. Then we’ll see how the authors evaluated the forced oscillation technique in patients with HPS to see if it can improve clinical
