# Three-Stage Heuristic (3SH)

**3SH optimizes the arrangement of containers in maritime terminals to minimize relocations.**

**Category:** optimization_algorithm  
**Maturity:** proven (widely used in production)

## How It Works

The Three-Stage Heuristic operates in three distinct stages. First, it assigns blocking containers to stacks without causing additional relocations. Next, it assigns remaining containers that may cause relocations using an enhanced Virtual Relocation Index. Finally, it adjusts the assignments to further optimize the arrangement, ensuring minimal relocations overall.

## Algorithm

**Input:** Data on container stacks, their heights, and the priority of containers for retrieval.

**Output:** An optimized arrangement of containers in stacks that minimizes the number of relocations.

**Steps:**

1. 1. Identify blocking containers above the target container.
2. 2. In the first stage, assign containers to stacks without causing additional relocations.
3. 3. In the second stage, assign remaining containers using an enhanced Virtual Relocation Index (VRI).
4. 4. In the last stage, adjust assignments to optimize the relocation of blocking containers.

**Core Operation:** `output = optimized arrangement of containers minimizing relocations`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `S` | number of stacks | More stacks can lead to better optimization. |
| `H` | maximum height limit | A higher limit allows for more containers but may complicate arrangements. |
| `N` | number of containers | Increasing the number of containers can affect the complexity of the optimization. |

## Complexity

- **Time:** Not stated
- **Space:** Not stated
- **In practice:** Performance may vary based on the number of containers and stacks.

## Implementation

```python
def three_stage_heuristic(container_data: List[Container]) -> List[Container]:
    # Step 1: Identify blocking containers
    blocking_containers = identify_blocking_containers(container_data)
    # Step 2: Assign containers without relocations
    assign_without_relocations(blocking_containers)
    # Step 3: Assign remaining containers using VRI
    remaining_containers = get_remaining_containers(container_data)
    assign_with_vri(remaining_containers)
    # Step 4: Adjust assignments
    optimized_arrangement = adjust_assignments()
    return optimized_arrangement
```

## Common Mistakes

- Failing to accurately identify blocking containers.
- Neglecting to consider the impact of stack height on assignments.
- Overcomplicating the VRI calculations, leading to inefficiencies.

## Use When

- Optimizing container retrieval in maritime terminals with high container volumes.
- Reducing operational costs associated with container relocations.
- Improving efficiency in logistics and supply chain management.

## Avoid When

- Dealing with small-scale instances where traditional heuristics perform adequately.
- When real-time decision-making is required and computational time is critical.

## Tradeoffs

**Strengths:**

- Effectively minimizes the number of relocations.
- Improves overall efficiency in container management.
- Can be adapted to various terminal configurations.

**Weaknesses:**

- Not suitable for small-scale operations.
- May require significant computational resources for large datasets.
- Real-time applications may be challenging due to processing time.

**Compared To:**

- **vs Min-Max heuristic:** 3SH is preferred for larger datasets where relocation costs are high.
- **vs PR4 heuristic:** 3SH generally outperforms PR4 in terms of relocation minimization.

## Connects To

- Container stacking algorithms
- Logistics optimization techniques
- Supply chain management strategies
- Heuristic optimization methods

## Evidence (Papers)

- **A Three-Stage Heuristic For Optimizing Container Relocations In Maritime Container Terminals** - [DOI](https://doi.org/10.3846/transport.2024.21668)
