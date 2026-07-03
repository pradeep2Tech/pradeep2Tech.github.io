"""Generate refactored Go handbook content (Phase B)."""
from __future__ import annotations

import re
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HB = ROOT / "content" / "golang-cheatsheet"
DATA = ROOT / "data"
DATE = "2026-07-03T12:00:00+00:00"
BASE = "/golang-cheatsheet"

FM = """---
title: "{title}"
date: {date}
draft: false
description: "{desc}"
tags: ["golang", "golang-cheatsheet", "golang-handbook", "go", "interview"]
categories: ["Go Handbook"]
shortTitle: "{short}"
module: {mod}
moduleTitle: "{mod_title}"
sectionRef: "{ref}"
weight: {weight}
ShowToc: true
interviewHandbook: true{aliases}
---

"""

FM_CHEAT = FM.replace("interviewHandbook: true", "cheatSheet: true\ninterviewHandbook: true")


def aliases_block(*paths: str) -> str:
    if not paths:
        return ""
    lines = "\n".join(f'  - "{p}"' for p in paths)
    return f"\naliases:\n{lines}"


def w(rel: str, body: str, *, cheat: bool = False, alias_paths: tuple[str, ...] = (), **fm):
    path = HB / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    tmpl = FM_CHEAT if cheat else FM
    alias = aliases_block(*alias_paths)
    path.write_text(tmpl.format(date=DATE, aliases=alias, **fm) + body.strip() + "\n", encoding="utf-8")


def read_old(name: str) -> str:
    p = HB / name
    if not p.exists():
        return ""
    text = p.read_text(encoding="utf-8")
    return re.sub(r"^---.*?---\n", "", text, count=1, flags=re.DOTALL)


def fix_links(body: str) -> str:
    flat_slugs = [
        "language-basics", "functions", "structs", "arrays", "slices", "maps", "methods",
        "interfaces", "pointers", "packages", "error-handling", "go-modules", "dependency-management",
        "goroutines", "channels", "select", "context", "mutex", "rwmutex", "sync-package",
        "memory-model", "garbage-collection", "reflection", "testing", "interview-questions",
    ]
    targets = {
        "language-basics": "01-fundamentals/language-basics",
        "functions": "01-fundamentals/functions",
        "structs": "01-fundamentals/structs",
        "arrays": "01-fundamentals/arrays",
        "slices": "01-fundamentals/slices",
        "maps": "01-fundamentals/maps",
        "methods": "01-fundamentals/methods",
        "interfaces": "02-core-go/interfaces",
        "pointers": "02-core-go/pointers",
        "packages": "02-core-go/packages",
        "error-handling": "02-core-go/error-handling",
        "go-modules": "02-core-go/go-modules",
        "dependency-management": "02-core-go/dependency-management",
        "goroutines": "04-concurrency/goroutines",
        "channels": "04-concurrency/channels",
        "select": "04-concurrency/select",
        "context": "04-concurrency/context",
        "mutex": "04-concurrency/mutex",
        "rwmutex": "04-concurrency/rwmutex",
        "sync-package": "04-concurrency/sync-package",
        "memory-model": "03-go-internals/memory-model",
        "garbage-collection": "03-go-internals/garbage-collection",
        "reflection": "03-go-internals/reflection",
        "testing": "07-testing/testing",
        "interview-questions": "08-interview-guide/top-150-interview-questions",
    }
    for slug, nested in targets.items():
        body = body.replace(f"{BASE}/{slug}/", f"{BASE}/{nested}/")
    return body


SECTIONS = [
    ("01-fundamentals", "Fundamentals", "Language syntax, types, collections, and methods.", 1),
    ("02-core-go", "Core Go", "Interfaces, pointers, packages, errors, and modules.", 2),
    ("03-go-internals", "Go Internals", "Runtime, scheduler, memory model, GC, escape analysis, reflection.", 3),
    ("04-concurrency", "Concurrency", "Goroutines, channels, sync primitives, context, and patterns.", 4),
    ("05-performance", "Performance", "Profiling, benchmarking, allocation tuning, and memory optimization.", 5),
    ("06-production-go", "Production Go", "Logging, config, observability, graceful shutdown, checklists.", 6),
    ("07-testing", "Testing", "Unit tests, mocking, and test strategies.", 7),
    ("08-interview-guide", "Interview Guide", "150-question bank and role-specific subsets.", 8),
    ("09-learning-paths", "Learning Paths", "Curated reading paths by seniority and goal.", 9),
]


def handbook_page(sections: dict[str, str]) -> str:
    parts = []
    for heading, content in sections.items():
        parts.append(f"## {heading}\n\n{content.strip()}")
    return "\n\n".join(parts) + "\n"


