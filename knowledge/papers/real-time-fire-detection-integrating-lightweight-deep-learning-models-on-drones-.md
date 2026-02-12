# Real-Time Fire Detection: Integrating Lightweight Deep Learning Models on Drones with Edge Computing

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3390/drones8090483` |
| Full Paper | [https://doi.org/10.3390/drones8090483](https://doi.org/10.3390/drones8090483) |
| Source | [https://journalclub.io/episodes/real-time-fire-detection-integrating-lightweight-deep-learning-models-on-drones-with-edge-computing](https://journalclub.io/episodes/real-time-fire-detection-integrating-lightweight-deep-learning-models-on-drones-with-edge-computing) |
| Year | 2026 |
| Citations | 0 |
| Authors |  |
| Paper ID | `c94b18e4-3fae-4f86-8238-4e3bc64c5521` |

## Classification

- **Problem Type:** real-time fire detection
- **Domain:** Machine Learning & AI
- **Sub-domain:** Deep Learning, Edge Computing
- **Technique:** YOLOv8n (Nano), YOLOv8m (Medium), Detection Transformer (DETR)
- **Technique Category:** classification_model
- **Type:** novel

## Summary

This paper presents a real-time fire detection system using lightweight deep learning models deployed on drones with edge computing capabilities. Engineers should care because it addresses the critical need for early fire detection in remote areas, potentially saving lives and reducing property damage.

## Key Contribution

**Integration of lightweight deep learning models with drone technology for real-time fire detection using edge computing.**

## Problem

The work is motivated by the need to detect fires early in sparsely populated areas to prevent extensive damage and loss of life.

## Method

**Approach:** The method employs a knowledge distillation technique where a larger teacher model (YOLOv8m) trains a smaller student model (YOLOv8n) to improve performance while reducing computational requirements. The system is deployed on a Raspberry Pi 5 for real-time fire detection using images captured by a drone.

**Algorithm:**

1. 1. Collect a comprehensive dataset of fire images.
2. 2. Train the YOLOv8m model as the teacher model on the dataset.
3. 3. Use the trained YOLOv8m to generate soft targets for the YOLOv8n student model.
4. 4. Train the YOLOv8n model using the soft targets from the teacher model.
5. 5. Deploy the YOLOv8n model on a Raspberry Pi 5 microcontroller.
6. 6. Integrate the model with a drone for real-time fire detection.

**Input:** Images of fire and non-fire scenarios (e.g., forest, vehicle, industrial, accidental, residential fires).

**Output:** Real-time detection of fire incidents with accuracy metrics.

**Key Parameters:**

- `learning_rate: 0.01`
- `batch_size: 32`
- `epochs: 50`
- `IoU: 0.7 for YOLOv8, 0.8 for DETR`
- `weight_decay: 0.0005 for YOLOv8, 1 × 10 −4 for DETR`

**Complexity:** Not stated.

## Benchmarks

**Tested on:** Comprehensive dataset of 7187 fire images, including various categories such as forest, vehicle, industrial, accidental, residential fires.

**Results:**

- detection accuracy: 95.21% for YOLOv8n, 89.23% for real-time experiments, F1 score: 0.985

**Compared against:** YOLOv8m (Medium) as the teacher model.

**Improvement:** YOLOv8n achieved 95.21% detection accuracy, outperforming the baseline.

## Implementation Guide

**Data Structures:** Image datasets, bounding boxes for fire detection.

**Dependencies:** Raspberry Pi 5, Pi camera module 3, YOLOv8, DETR, Roboflow for dataset annotation.

**Core Operation:**

```python
model = YOLOv8n.load('trained_model'); output = model.detect(image)
```

**Watch Out For:**

- Ensure the dataset is well-annotated to avoid misclassifications.
- Watch for the limitations of the Raspberry Pi in terms of processing power.
- Consider environmental factors that may affect drone flight stability.

## Use This When

- You need to implement a fire detection system in remote areas.
- You require a lightweight model for deployment on edge devices.
- Real-time processing of visual data is essential for your application.

## Don't Use When

- High computational resources are available for processing.
- The application does not require real-time detection.
- The environment is not constrained by power or processing limitations.

## Key Concepts

knowledge distillation, edge computing, drone technology, real-time detection, deep learning models

## Connects To

- YOLOv8, YOLOv7, Detectron2, knowledge distillation techniques, edge AI frameworks

## Prerequisites

- Understanding of deep learning models
- Familiarity with drone technology
- Knowledge of edge computing principles

## Limitations

- Performance may degrade in complex environments with multiple fire sources.
- Limited by the processing power of the Raspberry Pi.
- Potential issues with drone flight stability and battery life.

## Open Questions

- How can the model be further optimized for different environmental conditions?
- What additional sensors could enhance the fire detection capabilities?

## Abstract

In the immortal words of Frankenstein’s monster: FIRE BAD! And unfortunately, we often don’t spot fires until they’re really bad. We’ll miss the small brush fires and only take notice when they’re large and out of control. This happens for a few reasons: Fires can start anywhere, even away from the cities. In the middle of open land, or in a forest where nobody will notice. If someone does notice, there can be a “bystander-effect”: everyone thinks that someone else must have called 911 to report the fire, or that someone else must already be handling it. So nobody ends up calling at all, and the fire grows and grows. Where I live in California, this is a big problem. Large parts of the state are sparsely populated open areas with lots of fuel for wildfires (dry grass and the like). So every summer a sad ritual repeats itself here. Loose cigarette butts, mismanaged campfires, downed power lines, or any of several other causes can be the trigger. And once it starts, the fire goes unspotted for a while, It grows, it spreads and eventually causes real damage. These fires cost California billions of dollars, every single year.
