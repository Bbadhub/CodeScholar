# Active robotic search for victims using ensemble deep learning techniques

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1088/2632-2153/ad33df` |
| Full Paper | [https://doi.org/10.1088/2632-2153/ad33df](https://doi.org/10.1088/2632-2153/ad33df) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/4120340f79b6f439cfbe622236fd04d3b7907de8](https://www.semanticscholar.org/paper/4120340f79b6f439cfbe622236fd04d3b7907de8) |
| Source | [https://journalclub.io/episodes/active-robotic-search-for-victims-using-ensemble-deep-learning-techniques](https://journalclub.io/episodes/active-robotic-search-for-victims-using-ensemble-deep-learning-techniques) |
| Source | [https://www.semanticscholar.org/paper/4120340f79b6f439cfbe622236fd04d3b7907de8](https://www.semanticscholar.org/paper/4120340f79b6f439cfbe622236fd04d3b7907de8) |
| Year | 2026 |
| Citations | 5 |
| Authors | J. F. García-Samartín, Christyan Cruz Ulloa, J. del Cerro, Antonio Barrientos |
| Paper ID | `bb42a888-cefa-4c38-a8c6-effd790fcb5b` |

## Classification

- **Problem Type:** active search and rescue robotics
- **Domain:** Robotics & Control Systems
- **Sub-domain:** Search and Rescue Robotics
- **Technique:** ARTU-R autonomous search algorithm
- **Technique Category:** framework
- **Type:** novel

## Summary

The paper presents an autonomous robotic system using ensemble deep learning techniques for active search and rescue operations in post-disaster environments. Engineers should care because this approach enhances the efficiency and effectiveness of victim detection in complex terrains, leveraging both visual and spatial information.

## Key Contribution

**Development of an autonomous rescue system that integrates indirect search and next best view techniques using a quadruped robot and interpretable machine learning models.**

## Problem

The increasing frequency of natural disasters necessitates efficient and reliable methods for locating survivors trapped in collapsed structures.

## Method

**Approach:** The method employs a quadruped robot equipped with RGB-D cameras and lidar to autonomously explore disaster areas. It prioritizes exploration points based on the probability of finding victims, calculated using a Random Forest model that processes data from convolutional neural networks.

**Algorithm:**

1. 1. Initialize the robot and sensors.
2. 2. Capture environment data using RGB-D camera and lidar.
3. 3. Use CNN to detect room types and objects.
4. 4. Process detection results with Random Forest to estimate victim probability.
5. 5. Evaluate candidate exploration points based on distance, unexplored space, and victim probability.
6. 6. Select the next exploration point using a fitness function.
7. 7. Move the robot to the selected point and repeat.

**Input:** Sensor data from RGB-D camera and lidar, including images and spatial information.

**Output:** Path to the next exploration point and victim detection probabilities.

**Key Parameters:**

- `max_speed: 0.5 m/s`
- `robot_dimensions: 12 degrees of freedom`
- `lidar_distance_range: 40 m`
- `lidar_sample_rate: 9.2 kHz`
- `camera_resolution: 1920 x 1080 px`

**Complexity:** not stated

## Benchmarks

**Tested on:** NIST orange reconstructed environments, Common Objects in Context (COCO) for object detection

**Results:**

- mAP: 96.99%
- precision: 92.66%
- recall: 93.2%

**Compared against:** Standard search and rescue algorithms without active exploration

**Improvement:** Achieved logical exploration paths and improved victim detection efficiency compared to traditional methods.

## Implementation Guide

**Data Structures:** 2D arrays for storing detection results, Graphs for representing exploration paths

**Dependencies:** ROS for robot control and communication, OpenCV for image processing, TensorFlow or PyTorch for deep learning models

**Core Operation:**

```python
detected_victims = RandomForest.predict(CNN.output(image))
```

**Watch Out For:**

- Ensure the robot operates at reduced speeds to avoid image blurring.
- Carefully tune the Random Forest parameters to avoid overfitting.
- Monitor the robot's battery and computational load during operations.

## Use This When

- You need to perform search and rescue operations in complex terrains.
- You require a system that provides interpretable decision-making processes.
- You want to enhance victim detection capabilities in disaster scenarios.

## Don't Use When

- The environment is fully known and can be mapped beforehand.
- You have limited computational resources for real-time processing.
- The robot needs to operate in environments without obstacles.

## Key Concepts

ensemble learning, indirect search, next best view, random forests, convolutional neural networks, quadruped robotics, active exploration

## Connects To

- SLAM algorithms for mapping
- Other ensemble learning techniques
- Deep reinforcement learning for adaptive exploration

## Prerequisites

- Understanding of machine learning concepts
- Familiarity with robotic control systems
- Knowledge of computer vision techniques

## Limitations

- Performance may degrade in highly cluttered environments.
- Requires significant computational resources for real-time processing.
- Limited to scenarios where the robot can physically navigate.

## Open Questions

- How can the algorithm be adapted for multi-robot scenarios?
- What improvements can be made for real-time victim detection in dynamic environments?

## Abstract

Could you find a needle in a haystack? Sounds impossible right? Now imagine the needle is a person, and the haystack is a collapsed building. Now the question is no longer can you find the needle, it’s when will you find the needle. But what if a robot could do it for you, and do it with your thought process, and your sense of urgency? That’s the challenge that search and rescue (SAR) teams face with every natural disaster that occurs, which, by the way, is happening more frequently than ever. According to recent data, since the year 2000, the number of natural disasters has shifted from 300 to around 450 events per year. With it comes the need for more efficient, reliable, and safe ways to find survivors trapped in disaster zones. The stakes are high, and the terrain is often too dangerous for human rescuers. So, once again, we ask the question: can robots do the job for us?
