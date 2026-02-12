# QUIC

*Also known as: Quick UDP Internet Connections*

**QUIC is a transport layer network protocol designed to reduce latency and improve performance over unreliable networks.**

**Category:** networking_protocol  
**Maturity:** proven (widely used in production)

## How It Works

QUIC combines transport and application-layer functions to minimize handshake overhead and reduce latency. It uses multiplexing to allow multiple streams over a single connection, which helps in efficient data transmission. Additionally, QUIC implements built-in congestion control and supports connection migration, making it adaptable to changing network conditions.

## Algorithm

**Input:** UDP packets containing QUIC connection initiation and data streams.

**Output:** Established QUIC connections with multiplexed streams and reduced latency.

**Steps:**

1. 1. Initiate a QUIC connection using a single UDP packet.
2. 2. Perform a 0-RTT handshake if possible to establish the connection quickly.
3. 3. Multiplex multiple streams over the established connection.
4. 4. Implement built-in congestion control to adapt to network conditions.
5. 5. Handle incoming data streams without head-of-line blocking.
6. 6. Maintain connection migration capabilities for changing network environments.

**Core Operation:** `output = established QUIC connections with multiplexed streams and reduced latency`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `max_streams` | 100 | Increases the number of simultaneous streams that can be handled. |
| `initial_rtt` | 100ms | Affects the perceived latency during the initial connection setup. |
| `congestion_control_algorithm` | BBR | Determines how the protocol adapts to network congestion. |

## Complexity

- **Time:** Not explicitly stated
- **Space:** Not explicitly stated
- **In practice:** QUIC's performance can vary based on network conditions and implementation details.

## Implementation

```python
def quic_connection_initiation(data: bytes) -> str:
    # Step 1: Initiate QUIC connection
    send_udp_packet(data)
    # Step 2: Perform 0-RTT handshake if possible
    if can_perform_0_rtt():
        perform_handshake()
    # Step 3: Multiplex streams
    multiplex_streams()
    return 'QUIC connection established'
```

## Common Mistakes

- Neglecting to implement proper congestion control, leading to performance issues.
- Failing to handle connection migration, which can disrupt ongoing streams.
- Overlooking the need for a proper 0-RTT handshake implementation.

## Use When

- Building applications that require low-latency data transmission.
- Developing services that need to handle multiple streams efficiently.
- Creating applications that operate in unreliable network conditions.

## Avoid When

- Working in environments where TCP is mandated or required.
- Applications that do not require fast connection establishment.
- Scenarios where legacy support for TCP is critical.

## Tradeoffs

**Strengths:**

- Significantly reduces latency compared to traditional TCP.
- Supports multiplexing, allowing multiple streams without head-of-line blocking.
- Adapts well to changing network conditions with built-in congestion control.

**Weaknesses:**

- Not suitable for environments where TCP is required.
- May require more complex implementation compared to TCP.
- Limited support in some legacy systems.

**Compared To:**

- **vs TCP:** Use QUIC for low-latency applications; use TCP for legacy support and environments where it's mandated.

## Connects To

- TCP
- HTTP/3
- WebRTC
- SCTP

## Evidence (Papers)

- **QUIC and TCP in unsafe networks: A comparative analysis** [4 citations] - [DOI](https://doi.org/10.1049/smc2.12083)