def main() -> None:
    for folder, title, desc, mod in SECTIONS:
        w(
            f"{folder}/_index.md",
            f"# {title}\n\n{desc}\n",
            title=title,
            desc=desc,
            short=title,
            mod=mod,
            mod_title="Go Handbook",
            ref="0",
            weight=mod * 100,
        )

    def move_cheat(old, new, *, title, desc, short, mod, mod_title, ref, weight, alias, patch=None):
        body = fix_links(read_old(old))
        if patch:
            body = patch(body)
        w(new, body, cheat=True, title=title, desc=desc, short=short, mod=mod,
          mod_title=mod_title, ref=ref, weight=weight, alias_paths=(f"{BASE}/{alias}/",))

    def patch_functions(body: str) -> str:
        body = body.replace(
            'fmt.Printf(format+"\n", args...)',
            'fmt.Printf(format+"\\n", args...)',
        )
        return body

    def patch_interfaces(body: str) -> str:
        body = body.replace(
            "| Satisfaction | Pointer vs value receiver affects method set |",
            "| Satisfaction | See [Methods]({base}/01-fundamentals/methods/) for method-set rules |".format(base=BASE),
        )
        return body

    def patch_methods(body: str) -> str:
        if "## Quick Revision" not in body:
            body = body.replace(
                "## At a Glance",
                "## Quick Revision\n\n"
                "- **Pointer receiver** when mutating or struct contains `sync.Mutex`.\n"
                "- **Value receiver** for small immutable types.\n"
                "- Method set rules drive [interface satisfaction]({base}/02-core-go/interfaces/).\n\n"
                "## At a Glance".format(base=BASE),
            )
        return body

    def patch_maps(body: str) -> str:
        body = body.replace(
            "| Concurrent | Use `sync.Map` or mutex + map |",
            "| Concurrent | Not safe concurrent — use mutex or [sync.Map]({base}/04-concurrency/sync-package/) |".format(base=BASE),
        )
        return body

    def patch_goroutines(body: str) -> str:
        body = re.sub(
            r"```mermaid\nflowchart TB[\s\S]*?```\n",
            "For the **GMP scheduler** diagram and preemption detail, see "
            f"[Scheduler]({BASE}/03-go-internals/scheduler/).\n\n",
            body,
            count=1,
        )
        body = body.replace(
            "| Scheduler | M:N — work stealing |",
            "| Scheduler | M:N — see [Scheduler]({base}/03-go-internals/scheduler/) |".format(base=BASE),
        )
        body = body.replace(
            "Main exiting kills all goroutines — no graceful shutdown by default.",
            "Main exiting kills all goroutines — see [Graceful Shutdown]({base}/06-production-go/graceful-shutdown/).".format(base=BASE),
        )
        return body

    def patch_channels(body: str) -> str:
        body = re.sub(
            r"```go\n// fan-in[\s\S]*?```\n",
            "For **fan-in**, **fan-out**, and **pipelines**, see "
            f"[Concurrency Patterns]({BASE}/04-concurrency/concurrency-patterns/).\n\n",
            body,
            count=1,
        )
        return body

    def patch_gc(body: str) -> str:
        body = body.replace(
            "| Profile | `pprof` heap/allocs |",
            "| Profile | See [Profiling]({base}/05-performance/profiling/) |".format(base=BASE),
        )
        return body

    def patch_go_modules(body: str) -> str:
        body = body.replace(
            "```bash\ngo mod init example.com/myapp\ngo mod tidy\ngo mod verify\ngo mod graph\n```",
            "```bash\ngo mod init example.com/myapp\ngo mod tidy\ngo mod verify\ngo mod graph\n```\n\n"
            f"For **MVS**, `go get`, and vendoring, see [Dependency Management]({BASE}/02-core-go/dependency-management/).",
        )
        return body

    def patch_testing(body: str) -> str:
        body = body.replace(
            "## Production Notes",
            f"For **mocking** and **integration strategies**, see [Mocking]({BASE}/07-testing/mocking/) and "
            f"[Test Strategies]({BASE}/07-testing/test-strategies/).\n\n## Production Notes",
        )
        return body

    MOVES = [
        ("language-basics.md", "01-fundamentals/language-basics.md", "Go Language Basics", "Syntax, types, zero values, variables, constants, and control flow.", "Language Basics", 1, "Fundamentals", "1.1", 111, "language-basics", None),
        ("functions.md", "01-fundamentals/functions.md", "Functions", "Signatures, multiple returns, variadic params, closures, and named results.", "Functions", 1, "Fundamentals", "1.2", 112, "functions", patch_functions),
        ("structs.md", "01-fundamentals/structs.md", "Structs", "Struct types, embedding, tags, and JSON marshaling patterns.", "Structs", 1, "Fundamentals", "1.3", 113, "structs", None),
        ("arrays.md", "01-fundamentals/arrays.md", "Arrays", "Fixed-size arrays, array vs slice, and when arrays appear in APIs.", "Arrays", 1, "Fundamentals", "1.4", 114, "arrays", None),
        ("slices.md", "01-fundamentals/slices.md", "Slices", "Slice header, append, copy, subslicing, and capacity gotchas.", "Slices", 1, "Fundamentals", "1.5", 115, "slices", None),
        ("maps.md", "01-fundamentals/maps.md", "Maps", "Map operations, iteration order, nil maps, and concurrency safety.", "Maps", 1, "Fundamentals", "1.6", 116, "maps", patch_maps),
        ("methods.md", "01-fundamentals/methods.md", "Methods", "Value vs pointer receivers, method sets, and interface satisfaction.", "Methods", 1, "Fundamentals", "1.7", 117, "methods", patch_methods),
        ("interfaces.md", "02-core-go/interfaces.md", "Interfaces", "Implicit satisfaction, nil interfaces, type assertions, and type switches.", "Interfaces", 2, "Core Go", "2.1", 201, "interfaces", patch_interfaces),
        ("pointers.md", "02-core-go/pointers.md", "Pointers", "Address-of, dereference, new vs make, and when pointers matter in Go.", "Pointers", 2, "Core Go", "2.2", 202, "pointers", None),
        ("packages.md", "02-core-go/packages.md", "Packages", "Package layout, exports, init(), and internal packages.", "Packages", 2, "Core Go", "2.3", 203, "packages", None),
        ("go-modules.md", "02-core-go/go-modules.md", "Go Modules", "go.mod, go.sum, module path, replace, and workspace mode.", "Modules", 2, "Core Go", "2.4", 204, "go-modules", patch_go_modules),
        ("dependency-management.md", "02-core-go/dependency-management.md", "Dependency Management", "go get, versioning, minimal version selection, and vendoring.", "Dependencies", 2, "Core Go", "2.5", 205, "dependency-management", None),
        ("error-handling.md", "02-core-go/error-handling.md", "Error Handling", "error interface, fmt.Errorf, errors.Is/As, wrapping, and sentinel errors.", "Errors", 2, "Core Go", "2.6", 206, "error-handling", None),
        ("goroutines.md", "04-concurrency/goroutines.md", "Goroutines", "go keyword, lifecycle, GOMAXPROCS, and goroutine leaks.", "Goroutines", 4, "Concurrency", "4.1", 401, "goroutines", patch_goroutines),
        ("channels.md", "04-concurrency/channels.md", "Channels", "Buffered vs unbuffered, close semantics, range, and coordination.", "Channels", 4, "Concurrency", "4.2", 402, "channels", patch_channels),
        ("select.md", "04-concurrency/select.md", "Select", "Multiplexing channels, default case, timeouts, and non-blocking patterns.", "Select", 4, "Concurrency", "4.3", 403, "select", None),
        ("context.md", "04-concurrency/context.md", "Context", "context.Context, cancellation, deadlines, and passing values.", "Context", 4, "Concurrency", "4.4", 404, "context", None),
        ("mutex.md", "04-concurrency/mutex.md", "Mutex", "sync.Mutex, Lock/Unlock, defer unlock, and common deadlock patterns.", "Mutex", 4, "Concurrency", "4.5", 405, "mutex", None),
        ("rwmutex.md", "04-concurrency/rwmutex.md", "RWMutex", "sync.RWMutex — concurrent reads, exclusive writes, and upgrade rules.", "RWMutex", 4, "Concurrency", "4.6", 406, "rwmutex", None),
        ("sync-package.md", "04-concurrency/sync-package.md", "sync Package", "WaitGroup, Once, Pool, Cond, and Map — coordination primitives.", "sync", 4, "Concurrency", "4.7", 407, "sync-package", None),
        ("memory-model.md", "03-go-internals/memory-model.md", "Memory Model", "Happens-before, visibility, atomics, and data races in Go.", "Memory Model", 3, "Go Internals", "3.3", 303, "memory-model", None),
        ("garbage-collection.md", "03-go-internals/garbage-collection.md", "Garbage Collection", "Go GC tri-color mark-sweep, GOGC, pacing, and allocation tuning.", "GC", 3, "Go Internals", "3.4", 304, "garbage-collection", patch_gc),
        ("reflection.md", "03-go-internals/reflection.md", "Reflection", "reflect.Type, reflect.Value, Kind, and when to avoid reflection.", "Reflection", 3, "Go Internals", "3.6", 306, "reflection", None),
        ("testing.md", "07-testing/testing.md", "Testing", "testing package, table-driven tests, benchmarks, and race detector.", "Testing", 7, "Testing", "7.1", 701, "testing", patch_testing),
    ]

    for old, new, title, desc, short, mod, mod_title, ref, weight, alias, patch in MOVES:
        move_cheat(old, new, title=title, desc=desc, short=short, mod=mod, mod_title=mod_title,
                   ref=ref, weight=weight, alias=alias, patch=patch)

    # --- New canonical pages ---
    w("03-go-internals/go-runtime.md", handbook_page({
        "Quick Revision": textwrap.dedent(f"""
            - Go binary embeds the **runtime** — scheduler, GC, memory allocator, netpoller.
            - Compile: `go build` → static binary with runtime linked in.
            - `main` runs after runtime init (scheduler, GC, signal handlers).
        """),
        "Core Concepts": "| Component | Role |\n| :--- | :--- |\n| **Scheduler** | M:N goroutine scheduling — [Scheduler]({base}/03-go-internals/scheduler/) |\n| **GC** | Concurrent mark-sweep — [Garbage Collection]({base}/03-go-internals/garbage-collection/) |\n| **Allocator** | Per-P caches, heap spans |\n| **Netpoller** | epoll/kqueue integration for network I/O |\n| **Stack management** | Growable goroutine stacks |".format(base=BASE),
        "Internal Working": textwrap.dedent(f"""
            ```mermaid
            flowchart TB
              main[main.main] --> rt[Go runtime]
              rt --> sched[Scheduler GMP]
              rt --> gc[GC]
              rt --> alloc[Allocator]
              rt --> net[Netpoller]
            ```

            **Startup:** OS loads binary → runtime initializes → `init()` functions → `main.main()`.

            **Execution:** Goroutines scheduled on Ps; blocking syscalls detach M; network waits go to netpoller.
        """),
        "Production Usage": "- Pin Go version in `go.mod` and container images.\n- Use `runtime.MemStats`, `runtime.NumGoroutine()` for coarse health — prefer [Observability]({base}/06-production-go/observability/) for production.".format(base=BASE),
        "Interview Questions": "- What are the main components of the Go runtime?\n- How does the runtime differ from deploying with a separate JVM?",
    }), title="Go Runtime", desc="Runtime architecture, components, execution flow, and runtime services.",
       short="Runtime", mod=3, mod_title="Go Internals", ref="3.1", weight=301)

    w("03-go-internals/scheduler.md", handbook_page({
        "Quick Revision": "- **G** = goroutine, **M** = OS thread, **P** = logical processor (local run queue).\n- **GOMAXPROCS** = number of Ps (default `runtime.NumCPU()`).\n- Work stealing balances load across Ps.",
        "Core Concepts": "| Concept | Detail |\n| :--- | :--- |\n| Local run queue | Each P has a queue of Gs |\n| Global queue | Overflow and idle Ps steal from here |\n| Work stealing | Idle P steals half of another P's queue |\n| Syscall block | M may block; P can run other Gs |\n| Preemption | Async preemption (Go 1.14+) for tight loops |",
        "Internal Working": textwrap.dedent("""
            ```mermaid
            flowchart TB
              g1[Goroutine G] --> p[P logical processor]
              g2[Goroutine G] --> p
              p --> m[M OS thread]
              m --> os[OS scheduler]
            ```

            **Blocking:** Channel/mutex → G parks; scheduler runs another G on P.
            **Network:** G registers with netpoller; wakes when fd ready.
        """),
        "Performance Considerations": f"- CPU-bound: `GOMAXPROCS` ≈ CPU quota in containers.\n- Don't spawn unbounded Gs — see [Concurrency Patterns]({BASE}/04-concurrency/concurrency-patterns/).",
        "Common Mistakes": "- Setting `GOMAXPROCS` to 1 on multi-core hosts without reason.\n- Assuming `go` keyword creates an OS thread.",
        "Interview Questions": "- Explain GMP.\n- What is work stealing?\n- How did preemption change in Go 1.14?",
    }), title="Scheduler", desc="GMP model, goroutine scheduling, work stealing, preemption, and scheduler internals.",
       short="Scheduler", mod=3, mod_title="Go Internals", ref="3.2", weight=302)

    w("03-go-internals/escape-analysis.md", handbook_page({
        "Quick Revision": "- **Escape analysis** decides stack vs heap allocation at compile time.\n- Heap escape → GC pressure.\n- Inspect: `go build -gcflags='-m' ./...`",
        "Core Concepts": "| Escapes when | Example |\n| :--- | :--- |\n| Returned pointer to local | `func f() *T { t := T{}; return &t }` may stay stack if inlined |\n| Assigned to interface | Boxing may heap-allocate |\n| Closure captures variable referenced outside | Variable moves to heap |\n| Size unknown at compile time | Large or dynamic |",
        "Internal Working": "Compiler runs escape analysis per function. `-m` prints `moved to heap` decisions.",
        "Performance Considerations": f"- Reduce heap allocs in hot paths — see [Performance Optimization]({BASE}/05-performance/performance-optimization/).\n- Prefer value semantics for small structs.",
        "Interview Questions": "- What is escape analysis?\n- How do closures affect escape?\n- How do you profile alloc hotspots?",
    }), title="Escape Analysis", desc="Stack vs heap, escape rules, compiler decisions, and performance impact.",
       short="Escape", mod=3, mod_title="Go Internals", ref="3.5", weight=305)

    w("04-concurrency/concurrency-patterns.md", handbook_page({
        "Quick Revision": "- **Worker pool** — fixed goroutines + job channel.\n- **Fan-out** — distribute work; **fan-in** — merge results.\n- **Pipeline** — staged channel processing.\n- **Backpressure** — bounded buffers or semaphores.",
        "Core Concepts": "| Pattern | Use when |\n| :--- | :--- |\n| Worker pool | Bounded parallelism for CPU/IO work |\n| Fan-out/in | Parallel map-reduce style |\n| Pipeline | Sequential stages with overlap |\n| Semaphore | Limit in-flight requests |\n| Context cancel | Stop all stages on deadline |",
        "Production Usage": f"- Always bound concurrency — unbounded `go` causes OOM.\n- Propagate [Context]({BASE}/04-concurrency/context/) through pipeline stages.\n- Prefer [Mutex]({BASE}/04-concurrency/mutex/) when sharing simple state beats channel choreography.",
        "Common Mistakes": "- Fan-in without WaitGroup before close.\n- Missing backpressure on fast producer / slow consumer.",
        "Interview Questions": "- Implement a worker pool.\n- How do you add backpressure?\n- Mutex vs channel for shared counter?",
    }), title="Concurrency Patterns", desc="Worker pools, fan-out, fan-in, pipelines, backpressure, and cancellation.",
       short="Patterns", mod=4, mod_title="Concurrency", ref="4.8", weight=408)

    for slug, title, desc, short, ref, weight, body in [
        ("performance-optimization", "Performance Optimization", "Allocation reduction, object reuse, memory optimization, and efficient concurrency.", "Optimization", "5.1", 501,
         f"## Quick Revision\n\n- Reduce allocations in hot paths.\n- Reuse buffers with `sync.Pool` — see [sync Package]({BASE}/04-concurrency/sync-package/).\n- Bound goroutine count.\n\n## Core Concepts\n\n| Tactic | When |\n| :--- | :--- |\n| Preallocate slices | Known upper bound on size |\n| sync.Pool | Short-lived, resettable objects |\n| Value semantics | Small immutable structs |\n| String builder | Concatenation in loops |\n\n## Performance Considerations\n\nProfile before optimizing — [Profiling]({BASE}/05-performance/profiling/)."),
        ("profiling", "Profiling", "pprof CPU, memory, goroutine profiling, trace, and performance analysis.", "Profiling", "5.2", 502,
         f"## Quick Revision\n\n- CPU: `go tool pprof http://localhost:6060/debug/pprof/profile`\n- Heap: `/debug/pprof/heap`\n- Goroutine: `/debug/pprof/goroutine`\n- Trace: `runtime/trace`\n\n## Core Concepts\n\n| Profile | Shows |\n| :--- | :--- |\n| CPU | Hot functions |\n| heap / allocs | In-use or allocated objects |\n| goroutine | Stack traces per G |\n| block / mutex | Contention |\n\n## Production Usage\n\nImport `_ \"net/http/pprof\"` on admin port only; protect with network policy."),
        ("benchmarking", "Benchmarking", "testing.B, benchmem, benchstat, and benchmark methodology.", "Benchmarking", "5.3", 503,
         "## Quick Revision\n\n- `func BenchmarkX(b *testing.B)` in `*_test.go`\n- `b.ReportAllocs()` for allocs/op\n- `benchstat old.txt new.txt` for comparison\n\n## Common Mistakes\n\n- Benchmarking debug builds.\n- Not resetting timer after setup (`b.ResetTimer()`)."),
        ("memory-optimization", "Memory Optimization", "Slice preallocation, struct layout, pointer density, and GC interaction.", "Memory", "5.4", 504,
         f"## Quick Revision\n\n- `make([]T, 0, cap)` avoids repeated growth.\n- Reorder struct fields to reduce padding.\n- Fewer pointers in heap graph → faster GC mark phase.\n\n## Performance Considerations\n\nLink alloc rate to [Garbage Collection]({BASE}/03-go-internals/garbage-collection/)."),
    ]:
        w(f"05-performance/{slug}.md", body, title=title, desc=desc, short=short, mod=5, mod_title="Performance", ref=ref, weight=weight)

    for slug, title, desc, short, ref, weight, body in [
        ("logging", "Logging", "Structured logging, log correlation, and production logging.", "Logging", "6.1", 601,
         "## Quick Revision\n\n- Use **structured logs** (slog, zap, zerolog) — key-value fields.\n- Include `request_id`, `trace_id`, `service`, `level`.\n- Log at boundaries; avoid duplicate log+return.\n\n## Production Usage\n\n- JSON logs for aggregation (ELK, Loki).\n- Correlate with [Observability]({base}/06-production-go/observability/) traces.".format(base=BASE)),
        ("configuration-management", "Configuration Management", "Environment variables, configuration loading, and secrets management.", "Config", "6.2", 602,
         "## Quick Revision\n\n- **12-factor:** config in environment.\n- Load into typed struct; validate at startup.\n- Secrets from vault/K8s secrets — never commit.\n\n## Common Mistakes\n\n- Silent defaults for missing required config."),
        ("observability", "Observability", "Metrics, tracing, OpenTelemetry, and monitoring.", "Observability", "6.3", 603,
         "## Quick Revision\n\n- **Metrics:** Prometheus `/metrics` — RED (rate, errors, duration).\n- **Tracing:** OpenTelemetry SDK — propagate W3C tracecontext.\n- **Logs:** link trace_id for correlation.\n\n## Production Usage\n\n- Alert on SLO burn rate, goroutine count, GC pause, error rate."),
        ("graceful-shutdown", "Graceful Shutdown", "Context cancellation, signal handling, resource cleanup, and shutdown patterns.", "Shutdown", "6.4", 604,
         f"## Quick Revision\n\n- Listen for `SIGTERM` / `SIGINT`.\n- `server.Shutdown(ctx)` stops accepting; drains in-flight.\n- Cancel root context; close DB pools.\n\n## Production Usage\n\n- Shutdown timeout < K8s `terminationGracePeriodSeconds`.\n- See [Context]({BASE}/04-concurrency/context/) for cancellation tree."),
        ("production-checklists", "Production Checklists", "Pre-deploy checklists, CI gates, and production readiness.", "Checklists", "6.5", 605,
         "## Checklists\n\n- [ ] `go test -race ./...` in CI\n- [ ] `staticcheck` / `govulncheck`\n- [ ] pprof admin port not public\n- [ ] Graceful shutdown tested\n- [ ] Structured logging + metrics + traces\n- [ ] Go version pinned in go.mod and image"),
    ]:
        w(f"06-production-go/{slug}.md", body, title=title, desc=desc, short=short, mod=6, mod_title="Production Go", ref=ref, weight=weight)

    for slug, title, desc, short, ref, weight, body in [
        ("mocking", "Mocking", "Interface-based testing, test doubles, and mock generation.", "Mocking", "7.2", 702,
         f"## Quick Revision\n\n- **Accept interfaces, return structs** — mock interfaces in tests.\n- Tools: `gomock`, `mockery`, hand-written fakes.\n- Prefer fakes for simple behavior; mocks for interaction verification.\n\n## Core Concepts\n\n| Double | Use |\n| :--- | :--- |\n| Fake | Working in-memory implementation |\n| Stub | Canned responses |\n| Mock | Expect call sequences |"),
        ("test-strategies", "Test Strategies", "Unit, integration, benchmark, and concurrency testing.", "Strategies", "7.3", 703,
         f"## Quick Revision\n\n- **Unit:** pure logic, table-driven.\n- **Integration:** `//go:build integration` tag, real deps in CI.\n- **Concurrency:** `go test -race`; stress tests with `-count`.\n\n## Production Usage\n\n- [Benchmarking]({BASE}/05-performance/benchmarking/) for perf regression gates."),
    ]:
        w(f"07-testing/{slug}.md", body, title=title, desc=desc, short=short, mod=7, mod_title="Testing", ref=ref, weight=weight)

    # Learning paths
    w("09-learning-paths/golang-senior-engineer-path.md",
      f"# Go Senior Engineer Path\n\n| Week | Topics |\n| :--- | :--- |\n| 1 | [Slices]({BASE}/01-fundamentals/slices/) → [Interfaces]({BASE}/02-core-go/interfaces/) → [Errors]({BASE}/02-core-go/error-handling/) |\n| 2 | [Goroutines]({BASE}/04-concurrency/goroutines/) → [Channels]({BASE}/04-concurrency/channels/) → [Context]({BASE}/04-concurrency/context/) |\n| 3 | [Scheduler]({BASE}/03-go-internals/scheduler/) → [Memory Model]({BASE}/03-go-internals/memory-model/) → [GC]({BASE}/03-go-internals/garbage-collection/) |\n| 4 | [Testing]({BASE}/07-testing/testing/) → [Profiling]({BASE}/05-performance/profiling/) → [Graceful Shutdown]({BASE}/06-production-go/graceful-shutdown/) |",
      title="Senior Engineer Path", desc="Four-week path — fundamentals through production Go.", short="Senior Path", mod=9, mod_title="Learning Paths", ref="9.1", weight=901)

    w("09-learning-paths/golang-lead-path.md",
      f"# Go Technical Lead Path\n\n1. [Concurrency Patterns]({BASE}/04-concurrency/concurrency-patterns/)\n2. [Scheduler]({BASE}/03-go-internals/scheduler/) + [Escape Analysis]({BASE}/03-go-internals/escape-analysis/)\n3. [Observability]({BASE}/06-production-go/observability/) + [Production Checklists]({BASE}/06-production-go/production-checklists/)\n4. [Troubleshooting Questions]({BASE}/08-interview-guide/troubleshooting-questions/)",
      title="Technical Lead Path", desc="Concurrency, runtime, observability, and incident response for leads.", short="Lead Path", mod=9, mod_title="Learning Paths", ref="9.2", weight=902)

    w("09-learning-paths/golang-architect-path.md",
      f"# Go Architect Path\n\n1. [Go Runtime]({BASE}/03-go-internals/go-runtime/) → [Scheduler]({BASE}/03-go-internals/scheduler/) → [GC]({BASE}/03-go-internals/garbage-collection/)\n2. [Performance Optimization]({BASE}/05-performance/performance-optimization/) + [Memory Optimization]({BASE}/05-performance/memory-optimization/)\n3. [Graceful Shutdown]({BASE}/06-production-go/graceful-shutdown/) + [Configuration]({BASE}/06-production-go/configuration-management/)\n4. [Architect Questions]({BASE}/08-interview-guide/architect-questions/)",
      title="Architect Path", desc="Runtime, performance tradeoffs, and production architecture for Go services.", short="Architect Path", mod=9, mod_title="Learning Paths", ref="9.3", weight=903)

    w("09-learning-paths/golang-interview-revision-path.md",
      f"# Go Interview Revision Path\n\n| Block | Time | Focus |\n| :--- | :--- | :--- |\n| **1** | 2h | [Interfaces]({BASE}/02-core-go/interfaces/) · [Slices]({BASE}/01-fundamentals/slices/) · [Errors]({BASE}/02-core-go/error-handling/) |\n| **2** | 2h | [Scheduler]({BASE}/03-go-internals/scheduler/) · [Memory Model]({BASE}/03-go-internals/memory-model/) · [GC]({BASE}/03-go-internals/garbage-collection/) |\n| **3** | 2h | [Channels]({BASE}/04-concurrency/channels/) · [Context]({BASE}/04-concurrency/context/) · [Patterns]({BASE}/04-concurrency/concurrency-patterns/) |\n| **4** | 2h | [Profiling]({BASE}/05-performance/profiling/) · [Graceful Shutdown]({BASE}/06-production-go/graceful-shutdown/) |\n| **5** | 2h | [Top 150 Questions]({BASE}/08-interview-guide/top-150-interview-questions/) |",
      title="Interview Revision Path", desc="48-hour cram schedule mapped to handbook topics.", short="Interview Path", mod=9, mod_title="Learning Paths", ref="9.4", weight=904)

    from golang_questions_data import QUESTIONS

    q_rows = "\n".join(
        f'| {i} | {q} | {d} | {l} | {t} | [{t}]({BASE}/{doc.replace(".md", "")}/) |'
        for i, (q, d, l, t, doc) in enumerate(QUESTIONS, 1)
    )

    w("08-interview-guide/top-150-interview-questions.md",
      f"Curated questions for **6+ year** engineers, senior engineers, tech leads, and architects. Questions only — answers on linked canonical pages.\n\n"
      f"**Distribution:** Internals & Runtime 40 · Concurrency 30 · Performance 25 · Troubleshooting 20 · Production 15 · Core Go & Testing 20\n\n"
      f"| # | Question | Difficulty | Level | Topic | Deep Dive |\n|---|----------|------------|--------|-------|----------|\n{q_rows}",
      title="Top 150 Go Interview Questions", desc="150 production-oriented Go interview questions mapped to handbook topics.",
      short="Top 150", mod=8, mod_title="Interview Guide", ref="8.1", weight=801,
      alias_paths=(f"{BASE}/interview-questions/",))

    ARCHITECT_QS = [q for q, _, l, _, _ in QUESTIONS if l == "Architect"]
    TROUBLE_QS = [QUESTIONS[i][0] for i in range(95, 115)]
    PERF_QS = [QUESTIONS[i][0] for i in range(70, 95)]

    w("08-interview-guide/architect-questions.md",
      f"Questions only — no answers. Sourced from [Top 150]({BASE}/08-interview-guide/top-150-interview-questions/).\n\n# Architect-Level Questions\n\n"
      + "\n".join(f"{i}. {q}" for i, q in enumerate(ARCHITECT_QS, 1)),
      title="Architect-Level Questions", desc="Curated architect-level Go interview questions.", short="Architect", mod=8, mod_title="Interview Guide", ref="8.2", weight=802)

    w("08-interview-guide/troubleshooting-questions.md",
      f"Questions only — no answers.\n\n# Troubleshooting Questions\n\n" + "\n".join(f"{i}. {q}" for i, q in enumerate(TROUBLE_QS, 1)),
      title="Troubleshooting Questions", desc="Production troubleshooting interview questions for Go.", short="Troubleshooting Q", mod=8, mod_title="Interview Guide", ref="8.3", weight=803)

    w("08-interview-guide/performance-questions.md",
      f"Questions only — no answers.\n\n# Performance Questions\n\n" + "\n".join(f"{i}. {q}" for i, q in enumerate(PERF_QS, 1)),
      title="Performance Questions", desc="Go performance and profiling interview questions.", short="Performance Q", mod=8, mod_title="Interview Guide", ref="8.4", weight=804)

    w("_index.md",
      f"""# Go Handbook

Production and interview knowledge base for **Senior Engineers**, **Technical Leads**, and **Architects** (6+ years). Target **Go 1.22+**.

## Learning Paths

| Track | Start here | Goal |
| :--- | :--- | :--- |
| **Quick revision** | [Interview Revision Path]({BASE}/09-learning-paths/golang-interview-revision-path/) | 48-hour cram |
| **Senior engineer** | [Senior Engineer Path]({BASE}/09-learning-paths/golang-senior-engineer-path/) | Language → concurrency → runtime → ops |
| **Technical lead** | [Lead Path]({BASE}/09-learning-paths/golang-lead-path/) | Patterns, observability, troubleshooting |
| **Architect** | [Architect Path]({BASE}/09-learning-paths/golang-architect-path/) | Runtime, performance, production tradeoffs |
| **Interview prep** | [Top 150 Questions]({BASE}/08-interview-guide/top-150-interview-questions/) | Role-specific banks |

## Modules

1. **Fundamentals** — syntax, functions, structs, collections, methods
2. **Core Go** — interfaces, pointers, packages, errors, modules
3. **Go Internals** — runtime, scheduler, memory model, GC, escape analysis, reflection
4. **Concurrency** — goroutines, channels, sync, context, patterns
5. **Performance** — optimization, profiling, benchmarking, memory
6. **Production Go** — logging, config, observability, shutdown, checklists
7. **Testing** — unit tests, mocking, strategies
8. **Interview Guide** — 150 questions + subsets
9. **Learning Paths** — curated reading by role

{{% note %}}
Design patterns, system design, and microservices patterns live in **other handbook sections** — this is **Go language + runtime + production** only.
{{% /note %}}
""",
      title="Go Handbook", desc="Go handbook — runtime, concurrency, performance, production engineering, and interview prep.",
      short="Handbook", mod=0, mod_title="Go Handbook", ref="0", weight=1)

    modules_yaml = """# Go Handbook — module index.
modules:
  - id: 1
    focus: "Fundamentals"
    topics:
      - 01-fundamentals/language-basics
      - 01-fundamentals/functions
      - 01-fundamentals/structs
      - 01-fundamentals/arrays
      - 01-fundamentals/slices
      - 01-fundamentals/maps
      - 01-fundamentals/methods

  - id: 2
    focus: "Core Go"
    topics:
      - 02-core-go/interfaces
      - 02-core-go/pointers
      - 02-core-go/packages
      - 02-core-go/go-modules
      - 02-core-go/dependency-management
      - 02-core-go/error-handling

  - id: 3
    focus: "Go Internals"
    topics:
      - 03-go-internals/go-runtime
      - 03-go-internals/scheduler
      - 03-go-internals/memory-model
      - 03-go-internals/garbage-collection
      - 03-go-internals/escape-analysis
      - 03-go-internals/reflection

  - id: 4
    focus: "Concurrency"
    topics:
      - 04-concurrency/goroutines
      - 04-concurrency/channels
      - 04-concurrency/select
      - 04-concurrency/mutex
      - 04-concurrency/rwmutex
      - 04-concurrency/sync-package
      - 04-concurrency/context
      - 04-concurrency/concurrency-patterns

  - id: 5
    focus: "Performance"
    topics:
      - 05-performance/performance-optimization
      - 05-performance/profiling
      - 05-performance/benchmarking
      - 05-performance/memory-optimization

  - id: 6
    focus: "Production Go"
    topics:
      - 06-production-go/logging
      - 06-production-go/configuration-management
      - 06-production-go/observability
      - 06-production-go/graceful-shutdown
      - 06-production-go/production-checklists

  - id: 7
    focus: "Testing"
    topics:
      - 07-testing/testing
      - 07-testing/mocking
      - 07-testing/test-strategies

  - id: 8
    focus: "Interview Guide"
    topics:
      - 08-interview-guide/top-150-interview-questions
      - 08-interview-guide/architect-questions
      - 08-interview-guide/troubleshooting-questions
      - 08-interview-guide/performance-questions

  - id: 9
    focus: "Learning Paths"
    topics:
      - 09-learning-paths/golang-senior-engineer-path
      - 09-learning-paths/golang-lead-path
      - 09-learning-paths/golang-architect-path
      - 09-learning-paths/golang-interview-revision-path
"""

    order_yaml = """# Topic order — derived from golang_cheatsheet_modules.yaml.
topics:
  - 01-fundamentals/language-basics
  - 01-fundamentals/functions
  - 01-fundamentals/structs
  - 01-fundamentals/arrays
  - 01-fundamentals/slices
  - 01-fundamentals/maps
  - 01-fundamentals/methods
  - 02-core-go/interfaces
  - 02-core-go/pointers
  - 02-core-go/packages
  - 02-core-go/go-modules
  - 02-core-go/dependency-management
  - 02-core-go/error-handling
  - 03-go-internals/go-runtime
  - 03-go-internals/scheduler
  - 03-go-internals/memory-model
  - 03-go-internals/garbage-collection
  - 03-go-internals/escape-analysis
  - 03-go-internals/reflection
  - 04-concurrency/goroutines
  - 04-concurrency/channels
  - 04-concurrency/select
  - 04-concurrency/mutex
  - 04-concurrency/rwmutex
  - 04-concurrency/sync-package
  - 04-concurrency/context
  - 04-concurrency/concurrency-patterns
  - 05-performance/performance-optimization
  - 05-performance/profiling
  - 05-performance/benchmarking
  - 05-performance/memory-optimization
  - 06-production-go/logging
  - 06-production-go/configuration-management
  - 06-production-go/observability
  - 06-production-go/graceful-shutdown
  - 06-production-go/production-checklists
  - 07-testing/testing
  - 07-testing/mocking
  - 07-testing/test-strategies
  - 08-interview-guide/top-150-interview-questions
  - 08-interview-guide/architect-questions
  - 08-interview-guide/troubleshooting-questions
  - 08-interview-guide/performance-questions
  - 09-learning-paths/golang-senior-engineer-path
  - 09-learning-paths/golang-lead-path
  - 09-learning-paths/golang-architect-path
  - 09-learning-paths/golang-interview-revision-path
"""

    (DATA / "golang_cheatsheet_modules.yaml").write_text(modules_yaml, encoding="utf-8")
    (DATA / "golang_cheatsheet_order.yaml").write_text(order_yaml, encoding="utf-8")

    OLD_FLAT = [
        "language-basics.md", "functions.md", "structs.md", "arrays.md", "slices.md", "maps.md",
        "methods.md", "interfaces.md", "pointers.md", "packages.md", "error-handling.md",
        "go-modules.md", "dependency-management.md", "goroutines.md", "channels.md", "select.md",
        "context.md", "mutex.md", "rwmutex.md", "sync-package.md", "memory-model.md",
        "garbage-collection.md", "reflection.md", "testing.md", "interview-questions.md",
    ]
    for name in OLD_FLAT:
        p = HB / name
        if p.exists():
            p.unlink()

    print("Go handbook Phase B generated successfully.")


if __name__ == "__main__":
    main()
