# In-situ Participatory Design Methodology

*Also known as: Participatory Design, Co-design Methodology*

**A collaborative approach to design that involves stakeholders directly in the development process to ensure the final product meets their needs.**

**Category:** design_methodology  
**Maturity:** emerging

## How It Works

This methodology consists of three main phases: observation and inspiration, in-situ co-design through prototyping, and longitudinal evaluation. Initially, researchers observe and interview users to gather insights about their needs. Then, low-fidelity prototypes are developed and refined through collaborative sessions with stakeholders, allowing for iterative feedback. Finally, the prototypes are deployed in real-world settings to evaluate their effectiveness and gather further user feedback for refinement.

## Algorithm

**Input:** User requirements, environmental context, low-fidelity prototypes.

**Output:** Refined assistive robot design and functionality tailored to user needs.

**Steps:**

1. 1. Conduct initial observations and interviews to understand user needs.
2. 2. Develop a low-fidelity prototype based on initial insights.
3. 3. Engage stakeholders in co-design sessions to define functionalities and interactions.
4. 4. Iterate on the prototype based on user feedback.
5. 5. Deploy the prototype in a real-world setting for evaluation.
6. 6. Collect user feedback and performance data during the deployment.
7. 7. Refine the design based on longitudinal evaluation results.

**Core Operation:** `output = refined_design(user_feedback, performance_data)`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `iteration_count` | variable (depends on user feedback) | More iterations can lead to better alignment with user needs. |
| `deployment_duration` | 2 months | Longer deployment allows for more comprehensive feedback. |
| `evaluation_duration` | 10 months total (8 months design + 2 months evaluation) | Extended evaluation provides deeper insights into user adoption and satisfaction. |

## Complexity

- **Time:** Not explicitly stated
- **Space:** Not explicitly stated
- **In practice:** The methodology is resource-intensive due to the need for stakeholder involvement and iterative processes.

## Implementation

```python
def participatory_design(user_needs: List[str], context: str) -> str:
    prototype = develop_prototype(user_needs)
    feedback = []
    for stakeholder in engage_stakeholders():
        feedback.append(co_design_session(prototype, stakeholder))
    refined_design = iterate_prototype(prototype, feedback)
    deploy(refined_design)
    return evaluate_design(refined_design)
```

## Common Mistakes

- Neglecting to involve all relevant stakeholders in the design process.
- Rushing through the prototyping phase without adequate feedback.
- Failing to adapt the design based on user feedback during evaluation.

## Use When

- Designing assistive robots for healthcare settings.
- Engaging with stakeholders who have limited experience with robotic technologies.
- Seeking to align robotic functionalities with real-world user needs.

## Avoid When

- The user group has extensive prior experience with robotic systems.
- Rapid prototyping is required without stakeholder involvement.
- The project timeline does not allow for iterative feedback.

## Tradeoffs

**Strengths:**

- Ensures the final product is closely aligned with user needs.
- Encourages stakeholder buy-in and satisfaction.
- Facilitates the discovery of diverse user perspectives.

**Weaknesses:**

- Can be time-consuming and resource-intensive.
- May lead to scope creep if not managed properly.
- Requires skilled facilitation to manage stakeholder interactions.

**Compared To:**

- **vs Traditional Design Methodologies:** Use participatory design when user involvement is critical for success.

## Connects To

- User-Centered Design
- Agile Development
- Design Thinking
- Co-Creation

## Evidence (Papers)

- **An in-situ participatory approach for assistive robots: methodology and implementation in a healthcare setting** [1 citations] - [DOI](https://doi.org/10.3389/frobt.2025.1648737)
