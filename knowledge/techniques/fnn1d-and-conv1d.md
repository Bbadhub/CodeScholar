# FNN1D and Conv1D

*Also known as: Feedforward Neural Network 1D, Convolutional Neural Network 1D*

**FNN1D and Conv1D are neural network architectures used for classifying skeletal representations of poses.**

**Category:** neural_architecture  
**Maturity:** proven

## How It Works

FNN1D and Conv1D models process skeletal keypoints extracted from images to classify yoga poses. The skeletal data is transformed into feature vectors, which are then fed into the neural networks for training. The models learn to recognize patterns in the skeletal data, allowing them to predict the yoga pose from new input images.

## Algorithm

**Input:** Images of yoga poses in .jpg or .png format, converted to skeletal data.

**Output:** Predicted yoga pose labels corresponding to the input images.

**Steps:**

1. 1. Collect images of yoga poses.
2. 2. Use MoveNet to extract skeletal keypoints from images.
3. 3. Preprocess the keypoints into a feature vector.
4. 4. Train the FNN1D or Conv1D model using the feature vectors.
5. 5. Evaluate the model's performance using metrics like accuracy, precision, recall, and F1-score.
6. 6. Deploy the model in a web application for real-time yoga pose recognition.

**Core Operation:** `output = activation(weights · input + bias)`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `learning_rate` | 0.0005 | A higher learning rate may speed up training but can lead to instability. |
| `batch_size` | 32 | Larger batch sizes can improve training speed but may require more memory. |
| `epochs` | 80 | More epochs can improve accuracy but may lead to overfitting. |
| `dropout_rate` | 0.2 | Higher dropout rates can reduce overfitting but may hinder learning. |

## Complexity

- **Time:** O(n * m), where n is the number of samples and m is the number of features
- **Space:** O(m), where m is the number of features
- **In practice:** Real-world performance can vary based on dataset size and model architecture.

## Implementation

```python
def train_model(data: List[float], labels: List[int]) -> Model:
    model = create_model()
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    model.fit(data, labels, batch_size=32, epochs=80)
    return model
```

## Common Mistakes

- Neglecting to preprocess skeletal data properly.
- Using inappropriate learning rates leading to poor convergence.
- Overfitting the model by training for too many epochs without validation.

## Use When

- Building applications for yoga pose recognition.
- Creating virtual trainers for fitness applications.
- Developing systems that require real-time human pose analysis.

## Avoid When

- Working with non-human poses or actions.
- When RGB image data is preferred over skeletal data.
- In scenarios requiring 3D pose recognition.

## Tradeoffs

**Strengths:**

- High accuracy in recognizing yoga poses.
- Real-time processing capabilities.
- Effective with skeletal data representation.

**Weaknesses:**

- Limited to human poses.
- Dependent on quality of skeletal keypoint extraction.
- Not suitable for RGB image classification.

**Compared To:**

- **vs VGG16:** Use FNN1D or Conv1D for skeletal data; VGG16 for RGB images.
- **vs ResNet:** FNN1D and Conv1D are simpler and faster for skeletal data.

## Connects To

- MoveNet for keypoint extraction
- LSTM for sequential pose analysis
- Transfer learning techniques
- Data augmentation methods for training

## Evidence (Papers)

- **An Approach using Skeleton-based Representations and Neural Networks for Yoga Pose Recognition** - [DOI](https://doi.org/10.2478/acss-2025-0009)
