# A Randomized, Double-Blind, Placebo-Controlled Trial to Assess the Effectiveness and Safety of Melatonin and Three Formulations of Floraworks Proprietary TruCBN for Improving Sleep

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3390/ph17080977` |
| Full Paper | [https://doi.org/10.3390/ph17080977](https://doi.org/10.3390/ph17080977) |
| Source | [https://journalclub.io/episodes/a-randomized-double-blind-placebo-controlled-trial-to-assess-the-effectiveness-and-safety-of-melatonin-and-three-formulations-of-floraworks-proprietary-trucbn-for-improving-sleep](https://journalclub.io/episodes/a-randomized-double-blind-placebo-controlled-trial-to-assess-the-effectiveness-and-safety-of-melatonin-and-three-formulations-of-floraworks-proprietary-trucbn-for-improving-sleep) |
| Year | 2026 |
| Citations | 0 |
| Authors |  |
| Paper ID | `001976fa-7383-495a-be91-016d5f98b1ef` |

## Classification

- **Problem Type:** sleep quality improvement
- **Domain:** Bioinformatics & Health
- **Sub-domain:** Sleep Disorders
- **Technique:** TruCBN™
- **Technique Category:** pharmaceutical formulation
- **Type:** novel

## Summary

This study assessed the effectiveness and safety of three formulations of TruCBN™ (cannabinol) for improving sleep quality compared to a placebo and melatonin. Engineers should care because it provides insights into alternative sleep aids that could inform product development in health and wellness applications.

## Key Contribution

**Demonstrated that orally ingested CBN is a safe and effective alternative for improving sleep quality compared to placebo and comparable to melatonin.**

## Problem

Many individuals suffer from sleep disturbances due to disrupted circadian rhythms, impacting their overall well-being.

## Method

**Approach:** The study involved a randomized, double-blind, placebo-controlled trial where participants were assigned to receive one of four softgel formulations (melatonin or varying doses of CBN) or a placebo. Participants reported their sleep quality and other health metrics through online surveys over six weeks.

**Algorithm:**

1. 1. Recruit participants and obtain informed consent.
2. 2. Randomly assign participants to one of five groups: placebo, 4 mg melatonin, 25 mg CBN, 50 mg CBN, or 100 mg CBN.
3. 3. Instruct participants to take one softgel 1-2 hours before bedtime.
4. 4. Collect baseline health outcome assessments using validated measures.
5. 5. Administer weekly online surveys for six weeks to assess sleep quality and side effects.
6. 6. Analyze data using linear mixed-effects regression models.

**Input:** Participants' demographic data, baseline health assessments, and weekly survey responses.

**Output:** Changes in sleep quality, stress, anxiety, pain, and overall well-being scores.

**Key Parameters:**

- `softgel A: 4 mg melatonin`
- `softgel B: 25 mg CBN`
- `softgel C: 50 mg CBN`
- `softgel D: 100 mg CBN`
- `placebo: no active ingredients`

**Complexity:** not stated

## Benchmarks

**Tested on:** Participants' responses to PROMIS Sleep Disturbance 8A, PROMIS Stress 4A, PROMIS Anxiety 4A, and PEG scales.

**Results:**

- sleep quality improvement measured by PROMIS Sleep Disturbance 8A score change
- stress reduction
- anxiety levels
- pain levels
- overall well-being

**Compared against:** placebo group, 4 mg melatonin group

**Improvement:** Significant improvement in sleep quality for all active groups compared to placebo, with no significant differences between active groups and melatonin.

## Implementation Guide

**Data Structures:** Participant demographic data, Survey response data, Health outcome measures

**Dependencies:** Statistical analysis software (e.g., R, Python with Pandas) for data analysis, Survey distribution platform

**Core Operation:**

```python
for each participant in study: collect_data(participant); analyze_data(); report_results();
```

**Watch Out For:**

- Ensure participant compliance with dosage instructions.
- Monitor for potential side effects and interactions with other medications.
- Account for participant dropout rates in analysis.

## Use This When

- Developing alternative sleep aids for consumers seeking non-prescription options.
- Conducting clinical trials for dietary supplements targeting sleep improvement.
- Exploring the effects of cannabinoids on health and wellness.

## Don't Use When

- The target population does not experience sleep disturbances.
- Participants are on medications that may interact negatively with cannabinoids.
- Conducting trials that require in-person monitoring.

## Key Concepts

cannabinol, sleep quality, clinical trial, placebo-controlled, double-blind, phytocannabinoids

## Connects To

- clinical trial design
- cannabinoid pharmacology
- sleep disorder treatments
- patient-reported outcome measures

## Prerequisites

- Understanding of randomized controlled trials
- Knowledge of sleep physiology
- Familiarity with statistical analysis methods

## Limitations

- High dropout rate (26%)
- Limited generalizability due to specific participant criteria
- No significant differences in secondary outcomes compared to placebo

## Open Questions

- What are the long-term effects of CBN on sleep quality?
- How do different formulations of cannabinoids interact with other sleep aids?

## Abstract

Circadian rhythms are your body’s natural 24-hour clock. This internal clock uses hormones to make you feel sleepy and natural steroids to make you feel alert. It is controlled by signals like light and darkness. Light tells your brain to stay alert, and darkness triggers melatonin, the hormone that helps you sleep. Things like jet lag, working night shifts, late-night screen time, or an irregular sleep schedule can change or disrupt your circadian rhythm. If your internal clock is off, you may not get quality sleep at night and then struggle with low energy, grogginess, or trouble concentrating the next day. Over long periods, this pattern can seriously affect your overall well-being. For example, people with chronically disrupted rhythms often report mood changes and stress. Luckily, you have plenty of non-medicinal options to help you get a good night’s sleep. Unfortunately, they aren’t always effective, and you may end up joining the
