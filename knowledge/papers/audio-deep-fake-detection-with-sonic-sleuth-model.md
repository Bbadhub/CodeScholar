# Audio Deep Fake Detection with Sonic Sleuth Model

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3390/computers13100256` |
| Full Paper | [https://doi.org/10.3390/computers13100256](https://doi.org/10.3390/computers13100256) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/ba33e869949010f8b985df571b2e46e0d50c0cc9](https://www.semanticscholar.org/paper/ba33e869949010f8b985df571b2e46e0d50c0cc9) |
| Source | [https://journalclub.io/episodes/audio-deep-fake-detection-with-sonic-sleuth-model](https://journalclub.io/episodes/audio-deep-fake-detection-with-sonic-sleuth-model) |
| Source | [https://www.semanticscholar.org/paper/ba33e869949010f8b985df571b2e46e0d50c0cc9](https://www.semanticscholar.org/paper/ba33e869949010f8b985df571b2e46e0d50c0cc9) |
| Year | 2026 |
| Citations | 8 |
| Authors | Anfal Alshehri, Danah Almalki, Eaman Alharbi, Somayah Albaradei |
| Paper ID | `07687278-dcd1-4117-87ab-3ac84c7de91e` |

## Classification

- **Problem Type:** audio deepfake detection
- **Domain:** Cybersecurity
- **Sub-domain:** Audio forensics
- **Technique:** Sonic Sleuth
- **Technique Category:** neural_architecture
- **Type:** novel

## Summary

The Sonic Sleuth model is a novel AI detection system designed to identify audio deepfakes with high accuracy. Engineers should care because it provides a robust solution to combat the growing threat of misinformation through manipulated audio, achieving impressive performance metrics on diverse datasets.

## Key Contribution

**Introduction of Sonic Sleuth, a custom CNN model for detecting audio deepfakes with high accuracy and low equal error rate (EER).**

## Problem

The rise of audio deepfakes poses significant risks in cybersecurity, leading to misinformation and fraud.

## Method

**Approach:** Sonic Sleuth employs a custom convolutional neural network (CNN) architecture to classify audio samples as real or synthesized. The model utilizes advanced feature extraction techniques to analyze audio signals and improve detection accuracy.

**Algorithm:**

1. 1. Collect and preprocess audio datasets, ensuring uniformity.
2. 2. Extract features using short-time power spectrum and constant-Q transform.
3. 3. Train the CNN model on the processed audio data.
4. 4. Validate the model using a separate validation set.
5. 5. Test the model on external datasets to evaluate generalization.

**Input:** Audio files in WAV or MP3 format, standardized to 4 seconds and downsampled to 16 kHz.

**Output:** Probability score indicating whether the audio is real or deepfake.

**Key Parameters:**

- `learning_rate: 0.001`
- `batch_size: 32`
- `epochs: 100`
- `dropout_rate: 0.10`
- `class_weights: calculated based on dataset imbalance`

**Complexity:** Not stated

## Benchmarks

**Tested on:** ASVspoof2019, In-the-Wild, FakeAVCeleb, Fake-or-Real

**Results:**

- accuracy: 98.27%
- EER: 0.016 on primary dataset
- accuracy: 84.92%
- EER: 0.085 on external dataset

**Compared against:** Traditional deepfake detection methods

**Improvement:** Significant improvement over traditional methods, achieving high accuracy and low EER.

## Implementation Guide

**Data Structures:** Audio samples stored in arrays or tensors, Feature matrices for CNN input

**Dependencies:** TensorFlow or PyTorch for model training, Librosa for audio processing, NumPy for numerical computations

**Core Operation:**

```python
model.predict(audio_input) returns probability of being deepfake.
```

**Watch Out For:**

- Ensure audio data is preprocessed uniformly to avoid bias.
- Monitor for overfitting during training with early stopping.

## Use This When

- You need to detect manipulated audio in cybersecurity applications.
- You are developing tools for journalism to verify audio authenticity.
- You require a robust model that generalizes across various audio inputs.

## Don't Use When

- The audio data is highly specialized and not covered by the training datasets.
- Real-time detection is required with stringent latency constraints.

## Key Concepts

deep learning, convolutional neural networks, feature extraction, audio processing, deepfake detection

## Connects To

- Generative Adversarial Networks (GANs)
- Other deepfake detection models
- Audio feature extraction techniques

## Prerequisites

- Understanding of convolutional neural networks
- Familiarity with audio processing techniques
- Knowledge of deep learning frameworks

## Limitations

- Performance may degrade with highly specialized audio types.
- Model may require extensive computational resources for training.
- Not optimized for real-time detection scenarios.

## Open Questions

- How can the model be adapted for non-English languages?
- What additional features can improve detection accuracy in noisy environments?

## Abstract

In 2020, a bank manager in Hong Kong received a call. It was from the senior director of a company that regularly did business with the bank. The person explained that the company was about to make a major acquisition, and he requested $35 million to be transferred to the seller's account. The money was sent, and everything seemed normal. Not long after, the bank employee was shocked to learn that he had not spoken to the director at all. He had fallen victim to a Deepfake scam. Today we’ll look at how researchers are trying to stay ahead of the growing threat of Deepfake audio using a new AI detection model called Sonic Sleuth. We’ll look at how they created the model, what feature extraction tools were most effective, and if Sonic Sleuth might help us determine the difference between real and fake. Before we look at the model, let’s talk about what makes Deepfake audio so dangerous and hard to detect.
