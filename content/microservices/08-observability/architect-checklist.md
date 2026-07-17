---
title: "Observability Architect Checklist"
date: 2026-07-17T10:00:00+00:00
draft: false
description: "Review instrumentation, telemetry platforms, security, reliability, cost, ownership, and operational readiness before production approval."
tags: ["microservices", "observability", "architecture-review", "production-readiness"]
categories: ["Microservices Architecture Playbook"]
shortTitle: "Architect Checklist"
module: 8
moduleTitle: "Observability"
sectionRef: "8.18"
weight: 818
playbookVersion: 3
---

## 1. Executive Summary

An observability design is production-ready only when its evidence remains trustworthy during the failure it must explain. Architecture review must cover the application contract, telemetry pipeline, data controls, platform reliability, cost boundaries, and operating ownership—not merely the presence of dashboards.

Use this checklist at service onboarding, production-readiness review, material architecture changes, backend migration, and post-incident review. Record **pass**, **risk accepted**, **remediation owner**, and **due date** for every applicable item. A checked box without evidence is not an approval.

---

## 2. Instrumentation

| Check | Evidence expected |
| :--- | :--- |
| RED metrics cover every synchronous service entry point and critical dependency | Rate, error, duration, timeout, and retry views by bounded operation and outcome |
| USE metrics cover infrastructure and constrained resources | CPU, memory, disk, network, queues, thread pools, connection pools, brokers, nodes, and pods as applicable |
| Trace context crosses HTTP and RPC boundaries | W3C trace context is injected, accepted, and preserved through gateways and proxies |
| Trace context crosses messaging boundaries | Producer, broker wait, consumer, retry, and dead-letter work retain causal links without unsafe baggage |
| Database and external calls produce useful spans | Bounded operation and dependency identity are present; credentials, raw values, and unsafe statements are absent |
| Logs are structured events | Stable event name, severity, service, environment, trace/span IDs, outcome, and error class are queryable fields |
| Deployment metadata is present on every signal | Version, region, environment, workload, and rollout identity support before/after comparisons |
| Telemetry semantics are consistent | Names, units, route templates, status classes, resources, and clocks follow a versioned contract |
| Business-critical outcomes are observable | Technical signals connect to bounded journey outcomes without exposing sensitive identifiers |

**Approval gate:** demonstrate one successful and one failed request across a representative synchronous and asynchronous path, then pivot from metric to trace to correlated log and deployment version.

---

## 3. Platform

| Check | Evidence expected |
| :--- | :--- |
| Collectors are highly available | Failure-domain-aware replicas, health checks, disruption controls, and capacity headroom |
| Backpressure has bounded behavior | Queue, memory, timeout, load-shedding, and drop behavior cannot exhaust or block the business service |
| Retry and buffering are intentional | Bounded retries with jitter, durable buffering where justified, and documented loss/duplication semantics |
| Storage retention matches signal value | Hot, warm, and archive tiers reflect investigation, legal, and cost requirements |
| Multi-region routing is defined | Normal routing, regional failure, residency constraints, and recovery behavior are documented |
| Tenants are isolated | Collection, storage, query, quotas, credentials, and administrative access enforce isolation |
| Disaster recovery is exercised | Configuration, dashboards, rules, metadata, and required evidence meet explicit RPO and RTO targets |
| Backend portability is understood | OpenTelemetry boundaries, vendor-specific dependencies, export paths, and exit costs are recorded |
| Configuration changes are controlled | Collector and rule changes are versioned, reviewed, progressively delivered, and reversible |

**Approval gate:** inject an exporter or backend failure and show that application traffic remains protected, pipeline degradation is detected, and recovery does not create an uncontrolled retry surge.

---

## 4. Security and Compliance

| Check | Evidence expected |
| :--- | :--- |
| Secrets never enter telemetry | Tests and redaction rules cover tokens, credentials, connection strings, headers, and payloads |
| PII is minimized and masked | Approved fields, tokenization, purpose, access, and deletion paths are documented |
| Access is least privilege | Role-based query and administration access is separated by environment, tenant, and data class |
| Data is encrypted | Authenticated transport and managed encryption at rest include keys and rotation ownership |
| Actions are auditable | Queries, exports, rule changes, privilege changes, and administrative access produce protected audit evidence |
| Retention complies with policy | Legal minimums, maximums, holds, deletion, and backup retention are enforced by data class |
| Residency is preserved | Collection, processing, storage, support access, replication, and recovery stay within approved boundaries |
| Baggage and attributes are governed | Allowlisted keys, size limits, redaction, and downstream propagation boundaries are explicit |

**Approval gate:** security and data owners review a representative metric, log, trace, profile, and event payload—not only the documented schema.

---

## 5. Reliability

| Check | Evidence expected |
| :--- | :--- |
| The observability platform has an SLO | Availability, ingestion success, freshness, query behavior, and alert delivery have measurable objectives |
| Dropped telemetry is monitored | SDK, agent, collector, transport, and backend drops are attributable by signal and source |
| Collector queues are monitored | Queue use, enqueue failures, send failures, memory pressure, restarts, and time-to-exhaustion are visible |
| Scrape failures are monitored | Target discovery, scrape errors, stale series, interval drift, and rule-evaluation failures have owners |
| Backend capacity is monitored | Ingestion, storage, indexing, query concurrency, compaction, quotas, and notification paths have forecasts |
| Failure modes are rehearsed | Collector loss, network partition, credential expiry, quota exhaustion, and regional loss appear in exercises |
| Alerts degrade safely | Delivery paths, deduplication, routing fallbacks, and inhibition cannot silently suppress broad incidents |
| Telemetry health is independent | A primary application failure does not erase the only evidence or use the same saturated dependency unchecked |

