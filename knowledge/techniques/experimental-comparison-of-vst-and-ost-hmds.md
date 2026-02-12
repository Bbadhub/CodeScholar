# Experimental comparison of VST and OST HMDs

*Also known as: Virtual Spatial Technology (VST), Optical Spatial Technology (OST)*

**This technique compares the performance of tasks using Virtual Spatial Technology (VST) and Optical Spatial Technology (OST) head-mounted displays (HMDs) against unaided vision.**

**Category:** user_experience_research  
**Maturity:** emerging

## How It Works

Participants are divided into two groups, each using either VST or OST HMDs to perform specific tasks. Their performance is measured in terms of completion time, accuracy, and self-reported discomfort. The results are statistically analyzed to determine the effectiveness of each HMD type compared to unaided vision.

## Algorithm

**Input:** Participant performance data including completion times, accuracy scores, and self-reported discomfort levels.

**Output:** Statistical analysis results comparing task performance with VST and OST HMDs against unaided vision.

**Steps:**

1. 1. Recruit participants and divide them into two groups.
2. 2. Assign each group to perform tasks with either VST or OST HMDs.
3. 3. Each participant performs tasks twice: once with HMD and once without.
4. 4. Record completion time, accuracy, and self-reported discomfort.
5. 5. Analyze the collected data statistically to compare performance across conditions.

**Core Operation:** `output = statistical_analysis(performance_data)`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `number_of_participants` | 80 | More participants may yield more reliable results. |
| `task_types` | ['dart throwing', 'bottle filling'] | Different tasks may influence the effectiveness of HMDs. |
| `HMD_types` | ['Meta Quest 3', 'Microsoft HoloLens'] | Different HMDs may have varying impacts on performance. |

## Complexity

- **Time:** O(n)
- **Space:** O(1)
- **In practice:** The complexity is primarily dependent on the number of participants and tasks.

## Implementation

```python
def compare_hmd_performance(participants: List[Participant]) -> AnalysisResult:
    for participant in participants:
        perform_tasks(participant)
        record_performance(participant)
    return analyze_results(participants)
```

## Common Mistakes

- Not accounting for individual differences in participant performance.
- Failing to ensure a balanced design between VST and OST groups.
- Neglecting to measure and report discomfort levels adequately.

## Use When

- Designing AR applications that require high precision and user interaction.
- Evaluating the effectiveness of different HMD technologies in real-world tasks.
- Conducting user studies to assess the impact of visual technologies on task performance.

## Avoid When

- Tasks that do not require precise motor control or depth perception.
- When user comfort and visual fatigue are critical factors in task execution.
- In environments where latency and perceptual distortion are unacceptable.

## Tradeoffs

**Strengths:**

- Provides empirical data on HMD performance.
- Helps identify user preferences and discomfort levels.
- Facilitates informed decisions in AR application design.

**Weaknesses:**

- May not generalize to all types of tasks or environments.
- Participant variability can introduce noise in results.
- Requires careful experimental design to avoid bias.

**Compared To:**

- **vs User Experience Testing:** Use this technique for specific HMD comparisons, while user experience testing is broader.

## Connects To

- User Experience Testing
- Augmented Reality Development
- Human-Computer Interaction Research
- Virtual Reality Applications

## Evidence (Papers)

- **Perception and Precision: How VST and OST Headsets Influence Task Execution** - [DOI](https://doi.org/10.5753/jis.2025.5921)
