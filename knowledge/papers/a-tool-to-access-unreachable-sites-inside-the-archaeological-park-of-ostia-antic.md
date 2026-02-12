# A tool to access unreachable sites inside the Archaeological Park of Ostia Antica in Rome

## Access

| Field | Value |
|-------|-------|
| DOI | `10.6092/issn.1973-9494/20041` |
| Full Paper | [https://doi.org/10.6092/issn.1973-9494/20041](https://doi.org/10.6092/issn.1973-9494/20041) |
| Source | [https://journalclub.io/episodes/a-tool-to-access-unreachable-sites-inside-the-archaeological-park-of-ostia-antica-in-rome](https://journalclub.io/episodes/a-tool-to-access-unreachable-sites-inside-the-archaeological-park-of-ostia-antica-in-rome) |
| Year | 2026 |
| Citations | 0 |
| Authors |  |
| Paper ID | `d5affd7b-ef1e-4d02-826d-5a44f39eda6c` |

## Classification

- **Problem Type:** virtual site exploration
- **Domain:** Human-Computer Interaction
- **Sub-domain:** Virtual Reality Applications
- **Technique:** Virtual Access Tool
- **Technique Category:** framework
- **Type:** novel

## Summary

The paper presents a tool designed to provide virtual access to the archaeological site of Casa Di Diana in Ostia Antica, allowing users to explore its historical significance without physical presence. Engineers should care because it addresses the challenge of preserving fragile archaeological sites while making them accessible to the public.

## Key Contribution

**A virtual access tool that enables exploration of fragile archaeological sites without physical intrusion.**

## Problem

The need to share the historical and archaeological significance of fragile sites like Casa Di Diana with the public without causing damage.

## Method

**Approach:** The method involves creating a virtual representation of Casa Di Diana that users can interact with remotely. This allows for educational experiences without compromising the integrity of the physical site.

**Algorithm:**

1. 1. Collect data on the physical structure of Casa Di Diana.
2. 2. Create a 3D model based on the collected data.
3. 3. Develop a user interface for interaction with the 3D model.
4. 4. Implement navigation features to explore different areas of the site.
5. 5. Integrate educational content related to the site's history.

**Input:** 3D models and historical data of Casa Di Diana.

**Output:** An interactive virtual environment for users to explore.

**Key Parameters:**

- `model_resolution: high`
- `interaction_type: user-friendly`

**Complexity:** not stated

## Benchmarks

**Tested on:** 3D scans of Casa Di Diana, historical records

**Results:**

- user engagement: time spent in the virtual environment
- educational impact: user feedback

**Compared against:** traditional site tours, other virtual tours of archaeological sites

**Improvement:** Significantly enhances accessibility compared to physical tours.

## Implementation Guide

**Data Structures:** 3D model data, user interaction logs

**Dependencies:** Unity or Unreal Engine for 3D rendering, WebGL for browser-based access

**Core Operation:**

```python
create_virtual_tour(model_data): render(model_data) -> enable_user_interaction()
```

**Watch Out For:**

- Ensure high-quality 3D models to enhance user experience.
- Consider accessibility features for diverse user groups.
- Test the application on various devices for compatibility.

## Use This When

- You want to provide access to fragile archaeological sites.
- You need to create an educational tool for historical sites.
- You are developing a virtual reality application for cultural heritage.

## Don't Use When

- The site is stable and can be safely accessed by the public.
- You require real-time interaction with physical artifacts.
- The target audience lacks access to necessary technology.

## Key Concepts

3D modeling, user interface design, virtual reality, educational technology

## Connects To

- 3D rendering techniques
- virtual reality frameworks
- educational software development

## Prerequisites

- Basic understanding of 3D modeling
- Familiarity with user interface design principles
- Knowledge of virtual reality technologies

## Limitations

- Requires significant initial investment in 3D modeling.
- May not capture the full experience of physical presence.
- Dependent on user technology for access.

## Open Questions

- How can we improve user engagement in virtual environments?
- What are the best practices for preserving the integrity of virtual representations?

## Abstract

A half-hour drive south west of Rome sits an archaeological site called Ostia Antica. It’s the ruins of an ancient city from two millennia ago. Right in the center of the site is a brick house called “Casa Di Diana” (Diana’s House). It’s believed to originally have been a five-story building used for both residential and commercial activities. Now it’s a series of half-standing walls, chambers and pillars. From an archaeological perspective, Casa Di Diana is important. It’s one of the many treasures left from the Roman empire. A site that the archaeologists who have been studying it would love to share with the world. But, in its current form, it’s simply too fragile to let anyone but trained professionals visit.
