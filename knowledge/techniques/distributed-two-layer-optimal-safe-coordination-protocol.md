# Distributed Two-Layer Optimal Safe Coordination Protocol

**A protocol for coordinating swarms of hypersonic flight vehicles while ensuring safety and optimality.**

**Category:** control_system  
**Maturity:** emerging

## How It Works

This technique employs a two-layer protocol consisting of a decision layer and a control layer. The decision layer utilizes a distributed projection optimization algorithm to keep outputs within a predefined safety set. Meanwhile, the control layer implements a safety controller that uses feedback linearization to adjust control inputs. This structure allows for optimal output convergence while adhering to safety constraints throughout the operation.

## Algorithm

**Input:** Initial states of HFVs including velocity, altitude, and other dynamic parameters.

**Output:** Converged outputs of HFVs that are optimal and within the safety constraints.

**Steps:**

1. Initialize the safety set and control parameters.
2. For each hypersonic flight vehicle (HFV), compute intermediate and decision variables based on the current state.
3. Update the control input using the designed distributed control protocol.
4. Project the control input onto the safety set to ensure compliance.
5. Iterate until convergence to the optimal output.

**Core Operation:** `output = project(control_input, safety_set)`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `β` | 0.1 | Affects the sensitivity of the control adjustments. |
| `T` | 1 | Determines the time horizon for control updates. |
| `k1` | 6 | Influences the strength of the feedback control. |
| `k2` | 8 | Affects the convergence rate of the control inputs. |
| `c0` | 0.2 | Sets the initial condition for the control protocol. |
| `α` | 0.1 | Modulates the feedback linearization. |
| `λ0` | 0.8 | Determines the weight of safety in the optimization. |

## Complexity

- **Time:** Not stated
- **Space:** Not stated
- **In practice:** Performance may vary based on the complexity of the HFV dynamics and safety constraints.

## Implementation

```python
def distributed_safe_coordination(initial_states: List[State]) -> List[Output]:
    safety_set = initialize_safety_set()
    control_params = initialize_control_parameters()
    while not converged:
        for hfv in initial_states:
            intermediate_vars = compute_intermediate_variables(hfv)
            decision_vars = compute_decision_variables(intermediate_vars)
            control_input = update_control_input(decision_vars, control_params)
            control_input = project_onto_safety_set(control_input, safety_set)
    return converged_outputs
```

## Common Mistakes

- Neglecting to properly define the safety set, leading to unsafe outputs.
- Failing to iterate sufficiently, resulting in non-converged outputs.
- Overlooking the impact of parameter tuning on system performance.

## Use When

- Designing control systems for swarms of hypersonic vehicles.
- Ensuring safety in high-speed aerospace applications.
- Implementing distributed algorithms in dynamic environments.

## Avoid When

- The system dynamics are not well understood or modeled.
- Safety constraints are not a priority.
- The environment is static and does not require adaptive control.

## Tradeoffs

**Strengths:**

- Ensures safety compliance while optimizing outputs.
- Adaptable to dynamic environments with distributed control.
- Effective for high-speed aerospace applications.

**Weaknesses:**

- Complexity in modeling system dynamics accurately.
- Potentially high computational overhead in real-time applications.
- Requires thorough understanding of safety constraints.

**Compared To:**

- **vs Traditional Control Methods:** Use this protocol when safety is a priority and dynamic environments are involved.

## Connects To

- Distributed Control Systems
- Safety-Critical Systems
- Feedback Linearization
- Projection Optimization Algorithms

## Evidence (Papers)

- **Distributed integrated design for optimity and safety of hypersonic flight vehicle swarm** - [DOI](https://doi.org/10.1007/s43684-025-00115-y)
