# Stealthy Messaging: Leveraging Message Queuing Telemetry Transport for Covert Communication Channels

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3390/app14198874` |
| Full Paper | [https://doi.org/10.3390/app14198874](https://doi.org/10.3390/app14198874) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/d2a2e6c4eacb2689928200e6b16e3983adf445ac](https://www.semanticscholar.org/paper/d2a2e6c4eacb2689928200e6b16e3983adf445ac) |
| Source | [https://journalclub.io/episodes/stealthy-messaging-leveraging-message-queuing-telemetry-transport-for-covert-communication-channels](https://journalclub.io/episodes/stealthy-messaging-leveraging-message-queuing-telemetry-transport-for-covert-communication-channels) |
| Source | [https://www.semanticscholar.org/paper/d2a2e6c4eacb2689928200e6b16e3983adf445ac](https://www.semanticscholar.org/paper/d2a2e6c4eacb2689928200e6b16e3983adf445ac) |
| Year | 2026 |
| Citations | 1 |
| Authors | Sara Lazzaro, Francesco Buccafurri |
| Paper ID | `510c3b3c-4af6-42ac-b3c1-ce6de0dcd4f3` |

## Classification

- **Problem Type:** covert communication
- **Domain:** Cybersecurity
- **Sub-domain:** Covert channels, MQTT protocol
- **Technique:** Covert Communication via MQTT
- **Technique Category:** framework
- **Type:** novel

## Summary

The paper presents a novel method for covert communication using the MQTT protocol, allowing secret data exchange by embedding messages within normal MQTT traffic. Engineers should care because this approach enhances privacy and security in environments where communication is monitored or censored.

## Key Contribution

**A new covert communication method utilizing MQTT messages to create a storage channel for secure data exfiltration.**

## Problem

The need for secure and undetectable communication in environments subject to censorship and surveillance.

## Method

**Approach:** The method involves generating k parts of a secret message, applying modular exponentiation to obfuscate these parts, and sending them through MQTT messages. Subscribers can reconstruct the original message using the XOR operation on the received parts.

**Algorithm:**

1. 1. Generate k random parts of the same size as the message M.
2. 2. Compute the k-th part as Pk = M ⊕ P1 ⊕ ... ⊕ Pk-1.
3. 3. For each part Pi, compute the length L = (Pi^a mod n) mod l, where l is the maximum MQTT message size.
4. 4. Publish each part using the MQTT protocol with the computed lengths.
5. 5. Subscribers retrieve parts by brute-forcing possible values based on the lengths of incoming packets.
6. 6. Reconstruct the original message M using M = P1 ⊕ P2 ⊕ ... ⊕ Pk.

**Input:** The secret message M and parameters k, a, n, and the MQTT broker and topic information.

**Output:** The original message M reconstructed from the received parts.

**Key Parameters:**

- `k: number of parts (e.g., k = 3)`
- `a: exponent used in modular exponentiation (e.g., 1861836248542572424)`
- `n: prime modulus (e.g., 89802601036489635412700864252846407279584917476820871708772821852121126622533)`
- `l: maximum MQTT message size (268,435,456 bytes)`

**Complexity:** Not stated.

## Benchmarks

**Tested on:** Simulated MQTT traffic with covert messages.

**Results:**

- Execution time for operations on publisher and subscriber sides.

**Compared against:** Standard MQTT communication without covert channels.

**Improvement:** No significant time overhead; additional byte overhead remains within acceptable limits.

## Implementation Guide

**Data Structures:** MQTT message structure, Pseudo-Random Number Generator (PRNG)

**Dependencies:** MQTT library (e.g., Paho MQTT for Python)

**Core Operation:**

```python
for each part in parts: publish MQTT message with length L
```

**Watch Out For:**

- Ensure the secret key is sufficiently long to prevent brute-force attacks.
- Carefully choose topics to avoid detection by censors.
- Monitor the overhead introduced by the additional bytes in MQTT messages.

## Use This When

- You need to transmit sensitive information in environments with high surveillance.
- You want to avoid detection of communication patterns by censors.
- You are working with IoT devices that require secure data exchange.

## Don't Use When

- The communication environment is not subject to monitoring or censorship.
- You require high-speed data transmission without any overhead.
- The application does not support MQTT protocol.

## Key Concepts

covert channels, MQTT, modular exponentiation, XOR operation, data obfuscation

## Connects To

- Encryption algorithms (e.g., AES)
- Anonymous communication protocols
- Other covert channel techniques

## Prerequisites

- Understanding of MQTT protocol and its message structure.
- Knowledge of cryptographic principles, especially modular arithmetic.
- Familiarity with XOR operations and their properties.

## Limitations

- The method relies on the MQTT protocol, which may not be suitable for all applications.
- Potential overhead in terms of additional bytes transmitted.
- Requires pre-shared keys among communicating parties.

## Open Questions

- How can this method be adapted to other communication protocols?
- What are the implications of using this method in different regulatory environments?

## Abstract

If you just sent those 10 pieces as is, any eavesdropper could easily reconstruct the message. So you don’t do that. This is where that agreed-upon key comes in. You perform a mathematical operation called modular exponentiation on each of the 10 parts, using the key. Modular exponentiation involves raising a number to a certain power (the exponent) and then finding the remainder when divided by another number (the modulus). This operation is commonly used in cryptography because it's easy to perform in one direction but very difficult to reverse without knowing the exponent, which, in this case, is the key.
