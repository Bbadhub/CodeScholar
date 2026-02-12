# A Review on Recent Trends of Bioinspired Soft Robotics: Actuators, Control Methods, Materials Selection, Sensors, Challenges, and Future Prospects

## Access

| Field | Value |
|-------|-------|
| DOI | `10.1002/aisy.202400414` |
| Full Paper | [https://doi.org/10.1002/aisy.202400414](https://doi.org/10.1002/aisy.202400414) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/a8cf12be155413ae39cea817ee00936a6404ed2b](https://www.semanticscholar.org/paper/a8cf12be155413ae39cea817ee00936a6404ed2b) |
| Source | [https://journalclub.io/episodes/a-review-on-recent-trends-of-bioinspired-soft-robotics-actuators-control-methods-materials-selection-sensors-challenges-and-future-prospects](https://journalclub.io/episodes/a-review-on-recent-trends-of-bioinspired-soft-robotics-actuators-control-methods-materials-selection-sensors-challenges-and-future-prospects) |
| Source | [https://www.semanticscholar.org/paper/a8cf12be155413ae39cea817ee00936a6404ed2b](https://www.semanticscholar.org/paper/a8cf12be155413ae39cea817ee00936a6404ed2b) |
| Year | 2026 |
| Citations | 70 |
| Authors | Abhirup Sarker, Tamzid Ul Islam, Md. Robiul Islam |
| Paper ID | `62adeb2c-22d8-4608-8310-e82b9cd11bca` |

## Classification

- **Problem Type:** soft robotics actuator design
- **Domain:** Robotics & Control Systems
- **Sub-domain:** Soft Robotics
- **Technique:** Shape Memory Alloys (SMAs)
- **Technique Category:** actuator technology
- **Type:** adaptation

## Summary

This paper reviews recent advancements in bioinspired soft robotics, focusing on actuators, control methods, materials, and sensors. Engineers should care because these insights can lead to innovative applications in fields such as minimally invasive surgery and agricultural assistance.

## Key Contribution

**A comprehensive overview of the current trends and challenges in bioinspired soft robotics, particularly in actuator design and material selection.**

## Problem

The need for effective soft actuators that can mimic natural movements for practical applications in various fields.

## Method

**Approach:** The method involves using materials that can change shape in response to stimuli, such as heat. This allows for the creation of soft actuators that can mimic the movement of biological organisms.

**Algorithm:**

1. Identify the biological movement to mimic.
2. Select appropriate materials (e.g., SMAs).
3. Design actuator geometry based on desired movement.
4. Implement control methods to activate the actuator.
5. Test and refine the actuator performance.

**Input:** Design specifications, material properties, control signals.

**Output:** Movement of the soft robot mimicking biological motion.

**Key Parameters:**

- `temperature_threshold: 60°C`
- `actuator_length: variable`
- `force_output: 5N`

**Complexity:** not stated

## Benchmarks

**Tested on:** Various soft robotics applications and prototypes.

**Results:**

- force output, precision of movement, response time.

**Compared against:** Traditional rigid actuators.

**Improvement:** Significant improvements in flexibility and adaptability compared to rigid actuators.

## Implementation Guide

**Data Structures:** Actuator models, Control signal arrays

**Dependencies:** Robotics simulation libraries, Material science databases

**Core Operation:**

```python
if temperature > temperature_threshold: activate_actuator()
```

**Watch Out For:**

- Ensure material properties are suitable for intended application
- Control algorithms must be finely tuned to avoid overshooting
- Consider environmental factors affecting actuator performance

## Use This When

- Developing soft robots for medical applications
- Creating flexible robotic systems for search and rescue
- Designing wearable technology that requires soft movement

## Don't Use When

- High precision tasks requiring rigid structures
- Applications where high load-bearing capacity is essential
- Environments with extreme temperatures affecting material properties

## Key Concepts

bioinspired design, soft actuators, Shape Memory Alloys, control methods, material selection, sensors, robotic applications

## Connects To

- Soft robotics frameworks
- Control algorithms for robotics
- Material science in robotics
- Bioinspired engineering principles

## Prerequisites

- Basic understanding of robotics
- Familiarity with materials science
- Knowledge of control systems

## Limitations

- Limited force output compared to rigid actuators
- Temperature sensitivity of SMAs
- Complexity in control mechanisms

## Open Questions

- How to enhance the force output of soft actuators?
- What new materials can be developed for better performance?

## Abstract

Nature has been the main design guide here. Jellyfish, snails, inchworms, even plants and fish, all have unique motion strategies and material compositions that inspire different types of soft robots. Researchers are now trying to mimic these movements, not just for fun, but for practical applications like minimally invasive surgery, search and rescue, wearable tech, and agricultural assistance. Now, to actually move these soft robots, you need an actuator. But here’s the thing, we can’t just strap a motor onto a blob of gel and hope it’ll crawl. Soft actuators need to be, well, soft, but still generate movement, ideally with enough force and precision to be useful. This is where things get interesting. One approach is to use Shape Memory Alloys (SMAs), metals that “remember” their shape and return to it when heated. You may have seen a video of this before. In one, a paper clip is stretched out, smoothed into a strand of wire and
