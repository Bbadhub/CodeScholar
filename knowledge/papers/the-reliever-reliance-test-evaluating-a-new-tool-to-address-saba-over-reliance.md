# The Reliever Reliance Test: evaluating a new tool to address SABA over-reliance

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1038/s41533-024-00389-4` |
| Full Paper | [https://doi.org/10.1038/s41533-024-00389-4](https://doi.org/10.1038/s41533-024-00389-4) |
| Source | [https://journalclub.io/episodes/the-reliever-reliance-test-evaluating-a-new-tool-to-address-saba-over-reliance](https://journalclub.io/episodes/the-reliever-reliance-test-evaluating-a-new-tool-to-address-saba-over-reliance) |
| Year | 2026 |
| Citations | 0 |
| Authors |  |
| Paper ID | `184e1fd1-c664-48e7-8d8d-9daf1a44ca4d` |

## Classification

- **Problem Type:** behavior change intervention for asthma management
- **Domain:** Healthcare & Patient Management
- **Sub-domain:** Behavior Change Interventions
- **Technique:** Reliever Reliance Test (RRT)
- **Technique Category:** framework
- **Type:** novel

## Summary

The Reliever Reliance Test (RRT) is a self-completed behavior-change tool designed to identify and address over-reliance on short-acting beta2-agonists (SABA) among asthma patients. It has shown effectiveness in raising awareness about SABA overuse and encouraging patients to consult healthcare professionals about their asthma treatment.

## Key Contribution

**The RRT effectively identifies patients at risk of SABA over-reliance and motivates them to seek treatment reviews with healthcare professionals.**

## Problem

Patients with asthma often over-rely on SABA inhalers, leading to poor asthma control and increased health risks.

## Method

**Approach:** The RRT incorporates the SABA Reliance Questionnaire (SRQ) to assess patients' reliance on SABA and provides personalized feedback and recommendations. It encourages patients to reflect on their beliefs about SABA and prompts them to discuss their treatment with healthcare professionals.

**Algorithm:**

1. 1. Patient completes the RRT online.
2. 2. Calculate the SRQ score based on responses to 5 items.
3. 3. Classify the risk of SABA over-reliance as low, medium, or high based on the SRQ score.
4. 4. Provide personalized feedback and recommendations based on the risk classification.
5. 5. Encourage patients to discuss their treatment with healthcare professionals.

**Input:** Responses to the SABA Reliance Questionnaire (SRQ), which includes 5 items scored on a Likert scale.

**Output:** Risk classification (low, medium, high) and personalized feedback regarding SABA use.

**Key Parameters:**

- `SRQ items: 5-item scale`
- `Risk classification thresholds: low (<10), medium (11-17), high (18-25)`

**Complexity:** not stated

## Benchmarks

**Tested on:** Data from 670 participants in Argentina, with 93 completing the RRT.

**Results:**

- SABA over-reliance classification: 82% classified as medium-to-high risk.
- Intention to consult a doctor: 75% of medium-to-high risk participants.

**Compared against:** Comparison with previous studies on patient behavior change regarding asthma treatment.

**Improvement:** 75% of participants intended to make an appointment with a doctor after completing the RRT.

## Implementation Guide

**Data Structures:** Patient responses to the SRQ, Risk classification data

**Dependencies:** Web-based platform for RRT delivery, Survey tools (e.g., Qualtrics)

**Core Operation:**

```python
if patient completes_RRT: classify_risk = calculate_SRQ(patient.responses); provide_feedback(classify_risk)
```

**Watch Out For:**

- Ensure patients understand the importance of discussing results with healthcare professionals.
- Be aware of potential anxiety in patients regarding their reliance on SABA.
- Monitor for patients who may not follow through on their intentions to seek help.

## Use This When

- Patients exhibit high reliance on SABA for asthma management.
- There is a need to educate patients about the risks of SABA overuse.
- Healthcare professionals want to facilitate discussions about asthma treatment options.

## Don't Use When

- Patients are already well-controlled on their asthma treatment.
- Patients have limited access to alternative asthma treatments.
- Patients are not digitally literate and cannot complete the RRT online.

## Key Concepts

SABA over-reliance, behavior change, patient education, asthma management, self-assessment tool

## Connects To

- SABA Reliance Questionnaire (SRQ)
- Behavior Change Techniques
- Patient Education Strategies

## Prerequisites

- Understanding of asthma management guidelines
- Knowledge of behavior change theories
- Familiarity with patient engagement strategies

## Limitations

- Small sample size
- Self-reported data may introduce bias
- Limited exploration of accessibility issues for alternative treatments

## Open Questions

- How can the RRT be adapted for use in different cultural contexts?
- What long-term behavior changes result from using the RRT?

## Abstract

You’re short of breath, and a little light headed. Your chest feels tight, and you can feel that familiar wheezing fit starting to come on. You know what to do. Rummage through your bag until you find it. There it is. Remove the cap, shake it a little, try to breathe out, then put it to your lips. Breathe in, as you press down on the little canister. Hold your breath for a few seconds, and wait. Did it work? If not, try another round. If you suffer, or have ever suffered from asthma, I’m sure this sounded familiar. At times your SABA inhaler just might have been your best friend. Unfortunately, as we’ll explore in today's episode, overusing it has consequences. It might not be helping in the long run, it might actually be slowly making things worse. For many, the use of SABA is more than a medicine, it’s a ritual. But, if a ritual isn’t helping us, then it needs to change. But how? What is the
