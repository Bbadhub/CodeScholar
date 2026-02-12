# Application of Proximal Policy Optimization for Resource Orchestration in Serverless Edge Computing

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3390/computers13090224` |
| Full Paper | [https://doi.org/10.3390/computers13090224](https://doi.org/10.3390/computers13090224) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/be0431e7c285bc8e58ff8f397ffe002d7cc068db](https://www.semanticscholar.org/paper/be0431e7c285bc8e58ff8f397ffe002d7cc068db) |
| Source | [https://journalclub.io/episodes/application-of-proximal-policy-optimization-for-resource-orchestration-in-serverless-edge-computing](https://journalclub.io/episodes/application-of-proximal-policy-optimization-for-resource-orchestration-in-serverless-edge-computing) |
| Source | [https://www.semanticscholar.org/paper/be0431e7c285bc8e58ff8f397ffe002d7cc068db](https://www.semanticscholar.org/paper/be0431e7c285bc8e58ff8f397ffe002d7cc068db) |
| Year | 2026 |
| Citations | 2 |
| Authors | M. Femminella, G. Reali |
| Paper ID | `6030b77d-c81b-4696-a398-d60f568bd2bc` |

## Classification

- **Problem Type:** resource orchestration in serverless computing
- **Domain:** Cloud Computing
- **Sub-domain:** Serverless Computing, Edge Computing
- **Technique:** Proximal Policy Optimization (PPO)
- **Technique Category:** reinforcement_learning
- **Type:** novel

## Summary

The paper presents a reinforcement learning approach using Proximal Policy Optimization (PPO) to optimize resource orchestration in serverless edge computing environments, specifically targeting the cold start problem. Engineers should care because this method can enhance the performance and efficiency of serverless applications by dynamically configuring autoscaling parameters based on real-world traffic patterns.

## Key Contribution

**Introduction of a PPO-based control system for optimizing horizontal autoscaling in serverless edge computing environments.**

## Problem

The cold start problem in serverless computing can lead to increased latency and service request losses, hindering developer adoption.

## Method

**Approach:** The method leverages PPO to dynamically configure the Kubernetes Horizontal Pod Autoscaler (HPA) based on real traffic data. It uses a state space model that incorporates resource consumption, performance metrics, and time of day to optimize autoscaling decisions.

**Algorithm:**

1. 1. Collect real-world serverless traffic traces.
2. 2. Define the state space including resource consumption and performance metrics.
3. 3. Implement the PPO algorithm to learn optimal autoscaling thresholds.
4. 4. Use the learned policy to adjust the HPA configuration dynamically.
5. 5. Monitor performance metrics and adjust the policy as needed.

**Input:** Real-world serverless traffic traces including metrics such as CPU and memory usage.

**Output:** Dynamically configured autoscaling parameters for the Kubernetes HPA.

**Key Parameters:**

- `learning_rate: 0.001`
- `discount_factor: 0.99`
- `minimum_replicas: 1`
- `maximum_replicas: 10`
- `CPU_threshold: configurable`

**Complexity:** Not stated

## Benchmarks

**Tested on:** Real-world serverless traffic traces

**Results:**

- average latency: within SLA
- CPU usage: optimized
- memory usage: optimized
- loss percentage: minimized

**Compared against:** Default Kubernetes HPA configuration

**Improvement:** Achieved service time within SLA while limiting resource consumption and service loss.

## Implementation Guide

**Data Structures:** State space model, Traffic trace repository, Metrics storage

**Dependencies:** Kubernetes, OpenFaaS, PPO libraries (e.g., TensorFlow, PyTorch)

**Core Operation:**

```python
while True: state = get_current_state(); action = PPO_model.predict(state); apply_action(action);
```

**Watch Out For:**

- Ensure accurate state representation to avoid poor performance.
- Monitor the impact of autoscaling on overall system performance.
- Be cautious of the trade-off between exploration and exploitation in PPO.

## Use This When

- You need to optimize resource usage in a serverless application.
- You are facing latency issues due to cold starts in serverless functions.
- You want to ensure SLA compliance in a serverless edge computing environment.

## Don't Use When

- The application has very low traffic and does not require dynamic scaling.
- You are using a serverless platform that does not support Kubernetes.
- The overhead of implementing reinforcement learning is not justified for the use case.

## Key Concepts

serverless computing, edge computing, reinforcement learning, horizontal autoscaling, Kubernetes, Proximal Policy Optimization

## Connects To

- Kubernetes Horizontal Pod Autoscaler
- OpenFaaS
- Q-learning
- Deep Q-Networks
- Multi-agent reinforcement learning

## Prerequisites

- Basic understanding of reinforcement learning concepts.
- Familiarity with Kubernetes and serverless architectures.
- Knowledge of performance metrics in cloud computing.

## Limitations

- Performance heavily depends on the quality of traffic data.
- Requires tuning of multiple hyperparameters for optimal performance.
- May not perform well in highly variable traffic scenarios.

## Open Questions

- How can the approach be generalized to other serverless platforms?
- What are the long-term impacts of using reinforcement learning for autoscaling?

## Abstract

Serverless is great. In a number of ways it's truly a transformative technology. And it's spreading: every year more hosts jump into this space to offer their own Function as a Service (FaaS) platforms: from AWS, GCP and Azure, to the edge offerings available on Cloudflare, Fastly and Akamai, to the open-source options like OpenFaaS. But as with anything, serverless is not without its drawbacks. From the "uncapped costs" problem, to the "how do I run this locally?" problem, there are obviously a few areas where the developer-experience could be improved. And that's to be expected given how nascent the technology still is. But there is one issue that's a deal-breaker for many devs. An issue so off-putting that it actually prevents them from adopting serverless at all. That issue is the "cold start" problem.
