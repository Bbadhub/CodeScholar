# Token Probability Analysis

**Token Probability Analysis evaluates the accuracy of language model responses by analyzing token probabilities and expressed confidence levels.**

**Category:** statistical_method  
**Maturity:** emerging

## How It Works

This technique involves prompting large language models (LLMs) with specific questions and extracting both the confidence ratings and token probabilities associated with their answers. By comparing these metrics against the actual accuracy of the responses, it assesses how well the token probabilities predict the correctness of the answers. This method is particularly useful in high-stakes fields like medicine, where understanding model confidence is crucial.

## Algorithm

**Input:** Medical questions from datasets such as the USMLE MedQA database.

**Output:** Predicted accuracy of responses based on token probabilities and expressed confidence.

**Steps:**

1. Select a set of LLMs that provide access to internal probabilities.
2. Prompt each model with a medical question and request a confidence rating.
3. Extract the token probability for the chosen answer from the model's output.
4. Evaluate the accuracy of the model's response.
5. Compare the predictive performance of expressed confidence and token probabilities using statistical metrics.

**Core Operation:** `accuracy = f(token_probabilities, expressed_confidence)`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `temperature` | 0 | Reduces variability in model responses. |
| `prompting_strategy` | vanilla prompting | Standardizes the input format for consistency. |
| `confidence_scale` | 0 to 100 | Defines the range of expressed confidence levels. |

## Complexity

- **Time:** O(n) where n is the number of questions processed.
- **Space:** O(m) where m is the number of models evaluated.
- **In practice:** Real-world performance may vary based on model architecture and dataset size.

## Implementation

```python
def token_probability_analysis(models: List[LLM], questions: List[str]) -> List[float]:
    results = []
    for model in models:
        for question in questions:
            confidence = model.get_confidence(question)
            token_prob = model.get_token_probability(question)
            accuracy = evaluate_accuracy(model.answer(question))
            results.append((confidence, token_prob, accuracy))
    return results
```

## Common Mistakes

- Assuming all models provide internal probabilities.
- Neglecting to validate the accuracy of model responses.
- Using inappropriate datasets that do not reflect real-world scenarios.

## Use When

- Building medical chatbots that require reliable confidence estimation.
- Evaluating the performance of LLMs in clinical settings.
- Improving decision-making processes in healthcare applications.

## Avoid When

- The application does not require high-stakes decision-making.
- When using models that do not provide access to internal probabilities.
- In scenarios where expressed confidence is sufficient.

## Tradeoffs

**Strengths:**

- Provides a quantitative measure of model confidence.
- Improves decision-making in critical applications.
- Enhances understanding of model behavior.

**Weaknesses:**

- Requires models with accessible internal probabilities.
- May not be applicable in low-stakes scenarios.
- Performance can vary significantly between models.

**Compared To:**

- **vs Expressed Confidence Estimation:** Use Token Probability Analysis for more reliable predictions in high-stakes contexts.

## Connects To

- Confidence Estimation
- Large Language Models
- Medical Chatbots
- Statistical Analysis in AI

## Evidence (Papers)

- **Token Probabilities to Mitigate Large Language Models Overconfidence in Answering Medical Questions: Quantitative Study** [8 citations] - [DOI](https://doi.org/10.2196/64348)
