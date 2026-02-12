# Randomized Wait-Free Locks

**Randomized wait-free locks provide a mechanism for concurrent processes to access shared resources without blocking, ensuring fairness and bounded time complexity.**

**Category:** synchronization  
**Maturity:** emerging

## How It Works

This technique allows processes to attempt to acquire locks through a tryLock operation. If a process fails to acquire the lock due to contention, it can retry the operation while helping others complete their critical sections. This ensures that all processes make progress and that the system remains fair. The method is designed to handle high contention scenarios efficiently.

## Algorithm

**Input:** A set of locks and a thunk (code to execute in the critical section).

**Output:** Boolean indicating success or failure of the tryLock operation.

**Steps:**

1. 1. A process attempts to execute a tryLock operation with a specified set of locks.
2. 2. If the tryLock succeeds, the process runs the associated code.
3. 3. If the tryLock fails due to contention, the process retries the operation.
4. 4. Each process helps others complete their critical sections to ensure progress.
5. 5. The process remains in a pending state until it has taken a fixed number of steps before revealing its priority.

**Core Operation:** `Expected steps for success = O(κ³L³T)`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `κ` | maximum contention on any lock | Higher values increase contention and expected steps. |
| `L` | maximum number of locks in a tryLock's set | More locks can increase complexity. |
| `T` | maximum steps taken by critical section | Longer critical sections can lead to higher wait times. |

## Complexity

- **Time:** O(κ²L²T) for each tryLock attempt; expected O(κ³L³T) steps for retries.
- **Space:** O(1) for each process.
- **In practice:** Performance can degrade with high contention and many locks.

## Implementation

```python
def randomized_wait_free_lock(locks: List[Lock], code: Callable[[], None]) -> bool:
    for attempt in range(MAX_ATTEMPTS):
        if try_lock(locks):
            code()
            return True
        help_others()
    return False
```

## Common Mistakes

- Not accounting for the maximum contention when designing the system.
- Failing to implement the helping mechanism effectively.
- Overlooking the impact of retries on performance.

## Use When

- Building concurrent data structures that require fine-grained locking.
- Implementing systems where fairness in lock acquisition is critical.
- Developing applications that may experience high contention on shared resources.

## Avoid When

- In scenarios where deterministic locking is required.
- When the overhead of retries is unacceptable for the application.

## Tradeoffs

**Strengths:**

- Ensures fairness in lock acquisition.
- Provides bounded time complexity under contention.
- Allows for high concurrency in shared resource access.

**Weaknesses:**

- Can introduce overhead due to retries.
- Performance may degrade with high contention.
- Not suitable for deterministic locking requirements.

**Compared To:**

- **vs Traditional Locking Mechanisms:** Use randomized locks for fairness and bounded time; traditional locks for deterministic behavior.

## Connects To

- Lock-Free Data Structures
- Optimistic Concurrency Control
- Backoff Algorithms
- Priority Scheduling

## Evidence (Papers)

- **Fast and fair randomized wait-free locks** - [DOI](https://doi.org/10.1007/s00446-024-00474-4)