**Approval gate:** dashboards distinguish a healthy application from a blind telemetry pipeline; on-call can tell whether missing data means no traffic, instrumentation failure, or ingestion failure.

---

## 6. Cost and Capacity

| Check | Evidence expected |
| :--- | :--- |
| Cardinality is governed | Label allowlists, budgets, pre-production estimation, runtime detection, and owner attribution exist |
| Log volume has budgets | Volume by service and event, severity controls, duplicate-event detection, and debug expiry are visible |
| Trace sampling matches value | Baseline, error, latency, rare-path, and incident sampling balance evidence and cost |
| Retention uses tiers | Resolution and retention differ by signal, environment, sensitivity, and investigation value |
| Noisy services are detected | Sudden volume, span amplification, label growth, payload size, and query-cost changes route to owners |
| Showback or chargeback is possible | Shared platform cost is attributable to service, team, environment, signal, and retention class |
| Forecasts include failure traffic | Retry storms, incident sampling, deployments, seasonal peaks, and regional failover are capacity inputs |
| Optimization protects diagnostic value | Filtering and aggregation decisions state which investigations become impossible afterward |

**Approval gate:** owners can explain unit cost, top contributors, growth assumptions, enforced limits, and what happens when a service exceeds its budget.

---

## 7. Operations and Governance

| Check | Evidence expected |
| :--- | :--- |
| Every service has an owner | Catalog metadata connects service, repository, team, escalation, dependencies, and lifecycle state |
| Every production dashboard has an owner | Purpose, audience, freshness, source, and review date are recorded |
| Runbooks support decisions | Alerts link to validation, mitigation, rollback, escalation, and recovery verification steps |
| Alert routing is tested | Severity, ownership, schedules, fallbacks, deduplication, grouping, and maintenance behavior are exercised |
| Escalation crosses team boundaries | Dependency, platform, security, cloud, and vendor escalation paths have explicit triggers |
| Incidents improve telemetry | Reviews record evidence gaps, misleading signals, missed alerts, and owned corrective actions |
| Telemetry schemas are governed | Compatibility, semantic conventions, deprecation, versioning, and exception processes are defined |
| Dashboards and alerts follow service lifecycle | Creation, review, transfer, and retirement accompany ownership and deployment changes |
| Responders are trained | Teams practice RED-to-trace-to-USE-to-log diagnosis and understand platform failure modes |

**Approval gate:** conduct a scenario-based review with the actual service owner and on-call responder; platform documentation alone is insufficient.

---

## 8. Architecture Decision Record

Capture these decisions before approving the design:

1. Critical user journeys, SLIs, SLOs, owners, and escalation paths.
2. Required metrics, events, spans, logs, profiles, correlation fields, and semantic conventions.
3. SDK, automatic instrumentation, Collector topology, and deployment responsibility.
4. Sampling, filtering, aggregation, buffering, retry, backpressure, and loss policy.
5. Backend selection, regional routes, tenancy, retention, recovery, and exit strategy.
6. Data classification, redaction, access, encryption, residency, audit, and deletion controls.
7. Capacity assumptions, budgets, attribution, and over-limit behavior.
8. Platform SLOs, failure exercises, alert ownership, and review cadence.

Record alternatives and consequences. For example, direct-to-vendor export may accelerate access to proprietary features but increases application coupling; a Collector gateway improves governance but becomes a platform whose availability and capacity must be engineered.

---

## 9. Final Production Approval Questions

- Can responders identify what failed, where, why, who was affected, and which dependency contributed?
- Does telemetry remain available and trustworthy during application, network, collector, backend, and regional failures?
- Can the design bound runtime overhead, cardinality, volume, retention, sensitive-data exposure, and cost?
- Are missing or dropped signals detected before they invalidate incident conclusions?
- Do service, dashboard, alert, schema, platform, security, and cost decisions have accountable owners?
- Can the organization migrate backends without rewriting all application instrumentation?
- Has the design been validated through failure injection or an incident exercise?

If any answer is unknown, document the risk, owner, compensating control, and deadline. Unknown telemetry behavior during failure is an architecture risk, not a post-launch documentation task.

## Related Playbook Topics

- [Observability Architecture](/microservices/08-observability/observability/)
- [RED and USE Diagnostic Workflow](/microservices/08-observability/red-use-diagnostic-workflow/)
- [OpenTelemetry Architecture](/microservices/08-observability/opentelemetry-architecture/)
- [Alerting, SLOs, and Error Budgets](/microservices/08-observability/alerting-slos-and-error-budgets/)
- [Choosing an Observability Stack](/microservices/08-observability/choosing-observability-stack/)
- [Observability Maturity Model](/microservices/08-observability/observability-maturity-model/)
- [Telemetry FinOps](/microservices/08-observability/advanced/telemetry-finops/)
