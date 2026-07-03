---
title: "Testing"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "testing package, table-driven tests, benchmarks, and race detector."
tags: ["golang", "golang-cheatsheet", "golang-handbook", "go", "interview"]
categories: ["Go Handbook"]
shortTitle: "Testing"
module: 7
moduleTitle: "Testing"
sectionRef: "7.1"
weight: 701
ShowToc: true
cheatSheet: true
interviewHandbook: true
aliases:
  - "/golang-cheatsheet/testing/"
---

## At a Glance

- Tests live in `*_test.go` same package (or `package_test` for black-box). Use **table-driven tests**, **`t.Parallel()`**, and **`go test ./...`** in CI.

---

## Reference Tables

| Tool | Command / API |
| :--- | :--- |
| Run | `go test ./...` |
| Verbose | `go test -v` |
| Coverage | `go test -cover ./...` |
| Benchmark | `func BenchmarkX(b *testing.B)` |
| Example | `func ExampleX()` — compile-checked docs |

```go
func TestAdd(t *testing.T) {
    tests := []struct {
        a, b, want int
    }{
        {1, 2, 3},
        {0, 0, 0},
    }
    for _, tt := range tests {
        t.Run(fmt.Sprintf("%d+%d", tt.a, tt.b), func(t *testing.T) {
            if got := Add(tt.a, tt.b); got != tt.want {
                t.Fatalf("got %d want %d", got, tt.want)
            }
        })
    }
}
```

---

## Snippets

```go
func BenchmarkHash(b *testing.B) {
    b.ReportAllocs()
    for i := 0; i < b.N; i++ {
        _ = hash(payload)
    }
}
```

---

## Internals & Gotchas

- `t.Fatal` inside goroutine doesn't stop test reliably — use `t.Run` sync or channels.
- Race detector: `go test -race` — CI essential for concurrent code.
- `init()` in tests affects all tests in package.

---

For **mocking** and **integration strategies**, see [Mocking](/golang-cheatsheet/07-testing/mocking/) and [Test Strategies](/golang-cheatsheet/07-testing/test-strategies/).

## Production Notes

- Run `go test -race` in CI for concurrent packages.

---

## What does go test -race output tell you and what are false-positive pitfalls?

### Short Answer
Table-driven unit tests, race detector in CI, interface mocks/fakes, build-tagged integration tests.

### Detailed Explanation
Tests should be deterministic, fast, and parallel-safe where possible. Use interfaces at boundaries for test doubles. Integration tests hit real deps with tags.

### Internal Working
t.Parallel requires isolated state. Fuzzing (testing.F) finds edge cases. httptest records HTTP without network.

### Production Notes
Gate merges on `-race` for concurrent code. Use `-cover` for critical packages. Mock codegen for large interfaces only when hand fakes hurt maintenance.

### Common Mistakes
t.Fatal inside goroutines. Shared global state across parallel tests. Over-mocking internal concrete types.

### Follow-up Questions
How would you structure a concurrency regression test for a worker pool?

---
## How does table-driven testing scale to many edge cases?

### Short Answer
Table-driven unit tests, race detector in CI, interface mocks/fakes, build-tagged integration tests.

### Detailed Explanation
Tests should be deterministic, fast, and parallel-safe where possible. Use interfaces at boundaries for test doubles. Integration tests hit real deps with tags.

### Internal Working
t.Parallel requires isolated state. Fuzzing (testing.F) finds edge cases. httptest records HTTP without network.

### Production Notes
Gate merges on `-race` for concurrent code. Use `-cover` for critical packages. Mock codegen for large interfaces only when hand fakes hurt maintenance.

### Common Mistakes
t.Fatal inside goroutines. Shared global state across parallel tests. Over-mocking internal concrete types.

### Follow-up Questions
How would you structure a concurrency regression test for a worker pool?

---
## Why is t.Fatal unsafe inside a goroutine in tests?

### Short Answer
Table-driven unit tests, race detector in CI, interface mocks/fakes, build-tagged integration tests.

