# tapai

**tapai is a neural network-based method for classifying scorpion venom peptide sequences into toxin categories.**

**Category:** neural_architecture  
**Maturity:** proven (widely used in production)

## How It Works

tapai processes amino acid sequences from scorpion venom by padding or truncating them to a fixed length of 128 amino acids. A neural network is then trained on these sequences to classify them into various toxin categories. The model is validated using a separate dataset, achieving high accuracy in toxin classification compared to traditional methods like BLAST.

## Algorithm

**Input:** Amino acid sequences in fasta format.

**Output:** Classifications of sequences into toxin categories (ICK, KTx, NaTx, venom proteins, housekeeping genes).

**Steps:**

1. 1. Collect scorpion venom peptide sequences from databases.
2. 2. Preprocess sequences by padding or truncating to a fixed length (128 amino acids).
3. 3. Train the neural network on the processed sequences to classify them into toxin categories.
4. 4. Validate the model using a separate dataset and evaluate performance metrics.
5. 5. Use the trained model to classify new sequences from scorpion transcriptomes.

**Core Operation:** `output = neural_network(input_sequence)`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `input_length` | 128 | Determines the fixed size of input sequences for the model. |
| `training_sequences` | 5453 (positive), 49694 (negative) | Affects the model's ability to learn and generalize. |
| `validation_accuracy` | varies by category | Indicates the model's performance across different toxin categories. |

## Complexity

- **Time:** O(n * m) where n is the number of sequences and m is the sequence length
- **Space:** O(m) for storing sequences
- **In practice:** Performance may vary based on the size of the dataset and model architecture.

## Implementation

```python
def tapai_classify(sequences: List[str]) -> List[str]:
    processed_sequences = preprocess(sequences)
    model = load_trained_model()
    classifications = model.predict(processed_sequences)
    return classifications
```

## Common Mistakes

- Not preprocessing sequences correctly (padding/truncating).
- Using an insufficiently large dataset for training.
- Neglecting to validate the model with a separate dataset.

## Use When

- You need to classify short peptide sequences from scorpion venom.
- You want to improve the accuracy of toxin identification over traditional methods.
- You are working on drug discovery projects involving scorpion toxins.

## Avoid When

- You have a large dataset of well-annotated sequences that do not require further classification.
- You need real-time classification with minimal computational resources.

## Tradeoffs

**Strengths:**

- High accuracy in classifying toxin categories.
- Effective for short peptide sequences.
- Improves upon traditional classification methods.

**Weaknesses:**

- Requires a well-annotated training dataset.
- May not perform well with very large datasets.
- Computationally intensive compared to simpler methods.

**Compared To:**

- **vs BLAST:** tapai is preferred for higher accuracy in toxin classification.

## Connects To

- neural networks
- sequence classification
- bioinformatics
- toxin identification methods

## Evidence (Papers)

- **Optimizing Scorpion Toxin Processing through Artificial Intelligence** - [DOI](https://doi.org/10.3390/toxins16100437)
