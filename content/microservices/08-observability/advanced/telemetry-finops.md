---
title: "Telemetry FinOps"
date: 2026-07-17T10:00:00+00:00
draft: false
description: "Govern observability cost through signal value, cardinality, volume, sampling, retention, attribution, and ownership."
tags: ["microservices", "observability", "finops", "telemetry-cost"]
categories: ["Microservices Architecture Playbook"]
shortTitle: "Telemetry FinOps"
module: 8
moduleTitle: "Observability"
sectionRef: "8.25"
weight: 825
playbookVersion: 3
---

## 1. Cost Is an Architecture Outcome

Observability cost follows instrumentation, dimensions, fidelity, retention, topology, query, and ownership decisions—not only vendor pricing. Cutting volume without understanding diagnostic value can make the platform cheaper and incidents longer.

## 2. Cost Dimensions

| Signal or platform | Primary drivers |
| :--- | :--- |
| Metrics | Active series, cardinality, sample rate, custom metrics, HA replicas |
| Logs | Bytes, indexed fields, parsing, hot/archive retention |
| Traces | Span volume, sampling, attributes, retention, service graph processing |
| Profiles | Sample frequency, stack depth, symbol storage, retention |
| RUM/synthetics | Sessions, events, replay, executions, locations |
| Platform | Query volume, users, network egress, cross-region transfer, replicas |

## 3. Value Model

Classify every major stream as required for paging, diagnosis, compliance, capacity planning, temporary investigation, or low-value/duplicate. Record the owner, decision supported, minimum fidelity, search horizon, and deletion conditions.

## 4. Architecture Controls

- Metric label allowlists and active-series budgets.
- Log-volume budgets, severity policy, duplicate detection, and debug expiry.
- Baseline plus error/latency-aware trace sampling and incident overrides.
- Signal-specific hot, warm, and archive retention.
- Noisy-service detection with showback or chargeback.
- Per-team budgets, ownership metadata, archive policy, and query-cost governance.
- Aggregation at the lowest layer that preserves required decisions.

Controls must fail predictably: reject or shed low-value data before consuming memory needed for critical signals, and notify the accountable owner before silent evidence loss.

## 5. Cost Anti-Patterns

- User, request, order, session, or unbounded tenant IDs as metric labels.
- Full debug logging in production without automatic expiry.
- 100% tracing without a justified workload and duration.
- Duplicate export to multiple vendors without a migration or resilience purpose.
- Unlimited retention or indexing every log field.
- Multiple agents collecting the same infrastructure metrics.
- Excessive synthetic frequency and abandoned dashboards or alerts.

## 6. Decision Framework

```text
What decision does this data support?
Who owns it?
How frequently is it used?
What is the minimum required fidelity?
How long must it remain searchable?
Can it be sampled, aggregated, or archived?
```

Apply the framework before onboarding and during quarterly cost reviews. A temporary exception must have an owner and expiry.

## 7. Operating Model

Platform teams expose usage, cost, quotas, and optimization controls; service teams own signal value and remediation; finance supports allocation; security and compliance constrain deletion and locality. Track cost per request, service, signal, and retained diagnostic outcome where feasible. Pair cost with SLO coverage and diagnosis effectiveness so optimization does not reward blindness.

See [Metrics Design](/microservices/08-observability/metrics-design/) for cardinality controls and the [Architect Checklist](/microservices/08-observability/architect-checklist/) for approval gates.
