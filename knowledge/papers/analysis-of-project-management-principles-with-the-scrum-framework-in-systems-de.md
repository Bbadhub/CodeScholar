# Analysis of project management principles with the Scrum framework in systems development: a case study in a public organization

## Access

| Field | Value |
|-------|-------|
| DOI | `10.14488/BJOPM.1878.2024` |
| Full Paper | [https://doi.org/10.14488/BJOPM.1878.2024](https://doi.org/10.14488/BJOPM.1878.2024) |
| Source | [https://journalclub.io/episodes/analysis-of-project-management-principles-with-the-scrum-framework-in-systems-development-a-case-study-in-a-public-organization](https://journalclub.io/episodes/analysis-of-project-management-principles-with-the-scrum-framework-in-systems-development-a-case-study-in-a-public-organization) |
| Year | 2026 |
| Citations | 0 |
| Authors |  |
| Paper ID | `5820a9d5-6b46-4a8b-97e3-75ec75911aa8` |

## Classification

- **Problem Type:** workflow management in software development
- **Domain:** Software Engineering
- **Sub-domain:** Agile methodologies, Kanban framework
- **Technique:** Kanban
- **Technique Category:** framework
- **Type:** adaptation

## Summary

The paper analyzes the application of project management principles using the Scrum framework within systems development in a public organization, demonstrating how Kanban can enhance workflow management and service delivery. Engineers should care because it provides a structured approach to improve project efficiency and adaptability in software development.

## Key Contribution

**The introduction of Kanban as a method to manage knowledge work effectively within existing workflows.**

## Problem

The need for improved efficiency and adaptability in delivering software services in public organizations.

## Method

**Approach:** Kanban visualizes work to manage and improve the flow of tasks through a system, allowing teams to self-organize and adapt to changes. It emphasizes limiting work in progress (WIP) to enhance efficiency and predictability.

**Algorithm:**

1. 1. Visualize the workflow using a Kanban board.
2. 2. Limit the number of work items in progress (WIP).
3. 3. Manage flow by monitoring and adjusting the work process.
4. 4. Make policies explicit to guide decision-making.
5. 5. Implement feedback cycles to continuously improve the process.
6. 6. Evolve the system collaboratively through experimentation.

**Input:** Work items/tasks that need to be managed.

**Output:** Improved workflow efficiency and service delivery.

**Key Parameters:**

- `WIP limit: varies by team and project`
- `Feedback cycle frequency: daily/weekly`
- `Visualization tools: Kanban board, metrics`

**Complexity:** not stated

## Benchmarks

**Tested on:** Case study in a public organization

**Results:**

- Cycle time, lead time, throughput

**Compared against:** Traditional project management methods

**Improvement:** Significant improvements in workflow efficiency and adaptability were observed, though specific percentages were not stated.

## Implementation Guide

**Data Structures:** Kanban board, Task cards, Metrics tracking tools

**Dependencies:** Kanban software tools (e.g., Trello, Jira), Collaboration tools (e.g., Slack, Microsoft Teams)

**Core Operation:**

```python
for task in kanban_board: if task.is_ready(): move_to_next_stage(task)
```

**Watch Out For:**

- Failing to limit WIP can lead to bottlenecks.
- Not making policies explicit can cause confusion.
- Ignoring feedback cycles can hinder continuous improvement.

## Use This When

- You need to manage complex workflows in software development.
- Your team is facing challenges with project delivery timelines.
- You want to implement a flexible and adaptive project management approach.

## Don't Use When

- The project requires strict adherence to predefined methodologies.
- You have a small team with very simple workflows.
- The organization is not open to iterative improvements.

## Key Concepts

Kanban, Scrum, Agile, Workflow visualization, WIP limits, Feedback cycles, Continuous improvement

## Connects To

- Scrum
- Lean methodologies
- Agile project management
- Continuous delivery
- DevOps

## Prerequisites

- Understanding of Agile principles
- Familiarity with project management concepts
- Basic knowledge of workflow processes

## Limitations

- Kanban may not fit well in highly regulated environments.
- Requires cultural change within the organization to be effective.
- Not suitable for projects with fixed scope and timelines.

## Open Questions

- How can Kanban be integrated with other project management frameworks?
- What are the best practices for scaling Kanban in large organizations?

## Abstract

Let’s start at the beginning. Up until about two decades ago, you didn’t download software. You bought it at a store, in a box. It was a physical product. For that to happen, the software had to be put on some kind of medium, boxed, wrapped, put in a bigger box with others smaller boxes, then put on a pallet with other bigger boxes, wrapped in shrinkwrap, stored in a warehouse, sent to a distributor, trucked to the store, unpacked, and put on a shelf. There was a physical supply chain, and getting your code from your workstation to the customer’s machine took a very long time, and was very expensive. For this reason, software updates were
