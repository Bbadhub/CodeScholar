# Case Report: Electroanatomic mapping as an early diagnostic tool in arrhythmogenic cardiomyopathy

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3389/fcvm.2024.1392186` |
| Full Paper | [https://doi.org/10.3389/fcvm.2024.1392186](https://doi.org/10.3389/fcvm.2024.1392186) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/14301ff33a70dcd90a97e0dc7e4df690484b9fe0](https://www.semanticscholar.org/paper/14301ff33a70dcd90a97e0dc7e4df690484b9fe0) |
| Source | [https://journalclub.io/episodes/case-report-electroanatomic-mapping-as-an-early-diagnostic-tool-in-arrhythmogenic-cardiomyopathy](https://journalclub.io/episodes/case-report-electroanatomic-mapping-as-an-early-diagnostic-tool-in-arrhythmogenic-cardiomyopathy) |
| Source | [https://www.semanticscholar.org/paper/14301ff33a70dcd90a97e0dc7e4df690484b9fe0](https://www.semanticscholar.org/paper/14301ff33a70dcd90a97e0dc7e4df690484b9fe0) |
| Year | 2026 |
| Citations | 0 |
| Authors | Jose F de Melo, Samuel Shabtaie, Martin van Zyl, Jeremy D. Collins, K. Siontis |
| Paper ID | `96809995-239e-4d07-9113-f3f53e10dfc4` |

## Classification

- **Problem Type:** diagnostic tool for arrhythmogenic cardiomyopathy
- **Domain:** Bioinformatics & Health
- **Sub-domain:** Cardiovascular diagnostics
- **Technique:** Electroanatomic Mapping (EAM)
- **Technique Category:** detection_system
- **Type:** novel

## Summary

The paper presents a case study demonstrating the utility of electroanatomic mapping (EAM) as an early diagnostic tool for arrhythmogenic cardiomyopathy (ACM). It highlights that EAM can reveal abnormal electrical substrates before structural changes are detected by imaging, which is crucial for timely diagnosis and management.

## Key Contribution

**Electroanatomic mapping can identify early electrical abnormalities in arrhythmogenic cardiomyopathy, potentially improving diagnostic accuracy.**

## Problem

The need for early and accurate diagnosis of arrhythmogenic cardiomyopathy, which can lead to serious cardiac events if not identified.

## Method

**Approach:** Electroanatomic mapping is performed using a multielectrode catheter to assess the electrical activity of the heart. It identifies areas of low-voltage and fractionated electrograms that correlate with myocardial abnormalities associated with ACM.

**Algorithm:**

1. 1. Insert a multielectrode catheter into the heart.
2. 2. Perform endocardial high-density substrate bipolar voltage mapping.
3. 3. Identify areas with low-voltage and fractionated electrograms.
4. 4. Target specific PVC morphologies for ablation.
5. 5. Confirm findings with genetic testing if necessary.

**Input:** Electrophysiological data from the heart, including voltage measurements from the mapping catheter.

**Output:** Identification of abnormal electrical substrates and potential diagnosis of arrhythmogenic cardiomyopathy.

**Key Parameters:**

- `bipolar voltage threshold: <0.5 mV for low voltage`
- `unipolar voltage threshold: <0.5 mV for low voltage`

**Complexity:** not stated

## Benchmarks

**Tested on:** Electrophysiological data from patients with suspected ACM.

**Results:**

- Identification of abnormal substrates, diagnostic accuracy.

**Compared against:** Traditional imaging techniques such as echocardiography and cardiac MRI.

**Improvement:** EAM may increase sensitivity for detecting ACM compared to imaging alone.

## Implementation Guide

**Data Structures:** Multielectrode catheter data, Electrophysiological mapping data

**Dependencies:** Electrophysiology equipment, Cardiac imaging systems

**Core Operation:**

```python
map = EAM(catheter_data); abnormalities = identify_abnormalities(map);
```

**Watch Out For:**

- Ensure good contact of the mapping catheter to avoid false low-voltage readings.
- Be cautious of differentiating ACM from other conditions like myocarditis.

## Use This When

- Diagnosing patients with frequent PVCs and inconclusive imaging results.
- Assessing patients with suspected arrhythmogenic cardiomyopathy.
- Evaluating patients who have undergone previous catheter ablation without clear diagnosis.

## Don't Use When

- When clear structural abnormalities are evident on imaging.
- In patients without significant arrhythmias or symptoms.

## Key Concepts

electroanatomic mapping, arrhythmogenic cardiomyopathy, premature ventricular contractions, bipolar voltage mapping

## Connects To

- cardiac imaging techniques
- genetic testing for cardiomyopathies
- electrophysiological studies

## Prerequisites

- Understanding of cardiac anatomy
- Familiarity with electrophysiological mapping techniques

## Limitations

- EAM may not detect abnormalities in all patients with ACM.
- Requires specialized equipment and training.

## Open Questions

- What are the long-term outcomes of patients diagnosed with ACM using EAM?
- How can EAM be integrated into standard diagnostic criteria for ACM?

## Abstract

The heart’s electrical signals should be managed by the sinoatrial node, a small mass of specialized tissue located in the upper right atrium, a major traffic area. Oxygen depleted blood from all over the body passes through the vena cava into the right atrium. From this perch, the sinoatrial node sends out an electrical signal that initiates each heart beat. If PVCs are present, then something is happening to that electrical signal between its origin and its destination. Maybe an interception of the electrical signal from another tissue mass in the heart? Another signal location trying to take over the sinoatrial turf? Did it make any enemies recently? PVCs aren't necessarily life threatening, and in many cases, they don't warrant treatment. Her previous team however, decided to play it safe. They initiated a catheter ablation, the insertion of a catheter with a heating element to burn away any tissues that could be
