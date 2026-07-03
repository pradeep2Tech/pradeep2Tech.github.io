---
title: "Observability"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Actuator, MDC, correlation IDs, metrics, tracing, Prometheus — production observability."
tags: ["spring-boot", "spring", "handbook", "interview"]
categories: ["Spring Boot Handbook"]
shortTitle: "Observability"
module: 8
moduleTitle: "Observability"
sectionRef: "8.1"
ShowToc: true
interviewHandbook: true
aliases:
  - actuator-ref
  - observability-ref
---

## Correlation IDs and MDC?

**Difficulty:** Medium  
**Expected Answer Time:** 1 min

### Short Answer

Propagate unique request ID in header; store in SLF4J MDC so every log line includes `traceId`/`correlationId`.

### Detailed Explanation

Servlet `Filter` or WebMvc `HandlerInterceptor` reads/generates ID, puts in MDC, adds to response header. Clear MDC in `finally` — thread pool reuse leaks context without clear.

### Internal Working

Micrometer Tracing (Boot 3) bridges to OpenTelemetry; trace ID aligns with MDC when configured.

### Production Notes

Structured JSON logging in prod. Pass correlation ID to `RestTemplate`/`WebClient` downstream headers.

### Common Mistakes

Forgetting MDC clear in async — wrong ID on next request. Logging PII in MDC.

### Follow-up Questions

- W3C traceparent?
- How does Micrometer Tracing work?

---
## Actuator endpoints and K8s probes?

**Difficulty:** Medium  
**Expected Answer Time:** 1 min

### Short Answer

Actuator exposes `health`, `metrics`, `prometheus`; enable probes via `management.endpoint.health.probes.enabled=true` for separate liveness/readiness.

### Detailed Explanation

Liveness: JVM up — restart pod if fails. Readiness: DB/broker checks — remove from service endpoints. Expose only needed endpoints; secure `/actuator` with Security or network policy.

### Internal Working

Custom `HealthIndicator` beans contribute to composite health.

### Production Notes

Don't put slow external checks on liveness — causes restart loops. Readiness for dependency failures.

### Common Mistakes

Exposing `env` and `beans` publicly.

### Follow-up Questions

- Custom health groups?
- Startup probe for slow Boot apps?

---
## Metrics and distributed tracing?

**Difficulty:** Hard  
**Expected Answer Time:** 3 min

### Short Answer

Micrometer registers meters → Prometheus scrape or OTLP export. Tracing: spans across HTTP, JDBC, Kafka with trace context propagation.

### Detailed Explanation

RED metrics: Rate, Errors, Duration per endpoint. USE for resources. `@Timed` or `Observation` API (Boot 3). Grafana dashboards + alerts on SLO burn rate.

### Internal Working

`MeterRegistry` auto-configured; `ObservationRegistry` unifies metrics + traces.

### Production Notes

Sample traces in prod (tail sampling). Cardinality control on tags — don't tag userId on metrics.

### Common Mistakes

High-cardinality labels crashing Prometheus. No tracing on async without context propagation.

### Follow-up Questions

- Which metrics to alert on?
- OpenTelemetry agent vs starter?

---

## See Also

- [Previous: Messaging](/spring-boot/messaging-events/)
- [Next: Production](/spring-boot/production-deployment/)
- [Production](/spring-boot/production-deployment/)
- [100+ Interview Questions](/spring-boot/interview-questions/)
- [Spring Boot Handbook Index](/spring-boot/)
- [Java Engineering](/java-engineering/)
- [Microservices Playbook](/microservices/) — Saga, Outbox, CQRS, API Gateway
- [Kafka Handbook](/kafka-handbook/)
- [Security Architecture](/security-architecture/)
