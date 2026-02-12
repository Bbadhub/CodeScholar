# Asymmetric Byzantine Quorum Systems

**Asymmetric Byzantine Quorum Systems enable consensus in distributed systems with varying trust assumptions among processes.**

**Category:** distributed_systems  
**Maturity:** emerging

## How It Works

This technique allows each process in a distributed system to define its own trust assumptions about other processes. It constructs local quorum systems that ensure consistency and availability while implementing protocols for shared memory and reliable broadcasts. The approach extends traditional consensus protocols to accommodate asymmetric trust, ensuring safety for wise processes and liveness based on the presence of sufficient wise processes.

## Algorithm

**Input:** A set of processes with defined trust assumptions and communication links.

**Output:** Consensus decisions, reliable broadcasts, and shared memory states.

**Steps:**

1. 1. Define a fail-prone system for each process based on its trust assumptions.
2. 2. Construct local quorum systems for each process that satisfy consistency and availability conditions.
3. 3. Implement protocols for shared memory and broadcast using the defined quorums.
4. 4. Extend a randomized binary consensus protocol to work with asymmetric trust.
5. 5. Ensure that safety is guaranteed for wise processes and liveness depends on the presence of a sufficient number of wise processes.

**Core Operation:** `Consensus decisions are made based on the defined local quorum systems and trust assumptions.`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `n` | number of processes | Affects the overall system size and complexity. |
| `f` | maximum number of faulty processes (typically f < n/3) | Determines the fault tolerance of the system. |
| `local_quorum_size` | varies based on trust assumptions | Influences the safety and liveness guarantees. |

## Complexity

- **Time:** Not explicitly stated
- **Space:** Not explicitly stated
- **In practice:** Performance may vary based on the number of processes and the specific trust assumptions defined.

## Implementation

```python
def asymmetric_byzantine_quorum_system(processes: List[Process], trust_assumptions: Dict[Process, TrustAssumption]) -> ConsensusDecision:
    # Step 1: Define fail-prone systems
    for process in processes:
        define_fail_prone_system(process, trust_assumptions[process])
    # Step 2: Construct local quorum systems
    local_quorums = construct_local_quorum_systems(processes)
    # Step 3: Implement protocols
    implement_shared_memory_protocol(local_quorums)
    implement_broadcast_protocol(local_quorums)
    # Step 4: Extend consensus protocol
    return extend_consensus_protocol(local_quorums)
```

## Common Mistakes

- Assuming uniform trust across all processes when using asymmetric quorums.
- Neglecting to define clear trust assumptions for each process.
- Overlooking the impact of local quorum sizes on system performance.

## Use When

- Building decentralized applications that require flexible trust models.
- Implementing consensus protocols in permissioned blockchain systems.
- Designing distributed systems where nodes may have different trust levels.

## Avoid When

- The system requires uniform trust assumptions across all nodes.
- Performance is critical and the overhead of asymmetric trust is unacceptable.
- The application domain does not involve Byzantine faults.

## Tradeoffs

**Strengths:**

- Allows for flexible trust models among processes.
- Improves safety guarantees for wise processes.
- Enhances liveness conditions compared to traditional systems.

**Weaknesses:**

- Increased complexity in defining trust assumptions.
- Potential performance overhead due to asymmetric trust.
- Requires careful design to ensure safety and liveness.

**Compared To:**

- **vs Traditional Byzantine Quorum Systems:** Use asymmetric systems when trust levels vary; use traditional systems for uniform trust.

## Connects To

- Byzantine Fault Tolerance
- Consensus Algorithms
- Distributed Ledger Technologies
- Decentralized Applications

## Evidence (Papers)

- **Asymmetric Distributed Trust** [45 citations] - [DOI](https://doi.org/10.1007/s00446-024-00469-1)
