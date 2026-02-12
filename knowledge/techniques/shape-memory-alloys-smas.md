# Shape Memory Alloys (SMAs)

*Also known as: SMAs*

**Shape Memory Alloys are materials that can change shape in response to stimuli, enabling soft actuators that mimic biological movements.**

**Category:** material_technology  
**Maturity:** emerging

## How It Works

Shape Memory Alloys undergo a phase transformation when subjected to specific temperatures, allowing them to return to a predetermined shape. This property is harnessed to create soft actuators that can flex and move in ways similar to biological organisms. By controlling the temperature, these actuators can be activated to perform complex movements, making them suitable for various applications in soft robotics.

## Algorithm

**Input:** Design specifications, material properties, control signals.

**Output:** Movement of the soft robot mimicking biological motion.

**Steps:**

1. Identify the biological movement to mimic.
2. Select appropriate materials (e.g., SMAs).
3. Design actuator geometry based on desired movement.
4. Implement control methods to activate the actuator.
5. Test and refine the actuator performance.

**Core Operation:** `output = movement of the soft robot mimicking biological motion`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `temperature_threshold` | 60°C | Changing this affects the activation point of the SMA. |
| `actuator_length` | variable | Altering length changes the range of motion. |
| `force_output` | 5N | Increasing this enhances the actuator's strength. |

## Complexity

- **Time:** O(1) for activation, but design complexity varies.
- **Space:** O(1) for actuator storage, but design space can be large.
- **In practice:** Real-world performance can vary based on environmental conditions and material quality.

## Implementation

```python
def activate_sma(actuator_length: float, temperature: float) -> str:
    if temperature >= 60:
        return 'Actuator activated, mimicking movement'
    else:
        return 'Actuator not activated'
```

## Common Mistakes

- Neglecting the temperature range for activation.
- Overlooking the actuator's response time in design.
- Failing to test the actuator under expected environmental conditions.

## Use When

- Developing soft robots for medical applications
- Creating flexible robotic systems for search and rescue
- Designing wearable technology that requires soft movement

## Avoid When

- High precision tasks requiring rigid structures
- Applications where high load-bearing capacity is essential
- Environments with extreme temperatures affecting material properties

## Tradeoffs

**Strengths:**

- High flexibility and adaptability compared to rigid actuators.
- Ability to mimic complex biological movements.
- Lightweight and compact design.

**Weaknesses:**

- Limited load-bearing capacity.
- Temperature sensitivity can affect performance.
- Potential for fatigue over repeated cycles.

**Compared To:**

- **vs Traditional rigid actuators:** Use SMAs for flexibility; use rigid actuators for precision and load-bearing.

## Connects To

- Soft robotics
- Bioinspired design
- Actuator technology
- Material science

## Evidence (Papers)

- **A Review on Recent Trends of Bioinspired Soft Robotics: Actuators, Control Methods, Materials Selection, Sensors, Challenges, and Future Prospects** [70 citations] - [DOI](https://doi.org/10.1002/aisy.202400414)
