"""Phase C: answer layer, P0 mermaid, page depth, Top 150 anchors, See Also."""
from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

import yaml

from golang_answer_engine import (
    QUESTIONS,
    craft_answer,
    format_answer_block,
    slug_anchor,
)

ROOT = Path(__file__).resolve().parents[1]
HB = ROOT / "content" / "golang-cheatsheet"
DATA = ROOT / "data"
BASE = "/golang-cheatsheet"
TOP150 = HB / "08-interview-guide/top-150-interview-questions.md"

ANSWER_START = "<!-- interview-answers:start -->"
ANSWER_END = "<!-- interview-answers:end -->"

SKIP_ANSWER_PREFIXES = (
    "08-interview-guide/top-150",
    "08-interview-guide/architect-questions",
    "08-interview-guide/troubleshooting-questions",
    "08-interview-guide/performance-questions",
    "08-interview-guide/_index",
    "09-learning-paths/_index",
)

MERMAID_P0: dict[str, str] = {
    "02-core-go/interfaces.md": """
```mermaid
flowchart TB
  nil_iface["nil interface<br/>type=nil data=nil"] --> ok["i == nil true"]
  typed_nil["interface with typed nil<br/>type=*T data=nil"] --> bad["i == nil false"]
```
""",
    "03-go-internals/go-runtime.md": """
```mermaid
flowchart TB
  main[main.main] --> rt[runtime]
  rt --> sched[scheduler GMP]
  rt --> gc[garbage collector]
  rt --> alloc[memory allocator]
  rt --> net[netpoller]
```
""",
    "03-go-internals/scheduler.md": """
```mermaid
flowchart LR
  p1[P1 local queue] -->|work stealing| p2[P2 local queue]
  gq[global run queue] --> p1
  gq --> p2
```
""",
    "03-go-internals/escape-analysis.md": """
```mermaid
flowchart TD
  Q[Variable lifetime?] --> S{Escapes function?}
  S -->|no| ST[Stack frame]
  S -->|yes| H[Heap object]
  H --> GC[GC tracked]
```
""",
    "03-go-internals/memory-model.md": """
```mermaid
sequenceDiagram
  participant G1 as Goroutine A
  participant Ch as Channel
  participant G2 as Goroutine B
  G1->>Ch: send completes
  Ch->>G2: receive completes
  Note over G1,G2: send happens-before receive
```
""",
    "03-go-internals/garbage-collection.md": """
```mermaid
flowchart TB
  mut[Mutator] --> wb[write barrier]
  wb --> mark[concurrent mark]
  mark --> stw[short STW phases]
  stw --> sweep[sweep]
```
""",
    "04-concurrency/concurrency-patterns.md": """
```mermaid
flowchart LR
  jobs[jobs chan] --> w1[worker]
  jobs --> w2[worker]
  jobs --> w3[worker]
  w1 --> out[results chan]
  w2 --> out
  w3 --> out
```

```mermaid
flowchart TB
  in[input] --> f1[stage 1]
  f1 --> f2[stage 2]
  f2 --> f3[stage 3]
  f3 --> out[output]
```
""",
    "04-concurrency/channels.md": """
```mermaid
sequenceDiagram
  participant S as Sender
  participant C as Unbuffered chan
  participant R as Receiver
  S->>C: send blocks
  C->>R: rendezvous
  R->>C: receive unblocks send
```
""",
    "04-concurrency/context.md": """
```mermaid
flowchart TB
  root[context.Background] --> parent[parent ctx]
  parent --> child1[WithCancel child]
  parent --> child2[WithTimeout child]
  parent -->|cancel| child1
  parent -->|deadline| child2
```
""",
    "05-performance/profiling.md": """
```mermaid
flowchart TD
  A[Latency SLO miss] --> B[Capture CPU profile]
  B --> C[Capture heap/allocs]
  C --> D[Identify hot path]
  D --> E[Fix + benchstat]
  E --> F[Validate in staging]
```
""",
    "06-production-go/graceful-shutdown.md": """
```mermaid
sequenceDiagram
  participant K8s
  participant App
  participant DB
  K8s->>App: SIGTERM
  App->>App: stop accepting new requests
  App->>App: Shutdown(ctx) drain
  App->>DB: close pools
  App->>K8s: exit 0
```
""",
    "06-production-go/observability.md": """
```mermaid
flowchart LR
  req[HTTP request] --> trace[OTel trace]
  trace --> metrics[Prometheus metrics]
  trace --> logs[structured logs]
  logs --> corr[shared trace_id]
```
""",
}

