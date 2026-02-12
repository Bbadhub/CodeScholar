# Effectiveness of training under stress in immersive VR: an investigation of firefighter performance, gaze entropy, and pupillometry

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3389/frvir.2025.1542507` |
| Full Paper | [https://doi.org/10.3389/frvir.2025.1542507](https://doi.org/10.3389/frvir.2025.1542507) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/7e939b2e94ae92dc445b43d3575b691f3d307963](https://www.semanticscholar.org/paper/7e939b2e94ae92dc445b43d3575b691f3d307963) |
| Source | [https://journalclub.io/episodes/effectiveness-of-training-under-stress-in-immersive-vr-an-investigation-of-firefighter-performance-gaze-entropy-and-pupillometry](https://journalclub.io/episodes/effectiveness-of-training-under-stress-in-immersive-vr-an-investigation-of-firefighter-performance-gaze-entropy-and-pupillometry) |
| Source | [https://www.semanticscholar.org/paper/7e939b2e94ae92dc445b43d3575b691f3d307963](https://www.semanticscholar.org/paper/7e939b2e94ae92dc445b43d3575b691f3d307963) |
| Year | 2026 |
| Citations | 3 |
| Authors | Ranjana K. Mehta, John Kang, Yangming Shi, Jing Du |
| Paper ID | `e5165e2d-7a9b-4a1b-b830-90a0b7d4b24a` |

## Classification

- **Problem Type:** training effectiveness under stress in emergency response scenarios
- **Domain:** Virtual Reality & Training
- **Sub-domain:** Emergency Response Training
- **Technique:** Visuospatial Sequence Learning Task
- **Technique Category:** training_method
- **Type:** novel

## Summary

This study investigates the effectiveness of virtual reality (VR) training under stress for firefighters, focusing on task performance, eye movement data, and subjective evaluations. Engineers should care because it provides insights into how VR can be utilized to enhance training effectiveness in high-stress environments.

## Key Contribution

**The integration of eye-tracking metrics with VR training to assess cognitive states under stress in emergency response scenarios.**

## Problem

Firefighters need effective training methods to prepare for high-stress emergency situations, where traditional training can be dangerous and costly.

## Method

**Approach:** Participants memorize a sequence of actions in a VR environment designed to simulate emergency scenarios. Their performance is evaluated based on accuracy and time taken, while eye-tracking data provides insights into cognitive load and stress effects.

**Algorithm:**

1. 1. Participants enter the VR environment and undergo a calibration phase.
2. 2. Familiarization with the task is conducted using visual cues.
3. 3. Participants perform the task without cues to memorize the sequence.
4. 4. Stressors are introduced in the training phase for the stress group.
5. 5. Performance is measured based on accuracy and operation time.
6. 6. Eye-tracking data is collected throughout the task.
7. 7. Retrieval tasks are conducted under both control and stress conditions.

**Input:** VR environment with a sequence of valves to be closed, eye-tracking data from Tobii Pro integrated with HTC VIVE.

**Output:** Performance metrics (accuracy and operation time), gaze entropy, pupil dilation data, and subjective workload scores.

**Key Parameters:**

- `time_limit_per_trial: 60 seconds`
- `eye_tracking_frequency: 90 Hz`
- `number_of_trials: 8`

**Complexity:** Not stated

## Benchmarks

**Tested on:** 40 male firefighters from local fire departments

**Results:**

- accuracy: normalized performance using operation time per correct valve
- operation time: time taken to complete the task

**Compared against:** Control group without stressors

**Improvement:** Stress training group exhibited poorer performance scores and longer operation times compared to the control group.

## Implementation Guide

**Data Structures:** VR environment setup, eye-tracking data storage (CSV files)

**Dependencies:** Unity 3D, Tobii Pro SDK, HTC VIVE

**Core Operation:**

```python
initialize_VR_environment(); collect_eye_tracking_data(); evaluate_performance_metrics();
```

**Watch Out For:**

- Ensure proper calibration of eye-tracking before trials.
- Monitor participants for VR sickness during the experiment.
- Adjust stressor intensity based on participant feedback.

## Use This When

- Developing training programs for emergency responders using VR.
- Assessing cognitive load and performance under stress in training environments.
- Creating adaptive training paradigms based on eye-tracking data.

## Don't Use When

- Training scenarios do not involve high-stress environments.
- Resources for VR setup and eye-tracking technology are unavailable.
- Participants are not comfortable with VR technology.

## Key Concepts

eye tracking, pupillometry, cognitive load, stress training, VR training, task performance

## Connects To

- Cognitive load theory
- Virtual reality training systems
- Eye-tracking applications in training
- Stress-induced learning mechanisms

## Prerequisites

- Understanding of VR technology and setup
- Knowledge of cognitive load theory
- Familiarity with eye-tracking methodologies

## Limitations

- Limited to male firefighters, affecting generalizability.
- Potential for VR sickness impacting participant performance.
- Stressors may not accurately replicate real-world scenarios.

## Open Questions

- How can VR training be adapted for different emergency scenarios?
- What are the long-term effects of stress training on performance retention?

## Abstract

This study was designed to go well beyond a simple accuracy test. The authors split their measurements into three main categories: task performance, eye movement data, and subjective psychometric evaluations. Together, these provided a multilayered picture of how stress impacts learning and retrieval in a simulated emergency. Let’s start with performance. Each participant was asked to memorize and then execute the shutdown sequence. The researchers captured two main metrics: the number of valves closed in the correct order (sequence accuracy) and the time it took to complete the task (operation time). Because not everyone finished all eight steps, they normalized performance using “operation time per correct valve,” which adjusts for partial completions and allows a clean comparison across users with different accuracy levels. Then came the gaze data. The eye tracker recorded eye movements at 90 Hz. From this, the researchers computed gaze
