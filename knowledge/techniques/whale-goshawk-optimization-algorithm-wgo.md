# Whale-Goshawk Optimization Algorithm (WGO)

**WGO is an optimization algorithm designed for service composition in uncertain cloud manufacturing environments.**

**Category:** optimization_algorithm  
**Maturity:** emerging

## How It Works

WGO operates in two stages: first, it performs a global search to identify potential service combinations using a similar integer coding method based on Quality of Service (QoS) attributes. Next, it refines these combinations through a local search that groups services with similar QoS characteristics using cosine similarity. This dual approach enhances the search for optimal service compositions tailored to user preferences.

## Algorithm

**Input:** User request for service composition, including QoS preferences and task requirements.

**Output:** Optimal service composition that maximizes QoS attributes according to user preferences.

**Steps:**

1. 1. Decompose the user request into subtasks.
2. 2. Construct a candidate service set (CSS) for each subtask.
3. 3. Apply similar integer coding to the CSS based on QoS similarity.
4. 4. Perform a global search using WOA to identify promising service combinations.
5. 5. Execute a local search using NGO to refine the identified combinations.
6. 6. Evaluate the service combinations based on user-defined QoS preferences.
7. 7. Return the optimal service composition.

**Core Operation:** `output = optimal service composition based on QoS attributes`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `cosine_similarity_threshold` | 0.6 | Higher values may reduce the number of grouped services, potentially missing some optimal combinations. |
| `γ` | 0.3 | Adjusting this parameter influences the balance between exploration and exploitation in the search. |
| `max_iterations` | T (not specified) | More iterations may lead to better solutions but increase computation time. |

## Complexity

- **Time:** Not stated.
- **Space:** Not stated.
- **In practice:** The algorithm's performance may vary based on the size of the service repository and the complexity of the user request.

## Implementation

```python
def wgo_optimization(user_request: dict) -> dict:
    subtasks = decompose_request(user_request)
    candidate_services = construct_css(subtasks)
    coded_services = apply_integer_coding(candidate_services)
    global_combinations = global_search(coded_services)
    refined_combinations = local_search(global_combinations)
    optimal_composition = evaluate_combinations(refined_combinations, user_request['QoS_preferences'])
    return optimal_composition
```

## Common Mistakes

- Failing to properly define QoS preferences, leading to suboptimal service compositions.
- Overlooking the impact of cosine similarity threshold on service grouping.
- Not adjusting parameters like γ and max_iterations based on the specific problem context.

## Use When

- You need to optimize service composition in a cloud manufacturing environment with uncertain service states.
- You have a large repository of services with varying QoS attributes and need to group similar services.
- You require a flexible optimization algorithm that can adapt to dynamic service conditions.

## Avoid When

- The service repository is small and stable, where simpler methods may suffice.
- Real-time processing is critical and cannot accommodate the algorithm's computational overhead.
- You need guaranteed optimal solutions rather than near-optimal solutions.

## Tradeoffs

**Strengths:**

- Effectively handles large and uncertain service repositories.
- Utilizes a dual-stage search process for improved optimization.
- Adapts to varying QoS attributes, enhancing service composition.

**Weaknesses:**

- May not perform well with small, stable service repositories.
- Computational overhead can be significant in real-time applications.
- Does not guarantee optimal solutions, only near-optimal ones.

**Compared To:**

- **vs Traditional QoS-based service composition methods:** WGO is more flexible and can handle uncertainty better, while traditional methods may be simpler and faster for stable environments.

## Connects To

- Quality of Service (QoS) optimization techniques
- Cloud service composition methods
- Metaheuristic optimization algorithms
- Integer programming approaches

## Evidence (Papers)

- **WGO: a similarly encoded whale-goshawk optimization algorithm for uncertain cloud manufacturing service composition** - [DOI](https://doi.org/10.1007/s43684-025-00089-x)
