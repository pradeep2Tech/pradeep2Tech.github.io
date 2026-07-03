---
title: "Go Concept Registry"
date: 2026-07-03T12:00:00+00:00
draft: true
description: "Canonical source mapping — one authoritative page per Go concept."
tags: ["golang-cheatsheet", "meta", "planning"]
---

# Go Concept Registry

**Rule:** Full explanation lives on the canonical page only. All other pages: **≤ 2 sentences** + link.

**Status:** Phase A — registry defined; enforcement in Phase B/C.

**Path prefix:** `content/golang-cheatsheet/` (nested modules below).

---

## 01 Fundamentals

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| Language syntax & control flow | `01-fundamentals/language-basics.md` | Exists | Quick-revision only |
| Zero values | `01-fundamentals/language-basics.md` | Exists | |
| `iota` enumerations | `01-fundamentals/language-basics.md` | Exists | |
| `defer` LIFO semantics | `01-fundamentals/language-basics.md` | Exists | |
| Functions (signatures, closures) | `01-fundamentals/functions.md` | Exists | |
| Variadic parameters | `01-fundamentals/functions.md` | Exists | |
| Named return values | `01-fundamentals/functions.md` | Exists | |
| `recover()` semantics | `01-fundamentals/functions.md` | Exists | Goroutine panic → link goroutines |
| Structs & embedding | `01-fundamentals/structs.md` | Exists | |
| Struct tags (JSON/XML) | `01-fundamentals/structs.md` | Exists | |
| Arrays (fixed `[N]T`) | `01-fundamentals/arrays.md` | Exists | |
| Slices (header, len, cap) | `01-fundamentals/slices.md` | Exists | **Primary** slice source |
| `append` reallocation | `01-fundamentals/slices.md` | Exists | |
| Subslice aliasing / memory leaks | `01-fundamentals/slices.md` | Exists | |
| Maps (hash table ops) | `01-fundamentals/maps.md` | Exists | |
| Nil map read/write | `01-fundamentals/maps.md` | Exists | |
| Map iteration randomization | `01-fundamentals/maps.md` | Exists | |
| Map concurrent access (unsafe) | `01-fundamentals/maps.md` | Exists | Fix → sync or sync.Map |
| Value vs pointer receivers | `01-fundamentals/methods.md` | Exists | **Primary** method-set source |
| Method sets & interface satisfaction | `01-fundamentals/methods.md` | Exists | Interfaces page links here |

---

## 02 Core Go

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| Implicit interfaces | `02-core-go/interfaces.md` | Exists | |
| Interface value `(type, data)` | `02-core-go/interfaces.md` | Exists | |
| Nil interface vs typed nil | `02-core-go/interfaces.md` | Exists | **Primary** nil-interface source |
| Type assertions & type switches | `02-core-go/interfaces.md` | Exists | |
| Empty interface / `any` | `02-core-go/interfaces.md` | Exists | |
| Pointers (`&`, `*`, `new`) | `02-core-go/pointers.md` | Exists | |
| `new` vs `make` | `02-core-go/pointers.md` | Exists | |
| Package layout & exports | `02-core-go/packages.md` | Exists | |
| `init()` ordering | `02-core-go/packages.md` | Exists | |
| `internal/` packages | `02-core-go/packages.md` | Exists | |
| `error` interface | `02-core-go/error-handling.md` | Exists | |
| Error wrapping (`%w`) | `02-core-go/error-handling.md` | Exists | |
| `errors.Is` / `errors.As` | `02-core-go/error-handling.md` | Exists | |
| Sentinel errors | `02-core-go/error-handling.md` | Exists | |
| `go.mod` directives | `02-core-go/go-modules.md` | Exists | **Primary** module file |
| `go.sum` checksums | `02-core-go/go-modules.md` | Exists | |
| `replace` / `retract` | `02-core-go/go-modules.md` | Exists | |
| `go.work` workspaces | `02-core-go/go-modules.md` | Exists | |
| Minimal Version Selection (MVS) | `02-core-go/dependency-management.md` | Exists | |
| `go get` versioning | `02-core-go/dependency-management.md` | Exists | |
| Vendoring (`go mod vendor`) | `02-core-go/dependency-management.md` | Exists | |
| `GOPRIVATE` / private modules | `02-core-go/dependency-management.md` | Exists | |
| Semantic import versioning (`/v2`) | `02-core-go/dependency-management.md` | Exists | |

---

