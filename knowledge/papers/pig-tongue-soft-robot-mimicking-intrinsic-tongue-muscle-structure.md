# Pig tongue soft robot mimicking intrinsic tongue muscle structure

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3389/frobt.2024.1511422` |
| Full Paper | [https://doi.org/10.3389/frobt.2024.1511422](https://doi.org/10.3389/frobt.2024.1511422) |
| Source | [https://journalclub.io/episodes/pig-tongue-soft-robot-mimicking-intrinsic-tongue-muscle-structure](https://journalclub.io/episodes/pig-tongue-soft-robot-mimicking-intrinsic-tongue-muscle-structure) |
| Year | 2026 |
| Citations | 0 |
| Authors |  |
| Paper ID | `5d80a0a1-de08-499b-a9dc-62af123bbe6a` |

## Classification

- **Problem Type:** soft robotics design and muscle mimicry
- **Domain:** Robotics & Control Systems
- **Sub-domain:** Soft robotics, biomimetic design
- **Technique:** Pig tongue soft robot
- **Technique Category:** framework
- **Type:** novel

## Summary

This study presents a soft robot designed to mimic the intrinsic muscle structure of a pig tongue, utilizing silicone materials and McKibben artificial muscles. Engineers should care because this work advances soft robotics by providing a platform for studying muscle-motion relationships and developing multifunctional manipulators.

## Key Contribution

**Development of a soft robot that accurately replicates the intrinsic muscular structure of a pig tongue using advanced materials and techniques.**

## Problem

The need for advanced soft robotic systems that can replicate complex biological structures for manipulation and research purposes.

## Method

**Approach:** The method involves 3D scanning of a pig tongue to analyze the arrangement of intrinsic muscles, followed by the creation of a 3D model. This model is used to fabricate a soft robot using silicone materials and embedded McKibben artificial muscles to replicate muscle movements and stiffness.

**Algorithm:**

1. 1. Perform 3D scans of the pig tongue.
2. 2. Analyze muscle arrangement using heating and Dice-CT methods.
3. 3. Create a 3D model of the tongue.
4. 4. Fabricate molds for the tongue robot.
5. 5. Embed McKibben artificial muscles into the silicone structure.
6. 6. Fill the robot body with silicone gel to mimic muscle hydrostat properties.
7. 7. Conduct experiments to measure motion and stiffness.

**Input:** 3D scans of a pig tongue, silicone rubber, silicone gel, McKibben artificial muscles.

**Output:** A soft robotic tongue that mimics the movements and stiffness of a biological tongue.

**Key Parameters:**

- `silicone_rubber: Smooth-On, Ecoflex 00-10`
- `silicone_gel: Smooth-On, Ecoflex GEL`
- `artificial_muscle_diameter: 2-3 mm`
- `air_pressure: up to 0.5 MPa`

**Complexity:** not stated

## Benchmarks

**Tested on:** 3D scans of pig tongues

**Results:**

- displacement of tongue tip
- deformation measurements
- stiffness changes

**Compared against:** Previous robotic tongue designs using wires and motors

**Improvement:** Demonstrated characteristic tongue motions and variable stiffness not previously explored.

## Implementation Guide

**Data Structures:** 3D models of the tongue, molds for silicone casting

**Dependencies:** Blender for 3D modeling, Revopoint scanning software, Silicone materials

**Core Operation:**

```python
create_tongue_robot(model): embed_muscles(model); fill_with_gel(model); test_movement(model)
```

**Watch Out For:**

- Ensure accurate 3D scanning to avoid deformation in the model.
- Monitor the curing process of silicone to maintain structural integrity.
- Carefully position artificial muscles to avoid interference during movement.

## Use This When

- Developing soft robots for manipulation tasks requiring flexibility.
- Studying muscle dynamics and motion relationships in robotics.
- Creating biomimetic devices for research in biological systems.

## Don't Use When

- High precision tasks requiring rigid structures.
- Applications where high load-bearing capacity is essential.
- Environments with extreme temperatures affecting silicone materials.

## Key Concepts

soft robotics, biomimetic design, artificial muscles, 3D modeling, muscle hydrostat, Dice-CT imaging

## Connects To

- McKibben artificial muscles
- soft robotic manipulators
- biomimetic design principles

## Prerequisites

- Understanding of soft robotics
- Knowledge of 3D modeling techniques
- Familiarity with pneumatic systems

## Limitations

- Limited load capacity compared to rigid robots
- Potential degradation of silicone materials over time
- Complex manufacturing process requiring precision

## Open Questions

- How can the design be optimized for different applications?
- What are the long-term durability effects of the materials used?

## Abstract

This study exists for one reason: to push soft robotics forward, just a little. How? By attempting to reconstruct the internal muscle layout of a real tongue. The authors are building a pig tongue using silicone rubber, silicone gel, and embedded McKibben artificial muscles, all shaped using 3D-printed molds
