# Evolutionary Surrogate-assisted Prescription (ESP)

**ESP optimizes land-use policies by using a surrogate model to predict emissions and an evolutionary algorithm to explore solutions.**

**Category:** optimization_algorithm  
**Maturity:** emerging

## How It Works

ESP begins by collecting historical land-use data and training a surrogate model to predict emissions based on this data. It then initializes a population of candidate land-use policies represented as neural networks. Each candidate is evaluated using the surrogate model, and the best-performing candidates are selected for further evolution through crossover and mutation. This iterative process continues until a set of optimal policies is identified, represented as a Pareto front balancing emissions and land-use change.

## Algorithm

**Input:** Historical land-use data (latitude, longitude, area, year, current land use percentages)

**Output:** A Pareto front of optimal land-use policies minimizing emissions and land-use change

**Steps:**

1. 1. Collect historical data on land-use changes and associated emissions.
2. 2. Train a surrogate model to predict emissions based on land-use changes.
3. 3. Initialize a population of candidate policies (neural networks).
4. 4. Evaluate each candidate using the surrogate model to predict outcomes.
5. 5. Select the best-performing candidates based on their predicted outcomes.
6. 6. Apply crossover and mutation to generate new candidates.
7. 7. Repeat steps 4-6 until convergence or a stopping criterion is met.

**Core Operation:** `output = surrogate_model(land_use_changes)`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `population_size` | 100 | Larger populations may explore more solutions but increase computation time. |
| `mutation_rate` | 0.01 | Higher rates introduce more variability, potentially leading to better solutions. |
| `crossover_rate` | 0.7 | Affects the balance between exploration and exploitation in the search process. |
| `learning_rate` | 0.001 | Impacts the speed of convergence of the surrogate model. |

## Complexity

- **Time:** Not explicitly stated, but generally depends on population size and number of generations.
- **Space:** Not explicitly stated, but involves storage for population and surrogate model.
- **In practice:** Performance may vary based on the complexity of the surrogate model and the size of the dataset.

## Implementation

```python
def esp_algorithm(historical_data: List[Tuple[float, float, float, int, float]]) -> List[Policy]:
    surrogate_model = train_surrogate(historical_data)
    population = initialize_population(size=100)
    while not convergence_criteria_met():
        evaluations = evaluate_population(population, surrogate_model)
        selected = select_best_candidates(evaluations)
        population = generate_new_candidates(selected)
    return generate_pareto_front(population)
```

## Common Mistakes

- Neglecting to properly train the surrogate model, leading to inaccurate predictions.
- Using inappropriate parameters for population size or mutation rate.
- Failing to adequately evaluate the trade-offs represented in the Pareto front.

## Use When

- You need to optimize land-use decisions to minimize carbon emissions.
- You want to explore trade-offs between environmental impact and land-use change.
- You are working on climate change mitigation strategies.

## Avoid When

- The land-use decisions are highly localized and require fine-grained data.
- You need real-time decision-making without the ability to train models.
- The problem does not involve multiple conflicting objectives.

## Tradeoffs

**Strengths:**

- Effectively balances multiple conflicting objectives.
- Utilizes historical data to improve decision-making.
- Generates a diverse set of optimal solutions.

**Weaknesses:**

- May require significant computational resources for large datasets.
- Performance heavily relies on the quality of the surrogate model.
- Not suitable for real-time decision-making scenarios.

**Compared To:**

- **vs Multi-objective linear programming:** Use ESP when historical data is available and multiple objectives need balancing.
- **vs Causal machine learning approaches:** ESP is preferable for exploratory optimization in land-use scenarios.

## Connects To

- Multi-objective optimization
- Neuroevolution
- Surrogate modeling
- Land-use change modeling

## Evidence (Papers)

- **Discovering effective policies for land-use planning with neuroevolution** [1 citations] - [DOI](https://doi.org/10.1017/eds.2025.18)
