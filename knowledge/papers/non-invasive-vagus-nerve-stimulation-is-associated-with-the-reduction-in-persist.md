# Non-invasive vagus nerve stimulation is associated with the reduction in persistent post-concussion symptoms: an observational study

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3389/fneur.2025.1642034` |
| Full Paper | [https://doi.org/10.3389/fneur.2025.1642034](https://doi.org/10.3389/fneur.2025.1642034) |
| Source | [https://journalclub.io/episodes/non-invasive-vagus-nerve-stimulation-is-associated-with-the-reduction-in-persistent-post-concussion-symptoms-an-observational-study](https://journalclub.io/episodes/non-invasive-vagus-nerve-stimulation-is-associated-with-the-reduction-in-persistent-post-concussion-symptoms-an-observational-study) |
| Year | 2026 |
| Citations | 0 |
| Authors |  |
| Paper ID | `a7670ed0-a431-4986-a1fb-c1bfac301992` |

## Classification

- **Problem Type:** symptom management in traumatic brain injury
- **Domain:** Bioinformatics & Health
- **Sub-domain:** Traumatic Brain Injury Treatment
- **Technique:** Non-invasive Vagus Nerve Stimulation (nVNS)
- **Technique Category:** treatment_protocol
- **Type:** adaptation

## Summary

This study demonstrates that non-invasive vagus nerve stimulation (nVNS) can significantly reduce persistent post-concussion symptoms in patients with mild traumatic brain injury (mTBI). Engineers should care because this approach offers a practical, safe, and effective intervention that could be integrated into clinical practice for managing TBI-related symptoms.

## Key Contribution

**Adjunctive nVNS is associated with significant reductions in post-concussive symptom severity across multiple domains in mTBI patients.**

## Problem

Persistent cognitive, emotional, and somatic symptoms following mild traumatic brain injury (mTBI) disrupt daily functioning and are often resistant to standard rehabilitative care.

## Method

**Approach:** The method involves using a non-invasive device to stimulate the vagus nerve, which activates the cholinergic anti-inflammatory pathway. Patients use the device daily for symptom management, with treatment effects assessed through the Neurobehavioral Symptom Inventory (NSI).

**Algorithm:**

1. 1. Patient completes baseline NSI assessment.
2. 2. Patient is prescribed gammaCore™ device for nVNS.
3. 3. Patient is trained to use the device over the cervical pulse point.
4. 4. Patient uses the device for 2 minutes, twice in the morning and twice in the evening.
5. 5. Follow-up NSI assessment is conducted approximately 112 days post-treatment initiation.
6. 6. Analyze changes in NSI scores to evaluate treatment efficacy.

**Input:** Patient symptom data collected via the Neurobehavioral Symptom Inventory (NSI).

**Output:** Change in NSI scores indicating symptom severity before and after nVNS treatment.

**Key Parameters:**

- `stimulation_duration: 2 minutes`
- `stimulation_frequency: 25 Hz`
- `intensity: up to 60 milliamps`
- `voltage: 24 volts`
- `treatment_frequency: 4 sessions per day`

**Complexity:** not stated

## Benchmarks

**Tested on:** 102 patients with mTBI treated with nVNS

**Results:**

- NSI total score change: from 45.80 to 36.08
- p-values for symptom improvements: headache (p = 1.97 × 10−8), concentration (p = 1.79 × 10−5), dizziness (p = 7.11 × 10−5), depression (p = 9.09 × 10−5)

**Compared against:** Patients with mTBI receiving standard care without nVNS

**Improvement:** Significant reductions in 16 out of 22 NSI symptom domains, with 34% of patients meeting responder criteria for at least half of the assessed symptoms.

## Implementation Guide

**Data Structures:** Patient symptom data, NSI assessment scores

**Dependencies:** gammaCore™ device for nVNS, clinical assessment tools for NSI

**Core Operation:**

```python
if patient.symptoms == 'mTBI': initiate_nVNS(treatment_protocol)
```

**Watch Out For:**

- Ensure proper device placement for effective stimulation.
- Monitor patient compliance with daily usage.
- Be aware of potential variability in symptom reporting.

## Use This When

- Managing persistent post-concussion symptoms in patients with mTBI.
- Integrating adjunctive therapies into standard care for TBI.
- Seeking non-pharmacological interventions for symptom relief.

## Don't Use When

- Patients have contraindications such as implanted pacemakers.
- Immediate acute care is required for severe TBI symptoms.
- Patients are not compliant with treatment protocols.

## Key Concepts

vagus nerve stimulation, neuroinflammation, post-concussion syndrome, cholinergic anti-inflammatory pathway, mild traumatic brain injury, Neurobehavioral Symptom Inventory

## Connects To

- vagus nerve stimulation techniques
- neuroinflammatory response treatments
- cognitive rehabilitation therapies

## Prerequisites

- Understanding of vagus nerve anatomy
- Knowledge of neuroinflammatory processes
- Familiarity with clinical assessment tools

## Limitations

- Retrospective observational study design limits causal inference.
- Heterogeneity in patient symptom profiles may affect generalizability.
- Long-term effects of nVNS treatment are not established.

## Open Questions

- What are the long-term effects of nVNS on chronic TBI symptoms?
- How does nVNS interact with other therapeutic interventions?

## Abstract

The vagus nerve is like your body's built-in anti-inflammatory highway. It runs from your brainstem down through your neck and into your chest and abdomen, carrying signals that help regulate everything from your heart rate to your digestive system. And when you stimulate the vagus nerve, it activates what researchers call the "cholinergic anti-inflammatory pathway."