# Sections appended/replaced on thin handbook pages (before answers)
PAGE_EXPANSIONS: dict[str, str] = {
    "03-go-internals/go-runtime.md": """
## Runtime Behavior

1. OS loads binary → runtime initializes scheduler, memory allocator, GC.
2. Package `init()` functions run in dependency order.
3. `main.main` starts — typically spawns goroutines for servers/workers.
4. Process exits when main returns (or `os.Exit`) — all goroutines terminated.

## Design Tradeoffs

| Choice | Trade-off |
| :--- | :--- |
| Static binary | Simple deploy vs larger artifact than dynamic linking |
| Embedded runtime | Predictable behavior vs no external JVM-style tuning agent |
| Cooperative + preemptive scheduling | Low overhead vs rare long-run goroutine starvation pre-1.14 |

## Troubleshooting

| Symptom | Check |
| :--- | :--- |
| High RSS | Heap profile, goroutine count |
| Startup slow | `init()` side effects, large global maps |
| Mystery CPU | CPU profile, GC trace |
""",
    "03-go-internals/scheduler.md": """
## Runtime Behavior

- **Runnable** Gs sit on P local queues or global queue.
- **Running** G executes on an M bound to a P.
- **Blocked** G is parked (channel, mutex, syscall, network).
- On syscall block, M may detach from P; P runs other Gs on another M.

## Design Tradeoffs

| Knob | Effect |
| :--- | :--- |
| `GOMAXPROCS` | Upper bound on parallel OS-thread execution of Go code |
| More goroutines than CPUs | OK for I/O bound; oversubscription hurts CPU-bound |
| GOMAXPROCS > CPU quota | Throttling and latency inflation in cgroups |

## Architect Notes

Scheduler behavior explains why **CPU-bound worker count** should track cores, while **I/O-bound** workloads can use larger goroutine counts with bounded semaphores.
""",
    "03-go-internals/escape-analysis.md": """
## Internal Working

```bash
go build -gcflags="-m" ./...
```

Look for `moved to heap` lines. Common escape drivers:

- Returning `&local` (may stay stack if inlined and not leaked).
- Assigning to `interface{}` / `any`.
- Closure escaping outer scope.
- Sending pointer on channel stored beyond frame.

## Performance Considerations

Heap objects participate in GC scan. Reducing pointers in hot structs lowers mark cost.

## Checklists

- [ ] Run `-m` on packages with high allocs/op in benchmarks
- [ ] Compare value vs pointer receiver for hot structs
""",
    "04-concurrency/concurrency-patterns.md": """
## Internal Working

**Worker pool sketch:**

```go
func workerPool(ctx context.Context, jobs <-chan Job, n int) <-chan Result {
    out := make(chan Result)
    var wg sync.WaitGroup
    for i := 0; i < n; i++ {
        wg.Add(1)
        go func() {
            defer wg.Done()
            for {
                select {
                case <-ctx.Done():
                    return
                case j, ok := <-jobs:
                    if !ok {
                        return
                    }
                    out <- process(j)
                }
            }
        }()
    }
    go func() { wg.Wait(); close(out) }()
    return out
}
```

**Backpressure:** size `jobs` channel to limit queued work; use semaphore for in-flight HTTP calls.

## Performance Considerations

Pool size ≈ CPU cores for CPU work; higher for I/O with bounded semaphore.

## Troubleshooting

| Symptom | Likely cause |
| :--- | :--- |
| Goroutine count grows forever | Missing ctx cancel or blocked send |
| Deadlock | WaitGroup mismatch, send without receiver |
""",
    "05-performance/profiling.md": """
## Core Concepts

| Profile | Endpoint / flag | Shows |
| :--- | :--- | :--- |
| CPU | `/debug/pprof/profile?seconds=30` | On-CPU stacks |
| Heap | `/debug/pprof/heap` | In-use objects |
| Allocs | `/debug/pprof/allocs` | Allocation sites |
| Goroutine | `/debug/pprof/goroutine` | Stack per G |
| Block | `runtime.SetBlockProfileRate` | Blocking on sync |
| Mutex | `runtime.SetMutexProfileFraction` | Mutex contention |
| Trace | `go tool trace` | Scheduler, STW, goroutine events |

## Production Usage

```go
import _ "net/http/pprof"

go func() {
    http.ListenAndServe("localhost:6060", nil)
}()
```

Bind admin port to loopback or private network only.

## Troubleshooting

Compare **flat** vs **cum** in `go tool pprof` — flat is time in function; cum includes callees.
""",
    "05-performance/performance-optimization.md": """
## Core Concepts

| Tactic | Mechanism |
| :--- | :--- |
| Preallocate slices | Fewer grow copies |
| sync.Pool | Reuse transient buffers |
| strings.Builder | Avoid N² string concat |
| Pass `[]byte` | Reduce string conversions |
| Value receivers | Fewer heap objects |
| Bounded workers | Stable goroutine count |

## Design Tradeoffs

| sync.Pool | Custom free list |
| :--- | :--- |
| GC may clear pool anytime | Predictable reuse |
| Low boilerplate | Must size and audit manually |

## Checklists

- [ ] Baseline benchmark with `-benchmem`
- [ ] CPU + allocs profile before change
- [ ] benchstat compare after change
""",
    "05-performance/benchmarking.md": """
## Internal Working

```go
func BenchmarkFoo(b *testing.B) {
    b.ReportAllocs()
    data := setup()
    b.ResetTimer()
    for i := 0; i < b.N; i++ {
        Foo(data)
    }
}
```

```bash
go test -bench=. -benchmem -count=10 ./... > old.txt
# after change
go test -bench=. -benchmem -count=10 ./... > new.txt
benchstat old.txt new.txt
```

## Common Mistakes

- Benchmarking with `-race` (slow, different behavior).
- Not calling `ResetTimer` after expensive setup.
""",
    "05-performance/memory-optimization.md": """
## Internal Working

Struct padding example — reorder fields to reduce size:

```go
type Bad struct {
    a bool    // 1 + 7 pad
    b int64   // 8
    c bool    // 1 + 7 pad
} // 24 bytes

type Good struct {
    b int64   // 8
    a bool    // 1
    c bool    // 1 + 5 pad
} // 16 bytes
```

## Production Usage

Align optimization with GC: fewer pointers → faster mark phase.
""",
    "06-production-go/logging.md": """
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
""",
    "06-production-go/configuration-management.md": """
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
""",
    "06-production-go/observability.md": """
## Core Concepts

| Pillar | Go tooling |
| :--- | :--- |
| Metrics | Prometheus client_golang |
| Traces | OpenTelemetry Go SDK |
| Logs | slog + trace_id injection |

## Production Usage

Export RED metrics: request rate, errors, duration histograms. Propagate `traceparent` header through HTTP/gRPC middleware.

## Architect Notes

Observability is part of the **public contract** of a service — define required fields and cardinality limits before launch.
""",
    "06-production-go/graceful-shutdown.md": """
## Core Concepts

```go
srv := &http.Server{Addr: ":8080", Handler: mux}
go func() { srv.ListenAndServe() }()

stop := make(chan os.Signal, 1)
signal.Notify(stop, syscall.SIGINT, syscall.SIGTERM)
<-stop

ctx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
defer cancel()
_ = srv.Shutdown(ctx)
```

## Production Usage

- Stop accepting new work first.
- Wait for in-flight requests (Shutdown).
- Cancel background workers via context.
- Close DB/redis connections.

## Common Mistakes

- Shutdown timeout longer than K8s grace period.
- Not closing subscribers/consumers.
""",
    "06-production-go/production-checklists.md": """
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
""",
    "07-testing/mocking.md": """
## Core Concepts

```go
type Store interface {
    Get(ctx context.Context, id string) (Item, error)
}

type fakeStore struct{ data map[string]Item }

func (f *fakeStore) Get(ctx context.Context, id string) (Item, error) {
    item, ok := f.data[id]
    if !ok {
        return Item{}, ErrNotFound
    }
    return item, nil
}
```

## Production Usage

- **Fake** — in-memory working implementation for most tests.
- **Mock** (gomock/mockery) — verify call counts/order on complex collaborators.
- Keep interfaces small at package boundaries.

## Common Mistakes

- Mocking concrete types instead of interfaces.
- Testing mock expectations instead of behavior.
""",
    "07-testing/test-strategies.md": """
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
""",
}


