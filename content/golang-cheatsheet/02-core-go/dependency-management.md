---
title: "Dependency Management"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "go get, versioning, minimal version selection, and vendoring."
tags: ["golang", "golang-cheatsheet", "golang-handbook", "go", "interview"]
categories: ["Go Handbook"]
shortTitle: "Dependencies"
module: 2
moduleTitle: "Core Go"
sectionRef: "2.5"
weight: 205
cheatSheet: true
interviewHandbook: true
aliases:
  - "/golang-cheatsheet/dependency-management/"
---

## At a Glance

- Go uses **Minimal Version Selection (MVS)** — `go.mod` lists minimum versions; build picks lowest compatible set. Upgrade with **`go get pkg@version`**.

---

## Reference Tables

| Command | Action |
| :--- | :--- |
| `go get pkg@latest` | Upgrade to latest |
| `go get pkg@v1.2.3` | Pin version |
| `go get pkg@none` | Remove dependency |
| `go mod vendor` | Copy deps to `vendor/` |
| `go list -m all` | Resolved module list |

```bash
go get -u ./...
go get github.com/foo/bar@v1.5.0
go mod tidy   # add missing, drop unused
```

---

## Snippets

```bash
# private module
GOPRIVATE=github.com/myorg/*
go env -w GOPRIVATE=github.com/myorg/*
```

---

## Internals & Gotchas

- `go get -u` in library repos — bump carefully; consumers resolve MVS.
- Vendoring: `-mod=vendor` in CI for hermetic builds.
- Pseudo-versions for untagged commits: `v0.0.0-20240101120000-abcdef`.

---

## Production Notes

- Apply patterns from this page in code review and incident postmortems.

---

## How do you handle private module fetch in CI without GOPATH hacks?

### Short Answer
go.mod defines module path and requirements; MVS picks minimum compatible versions; commit go.sum for reproducibility.

### Detailed Explanation
Modules replaced GOPATH for dependency management. replace is for local dev; retract withdraws bad versions. Vendoring supports hermetic CI.

### Internal Working
The module graph is resolved with minimal version selection — not latest-wins. Major versions v2+ require /v2 in module path.

### Production Notes
Pin Go toolchain in go.mod and Docker. Use GOPRIVATE for internal modules. Run go mod verify in CI.

### Common Mistakes
Committing replace directives meant for local forks. Using go get -u blindly in libraries. Omitting go.sum from VCS.

### Follow-up Questions
How does MVS behave when two modules require different minimum versions of the same dependency?

---
## How does Minimal Version Selection resolve conflicting module requirements?

### Short Answer
Prefer clear ownership: channels for orchestration, mutex for shared state; always bound concurrency and propagate context.

### Detailed Explanation
Go encourages sharing memory by communicating, but mutexes are often simpler for caches and counters. Combine WaitGroup, context, and buffered channels for backpressure.

### Internal Working
Unbuffered channels synchronize; buffered channels decouple up to capacity. nil channels block forever in select — useful for disabling cases.

### Production Notes
Define goroutine lifecycle: who starts, who stops, how errors return. Implement graceful shutdown with context cancel and server drain.

### Common Mistakes
Leaked goroutines blocked on channels. Closing channels from the receiver side. select+default spin loops.

### Follow-up Questions
When would you choose errgroup with context over a raw WaitGroup?

---
## When is vendoring required for reproducible builds?

### Short Answer
go.mod defines module path and requirements; MVS picks minimum compatible versions; commit go.sum for reproducibility.

### Detailed Explanation
Modules replaced GOPATH for dependency management. replace is for local dev; retract withdraws bad versions. Vendoring supports hermetic CI.

### Internal Working
The module graph is resolved with minimal version selection — not latest-wins. Major versions v2+ require /v2 in module path.

### Production Notes
Pin Go toolchain in go.mod and Docker. Use GOPRIVATE for internal modules. Run go mod verify in CI.

### Common Mistakes
Committing replace directives meant for local forks. Using go get -u blindly in libraries. Omitting go.sum from VCS.

### Follow-up Questions
How does MVS behave when two modules require different minimum versions of the same dependency?

---
<!-- interview-answers:end -->

---

## How do you handle private module fetch in CI without GOPATH hacks?

### Short Answer
The senior-level answer is go.mod/go.sum, MVS resolution, vendoring, GOPRIVATE — for: How do you handle private module fetch in CI without GOPATH hacks.

### Detailed Explanation
Explain semver import paths (/v2), retract, and verify in CI for: How do you handle private module fetch in CI without GOPATH hacks.

### Internal Working
MVS picks minimum compatible versions across the module graph — internal rule for: How do you handle private module fetch in CI without GOPATH hacks.

### Production Notes
Pin toolchain; never commit local replace forks for: How do you handle private module fetch in CI without GOPATH hacks.

### Common Mistakes
Omitting go.sum or blind `go get -u` in libraries hurts: How do you handle private module fetch in CI without GOPATH hacks.

### Follow-up Questions
How would MVS resolve a conflicting requirement in: How do you handle private module fetch in CI without GOPATH hacks?

---
## How does Minimal Version Selection resolve conflicting module requirements?

### Short Answer
The mechanism-first explanation is bound concurrency, define goroutine exit, and choose mutex vs channel deliberately — for: How does Minimal Version Selection resolve conflicting module requirements.

### Detailed Explanation
Channels orchestrate; mutexes protect shared state; WaitGroup/ctx coordinate lifecycle — apply to: How does Minimal Version Selection resolve conflicting module requirements.

### Internal Working
Unbuffered channels rendezvous; buffered channels decouple until full; nil chans disable select cases — internals for: How does Minimal Version Selection resolve conflicting module requirements.

### Production Notes
Propagate context, add backpressure, and test with `-race` when implementing: How does Minimal Version Selection resolve conflicting module requirements.

### Common Mistakes
Leaked goroutines, send-on-closed-channel panics, and select spin loops are frequent failures in: How does Minimal Version Selection resolve conflicting module requirements.

### Follow-up Questions
How would you structure shutdown so: How does Minimal Version Selection resolve conflicting module requirements cannot hang the process?

---
## When is vendoring required for reproducible builds?

### Short Answer
The senior-level answer is go.mod/go.sum, MVS resolution, vendoring, GOPRIVATE — for: When is vendoring required for reproducible builds.

### Detailed Explanation
Explain semver import paths (/v2), retract, and verify in CI for: When is vendoring required for reproducible builds.

### Internal Working
MVS picks minimum compatible versions across the module graph — internal rule for: When is vendoring required for reproducible builds.

### Production Notes
Pin toolchain; never commit local replace forks for: When is vendoring required for reproducible builds.

### Common Mistakes
Omitting go.sum or blind `go get -u` in libraries hurts: When is vendoring required for reproducible builds.

### Follow-up Questions
How would MVS resolve a conflicting requirement in: When is vendoring required for reproducible builds?

---
<!-- interview-answers:end -->

---

## See Also

- [Previous: Go Modules](/golang-cheatsheet/02-core-go/go-modules/)
- [Next: Error Handling](/golang-cheatsheet/02-core-go/error-handling/)
- [Go Handbook Index](/golang-cheatsheet/)
- [Top 150 Interview Questions](/golang-cheatsheet/08-interview-guide/top-150-interview-questions/)
