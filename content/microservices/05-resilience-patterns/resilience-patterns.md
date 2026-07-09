---
title: "Resilience Patterns"
date: 2026-07-03T15:00:00+00:00
draft: false
description: "Circuit breaker, bulkhead, retry, timeout, and fallback — the production resilience stack for microservices."
tags: ["microservices", "architecture-playbook", "distributed-systems", "resilience", "circuit-breaker", "bulkhead", "retry"]
categories: ["Microservices Architecture Playbook"]
shortTitle: "Resilience"
module: 5
moduleTitle: "Resilience Patterns"
sectionRef: "5.1"
weight: 501
playbookVersion: 3
aliases:
  - "/microservices/circuit-breaker-pattern/"
  - "/microservices/bulkhead-isolation-pattern/"
  - "/microservices/transient-fault-handling-timeouts-retries/"
---

## Executive Summary

Resilience patterns contain failure **before** it cascades across a microservices fleet. Production systems stack **bulkhead → timeout → circuit breaker → fallback → retry (reads only)** on every outbound dependency. Each pattern addresses a different failure mode: resource exhaustion, unbounded waits, sustained errors, degraded UX, and transient blips.

---

## Problem It Solves

Distributed calls fail more often than in-process calls. Without deliberate containment, one slow payment service can exhaust checkout thread pools, trigger retry storms, and cause a platform-wide outage.

---

## Where It Fits

Apply at **service boundaries** (HTTP/gRPC clients), **API gateway** egress, and **mesh sidecars** for platform-wide policy. Not needed for in-process monolith calls.

---

## Design Decisions

### Circuit Breaker

Closed/open/half-open state machine; trip on failure rate or slow-call ratio.

### Bulkhead

Isolated thread pools or semaphores per dependency.

### Retry

Exponential backoff with full jitter; retry budget; idempotent reads only.

### Timeout

`client_timeout > upstream_timeout > downstream_timeout` chain; propagate gRPC deadlines.

### Fallback

Reads: cache/static degrade. Writes: structured 503 + `Retry-After` — never fake success.

---

## Scalability

Bulkheads cap per-dependency concurrency — tune pool sizes to expected QPS and p99 latency.

---

## Reliability

Align timeouts so breakers observe failures before clients abandon. Export breaker state metrics.

---

## Security Considerations

Fallback responses must not leak internal errors or bypass authz checks.

---

## Observability

Metrics: `circuitbreaker_state`, `bulkhead_available_concurrent_calls`, retry counts, timeout histograms.

---

## Production Lessons

Test HALF-OPEN probe volume in staging. Separate read vs write fallback policies.

---

## Common Failures

| Flapping breaker | Threshold too aggressive | Increase wait window |
| Retry storm | Retries on writes | Idempotency keys only |
| Pool starvation | Shared pool | Bulkhead per dependency |

---

## Common Mistakes

Using circuit breaker without timeout; retrying non-idempotent POST; faking successful payment on OPEN state.

---

## Interview Questions

1. Walk through CLOSED → OPEN → HALF-OPEN recovery.
2. Why must breaker timeout be shorter than client timeout?
3. When is retry safe on a distributed write?
4. How does bulkhead differ from circuit breaker?
5. Design fallback for recommendations vs payments.

---

## Architect Notes

Canonical resilience page. Implementation libraries: Resilience4j, Envoy outlier detection, Istio destination rules.
