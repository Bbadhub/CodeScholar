# Covert Communication via MQTT

*Also known as: Stealthy Messaging*

**This technique enables covert communication by obfuscating messages and transmitting them via the MQTT protocol.**

**Category:** communication_protocol  
**Maturity:** emerging

## How It Works

The technique splits a secret message into multiple parts and obfuscates these parts using modular exponentiation. Each part is then sent as an MQTT message. Subscribers can reconstruct the original message by applying the XOR operation on the received parts. This method allows for stealthy communication in environments where message patterns are monitored.

## Algorithm

**Input:** The secret message M and parameters k, a, n, and the MQTT broker and topic information.

**Output:** The original message M reconstructed from the received parts.

**Steps:**

1. 1. Generate k random parts of the same size as the message M.
2. 2. Compute the k-th part as Pk = M XOR P1 XOR ... XOR Pk-1.
3. 3. For each part Pi, compute the length L = (Pi^a mod n) mod l, where l is the maximum MQTT message size.
4. 4. Publish each part using the MQTT protocol with the computed lengths.
5. 5. Subscribers retrieve parts by brute-forcing possible values based on the lengths of incoming packets.
6. 6. Reconstruct the original message M using M = P1 XOR P2 XOR ... XOR Pk.

**Core Operation:** `M = P1 XOR P2 XOR ... XOR Pk`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `k` | 3 | Increases the number of parts, enhancing security but requiring more overhead. |
| `a` | 1861836248542572424 | Affects the obfuscation strength of the message parts. |
| `n` | 89802601036489635412700864252846407279584917476820871708772821852121126622533 | Defines the modulus for the modular exponentiation. |
| `l` | 268,435,456 bytes | Limits the maximum size of each MQTT message. |

## Complexity

- **Time:** Not explicitly stated.
- **Space:** Not explicitly stated.
- **In practice:** No significant time overhead; additional byte overhead remains within acceptable limits.

## Implementation

```python
def covert_communication(message: str, k: int, a: int, n: int, broker: str, topic: str) -> str:
    parts = generate_random_parts(message, k)
    for i in range(k):
        length = (parts[i] ** a % n) % max_mqtt_size
        publish_mqtt(broker, topic, parts[i], length)
    received_parts = subscribe_mqtt(broker, topic)
    return reconstruct_message(received_parts)
```

## Common Mistakes

- Not properly handling the MQTT message size limits.
- Failing to securely generate random parts, compromising the message's security.
- Neglecting to account for potential packet loss in MQTT communication.

## Use When

- You need to transmit sensitive information in environments with high surveillance.
- You want to avoid detection of communication patterns by censors.
- You are working with IoT devices that require secure data exchange.

## Avoid When

- The communication environment is not subject to monitoring or censorship.
- You require high-speed data transmission without any overhead.
- The application does not support MQTT protocol.

## Tradeoffs

**Strengths:**

- Provides a covert channel for sensitive communication.
- Utilizes existing MQTT infrastructure, making it easy to implement.
- Low overhead in terms of execution time.

**Weaknesses:**

- Requires careful management of message parts to avoid detection.
- Brute-forcing may be necessary for subscribers, which can be resource-intensive.
- Dependent on the MQTT protocol, limiting its applicability.

**Compared To:**

- **vs Standard Encryption:** Use standard encryption for environments where covert communication is not necessary.

## Connects To

- MQTT Protocol
- Steganography
- Secure Messaging
- Data Obfuscation Techniques

## Evidence (Papers)

- **Stealthy Messaging: Leveraging Message Queuing Telemetry Transport for Covert Communication Channels** [1 citations] - [DOI](https://doi.org/10.3390/app14198874)
