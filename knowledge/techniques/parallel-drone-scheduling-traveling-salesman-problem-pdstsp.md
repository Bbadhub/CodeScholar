# Parallel Drone Scheduling Traveling Salesman Problem (PDSTSP)

**PDSTSP optimizes delivery routes for a fleet of drones and trucks operating in parallel to minimize completion time and environmental impact.**

**Category:** optimization_algorithm  
**Maturity:** emerging

## How It Works

PDSTSP formulates the delivery routing problem as a Mixed-Integer Linear Programming (MILP) model. It categorizes customers based on whether they can be served by drones, trucks, or both. The algorithm then optimizes the routes while considering constraints like vehicle capacities and operational parameters, ultimately minimizing total delivery time and assessing environmental and economic impacts.

## Algorithm

**Input:** Set of customer locations, demand weights, vehicle capacities, and operational parameters.

**Output:** Optimized delivery routes for drones and trucks, total completion time, and environmental/economic impact metrics.

**Steps:**

1. Define the set of nodes representing the depot and customer locations.
2. Categorize customers into those served by trucks and those that can be served by either drones or trucks.
3. Formulate the problem as a Mixed-Integer Linear Programming (MILP) model.
4. Set constraints for load capacities, travel distances, and operational parameters.
5. Optimize the delivery routes to minimize total completion time.
6. Perform sensitivity analysis on factors like delivery density and traffic conditions.

**Core Operation:** `output = optimized delivery routes for drones and trucks`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `drone_capacity` | 2.5 kg | Limits the weight of parcels that drones can deliver. |
| `truck_capacity` | 1300 kg | Limits the weight of parcels that trucks can deliver. |
| `annual_operation_days` | 300 | Affects the total number of operational days in a year. |
| `daily_operation_hours` | 8 | Affects the total operational hours available each day. |

## Complexity

- **Time:** Not stated
- **Space:** Not stated
- **In practice:** Performance may vary based on customer density and traffic conditions.

## Implementation

```python
def optimize_routes(customer_locations: List[Tuple[float, float]], demand_weights: List[float], vehicle_capacities: Dict[str, float]) -> Tuple[List[List[Tuple[float, float]]], float]:
    # Define nodes and categorize customers
    # Formulate MILP model
    # Set constraints
    # Optimize routes
    # Return optimized routes and metrics
    pass
```

## Common Mistakes

- Underestimating the impact of drone capacity on delivery options.
- Neglecting to account for regulatory restrictions on drone usage.
- Failing to perform sensitivity analysis on operational parameters.

## Use When

- Implementing last-mile delivery solutions in urban areas with high demand density.
- Seeking to reduce operational costs and environmental impacts in logistics.
- Integrating drone technology into existing delivery systems.

## Avoid When

- Delivering large, heavy parcels that exceed drone capacity.
- Operating in areas with strict regulations against drone usage.
- When delivery time windows are critical and cannot be accommodated.

## Tradeoffs

**Strengths:**

- Reduces total delivery time by optimizing routes.
- Lowers operational costs compared to traditional delivery systems.
- Minimizes environmental impact through efficient routing.

**Weaknesses:**

- Limited by drone capacity for heavier parcels.
- Complexity in regulatory compliance for drone operations.
- Potentially high initial setup costs for integrating drone technology.

**Compared To:**

- **vs Traditional Truck-Only Delivery Systems:** Use PDSTSP for mixed delivery scenarios to leverage both drones and trucks.

## Connects To

- Mixed-Integer Linear Programming (MILP)
- Last-Mile Delivery Optimization
- Drone Technology in Logistics
- Environmental Impact Assessment in Delivery Systems

## Evidence (Papers)

- **The Future of Last-Mile Delivery: Lifecycle Environmental and Economic Impacts of Drone-Truck Parallel Systems** [14 citations] - [DOI](https://doi.org/10.3390/drones9010054)