## 03 Go Internals

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| Go runtime architecture | `03-go-internals/go-runtime.md` | **Planned** | |
| Runtime components (scheduler, GC, netpoller) | `03-go-internals/go-runtime.md` | **Planned** | |
| Execution flow (compile → link → run) | `03-go-internals/go-runtime.md` | **Planned** | |
| GMP model (G, M, P) | `03-go-internals/scheduler.md` | **Planned** | Strip from goroutines.md |
| Goroutine scheduling | `03-go-internals/scheduler.md` | **Planned** | |
| Work stealing | `03-go-internals/scheduler.md` | **Planned** | |
| Cooperative vs preemptive scheduling | `03-go-internals/scheduler.md` | **Planned** | |
| `GOMAXPROCS` | `03-go-internals/scheduler.md` | **Planned** | Mention only on goroutines |
| Goroutine stack growth/shrink | `03-go-internals/scheduler.md` | **Planned** | |
| Happens-before relations | `03-go-internals/memory-model.md` | Exists | **Primary** |
| Data races | `03-go-internals/memory-model.md` | Exists | |
| `sync/atomic` synchronization | `03-go-internals/memory-model.md` | Exists | |
| Channel happens-before | `03-go-internals/memory-model.md` | Exists | |
| Tri-color mark-sweep GC | `03-go-internals/garbage-collection.md` | Exists | **Primary** |
| `GOGC` pacing | `03-go-internals/garbage-collection.md` | Exists | |
| STW pauses | `03-go-internals/garbage-collection.md` | Exists | |
| `runtime.SetFinalizer` | `03-go-internals/garbage-collection.md` | Exists | |
| Stack vs heap allocation | `03-go-internals/escape-analysis.md` | **Planned** | |
| Escape analysis rules | `03-go-internals/escape-analysis.md` | **Planned** | |
| `go build -gcflags=-m` | `03-go-internals/escape-analysis.md` | **Planned** | |
| `reflect.Type` / `reflect.Value` | `03-go-internals/reflection.md` | Exists | |
| Reflection addressability | `03-go-internals/reflection.md` | Exists | |
| When to avoid reflection | `03-go-internals/reflection.md` | Exists | |

---

## 04 Concurrency

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| `go` statement / goroutine lifecycle | `04-concurrency/goroutines.md` | Exists | Links scheduler for GMP |
| Goroutine leaks | `04-concurrency/goroutines.md` | Exists | |
| Panic in goroutines | `04-concurrency/goroutines.md` | Exists | |
| Channels (unbuffered) | `04-concurrency/channels.md` | Exists | **Primary** |
| Buffered channels | `04-concurrency/channels.md` | Exists | |
| Channel close semantics | `04-concurrency/channels.md` | Exists | |
| Send on closed channel panic | `04-concurrency/channels.md` | Exists | |
| `nil` channel blocking | `04-concurrency/channels.md` | Exists | |
| `select` multiplexing | `04-concurrency/select.md` | Exists | **Primary** |
| `select` + `default` (non-blocking) | `04-concurrency/select.md` | Exists | |
| `select` + timeout (`time.After`) | `04-concurrency/select.md` | Exists | |
| `context.Context` API | `04-concurrency/context.md` | Exists | **Primary** |
| Cancellation propagation | `04-concurrency/context.md` | Exists | |
| `WithTimeout` / `WithDeadline` | `04-concurrency/context.md` | Exists | |
| `WithValue` (request-scoped) | `04-concurrency/context.md` | Exists | |
| `sync.Mutex` | `04-concurrency/mutex.md` | Exists | |
| Lock ordering / deadlock | `04-concurrency/mutex.md` | Exists | |
| `sync.RWMutex` | `04-concurrency/rwmutex.md` | Exists | |
| Writer starvation | `04-concurrency/rwmutex.md` | Exists | |
| `sync.WaitGroup` | `04-concurrency/sync-package.md` | Exists | |
| `sync.Once` | `04-concurrency/sync-package.md` | Exists | |
| `sync.Pool` | `04-concurrency/sync-package.md` | Exists | Perf tuning → performance-optimization |
| `sync.Cond` | `04-concurrency/sync-package.md` | Exists | |
| `sync.Map` | `04-concurrency/sync-package.md` | Exists | |
| Worker pools | `04-concurrency/concurrency-patterns.md` | **Planned** | |
| Fan-out / fan-in | `04-concurrency/concurrency-patterns.md` | **Planned** | Strip from channels.md |
| Pipelines | `04-concurrency/concurrency-patterns.md` | **Planned** | |
| Backpressure | `04-concurrency/concurrency-patterns.md` | **Planned** | |
| Cancellation patterns (beyond API) | `04-concurrency/concurrency-patterns.md` | **Planned** | API on context.md |

---

