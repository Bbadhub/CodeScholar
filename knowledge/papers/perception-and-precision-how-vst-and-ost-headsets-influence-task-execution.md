# Perception and Precision: How VST and OST Headsets Influence Task Execution

## Access

| Field | Value |
|-------|-------|
| DOI | `10.5753/jis.2025.5921` |
| Full Paper | [https://doi.org/10.5753/jis.2025.5921](https://doi.org/10.5753/jis.2025.5921) |
| Source | [https://journalclub.io/episodes/perception-and-precision-how-vst-and-ost-headsets-influence-task-execution](https://journalclub.io/episodes/perception-and-precision-how-vst-and-ost-headsets-influence-task-execution) |
| Year | 2026 |
| Citations | 0 |
| Authors |  |
| Paper ID | `56c20682-04f4-465c-a26b-75b1c03307c9` |

## Classification

- **Problem Type:** user interaction performance evaluation
- **Domain:** Human-Computer Interaction
- **Sub-domain:** Augmented Reality (AR) Systems
- **Technique:** Experimental comparison of VST and OST HMDs
- **Technique Category:** statistical_method
- **Type:** comparison

## Summary

This paper investigates the impact of Video See-Through (VST) and Optical See-Through (OST) head-mounted displays (HMDs) on task execution accuracy and efficiency. Engineers should care because understanding these effects can guide the design of more effective AR applications and improve user interaction in various domains.

## Key Contribution

**The study provides empirical evidence comparing the performance of VST and OST HMDs in precision tasks, highlighting the perceptual distortions introduced by each technology.**

## Problem

The work is motivated by the need to understand how different HMD technologies affect user accuracy and efficiency in real-world tasks.

## Method

**Approach:** The method involves conducting two experiments where participants perform tasks using either VST or OST HMDs and compare their performance against unaided vision. The tasks include dart throwing and bottle filling, measuring completion time and accuracy.

**Algorithm:**

1. 1. Recruit participants and divide them into two groups.
2. 2. Assign each group to perform tasks with either VST or OST HMDs.
3. 3. Each participant performs tasks twice: once with HMD and once without.
4. 4. Record completion time, accuracy, and self-reported discomfort.
5. 5. Analyze the collected data statistically to compare performance across conditions.

**Input:** Participant performance data including completion times, accuracy scores, and self-reported discomfort levels.

**Output:** Statistical analysis results comparing task performance with VST and OST HMDs against unaided vision.

**Key Parameters:**

- `number_of_participants: 80`
- `task_types: ['dart throwing', 'bottle filling']`
- `HMD_types: ['Meta Quest 3', 'Microsoft HoloLens']`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Performance data from 80 participants across two tasks (dart throwing and bottle filling)

**Results:**

- completion time
- dart-board error
- water-level deviation
- self-reported visual discomfort

**Compared against:** Performance without HMD (naked-eye baseline)

**Improvement:** Both VST and OST HMDs lengthened task completion and reduced precision compared to naked-eye performance.

## Implementation Guide

**Data Structures:** Participant data records, Task performance metrics

**Dependencies:** Statistical analysis software (e.g., R, Python libraries)

**Core Operation:**

```python
for each participant in participants: perform_task_with_HMD(); record_metrics(); perform_task_without_HMD(); record_metrics();
```

**Watch Out For:**

- Ensure proper calibration of HMDs before experiments.
- Monitor participant comfort to avoid fatigue affecting results.
- Randomize task order to mitigate learning effects.

## Use This When

- Designing AR applications that require high precision and user interaction.
- Evaluating the effectiveness of different HMD technologies in real-world tasks.
- Conducting user studies to assess the impact of visual technologies on task performance.

## Don't Use When

- Tasks that do not require precise motor control or depth perception.
- When user comfort and visual fatigue are critical factors in task execution.
- In environments where latency and perceptual distortion are unacceptable.

## Key Concepts

perceptual distortion, task execution, HMD performance, user interaction, AR technology, depth perception, visual discomfort

## Connects To

- User experience design in AR
- Statistical methods for performance evaluation
- Depth perception studies in augmented reality

## Prerequisites

- Understanding of AR technologies and their applications.
- Familiarity with statistical analysis methods.
- Knowledge of user interaction principles in HCI.

## Limitations

- The study is limited to two specific tasks and may not generalize to all AR applications.
- Potential biases in participant selection and task familiarity.
- The impact of individual differences in user experience with HMDs is not fully explored.

## Open Questions

- How can calibration procedures be refined to improve accuracy in HMDs?
- What are the long-term effects of using VST and OST HMDs on user performance?

## Abstract

In a VST system, the user never sees the real world directly. Instead, the headset uses one or more forward-facing RGB cameras (typically positioned near eye level) to continuously capture the external environment. These camera feeds are sent through an image processing pipeline that may include distortion correction, color balancing, depth estimation, and pose tracking. Virtual content is then rendered into the same space using 3D engines, and the composited output is displayed on internal near-eye screens (typically OLED or LCD panels). What this means, practically, is that your entire visual field, including what would otherwise be raw, unaided vision, is now a digital reconstruction of the world. The system has full control over the pixels, allowing for very tight integration of virtual and physical elements, as well as visual effects like occlusion or global relighting. However, this full-pipeline approach introduces a measurable delay, because the physical light rays that would normally reach your retina must first pass through a camera sensor, travel through a software stack, and finally be emitted by a display panel. That end-to-end latency is usually in the range of 20 to 50 milliseconds, depending on frame rate, encoding pipeline, sensor speed, and whether motion prediction is used to compensate. Even with low-latency optimizations, that delay can disrupt fast visuomotor coupling, especially during quick eye movements or rapid head turns. Additionally, because the image is generated from stereo cameras mounted a few centimeters apart on the headset shell (not from your actual eye position) parallax errors can emerge when interacting with objects at arm’s length. This makes fine-grained depth judgment more difficult. Additionally, most VST systems are limited in dynamic range and focus flexibility: unlike the human eye, which can adaptively accommodate to nearby or distant objects, most camera lenses are fixed-focus and tuned for a depth of field optimized for mid-range vision. This can make close-up content look subtly blurred or unnatural. Finally, VST systems typically restrict peripheral vision because the rendered image field is constrained by the display optics, which in turn can limit ambient spatial awareness and increase cognitive load in tasks requiring precise motor control.
