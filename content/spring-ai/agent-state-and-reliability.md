---
title: "Agent State & Reliability"
date: 2026-08-22T00:00:00+05:30
draft: false
description: "State, idempotency, timeouts, termination, recovery, testing and debugging."
tags: ["spring-ai", "genai", "interview-preparation"]
categories: ["Spring AI"]
interviewHandbook: true
---

State, idempotency, timeouts, termination, recovery, testing and debugging.

## Core Flow

```mermaid
flowchart LR
    R[Request] --> B[Load state and budgets] --> A[Next action]
    A --> D{Duplicate or over budget?}
    D -->|yes| S[Terminate or escalate]
    D -->|no| E[Idempotent execution] --> C[(Checkpoint)] --> A
```

## Revision Map

### What happens if the LLM generates invalid tool arguments?

Schema validation, deserialization failure, validation, retry/correction, controlled failure form a controlled end-to-end capability rather than a set of independent features.

- **Key areas:** Schema validation, deserialization failure, validation, retry/correction, controlled failure.
- **How it works:** Define what enters each boundary, what transformation or decision occurs, and what invariant must hold before the result moves forward.
- **Production:** In production, make limits and failure behavior explicit and measure quality, latency, security and cost across the complete path.

### What happens if a tool execution fails?

Use an end-to-end deadline and tracing to locate the failing segment before retrying.

- **Key areas:** Timeout, retry, fallback, error propagation, agent decision, user response.
- **How it works:** Protect capacity with bounded concurrency, backoff and circuit breaking, and make retries idempotent when side effects are possible.
- **Production:** Recover through a tested fallback or safe degradation, then verify Timeout, retry, fallback, error propagation, agent decision, user response and add the incident to regression coverage.

### How do you prevent an agent from entering an infinite tool-calling loop?

Max iterations, state tracking, duplicate detection, timeout, termination conditions form a controlled end-to-end capability rather than a set of independent features.

- **Key areas:** Max iterations, state tracking, duplicate detection, timeout, termination conditions.
- **How it works:** Define what enters each boundary, what transformation or decision occurs, and what invariant must hold before the result moves forward.
- **Production:** In production, make limits and failure behavior explicit and measure quality, latency, security and cost across the complete path.

### How do you prevent duplicate tool execution?

Idempotency keys, execution state, request IDs, deduplication form a controlled end-to-end capability rather than a set of independent features.

- **Key areas:** Idempotency keys, execution state, request IDs, deduplication.
- **How it works:** Define what enters each boundary, what transformation or decision occurs, and what invariant must hold before the result moves forward.
- **Production:** In production, make limits and failure behavior explicit and measure quality, latency, security and cost across the complete path.

### How do you handle tool timeouts and slow downstream APIs?

Use an end-to-end deadline and tracing to locate the failing segment before retrying.

- **Key areas:** Timeout, retry policy, circuit breaker, async execution, fallback.
- **How it works:** Protect capacity with bounded concurrency, backoff and circuit breaking, and make retries idempotent when side effects are possible.
- **Production:** Recover through a tested fallback or safe degradation, then verify Timeout, retry policy, circuit breaker, async execution, fallback and add the incident to regression coverage.

### How do you control agent token consumption and cost?

Token budgets, iteration limits, prompt compression, model routing, caching form a controlled end-to-end capability rather than a set of independent features.

- **Key areas:** Token budgets, iteration limits, prompt compression, model routing, caching.
- **How it works:** Define what enters each boundary, what transformation or decision occurs, and what invariant must hold before the result moves forward.
- **Production:** In production, make limits and failure behavior explicit and measure quality, latency, security and cost across the complete path.

### How would you design an Agent that uses RAG + REST APIs + database tools?

Separate the design into explicit components for Agent orchestration, retrieval, tools, authorization, state, error handling, with a clear contract and owner for each boundary.

- **Key areas:** Agent orchestration, retrieval, tools, authorization, state, error handling.
- **How it works:** Show how authenticated context, state and evidence move through the system, and where deterministic policy constrains model decisions.
- **Production:** Then explain bottlenecks, partial failures, recovery, scaling signals and the metrics that prove the complete task works.

### How do you maintain state during multi-step agent execution?

Agent state, conversation state, tool results, workflow state, persistence form a controlled end-to-end capability rather than a set of independent features.

- **Key areas:** Agent state, conversation state, tool results, workflow state, persistence.
- **How it works:** Define what enters each boundary, what transformation or decision occurs, and what invariant must hold before the result moves forward.
- **Production:** In production, make limits and failure behavior explicit and measure quality, latency, security and cost across the complete path.

### How do you observe and debug an Agent execution?

Trace ID, LLM calls, prompts, tool calls, latency, errors, token usage, decisions form a controlled end-to-end capability rather than a set of independent features.

- **Key areas:** Trace ID, LLM calls, prompts, tool calls, latency, errors, token usage, decisions.
- **How it works:** Define what enters each boundary, what transformation or decision occurs, and what invariant must hold before the result moves forward.
- **Production:** In production, make limits and failure behavior explicit and measure quality, latency, security and cost across the complete path.

### How do you test an AI Agent?

Build a versioned dataset of representative, edge and adversarial scenarios and define expected evidence or outcomes before testing.

- **Key areas:** Unit tests, mocked LLM, tool tests, integration tests, scenario tests, evaluation.
- **How it works:** Measure Unit tests, mocked LLM, tool tests, integration tests, scenario tests, evaluation separately so retrieval, generation and end-task failures are distinguishable.
- **Production:** Compare against a baseline, inspect failures rather than relying on one aggregate score, and retain every accepted defect as a regression case.

### How do you handle an LLM provider failure during agent execution?

Use an end-to-end deadline and tracing to locate the failing segment before retrying.

- **Key areas:** Timeout, fallback model, provider routing, state preservation, retry.
- **How it works:** Protect capacity with bounded concurrency, backoff and circuit breaking, and make retries idempotent when side effects are possible.
- **Production:** Recover through a tested fallback or safe degradation, then verify Timeout, fallback model, provider routing, state preservation, retry and add the incident to regression coverage.

### What is multi-agent architecture?

Separate the design into explicit components for Specialized agents, coordinator, delegation, communication, shared state, with a clear contract and owner for each boundary.

- **Key areas:** Specialized agents, coordinator, delegation, communication, shared state.
- **How it works:** Show how authenticated context, state and evidence move through the system, and where deterministic policy constrains model decisions.
- **Production:** Then explain bottlenecks, partial failures, recovery, scaling signals and the metrics that prove the complete task works.

### What happens when the LLM generates invalid tool arguments?

Validation/recovery form a controlled end-to-end capability rather than a set of independent features.

- **Key areas:** Validation/recovery.
- **How it works:** Define what enters each boundary, what transformation or decision occurs, and what invariant must hold before the result moves forward.
- **Production:** In production, make limits and failure behavior explicit and measure quality, latency, security and cost across the complete path.

### How do you prevent infinite Agent loops?

Iteration/time/token limits form a controlled end-to-end capability rather than a set of independent features.

- **Key areas:** Iteration/time/token limits.
- **How it works:** Define what enters each boundary, what transformation or decision occurs, and what invariant must hold before the result moves forward.
- **Production:** In production, make limits and failure behavior explicit and measure quality, latency, security and cost across the complete path.

## Interview Lens

Keep probabilistic interpretation separate from authorization, policy, transactions and recovery. Explain trade-offs with evidence: task quality, latency, resilience, security, operating cost and auditability.
