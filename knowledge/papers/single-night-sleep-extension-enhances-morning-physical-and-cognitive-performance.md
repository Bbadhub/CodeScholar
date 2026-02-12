# Single-Night Sleep Extension Enhances Morning Physical and Cognitive Performance Across Time of Day in Physically Active University Students: A Randomized Crossover Study

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3390/life15081178` |
| Full Paper | [https://doi.org/10.3390/life15081178](https://doi.org/10.3390/life15081178) |
| Source | [https://journalclub.io/episodes/single-night-sleep-extension-enhances-morning-physical-and-cognitive-performance-across-time-of-day-in-physically-active-university-students-a-randomized-crossover-study](https://journalclub.io/episodes/single-night-sleep-extension-enhances-morning-physical-and-cognitive-performance-across-time-of-day-in-physically-active-university-students-a-randomized-crossover-study) |
| Year | 2026 |
| Citations | 0 |
| Authors |  |
| Paper ID | `880f8973-49c2-48e8-a60f-aeeed9bcb0e0` |

## Classification

- **Problem Type:** performance optimization
- **Domain:** Health and Sports Science
- **Sub-domain:** Sleep Optimization
- **Technique:** Sleep Extension Protocol
- **Technique Category:** intervention strategy
- **Type:** novel

## Summary

This study demonstrates that a single night of sleep extension significantly enhances physical and cognitive performance in physically active university students, particularly during morning assessments. Engineers should care because this research provides insights into optimizing performance through non-pharmacological means, which can be applied in various fields such as sports science and health technology.

## Key Contribution

**Establishing sleep extension as an effective strategy for improving physical and cognitive performance across different times of day.**

## Problem

The need to enhance physical and cognitive performance in physically active individuals through improved sleep strategies.

## Method

**Approach:** The method involves extending sleep duration by adjusting bedtimes to increase total sleep time. Performance assessments are conducted under both normal sleep and sleep extension conditions to evaluate the effects on physical and cognitive tasks.

**Algorithm:**

1. 1. Recruit participants and ensure they meet inclusion criteria.
2. 2. Randomly assign participants to normal sleep and sleep extension conditions with a washout period.
3. 3. Monitor sleep using wrist actigraphy to measure total sleep time.
4. 4. Conduct performance assessments at specified times (8 PM, 8 AM, 4 PM).
5. 5. Compare performance metrics between conditions.

**Input:** Participant sleep data (wrist actigraphy), performance test results.

**Output:** Performance metrics (e.g., shuttle-run distance, reaction times) under different sleep conditions.

**Key Parameters:**

- `bedtime: 21:00 (sleep extension), 22:30 (normal sleep)`
- `wake time: 07:00 (both conditions)`
- `total sleep time: 531.3 ± 56.8 min (extension), 476.5 ± 64.2 min (normal)`

**Complexity:** not stated

## Benchmarks

**Tested on:** 24 physically active university students (17 males, 7 females)

**Results:**

- 5 m shuttle-run best distance: 102.8 ± 11.9 m (EXT) vs. 93.3 ± 8.5 m (NS)
- squat-jump height: 28.2 ± 8.0 cm (EXT) vs. 26.3 ± 7.2 cm (NS)
- simple reaction time: 252.8 ± 55.3 ms (EXT) vs. 296.4 ± 75.2 ms (NS)
- digit-cancellation performance: 67.6 ± 12.6 (EXT) vs. 63.0 ± 10.0 (NS)

**Compared against:** Normal Sleep (NS) performance metrics

**Improvement:** Significant improvements in performance metrics, e.g., 9.5 m increase in shuttle-run best distance at 8 AM.

## Implementation Guide

**Data Structures:** Participant sleep data records, Performance test results database

**Dependencies:** ActiGraph for actigraphy data, Statistical software (e.g., SPSS, Python) for analysis

**Core Operation:**

```python
if sleep_extension: measure_performance() else: measure_performance()
```

**Watch Out For:**

- Ensure participants adhere to the sleep schedule to avoid data variability.
- Monitor for external factors that may influence performance (e.g., diet, stress).
- Validate actigraphy data with subjective sleep reports to ensure accuracy.

## Use This When

- Designing interventions to enhance athletic performance through sleep management.
- Developing health applications focused on sleep tracking and optimization.
- Creating training programs for physically active individuals aiming to improve performance.

## Don't Use When

- When working with individuals who have chronic sleep disorders.
- In scenarios where sleep duration cannot be manipulated due to lifestyle constraints.
- For populations that do not engage in regular physical activity.

## Key Concepts

sleep extension, performance optimization, cognitive function, physical performance, actigraphy, circadian rhythms

## Connects To

- Chronobiology studies
- Sleep quality assessment tools
- Performance enhancement strategies in sports science

## Prerequisites

- Understanding of sleep physiology
- Knowledge of performance testing protocols
- Familiarity with actigraphy and sleep monitoring techniques

## Limitations

- Results may not generalize to non-physically active populations.
- Short duration of sleep extension may limit long-term applicability.
- Potential variability in individual responses to sleep extension.

## Open Questions

- What are the long-term effects of repeated sleep extension on performance?
- How do individual differences (e.g., chronotype) affect the efficacy of sleep extension?

## Abstract

To take measurements, the authors used wrist actigraphy devices. These work like activity trackers. They continuously monitor movement patterns to determine when someone is asleep versus awake. It uses accelerometers to detect the movements that occur during different sleep stages, then applies algorithms to translate movement data into sleep metrics. These measurements are designed (in theory) to eliminate the reliability issues that come with self-reported sleep data. Though it's worth noting that actigraphy can sometimes misclassify quiet wakefulness as sleep. That is: the device might not know the difference between zoning-out watching TV or actually taking a nap.
