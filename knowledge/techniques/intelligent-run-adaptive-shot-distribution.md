# Intelligent Run-Adaptive Shot Distribution

**This technique adaptively distributes quantum shots across multiple hardware options to enhance reliability and mitigate tampering effects.**

**Category:** quantum_computing  
**Maturity:** emerging

## How It Works

The technique identifies available quantum hardware options and distributes a total number of shots across them. It executes quantum programs on each option and collects results to analyze their probability distributions. Based on the observed performance of the hardware, the shot distribution is adjusted dynamically to favor more reliable hardware, ultimately combining the results to form a final probability distribution of solutions.

## Algorithm

**Input:** Quantum programs and the number of total shots to be executed.

**Output:** Probability distribution of the solution space after combining results from different hardware.

**Steps:**

1. 1. Identify available quantum hardware options.
2. 2. Distribute total shots across these hardware options.
3. 3. Execute quantum programs on each hardware option.
4. 4. Collect results and analyze probability distributions.
5. 5. Adjust shot distribution based on observed hardware performance.
6. 6. Combine results to form a final probability distribution of solutions.

**Core Operation:** `output = combine(results from all hardware options)`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `total_shots` | 1000 | Increasing total shots improves statistical reliability but may increase execution time. |
| `tampering_coefficient` | 0.1 to 0.5 | Adjusting this coefficient influences how aggressively shots are reallocated based on hardware reliability. |

## Complexity

- **Time:** Not explicitly stated.
- **Space:** Not explicitly stated.
- **In practice:** Performance can vary significantly based on the reliability of the hardware options used.

## Implementation

```python
def intelligent_shot_distribution(quantum_program: str, total_shots: int) -> dict:
    hardware_options = identify_hardware()
    shot_distribution = distribute_shots(total_shots, hardware_options)
    results = {}
    for hardware in hardware_options:
        results[hardware] = execute_program(quantum_program, shot_distribution[hardware])
    adjusted_distribution = adjust_distribution(results)
    final_output = combine_results(results)
    return final_output
```

## Common Mistakes

- Failing to accurately assess hardware reliability before distribution.
- Not adjusting the shot distribution based on real-time performance data.
- Overloading a single hardware option with too many shots.

## Use When

- You need to run quantum algorithms on unreliable hardware.
- You are working with critical applications where tampering could lead to significant consequences.
- You want to improve the reliability of quantum computations in a mixed hardware environment.

## Avoid When

- You have access to fully trusted and reliable quantum hardware.
- The application does not require high reliability in quantum results.

## Tradeoffs

**Strengths:**

- Improves reliability of quantum computations.
- Mitigates effects of adversarial tampering.
- Enhances performance in mixed hardware environments.

**Weaknesses:**

- Complexity in dynamically adjusting shot distribution.
- Potential overhead in managing multiple hardware options.
- May not be beneficial with fully reliable hardware.

**Compared To:**

- **vs Single hardware execution:** Use Intelligent Run-Adaptive Shot Distribution when reliability is critical; otherwise, single execution may suffice.

## Connects To

- Quantum error correction
- Quantum hardware benchmarking
- Adversarial machine learning
- Mixed quantum-classical algorithms

## Evidence (Papers)

- **Trustworthy and reliable computing using untrusted and unreliable quantum hardware** - [DOI](https://doi.org/10.3389/fcomp.2024.1431788)
