# DeepWalk

*Also known as: Graph Embedding, Random Walk Embedding*

**DeepWalk is a technique for learning latent representations of nodes in a graph using random walks.**

**Category:** neural_architecture  
**Maturity:** proven

## How It Works

DeepWalk generates random walks from each node in a graph to capture the local structure of the graph. These walks are treated as sentences in a natural language processing context, allowing the use of techniques like Word2Vec to learn embeddings. The resulting embeddings can then be used for various tasks, such as node classification or link prediction.

## Algorithm

**Input:** Graph represented as an adjacency list or matrix.

**Output:** Node embeddings in a vector space.

**Steps:**

1. 1. For each node in the graph, perform a fixed number of random walks.
2. 2. Treat each random walk as a sequence of nodes (like a sentence).
3. 3. Use a skip-gram model to learn embeddings from these sequences.
4. 4. Optimize the embeddings to minimize the loss function based on the context of nodes.
5. 5. Output the learned node embeddings.

**Core Operation:** `output = argmin(sum(log(P(context|node))))`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `embedding_dimension` | 64 | Higher dimensions can capture more complex relationships but may lead to overfitting. |
| `walk_length` | 10 | Longer walks capture more context but increase computational cost. |
| `num_walks` | 10 | More walks per node improve representation but also increase runtime. |

## Complexity

- **Time:** O(n * num_walks * walk_length)
- **Space:** O(n * embedding_dimension)
- **In practice:** Performance can vary significantly based on graph size and structure.

## Implementation

```python
def deepwalk(graph: Dict[int, List[int]], embedding_dim: int) -> Dict[int, List[float]]:
    # Initialize embeddings
    embeddings = initialize_embeddings(graph, embedding_dim)
    for node in graph:
        walks = generate_random_walks(node, graph)
        for walk in walks:
            update_embeddings(embeddings, walk)
    return embeddings
```

## Common Mistakes

- Not normalizing the graph before applying DeepWalk.
- Choosing inappropriate parameters for the random walks.
- Ignoring the impact of node degree on embedding quality.

## Use When

- Designing educational tools that require efficient information retrieval.
- Creating user interfaces for knowledge-based applications.
- Analyzing user behavior in navigation-heavy applications.

## Avoid When

- The application does not involve knowledge networks.
- Real-time navigation is not a priority.

## Tradeoffs

**Strengths:**

- Captures local and global structure of the graph.
- Scalable to large graphs.
- Flexible for various downstream tasks.

**Weaknesses:**

- Sensitive to parameter choices.
- Random walks can miss important structural information.
- May require significant computational resources for large graphs.

**Compared To:**

- **vs Node2Vec:** Use Node2Vec when you need more control over the exploration of the graph structure.

## Connects To

- Node2Vec
- Graph Convolutional Networks
- Word2Vec
- Random Walks

## Evidence (Papers)

- **Milgram’s experiment in the knowledge space: individual navigation strategies** [1 citations] - [DOI](https://doi.org/10.1140/epjds/s13688-025-00558-6)
