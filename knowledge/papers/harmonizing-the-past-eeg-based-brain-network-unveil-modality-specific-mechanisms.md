# Harmonizing the past: EEG-based brain network unveil modality-specific mechanisms of nostalgia

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3389/fpsyg.2025.1517449` |
| Full Paper | [https://doi.org/10.3389/fpsyg.2025.1517449](https://doi.org/10.3389/fpsyg.2025.1517449) |
| Source | [https://journalclub.io/episodes/harmonizing-the-past-eeg-based-brain-network-unveil-modality-specific-mechanisms-of-nostalgia](https://journalclub.io/episodes/harmonizing-the-past-eeg-based-brain-network-unveil-modality-specific-mechanisms-of-nostalgia) |
| Year | 2026 |
| Citations | 0 |
| Authors |  |
| Paper ID | `8f710ae1-f6fe-40ea-878a-7aebbd4721aa` |

## Classification

- **Problem Type:** emotional response analysis
- **Domain:** Machine Learning & AI
- **Sub-domain:** Neuroscience and Emotional Computing
- **Technique:** Weighted Phase Lag Index (WPLI)
- **Technique Category:** statistical_method
- **Type:** novel

## Summary

This research investigates the emotional and neural effects of nostalgia through various sensory channels using EEG measurements. Engineers should care because it provides insights into how different modalities can enhance emotional responses, which can be applied in therapeutic tools and multimedia applications.

## Key Contribution

**The study demonstrates that audiovisual stimuli elicit stronger nostalgic emotions and neural responses compared to auditory or visual stimuli alone.**

## Problem

Understanding how different sensory modalities influence emotional experiences, particularly nostalgia, to improve emotional well-being.

## Method

**Approach:** The method involves presenting participants with nostalgic and non-nostalgic stimuli through auditory, visual, and audiovisual channels while recording their EEG. The emotional responses are measured using subjective scales, and the neural activity is analyzed using WPLI to assess brain connectivity.

**Algorithm:**

1. 1. Select nostalgic and non-nostalgic stimuli based on participant feedback.
2. 2. Present stimuli through auditory, visual, and audiovisual channels.
3. 3. Record EEG data during stimulus presentation.
4. 4. Measure emotional responses using Likert scales.
5. 5. Preprocess EEG data (filtering, artifact removal).
6. 6. Calculate WPLI to assess functional connectivity.
7. 7. Analyze emotional response data using ANOVA.

**Input:** EEG signals from participants, emotional response ratings from Likert scales.

**Output:** Analysis of emotional responses and brain connectivity metrics.

**Key Parameters:**

- `number_of_participants: 38`
- `stimulus_duration: 30-40 seconds`
- `EEG_channels: 64`
- `frequency_bands: Delta (1-4 Hz), Theta (4-8 Hz), Alpha (8-13 Hz), Beta (13-30 Hz), Gamma (30-50 Hz)`

**Complexity:** not stated

## Benchmarks

**Tested on:** EEG data from 36 participants, emotional response ratings from 257 valid questionnaires

**Results:**

- pleasure, arousal, dominance ratings
- WPLI values for brain connectivity

**Compared against:** non-nostalgic stimuli responses

**Improvement:** Nostalgic stimuli elicited significantly higher emotional responses (e.g., pleasure: 7.13 vs 4.91 for auditory).

## Implementation Guide

**Data Structures:** EEG data arrays, emotional response matrices

**Dependencies:** EEG recording devices, data analysis software (e.g., SPSS)

**Core Operation:**

```python
for each stimulus in stimuli: record EEG; measure emotional response; calculate WPLI;
```

**Watch Out For:**

- Ensure participants have no prior exposure to the stimuli to avoid bias.
- Carefully preprocess EEG data to remove artifacts for accurate analysis.
- Be aware of individual differences in nostalgia triggers.

## Use This When

- Designing applications that leverage nostalgia for emotional engagement.
- Creating therapeutic tools that utilize music and imagery for emotional well-being.
- Conducting research on emotional responses to multimedia stimuli.

## Don't Use When

- The target audience has no emotional connection to the stimuli.
- The application requires real-time processing of emotional responses.
- The focus is solely on visual or auditory stimuli without integration.

## Key Concepts

nostalgia, EEG, emotional response, multisensory integration, brain connectivity, WPLI, cognitive processing

## Connects To

- emotional computing
- neuroscience
- multisensory processing
- psychological interventions

## Prerequisites

- basic understanding of EEG technology
- knowledge of emotional psychology
- familiarity with statistical analysis methods

## Limitations

- Findings may not generalize beyond the studied demographic
- Potential variability in individual nostalgia triggers
- EEG data quality can be affected by external noise

## Open Questions

- How can nostalgia be effectively integrated into digital media for therapeutic purposes?
- What are the long-term effects of nostalgia on emotional health?

## Abstract

You’re at a bar with your friends, having a few drinks. There’s a DJ in the corner going through the Top 40. Not terrible, but not great, so you’re not paying much attention to the music. Then, all of a sudden they put on that song. That song from childhood, or from middle school or from high school. The song that you can remember hearing and singing along with for the first time all those years ago. The song that takes you right back to that time and place. You and your friends jump off the bar stools and hit the dance floor. The party is on.
