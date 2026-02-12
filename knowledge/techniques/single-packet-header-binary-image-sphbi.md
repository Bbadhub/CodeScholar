# Single Packet Header Binary Image (SPHBI)

**SPHBI converts TCP/IP packet headers into binary images for efficient classification of network traffic.**

**Category:** intrusion_detection  
**Maturity:** emerging

## How It Works

The SPHBI technique extracts relevant fields from TCP/IP packet headers and converts them into a binary format. This binary data is then arranged into a 12x12 matrix, forming a binary image. A lightweight Convolutional Neural Network (CNN) is used to classify these images as benign or malicious, making it suitable for real-time applications in IoT networks.

## Algorithm

**Input:** Raw TCP/IP packet headers converted into 12x12 binary images.

**Output:** Classification results indicating whether the traffic is benign or malicious.

**Steps:**

1. 1. Extract relevant fields from the TCP/IP packet header.
2. 2. Convert the extracted fields into a binary format.
3. 3. Arrange the binary data into a 12x12 matrix to form a binary image.
4. 4. Input the binary image into a CNN model for classification.
5. 5. Train the CNN model on labeled data (benign vs. malicious).
6. 6. Evaluate the model's performance on test datasets.

**Core Operation:** `output = CNN(binary_image)`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `learning_rate` | 0.001 | Affects the speed of convergence during training. |
| `batch_size` | 32 | Impacts the stability of the training process. |
| `epochs` | 50 | Determines how many times the model will see the training data. |
| `trainable_parameters` | 35 | Influences the model's capacity to learn from data. |

## Complexity

- **Time:** Not explicitly stated
- **Space:** Not explicitly stated
- **In practice:** Performance is optimized for real-time detection in constrained environments.

## Implementation

```python
def classify_packet(packet: bytes) -> str:
    binary_image = extract_and_convert(packet)
    result = cnn_model.predict(binary_image)
    return 'benign' if result == 0 else 'malicious'
```

## Common Mistakes

- Ignoring the importance of selecting relevant fields from the packet header.
- Overfitting the CNN model to the training data.
- Not properly evaluating the model on diverse test datasets.

## Use When

- You need a lightweight intrusion detection system for IoT devices.
- Real-time detection with minimal latency is required.
- You want to avoid complex feature extraction processes.

## Avoid When

- You require detailed packet payload analysis.
- Memory resources are not constrained.
- You need to detect a wide variety of attack types beyond those represented in the training data.

## Tradeoffs

**Strengths:**

- Achieves high accuracy in binary classification.
- Lightweight and suitable for real-time applications.
- Reduces the need for complex feature extraction.

**Weaknesses:**

- Limited to the types of attacks represented in the training data.
- May not perform well with detailed packet payload analysis.
- Resource constraints may limit model complexity.

**Compared To:**

- **vs Traditional feature extraction methods:** SPHBI is more efficient and requires less manual feature engineering.
- **vs Other deep learning models:** SPHBI is lighter and faster, making it suitable for IoT environments.

## Connects To

- Convolutional Neural Networks (CNNs)
- Intrusion Detection Systems (IDS)
- Feature Extraction Techniques
- Binary Classification Methods

## Evidence (Papers)

- **Intrusion detection using TCP/IP single packet header binary image for IoT networks** - [DOI](https://doi.org/10.1186/s42400-025-00441-x)
