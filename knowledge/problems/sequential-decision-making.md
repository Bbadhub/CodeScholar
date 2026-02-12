# Problem: Sequential Decision-Making

Sequential decision-making involves making a series of decisions over time, where each decision can affect future outcomes. This type of problem is common in areas like online advertising, clinical trials, and adaptive learning systems.

## You Have This Problem If

- You are faced with a series of choices that depend on previous outcomes.
- You need to optimize a process over time rather than in a single step.
- You have limited resources and need to make decisions that minimize regret.
- You have access to causal information that can guide your decisions.
- You are conducting experiments that require simultaneous decision-making.

## Start Here

**Start with CoBA if you have causal information and need to minimize regret while conducting multiple experiments within a budget.**

## Decision Matrix

| Technique | Speed | Memory | Accuracy | Ease | Best When |
|-----------|-------|--------|----------|------|-----------|
| **CoBA** | medium | medium | high | medium | You have causal side information and need to optimize decisions across multiple experiments. |

## Approaches

### CoBA (Causal contextual Bandits with One-shot data integration)

**Best for:** when you need to conduct multiple experiments simultaneously within a budget and have causal side information.

**Tradeoff:** While CoBA can effectively minimize regret, it may require careful setup and understanding of causal relationships.

*1 papers, up to 1 citations*

## Related Problems

- Multi-armed Bandit Problems
- Reinforcement Learning
- Adaptive Experimentation
- Dynamic Pricing Strategies
