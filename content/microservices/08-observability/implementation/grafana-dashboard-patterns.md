---
title: "Grafana Dashboard Patterns"
date: 2026-07-17T10:00:00+00:00
draft: false
description: "Design layered Grafana dashboards from customer impact through service, resource, dependency, and telemetry-pipeline diagnosis."
tags: ["microservices", "grafana", "dashboards", "observability"]
categories: ["Microservices Architecture Playbook"]
shortTitle: "Grafana Dashboard Patterns"
module: 8
moduleTitle: "Observability"
sectionRef: "8.30"
weight: 830
playbookVersion: 3
---

## 1. Dashboard Hierarchy

Dashboards are navigation aids for decisions, not collections of every available metric.

| Level | Audience and panels |
| :--- | :--- |
| 1. Service portfolio | SLO status, error-budget burn, critical journeys, incidents, deployments |
| 2. Service overview | Rate, error ratio, P50/P95/P99, timeouts, retries, version, region, dependencies |
| 3. Resource diagnosis | CPU/throttling, memory/OOM, threads, pools, disk, network, Kafka lag |
| 4. Dependency view | Downstream RED, retries, circuit state, database latency, provider comparison |
| 5. Telemetry pipeline | Collector accepted/refused/dropped, queues, exporters, scrapes, storage/query health |

Each level links downward with the same time range, service, environment, region, and release context.

## 2. Panel Patterns

| Panel title | Query intent |
| :--- | :--- |
| Checkout SLO: current window | Good/valid events and budget remaining |
| Error-budget burn: fast and slow | Multi-window user-impact urgency |
| Request rate by outcome | Traffic shifts and lost traffic |
| Successful vs failed P95 duration | Avoid hiding fast failures in aggregate latency |
| Retry amplification by dependency | Attempts divided by logical operations |
| DB pool: used, waiting, limit | Separate pool saturation from database CPU |
| Collector queue time to exhaust | Queue depth relative to net growth rate |
| Deployments and configuration changes | Event annotations aligned to symptoms |

Use [recording rules](/microservices/08-observability/implementation/prometheus-recording-rules/) for stable repeated calculations rather than copying complex PromQL into every panel.

## 3. Design Principles

- Start with customer impact, then narrow to service, dependency, and resource causes.
- Put current value beside a meaningful historical or seasonal baseline.
- Show deployments and configuration changes on relevant time series.
- Separate success and failure latency; never average percentiles.
- Use bounded variables and route templates, not raw URLs or user identifiers.
- Link metric anomalies to representative traces and correlated logs.
- Link panels and alerts to decision-oriented runbooks.
- Give every dashboard an owner, review date, purpose, and retirement rule.
- Prefer a few diagnostic panels over a visually dense wall of graphs.

## 4. Production Hardening

Provision dashboards as reviewed, versioned artifacts when practical. Pin data-source identity, restrict editing, test variables with high service counts, and define behavior for no data, partial regions, stale series, and backend errors. Avoid queries that scan unbounded time or cardinality. Measure dashboard load time and query cost.

Annotate panels with units, aggregation, source, sampling, and known blind spots. A green panel with missing data must not resemble a healthy zero.

## 5. Validation

Replay known incidents or inject latency, errors, saturation, and Collector failure. Confirm operators can start at the portfolio, identify affected users/services, reach causal evidence, and open the correct runbook without constructing new queries. Review mobile/narrow rendering for tables, legends, and repeated panels before publishing.

