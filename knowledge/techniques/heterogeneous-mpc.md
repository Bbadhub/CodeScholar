# Heterogeneous MPC

**Heterogeneous MPC efficiently solves graph problems using a combination of a powerful machine and smaller machines in a distributed environment.**

**Category:** optimization_algorithm  
**Maturity:** emerging

## How It Works

Heterogeneous MPC leverages a single large machine with higher memory capacity to compute partial solutions on a sparse subgraph of the input graph. This large machine processes the data and encodes the results as labels for the vertices. These labels are then sent to smaller machines, which use them to identify edges that contribute to the final solution. The selected edges are combined to produce the desired output, such as a minimum spanning tree or maximal matching.

## Algorithm

**Input:** A weighted or unweighted undirected graph G = (V, E) with edges distributed across small machines.

**Output:** The minimum spanning tree, O(k)-spanner, or maximal matching of the graph.

**Steps:**

1. 1. Select a sparse subgraph G' from the input graph G.
2. 2. Send G' to the large machine to compute a partial solution.
3. 3. The large machine encodes the partial solution as labels for the vertices.
4. 4. Send the labels to the small machines.
5. 5. Each small machine identifies edges that are part of the true solution using the labels.
6. 6. Combine the selected edges to form the final solution.

**Core Operation:** `output = combine(selected_edges)`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `memory_large_machine` | O(n polylog n) | Increases the capacity for processing larger subgraphs. |
| `memory_small_machine` | O(n^γ polylog n) for γ ∈ (0, 1) | Affects the ability of small machines to handle data. |
| `number_of_small_machines` | K = m/n^γ | Determines the distribution of workload across smaller machines. |

## Complexity

- **Time:** O(log log(m/n)) for MST, O(log(m/n) log log(m/n)) for maximal matching
- **Space:** O(n polylog n)
- **In practice:** The technique is efficient for large graphs where communication overhead is a concern.

## Implementation

```python
def heterogeneous_mpc(graph: Graph, large_machine: Machine, small_machines: List[Machine]) -> Solution:
    sparse_subgraph = select_sparse_subgraph(graph)
    partial_solution = large_machine.compute_partial_solution(sparse_subgraph)
    labels = encode_partial_solution(partial_solution)
    for machine in small_machines:
        machine.identify_edges(labels)
    final_solution = combine_selected_edges(small_machines)
    return final_solution
```

## Common Mistakes

- Assuming all machines have similar capabilities, leading to inefficient resource use.
- Neglecting the communication overhead when designing the system.
- Not properly selecting the sparse subgraph, which can affect the solution quality.

## Use When

- You need to solve graph problems in a distributed environment with varying machine capabilities.
- You want to minimize communication overhead in a parallel computing setup.
- You have access to a single powerful machine among weaker nodes.

## Avoid When

- The problem size is small enough to be handled by a single machine.
- The communication latency between machines is negligible.
- All machines have similar memory and processing capabilities.

## Tradeoffs

**Strengths:**

- Reduces communication overhead by leveraging a powerful machine.
- Efficiently handles large graphs with distributed data.
- Achieves faster computation times compared to traditional methods.

**Weaknesses:**

- Requires careful management of machine capabilities.
- May not be suitable for small-scale problems.
- Complexity in implementation due to distributed nature.

**Compared To:**

- **vs Traditional MPC:** Use Heterogeneous MPC when machine capabilities vary significantly.

## Connects To

- Distributed Computing
- Graph Algorithms
- Parallel Processing
- Sparse Graph Techniques

## Evidence (Papers)

- **Massively parallel computation in a heterogeneous regime** - [DOI](https://doi.org/10.1007/s00446-025-00479-7)
