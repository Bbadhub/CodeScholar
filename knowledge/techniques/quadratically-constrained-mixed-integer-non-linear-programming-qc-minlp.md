# Quadratically Constrained Mixed-Integer Non-Linear Programming (QC-MINLP)

**QC-MINLP optimizes resource allocation and routing in logistics while incorporating quadratic constraints.**

**Category:** optimization_algorithm  
**Maturity:** emerging

## How It Works

QC-MINLP formulates complex distribution problems by defining an objective function that minimizes costs while considering multiple constraints. It incorporates quadratic constraints that reflect real-world logistics challenges, allowing for a more accurate representation of the problem. A suitable solver is then used to find optimal solutions, which can be analyzed and adjusted as necessary.

## Algorithm

**Input:** Data on product demand, transportation costs, vehicle capacities, and distribution center locations.

**Output:** Optimal distribution plan detailing routes and quantities for each sink location.

**Steps:**

1. Define the objective function to minimize transportation costs.
2. Identify constraints related to capacity, demand, and delivery times.
3. Incorporate quadratic constraints that model logistical relationships.
4. Use a suitable solver for QC-MINLP to find optimal solutions.
5. Analyze the results and adjust parameters as necessary.

**Core Operation:** `minimize transportation_cost subject to capacity, demand, and quadratic constraints`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `demand` | varies by retail location | affects the allocation of resources |
| `transportation_cost` | varies by route | influences the overall cost minimization |
| `vehicle_capacity` | e.g., 1000 kg | limits the amount that can be transported |

## Complexity

- **Time:** Not stated
- **Space:** Not stated
- **In practice:** Performance may vary based on the complexity of constraints and the solver used.

## Implementation

```python
def qc_minlp_solver(demand: List[float], transportation_cost: List[float], vehicle_capacity: float) -> Dict[str, Any]:
    # Define objective function
    # Identify constraints
    # Incorporate quadratic constraints
    # Use solver to find optimal solution
    # Return optimal distribution plan
    return optimal_plan
```

## Common Mistakes

- Neglecting to accurately model quadratic constraints.
- Using incomplete or unreliable data for constraints.
- Overcomplicating the model when simpler solutions exist.

## Use When

- You need to optimize distribution logistics for multiple products.
- You are dealing with complex constraints that affect transportation.
- You want to minimize costs while meeting delivery requirements.

## Avoid When

- The problem can be solved with simpler linear programming techniques.
- Real-time dynamic adjustments are required during distribution.
- Data on constraints is incomplete or unreliable.

## Tradeoffs

**Strengths:**

- Handles complex constraints effectively.
- Provides more accurate solutions for logistics problems.
- Can lead to significant cost reductions.

**Weaknesses:**

- May require more computational resources than simpler models.
- Not suitable for real-time adjustments.
- Complexity can lead to longer solution times.

**Compared To:**

- **vs Linear Programming:** Use QC-MINLP for complex constraints; use Linear Programming for simpler problems.

## Connects To

- Linear Programming
- Mixed-Integer Programming
- Non-Linear Programming
- Logistics Optimization Techniques

## Evidence (Papers)

- **A quadratically constrained mixed-integer non-linear programming model for multiple sink distributions** - [DOI](https://doi.org/10.1016/j.heliyon.2024.e38528)
