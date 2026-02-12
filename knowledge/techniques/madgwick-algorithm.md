# Madgwick algorithm

*Also known as: Madgwick filter*

**The Madgwick algorithm is used for real-time orientation estimation from inertial and magnetic sensor data.**

**Category:** sensor_fusion  
**Maturity:** proven (widely used in production)

## How It Works

The Madgwick algorithm fuses data from accelerometers, gyroscopes, and magnetometers to estimate the orientation of a device. It uses quaternion representation to minimize errors in sensor readings and applies an optimization step to update the orientation in real-time. This approach is particularly effective for applications requiring accurate motion tracking, such as in wearable devices and virtual reality systems.

## Algorithm

**Input:** Raw sensor data from accelerometers, gyroscopes, and magnetometers.

**Output:** Fused joint motion data with optimized joint angles and segment orientations.

**Steps:**

1. 1. Initialize the sensor data collection.
2. 2. Calibrate accelerometer, gyroscope, and magnetometer data to correct errors.
3. 3. Apply the Madgwick algorithm for attitude estimation.
4. 4. Update the quaternion using gyroscope data and optimization steps.
5. 5. Normalize the quaternion.
6. 6. Use the forward kinematics method to describe joint motion.
7. 7. Output the fused data for real-time applications.

**Core Operation:** `output = quaternion_update(gyro_data, error_compensation) · normalize(quaternion)`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `sampling_frequency` | 80 Hz | Higher frequencies can improve responsiveness but may introduce noise. |
| `η (error compensation factor)` | > 1 | Adjusting this factor can help in compensating for sensor errors. |
| `optimal bias vector for gyroscope` | [5, 6.2] for X-axis, [0, 5] for Y-axis, [-5, 3] for Z-axis | Fine-tuning these values can reduce drift in orientation estimates. |
| `optimal bias vector for accelerometer` | [7.5, 10] for X-axis, [7.5, 10] for Y-axis, [0, 10] for Z-axis | Improves accuracy of motion tracking. |
| `optimal bias vector for magnetometer` | [0, 5] for X-axis, [10, +00] for Y-axis, [-3.5, 0] for Z-axis | Enhances the reliability of magnetic field readings. |

## Complexity

- **Time:** O(n) where n is the number of sensor readings processed
- **Space:** O(1) for storing quaternion and bias vectors
- **In practice:** The algorithm is efficient for real-time applications, but performance may vary based on sensor quality.

## Implementation

```python
def madgwick_algorithm(accel: List[float], gyro: List[float], mag: List[float]) -> Tuple[float, float, float]:
    # Initialize quaternion and bias vectors
    quaternion = initialize_quaternion()
    # Calibrate sensor data
    calibrated_accel, calibrated_gyro, calibrated_mag = calibrate_sensors(accel, gyro, mag)
    # Apply Madgwick algorithm
    quaternion = update_quaternion(quaternion, calibrated_gyro)
    quaternion = normalize(quaternion)
    return quaternion
```

## Common Mistakes

- Neglecting to calibrate sensors before using the algorithm.
- Using incorrect bias values leading to inaccurate orientation estimates.
- Failing to normalize the quaternion after updates.

## Use When

- Building applications for real-time motion tracking in sports and rehabilitation.
- Developing virtual reality systems that require accurate motion capture.
- Creating wearable devices for health monitoring that need precise joint motion data.

## Avoid When

- When high computational complexity is a concern and real-time processing is not required.
- In environments where sensor drift and noise cannot be effectively managed.
- For applications needing extensive multi-modal data integration beyond joint motion.

## Tradeoffs

**Strengths:**

- Provides real-time orientation estimates.
- Reduces errors compared to traditional filtering methods.
- Simple to implement and computationally efficient.

**Weaknesses:**

- May struggle in environments with significant magnetic interference.
- Performance can degrade with poor sensor quality.
- Requires careful tuning of parameters for optimal results.

**Compared To:**

- **vs Complementary Filter:** Use Madgwick for more accurate orientation estimates in dynamic environments.
- **vs Extended Kalman Filter:** Use EKF for applications needing extensive multi-modal data integration.

## Connects To

- Complementary Filter
- Extended Kalman Filter
- Unscented Kalman Filter
- Sensor calibration techniques

## Evidence (Papers)

- **Human joint motion data capture and fusion based on wearable sensors** [1 citations] - [DOI](https://doi.org/10.1007/s43684-025-00098-w)
