---
title: "Configuration Management"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "Environment variables, configuration loading, and secrets management."
tags: ["golang", "golang-cheatsheet", "golang-handbook", "go", "interview"]
categories: ["Go Handbook"]
shortTitle: "Config"
module: 6
moduleTitle: "Production Go"
sectionRef: "6.2"
weight: 602
interviewHandbook: true
---

## Quick Revision

- **12-factor:** config in environment.
- Load into typed struct; validate at startup.
- Secrets from vault/K8s secrets — never commit.

## Common Mistakes

- Silent defaults for missing required config.

## Core Concepts

| Source | Precedence (typical) |
| :--- | :--- |
| CLI flags | Highest |
| Environment variables | High |
| Config file | Medium |
| Defaults in code | Lowest |

## Production Usage

Validate required config at startup — fail fast. Use `os.LookupEnv` for optional values. Secrets from K8s secrets / vault, not ConfigMaps in plain text.

## Checklists

- [ ] No secrets in repo or images
- [ ] Config struct validated with tags or custom Validate()


---

## What is the recommended pattern for loading config from env versus files?

### Short Answer
The mechanism-first explanation is structured logs, metrics, traces, safe config, and graceful shutdown are baseline — for: What is the recommended pattern for loading config from env versus files.

### Detailed Explanation
Correlate trace_id across logs/metrics; validate config at startup; drain on SIGTERM for: What is the recommended pattern for loading config from env versus files.

### Internal Working
OTel SDK exports spans; Prometheus RED metrics; slog JSON logs — stack for: What is the recommended pattern for loading config from env versus files.

### Production Notes
Run staticcheck/govulncheck; protect pprof admin ports for: What is the recommended pattern for loading config from env versus files.

### Common Mistakes
Missing readiness vs liveness or logging secrets breaks production answers to: What is the recommended pattern for loading config from env versus files.

### Follow-up Questions
What alert would fire first if: What is the recommended pattern for loading config from env versus files regresses in prod?

---
## How do you avoid committing secrets while using environment variables?

### Short Answer
The senior-level answer is structured logs, metrics, traces, safe config, and graceful shutdown are baseline — for: How do you avoid committing secrets while using environment variables.

### Detailed Explanation
Correlate trace_id across logs/metrics; validate config at startup; drain on SIGTERM for: How do you avoid committing secrets while using environment variables.

### Internal Working
OTel SDK exports spans; Prometheus RED metrics; slog JSON logs — stack for: How do you avoid committing secrets while using environment variables.

### Production Notes
Run staticcheck/govulncheck; protect pprof admin ports for: How do you avoid committing secrets while using environment variables.

### Common Mistakes
Missing readiness vs liveness or logging secrets breaks production answers to: How do you avoid committing secrets while using environment variables.

### Follow-up Questions
What alert would fire first if: How do you avoid committing secrets while using environment variables regresses in prod?

---
<!-- interview-answers:end -->

---

## See Also

- [Previous: Logging](/golang-cheatsheet/06-production-go/logging/)
- [Next: Observability](/golang-cheatsheet/06-production-go/observability/)
- [Go Handbook Index](/golang-cheatsheet/)
- [Top 150 Interview Questions](/golang-cheatsheet/08-interview-guide/top-150-interview-questions/)
