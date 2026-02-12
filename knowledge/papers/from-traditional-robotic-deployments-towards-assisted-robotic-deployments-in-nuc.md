# From traditional robotic deployments towards assisted robotic deployments in nuclear decommissioning

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3389/frobt.2025.1432845` |
| Full Paper | [https://doi.org/10.3389/frobt.2025.1432845](https://doi.org/10.3389/frobt.2025.1432845) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/a9a6cfb2291bd9a7005bc138aeb6b5546abd5f08](https://www.semanticscholar.org/paper/a9a6cfb2291bd9a7005bc138aeb6b5546abd5f08) |
| Source | [https://journalclub.io/episodes/from-traditional-robotic-deployments-towards-assisted-robotic-deployments-in-nuclear-decommissioning](https://journalclub.io/episodes/from-traditional-robotic-deployments-towards-assisted-robotic-deployments-in-nuclear-decommissioning) |
| Source | [https://www.semanticscholar.org/paper/a9a6cfb2291bd9a7005bc138aeb6b5546abd5f08](https://www.semanticscholar.org/paper/a9a6cfb2291bd9a7005bc138aeb6b5546abd5f08) |
| Year | 2026 |
| Citations | 1 |
| Authors | Erwin Jose López Pulgarín, Dave Hopper, Jon Montgomerie, James Kell, Joaquín Carrasco, Guido Herrmann |
| Paper ID | `fc7fe4fe-91a8-45ad-be60-28f6a43442f0` |

## Classification

- **Problem Type:** robotic deployment in hazardous environments
- **Domain:** Robotics & Control Systems
- **Sub-domain:** Teleoperation and Haptic Feedback Systems
- **Technique:** Haptic Digital Twins (HDT) and Assisted Operations (AO)
- **Technique Category:** framework
- **Type:** novel

## Summary

The paper discusses the transition from traditional robotic deployments to assisted robotic deployments in nuclear decommissioning, emphasizing the integration of Haptic Digital Twins and Assisted Operations to enhance safety and efficiency. Engineers should care because these innovations can significantly improve task performance and reduce risks in hazardous environments.

## Key Contribution

**Introduction of Haptic Digital Twins and Assisted Operations to enhance robotic deployments in nuclear decommissioning.**

## Problem

The need for effective and safe robotic systems to perform decommissioning tasks in environments with high radiation and limited human access.

## Method

**Approach:** The method involves creating Haptic Digital Twins that simulate real-world environments for training and deployment, integrating live sensor data for visualization. Assisted Operations provide varying levels of autonomy to improve task performance during teleoperation.

**Algorithm:**

1. 1. Create a Haptic Digital Twin of the deployment environment using sensor data.
2. 2. Integrate physics-based simulations to predict robot interactions.
3. 3. Implement multimodal feedback mechanisms for operator guidance.
4. 4. Develop Assisted Operations with varying levels of autonomy.
5. 5. Train operators using the HDT interface.
6. 6. Deploy robots with real-time feedback and assistance.

**Input:** Sensor data from cameras, radiation sensors, and other environmental scanners.

**Output:** Enhanced robotic control and feedback during deployment, improved training for operators.

**Key Parameters:**

- `sensor_resolution: high`
- `feedback_frequency: 60Hz`
- `robot_control_mode: semi-autonomous`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Nuclear decommissioning environments, including Sellafield and Fukushima sites.

**Results:**

- Task completion time, operator safety, and performance accuracy.

**Compared against:** Traditional teleoperation methods without HDT and AO.

**Improvement:** Expected to improve task performance to expert operator-level without exposing operators to hazardous environments.

## Implementation Guide

**Data Structures:** 3D models of environments, Sensor data arrays, Robot control state machines

**Dependencies:** ROS (Robot Operating System), OpenGL for visualization, Physics engines for simulation

**Core Operation:**

```python
initialize_HDT(environment_data); setup_AO(robot_control); train_operator(HDT); deploy_robot();
```

**Watch Out For:**

- Ensure sensor calibration to avoid inaccurate data.
- Operator training must include all levels of assistance.
- Monitor for system overload during high feedback scenarios.

## Use This When

- Deploying robots in environments with high radiation levels.
- Training operators for complex robotic tasks in hazardous settings.
- Improving task performance in teleoperated robotic systems.

## Don't Use When

- The environment is fully accessible to human operators.
- Robotic systems are not required due to low-risk tasks.
- Cost constraints do not allow for advanced technology integration.

## Key Concepts

Haptic feedback, Digital twins, Teleoperation, Assisted operations, Robotic autonomy, Safety case, Fault tree analysis

## Connects To

- Neural Radiance Fields (NeRF)
- Gaussian Splatting
- Shared autonomy frameworks
- Robotic manipulation techniques
- Safety assessment principles

## Prerequisites

- Understanding of teleoperation systems
- Familiarity with robotic control algorithms
- Knowledge of haptic feedback mechanisms

## Limitations

- Increased complexity in system management and validation.
- Training requirements for operators may increase.
- Potential regulatory hurdles for semi-autonomous operations.

## Open Questions

- How to effectively transition between assisted and manual control?
- What are the long-term impacts of using HDTs on operator performance?

## Abstract

If you watched the HBO miniseries “Chernobyl” a few years back, then this is a story you already know well. In 1986 there was an explosion in Reactor 4 at the Chernobyl Nuclear Power Plant in modern-day Ukraine. This accident released massive amounts of radiation, and created an environment that was lethal not just to humans and animals, but also to machines. You see, when Soviet engineers sent in remote-controlled robots to aid in the cleanup, many of them failed almost immediately. The radiation fried their electronics. It caused their systems to glitch, their sensors to malfunction, and their circuits to burn out. Some of the robots just stopped moving, others spun around aimlessly, and others lost communication with their operators. This led to one of the darkest moments in an already tragic event. Officials decided to send in what they termed "bio-robots" instead. Of course, these weren't robots at all
