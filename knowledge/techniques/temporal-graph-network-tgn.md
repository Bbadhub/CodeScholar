# Temporal Graph Network (TGN)

**TGN is a neural network architecture designed to process dynamic graphs that evolve over time for tasks such as fraud detection.**

**Category:** neural_architecture  
**Maturity:** emerging

## How It Works

Temporal Graph Networks utilize an Event-Based Temporal Graph (ETG) to represent transactions as a dynamic graph where vertices and edges change over time based on transaction events. The TGN employs a message-passing mechanism to compute messages from neighboring vertices, aggregate these messages, and update memory states. This allows the model to learn embeddings for vertices involved in transactions and predict their class labels as fraudulent or legitimate.

## Algorithm

**Input:** Event-Based Temporal Graph (ETG) containing vertices, edges, and timestamps of transactions.

**Output:** Predicted class labels for transactions (fraudulent or normal) along with evaluation metrics like F1 score and AUC.

**Steps:**

1. 1. Initialize memory states and raw messages.
2. 2. For each epoch, iterate through batches of events in the training set.
3. 3. Compute messages based on the current state.
4. 4. Aggregate messages from neighboring vertices.
5. 5. Update memory states with aggregated messages.
6. 6. Compute embeddings for the vertices involved in the transaction.
7. 7. Apply a sigmoid function to predict the class of the transaction.
8. 8. Calculate the weighted cross-entropy loss and update model parameters.

**Core Operation:** `output = sigmoid(embedding · W + b)`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `train_ratio` | 0.7 | Affects the amount of data used for training. |
| `validation_ratio` | 0.15 | Determines the size of the validation set for tuning. |
| `test_ratio` | 0.15 | Sets aside data for final evaluation. |
| `n_epochs` | 100 | Controls how many times the model will see the training data. |

## Complexity

- **Time:** Not explicitly stated.
- **Space:** Not explicitly stated.
- **In practice:** Performance may vary based on the size and complexity of the input graph.

## Implementation

```python
def temporal_graph_network(data: ETG) -> List[str]:
    initialize_memory_states()
    for epoch in range(n_epochs):
        for batch in get_batches(data):
            messages = compute_messages(batch)
            aggregated_messages = aggregate(messages)
            update_memory_states(aggregated_messages)
            embeddings = compute_embeddings(batch)
            predictions = sigmoid(embeddings)
            update_model_parameters(predictions)
    return predictions
```

## Common Mistakes

- Neglecting to preprocess the temporal data correctly.
- Using an inappropriate train-validation-test split.
- Failing to tune hyperparameters effectively.

## Use When

- You need to detect fraudulent transactions in a dynamic environment.
- You have access to time-stamped transaction data.
- You want to leverage the relationships between different entities involved in transactions.

## Avoid When

- You are working with static transaction data without temporal information.
- You require real-time processing with extremely low latency.
- You have a very small dataset that cannot effectively train a neural network.

## Tradeoffs

**Strengths:**

- Effectively captures temporal dependencies in data.
- Utilizes relationships between entities for better predictions.
- Can improve detection metrics with more interaction events.

**Weaknesses:**

- Requires a substantial amount of data for training.
- May not perform well with static datasets.
- Complexity can lead to longer training times.

**Compared To:**

- **vs Traditional machine learning algorithms:** Use TGN for dynamic data; traditional methods may suffice for static data.

## Connects To

- Graph Neural Networks (GNN)
- Recurrent Neural Networks (RNN)
- Temporal Convolutional Networks (TCN)
- Dynamic Graph Representation Learning

## Evidence (Papers)

- **A Temporal Graph Network Algorithm for Detecting Fraudulent Transactions on Online Payment Platforms** [4 citations] - [DOI](https://doi.org/10.3390/a17120552)