def load_topic_order() -> list[str]:
    order = yaml.safe_load((DATA / "golang_cheatsheet_order.yaml").read_text(encoding="utf-8"))
    return order["topics"]


def topic_url(slug: str) -> str:
    return f"{BASE}/{slug}/"


def title_from_slug(slug: str) -> str:
    return slug.split("/")[-1].replace("-", " ").title()


def strip_front_matter(text: str) -> tuple[str, str]:
    if text.startswith("---"):
        end = text.index("---", 3) + 3
        return text[:end], text[end:].lstrip("\n")
    return "", text


def remove_section(body: str, heading: str) -> str:
    pattern = rf"\n## {re.escape(heading)}[\s\S]*?(?=\n## |\Z)"
    return re.sub(pattern, "", body, count=1)


def remove_old_answers(body: str) -> str:
    if ANSWER_START in body and ANSWER_END in body:
        return re.sub(
            rf"\n?{re.escape(ANSWER_START)}[\s\S]*?{re.escape(ANSWER_END)}\n?",
            "\n",
            body,
        )
    return body


def build_see_also(slug: str, topics: list[str]) -> str:
    if slug not in topics:
        return ""
    idx = topics.index(slug)
    lines = ["## See Also", ""]
    if idx > 0:
        prev = topics[idx - 1]
        lines.append(f"- [Previous: {title_from_slug(prev)}]({topic_url(prev)})")
    if idx < len(topics) - 1:
        nxt = topics[idx + 1]
        lines.append(f"- [Next: {title_from_slug(nxt)}]({topic_url(nxt)})")
    lines.append(f"- [Go Handbook Index]({BASE}/)")
    lines.append(f"- [Top 150 Interview Questions]({BASE}/08-interview-guide/top-150-interview-questions/)")
    return "\n".join(lines) + "\n"


