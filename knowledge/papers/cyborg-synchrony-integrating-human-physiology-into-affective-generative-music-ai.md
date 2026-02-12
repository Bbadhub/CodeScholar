# Cyborg synchrony: integrating human physiology into affective generative music AI

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3389/fcomp.2025.1593905` |
| Full Paper | [https://doi.org/10.3389/fcomp.2025.1593905](https://doi.org/10.3389/fcomp.2025.1593905) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/67a25e30620c7349226c169c2623b6203df61348](https://www.semanticscholar.org/paper/67a25e30620c7349226c169c2623b6203df61348) |
| Source | [https://journalclub.io/episodes/cyborg-synchrony-integrating-human-physiology-into-affective-generative-music-ai](https://journalclub.io/episodes/cyborg-synchrony-integrating-human-physiology-into-affective-generative-music-ai) |
| Source | [https://www.semanticscholar.org/paper/67a25e30620c7349226c169c2623b6203df61348](https://www.semanticscholar.org/paper/67a25e30620c7349226c169c2623b6203df61348) |
| Year | 2026 |
| Citations | 0 |
| Authors | Senaida Ng, Kaia Sargent, Jason J. Snell |
| Paper ID | `27543198-fc6d-4dd1-a9ad-83357607b65e` |

## Classification

- **Problem Type:** interpersonal musical biofeedback
- **Domain:** Machine Learning & AI
- **Sub-domain:** Affective Computing, Music Information Retrieval
- **Technique:** Affective Generative Music AI (AGM-AI)
- **Technique Category:** framework
- **Type:** novel

## Summary

The paper proposes an Affective Generative Music AI (AGM-AI) framework that integrates human physiological data to create personalized music experiences that promote synchrony and emotional bonding between users. Engineers should care because this approach offers a novel way to enhance interpersonal communication through music, leveraging real-time biometric feedback.

## Key Contribution

**Introduction of a dual-layer AI system that combines a Foundational Model with Individualized Tuning to create personalized, synchronizable musical experiences based on real-time physiological data.**

## Problem

The need for AI systems that foster meaningful social interactions through shared physiological experiences.

## Method

**Approach:** The AGM-AI framework consists of two stages: a Foundational Model that learns from diverse physiological responses to music, and Individualized Tuning that adapts the system to each user's unique responses. This allows for real-time generation of music that aligns with users' physiological states.

**Algorithm:**

1. 1. Collect physiological data (EEG, ECG, GSR, motion) while participants listen to music.
2. 2. Analyze musical features (tempo, loudness, timbre, harmony, rhythm) using signal preprocessing and feature extraction.
3. 3. Train a neural network on synchronized datasets to form the Foundational Model.
4. 4. For Individualized Tuning, collect user-specific biometric responses to the Foundational Model music.
5. 5. Identify outlier responses and adapt the Local Adaptation Layer to refine music generation.
6. 6. Generate music in real-time based on live biometric data using AI-driven synthesis.
7. 7. Facilitate interpersonal synchronization by sharing biometric data between users.

**Input:** Real-time physiological data from users (EEG, ECG, GSR, motion sensors) and musical features from a curated music library.

**Output:** Dynamically generated music that aligns with users' physiological states to enhance synchrony.

**Key Parameters:**

- `sampling_rate: varies by sensor (e.g., EEG: 256 Hz, ECG: 500 Hz)`
- `window_length: variable based on analysis needs`
- `feature_extraction_methods: Short-Time Fourier Transform, RMS energy, chroma features`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Physiological responses from over 1,000 diverse participants listening to a curated music library.

**Results:**

- Physiological synchrony measures (e.g., heart rate alignment, EEG coherence)
- User satisfaction and emotional bonding assessments

**Compared against:** Existing biofeedback music systems (e.g., Muse EEG Headband, Brain.fm)

**Improvement:** Not stated

## Implementation Guide

**Data Structures:** Neural network models for Foundational and Individualized Tuning layers, Data structures for storing physiological and musical feature data

**Dependencies:** TensorFlow or PyTorch for neural network implementation, Signal processing libraries for audio analysis (e.g., Librosa)

**Core Operation:**

```python
music = generate_music(biometric_data, foundational_model, local_adaptation_layer)
```

**Watch Out For:**

- Ensure accurate synchronization of biometric data with music events.
- Be cautious of overfitting the Individualized Tuning model to outlier responses.
- Consider ethical implications of using biometric data in social contexts.

## Use This When

- Developing applications for enhancing interpersonal communication through music.
- Creating therapeutic tools for mental health that leverage physiological data.
- Designing interactive art installations that respond to audience biometrics.

## Don't Use When

- When the focus is solely on individual music experiences without social interaction.
- In scenarios where real-time biometric data collection is not feasible.
- For applications requiring strict emotional categorization rather than fluid adaptation.

## Key Concepts

physiological synchrony, biofeedback, Affective Computing, music generation, neural networks, real-time adaptation

## Connects To

- Affective Computing frameworks
- Music Information Retrieval techniques
- Biofeedback systems
- Generative music algorithms

## Prerequisites

- Understanding of neural networks and machine learning principles
- Familiarity with physiological data collection methods
- Knowledge of music theory and audio signal processing

## Limitations

- The Foundational Model may not capture individual variability in physiological responses.
- Potential data fidelity issues due to environmental influences on biometric signals.
- Ethical concerns regarding dependency on AI for social bonding.

## Open Questions

- How can the system be adapted for diverse cultural contexts?
- What are the long-term effects of using biofeedback technologies on human relationships?

## Abstract

Have you ever seen two people walking down the street together and thought “wow, those two are really synced up”? It could be two siblings, or a couple that’s been together for decades. Same gait, same arm swings, same stride length. They almost seem to be breathing at the same time. The micro-movements of their bodies aren’t necessarily identical, but they mesh together, in complementary rhythms.
