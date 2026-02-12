# Spatial identification of manipulable objects for a bionic hand prosthesis

## Access

| Field | Value |
|-------|-------|
| DOI | `10.35784/acs_6867` |
| Full Paper | [https://doi.org/10.35784/acs_6867](https://doi.org/10.35784/acs_6867) |
| Source | [https://journalclub.io/episodes/spatial-identification-of-manipulable-objects-for-a-bionic-hand-prosthesis](https://journalclub.io/episodes/spatial-identification-of-manipulable-objects-for-a-bionic-hand-prosthesis) |
| Year | 2026 |
| Citations | 0 |
| Authors |  |
| Paper ID | `1692708a-c6d6-4849-b255-e1c544ba3780` |

## Classification

- **Problem Type:** intention recognition
- **Domain:** Robotics & Control Systems
- **Sub-domain:** Bionic limb prosthetics
- **Technique:** FOMO (MobileNetV2)
- **Technique Category:** neural_architecture
- **Type:** novel

## Summary

This paper presents a method for spatial identification of objects for bionic upper limb prostheses using an optoelectronic module and neural network algorithms. Engineers should care because it enhances the accuracy of prosthetic grip types based on object shapes, improving user experience and functionality.

## Key Contribution

**Integration of spatial identification of object shapes with myographic signal analysis for improved grip-type recognition in bionic prostheses.**

## Problem

The challenge of accurately interpreting user intentions through noisy and variable EMG signals in bionic hand prostheses.

## Method

**Approach:** The method utilizes an optoelectronic module to capture images of objects and classifies them using a neural network. It correlates the identified object shape with myographic signals to determine the appropriate grip type for the prosthesis.

**Algorithm:**

1. 1. Capture images of objects using the ESP32-CAM.
2. 2. Preprocess images to standardize size and format.
3. 3. Feed images into the MobileNetV2 neural network.
4. 4. Classify the object shape into predefined categories (spherical, rectangular, cylindrical).
5. 5. Analyze myographic signals to determine user intent.
6. 6. Match identified shape with appropriate grip type.
7. 7. Execute grip type based on the classification results.

**Input:** Digital images of objects (240x240 pixels) captured by the ESP32-CAM.

**Output:** Identified object shape, grip type, coordinates of the object in the camera's field of view, and dimensions in the X and Y planes.

**Key Parameters:**

- `learning_rate: 0.005`
- `epochs: 30`
- `width_factor (kw): 0.35`
- `image_size: 240x240 pixels`

**Complexity:** not stated

## Benchmarks

**Tested on:** 235 color images of basic shapes (spherical, rectangular, cylindrical)

**Results:**

- accuracy: 89.2%
- F1-score: 0.89

**Compared against:** YOLOv5, YOLOX, Deep SORT

**Improvement:** Achieved 89.2% accuracy with a processing time of 2 ms per image.

## Implementation Guide

**Data Structures:** Image arrays, Neural network model structure

**Dependencies:** ESP32-CAM, TensorFlow Lite, OpenCV

**Core Operation:**

```python
image = capture_image(); shape = classify_shape(image); grip_type = determine_grip(shape, myographic_signal);
```

**Watch Out For:**

- Ensure proper lighting conditions for image capture.
- Be aware of the camera's resolution limitations.
- Training dataset should include diverse object shapes to improve accuracy.

## Use This When

- Developing low-cost bionic prostheses that require object shape recognition.
- Integrating machine learning for real-time object identification in prosthetic devices.
- Enhancing user experience in prosthetics through improved grip type accuracy.

## Don't Use When

- High precision is required beyond the capabilities of the proposed method.
- Complex object shapes that exceed the training dataset's scope.
- When additional computational resources are available for more complex algorithms.

## Key Concepts

object recognition, myographic signals, neural networks, bionic prosthetics, image processing, grip type classification

## Connects To

- Computer vision techniques
- Machine learning for signal processing
- Robotic control systems

## Prerequisites

- Basic understanding of neural networks
- Familiarity with image processing
- Knowledge of EMG signal interpretation

## Limitations

- Limited to basic shapes defined in the training set.
- Performance may degrade with complex object shapes.
- Dependent on the quality of the captured images.

## Open Questions

- How can the system be improved to handle more complex object shapes?
- What additional sensors could enhance the accuracy of grip type recognition?

## Abstract

Your primary input signal is EMG (electromyography), gathered from the terminal-end of the user’s limb. But if you’ve worked with EMG before, you know the limits. It’s noisy, it’s variable, and it’s ambiguous. A single muscle firing pattern can mean different things depending on context. One user might flex to grab a doorknob, another to grasp a cup. The signals are biologically real but semantically weak. That’s your problem-space: intention recognition. If you misclassify the user’s intent, the hand grabs the wrong way. If the grip doesn't match the object, the fingers slip, or the object is crushed, or the hand locks into an unusable position. Or worse. And in a constrained embedded environment, you don’t have the luxury of adding lidar, tactile arrays, or high-res cameras. What you need is a second signal. Something fast, cheap, and good enough. Not perfect classification, just something that gives your system enough context to