### Detailed Explanation
Tests should be deterministic, fast, and parallel-safe where possible. Use interfaces at boundaries for test doubles. Integration tests hit real deps with tags.

### Internal Working
t.Parallel requires isolated state. Fuzzing (testing.F) finds edge cases. httptest records HTTP without network.

### Production Notes
Gate merges on `-race` for concurrent code. Use `-cover` for critical packages. Mock codegen for large interfaces only when hand fakes hurt maintenance.

### Common Mistakes
t.Fatal inside goroutines. Shared global state across parallel tests. Over-mocking internal concrete types.

### Follow-up Questions
How would you structure a concurrency regression test for a worker pool?

---
<!-- interview-answers:end -->

---

## What does go test -race output tell you and what are false-positive pitfalls?

### Short Answer
The architecturally sound response is table-driven tests, `-race`, interface fakes/mocks, build-tagged integration — for: What does go test -race output tell you and what are false-positive pitfalls.

### Detailed Explanation
Keep tests deterministic; avoid t.Fatal in goroutines; fuzz edge cases for: What does go test -race output tell you and what are false-positive pitfalls.

### Internal Working
Parallel tests need isolated state; httptest fakes network — techniques for: What does go test -race output tell you and what are false-positive pitfalls.

### Production Notes
Gate merges on race detector for concurrent packages related to: What does go test -race output tell you and what are false-positive pitfalls.

### Common Mistakes
Over-mocking concrete types or flaky timing-based tests weaken: What does go test -race output tell you and what are false-positive pitfalls.

### Follow-up Questions
How would you regression-test concurrency behavior for: What does go test -race output tell you and what are false-positive pitfalls?

---
## How does table-driven testing scale to many edge cases?

### Short Answer
The senior-level answer is table-driven tests, `-race`, interface fakes/mocks, build-tagged integration — for: How does table-driven testing scale to many edge cases.

### Detailed Explanation
Keep tests deterministic; avoid t.Fatal in goroutines; fuzz edge cases for: How does table-driven testing scale to many edge cases.

### Internal Working
Parallel tests need isolated state; httptest fakes network — techniques for: How does table-driven testing scale to many edge cases.

### Production Notes
Gate merges on race detector for concurrent packages related to: How does table-driven testing scale to many edge cases.

### Common Mistakes
Over-mocking concrete types or flaky timing-based tests weaken: How does table-driven testing scale to many edge cases.

### Follow-up Questions
How would you regression-test concurrency behavior for: How does table-driven testing scale to many edge cases?

---
## Why is t.Fatal unsafe inside a goroutine in tests?

### Short Answer
In production Go, the decisive factor is table-driven tests, `-race`, interface fakes/mocks, build-tagged integration — for: Why is t.Fatal unsafe inside a goroutine in tests.

### Detailed Explanation
Keep tests deterministic; avoid t.Fatal in goroutines; fuzz edge cases for: Why is t.Fatal unsafe inside a goroutine in tests.

### Internal Working
Parallel tests need isolated state; httptest fakes network — techniques for: Why is t.Fatal unsafe inside a goroutine in tests.

### Production Notes
Gate merges on race detector for concurrent packages related to: Why is t.Fatal unsafe inside a goroutine in tests.

### Common Mistakes
Over-mocking concrete types or flaky timing-based tests weaken: Why is t.Fatal unsafe inside a goroutine in tests.

### Follow-up Questions
How would you regression-test concurrency behavior for: Why is t.Fatal unsafe inside a goroutine in tests?

---
<!-- interview-answers:end -->

---

## See Also

- [Previous: Production Checklists](/golang-cheatsheet/06-production-go/production-checklists/)
- [Next: Mocking](/golang-cheatsheet/07-testing/mocking/)
- [Go Handbook Index](/golang-cheatsheet/)
- [Top 150 Interview Questions](/golang-cheatsheet/08-interview-guide/top-150-interview-questions/)
