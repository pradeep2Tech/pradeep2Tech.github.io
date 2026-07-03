---
title: "Test Strategies"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "Unit, integration, benchmark, and concurrency testing."
tags: ["golang", "golang-cheatsheet", "golang-handbook", "go", "interview"]
categories: ["Go Handbook"]
shortTitle: "Strategies"
module: 7
moduleTitle: "Testing"
sectionRef: "7.3"
weight: 703
ShowToc: true
interviewHandbook: true
---

## Quick Revision

- **Unit:** pure logic, table-driven.
- **Integration:** `//go:build integration` tag, real deps in CI.
- **Concurrency:** `go test -race`; stress tests with `-count`.

## Production Usage

- [Benchmarking](/golang-cheatsheet/05-performance/benchmarking/) for perf regression gates.

## Core Concepts

| Layer | Scope | Tools |
| :--- | :--- | :--- |
| Unit | Pure logic, fast | table tests, t.Parallel |
| Integration | Real DB/HTTP | `//go:build integration`, testcontainers |
| Benchmark | Perf regression | testing.B, benchstat |
| Fuzz | Edge inputs | testing.F (Go 1.18+) |
| Race | Concurrency | `-race` |

## Production Usage

Run unit tests on every PR; integration nightly or on label; race on packages with sync.

## Architect Notes

Test strategy should mirror **failure modes**: cancellation, timeout, partial errors, concurrent access.


---

## How do you structure integration tests with build tags?

### Short Answer
The architecturally sound response is table-driven tests, `-race`, interface fakes/mocks, build-tagged integration — for: How do you structure integration tests with build tags.

### Detailed Explanation
Keep tests deterministic; avoid t.Fatal in goroutines; fuzz edge cases for: How do you structure integration tests with build tags.

### Internal Working
Parallel tests need isolated state; httptest fakes network — techniques for: How do you structure integration tests with build tags.

### Production Notes
Gate merges on race detector for concurrent packages related to: How do you structure integration tests with build tags.

### Common Mistakes
Over-mocking concrete types or flaky timing-based tests weaken: How do you structure integration tests with build tags.

### Follow-up Questions
How would you regression-test concurrency behavior for: How do you structure integration tests with build tags?

---
## How do you test concurrent code deterministically?

### Short Answer
In production Go, the decisive factor is table-driven tests, `-race`, interface fakes/mocks, build-tagged integration — for: How do you test concurrent code deterministically.

### Detailed Explanation
Keep tests deterministic; avoid t.Fatal in goroutines; fuzz edge cases for: How do you test concurrent code deterministically.

### Internal Working
Parallel tests need isolated state; httptest fakes network — techniques for: How do you test concurrent code deterministically.

### Production Notes
Gate merges on race detector for concurrent packages related to: How do you test concurrent code deterministically.

### Common Mistakes
Over-mocking concrete types or flaky timing-based tests weaken: How do you test concurrent code deterministically.

### Follow-up Questions
How would you regression-test concurrency behavior for: How do you test concurrent code deterministically?

---
<!-- interview-answers:end -->

---

## See Also

- [Previous: Mocking](/golang-cheatsheet/07-testing/mocking/)
- [Go Handbook Index](/golang-cheatsheet/)
- [Top 150 Interview Questions](/golang-cheatsheet/08-interview-guide/top-150-interview-questions/)
