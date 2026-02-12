# Causal Graph Extraction

**This technique constructs causal graphs from communication logs to analyze subsystem interactions and identify root causes of failures.**

**Category:** statistical_method  
**Maturity:** emerging

## How It Works

Causal Graph Extraction analyzes communication logs from systems, such as air traffic control, to identify state transitions and events. It constructs a causal graph that represents the relationships between different components and their failure modes. The graph is refined using statistical methods to establish causal relationships, allowing for effective root cause analysis of system behavior.

## Algorithm

**Input:** Machine-generated communication logs from air traffic control systems.

**Output:** Causal graphs representing the relationships and dependencies between subsystems.

**Steps:**

1. 1. Collect communication logs from the air traffic control system.
2. 2. Parse the logs to extract relevant state transition data.
3. 3. Identify events and their timestamps for each subsystem.
4. 4. Construct a preliminary causal graph based on identified events.
5. 5. Refine the causal graph using statistical methods to establish causal relationships.
6. 6. Validate the causal graph against known failure scenarios.

**Core Operation:** `Causal Graph = f(Events, State Transitions)`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `log_window_size` | 1000 | Larger sizes may capture more context but increase processing time. |
| `event_threshold` | 5 | Higher thresholds may filter out noise but risk missing important events. |

## Complexity

- **Time:** Not stated
- **Space:** Not stated
- **In practice:** Performance may vary based on the size and quality of the logs.

## Implementation

```python
def extract_causal_graph(logs: List[str]) -> CausalGraph:
    # Step 1: Parse logs
    events = parse_logs(logs)
    # Step 2: Construct preliminary graph
    graph = construct_graph(events)
    # Step 3: Refine graph
    refined_graph = refine_graph(graph)
    # Step 4: Validate graph
    validate_graph(refined_graph)
    return refined_graph
```

## Common Mistakes

- Failing to account for noise in the logs, leading to inaccurate graphs.
- Overlooking the importance of validating the causal graph against known scenarios.
- Not refining the graph adequately, resulting in misleading causal relationships.

## Use When

- You need to diagnose failures in complex distributed systems.
- You want to improve the reliability of air traffic control systems.
- You require explainable analysis of system behavior.

## Avoid When

- The logs are incomplete or corrupted.
- Real-time analysis is required without historical data.
- The system is not safety-critical.

## Tradeoffs

**Strengths:**

- Provides a clear visual representation of subsystem interactions.
- Facilitates explainable root cause analysis.
- Improves accuracy of failure diagnosis compared to traditional methods.

**Weaknesses:**

- Dependent on the quality and completeness of the input logs.
- May require significant preprocessing of data.
- Not suitable for real-time applications.

**Compared To:**

- **vs Traditional log analysis methods:** Use Causal Graph Extraction for better accuracy and explainability.
- **vs Manual root cause analysis:** Causal Graph Extraction automates and enhances the analysis process.

## Connects To

- Statistical Inference
- Data Mining Techniques
- Fault Tree Analysis
- Bayesian Networks

## Evidence (Papers)

- **Uncovering causal graphs in air traffic control communication logs for explainable root cause analysis** - [DOI](https://doi.org/10.1080/00051144.2025.2518794)
