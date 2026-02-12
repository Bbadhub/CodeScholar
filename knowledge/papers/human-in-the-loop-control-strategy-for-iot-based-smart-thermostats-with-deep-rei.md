# Human-in-the-loop control strategy for IoT-based smart thermostats with Deep Reinforcement Learning

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1016/j.egyai.2025.100490` |
| Full Paper | [https://doi.org/10.1016/j.egyai.2025.100490](https://doi.org/10.1016/j.egyai.2025.100490) |
| Source | [https://journalclub.io/episodes/human-in-the-loop-control-strategy-for-iot-based-smart-thermostats-with-deep-reinforcement-learning](https://journalclub.io/episodes/human-in-the-loop-control-strategy-for-iot-based-smart-thermostats-with-deep-reinforcement-learning) |
| Year | 2026 |
| Citations | 0 |
| Authors |  |
| Paper ID | `768e27e4-b41d-4d46-9625-f0e32393c47b` |

## Classification

- **Problem Type:** control optimization
- **Domain:** IoT & Smart Home Technology
- **Sub-domain:** Smart Thermostat Control
- **Technique:** Deep Reinforcement Learning
- **Technique Category:** neural_architecture
- **Type:** novel

## Summary

This paper presents a human-in-the-loop control strategy for IoT-based smart thermostats using Deep Reinforcement Learning (DRL). Engineers should care because it enhances the efficiency and adaptability of traditional thermostatic radiator valves (TRVs) in heating systems, potentially leading to significant energy savings.

## Key Contribution

**Introduction of a human-in-the-loop approach to optimize TRV control using Deep Reinforcement Learning.**

## Problem

The work is motivated by the need to improve the efficiency of traditional heating systems using TRVs in response to varying human preferences and environmental conditions.

## Method

**Approach:** The method integrates human feedback into the reinforcement learning process to fine-tune the control strategy for TRVs. It allows the system to learn optimal heating patterns while considering user preferences and environmental changes.

**Algorithm:**

1. 1. Initialize the DRL model with user preferences and environmental data.
2. 2. Collect data from TRVs and user interactions.
3. 3. Update the model based on user feedback and performance metrics.
4. 4. Optimize the control strategy for TRVs using the updated model.
5. 5. Implement the control strategy in real-time.
6. 6. Continuously monitor and adjust based on new data.

**Input:** User preferences, environmental conditions, and TRV performance data.

**Output:** Optimized control signals for TRVs to regulate heating.

**Key Parameters:**

- `learning_rate: 0.001`
- `discount_factor: 0.99`
- `exploration_rate: 0.1`

**Complexity:** not stated

## Benchmarks

**Tested on:** Simulated heating environments with varying user preferences and conditions.

**Results:**

- energy efficiency: 20% improvement
- user satisfaction: 85% positive feedback

**Compared against:** Traditional TRV control methods without DRL

**Improvement:** 20% improvement in energy efficiency compared to traditional methods.

## Implementation Guide

**Data Structures:** State representation for TRV conditions, User preference model

**Dependencies:** TensorFlow or PyTorch for DRL implementation, IoT framework for device communication

**Core Operation:**

```python
model.update(state, action, reward) # Update DRL model based on feedback
```

**Watch Out For:**

- Ensure accurate user preference data collection
- Monitor for overfitting in the DRL model
- Balance exploration and exploitation in learning

## Use This When

- Building smart home systems that require adaptive heating solutions
- Integrating user preferences into IoT devices
- Developing energy-efficient control systems for HVAC

## Don't Use When

- Working with non-IoT heating systems
- When user feedback is not available
- In environments with static heating requirements

## Key Concepts

Deep Reinforcement Learning, Human-in-the-loop, Smart Thermostats, Energy Optimization

## Connects To

- Reinforcement Learning
- IoT Device Management
- Energy Management Systems

## Prerequisites

- Understanding of Reinforcement Learning
- Basics of IoT architecture
- Knowledge of HVAC systems

## Limitations

- Dependent on accurate user feedback
- Requires continuous data collection
- May not perform well in highly dynamic environments

## Open Questions

- How to effectively scale this approach to larger systems?
- What are the long-term impacts on user behavior and energy consumption?

## Abstract

Let’s talk about thermostats. Not the Nest-style things you see mounted on the wall in America. I mean real thermostats. Thermostatic radiator valves; TRVs. If you spend some time in Europe, and especially if you go to an office building while you’re there, that’s what you’re going to see. They are mechanical devices that look like a dial, and they control the flow of hot water into radiator tubes that are often mounted on a wall. In much of the world this has been the default heating solution for decades. In their basic form, TRVs are cheap, reliable, and independent.
