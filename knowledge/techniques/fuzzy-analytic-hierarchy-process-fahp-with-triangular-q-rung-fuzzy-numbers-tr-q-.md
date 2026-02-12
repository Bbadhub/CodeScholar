# Fuzzy Analytic Hierarchy Process (FAHP) with Triangular q-rung Fuzzy Numbers (TR-q-ROFNS)

**FAHP with TR-q-ROFNS is a method for ranking alternatives based on fuzzy evaluations of subjective criteria.**

**Category:** decision_making  
**Maturity:** proven

## How It Works

FAHP utilizes fuzzy logic to handle uncertainty in decision-making. It employs triangular q-rung fuzzy numbers to represent the fuzziness in pairwise comparisons. The method involves calculating fuzzy weights for each criterion, aggregating these weights, and defuzzifying the results to obtain crisp scores for ranking alternatives.

## Algorithm

**Input:** Criteria and alternatives defined in terms of triangular q-rung fuzzy numbers.

**Output:** Ranked list of alternatives based on fuzzy evaluations.

**Steps:**

1. Define the decision criteria and alternatives.
2. Construct the pairwise comparison matrix using TR-q-ROFNS.
3. Calculate the fuzzy weights for each criterion.
4. Aggregate the fuzzy weights to rank the alternatives.
5. Defuzzify the aggregated fuzzy scores to obtain crisp values.
6. Select the alternative with the highest score.

**Core Operation:** `output = defuzzify(aggregate(fuzzy_weights))`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `q` | 1 to 5 | Increases the degree of fuzziness in evaluations. |
| `weights` | normalized to sum to 1 | Determines the influence of each criterion in the final ranking. |

## Complexity

- **Time:** O(n²)
- **Space:** O(n)
- **In practice:** Performance is manageable for moderate-sized decision problems.

## Implementation

```python
def fuzzy_ahp(criteria: List[str], alternatives: List[str], comparisons: List[List[Tuple[float, float]]]) -> List[str]:
    # Step 1: Define criteria and alternatives
    # Step 2: Construct pairwise comparison matrix using TR-q-ROFNS
    # Step 3: Calculate fuzzy weights
    # Step 4: Aggregate fuzzy weights
    # Step 5: Defuzzify scores
    # Step 6: Return ranked alternatives
    return ranked_alternatives
```

## Common Mistakes

- Neglecting to normalize the weights derived from pairwise comparisons.
- Using inappropriate fuzzy numbers that do not accurately represent the decision context.
- Failing to properly defuzzify the aggregated scores.

## Use When

- You need to evaluate options with subjective criteria.
- The decision-making process involves uncertainty.
- You want to incorporate human-like reasoning into decision models.

## Avoid When

- The problem can be solved with clear binary decisions.
- Data is strictly quantitative without ambiguity.
- The decision criteria are not conflicting.

## Tradeoffs

**Strengths:**

- Handles uncertainty and subjectivity effectively.
- Incorporates human-like reasoning into decision-making.
- Improves decision accuracy over traditional methods.

**Weaknesses:**

- Can be computationally intensive for large datasets.
- Requires careful selection of fuzzy parameters.
- May lead to ambiguity if not properly defined.

**Compared To:**

- **vs Traditional AHP:** Use FAHP when dealing with uncertainty and subjective criteria.

## Connects To

- Analytic Hierarchy Process (AHP)
- Fuzzy Logic
- Multi-Criteria Decision Analysis (MCDA)
- Triangular Fuzzy Numbers

## Evidence (Papers)

- **The technique of fuzzy analytic hierarchy process (FAHP) based on the triangular q-rung fuzzy numbers (TR-q-ROFNS) with applications in best African coffee brand selection** [2 citations] - [DOI](https://doi.org/10.7717/peerj-cs.2555)
