# Multi-Armed Bandit

*Also known as: Bandit Algorithm, Stochastic Bandit*

**A strategy for resource allocation that balances exploration and exploitation based on performance feedback.**

**Category:** optimization_algorithm  
**Maturity:** proven

## How It Works

The Multi-Armed Bandit technique dynamically allocates resources by selecting options based on their performance. It uses a balance of exploration, where new configurations are tested, and exploitation, where known effective configurations are utilized. Over time, the algorithm refines its resource allocation strategy to optimize overall system performance.

## Algorithm

**Input:** Resource options and their initial performance metrics.

**Output:** Optimized resource allocation strategy with expected performance improvements.

**Steps:**

1. 1. Initialize resource options and their associated rewards.
2. 2. For each time step, select a resource option based on a balance of exploration and exploitation.
3. 3. Allocate resources accordingly and monitor performance.
4. 4. Update the reward estimates based on the observed performance.
5. 5. Repeat the process to continuously refine resource allocation.

**Core Operation:** `output = select(resource_options) based on exploration_exploitation_balance()`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `exploration_rate` | 0.1 | Higher values increase exploration, potentially improving performance but may reduce short-term gains. |
| `num_iterations` | 1000 | More iterations allow for better performance estimates but increase computation time. |

## Complexity

- **Time:** O(n log n)
- **Space:** O(n)
- **In practice:** Real-world performance may vary based on the number of resource options and the dynamics of the environment.

## Implementation

```python
def multi_armed_bandit(resource_options: List[Resource], num_iterations: int, exploration_rate: float) -> Allocation:
    rewards = initialize_rewards(resource_options)
    for t in range(num_iterations):
        option = select_option(resource_options, rewards, exploration_rate)
        performance = allocate_and_monitor(option)
        update_rewards(rewards, option, performance)
    return optimize_allocation(rewards)
```

## Common Mistakes

- Neglecting to properly balance exploration and exploitation.
- Failing to update reward estimates accurately.
- Overlooking the impact of the exploration rate on performance.

## Use When

- You need to dynamically allocate resources in a computing environment.
- You want to optimize performance based on uncertain outcomes.
- You are working with Near Memory Processing architectures.

## Avoid When

- The resource options are deterministic and known.
- You have a fixed resource allocation without the need for optimization.
- The overhead of exploration is too high compared to potential gains.

## Tradeoffs

**Strengths:**

- Adapts to changing environments and performance metrics.
- Can significantly improve resource utilization.
- Effective in scenarios with uncertain outcomes.

**Weaknesses:**

- May require significant iterations to converge on optimal solutions.
- Exploration can lead to suboptimal performance in the short term.
- Overhead of exploration may not be justified in all contexts.

**Compared To:**

- **vs Static Resource Allocation:** Use Multi-Armed Bandit when performance is uncertain and dynamic; use static when conditions are stable.

## Connects To

- Reinforcement Learning
- Thompson Sampling
- Epsilon-Greedy Algorithm
- Contextual Bandits

## Evidence (Papers)

- **Multi armed bandit based resource allocation in Near Memory Processing architectures** - [DOI](https://doi.org/10.1016/j.memori.2025.100132)
