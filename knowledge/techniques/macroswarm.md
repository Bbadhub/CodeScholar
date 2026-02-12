# MacroSwarm

**MacroSwarm enables decentralized coordination among devices to perform complex swarm behaviors through a sense-compute-interact loop.**

**Category:** swarm_programming  
**Maturity:** emerging

## How It Works

MacroSwarm models swarm behavior using an augmented event structure, allowing each device to operate independently while coordinating with neighbors. Each device continuously senses its environment and gathers messages from nearby devices. It then computes new values based on the sensed data and decides on actions, which are communicated through messages and actuations. This loop continues, enabling dynamic and resilient swarm behaviors.

## Algorithm

**Input:** Sensor data from the environment and messages from neighboring devices.

**Output:** Actuation commands and updated state information for each device.

**Steps:**

1. 1. Each device senses the environment and gathers messages from neighbors.
2. 2. The device computes new values based on the sensed data.
3. 3. The device decides on actions and interacts by sending messages and performing actuations.
4. 4. This process is repeated in a loop for all devices in the swarm.

**Core Operation:** `output = actuation_commands + updated_state_information`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `message_expiration_threshold` | configurable based on application needs | Affects how long messages are considered valid before being discarded. |
| `sensing_interval` | typically in milliseconds | Determines how frequently devices sense the environment, impacting responsiveness. |

## Complexity

- **Time:** Not stated
- **Space:** Not stated
- **In practice:** Performance may vary based on the number of devices and environmental complexity.

## Implementation

```python
def macro_swarm_loop(devices: List[Device]) -> None:
    while True:
        for device in devices:
            sensed_data = device.sense_environment()
            messages = device.receive_messages()
            new_values = device.compute(sensed_data, messages)
            commands = device.decide_actions(new_values)
            device.actuate(commands)
            device.send_messages()
```

## Common Mistakes

- Neglecting to tune the message expiration threshold, leading to outdated information.
- Setting the sensing interval too low, causing excessive resource consumption.
- Failing to account for communication delays among devices.

## Use When

- Designing decentralized systems with multiple interacting agents.
- Implementing complex swarm behaviors like flocking or pattern formation.
- Developing applications that require resilience to environmental changes.

## Avoid When

- When centralized control is preferred for simplicity.
- For applications with very low resource constraints where overhead is critical.

## Tradeoffs

**Strengths:**

- Enables decentralized decision-making and coordination.
- Robustness and resilience in dynamic environments.
- Supports complex swarm behaviors effectively.

**Weaknesses:**

- Higher overhead compared to centralized systems.
- Potentially increased complexity in debugging and monitoring.
- Performance may degrade with a large number of devices.

**Compared To:**

- **vs Centralized Control Systems:** Use MacroSwarm for decentralized applications; prefer centralized systems for simpler management.

## Connects To

- Multi-Agent Systems
- Distributed Computing
- Flocking Algorithms
- Pattern Formation Techniques

## Evidence (Papers)

- **Macroswarm: A field-based compositional framework for swarm programming** [17 citations] - [DOI](https://doi.org/10.46298/LMCS-21(3:13)2025)
