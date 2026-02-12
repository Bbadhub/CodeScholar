# Dynamic Car-Following Model With Jerk Suppression for Highway Autonomous Driving

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1109/ACCESS.2025.3535596` |
| Full Paper | [https://doi.org/10.1109/ACCESS.2025.3535596](https://doi.org/10.1109/ACCESS.2025.3535596) |
| Source | [https://journalclub.io/episodes/dynamic-car-following-model-with-jerk-suppression-for-highway-autonomous-driving](https://journalclub.io/episodes/dynamic-car-following-model-with-jerk-suppression-for-highway-autonomous-driving) |
| Year | 2026 |
| Citations | 0 |
| Authors |  |
| Paper ID | `08c432ba-f24c-45ab-9865-193bad898ec8` |

## Classification

- **Problem Type:** dynamic car-following model
- **Domain:** Robotics & Control Systems
- **Sub-domain:** Autonomous Vehicle Control
- **Technique:** Dynamic Car-Following Model with Jerk Suppression
- **Technique Category:** control_algorithm
- **Type:** novel

## Summary

This paper presents a dynamic car-following model that incorporates jerk suppression to enhance the safety and comfort of highway autonomous driving. Engineers should care because it addresses the critical balance between maintaining safe headway and minimizing abrupt vehicle movements, which is essential for passenger comfort and traffic flow.

## Key Contribution

**Introduction of a jerk suppression mechanism in a dynamic car-following model for autonomous vehicles.**

## Problem

The need for safe and comfortable vehicle following distances in highway driving scenarios.

## Method

**Approach:** The proposed method models the behavior of following vehicles based on headway time and incorporates a jerk suppression mechanism to reduce abrupt changes in acceleration. This results in smoother driving experiences while maintaining safe distances from leading vehicles.

**Algorithm:**

1. 1. Measure the headway time between the following and leading vehicle.
2. 2. Calculate the desired speed and acceleration based on the headway.
3. 3. Apply jerk suppression to smooth out acceleration changes.
4. 4. Adjust the following vehicle's speed to maintain the desired headway.
5. 5. Continuously monitor the leading vehicle's behavior and update the following vehicle's actions accordingly.

**Input:** Real-time data on vehicle speeds, distances, and headway times.

**Output:** Adjusted speed and acceleration commands for the following vehicle.

**Key Parameters:**

- `headway_time: 1.5 seconds`
- `jerk_limit: 0.5 m/s³`

**Complexity:** O(n) time, O(1) space

## Benchmarks

**Tested on:** Simulated highway driving scenarios with varying traffic conditions.

**Results:**

- jerk: reduced by 30%
- headway compliance: 95%

**Compared against:** Traditional car-following models without jerk suppression.

**Improvement:** 30% reduction in jerk compared to baseline models.

## Implementation Guide

**Data Structures:** Vehicle state representation (position, speed, acceleration), Traffic environment model

**Dependencies:** Control system libraries, Simulation frameworks for vehicle dynamics

**Core Operation:**

```python
while driving: update_speed_and_acceleration(leading_vehicle_data)
```

**Watch Out For:**

- Ensure accurate measurement of headway time.
- Monitor for sudden changes in leading vehicle behavior.

## Use This When

- Implementing autonomous driving systems for highway scenarios.
- Designing vehicle control algorithms that prioritize passenger comfort.
- Developing traffic management systems that require vehicle spacing optimization.

## Don't Use When

- Operating in low-speed urban environments where headway is less critical.
- When vehicle dynamics are not a primary concern.

## Key Concepts

jerk suppression, headway time, autonomous driving, dynamic modeling

## Connects To

- PID control algorithms
- Adaptive cruise control systems
- Traffic flow modeling

## Prerequisites

- Understanding of vehicle dynamics
- Familiarity with control theory

## Limitations

- Assumes constant traffic conditions
- May not account for unpredictable driver behavior

## Open Questions

- How to adapt the model for mixed traffic with human drivers?
- What are the effects of varying road conditions on jerk suppression?

## Abstract

The first thing you need to know is that there’s something called "Headway". Headway is the time it takes for a following-vehicle to reach the same point that a leading-vehicle just passed. It is typically measured in seconds and helps determine safe following distances in traffic. If you’ve ever heard someone say to "give x seconds to the car in front of you", that number of seconds is headway. Today’s research largely concerns highway driving, where headway is crucial. Too much headway, and the cars behind you will start passing you; leapfrogging to the space you should have been occupying. Too little headway and not only do you risk running into the back of the next car, but you’re much more likely to feel the need to hit the brakes hard when the next car’s brake lights come on. For your passenger, that results in jerkiness. Prior to this paper, a number of systems
