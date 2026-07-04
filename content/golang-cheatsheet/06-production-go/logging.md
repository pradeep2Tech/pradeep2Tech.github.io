---
title: "Logging"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "Structured logging, log correlation, and production logging."
tags: ["golang", "golang-cheatsheet", "golang-handbook", "go", "interview"]
categories: ["Go Handbook"]
shortTitle: "Logging"
module: 6
moduleTitle: "Production Go"
sectionRef: "6.1"
weight: 601
interviewHandbook: true
---

## Quick Revision

- Use **structured logs** (slog, zap, zerolog) — key-value fields.
- Include `request_id`, `trace_id`, `service`, `level`.
- Log at boundaries; avoid duplicate log+return.

## Production Usage

- JSON logs for aggregation (ELK, Loki).
- Correlate with [Observability](/golang-cheatsheet/06-production-go/observability/) traces.

## Core Concepts

| Field | Purpose |
| :--- | :--- |
| `timestamp` | ISO8601 |
| `level` | info/warn/error |
| `msg` | Human-readable summary |
| `trace_id` / `span_id` | Correlation with OTel |
| `service` | Service name |
| `request_id` | Per-request correlation |

## Production Usage

Use `log/slog` (Go 1.21+) or zap/zerolog with JSON handler in production. Log at boundaries (HTTP in/out, errors) — not every function.

## Common Mistakes

- Logging PII or secrets.
- Duplicate logs on wrap-and-return paths.


---

## How do you trace a request ID through logs when middleware order is wrong?

### Short Answer
In production Go, the decisive factor is structured logs, metrics, traces, safe config, and graceful shutdown are baseline — for: How do you trace a request ID through logs when middleware order is wrong.

### Detailed Explanation
Correlate trace_id across logs/metrics; validate config at startup; drain on SIGTERM for: How do you trace a request ID through logs when middleware order is wrong.

### Internal Working
OTel SDK exports spans; Prometheus RED metrics; slog JSON logs — stack for: How do you trace a request ID through logs when middleware order is wrong.

### Production Notes
Run staticcheck/govulncheck; protect pprof admin ports for: How do you trace a request ID through logs when middleware order is wrong.

### Common Mistakes
Missing readiness vs liveness or logging secrets breaks production answers to: How do you trace a request ID through logs when middleware order is wrong.

### Follow-up Questions
What alert would fire first if: How do you trace a request ID through logs when middleware order is wrong regresses in prod?

---
## What fields belong in structured production logs for a REST API?

### Short Answer
The mechanism-first explanation is structured logs, metrics, traces, safe config, and graceful shutdown are baseline — for: What fields belong in structured production logs for a REST API.

### Detailed Explanation
Correlate trace_id across logs/metrics; validate config at startup; drain on SIGTERM for: What fields belong in structured production logs for a REST API.

### Internal Working
OTel SDK exports spans; Prometheus RED metrics; slog JSON logs — stack for: What fields belong in structured production logs for a REST API.

### Production Notes
Run staticcheck/govulncheck; protect pprof admin ports for: What fields belong in structured production logs for a REST API.

### Common Mistakes
Missing readiness vs liveness or logging secrets breaks production answers to: What fields belong in structured production logs for a REST API.

### Follow-up Questions
What alert would fire first if: What fields belong in structured production logs for a REST API regresses in prod?

---
<!-- interview-answers:end -->

---

## See Also

- [Previous: Memory Optimization](/golang-cheatsheet/05-performance/memory-optimization/)
- [Next: Configuration Management](/golang-cheatsheet/06-production-go/configuration-management/)
- [Go Handbook Index](/golang-cheatsheet/)
- [Top 150 Interview Questions](/golang-cheatsheet/08-interview-guide/top-150-interview-questions/)