def insert_mermaid(rel_path: str, body: str) -> str:
    snippet = MERMAID_P0.get(rel_path)
    if not snippet or snippet.strip() in body:
        return body
    for heading in ("## Internal Working", "## Core Concepts", "## Quick Revision"):
        if heading in body:
            return body.replace(heading, f"{heading}\n{snippet.strip()}\n", 1)
    return body.rstrip() + "\n\n" + snippet.strip() + "\n"


def apply_page_expansion(rel_path: str, body: str) -> str:
    extra = PAGE_EXPANSIONS.get(rel_path)
    if not extra or extra.strip() in body:
        return body
    body = remove_section(body, "Interview Questions")
    marker = ANSWER_START if ANSWER_START in body else None
    if marker:
        idx = body.index(marker)
        return body[:idx].rstrip() + "\n\n" + extra.strip() + "\n\n" + body[idx:]
    return body.rstrip() + "\n\n" + extra.strip() + "\n"


def fix_production_notes(body: str, rel_path: str) -> str:
    generic = "- See [Effective Go](https://go.dev/doc/effective_go) for idioms."
    replacements = {
        "01-fundamentals/slices.md": "- Preallocate when size known; watch subslice leaks on large backing arrays.",
        "02-core-go/interfaces.md": "- Accept interfaces at API boundaries; return concrete types. Test nil-interface JSON edge cases.",
        "02-core-go/error-handling.md": "- Wrap with context at boundaries; use `errors.Is/As` at handlers — never log and return same error.",
        "04-concurrency/goroutines.md": "- Bound goroutine count; always pair spawn with exit/cancel path.",
        "04-concurrency/channels.md": "- Document channel ownership (who closes). Prefer context cancel for shutdown.",
        "07-testing/testing.md": "- Run `go test -race` in CI for concurrent packages.",
    }
    if generic in body and rel_path in replacements:
        return body.replace(generic, replacements[rel_path])
    if generic in body:
        return body.replace(generic, "- Apply patterns from this page in code review and incident postmortems.")
    return body