## 05 Performance

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| Allocation reduction | `05-performance/performance-optimization.md` | **Planned** | |
| Object reuse strategies | `05-performance/performance-optimization.md` | **Planned** | |
| Efficient concurrency (avoid overspawn) | `05-performance/performance-optimization.md` | **Planned** | |
| `pprof` (CPU, heap, goroutine) | `05-performance/profiling.md` | **Planned** | |
| `go tool pprof` workflow | `05-performance/profiling.md` | **Planned** | |
| Trace (`runtime/trace`) | `05-performance/profiling.md` | **Planned** | |
| `testing.B` benchmarks | `05-performance/benchmarking.md` | **Planned** | Basics on testing.md |
| `benchstat` / comparison | `05-performance/benchmarking.md` | **Planned** | |
| Benchmark noise & warmup | `05-performance/benchmarking.md` | **Planned** | |
| Slice preallocation | `05-performance/memory-optimization.md` | **Planned** | |
| Pointer density / struct layout | `05-performance/memory-optimization.md` | **Planned** | |
| GC interaction (alloc rate) | `05-performance/memory-optimization.md` | **Planned** | GC theory → garbage-collection.md |

---

## 06 Production Go

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| Structured logging (slog, zap) | `06-production-go/logging.md` | **Planned** | |
| Log correlation / request IDs | `06-production-go/logging.md` | **Planned** | |
| Environment variables | `06-production-go/configuration-management.md` | **Planned** | |
| Config loading (viper, envconfig) | `06-production-go/configuration-management.md` | **Planned** | |
| Secrets management | `06-production-go/configuration-management.md` | **Planned** | |
| Metrics (Prometheus) | `06-production-go/observability.md` | **Planned** | |
| Distributed tracing | `06-production-go/observability.md` | **Planned** | |
| OpenTelemetry Go SDK | `06-production-go/observability.md` | **Planned** | |
| Signal handling (`SIGTERM`) | `06-production-go/graceful-shutdown.md` | **Planned** | |
| HTTP server drain | `06-production-go/graceful-shutdown.md` | **Planned** | |
| Resource cleanup on shutdown | `06-production-go/graceful-shutdown.md` | **Planned** | |
| Pre-production checklist | `06-production-go/production-checklists.md` | **Planned** | |
| CI/CD Go checklist | `06-production-go/production-checklists.md` | **Planned** | |

---

## 07 Testing

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| `testing.T` / table-driven tests | `07-testing/testing.md` | Exists | |
| `t.Parallel()` | `07-testing/testing.md` | Exists | |
| `go test -race` | `07-testing/testing.md` | Exists | Why → memory-model.md |
| Coverage | `07-testing/testing.md` | Exists | |
| `Example` functions | `07-testing/testing.md` | Exists | |
| Fuzzing (`testing.F`) | `07-testing/testing.md` | **Planned** | Phase C expansion |
| Interface-based testing | `07-testing/mocking.md` | **Planned** | |
| Test doubles / stubs | `07-testing/mocking.md` | **Planned** | |
| Mock generation (gomock, mockery) | `07-testing/mocking.md` | **Planned** | |
| Unit vs integration tests | `07-testing/test-strategies.md` | **Planned** | |
| `httptest` patterns | `07-testing/test-strategies.md` | **Planned** | |
| Concurrency test patterns | `07-testing/test-strategies.md` | **Planned** | |
| Build tags for integration | `07-testing/test-strategies.md` | **Planned** | |

---

## 08 Interview Guide (Layer 1 — Questions Only)

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| Top 150 question index | `08-interview-guide/top-150-interview-questions.md` | **Planned** | No answers on this page |
| Architect subset | `08-interview-guide/architect-questions.md` | **Planned** | |
| Troubleshooting subset | `08-interview-guide/troubleshooting-questions.md` | **Planned** | |
| Performance subset | `08-interview-guide/performance-questions.md` | **Planned** | |

**Answer layer:** Canonical topic pages (prefer existing). Format: `## Question` → Short Answer → Detailed Explanation → …

---

## Cross-Registry Duplication Rules (Phase B Enforcement)

| If mentioned on… | Max detail | Link to |
| :--- | :--- | :--- |
| Any fundamentals page | 2 sentences | Relevant `03-go-internals/*` for runtime |
| `goroutines.md` | GMP overview only | `scheduler.md` |
| `channels.md` | No fan-in/out implementation | `concurrency-patterns.md` |
| `garbage-collection.md` | No pprof walkthrough | `profiling.md` |
| `sync-package.md` | Pool API only | `performance-optimization.md` for tuning |
| `testing.md` | No benchstat depth | `benchmarking.md` |
| `interfaces.md` | No method-set table | `methods.md` |
| `go-modules.md` | No MVS essay | `dependency-management.md` |

---

## Out of Scope (Other Handbooks)

Do **not** duplicate canonical content for: Design Patterns, System Design, SOLID, Architecture Patterns, Microservices Patterns, Kubernetes deployment patterns (link only).

---

**STOP — Enforce registry during Phase B/C content work.**
