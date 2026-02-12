# FIESTA

**FIESTA evaluates hardware circuits under random fault models to analyze their resilience against fault injection attacks.**

**Category:** fault_injection_analysis  
**Maturity:** emerging

## How It Works

FIESTA employs a non-exhaustive approach to assess the vulnerability of hardware circuits by simulating random faults. It generates a subset of gates to be faulted based on a defined probability distribution and evaluates the circuit's response to these faults. The results yield success probability bounds, indicating the effectiveness of potential fault injection attacks on the design.

## Algorithm

**Input:** A circuit design represented in a suitable format (e.g., GDSII file) and a defined probability distribution for faults.

**Output:** Success probability bounds indicating the effectiveness of fault injection attacks on the circuit.

**Steps:**

1. 1. Define the circuit under test and its parameters.
2. 2. Specify the fault model and the probability distribution of faults.
3. 3. Generate a randomized subset of gates to be faulted based on the defined model.
4. 4. Simulate the circuit with the injected faults.
5. 5. Analyze the output to determine if the faults were effective.
6. 6. Report the success probability bounds based on the analysis.

**Core Operation:** `success_probability_bounds = (μℓ, μu)`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `error_probability` | α > 0 | Affects the likelihood of faults being injected. |
| `fault_probability_distribution` | user-defined | Determines how faults are distributed across the circuit. |

## Complexity

- **Time:** Not stated
- **Space:** Not stated
- **In practice:** FIESTA is designed to evaluate larger designs in less time compared to traditional exhaustive methods.

## Implementation

```python
def fiesta_evaluation(circuit: str, fault_model: str, fault_distribution: dict) -> tuple:
    # Step 1: Define the circuit and parameters
    # Step 2: Specify the fault model
    # Step 3: Generate randomized faults
    # Step 4: Simulate circuit with faults
    # Step 5: Analyze output
    # Step 6: Return success probability bounds
    return success_probability_bounds
```

## Common Mistakes

- Neglecting to define an appropriate fault model for the circuit.
- Using an inadequate probability distribution that does not reflect real-world scenarios.
- Failing to analyze the output correctly to determine fault effectiveness.

## Use When

- Evaluating the security of large cryptographic hardware designs against fault injection attacks.
- Needing a framework that supports various adversary models for customized resistance analysis.
- Conducting pre-fabrication security assessments of hardware implementations.

## Avoid When

- Working with very small circuits where exhaustive verification is feasible.
- When precise fault injection techniques are required that FIESTA does not support.
- If the application does not involve cryptographic hardware.

## Tradeoffs

**Strengths:**

- Allows for the evaluation of larger designs without exhaustive simulation.
- Supports various adversary models for tailored security assessments.
- Provides probabilistic bounds on fault injection success.

**Weaknesses:**

- Not suitable for very small circuits where exhaustive methods are feasible.
- May not support precise fault injection techniques.
- Limited to applications involving cryptographic hardware.

**Compared To:**

- **vs VERICA+:** Use FIESTA for larger designs; VERICA+ may be better for smaller circuits.
- **vs IronMask+:** FIESTA is faster for larger designs, while IronMask+ may provide more detailed analysis.

## Connects To

- Fault Injection Testing
- Hardware Security Analysis
- Cryptographic Hardware Evaluation
- Adversarial Machine Learning

## Evidence (Papers)

- **Fault Injection Evaluation with Statistical Analysis** - [DOI](https://doi.org/10.46586/tches.v2025.i4.215-253)
