# Bayesian Inference with Synthetic Likelihoods

**This technique uses Bayesian inference to estimate model parameters and quantify uncertainties in simulations through synthetic likelihoods.**

**Category:** statistical_method  
**Maturity:** emerging

## How It Works

Bayesian inference with synthetic likelihoods integrates experimental data to estimate the posterior distribution of model parameters. It constructs synthetic likelihoods from simulation outputs, allowing for the incorporation of various observables. The Metropolis-Hastings algorithm is employed to sample from the posterior distribution, enabling the identification of optimal parameter sets and quantification of uncertainties in predictions.

## Algorithm

**Input:** Experimental observables including enthalpy of vaporization, molecular volume, radial distribution function, and hydrogen bonding patterns.

**Output:** Posterior distributions of model parameters (ε, σ, q) and quantified uncertainties in inference and validation observables.

**Steps:**

1. 1. Define the model parameters (ε, σ, q) for the water model.
2. 2. Collect experimental observables: enthalpy of vaporization, molecular volume, radial distribution function, and hydrogen bonding patterns.
3. 3. Construct synthetic likelihoods based on simulation outputs.
4. 4. Use Metropolis-Hastings sampling to explore the posterior distribution.
5. 5. Analyze the response of observables to parameter variations to identify limitations.
6. 6. Propose new parameter sets based on the mode and mean of the posterior distribution.
7. 7. Quantify uncertainties for both inference and validation observables.

**Core Operation:** `posterior ∝ likelihood × prior`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `ε` | > 2 kJ mol⁻¹ | Affects the strength of non-bonded interactions. |
| `σ` | around 0.317 nm | Influences the size of the interaction potential. |
| `q` | around -0.834 e | Determines the charge distribution in the model. |

## Complexity

- **Time:** O(n log n) for sampling, depending on the number of parameters and iterations.
- **Space:** O(n) for storing posterior samples.
- **In practice:** The computational overhead can be significant due to the Bayesian sampling process.

## Implementation

```python
def bayesian_inference(data: List[float]) -> Tuple[float, float, float]:
    # Step 1: Define model parameters
    epsilon, sigma, q = initialize_parameters()
    # Step 2: Collect observables
    observables = collect_observables(data)
    # Step 3: Construct synthetic likelihoods
    likelihoods = construct_likelihoods(observables)
    # Step 4: Sample from posterior using Metropolis-Hastings
    posterior_samples = metropolis_hastings(likelihoods)
    # Step 5: Analyze and propose new parameters
    new_params = analyze_samples(posterior_samples)
    return new_params
```

## Common Mistakes

- Neglecting to properly define prior distributions, leading to biased results.
- Using insufficient experimental data, which can result in poor parameter estimation.
- Failing to validate the model against independent datasets.

## Use When

- You need to improve the accuracy of molecular dynamics simulations involving water.
- You require a robust method for parameter estimation in force fields.
- You want to quantify uncertainties in simulation predictions.

## Avoid When

- You are working with systems where water representation is not critical.
- You need a quick, non-Bayesian parameter estimation method.
- You are limited by computational resources and cannot afford the overhead of Bayesian sampling.

## Tradeoffs

**Strengths:**

- Provides a rigorous framework for parameter estimation.
- Quantifies uncertainties in predictions, enhancing model reliability.
- Integrates multiple data sources for improved accuracy.

**Weaknesses:**

- Computationally intensive due to sampling methods.
- Requires careful selection of priors to avoid bias.
- May not be suitable for systems with limited data.

**Compared To:**

- **vs Frequentist methods:** Use Bayesian inference when uncertainty quantification is critical; frequentist methods may be faster but less informative.

## Connects To

- Markov Chain Monte Carlo (MCMC)
- Synthetic Likelihood Methods
- Bayesian Parameter Estimation
- Molecular Dynamics Simulations

## Evidence (Papers)

- **Bayesian three-point water models** - [DOI](https://doi.org/10.1038/s41524-025-01879-w)
