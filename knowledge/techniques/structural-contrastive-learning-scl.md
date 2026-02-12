# Structural Contrastive Learning (SCL)

**SCL is a framework for unsupervised fake news detection that learns representations from augmented views of news propagation structures.**

**Category:** neural_architecture  
**Maturity:** emerging

## How It Works

SCL employs a twin-network architecture to process augmented views of news propagation trees. By using random cropping, it generates positive instances that are fed into graph convolutional networks (GCNs) for feature encoding. The outputs from the online and target networks are then compared using a contrastive loss, which helps in learning effective representations for distinguishing between fake and real news.

## Algorithm

**Input:** News propagation trees represented as graphs with nodes and edges.

**Output:** Predictions of whether news is fake or real.

**Steps:**

1. 1. Perform data augmentation on the news propagation tree using random cropping.
2. 2. Input the two positive instances into the online and target networks.
3. 3. Use GCN to encode the structure features of the news propagation tree.
4. 4. Apply a nonlinear projection to obtain low-dimensional representations.
5. 5. Compute the contrastive loss between the online and target network outputs.
6. 6. Optimize the online network parameters using gradient descent.
7. 7. Update the target network parameters based on a momentum function.

**Core Operation:** `loss = contrastive_loss(output_online, output_target)`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `learning_rate` | 0.001 | A higher learning rate may speed up training but can lead to instability. |
| `momentum_decay_rate` | 0.996 | Adjusting this affects how quickly the target network updates. |
| `random_cropping_rate` | 0.1/0.2/0.3/0.4/0.5 | Higher rates may create more diverse positive instances. |
| `batch_size` | 128 | Larger batch sizes can stabilize training but require more memory. |
| `hidden_size_of_GCN` | 128 | Increasing this can capture more complex features but may lead to overfitting. |
| `output_dimension_of_projection_head` | 128 | Higher dimensions can improve representation capacity but increase computational cost. |
| `output_dimension_of_prediction_head` | 128 | Similar to projection head, affects the model's capacity. |

## Complexity

- **Time:** Not stated
- **Space:** Not stated
- **In practice:** Performance may vary based on the complexity of the news propagation structures.

## Implementation

```python
def structural_contrastive_learning(data: Graph, learning_rate: float) -> Model:
    online_net = initialize_network()
    target_net = initialize_network()
    for batch in data:
        pos_instance1, pos_instance2 = augment_data(batch)
        features1 = gcn_encode(online_net, pos_instance1)
        features2 = gcn_encode(target_net, pos_instance2)
        loss = compute_contrastive_loss(features1, features2)
        update_network(online_net, loss, learning_rate)
        update_target_network(target_net)
    return online_net
```

## Common Mistakes

- Neglecting to properly tune the random cropping rate, which can affect the quality of positive instances.
- Failing to update the target network correctly, leading to suboptimal performance.
- Overfitting due to too complex GCN architectures without proper regularization.

## Use When

- You need to detect fake news without labeled datasets.
- You want to leverage the propagation structure of news for detection.
- You are working with social media data that is rapidly generated.

## Avoid When

- You have access to large labeled datasets for supervised learning.
- You require real-time detection with minimal latency.
- You need a method that is easily interpretable.

## Tradeoffs

**Strengths:**

- Effective in unsupervised settings without labeled data.
- Utilizes the structure of news propagation for better feature extraction.
- Improves performance significantly over traditional methods.

**Weaknesses:**

- May require extensive tuning of hyperparameters.
- Not suitable for real-time applications due to potential latency.
- Interpretability of the model can be challenging.

**Compared To:**

- **vs Supervised Learning:** Use SCL when labeled data is unavailable; otherwise, supervised methods may yield better results.

## Connects To

- Graph Neural Networks
- Contrastive Learning
- Unsupervised Learning Techniques
- Fake News Detection Methods

## Evidence (Papers)

- **An Unsupervised Fake News Detection Framework Based on Structural Contrastive Learning** - [DOI](https://doi.org/10.1186/s42400-024-00342-5)
