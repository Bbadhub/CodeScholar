# Friendship Index

**The Friendship Index measures the ratio of the average degree of an individual's friends to their own degree over time.**

**Category:** statistical_method  
**Maturity:** emerging

## How It Works

The Friendship Index is calculated using smartphone communication data to analyze social interactions. It constructs undirected networks based on daily interactions, allowing for the computation of each individual's degree and the average degree of their friends. By tracking these metrics over time, the Friendship Index reveals how perceptions of social norms evolve within a network.

## Algorithm

**Input:** Smartphone communication records detailing interactions among individuals.

**Output:** Dynamic friendship index values for each individual over time.

**Steps:**

1. 1. Collect smartphone communication data over a specified period.
2. 2. Construct undirected networks daily based on interactions.
3. 3. Calculate the degree of each node (individual) in the network.
4. 4. Compute the average degree of each individual's friends.
5. 5. Calculate the friendship index for each individual at each time point.
6. 6. Analyze the temporal changes in the friendship index.

**Core Operation:** `friendship_index = average_degree_of_friends / own_degree`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `time_period` | 119 days | Longer periods may reveal more trends. |
| `number_of_participants` | 692 | More participants can lead to a more robust analysis. |
| `communication_records` | over 60 million | Higher volume of records improves accuracy. |

## Complexity

- **Time:** Not stated
- **Space:** Not stated
- **In practice:** The complexity may vary based on the size of the network and the duration of data collection.

## Implementation

```python
def calculate_friendship_index(data: List[Interaction]) -> Dict[str, float]:
    # Step 1: Collect data
    # Step 2: Construct daily networks
    networks = construct_networks(data)
    indices = {}
    for day, network in networks.items():
        for individual in network:
            degree = calculate_degree(individual)
            avg_friend_degree = calculate_avg_friend_degree(individual, network)
            indices[individual] = avg_friend_degree / degree
    return indices
```

## Common Mistakes

- Neglecting to account for the dynamic nature of the network.
- Using static measures when the network is evolving.
- Failing to validate the data quality before analysis.

## Use When

- Designing social networks that aim to mitigate distorted perceptions of social norms.
- Analyzing communication patterns in educational or workplace settings.
- Studying the influence of highly connected individuals on group behavior.

## Avoid When

- The network is static and does not evolve over time.
- Data on individual interactions is not available.
- The focus is solely on individual behaviors without considering network effects.

## Tradeoffs

**Strengths:**

- Provides a dynamic view of social interactions.
- Helps in understanding the evolution of social norms.
- Can reveal insights into group behavior influenced by connected individuals.

**Weaknesses:**

- Requires extensive data collection over time.
- May not be applicable to static networks.
- Data privacy concerns with smartphone communication records.

**Compared To:**

- **vs Static Friendship Index:** Use the dynamic index for evolving networks; static for fixed networks.

## Connects To

- Social Network Analysis
- Dynamic Graph Theory
- Communication Patterns in Networks
- Influence of Social Norms

## Evidence (Papers)

- **Temporal dynamics of the friendship paradox in a smartphone communication network** [1 citations] - [DOI](https://doi.org/10.1007/s41109-025-00710-1)
