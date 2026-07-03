"""Full page bodies for Phase C expansion of stub Python handbook pages."""

from __future__ import annotations

BASE = "/python-cheatsheet"

EXPANDED_PAGES: dict[str, str] = {
    "05-performance/performance-optimization.md": f"""## Quick Revision

- Profile first — [Profiling]({BASE}/05-performance/profiling/) before micro-opts.
- Win on algorithm and data structure, then C extensions/NumPy, then bytecode tricks.
- Set SLO budgets (p95 latency, RSS) before tuning.

## Core Concepts

| Layer | Actions |
| :--- | :--- |
| Algorithm | Better complexity class, fewer passes |
| Data structures | `deque`, `set`, generators vs materialized lists |
| Stdlib vs native | NumPy, `orjson`, Rust/C extensions for hot loops |
| Interpreter | Locals over globals; avoid attribute chains in tight loops |

## Internal Working

Python bytecode executes under the [GIL]({BASE}/03-python-internals/gil/) in threads — CPU-bound pure Python needs processes or native code. Optimizing Python loops without measuring often fights the interpreter instead of the real bottleneck.

## Design Tradeoffs

| Choice | Trade-off |
| :--- | :--- |
| List comp vs generator | Memory vs reuse/random access |
| `__slots__` | Memory vs flexibility |
| Cython/Rust extension | Speed vs build/deploy complexity |
| Async rewrite | Throughput vs library ecosystem |

## Production Usage

- Establish baseline with `cProfile` + `tracemalloc` on representative traffic.
- Optimize top 3 cumulative-time functions only; re-profile after each change.
- Document performance assumptions in ADRs for hot services.

## Performance Considerations

- Exception-based control flow in hot paths is costly.
- String `+=` in loops — use `''.join` for many concatenations.
- Import time matters for CLI/serverless cold start.

## Troubleshooting

| Symptom | Likely cause |
| :--- | :--- |
| CPU high, few threads busy | GIL + CPU-bound Python loop |
| Memory climb per request | Unbounded list materialization or cache |
| Slow after deploy | New import side effect or logging volume |

## Common Mistakes

- Premature optimization without profiler evidence.
- Rewriting in async when workload is CPU-bound.

## Interview Questions

See [Top 150]({BASE}/09-interview-guide/top-150-interview-questions/) — Performance category.

## Architect Notes

Performance work is a **measurement discipline** — tie every change to a metric and rollback plan.
""",
    "05-performance/profiling.md": f"""## Quick Revision

- **`cProfile`** — who calls whom; cumulative vs per-call time.
- **`line_profiler`** — line hotspots in one function.
- **`tracemalloc`** / **`memory_profiler`** — allocation sites and RSS drivers.
- **`py-spy`** — sampling profiler for live processes with low overhead.

## Core Concepts

| Tool | Measures | When |
| :--- | :--- | :--- |
| `cProfile` | Function call graph | First pass CPU triage |
| `line_profiler` | Per-line time in one function | Hot function identified |
| `tracemalloc` | Allocations by traceback | Memory growth |
| `memory_profiler` | Line memory (@profile) | Heap churn in one module |
| `py-spy` | Stack samples | Production-safe sampling |

## Internal Working

```mermaid
flowchart LR
  CPU[cProfile / py-spy] --> HOT[Hot functions]
  HOT --> LINE[line_profiler]
  MEM[tracemalloc] --> SITE[Allocation sites]
  SITE --> FIX[Fix data structure / cache bound]
```

Deterministic profilers instrument every call — higher overhead. Sampling profilers approximate hotspots with less distortion under load.

## Production Usage

```python
import cProfile
import pstats
import tracemalloc

cProfile.run("main()", "out.prof")
pstats.Stats("out.prof").sort_stats("cumulative").print_stats(20)

tracemalloc.start()
# workload
for stat in tracemalloc.take_snapshot().statistics("lineno")[:10]:
    print(stat)
```

## Performance Considerations

- Profile with production-like data volume and concurrency.
- Compare snapshots (before/after deploy) for memory regressions.

## Troubleshooting

| Pattern | Next step |
| :--- | :--- |
| High cumulative in one helper | `line_profiler` that function |
| RSS up, Python heap flat | C extension or buffer off-heap |
| Spiky latency | Sample with `py-spy` under load |

## Common Mistakes

- Optimizing functions that are not on the critical path.
- Single-run benchmarks without warmup.

## Interview Questions

See [Top 150]({BASE}/09-interview-guide/top-150-interview-questions/).
""",
    "05-performance/benchmarking.md": f"""## Quick Revision

- Warmup iterations discard JIT/cache effects (less relevant in CPython than JVM, still stabilizes I/O caches).
- Report **median** and **p95** — not single best run.
- Use `timeit` for micro-benchmarks; `pytest-benchmark` for CI regression gates.

## Core Concepts

| Practice | Why |
| :--- | :--- |
| Warmup | Stabilize caches and connection pools |
| Multiple iterations | Reduce noise |
| Same hardware/CI agent | Comparable runs |
| Isolate | Close other workloads |

## Internal Working

```mermaid
sequenceDiagram
  participant Dev
  participant Bench
  participant Stats
  Dev->>Bench: warmup N iterations
  Dev->>Bench: measure M iterations
  Bench->>Stats: aggregate median/p95
  Stats-->>Dev: compare to budget
```

## Production Usage

```python
import timeit

timeit.timeit("sorted(range(1000))", number=10000)

# pytest-benchmark in CI for regression on parse_serialization()
```

## Design Tradeoffs

| Approach | Trade-off |
| :--- | :--- |
| Micro-benchmark | Precise but may not reflect system behavior |
| End-to-end load test | Realistic but noisy |
| CI benchmark gate | Catches regressions; flaky if environment varies |

## Common Mistakes

- Benchmarking debug builds or dev machines only.
- Comparing asyncio and sync without same concurrency model.

## Interview Questions

See [Top 150]({BASE}/09-interview-guide/top-150-interview-questions/).
""",
    "05-performance/memory-optimization.md": f"""## Quick Revision

- Prefer **generators** and streaming over giant lists.
- Bound caches: `lru_cache(maxsize=...)`, TTL, `weakref`.
- `__slots__` after profiling — see [Object Model]({BASE}/03-python-internals/object-model/).

## Core Concepts

| Technique | Effect |
| :--- | :--- |
| Generator pipeline | O(1) peak memory for single-pass consumers |
| Bounded cache | Prevents unbounded RSS growth |
| `__slots__` | Smaller instances at scale |
| `weakref` | Break cycles / non-owning registries |

## Internal Working

Peak memory often comes from materializing intermediate collections, not individual object size. [Garbage Collection]({BASE}/03-python-internals/garbage-collection/) reclaims cycles but does not prevent spikes from large allocations.

## Production Usage

- Stream file/HTTP responses; chunk DB reads.
- Cap in-memory buffers (`deque(maxlen=...)`).
- Monitor RSS alongside Python allocation profilers.

## Troubleshooting

```mermaid
flowchart TD
  G[RSS growing] --> C{{Global cache?}}
  C -->|yes| B[Bound or TTL]
  C -->|no| CY{{Cycles?}}
  CY -->|yes| GC[gc / weakref]
  CY -->|no| CEXT[C extension / buffer]
```

## Common Mistakes

- `lru_cache` without `maxsize` on unbounded key spaces.
- Reading multi-GB files into memory.

## Interview Questions

See [Top 150]({BASE}/09-interview-guide/top-150-interview-questions/).
""",
    "06-production-python/logging.md": f"""## Quick Revision

- One configured root hierarchy — avoid duplicate handlers.
- **Structured JSON** logs for search/alerting; include `trace_id`, `level`, `message`.
- Log once at boundary with `exc_info=True` on errors.

## Core Concepts

| Piece | Role |
| :--- | :--- |
| `Logger` | Named channel (`logging.getLogger(__name__)`) |
| `Handler` | Where records go (stdout, file, HTTP) |
| `Formatter` | Layout (JSON vs text) |
| `Filter` | Sampling, PII redaction |

## Internal Working

```mermaid
flowchart LR
  LOG[Logger] --> H[Handler]
  H --> F[Formatter]
  F --> OUT[stdout / aggregator]
```

Use `contextvars` to inject correlation IDs into log records across [asyncio]({BASE}/04-concurrency/asyncio/) tasks.

## Production Usage

```python
import logging
import json
import contextvars

request_id = contextvars.ContextVar("request_id", default="-")

class JsonFormatter(logging.Formatter):
    def format(self, record):
        return json.dumps({{
            "level": record.levelname,
            "msg": record.getMessage(),
            "request_id": request_id.get(),
            "logger": record.name,
        }})

logger = logging.getLogger("app")
handler = logging.StreamHandler()
handler.setFormatter(JsonFormatter())
logger.addHandler(handler)
logger.setLevel(logging.INFO)
```

## Troubleshooting

| Symptom | Fix |
| :--- | :--- |
| Duplicate log lines | Multiple handlers on root + child |
| Missing context | Set `ContextVar` in middleware |
| Log volume cost | INFO in hot path → DEBUG behind flag |

## Common Mistakes

- `logging.basicConfig` in libraries.
- Logging full payloads with PII.

## Interview Questions

See [Top 150]({BASE}/09-interview-guide/top-150-interview-questions/).
""",
    "06-production-python/configuration-management.md": f"""## Quick Revision

- Precedence: **defaults → config file → environment → secrets**.
- Never commit secrets; inject at runtime (vault, K8s secrets).
- `pydantic-settings` for typed, validated config.

## Core Concepts

| Source | Use |
| :--- | :--- |
| Defaults in code | Safe dev experience |
| `.env` / files | Non-secret environment-specific |
| Environment variables | 12-factor override |
| Secret store | Credentials, API keys |

## Internal Working

```mermaid
flowchart TB
  DEF[Defaults] --> FILE[Config file]
  FILE --> ENV[Environment]
  ENV --> SEC[Secrets]
  SEC --> APP[Validated Settings object]
```

## Production Usage

- Fail fast on missing required config at startup.
- Separate `DATABASE_URL` secret from feature flags.
- Document every env var in README/runbook.

## Common Mistakes

- Boolean env vars as loose strings (`"false"` is truthy).
- Same secret in repo and production without rotation.

## Interview Questions

See [Top 150]({BASE}/09-interview-guide/top-150-interview-questions/).
""",
    "06-production-python/observability.md": f"""## Quick Revision

- **Logs** — discrete events; **metrics** — aggregates; **traces** — request paths.
- OpenTelemetry for vendor-neutral traces and metrics.
- Propagate trace context across threads and asyncio.

## Core Concepts

| Pillar | Examples |
| :--- | :--- |
| Logs | JSON lines, error rate |
| Metrics | Prometheus RED: rate, errors, duration |
| Traces | Span per outbound call, DB query |

## Internal Working

```mermaid
flowchart LR
  APP[Python service] --> LOG[Logs]
  APP --> MET[Metrics]
  APP --> TR[Traces]
  MET --> PROM[Prometheus / Grafana]
  TR --> OTEL[OTLP collector]
```

```mermaid
sequenceDiagram
  participant API
  participant OTEL
  participant DB
  API->>OTEL: start span
  API->>DB: query (child span)
  DB-->>API: result
  OTEL-->>API: export trace
```

## Production Usage

- Sample traces under high traffic; always trace errors.
- Align metric labels with SLO dashboards.
- Use `contextvars` + OTEL propagators for async handlers.

## Common Mistakes

- High-cardinality metric labels (user IDs).
- Broken parent span context across thread boundaries.

## Interview Questions

See [Top 150]({BASE}/09-interview-guide/top-150-interview-questions/).
""",
    "06-production-python/error-handling.md": f"""## Quick Revision

- Catch **specific** exceptions; map to HTTP/status at **outer boundary** only.
- `raise ... from e` preserves chains for debugging.
- Retry transient errors with backoff — not all exceptions.

## Core Concepts

| Layer | Responsibility |
| :--- | :--- |
| Domain | Raise meaningful `AppError` types |
| Service | Translate infrastructure failures |
| API boundary | Map to status codes, log once |

## Production Usage

- Log with `logger.exception` or `exc_info=True` once at handler.
- Use idempotency keys for safe retries on 5xx paths.
- Distinguish client errors (4xx) from server errors (5xx).

## Common Mistakes

- Bare `except:` swallowing `KeyboardInterrupt`.
- Returning stack traces to clients in production.

## Interview Questions

See [Top 150]({BASE}/09-interview-guide/top-150-interview-questions/).
""",
    "06-production-python/production-checklists.md": f"""## Quick Revision

Pre-deploy and incident checklists for Python services in production.

## Core Concepts

### Pre-deploy

| Check | Done |
| :--- | :---: |
| `requires-python` tested in CI matrix | ☐ |
| Lock file or pinned deps for apps | ☐ |
| Structured logging configured | ☐ |
| Health + readiness endpoints | ☐ |
| Secrets from vault/env — not repo | ☐ |
| Timeouts on outbound HTTP/DB | ☐ |
| Profiling baseline for hot paths | ☐ |

### Incident (first hour)

| Step | Action |
| :--- | :--- |
| 1 | Confirm scope — error rate, latency, which endpoints |
| 2 | Check recent deploys and config changes |
| 3 | Inspect logs with correlation ID |
| 4 | Metrics: CPU, memory, event-loop lag, pool exhaustion |
| 5 | Roll back or scale if clear regression |
| 6 | Profile if CPU/memory anomaly — [Profiling]({BASE}/05-performance/profiling/) |

## Production Usage

- Run tabletop exercises on checklists quarterly.
- Link runbooks from alerts.

## Interview Questions

See [Top 150]({BASE}/09-interview-guide/top-150-interview-questions/).
""",
    "08-testing/testing.md": f"""## Quick Revision

- **Pyramid:** many unit, fewer integration, minimal e2e.
- Unit tests: fast, isolated, no network.
- Integration tests: real DB/message broker in containers.

## Core Concepts

| Level | Scope | Speed |
| :--- | :--- | :--- |
| Unit | One module/class | ms |
| Integration | DB, HTTP, queue | seconds |
| E2E | Full stack | minutes |

## Internal Working

```mermaid
flowchart TB
  UNIT[Unit tests - many] --> INT[Integration - some]
  INT --> E2E[E2E - few]
```

## Production Usage

- CI order: lint → typecheck → unit → integration.
- Fail fast; parallelize unit tests.
- Coverage on critical domains — not 100% everywhere.

## Common Mistakes

- Integration tests depending on prod APIs.
- No tests for packaging/import paths.

## Interview Questions

See [Top 150]({BASE}/09-interview-guide/top-150-interview-questions/).
""",
    "08-testing/pytest.md": f"""## Quick Revision

- Fixtures in `conftest.py` — scoped `function`, `module`, `session`.
- `@pytest.mark.parametrize` for table-driven cases.
- `pytest.raises` for exception contracts.

## Core Concepts

| Feature | Use |
| :--- | :--- |
| `fixture` | Setup/teardown reuse |
| `parametrize` | Many inputs, one test function |
| `mark` | slow, integration, skip |
| `monkeypatch` | Env/path stubs |

## Production Usage

```python
import pytest

@pytest.fixture
def client():
    app = create_app(testing=True)
    with app.test_client() as c:
        yield c

@pytest.mark.parametrize("status", [200, 404])
def test_health(client, status):
    ...
```

## Common Mistakes

- Shared mutable fixture state between tests.
- Over-broad `autouse=True` fixtures slowing all tests.

## Interview Questions

See [Top 150]({BASE}/09-interview-guide/top-150-interview-questions/).
""",
    "08-testing/mocking.md": f"""## Quick Revision

- **`patch` where the name is used**, not where defined.
- `Mock` / `MagicMock` for collaborators; `spec` for interface safety.
- Prefer fakes over mocks for complex domain behavior.

## Core Concepts

| Tool | When |
| :--- | :--- |
| `patch("pkg.module.func")` | Replace at import site in module under test |
| `Mock(return_value=...)` | Stub return |
| `side_effect` | Exceptions or dynamic returns |

## Internal Working

```mermaid
sequenceDiagram
  participant Test
  participant ModuleUnderTest
  participant PatchedAPI
  Test->>ModuleUnderTest: call function
  ModuleUnderTest->>PatchedAPI: import-time binding
  PatchedAPI-->>ModuleUnderTest: mock return
```

## Production Usage

```python
from unittest.mock import patch, MagicMock

@patch("myapp.service.http_client.get")
def test_fetch(mock_get):
    mock_get.return_value = MagicMock(status_code=200, json=lambda: {{"ok": True}})
    assert fetch_status() == "ok"
```

## Common Mistakes

- Patching `requests.get` when code uses `from requests import get`.
- Mocking so much that test only asserts mock was called.

## Interview Questions

See [Top 150]({BASE}/09-interview-guide/top-150-interview-questions/).
""",
    "08-testing/test-strategies.md": f"""## Quick Revision

- CI gates: ruff/mypy → unit → integration.
- Property-based (`hypothesis`) for parsers and serializers.
- Record/replay fixtures for external APIs — scrub secrets.

## Core Concepts

| Strategy | Purpose |
| :--- | :--- |
| Contract tests | API schema stability |
| Property-based | Edge case discovery |
| Snapshot tests | Careful — avoid brittle JSON dumps |
| Load tests | Separate pipeline, not every PR |

## Production Usage

- Mark slow tests; run nightly if needed.
- Flaky test policy: fix or quarantine — never ignore.
- Test minimum Python version from `requires-python`.

## Common Mistakes

- Chasing 100% coverage on UI glue code.
- Parallel integration tests on shared DB without isolation.

## Interview Questions

See [Top 150]({BASE}/09-interview-guide/top-150-interview-questions/).
""",
    "04-concurrency/concurrency-patterns.md": f"""## Quick Revision

- **Thread pool** — blocking I/O; **process pool** — CPU-bound Python.
- **Bounded `Queue`** — producer-consumer with backpressure.
- **`asyncio.Semaphore`** — cap concurrent coroutines.

## Core Concepts

| Pattern | Tool |
| :--- | :--- |
| Thread pool | `ThreadPoolExecutor` |
| Process pool | `ProcessPoolExecutor` |
| Producer-consumer | `queue.Queue(maxsize=N)` |
| Async rate limit | `asyncio.Semaphore` |

## Internal Working

```mermaid
flowchart TB
  W[Workload] --> IO{{I/O bound?}}
  IO -->|yes| TP[ThreadPool / asyncio]
  IO -->|no| CPU{{CPU Python?}}
  CPU -->|yes| PP[ProcessPool]
  CPU -->|no| NATIVE[NumPy / C ext]
```

```mermaid
sequenceDiagram
  participant P as Producer
  participant Q as Bounded Queue
  participant C as Consumer
  P->>Q: put (blocks if full)
  Q->>C: get
  C->>C: process
```

## Production Usage

```python
from concurrent.futures import ThreadPoolExecutor, as_completed
from queue import Queue
import asyncio

async def bounded_fetch(urls, limit=10):
    sem = asyncio.Semaphore(limit)
    async def one(url):
        async with sem:
            return await client.get(url)
    return await asyncio.gather(*(one(u) for u in urls))
```

## Design Tradeoffs

| Pattern | Risk |
| :--- | :--- |
| Unbounded queue | Memory blowup under slow consumers |
| Huge thread pool | FD exhaustion, context switching |
| Tiny process pool | Queue backlog, latency |

## Performance Considerations

- Pool size ≈ downstream connection limits, not CPU count alone.
- Batch work to amortize IPC/pickle in process pools.

## Common Mistakes

- No shutdown protocol for worker threads (`Queue.join` + sentinels).
- Process pool for sub-millisecond tasks.

## Interview Questions

See [Top 150]({BASE}/09-interview-guide/top-150-interview-questions/).
""",
}
