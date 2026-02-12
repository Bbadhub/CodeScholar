# Tentative Operations

**Tentative operations enable real-time collaborative editing of geospatial data while minimizing concurrency issues.**

**Category:** conflict_resolution  
**Maturity:** emerging

## How It Works

Tentative operations leverage Conflict-free Replicated Data Types (CRDTs) to allow users to edit local copies of geospatial data. When a user makes an edit, a new CRDT element is generated and inserted into their local data structure. This element is then transmitted to other users, who integrate it into their own local copies while resolving any conflicts using predefined strategies.

## Algorithm

**Input:** Geospatial data in the form of linear geometries represented as ordered sets of points.

**Output:** A synchronized state of geospatial data across multiple users' local copies, conflict-free.

**Steps:**

1. 1. User performs an edit on their local copy of the geospatial data.
2. 2. Generate a new CRDT element representing the edit.
3. 3. Insert the new element into the local CRDT data structure.
4. 4. Transmit the new element to all other sites.
5. 5. Each site integrates the new element into their local data structure based on the originLeft parameter.
6. 6. Resolve any conflicts using the CRDT's conflict resolution strategies.

**Core Operation:** `output = synchronized_state(local_copies) after conflict_resolution`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `max_concurrent_users` | 10 | Limits the number of simultaneous edits, affecting performance. |
| `update_frequency` | 100ms | Determines how often updates are sent, impacting latency. |
| `geometry_type` | linear | Specifies the type of geospatial data being edited. |

## Complexity

- **Time:** Not stated
- **Space:** Not stated
- **In practice:** Performance is optimized for real-time collaboration, but specific complexities are not detailed.

## Implementation

```python
def tentative_operations_edit(local_data: List[Point], edit: Edit) -> None:
    new_element = generate_crdt_element(edit)
    local_data.append(new_element)
    transmit_to_other_sites(new_element)
    for site in other_sites:
        site.integrate(new_element)
        resolve_conflicts(site.local_data)
```

## Common Mistakes

- Failing to properly handle conflict resolution, leading to data inconsistencies.
- Not considering the impact of high concurrency on performance.
- Neglecting to test with real-time data updates, resulting in unexpected behavior.

## Use When

- Building applications for real-time collaborative mapping.
- Developing systems for emergency response requiring live data updates.
- Creating tools for crowdsourced geographic information systems.

## Avoid When

- Working with static geospatial data that does not require real-time updates.
- In scenarios with very low user concurrency (e.g., single-user applications).

## Tradeoffs

**Strengths:**

- Enables real-time collaboration with minimal latency.
- Reduces conflict resolution time compared to traditional methods.
- Supports multiple concurrent users effectively.

**Weaknesses:**

- Complexity in implementing CRDTs and conflict resolution strategies.
- Potential performance issues with very high user concurrency.
- May not be suitable for applications with static data.

**Compared To:**

- **vs Traditional Optimistic Concurrency Control:** Use Tentative Operations for real-time collaboration; use traditional methods for simpler, static scenarios.

## Connects To

- Conflict-free Replicated Data Types (CRDTs)
- Operational Transformation
- Real-time Data Synchronization
- Collaborative Editing Systems

## Evidence (Papers)

- **Real-Time Co-Editing of Geographic Features** - [DOI](https://doi.org/10.3390/ijgi13120441)
