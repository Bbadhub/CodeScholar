# CoBA (Causal contextual Bandits with One-shot data integration)

**CoBA is a method for optimizing decision-making in contextual bandit settings using one-shot data integration.**

**Category:** optimization_algorithm  
**Maturity:** emerging

## How It Works

CoBA maintains beliefs about conditional probability distributions (CPDs) and selects samples for various context-action pairs while adhering to budget constraints. It integrates the acquired data to update its policy, aiming to minimize an entropy-like measure. The method is particularly useful when causal side information is available, allowing for more informed decision-making in sequential contexts.

## Algorithm

**Input:** Logged offline data consisting of context-action-reward tuples.

**Output:** A learned policy mapping contexts to actions.

**Steps:**

1. Initialize beliefs about CPDs using logged offline data.
2. Specify the number of samples required for each context-action pair.
3. Calculate costs associated with acquiring those samples.
4. Ensure total cost does not exceed the budget.
5. Integrate acquired samples to update beliefs.
6. Learn a policy based on updated beliefs.
7. Evaluate the learned policy and measure regret.

**Core Operation:** `Regret = O(s(MC/mB - ε) ln(MXMC/δ))`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `budget` | B (total cost for acquiring samples) | Limits the number of samples that can be acquired. |
| `cost function` | β(x, cA, Nx,cA) | Determines the cost associated with acquiring samples. |
| `number of samples` | Nx,cA for each (x, cA) | Specifies how many samples to acquire for each context-action pair. |

## Complexity

- **Time:** Not stated.
- **Space:** Not stated.
- **In practice:** Performance may vary based on the complexity of the context-action space and the budget constraints.

## Implementation

```python
def coBA(logged_data: List[Tuple[Context, Action, Reward]], budget: float) -> Policy:
    beliefs = initialize_beliefs(logged_data)
    while budget > 0:
        samples = specify_samples(beliefs)
        costs = calculate_costs(samples)
        if sum(costs) <= budget:
            update_beliefs(samples)
            budget -= sum(costs)
    policy = learn_policy(beliefs)
    return policy
```

## Common Mistakes

- Failing to properly initialize beliefs about CPDs.
- Not accurately calculating the costs associated with sample acquisition.
- Exceeding the budget without realizing it.
- Neglecting to evaluate the learned policy effectively.

## Use When

- You need to conduct multiple experiments simultaneously within a budget.
- You have causal side information that can inform decision-making.
- You want to minimize regret in a sequential decision-making context.

## Avoid When

- The environment does not allow for one-shot data acquisition.
- You lack causal side information.
- The cost of acquiring samples is prohibitively high.

## Tradeoffs

**Strengths:**

- Allows for simultaneous experimentation under budget constraints.
- Utilizes causal information to enhance decision-making.
- Minimizes regret in sequential contexts.

**Weaknesses:**

- Requires careful budget management.
- Dependent on the availability of causal side information.
- May not perform well in environments with high sample acquisition costs.

**Compared To:**

- **vs Standard contextual bandit algorithms:** CoBA is preferable when causal information is available and budget constraints are critical.

## Connects To

- Contextual Bandits
- Causal Inference
- Multi-Armed Bandits
- Reinforcement Learning

## Evidence (Papers)

- **Causal contextual bandits with one-shot data integration** [1 citations] - [DOI](https://doi.org/10.3389/frai.2024.1346700)
