---
title: "Observability"
date: 2026-07-03T15:00:00+00:00
draft: false
description: "Production observability architecture: correlated telemetry, diagnosis methods, instrumentation, SLOs, platform selection, and governance."
tags: ["microservices", "architecture-playbook", "distributed-systems"]
categories: ["Microservices Architecture Playbook"]
shortTitle: "Observability"
module: 8
moduleTitle: "Microservices Architecture Playbook"
sectionRef: "0"
weight: 800
playbookVersion: 3
---

# Observability

Design observability as a production subsystem: correlated evidence, portable instrumentation, reliable telemetry pipelines, actionable alerts, controlled cost, and explicit ownership.

## Start Here

1. [Observability Architecture](/microservices/08-observability/observability/) — why monitoring is insufficient and which standards architects must mandate
2. [Metrics, Logs, Traces, Profiles, and Events](/microservices/08-observability/metrics-logs-and-traces/) — choose the right signal and pivot between evidence types
3. [Correlation IDs and Context Propagation](/microservices/08-observability/correlation-and-context-propagation/) — preserve causality across HTTP, RPC, messaging, and asynchronous work

## Diagnose Service Failures

4. [RED Method](/microservices/08-observability/red-method/) — measure rate, errors, duration, tail latency, timeouts, and retry amplification
5. [USE Method](/microservices/08-observability/use-method/) — test utilization, saturation, and errors across constrained resources
6. [Golden Signals](/microservices/08-observability/golden-signals/) — combine service health and saturation without conflating RED and USE
7. [RED and USE Diagnostic Workflow](/microservices/08-observability/red-use-diagnostic-workflow/) — move from customer symptoms to validated resource causes

## Build the Telemetry Platform

8. [OpenTelemetry Architecture](/microservices/08-observability/opentelemetry-architecture/) — standardize instrumentation, Collector deployment, sampling, routing, backpressure, and backend portability
9. [Metrics Design](/microservices/08-observability/metrics-design/) — choose instruments, distributions, dimensions, exemplars, units, and cardinality controls
10. [Structured Logging](/microservices/08-observability/structured-logging/) — standardize event schemas, correlation, boundaries, retention, volume, and sensitive-data controls
11. [Distributed Tracing](/microservices/08-observability/distributed-tracing/) — trace synchronous and asynchronous paths with governed spans, propagation, sampling, retention, and correlation
12. [Alerting, SLOs, and Error Budgets](/microservices/08-observability/alerting-slos-and-error-budgets/) — translate user outcomes into objectives, budget policy, burn-rate alerts, and actionable routing
13. [Observability Tool Landscape](/microservices/08-observability/observability-tool-landscape/) — compare open-source, commercial, managed, and cloud-native capabilities without assuming one universal winner
14. [Choosing an Observability Stack](/microservices/08-observability/choosing-observability-stack/) — select a reference architecture using technical, ownership, compliance, residency, cost, and exit criteria
15. [Cloud Provider Observability](/microservices/08-observability/cloud-provider-observability/) — design Azure, AWS, and Google Cloud native-first, OpenTelemetry-first, and hybrid telemetry paths
16. [Production Failure Scenarios](/microservices/08-observability/production-failure-scenarios/) — diagnose application, platform, dependency, data, network, cache, and telemetry-pipeline incidents
17. [Observability Maturity Model](/microservices/08-observability/observability-maturity-model/) — progress from reactive debugging to standardized telemetry, SLO-driven operations, and governed advanced diagnosis
18. [Observability Architect Checklist](/microservices/08-observability/architect-checklist/) — review instrumentation, platform resilience, security, cost, ownership, and production-readiness evidence

## Advanced Observability

19. [Continuous Profiling](/microservices/08-observability/advanced/continuous-profiling/) — attribute CPU, allocation, heap, lock, and runtime effort to code paths
20. [eBPF-Based Observability](/microservices/08-observability/advanced/ebpf-observability/) — correlate kernel, network, process, and container evidence with application telemetry
21. [Frontend and Mobile RUM](/microservices/08-observability/advanced/frontend-mobile-rum/) — measure actual client performance and reliability under explicit privacy controls
22. [Synthetic Monitoring](/microservices/08-observability/advanced/synthetic-monitoring/) — validate controlled critical journeys from public and private locations
23. [Database Observability](/microservices/08-observability/advanced/database-observability/) — diagnose query, plan, pool, lock, replication, and storage behavior
24. [Service Topology and Dependency Intelligence](/microservices/08-observability/advanced/service-topology-dependency-intelligence/) — derive evidence-based runtime dependencies and blast radius
25. [Telemetry FinOps](/microservices/08-observability/advanced/telemetry-finops/) — govern signal cost using value, fidelity, attribution, retention, and ownership

## Implementation Guides

26. [Spring Boot OpenTelemetry](/microservices/08-observability/implementation/spring-boot-opentelemetry/) — instrument Java services with portable agent, domain-span, metric, and log-correlation patterns
27. [Go OpenTelemetry](/microservices/08-observability/implementation/golang-opentelemetry/) — configure providers, propagation, batch export, graceful shutdown, and domain telemetry
28. [Kubernetes Collector Patterns](/microservices/08-observability/implementation/kubernetes-collector-patterns/) — deploy agent, gateway, hybrid, and exceptional sidecar topologies safely
29. [Prometheus Recording Rules](/microservices/08-observability/implementation/prometheus-recording-rules/) — standardize reusable RED, retry, pool, and queue calculations
30. [Grafana Dashboard Patterns](/microservices/08-observability/implementation/grafana-dashboard-patterns/) — navigate from customer impact through service, dependency, resource, and pipeline evidence
31. [SLO Alert Examples](/microservices/08-observability/implementation/slo-alert-examples/) — implement and validate multi-window availability, latency, freshness, and outcome alerts

## Module Roadmap

| Area | Coverage |
| :--- | :--- |
| Foundations | Overview, telemetry signals, correlation and context propagation |
| Diagnosis | RED, USE, Golden Signals, combined workflow, production scenarios |
| Instrumentation | OpenTelemetry, metrics, structured logging, distributed tracing |
| Operations | Alerting, SLOs, error budgets, maturity, architect checklist |
| Platform decisions | Tool landscape, stack selection, cloud-provider architectures |
| Advanced capabilities | Profiles, eBPF, RUM, synthetics, databases, topology, telemetry FinOps |
| Implementation | Spring Boot, Go, Kubernetes Collectors, Prometheus, Grafana, SLO alerts |

Use the architect checklist as the production-readiness gate. The [Advanced Observability](/microservices/08-observability/advanced/) and [Implementation Guides](/microservices/08-observability/implementation/) branch indexes separate architecture decisions from practical configuration.

## Related Playbooks

- [System Design — Observability Fundamentals](/system-design/observability-fundamentals/) — concise interview-oriented treatment
- [Distributed Logging System](/system-design/distributed-logging-system/) — design of a log ingestion and search platform
- [Reliability Engineering](/microservices/10-production-playbook/reliability-engineering/) — SLO and operational reliability practices
- [Kubernetes — OpenTelemetry](/kubernetes-handbook/opentelemetry/) — cluster-oriented instrumentation
