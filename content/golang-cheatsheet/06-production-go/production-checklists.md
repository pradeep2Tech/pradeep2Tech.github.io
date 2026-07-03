---
title: "Production Checklists"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "Pre-deploy checklists, CI gates, and production readiness."
tags: ["golang", "golang-cheatsheet", "golang-handbook", "go", "interview"]
categories: ["Go Handbook"]
shortTitle: "Checklists"
module: 6
moduleTitle: "Production Go"
sectionRef: "6.5"
weight: 605
ShowToc: true
interviewHandbook: true
---

## Checklists

- [ ] `go test -race ./...` in CI
- [ ] `staticcheck` / `govulncheck`
- [ ] pprof admin port not public
- [ ] Graceful shutdown tested
- [ ] Structured logging + metrics + traces
- [ ] Go version pinned in go.mod and image

## Checklists

### Pre-production

- [ ] `go test ./...` and `go test -race` on concurrent packages
- [ ] `staticcheck` / `govulncheck` clean
- [ ] Graceful shutdown tested under load
- [ ] pprof/metrics on private port
- [ ] Structured logging with correlation IDs
- [ ] GOMAXPROCS matches CPU limit
- [ ] Resource limits (memory, FD) sized with headroom

### Release

- [ ] Go version pinned in go.mod and container image
- [ ] Rollback plan documented
- [ ] Dashboards for goroutines, GC, latency, errors


---

## What is your first-hour checklist for a Go service latency regression after deploy?

### Short Answer
The architecturally sound response is structured logs, metrics, traces, safe config, and graceful shutdown are baseline — for: What is your first-hour checklist for a Go service latency regression after deploy.

### Detailed Explanation
Correlate trace_id across logs/metrics; validate config at startup; drain on SIGTERM for: What is your first-hour checklist for a Go service latency regression after deploy.

### Internal Working
OTel SDK exports spans; Prometheus RED metrics; slog JSON logs — stack for: What is your first-hour checklist for a Go service latency regression after deploy.

### Production Notes
Run staticcheck/govulncheck; protect pprof admin ports for: What is your first-hour checklist for a Go service latency regression after deploy.

### Common Mistakes
Missing readiness vs liveness or logging secrets breaks production answers to: What is your first-hour checklist for a Go service latency regression after deploy.

### Follow-up Questions
What alert would fire first if: What is your first-hour checklist for a Go service latency regression after deploy regresses in prod?

---
## What belongs on a Go service production readiness checklist?

### Short Answer
The senior-level answer is structured logs, metrics, traces, safe config, and graceful shutdown are baseline — for: What belongs on a Go service production readiness checklist.

### Detailed Explanation
Correlate trace_id across logs/metrics; validate config at startup; drain on SIGTERM for: What belongs on a Go service production readiness checklist.

### Internal Working
OTel SDK exports spans; Prometheus RED metrics; slog JSON logs — stack for: What belongs on a Go service production readiness checklist.

### Production Notes
Run staticcheck/govulncheck; protect pprof admin ports for: What belongs on a Go service production readiness checklist.

### Common Mistakes
Missing readiness vs liveness or logging secrets breaks production answers to: What belongs on a Go service production readiness checklist.

### Follow-up Questions
What alert would fire first if: What belongs on a Go service production readiness checklist regresses in prod?

---
## When do you run go vet, staticcheck, and -race in CI pipelines?

### Short Answer
In production Go, the decisive factor is bound concurrency, define goroutine exit, and choose mutex vs channel deliberately — for: When do you run go vet, staticcheck, and -race in CI pipelines.

### Detailed Explanation
Channels orchestrate; mutexes protect shared state; WaitGroup/ctx coordinate lifecycle — apply to: When do you run go vet, staticcheck, and -race in CI pipelines.

### Internal Working
Unbuffered channels rendezvous; buffered channels decouple until full; nil chans disable select cases — internals for: When do you run go vet, staticcheck, and -race in CI pipelines.

### Production Notes
Propagate context, add backpressure, and test with `-race` when implementing: When do you run go vet, staticcheck, and -race in CI pipelines.

### Common Mistakes
Leaked goroutines, send-on-closed-channel panics, and select spin loops are frequent failures in: When do you run go vet, staticcheck, and -race in CI pipelines.

### Follow-up Questions
How would you structure shutdown so: When do you run go vet, staticcheck, and -race in CI pipelines cannot hang the process?

---
<!-- interview-answers:end -->

---

## See Also

- [Previous: Graceful Shutdown](/golang-cheatsheet/06-production-go/graceful-shutdown/)
- [Next: Testing](/golang-cheatsheet/07-testing/testing/)
- [Go Handbook Index](/golang-cheatsheet/)
- [Top 150 Interview Questions](/golang-cheatsheet/08-interview-guide/top-150-interview-questions/)
