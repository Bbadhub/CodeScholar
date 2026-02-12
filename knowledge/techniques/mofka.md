# Mofka

**Mofka is an event-streaming system optimized for high-performance computing applications.**

**Category:** event_streaming  
**Maturity:** emerging

## How It Works

Mofka separates event data into metadata and payloads, optimizing the transfer of each component. It utilizes Remote Direct Memory Access (RDMA) for high-speed data transfers, making it suitable for handling large scientific payloads. The system supports batching of metadata and allows consumers to selectively retrieve data, enhancing efficiency in high-performance computing environments.

## Algorithm

**Input:** Events consisting of metadata (small, structured) and data (large, scientific payloads)

**Output:** Streamed events with metadata and selected data parts

**Steps:**

1. 1. Producer creates a topic with a validator, partition selector, and serializer.
2. 2. Producer batches metadata and sends it to the partition manager.
3. 3. Partition manager redirects metadata to a log provider and RDMA handles for data to a storage provider.
4. 4. Consumer subscribes to partitions and receives metadata batches.
5. 5. Consumer uses a data selector to specify which data parts to retrieve.
6. 6. Data broker transfers the selected data directly to the consumer's memory.

**Core Operation:** `output = streamed events with metadata and selected data parts`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `batch_size` | 128 | Increasing batch size can improve throughput but may increase latency. |
| `number_of_threads` | 4 | More threads can enhance parallel processing capabilities. |

## Complexity

- **Time:** Not stated
- **Space:** Not stated
- **In practice:** Performance improvements can be significant in high-throughput scenarios.

## Implementation

```python
def mofka_producer(topic: str, metadata: dict, data: bytes) -> None:
    # Create topic with validator and serializer
    # Batch metadata and send to partition manager
    pass

def mofka_consumer(topic: str) -> bytes:
    # Subscribe to partitions and receive metadata
    # Selectively retrieve data parts
    pass
```

## Common Mistakes

- Not optimizing batch sizes for specific workloads.
- Neglecting to configure RDMA settings for optimal performance.
- Failing to properly manage memory allocation for large payloads.

## Use When

- You need to manage large data streams in HPC applications.
- You require high throughput and low latency for data transfer in scientific workflows.
- You want to leverage advanced networking capabilities of HPC systems.

## Avoid When

- Your application does not require persistence of data.
- You are working with small, structured messages typical in enterprise contexts.
- You need a solution that is not tailored for HPC environments.

## Tradeoffs

**Strengths:**

- Significantly improved throughput compared to traditional systems like Kafka.
- Optimized for large payloads typical in scientific computing.
- Utilizes advanced networking features for efficient data transfer.

**Weaknesses:**

- Not suitable for small, structured message scenarios.
- Requires a specific HPC environment for optimal performance.
- Complex setup and configuration compared to simpler messaging systems.

**Compared To:**

- **vs Kafka:** Use Mofka for high-throughput HPC applications; use Kafka for general-purpose messaging.

## Connects To

- RDMA
- Apache Kafka
- Redpanda
- High-Performance Computing (HPC) frameworks

## Evidence (Papers)

- **Toward a persistent event-streaming system for high-performance computing applications** [3 citations] - [DOI](https://doi.org/10.3389/fhpcp.2025.1638203)
