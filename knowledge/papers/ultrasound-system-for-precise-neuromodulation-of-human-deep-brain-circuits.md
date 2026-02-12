# Ultrasound system for precise neuromodulation of human deep brain circuits

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1038/s41467-025-63020-1` |
| Full Paper | [https://doi.org/10.1038/s41467-025-63020-1](https://doi.org/10.1038/s41467-025-63020-1) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/2f852af96226c01598dcaf5ad427b29816e39f74](https://www.semanticscholar.org/paper/2f852af96226c01598dcaf5ad427b29816e39f74) |
| Source | [https://journalclub.io/episodes/ultrasound-system-for-precise-neuromodulation-of-human-deep-brain-circuits](https://journalclub.io/episodes/ultrasound-system-for-precise-neuromodulation-of-human-deep-brain-circuits) |
| Source | [https://www.semanticscholar.org/paper/2f852af96226c01598dcaf5ad427b29816e39f74](https://www.semanticscholar.org/paper/2f852af96226c01598dcaf5ad427b29816e39f74) |
| Year | 2026 |
| Citations | 25 |
| Authors | Eleanor Martin, Morgan Roberts, Ioana F Grigoras, Olivia Wright, T. Nandi, Sebastian W Rieger |
| Paper ID | `29b3996b-234f-4e5d-8084-f064f573f56b` |

## Classification

- **Problem Type:** non-invasive deep brain stimulation
- **Domain:** Medical Engineering
- **Sub-domain:** Transcranial Ultrasound Stimulation
- **Technique:** Transcranial Ultrasound Stimulation (TUS)
- **Technique Category:** detection_system
- **Type:** novel

## Summary

The paper presents an advanced transcranial ultrasound stimulation (TUS) system that enables precise neuromodulation of deep brain circuits non-invasively. This system allows for targeted stimulation of small brain structures, such as the lateral geniculate nucleus (LGN), which could revolutionize treatments for neurological and psychiatric disorders.

## Key Contribution

**Introduction of a 256-element helmet-shaped transducer array for precise deep brain neuromodulation with real-time fMRI monitoring.**

## Problem

The need for precise targeting of deep brain structures for therapeutic interventions without invasive procedures.

## Method

**Approach:** The method utilizes a 256-element transducer array to deliver ultrasound waves that modulate neuronal activity in deep brain structures. The system is designed for high spatial precision and is compatible with real-time fMRI monitoring to observe neuromodulatory effects.

**Algorithm:**

1. 1. Position participant using a custom-designed stereotactic mask.
2. 2. Use low-dose CT scans to derive participant-specific skull and brain properties.
3. 3. Compute driving parameters for each transducer element using a full-wave acoustic model.
4. 4. Apply TUS to the target area with specified pulse parameters.
5. 5. Monitor brain activity using fMRI during and after stimulation.
6. 6. Adjust stimulation parameters in real-time based on feedback.

**Input:** Participant-specific anatomical data from CT scans and fMRI imaging.

**Output:** Modulated neuronal activity in targeted brain regions, observed through fMRI.

**Key Parameters:**

- `frequency: 555 kHz`
- `target pressure: 775 kPa`
- `pulse duration: 300 ms`
- `pulse interval: 3 s`
- `theta burst stimulation duration: 80 s`
- `theta burst frequency: 5 Hz`

**Complexity:** not stated

## Benchmarks

**Tested on:** Human participants' fMRI data during visual tasks

**Results:**

- visual cortex activity increase during TUS: significant
- decrease in visual cortex activity post-TUS: significant at 40 min

**Compared against:** Sham stimulation with no ultrasound delivered

**Improvement:** Significant increase in task-related activity in the visual cortex during active TUS compared to sham.

## Implementation Guide

**Data Structures:** 256-element transducer array, stereotactic face and neck mask, acoustic model parameters

**Dependencies:** MRI scanner, custom software for treatment planning (k-Plan)

**Core Operation:**

```python
apply_TUS(target_region, parameters) -> monitor_fMRI()
```

**Watch Out For:**

- Ensure precise alignment between the participant's head and transducer array.
- Account for skull attenuation and aberration in treatment planning.
- Monitor for potential motion artifacts during fMRI scans.

## Use This When

- You need to target deep brain structures non-invasively.
- You want to study the effects of neuromodulation on brain function.
- You are developing therapies for neurological disorders.

## Don't Use When

- You require immediate invasive intervention.
- You are targeting superficial cortical regions with high angles of incidence.

## Key Concepts

transcranial ultrasound, neuromodulation, real-time fMRI, deep brain stimulation, theta burst stimulation, spatial precision, individualized treatment planning

## Connects To

- Deep Brain Stimulation (DBS)
- Transcranial Magnetic Stimulation (TMS)
- MR-guided Focused Ultrasound (MRgFUS)

## Prerequisites

- Understanding of ultrasound physics
- Knowledge of brain anatomy
- Familiarity with fMRI technology

## Limitations

- Requires precise participant positioning for effective targeting.
- Potential challenges in targeting superficial cortical regions.
- Limited to specific brain structures based on the array design.

## Open Questions

- What are the long-term effects of TUS on brain function?
- Can this system be adapted for other neurological conditions?

## Abstract

Imagine that you're a neurosurgeon, and you’re trying to treat a patient with severe depression. Your target is a tiny brain structure buried deep in the skull, smaller than a grape. Your only options are to either drill through the skull and insert electrodes, or give up on precision entirely and just use drugs instead. The issue is that the drugs will affect the whole brain. Neither option is ideal. But what if there was a third way? What if you could reach that deep brain structure without breaking the skin, and target it with precision?
