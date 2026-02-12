# Break-Pad

**Break-Pad injects random padding packets into traffic bursts to enhance privacy in the Tor network.**

**Category:** traffic_obfuscation  
**Maturity:** emerging

## How It Works

Break-Pad operates by monitoring incoming traffic packets and injecting a random number of padding packets when a specified threshold of consecutive packets is reached. This randomness disrupts predictable traffic patterns, making it harder for adversaries to analyze the traffic flow. The technique dynamically adjusts the threshold and the number of padding packets based on sampled probability distributions.

## Algorithm

**Input:** Traffic packets flowing through the Tor network.

**Output:** Modified traffic with injected padding packets to disrupt burst patterns.

**Steps:**

1. Sample threshold p and padding burst b from their respective probability distributions.
2. Initialize a counter n for consecutive incoming packets.
3. For each incoming packet, increment n.
4. If n equals p, send b padding packets and resample p and b.
5. If an outgoing packet is detected and n is not zero, reset n and resample p and b.

**Core Operation:** `output = incoming_packets + padding_packets`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `p` | sampled from Dp | Increases the threshold for injecting padding. |
| `b` | sampled from Db | Determines the number of padding packets injected. |
| `Dp` | probability distribution for p | Affects the variability of the threshold. |
| `Db` | probability distribution for b | Affects the variability in the number of padding packets. |

## Complexity

- **Time:** Not stated
- **Space:** Not stated
- **In practice:** Performance metrics indicate a bandwidth overhead of 29% to 36% depending on the dataset.

## Implementation

```python
def break_pad(incoming_packets: List[Packet]) -> List[Packet]:
    p = sample_from_distribution(Dp)
    b = sample_from_distribution(Db)
    n = 0
    modified_packets = []
    for packet in incoming_packets:
        n += 1
        if n == p:
            modified_packets.extend(generate_padding_packets(b))
            p = sample_from_distribution(Dp)
            b = sample_from_distribution(Db)
        modified_packets.append(packet)
        if is_outgoing_packet(packet):
            n = 0
            p = sample_from_distribution(Dp)
            b = sample_from_distribution(Db)
    return modified_packets
```

## Common Mistakes

- Failing to properly sample from the probability distributions for p and b.
- Not resetting the counter n correctly when an outgoing packet is detected.
- Overlooking the impact of bandwidth overhead on application performance.

## Use When

- You need to enhance user privacy in applications using the Tor network.
- You are facing challenges with existing WF defenses being ineffective against advanced attacks.
- You want to minimize bandwidth overhead while implementing traffic obfuscation.

## Avoid When

- The application does not require strong privacy protections.
- You are working in a low-latency environment where bandwidth overhead is critical.
- Existing defenses are sufficient for your use case.

## Tradeoffs

**Strengths:**

- Enhances user privacy by obfuscating traffic patterns.
- Reduces predictability of packet flow, complicating traffic analysis.
- Minimizes bandwidth overhead compared to some existing methods.

**Weaknesses:**

- May introduce latency due to additional padding packets.
- Not suitable for applications requiring low-latency communication.
- Effectiveness can vary based on the chosen probability distributions.

**Compared To:**

- **vs WTF-PAD:** Use Break-Pad for better bandwidth efficiency while maintaining privacy.
- **vs RBB:** Break-Pad offers improved performance with less bandwidth overhead.

## Connects To

- Traffic Padding Techniques
- Tor Network Enhancements
- Privacy-preserving Protocols
- Traffic Analysis Resistance Methods

## Evidence (Papers)

- **Break-Pad: effective padding machines for tor with break burst padding** - [DOI](https://doi.org/10.1186/s42400-024-00222-y)
