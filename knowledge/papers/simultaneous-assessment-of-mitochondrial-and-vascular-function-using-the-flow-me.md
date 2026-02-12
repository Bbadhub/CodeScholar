# Simultaneous assessment of mitochondrial and vascular function using the Flow Mediated Skin Fluorescence technique

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3389/fphys.2025.1509159` |
| Full Paper | [https://doi.org/10.3389/fphys.2025.1509159](https://doi.org/10.3389/fphys.2025.1509159) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/b8a05e8310350ce6b48103b6f51f521af892246e](https://www.semanticscholar.org/paper/b8a05e8310350ce6b48103b6f51f521af892246e) |
| Source | [https://journalclub.io/episodes/simultaneous-assessment-of-mitochondrial-and-vascular-function-using-the-flow-mediated-skin-fluorescence-technique](https://journalclub.io/episodes/simultaneous-assessment-of-mitochondrial-and-vascular-function-using-the-flow-mediated-skin-fluorescence-technique) |
| Source | [https://www.semanticscholar.org/paper/b8a05e8310350ce6b48103b6f51f521af892246e](https://www.semanticscholar.org/paper/b8a05e8310350ce6b48103b6f51f521af892246e) |
| Year | 2026 |
| Citations | 3 |
| Authors | A. Marcinek, Joanna Katarzyńska, Jerzy Gebicki |
| Paper ID | `2e7fd63a-dc68-40dc-b3be-66e105ad58e5` |

## Classification

- **Problem Type:** diagnostic assessment of mitochondrial and vascular function
- **Domain:** Bioinformatics & Health
- **Sub-domain:** Non-invasive diagnostic techniques
- **Technique:** Flow Mediated Skin Fluorescence (FMSF)
- **Technique Category:** detection_system
- **Type:** novel

## Summary

The paper presents the Flow Mediated Skin Fluorescence (FMSF) technique, a non-invasive method for assessing both mitochondrial and vascular function by measuring NADH fluorescence in skin tissue. Engineers should care because this technique provides a dual assessment of metabolic and circulatory health, which can be critical for diagnosing various diseases.

## Key Contribution

**The ability to simultaneously assess mitochondrial and vascular function using a single measurement technique based on NADH fluorescence.**

## Problem

The need for a reliable diagnostic method that can differentiate between vascular and mitochondrial dysfunction in patients.

## Method

**Approach:** The FMSF technique measures changes in NADH fluorescence from skin tissue in response to post-occlusive reactive hyperemia (PORH). It analyzes the fluorescence signal to derive parameters indicative of mitochondrial and vascular function.

**Algorithm:**

1. 1. Apply a cuff to occlude blood flow in the brachial artery.
2. 2. Measure NADH fluorescence at baseline for 3 minutes.
3. 3. Inflate the cuff to 60 mmHg above systolic blood pressure to induce ischemia.
4. 4. Record changes in NADH fluorescence during ischemia to determine ischemic response (IRmax).
5. 5. Release the cuff and measure the hyperemic response (HRmax) as NADH fluorescence decreases.
6. 6. Analyze the fluorescence signal to derive flowmotion (FM) and hypoxia sensitivity (HS).

**Input:** NADH fluorescence data collected from skin tissue during various stages of blood flow occlusion and reperfusion.

**Output:** Parameters including baseline fluorescence (FLbase), ischemic response (IRmax), hyperemic response (HRmax), flowmotion (FM), and hypoxia sensitivity (HS).

**Key Parameters:**

- `cuff_pressure: 60 mmHg above systolic blood pressure`
- `sampling_frequency: 25 Hz`
- `measurement_duration: 3 minutes for baseline`

**Complexity:** not stated

## Benchmarks

**Tested on:** Patient groups with cardiovascular diseases (CVD) and type 2 diabetes (DM2)

**Results:**

- FLbase: 474 ± 213 (CVD), 657 ± 277 (DM2)
- IRmax: 11.2 ± 5.7 (CVD), 11.5 ± 4.6 (DM2)
- HRmax: 15.5 ± 5.1 (CVD), 15.6 ± 4.4 (DM2)
- log(HS): 1.19 ± 0.54 (CVD), 1.42 ± 0.47 (DM2)

**Compared against:** Laser Doppler flowmetry (LDF), Laser speckle contrast imaging (LSCI), Flow mediated dilation (FMD), Reactive hyperemia peripheral arterial tonometry (RH-PAT)

**Improvement:** Statistically significant differences in parameters between CVD and DM2 groups.

## Implementation Guide

**Data Structures:** NADH fluorescence signal data structure, Patient demographic and clinical data structure

**Dependencies:** Fluorescence measurement devices (e.g., AngioExpert), Data analysis software for signal processing (e.g., FFT algorithms)

**Core Operation:**

```python
measure_nadh_fluorescence(cuff_pressure, duration) -> return parameters (FLbase, IRmax, HRmax, FM, HS)
```

**Watch Out For:**

- Ensure proper calibration for skin type and condition.
- Monitor for patient comfort during measurement to avoid movement artifacts.
- Be aware of the variability in baseline fluorescence due to individual differences.

## Use This When

- Assessing patients for cardiovascular diseases or diabetes.
- Monitoring metabolic health in athletes.
- Evaluating microcirculatory dysfunction in chronic diseases.

## Don't Use When

- When immediate results are required without setup time.
- In patients with skin conditions that may affect fluorescence measurements.

## Key Concepts

NADH fluorescence, ischemic response, hyperemic response, flowmotion, hypoxia sensitivity, microcirculation, vascular dysfunction, mitochondrial dysfunction

## Connects To

- Laser Doppler flowmetry (LDF)
- Laser speckle contrast imaging (LSCI)
- Flow mediated dilation (FMD)
- Reactive hyperemia peripheral arterial tonometry (RH-PAT)

## Prerequisites

- Understanding of fluorescence measurement techniques.
- Knowledge of vascular and mitochondrial physiology.
- Familiarity with signal processing methods.

## Limitations

- Variability in NADH fluorescence due to skin pigmentation and lesions.
- Requires patient immobility during measurement.
- May not differentiate between all types of vascular and mitochondrial dysfunction.

## Open Questions

- How can the FMSF technique be adapted for real-time monitoring?
- What are the long-term effects of using FMSF in diverse patient populations?

## Abstract

In order for a diagnostic method to stand out, we need a method that has a standard unit of measure that is specific and reliable. Flow Mediated Skin Fluorescence (FMSF) can potentially fill this gap. While it has certain disadvantages, new research is finding ways to work around them. Previously, one of the main disadvantages was that FMSF failed to differentiate between vascular and mitochondrial dysfunction. But, in this paper, the authors managed to distinguish one from the other. Let’s dive in to see how this was done. So what is FMSF? It is a non-invasive test that evaluates microcirculation by detecting changes in skin fluorescence. Fluorescence is a phenomenon that occurs when light is absorbed by a molecule and then re-emitted as a different color. This happens because the light absorption excites the electrons in the molecule which causes it to glow. Nicotinamide Adenine Dinucleotide (NAD) is a coenzyme that exists in two
