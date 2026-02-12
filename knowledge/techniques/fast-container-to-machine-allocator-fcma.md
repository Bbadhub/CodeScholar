# Fast Container to Machine Allocator (FCMA)

**FCMA optimizes the allocation of containers and virtual machines based on workload predictions to minimize costs.**

**Category:** optimization_algorithm  
**Maturity:** emerging

## How It Works

FCMA calculates the optimal allocation of containers and virtual machines (VMs) by analyzing workload predictions. It reduces the problem size and combines Integer Linear Programming (ILP) methods with heuristics to achieve near-optimal solutions quickly. The algorithm considers available instance classes and their resources to allocate containers efficiently while minimizing costs.

## Algorithm

**Input:** Workload data (requests per second), instance class specifications (CPU cores, memory, price), container class requirements.

**Output:** Number of VMs and containers allocated for each application, along with their respective resources.

**Steps:**

1. 1. Define the workload for each application in requests per second.
2. 2. Identify available instance classes and their resources (CPU, memory, price).
3. 3. Formulate a partial ILP problem to determine initial allocations.
4. 4. Aggregate nodes based on resource requirements.
5. 5. Allocate containers to nodes based on performance and cost.
6. 6. Aggregate containers to optimize resource usage.

**Core Operation:** `output = number of VMs and containers allocated for each application based on workload and resource requirements`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `workload` | requests per second (rps) | Higher workload increases resource allocation. |
| `instance_classes` | number of available instance classes | More classes can lead to better optimization. |
| `containers` | number of container classes | More container classes may complicate allocation. |
| `cores` | CPU cores required per container | More cores per container increases resource demand. |
| `memory` | memory required per container (GB) | Higher memory requirements may limit VM options. |
| `price` | cost per hour of instance classes ($/h) | Higher prices may lead to fewer allocations. |

## Complexity

- **Time:** Not stated.
- **Space:** Not stated.
- **In practice:** FCMA shows an average solving time reduction of two orders of magnitude compared to traditional ILP methods.

## Implementation

```python
def fcma_allocate(workload: float, instance_classes: List[InstanceClass], containers: List[ContainerClass]) -> Allocation:
    # Step 1: Define workload
    # Step 2: Identify instance classes
    # Step 3: Formulate ILP problem
    # Step 4: Aggregate nodes
    # Step 5: Allocate containers
    # Step 6: Optimize resource usage
    return allocation
```

## Common Mistakes

- Ignoring the variability in workload predictions.
- Overcomplicating the model with too many instance or container classes.
- Failing to consider cost implications of resource allocation.

## Use When

- You need to optimize resource allocation in a cloud environment with variable workloads.
- Real-time autoscaling decisions are critical for maintaining service levels.
- You want to minimize costs associated with deploying containers and VMs.

## Avoid When

- The workload is predictable and does not require dynamic scaling.
- You have a very small number of containers and VMs, making the problem trivial.
- You require absolute optimality over speed in resource allocation.

## Tradeoffs

**Strengths:**

- Significantly faster than traditional ILP methods.
- Cost-effective solutions comparable to ILP.
- Scalable to various workloads and resource configurations.

**Weaknesses:**

- May not achieve absolute optimality.
- Performance can degrade with highly complex workloads.
- Requires accurate workload predictions for best results.

**Compared To:**

- **vs Integer Linear Programming (ILP):** Use FCMA for speed and cost-effectiveness; use ILP for absolute optimality.

## Connects To

- Dynamic resource allocation techniques
- Container orchestration frameworks
- Cloud cost optimization strategies
- Autoscaling algorithms

## Evidence (Papers)

- **Fast autoscaling algorithm for cost optimization of container clusters** - [DOI](https://doi.org/10.1186/s13677-025-00748-7)
