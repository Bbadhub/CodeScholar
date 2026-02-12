# RT-MQTT and MRT-MQTT

*Also known as: Real-Time MQTT, Multicast Real-Time MQTT*

**RT-MQTT and MRT-MQTT enhance MQTT for real-time communication in industrial applications using SDN integration.**

**Category:** networking_protocol  
**Maturity:** emerging

## How It Works

RT-MQTT allows applications to specify real-time requirements for MQTT messages, which are enforced by a Software-Defined Networking (SDN) controller. The framework intercepts MQTT traffic to extract these requirements and creates network reservations to ensure low latency and reliable communication. Multicast is utilized to efficiently propagate MQTT messages across multiple edge networks, optimizing performance in industrial scenarios.

## Algorithm

**Input:** MQTT messages with specified real-time requirements in User Properties.

**Output:** Real-time MQTT communication with guaranteed latency and reliability across the network.

**Steps:**

1. 1. Define real-time requirements using MQTT User Properties.
2. 2. Intercept MQTT traffic with a Network Manager.
3. 3. Extract real-time information from the intercepted traffic.
4. 4. Instruct the SDN controller to create network reservations based on the extracted information.
5. 5. Deploy multicast across selected brokers to propagate MQTT traffic.
6. 6. Monitor and adjust network reservations as needed.

**Core Operation:** `output = real-time MQTT communication with guaranteed latency and reliability`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `QoS levels` | 0, 1, 2 | Determines the delivery guarantee of messages. |
| `Latency requirements` | application-specific | Specifies the acceptable delay for message delivery. |
| `Network reservation parameters` | application-specific | Defines the resources reserved for real-time communication. |

## Complexity

- **Time:** Not stated.
- **Space:** Not stated.
- **In practice:** Performance improvements are observed in latency reduction compared to standard MQTT and DM-MQTT.

## Implementation

```python
def rt_mqtt_implementation(mqtt_message: str, user_properties: dict) -> None:
    # Step 1: Define real-time requirements
    define_real_time_requirements(user_properties)
    # Step 2: Intercept MQTT traffic
    intercepted_traffic = intercept_mqtt_traffic(mqtt_message)
    # Step 3: Extract real-time information
    real_time_info = extract_real_time_info(intercepted_traffic)
    # Step 4: Instruct SDN controller
    create_network_reservations(real_time_info)
    # Step 5: Deploy multicast
    deploy_multicast()
    # Step 6: Monitor and adjust
    monitor_and_adjust_reservations()
```

## Common Mistakes

- Failing to properly define real-time requirements in User Properties.
- Neglecting to monitor network performance after deployment.
- Overcomplicating the network configuration without clear benefits.

## Use When

- You need to ensure real-time communication in industrial IoT applications.
- You are working with heterogeneous devices that require dynamic network management.
- You want to reduce latency in MQTT communications across multiple edge networks.

## Avoid When

- The application does not require real-time guarantees.
- You are working in a static network environment with no need for dynamic reconfiguration.
- The overhead of integrating SDN is not justified for your use case.

## Tradeoffs

**Strengths:**

- Ensures low latency and reliable communication for real-time applications.
- Utilizes SDN for dynamic network management.
- Efficiently propagates messages using multicast.

**Weaknesses:**

- Increased complexity due to SDN integration.
- Potential overhead in network management.
- Not suitable for static network environments.

**Compared To:**

- **vs Standard MQTT:** Use RT-MQTT when real-time guarantees are needed; otherwise, standard MQTT suffices.
- **vs DM-MQTT:** RT-MQTT is preferred for lower latency requirements in dynamic environments.

## Connects To

- MQTT
- Software-Defined Networking (SDN)
- Multicast Networking
- Industrial IoT Protocols

## Evidence (Papers)

- **A Scalable Real-Time SDN-Based MQTT Framework for Industrial Applications** - [DOI](https://doi.org/10.1109/OJIES.2024.3373232)
