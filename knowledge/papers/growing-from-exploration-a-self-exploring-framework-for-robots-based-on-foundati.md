# Growing from Exploration: A Self-Exploring Framework for Robots Based on Foundation Models

## Access

| Field | Value |
|-------|-------|
| DOI | `10.26599/AIR.2024.9150037` |
| Full Paper | [https://doi.org/10.26599/AIR.2024.9150037](https://doi.org/10.26599/AIR.2024.9150037) |
| Source | [https://journalclub.io/episodes/growing-from-exploration-a-self-exploring-framework-for-robots-based-on-foundation-models](https://journalclub.io/episodes/growing-from-exploration-a-self-exploring-framework-for-robots-based-on-foundation-models) |
| Year | 2026 |
| Citations | 0 |
| Authors |  |
| Paper ID | `7d58c3f9-8e1f-4eba-81bd-cba9ffaffe2f` |

## Classification

- **Problem Type:** autonomous exploration and skill acquisition
- **Domain:** Robotics & Control Systems
- **Sub-domain:** Autonomous Robotics
- **Technique:** GExp
- **Technique Category:** framework
- **Type:** novel

## Summary

The paper presents GExp, a self-exploring framework for robots that enables autonomous exploration and skill acquisition without human intervention. This framework leverages foundation models to allow robots to generate and execute tasks based on their experiences, enhancing their adaptability to various environments.

## Key Contribution

**A framework for autonomous self-exploration in robots that does not require prior knowledge or human-defined tasks.**

## Problem

The challenge of enabling robots to explore various environments and learn autonomously remains unresolved.

## Method

**Approach:** GExp allows robots to autonomously explore their environment, generate tasks, and learn from successful experiences. It employs vision-language models for scene understanding and large language models for task generation and execution.

**Algorithm:**

1. 1. Observe the environment using an RGB-D camera.
2. 2. Generate a scene description and identify objects.
3. 3. Use LLM to create manipulation tasks based on the scene.
4. 4. Execute the tasks using a library of acquired skills.
5. 5. Verify the success of each task using vision-based and code-based methods.
6. 6. Reflect on successful tasks to refine and add new skills to the library.

**Input:** RGB-D camera data, initial skills library, scene language description, observed objects.

**Output:** Refined skills library with newly acquired skills.

**Key Parameters:**

- `initial_skills: [movep, close_gripper, open_gripper, get_obj_position, go_home]`
- `BOUNDS: [[xmin, xmax], [ymin, ymax], [zmin, zmax]]`

**Complexity:** not stated

## Benchmarks

**Tested on:** BLOCKS WORLD, RLBench

**Results:**

- successful rate

**Compared against:** framework without collecting skills, framework without self-verification

**Improvement:** GExp achieved an average successful rate of 0.83 compared to 0.32 and 0.25 for the baselines.

## Implementation Guide

**Data Structures:** skills library, scene description, task list

**Dependencies:** Foundation models (LLM, VLM), Robot SDK

**Core Operation:**

```python
while exploring: generate_task(scene) -> execute_task(task) -> verify_success(task)
```

**Watch Out For:**

- Ensure the skills library is updated after each successful task.
- Be cautious of grounding errors during execution.
- Monitor the robot's ability to adapt to new environments.

## Use This When

- You need a robot to autonomously explore and learn in an unknown environment.
- You want to enable a robot to generate tasks based on its observations.
- You require a system that can adapt to various scenarios without prior human input.

## Don't Use When

- The robot requires precise human-defined tasks.
- The environment is highly structured and predictable.
- Real-time human intervention is necessary for task execution.

## Key Concepts

self-exploration, skills library, task generation, scene understanding, backtracking control, vision-language models, large language models

## Connects To

- Reinforcement Learning
- Imitation Learning
- Multi-robot Coordination

## Prerequisites

- Understanding of foundation models
- Basic robotics programming
- Knowledge of task planning

## Limitations

- Performance may degrade in highly complex environments.
- Limited capability in object detection and semantic grounding.
- Not all self-generated plans may be feasible.

## Open Questions

- How can the framework be improved for real-time applications?
- What additional skills can be integrated into the skills library?

## Abstract

The planning and execution module decomposes tasks into executable sub-tasks, again using LLM-based reasoning. Each task is processed into a sequence of commands. These commands are specific to whatever kind of robot the system is running onboard. And they could either be straight from the SDK or from a source we haven’t mentioned yet. The system has an onboard list of previously acquired skills. They call it the skills library. We’ll come back to how skills get into the library in a moment. For now, just know that as the robot is exploring its environment, the actions it previously tried that were successful in other contexts are available to it in the skills library. Once a series of actions is chosen, the execution module generates code to control the robot. During execution, the module ensures task
