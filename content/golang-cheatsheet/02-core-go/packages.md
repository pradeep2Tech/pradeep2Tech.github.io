---
title: "Packages"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "Package layout, exports, init(), and internal packages."
tags: ["golang", "golang-cheatsheet", "golang-handbook", "go", "interview"]
categories: ["Go Handbook"]
shortTitle: "Packages"
module: 2
moduleTitle: "Core Go"
sectionRef: "2.3"
weight: 203
ShowToc: true
cheatSheet: true
interviewHandbook: true
aliases:
  - "/golang-cheatsheet/packages/"
---

## At a Glance

- Code is organized in **packages** — one directory, one package (usually). **Exported** names start with uppercase. `init()` runs at package load time.

---

## Reference Tables

| Rule | Detail |
| :--- | :--- |
| Package name | Short, lowercase, matches last import path segment |
| Export | `Foo` exported; `foo` package-private |
| `internal/` | Importable only from parent tree |
| `init()` | No args/returns; multiple per file; order within package undefined |
| `main` | `func main()` in `package main` |

```
myapp/
  cmd/api/main.go      # package main
  internal/service/    # internal packages
  pkg/client/          # public library code
```

---

## Snippets

```go
// client/client.go
package client

import "errors"

var ErrNotFound = errors.New("not found")

func Get(id string) (*Item, error) {
    // ...
    return nil, ErrNotFound
}
```

---

## Internals & Gotchas

- Import cycle is a **compile error** — extract shared types to third package.
- `init()` side effects make testing harder — keep minimal.
- Package name should not include underscores or `util`.

---

## Production Notes

- Apply patterns from this page in code review and incident postmortems.

---

## What is the package layout convention for cmd, internal, and pkg?

### Short Answer
Anchor the answer in Go runtime semantics, observable behavior, and production tradeoffs for packages.

### Detailed Explanation
Senior interviews expect mechanism-first reasoning: what the language/runtime guarantees, what it does not, and how that shows up under load or failure.

### Internal Working
Go couples language rules (types, interfaces, concurrency primitives) with a runtime scheduler, GC, and memory model. Correct answers connect API behavior to these subsystems.

### Production Notes
Validate assumptions with `go test -race`, benchmarks, and pprof before changing architecture. Pin Go versions and document SLO impact of concurrency/GC choices.

### Common Mistakes
Hand-waving 'Go is fast' without allocation, scheduling, or cancellation analysis. Copying patterns without bounding goroutines or defining shutdown behavior.

### Follow-up Questions
What observable metric or test would prove your design handles this packages concern in production?

---
## How do init() functions complicate testing and what is the mitigation?

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

## What is the package layout convention for cmd, internal, and pkg?

### Short Answer
The architecturally sound response is cmd/internal/pkg layout; minimal init(); explicit exports — for: What is the package layout convention for cmd, internal, and pkg.

### Detailed Explanation
internal/ enforces boundaries; init ordering is dependency-defined for: What is the package layout convention for cmd, internal, and pkg.

### Internal Working
Import cycles are compile-time failures — design packages to avoid for: What is the package layout convention for cmd, internal, and pkg.

### Production Notes
Keep init light; inject deps in tests for: What is the package layout convention for cmd, internal, and pkg.

### Common Mistakes
Heavy init() harms testability and startup for: What is the package layout convention for cmd, internal, and pkg.

### Follow-up Questions
Where would you draw the module boundary for: What is the package layout convention for cmd, internal, and pkg?

---
## How do init() functions complicate testing and what is the mitigation?

### Short Answer
In production Go, the decisive factor is table-driven tests, `-race`, interface fakes/mocks, build-tagged integration — for: How do init() functions complicate testing and what is the mitigation.

### Detailed Explanation
Keep tests deterministic; avoid t.Fatal in goroutines; fuzz edge cases for: How do init() functions complicate testing and what is the mitigation.

### Internal Working
Parallel tests need isolated state; httptest fakes network — techniques for: How do init() functions complicate testing and what is the mitigation.

### Production Notes
Gate merges on race detector for concurrent packages related to: How do init() functions complicate testing and what is the mitigation.

### Common Mistakes
Over-mocking concrete types or flaky timing-based tests weaken: How do init() functions complicate testing and what is the mitigation.

### Follow-up Questions
How would you regression-test concurrency behavior for: How do init() functions complicate testing and what is the mitigation?

---
<!-- interview-answers:end -->

---

## See Also

- [Previous: Pointers](/golang-cheatsheet/02-core-go/pointers/)
- [Next: Go Modules](/golang-cheatsheet/02-core-go/go-modules/)
- [Go Handbook Index](/golang-cheatsheet/)
- [Top 150 Interview Questions](/golang-cheatsheet/08-interview-guide/top-150-interview-questions/)