def append_answers(body: str, blocks: list[str]) -> str:
    if not blocks:
        return body
    body = remove_section(body, "Interview Questions")
    section = (
        f"\n{ANSWER_START}\n\n"
        "# Interview Answers (Top 150)\n\n"
        + "".join(blocks)
        + f"{ANSWER_END}\n"
    )
    return body.rstrip() + "\n" + section


def group_questions_by_page() -> dict[str, list[tuple]]:
    groups: dict[str, list[tuple]] = defaultdict(list)
    for num, (question, difficulty, level, topic, doc) in enumerate(QUESTIONS, 1):
        groups[doc].append((num, question, difficulty, level, topic, doc))
    return groups


def build_answer_blocks(rows: list[tuple]) -> list[str]:
    blocks = []
    for num, question, _d, _l, topic, doc in sorted(rows, key=lambda r: r[0]):
        sections = craft_answer(num, question, topic, doc)
        blocks.append(format_answer_block(question, sections))
    return blocks


def update_topic_pages(topics: list[str], groups: dict[str, list[tuple]]) -> int:
    count = 0
    for slug in topics:
        rel = f"{slug}.md"
        path = HB / rel
        if not path.exists():
            continue
        if any(slug.startswith(p) for p in SKIP_ANSWER_PREFIXES):
            continue
        fm, body = strip_front_matter(path.read_text(encoding="utf-8"))
        body = remove_old_answers(body)
        body = apply_page_expansion(rel, body)
        body = insert_mermaid(rel, body)
        body = fix_production_notes(body, rel)
        blocks = build_answer_blocks(groups.get(rel, []))
        body = append_answers(body, blocks)
        body = remove_section(body, "See Also")
        body = body.rstrip() + "\n\n---\n\n" + build_see_also(slug, topics)
        path.write_text(fm + "\n\n" + body.lstrip("\n"), encoding="utf-8")
        count += 1
    return count


def deep_dive_link(num: int, question: str, doc: str) -> str:
    slug = doc.replace(".md", "")
    anchor = slug_anchor(question)
    label = title_from_slug(slug)
    return f"[{label} — Q{num}]({topic_url(slug)}#{anchor})"


def update_top150() -> None:
    text = TOP150.read_text(encoding="utf-8")
    out = []
    for line in text.splitlines():
        m = re.match(
            r"^\| (\d+) \| (.+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| \[([^\]]+)\]\(([^)]+)\) \|",
            line,
        )
        if m:
            num = int(m.group(1))
            question = m.group(2)
            doc_path = m.group(7).replace(BASE + "/", "").strip("/").rstrip("/")
            if not doc_path.endswith(".md"):
                doc_path += ".md"
            link = deep_dive_link(num, question, doc_path)
            out.append(
                f"| {num} | {question} | {m.group(3).strip()} | {m.group(4).strip()} | "
                f"{m.group(5).strip()} | {link} |"
            )
        else:
            out.append(line)
    TOP150.write_text("\n".join(out) + "\n", encoding="utf-8")


def main() -> None:
    topics = load_topic_order()
    nav_topics = [
        t for t in topics
        if not t.startswith("08-interview-guide/") and not t.startswith("09-learning-paths/")
    ]
    groups = group_questions_by_page()
    n = update_topic_pages(nav_topics, groups)
    update_top150()
    total_answers = sum(len(v) for v in groups.values())
    print(
        f"Phase C complete: {n} topic pages, {total_answers} answer blocks, "
        f"P0 mermaid on {len(MERMAID_P0)} pages, {len(PAGE_EXPANSIONS)} expansions."
    )


if __name__ == "__main__":
    main()
