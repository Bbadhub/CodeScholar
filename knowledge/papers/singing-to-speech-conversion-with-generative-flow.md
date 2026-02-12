# Singing to speech conversion with generative flow

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1186/s13636-025-00400-x` |
| Full Paper | [https://doi.org/10.1186/s13636-025-00400-x](https://doi.org/10.1186/s13636-025-00400-x) |
| Source | [https://journalclub.io/episodes/singing-to-speech-conversion-with-generative-flow](https://journalclub.io/episodes/singing-to-speech-conversion-with-generative-flow) |
| Year | 2026 |
| Citations | 0 |
| Authors |  |
| Paper ID | `71f51829-793c-4c55-a100-d16ddfb46754` |

## Classification

- **Problem Type:** cross-domain voice conversion
- **Domain:** Machine Learning & AI
- **Sub-domain:** Voice Conversion
- **Technique:** Generative Flow-based Singing-to-Speech Conversion
- **Technique Category:** neural_architecture
- **Type:** novel

## Summary

The paper presents a novel Singing-to-Speech (S2S) conversion system that transforms singing into speech while preserving phonetic information. This is significant for applications in Automatic Speech Recognition and for enhancing the listening experience for individuals with hearing impairments.

## Key Contribution

**Introduction of the first deep learning-based Singing-to-Speech conversion system leveraging generative flow and an adapted alignment module.**

## Problem

The challenge of accurately transcribing sung lyrics into spoken text due to variations in pitch, rhythm, and timbre.

## Method

**Approach:** The method utilizes a generative flow model to convert singing Mel-spectrograms into speech-like Mel-spectrograms while retaining phonetic information. It incorporates a modified monotonic alignment search algorithm to handle timing differences between singing and speech.

**Algorithm:**

1. 1. Input singing Mel-spectrograms into the Mel encoder.
2. 2. Map the input to a latent space using the encoder.
3. 3. Predict phoneme posteriorgrams for both singing and speech.
4. 4. Apply the modified monotonic alignment search (MAST) to align phoneme posteriorgrams.
5. 5. Use the flow-based decoder to generate speech Mel-spectrograms from the latent representation.
6. 6. Convert the generated Mel-spectrograms to audio using a vocoder.

**Input:** Singing Mel-spectrograms (80-bin, 16 kHz sampling rate)

**Output:** Speech-like Mel-spectrograms

**Key Parameters:**

- `learning_rate: 0.0001`
- `ω (weight for loss components): 10`
- `noise_level: 0.3 (for fine-tuning)`
- `epochs: 223 (initial), 60 (fine-tuning)`

**Complexity:** Not stated

## Benchmarks

**Tested on:** DAMP Sing! 300×30×2 dataset (DSing), NHSS dataset

**Results:**

- Mean Opinion Score (MOS)
- Speech-to-Reverberation Modulation Energy Ratio (SRMR)
- Word Error Rate (WER)
- Character Error Rate (CER)

**Compared against:** ALT-TTS, WORLD-nodur, WORLD-dur

**Improvement:** Outperformed signal processing baselines in naturalness and transcribe-and-synthesize baselines in phonetic similarity.

## Implementation Guide

**Data Structures:** Mel-spectrograms, Phoneme posteriorgrams, Latent space representations

**Dependencies:** Deep learning frameworks (e.g., PyTorch, TensorFlow), Vocoder (e.g., Parallel Wave GAN)

**Core Operation:**

```python
zsi = fenc(xsi); Qsi = fphone(zsi); zsp = fdec(zsp); xsp = fdec(zsp)
```

**Watch Out For:**

- Ensure proper alignment between singing and speech data.
- Monitor the impact of duration adjustments on output quality.
- Fine-tuning the model is crucial for better performance.

## Use This When

- You need to convert singing to speech for applications in music technology.
- You want to improve Automatic Lyrics Transcription systems.
- You are working on enhancing audio intelligibility for hearing-impaired users.

## Don't Use When

- You require high-quality, intelligible spoken output from singing.
- You have access to high-quality transcribed data for training.
- You need real-time processing capabilities.

## Key Concepts

Generative flow, Monotonic alignment search, Mel-spectrogram, Phoneme prediction, Duration prediction, Voice conversion, Data augmentation

## Connects To

- Glow-TTS
- Tacotron2
- Voice Conversion models
- Automatic Speech Recognition systems

## Prerequisites

- Understanding of deep learning architectures
- Familiarity with audio processing techniques
- Knowledge of phoneme representation

## Limitations

- Requires large datasets for effective training.
- Performance may vary with different singing styles.
- Not suitable for languages with limited phoneme mapping.

## Open Questions

- How can S2S be adapted for real-time applications?
- What improvements can be made for low-resource languages?

## Abstract

Today we’ll look at why sung text is so much harder to work with than spoken text and why this matters in the field of Automatic Speech Recognition. We’ll then learn how researchers are attempting to tackle this problem by developing a deep-learning based system for Singing-to-Speech conversion or S2S. Automatic Speech Recognition (ASR) is the use of machine learning to transcribe text from recordings of the human voice. When this technology is applied to song, it is referred to as Automatic Lyric Transcription (ALT). In comparison with speech, singing usually contains wider variation in pitch, duration, and timbre. Singing can also cause substantial changes in pronunciation. This increased variation means that you need more complex models and larger data sets to transcribe it. In today’s article, the authors propose an entirely new task, Singing-to-Speech (S2S), that may act as a bridge between song and text. Their goal was not to create something
