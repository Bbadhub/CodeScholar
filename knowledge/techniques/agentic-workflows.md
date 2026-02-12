# Agentic Workflows

**Agentic Workflows enhance large language model reasoning through structured iterative feedback in robotic object-centered planning.**

**Category:** neural_architecture  
**Maturity:** emerging

## How It Works

Agentic Workflows integrate large language models (LLMs) with structured workflows to improve reasoning and reduce inaccuracies in outputs. The process begins with inputting a semantic map and a natural language query into the LLM. An initial response is generated, which is then evaluated and refined through a self-reflection mechanism, allowing for iterative feedback. This approach helps in achieving more accurate object identification and reduces hallucinations in the model's responses.

## Algorithm

**Input:** A semantic map in JSON format and a natural language query.

**Output:** A ranked list of relevant object identifiers from the semantic map.

**Steps:**

1. 1. Input a semantic map and a natural language query to the LLM.
2. 2. Generate an initial response listing relevant objects.
3. 3. Apply the Self-Reflection workflow to evaluate the response based on correctness, relevance, and clarity.
4. 4. Generate feedback and refine the initial response based on this feedback.
5. 5. Optionally repeat the reflection and refinement steps for improved accuracy.

**Core Operation:** `output = refined_response(initial_response, feedback)`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `max_iterations` | 5 | Limits the number of refinement cycles, impacting the thoroughness of the output. |
| `feedback_threshold` | 0.8 | Determines the minimum feedback score required to trigger further refinement. |

## Complexity

- **Time:** Not stated
- **Space:** Not stated
- **In practice:** Performance may vary based on the complexity of the input queries and the size of the semantic map.

## Implementation

```python
def agentic_workflow(semantic_map: dict, query: str) -> list:
    initial_response = generate_initial_response(semantic_map, query)
    feedback = evaluate_response(initial_response)
    refined_response = refine_response(initial_response, feedback)
    return refined_response
```

## Common Mistakes

- Neglecting to set appropriate feedback thresholds, leading to ineffective refinements.
- Failing to iterate sufficiently, resulting in suboptimal outputs.
- Overlooking the importance of the semantic map's quality in generating accurate responses.

## Use When

- You need to improve the accuracy of object identification in robotic systems.
- Your application involves complex queries that require reasoning about object functions.
- You want to mitigate hallucinations in LLM outputs for robotic tasks.

## Avoid When

- The task requires real-time responses with minimal processing time.
- The environment is static and does not require complex reasoning.
- You have a limited computational budget that cannot support multiple LLMs.

## Tradeoffs

**Strengths:**

- Improves reasoning capabilities of LLMs in complex tasks.
- Reduces hallucinations in model outputs.
- Facilitates iterative learning and refinement.

**Weaknesses:**

- May require significant computational resources.
- Not suitable for real-time applications.
- Complexity in implementation may deter some users.

**Compared To:**

- **vs Single-step LLM prompt approach:** Use Agentic Workflows for improved accuracy and reasoning in complex scenarios.

## Connects To

- Reinforcement Learning
- Self-Reflection Mechanisms
- Multi-Agent Systems
- Natural Language Processing

## Evidence (Papers)

- **Agentic Workflows for Improving Large Language Model Reasoning in Robotic Object-Centered Planning** - [DOI](https://doi.org/10.3390/robotics14030024)
