# Cognitive Style and Visual Attention in Multimodal Museum Exhibitions: An Eye-Tracking Study on Visitor Experience

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3390/buildings15162968` |
| Full Paper | [https://doi.org/10.3390/buildings15162968](https://doi.org/10.3390/buildings15162968) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/df637e41a286b4e72c917e11d0dfefce27ad87cd](https://www.semanticscholar.org/paper/df637e41a286b4e72c917e11d0dfefce27ad87cd) |
| Source | [https://journalclub.io/episodes/cognitive-style-and-visual-attention-in-multimodal-museum-exhibitions-an-eye-tracking-study-on-visitor-experience](https://journalclub.io/episodes/cognitive-style-and-visual-attention-in-multimodal-museum-exhibitions-an-eye-tracking-study-on-visitor-experience) |
| Source | [https://www.semanticscholar.org/paper/df637e41a286b4e72c917e11d0dfefce27ad87cd](https://www.semanticscholar.org/paper/df637e41a286b4e72c917e11d0dfefce27ad87cd) |
| Year | 2026 |
| Citations | 4 |
| Authors | Wenjia Shi, Mengcai Zhou, Kenta Ono |
| Paper ID | `2582a60e-a38f-486a-bc85-9858f30c843f` |

## Classification

- **Problem Type:** cognitive style influence on information processing in multimodal environments
- **Domain:** Human-Computer Interaction
- **Sub-domain:** Cognitive Style and User Experience Design
- **Technique:** Eye-Tracking Analysis
- **Technique Category:** statistical_method
- **Type:** comparison

## Summary

This study investigates how cognitive styles (visualizer vs. verbalizer) influence visual attention and comprehension in multimodal museum exhibitions using eye-tracking technology. Engineers should care because the findings provide insights for designing cognitively adaptive exhibition interfaces that enhance visitor engagement and learning outcomes.

## Key Contribution

**Empirical evidence demonstrating the impact of cognitive style on visual attention patterns and comprehension in museum environments.**

## Problem

Visitors in museums often engage with complex, multimodal content, and understanding how cognitive styles affect their interaction can improve exhibition design.

## Method

**Approach:** Participants are classified as visualizers or verbalizers and engage with multimodal exhibition content while their eye movements are tracked. The data collected includes fixation durations and transition patterns to assess how cognitive style influences visual processing behavior.

**Algorithm:**

1. 1. Classify participants as visualizers or verbalizers using questionnaires.
2. 2. Present exhibition content under varying complexity levels.
3. 3. Record eye movements using an eye-tracking device.
4. 4. Analyze fixation durations and counts for different content types.
5. 5. Conduct statistical analysis to compare visual attention patterns.
6. 6. Evaluate knowledge acquisition through retention and transfer tests.

**Input:** Exhibition content consisting of artifacts, images, text descriptions, and videos presented in varying complexity levels.

**Output:** Data on eye movement patterns, including total fixation duration, fixation count, and knowledge assessment scores.

**Key Parameters:**

- `sampling_rate: 2000 Hz`
- `display_resolution: 1280 x 1024 pixels`
- `number_of_participants: 54`
- `complexity_levels: 3 (low, moderate, high)`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Eye-tracking data from 54 participants interacting with six artifacts from Liangzhu culture.

**Results:**

- Total Fixation Duration (TFD), Fixation Count (FC), Pupil Size (PS), Retention Test Scores, Transfer Test Scores.

**Compared against:** Previous studies on visual attention in museum contexts.

**Improvement:** Not stated

## Implementation Guide

**Data Structures:** Data structures for storing eye-tracking metrics and participant responses.

**Dependencies:** Eye-tracking hardware (e.g., EyeLink1000), data analysis software (e.g., Jamovi, Eyelink Data View).

**Core Operation:**

```python
track_eye_movements(participant) -> analyze_fixation_data() -> generate_report()
```

**Watch Out For:**

- Ensure accurate calibration of eye-tracking equipment.
- Control for external distractions during the experiment.
- Be aware of individual differences in cognitive load and prior knowledge.

## Use This When

- Designing museum exhibitions that cater to diverse cognitive styles.
- Evaluating the effectiveness of multimodal content in educational settings.
- Researching user interaction patterns in complex information environments.

## Don't Use When

- The exhibition content is purely textual or visual without multimodal elements.
- Resources for eye-tracking technology are unavailable.
- The target audience has a uniform cognitive style.

## Key Concepts

Cognitive Style, Eye-Tracking, Multimodal Learning, Visitor Engagement, Information Processing

## Connects To

- Cognitive Load Theory
- Multimedia Learning Theory
- User Experience Research
- Educational Psychology

## Prerequisites

- Understanding of cognitive psychology principles.
- Familiarity with eye-tracking technology.
- Knowledge of statistical analysis methods.

## Limitations

- Findings may not generalize beyond the specific cultural context of Liangzhu artifacts.
- Limited sample size may affect statistical power.
- Potential biases in self-reported cognitive style assessments.

## Open Questions

- How can exhibition design be further optimized for mixed cognitive styles?
- What other factors influence visitor engagement in museum settings?

## Abstract

Human cognition isn't one-size-fits-all. According to dual-coding theory, we process information through two distinct channels: visual and verbal. Some people lean heavily toward visual processing, these are the visualizers. Others prefer linguistic and textual information, those are the verbalizers.
