# Hierarchical Attention Network (HAN)

**HAN is a neural network architecture designed to capture long-term dependencies and semantic relationships in data through hierarchical attention mechanisms.**

**Category:** neural_architecture  
**Maturity:** emerging

## How It Works

The Hierarchical Attention Network processes data at multiple levels, allowing it to focus on important parts of the input while ignoring irrelevant information. It uses attention mechanisms to weigh the significance of different segments of the input, which is particularly useful for tasks involving complex structures. In the context of smart contracts, HAN can effectively analyze both source code and opcode to detect vulnerabilities by capturing relationships between these modalities.

## Algorithm

**Input:** Source code and opcode of smart contracts (text data).

**Output:** Classification results indicating the presence of vulnerabilities (binary or categorical labels).

**Steps:**

1. Input the source code and opcode of the smart contract.
2. Preprocess the source code to remove irrelevant parts and standardize variable names.
3. Preprocess the opcode to eliminate unnecessary operations and standardize formats.
4. Use word embedding to convert the preprocessed data into vector representations.
5. Input the vectors into the hierarchical attention network for feature extraction.
6. Fuse the extracted features from both modalities.
7. Classify the vulnerabilities based on the fused features.

**Core Operation:** `output = attention(fused_features)`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `learning_rate` | 0.001 | A lower learning rate may lead to more stable convergence but slower training. |
| `batch_size` | 32 | Changing the batch size affects the training speed and memory usage. |
| `epochs` | 50 | More epochs can improve accuracy but may lead to overfitting. |

## Complexity

- **Time:** O(n * m) where n is the number of tokens and m is the number of features extracted.
- **Space:** O(n + m) for storing input and output representations.
- **In practice:** Performance may vary based on the complexity of the smart contracts being analyzed.

## Implementation

```python
def hierarchical_attention_network(source_code: str, opcode: str) -> str:
    preprocessed_code = preprocess(source_code)
    preprocessed_opcode = preprocess(opcode)
    vectors_code = word_embedding(preprocessed_code)
    vectors_opcode = word_embedding(preprocessed_opcode)
    features = extract_features(vectors_code, vectors_opcode)
    fused_features = fuse(features)
    return classify(fused_features)
```

## Common Mistakes

- Neglecting to preprocess the input data properly, leading to poor model performance.
- Using inappropriate hyperparameters without tuning, which can hinder learning.
- Failing to validate the model on unseen data, risking overfitting.

## Use When

- You need to detect vulnerabilities in long smart contracts.
- Existing methods fail to analyze complex smart contract structures.
- You want a lightweight solution that can run on low to medium performance computers.

## Avoid When

- You are working with short smart contracts where traditional methods suffice.
- You require real-time detection in a high-performance environment.
- You need to analyze contracts with very high complexity beyond the model's capacity.

## Tradeoffs

**Strengths:**

- Effectively captures long-term dependencies in complex data.
- Improves vulnerability detection accuracy compared to traditional methods.
- Lightweight and suitable for low to medium performance environments.

**Weaknesses:**

- May struggle with very high complexity contracts beyond its capacity.
- Not suitable for real-time detection scenarios.
- Performance can degrade with very short contracts.

**Compared To:**

- **vs Traditional static analyzers:** Use HAN for better accuracy in complex contracts.
- **vs BiLSTM-based classifiers:** HAN may outperform BiLSTM in capturing relationships between modalities.

## Connects To

- Attention Mechanisms
- Recurrent Neural Networks (RNN)
- Bidirectional LSTM (BiLSTM)
- Convolutional Neural Networks (CNN)

## Evidence (Papers)

- **A lightweight vulnerability detection method for long smart contracts based on bimodal feature fusion** - [DOI](https://doi.org/10.1186/s42400-024-00332-7)
