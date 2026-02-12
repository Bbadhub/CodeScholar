# An in-situ participatory approach for assistive robots: methodology and implementation in a healthcare setting

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3389/frobt.2025.1648737` |
| Full Paper | [https://doi.org/10.3389/frobt.2025.1648737](https://doi.org/10.3389/frobt.2025.1648737) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/1ace136fd58c90754b5369eb5dfd0dc49da68df4](https://www.semanticscholar.org/paper/1ace136fd58c90754b5369eb5dfd0dc49da68df4) |
| Source | [https://journalclub.io/episodes/an-in-situ-participatory-approach-for-assistive-robots-methodology-and-implementation-in-a-healthcare-setting](https://journalclub.io/episodes/an-in-situ-participatory-approach-for-assistive-robots-methodology-and-implementation-in-a-healthcare-setting) |
| Source | [https://www.semanticscholar.org/paper/1ace136fd58c90754b5369eb5dfd0dc49da68df4](https://www.semanticscholar.org/paper/1ace136fd58c90754b5369eb5dfd0dc49da68df4) |
| Year | 2026 |
| Citations | 1 |
| Authors | Ferran Gebellí, Raquel Ros |
| Paper ID | `db35225c-396b-4b42-9505-ff26828d4571` |

## Classification

- **Problem Type:** human-robot interaction design
- **Domain:** Robotics & Control Systems
- **Sub-domain:** Assistive Robotics
- **Technique:** In-situ Participatory Design Methodology
- **Technique Category:** framework
- **Type:** novel

## Summary

This paper presents a participatory design methodology for developing assistive robots tailored to real-world user needs, particularly in healthcare settings. Engineers should care because it emphasizes iterative co-design with stakeholders, leading to more effective and user-friendly robotic systems.

## Key Contribution

**A comprehensive participatory design approach that integrates iterative in-situ co-design for developing assistive robots in healthcare environments.**

## Problem

The traditional design of assistive robots often fails to meet the practical needs of users due to a disconnect between technology and real-world application contexts.

## Method

**Approach:** The methodology consists of three phases: observation and inspiration, in-situ co-design through prototyping, and longitudinal evaluation. Stakeholders collaborate with researchers using low-fidelity prototypes to define functionality and refine system behavior.

**Algorithm:**

1. 1. Conduct initial observations and interviews to understand user needs.
2. 2. Develop a low-fidelity prototype based on initial insights.
3. 3. Engage stakeholders in co-design sessions to define functionalities and interactions.
4. 4. Iterate on the prototype based on user feedback.
5. 5. Deploy the prototype in a real-world setting for evaluation.
6. 6. Collect user feedback and performance data during the deployment.
7. 7. Refine the design based on longitudinal evaluation results.

**Input:** User requirements, environmental context, low-fidelity prototypes.

**Output:** Refined assistive robot design and functionality tailored to user needs.

**Key Parameters:**

- `iteration_count: variable (depends on user feedback)`
- `deployment_duration: 2 months`
- `evaluation_duration: 10 months total (8 months design + 2 months evaluation)`

**Complexity:** Not stated

## Benchmarks

**Tested on:** User feedback from healthcare staff and patients during the 2-month deployment period.

**Results:**

- Usability, user adoption patterns, satisfaction levels.

**Compared against:** Traditional design methodologies without participatory design.

**Improvement:** Identified five distinct user personas reflecting varying levels of adoption and satisfaction.

## Implementation Guide

**Data Structures:** User feedback forms, Prototype design documents, Deployment logs

**Dependencies:** Prototyping tools (e.g., CAD software), User feedback collection tools (e.g., surveys)

**Core Operation:**

```python
for each user in stakeholders: gather feedback; refine prototype; repeat until satisfactory.
```

**Watch Out For:**

- Ensure stakeholders are engaged throughout the process to avoid misalignment.
- Be prepared for continuous iteration based on user feedback.
- Manage expectations regarding the capabilities of the robotic system.

## Use This When

- Designing assistive robots for healthcare settings.
- Engaging with stakeholders who have limited experience with robotic technologies.
- Seeking to align robotic functionalities with real-world user needs.

## Don't Use When

- The user group has extensive prior experience with robotic systems.
- Rapid prototyping is required without stakeholder involvement.
- The project timeline does not allow for iterative feedback.

## Key Concepts

participatory design, human-robot interaction, iterative prototyping, contextual requirements gathering, longitudinal evaluation

## Connects To

- User-Centered Design
- Agile Development Methodologies
- Human Factors Engineering

## Prerequisites

- Basic understanding of robotics
- Familiarity with participatory design principles
- Knowledge of user experience research methods

## Limitations

- May require significant time investment for iterative design
- Dependent on stakeholder availability and engagement
- Performance issues may arise during initial deployments

## Open Questions

- How can this methodology be adapted for other domains beyond healthcare?
- What are the long-term impacts of assistive robots on user behavior and workflow?

## Abstract

The authors are making the argument that the way we design assistive robots (particularly for the elderly) is all wrong. The status-quo is that we start from technology that's available, build a robot with all the latest bells and whistles, and then try to adapt it for use as a helper or companion in real-world settings.
