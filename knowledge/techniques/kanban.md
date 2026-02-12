# Kanban

*Also known as: Kanban Method, Kanban System*

**Kanban visualizes work to manage and improve the flow of tasks through a system, allowing teams to self-organize and adapt to changes.**

**Category:** project_management  
**Maturity:** proven (widely used in production)

## How It Works

Kanban uses a visual board to represent the workflow of tasks, helping teams to see the status of work items at a glance. By limiting the number of tasks in progress (WIP), it enhances efficiency and predictability. Teams continuously monitor and adjust their processes based on feedback, fostering a culture of iterative improvement and collaboration.

## Algorithm

**Input:** Work items/tasks that need to be managed.

**Output:** Improved workflow efficiency and service delivery.

**Steps:**

1. 1. Visualize the workflow using a Kanban board.
2. 2. Limit the number of work items in progress (WIP).
3. 3. Manage flow by monitoring and adjusting the work process.
4. 4. Make policies explicit to guide decision-making.
5. 5. Implement feedback cycles to continuously improve the process.
6. 6. Evolve the system collaboratively through experimentation.

**Core Operation:** `output = improved workflow efficiency and service delivery`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `WIP limit` | varies by team and project | Limiting WIP can enhance focus and reduce bottlenecks. |
| `Feedback cycle frequency` | daily/weekly | More frequent feedback can lead to quicker adjustments and improvements. |
| `Visualization tools` | Kanban board, metrics | Effective visualization aids in tracking progress and identifying issues. |

## Complexity

- **Time:** O(n) for monitoring tasks
- **Space:** O(n) for storing task states
- **In practice:** Real-world performance can vary based on team size and complexity of workflows.

## Implementation

```python
def kanban_board(tasks: List[Task], wip_limit: int) -> None:
    visualize_workflow(tasks)
    while not all_tasks_completed(tasks):
        if current_wip(tasks) < wip_limit:
            start_next_task(tasks)
        monitor_flow(tasks)
        implement_feedback_cycle()
        evolve_system()
```

## Common Mistakes

- Not setting appropriate WIP limits, leading to bottlenecks.
- Failing to visualize the workflow effectively.
- Ignoring feedback cycles, which can hinder improvement.

## Use When

- You need to manage complex workflows in software development.
- Your team is facing challenges with project delivery timelines.
- You want to implement a flexible and adaptive project management approach.

## Avoid When

- The project requires strict adherence to predefined methodologies.
- You have a small team with very simple workflows.
- The organization is not open to iterative improvements.

## Tradeoffs

**Strengths:**

- Enhances visibility of work processes.
- Promotes team autonomy and self-organization.
- Facilitates continuous improvement through feedback.

**Weaknesses:**

- May not suit projects requiring strict methodologies.
- Can become chaotic without proper management.
- Requires cultural buy-in for effective implementation.

**Compared To:**

- **vs Scrum:** Use Kanban for continuous flow and flexibility; use Scrum for structured sprints and roles.

## Connects To

- Scrum
- Lean
- Agile methodologies
- Continuous Delivery
- Value Stream Mapping

## Evidence (Papers)

- **Analysis of project management principles with the Scrum framework in systems development: a case study in a public organization** - [DOI](https://doi.org/10.14488/BJOPM.1878.2024)
