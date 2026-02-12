# PDGPT

*Also known as: Phase Diagram Generative Pre-trained Transformer*

**PDGPT is a large language model tailored for acquiring phase diagram information in magnesium alloys.**

**Category:** neural_architecture  
**Maturity:** emerging

## How It Works

PDGPT is trained specifically on magnesium alloy phase diagrams by integrating domain-specific knowledge. It employs three main strategies: using unmodified large language models (LLMs) enhanced with prompt-engineering, implementing Retrieval-Augmented Generation (RAG) for information retrieval, and creating new models through Supervised Fine Tuning (SFT). This combination allows the model to provide accurate insights related to magnesium alloys during inference.

## Algorithm

**Input:** Queries related to magnesium alloy phase diagrams (text format).

**Output:** Accurate phase diagram information and insights for magnesium alloys (text format).

**Steps:**

1. 1. Gather a comprehensive dataset on magnesium alloys and phase diagrams.
2. 2. Choose a base LLM architecture.
3. 3. Apply prompt-engineering techniques to enhance the model's responses.
4. 4. Implement RAG to retrieve relevant information during inference.
5. 5. Conduct Supervised Fine Tuning on the model with domain-specific data.
6. 6. Evaluate the model's performance on phase diagram queries.

**Core Operation:** `output = model(query) + RAG(retrieved_info)`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `learning_rate` | 0.001 | A higher learning rate may lead to faster convergence but risks overshooting the optimal solution. |
| `batch_size` | 32 | Larger batch sizes can stabilize training but require more memory. |
| `num_epochs` | 10 | More epochs can improve accuracy but may lead to overfitting. |

## Complexity

- **Time:** O(n * m) where n is the number of queries and m is the model size.
- **Space:** O(m) where m is the model size.
- **In practice:** Real-world performance may vary based on the dataset size and model architecture.

## Implementation

```python
def pdgpt_model(query: str) -> str:
    dataset = load_dataset('magnesium_alloys')
    model = initialize_llm('base_model')
    enhanced_query = apply_prompt_engineering(query)
    retrieved_info = retrieve_with_rag(enhanced_query)
    output = model(enhanced_query + retrieved_info)
    return output
```

## Common Mistakes

- Neglecting to gather a comprehensive dataset, which can lead to poor model performance.
- Underestimating the importance of prompt-engineering for enhancing model responses.
- Failing to evaluate the model thoroughly on phase diagram queries.

## Use When

- You need to extract specific phase diagram information for magnesium alloys.
- You are developing an expert system in a niche domain.
- You want to enhance LLMs with domain-specific knowledge.

## Avoid When

- The application does not require specialized knowledge in metallurgy.
- You need a general-purpose LLM without domain constraints.
- Resources for training a specialized model are limited.

## Tradeoffs

**Strengths:**

- High accuracy in domain-specific queries (92% accuracy).
- Improved performance over standard LLMs (20% improvement).
- Ability to integrate domain-specific knowledge effectively.

**Weaknesses:**

- Limited applicability outside of magnesium alloys.
- Requires significant resources for training a specialized model.
- May not perform well on general-purpose queries.

**Compared To:**

- **vs Standard LLMs:** Use PDGPT for specialized queries; standard LLMs for general queries.

## Connects To

- Retrieval-Augmented Generation (RAG)
- Supervised Fine Tuning (SFT)
- Prompt Engineering
- Domain-Specific Language Models

## Evidence (Papers)

- **PDGPT: A large language model for acquiring phase diagram information in magnesium alloys** - [DOI](https://doi.org/10.1002/mgea.77)
