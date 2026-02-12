# GExp

**GExp enables robots to autonomously explore their environment, generate tasks, and learn from experiences using vision-language and large language models.**

**Category:** robotics, autonomous exploration  
**Maturity:** emerging

## How It Works

GExp utilizes an RGB-D camera to observe and understand the environment. It generates scene descriptions to identify objects and employs a large language model (LLM) to create manipulation tasks based on these observations. The robot executes these tasks using a library of skills and verifies their success through both vision-based and code-based methods. Successful tasks are reflected upon to refine the skills library and add new capabilities.

## Algorithm

**Input:** RGB-D camera data, initial skills library, scene language description, observed objects.

**Output:** Refined skills library with newly acquired skills.

**Steps:**

1. 1. Observe the environment using an RGB-D camera.
2. 2. Generate a scene description and identify objects.
3. 3. Use LLM to create manipulation tasks based on the scene.
4. 4. Execute the tasks using a library of acquired skills.
5. 5. Verify the success of each task using vision-based and code-based methods.
6. 6. Reflect on successful tasks to refine and add new skills to the library.

**Core Operation:** `output = refined skills library with newly acquired skills`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `initial_skills` | [movep, close_gripper, open_gripper, get_obj_position, go_home] | Changing the initial skills affects the robot's ability to perform tasks. |
| `BOUNDS` | [[xmin, xmax], [ymin, ymax], [zmin, zmax]] | Adjusting bounds influences the robot's operational area. |

## Complexity

- **Time:** Not explicitly stated
- **Space:** Not explicitly stated
- **In practice:** Performance may vary based on the complexity of the environment and the tasks generated.

## Implementation

```python
def gexp_algorithm(rgbd_data: Any, initial_skills: List[str]) -> List[str]:
    scene_description = observe_environment(rgbd_data)
    objects = identify_objects(scene_description)
    tasks = generate_tasks(objects)
    skills_library = initial_skills
    for task in tasks:
        success = execute_task(task, skills_library)
        if success:
            skills_library = refine_skills(skills_library, task)
    return skills_library
```

## Common Mistakes

- Neglecting to verify task success can lead to skill library inaccuracies.
- Failing to update the skills library may result in outdated capabilities.
- Overlooking the importance of scene understanding can hinder task generation.

## Use When

- You need a robot to autonomously explore and learn in an unknown environment.
- You want to enable a robot to generate tasks based on its observations.
- You require a system that can adapt to various scenarios without prior human input.

## Avoid When

- The robot requires precise human-defined tasks.
- The environment is highly structured and predictable.
- Real-time human intervention is necessary for task execution.

## Tradeoffs

**Strengths:**

- Enables autonomous learning and adaptation.
- Reduces the need for human intervention.
- Utilizes advanced models for scene understanding and task generation.

**Weaknesses:**

- May struggle in highly structured environments.
- Performance can be inconsistent without proper task verification.
- Requires significant computational resources for model inference.

**Compared To:**

- **vs Traditional robotic programming:** GExp is preferable for environments requiring adaptability, while traditional methods are better for predictable tasks.

## Connects To

- Reinforcement Learning
- Vision-Language Models
- Task Planning Algorithms
- Autonomous Navigation Systems

## Evidence (Papers)

- **Growing from Exploration: A Self-Exploring Framework for Robots Based on Foundation Models** - [DOI](https://doi.org/10.26599/AIR.2024.9150037)
