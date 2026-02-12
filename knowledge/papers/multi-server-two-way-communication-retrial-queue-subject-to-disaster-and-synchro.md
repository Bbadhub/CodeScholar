# Multi-Server Two-Way Communication Retrial Queue Subject to Disaster and Synchronous Working Vacation

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3390/a18010024` |
| Full Paper | [https://doi.org/10.3390/a18010024](https://doi.org/10.3390/a18010024) |
| Source | [https://journalclub.io/episodes/multi-server-two-way-communication-retrial-queue-subject-to-disaster-and-synchronous-working-vacation](https://journalclub.io/episodes/multi-server-two-way-communication-retrial-queue-subject-to-disaster-and-synchronous-working-vacation) |
| Year | 2026 |
| Citations | 0 |
| Authors |  |
| Paper ID | `5472fb7a-8727-498e-99ec-4d6003a10ead` |

## Classification

- **Problem Type:** queueing theory, retrial queues
- **Domain:** Optimization & Operations Research
- **Sub-domain:** Queueing Theory
- **Technique:** Multi-Server Two-Way Communication Retrial Queue
- **Technique Category:** statistical_method
- **Type:** novel

## Summary

This paper presents a multi-server retrial queue model that incorporates two-way communication, synchronous working vacations, and disaster scenarios. Engineers should care because this model addresses the complexities of real-world telephony systems, where customer behavior and server availability significantly impact service efficiency.

## Key Contribution

**The introduction of a multi-server, two-way communication retrial queue model that accounts for synchronous working vacations and disasters, along with explicit performance indices derived using the matrix geometric method.**

## Problem

The need to manage retrial phenomena in telephony systems where customers may hang up or retry service, leading to congestion and inefficiencies.

## Method

**Approach:** The method models a multi-server queue where incoming calls may enter a retrial queue if all servers are busy. The servers can also make outgoing calls during idle times, and the model accounts for disasters that can cause server failures and require repairs.

**Algorithm:**

1. 1. Define the state space for the system including incoming and outgoing calls, retrial queue size, and server states.
2. 2. Establish the transition rates for incoming calls, outgoing calls, and server states.
3. 3. Use the matrix geometric method to derive the stationary distribution of the system.
4. 4. Calculate performance indices based on the stationary probabilities.
5. 5. Perform numerical experiments to validate the analytical results.

**Input:** Parameters: arrival rate (λ), service rates (µ1, µ2, µw), retrial rate (ν), disaster rate (δ), repair rate (γ), vacation rate (η), probabilities of joining retrial queue (bb, bv, br), number of servers (c).

**Output:** Performance indices including average size of retrial queue, average time spent in retrial queue, server utilization, and probabilities of server states.

**Key Parameters:**

- `λ: 4 (arrival rate)`
- `µ1: 3 (service rate for incoming calls)`
- `µ2: 1.5 (service rate for outgoing calls)`
- `µw: 1 (service rate during working vacation)`
- `ν: 10 (retrial rate)`
- `δ: 0.1 (disaster rate)`
- `γ: 1 (repair rate)`
- `η: 0.3 (vacation rate)`
- `bb: 0.8 (probability of joining retrial queue during busy period)`
- `bv: 0.6 (probability during vacation)`
- `br: 0.6 (probability during repair)`
- `c: 4 (number of main servers)`

**Complexity:** Not stated.

## Benchmarks

**Tested on:** Numerical experiments conducted in MATLAB R2022a.

**Results:**

- Average size of retrial queue: O
- Average time spent in retrial queue: W
- Probability that servers are on vacation: Pv
- Probability that servers are busy: Pb
- Probability that servers are being repaired: Pr
- Utilization of the server: U

**Compared against:** Standard single-server retrial queue models.

**Improvement:** The model shows improved average time spent in the buffer compared to standard FIFO queues.

## Implementation Guide

**Data Structures:** State transition matrix for the Markov process., Matrices for performance indices calculations.

**Dependencies:** MATLAB for numerical simulations., Matrix computation libraries.

**Core Operation:**

```python
Define state space; calculate transition rates; derive stationary distribution using matrix geometric method.
```

**Watch Out For:**

- Ensure all stochastic processes are mutually independent.
- Validate ergodicity conditions before applying the model.
- Carefully tune parameters to avoid instability in the queue.

## Use This When

- Modeling telephony systems with high retry rates.
- Designing call centers that require proactive customer follow-up.
- Analyzing systems where server availability fluctuates due to disasters.

## Don't Use When

- The system has a very low retry rate.
- The application does not involve two-way communication.
- The system is not subject to disasters or server failures.

## Key Concepts

retrial queues, two-way communication, synchronous working vacation, disaster recovery, matrix geometric method, performance indices

## Connects To

- Single-server retrial queue models
- Queueing theory in telecommunications
- Matrix geometric methods in stochastic processes

## Prerequisites

- Basic understanding of queueing theory.
- Familiarity with Markov processes.
- Knowledge of matrix operations and geometric methods.

## Limitations

- Assumes exponential service and arrival distributions.
- May not accurately model systems with highly variable service times.
- Complexity increases significantly with the number of servers.

## Open Questions

- How can this model be adapted for non-exponential service times?
- What are the implications of varying the number of standby servers?

## Abstract

Traditional FIFO (First-In-First-Out) are ill-suited for telephony because customers do not passively wait in line. They either hang-up and redial, or they give up entirely. This leads to something called a “retrial phenomenon”, where unserved customers retry the system in an attempt to obtain service. Sometimes they do this immediately, sometimes they do it after a delay. If this isn’t managed properly, retrial traffic can become self-perpetuating. It causes waves of congestion that overload the system, creating a kind of cyclic doom spiral that takes everything down. To make it more complicated, servers are not merely passive responders to inbound requests; they also initiate outbound calls. Many helplines proactively reach out to clients (for follow-up care, appointment reminders, or callbacks). This means that server availability is not solely determined by inbound traffic but also by internally
