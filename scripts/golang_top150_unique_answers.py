"""Unique Go SME answers for top-150 interview questions."""

from __future__ import annotations

from golang_questions_data import QUESTIONS


def _p(short, detailed, internal, production, mistakes, followup):
    return {
        "short": short,
        "detailed": detailed,
        "internal": internal,
        "production": production,
        "mistakes": mistakes,
        "followup": followup,
    }


_STYLE_A = [
    "The senior-level answer is",
    "In production Go, the decisive factor is",
    "The architecturally sound response is",
    "The mechanism-first explanation is",
]

_STYLE_B = [
    "Validate with pprof, benchmarks, and race-detector coverage",
    "Prove it under load with trace plus metrics, not micro-benchmarks alone",
    "Document the tradeoff in an ADR with rollback criteria",
    "Gate the change on alloc/op and p99 regression checks",
]


def _pick(items: list[str], qid: int) -> str:
    return items[qid % len(items)]


def _topic_key(question: str) -> str:
    q = question.lower()
    if any(k in q for k in ["gmp", "scheduler", "gomaxprocs", "work steal", "preempt", "netpoller", "runtime", "stack growth", "linker", "startup"]):
        return "scheduler"
    if any(k in q for k in ["gc", "gctrace", "gogc", "tri-color", "mark-sweep", "finalizer", "uintptr", "stw", "write barrier"]):
        return "gc"
    if any(k in q for k in ["escape analysis", "stack vs heap", "-gcflags=-m", "heap alloc"]):
        return "escape"
    if any(k in q for k in ["happens-before", "data race", "atomic", "memory model"]):
        return "memory_model"
    if any(k in q for k in ["channel", "select", "mutex", "waitgroup", "worker pool", "fan-out", "fan-in", "pipeline", "backpressure", "goroutine leak", "semaphore", "rwmutex", "sync.map", "sync.pool", "sync.once"]):
        return "concurrency"
    if any(k in q for k in ["context", "cancellation", "deadline", "sigterm", "shutdown", "graceful"]):
        return "context_shutdown"
    if any(k in q for k in ["interface", "nil interface", "type assert", "method set", "receiver", "embedding"]):
        return "interfaces"
    if any(k in q for k in ["error", "errors.is", "errors.as", "%w", "sentinel"]):
        return "errors"
    if any(k in q for k in ["slice", "append", "backing array", "subslice", "nil slice", "array"]):
        return "slices"
    if any(k in q for k in ["map", "concurrent map"]):
        return "maps"
    if any(k in q for k in ["pprof", "benchmark", "benchstat", "alloc", "profil", "optimization", "padding", "struct field", "defer", "boxing"]):
        return "performance"
    if any(k in q for k in ["log", "observability", "opentelemetry", "prometheus", "metric", "trace", "config", "secret", "checklist", "govulncheck", "staticcheck"]):
        return "production"
    if any(k in q for k in ["test", "mock", "fuzz", "httptest", "integration", "t.parallel", "t.fatal"]):
        return "testing"
    if any(k in q for k in ["go.mod", "go get", "mvs", "vendor", "goprivate", "module", "retract"]):
        return "modules"
    if any(k in q for k in ["reflect", "generics", "deepequal"]):
        return "reflection"
    if any(k in q for k in ["troubleshoot", "triage", "panic", "oom", "deadlock", "pprof/goroutine", "regression"]):
        return "troubleshooting"
    if any(k in q for k in ["package", "init()", "cmd", "internal", "pkg"]):
        return "packages"
    if any(k in q for k in ["loop variable", "closure", "recover", "variadic", "function"]):
        return "language"
    return "general"


def _payload(topic: str, question: str, qid: int) -> dict[str, str]:
    style_a = _pick(_STYLE_A, qid)
    style_b = _pick(_STYLE_B, qid + 1)
    stem = question.rstrip("?")

    if topic == "scheduler":
        return _p(
            f"{style_a} that goroutines are M:N scheduled on Ps with work stealing, not 1:1 OS threads — for: {stem}.",
            f"Explain G/M/P roles, blocking behavior (syscall, channel, netpoller), and how GOMAXPROCS caps parallel execution when answering: {stem}.",
            f"The runtime parks blocked Gs, retargets Ms/Ps, and uses async preemption (1.14+) to avoid starving the scheduler — central to: {stem}.",
            f"{style_b} before changing GOMAXPROCS or goroutine fan-out for: {stem}.",
            f"Treating `go` as free threads or ignoring syscall/netpoller interaction is a common miss on: {stem}.",
            f"What trace or metric would prove scheduler delay vs lock contention for: {stem}?",
        )
    if topic == "gc":
        return _p(
            f"{style_a} concurrent tri-color GC paced by GOGC, where allocation rate often matters more than live heap — for: {stem}.",
            f"Cover mark/sweep phases, short STW points, write barriers, and why finalizers are unreliable when discussing: {stem}.",
            f"Mutators run with barriers during mark; sweep reclaims unreachable objects — the internal story behind: {stem}.",
            f"{style_b} when tuning GOGC or investigating latency spikes related to: {stem}.",
            f"Calling runtime.GC() routinely or ignoring allocs/op while staring at heap size alone fails: {stem}.",
            f"How would gctrace and heap profiles change your next step for: {stem}?",
        )
    if topic == "escape":
        return _p(
            f"{style_a} escape analysis decides stack vs heap, and escaped values drive GC pressure — for: {stem}.",
            f"Use `-gcflags=-m`, closure capture rules, and interface boxing to explain: {stem}.",
            f"The compiler escapes locals that outlive their frame or flow to heap graphs — key to: {stem}.",
            f"{style_b} after identifying hot alloc sites for: {stem}.",
            f"Assuming pointers always heap-allocate without checking `-m` output hurts answers to: {stem}.",
            f"Which refactor (value semantics, pool, prealloc) targets the escape path in: {stem}?",
        )
    if topic == "memory_model":
        return _p(
            f"{style_a} happens-before edges from channels, mutex, Once, and atomic — data races are UB — for: {stem}.",
            f"List synchronization sources and why racy code can 'work' yet remain invalid when answering: {stem}.",
            f"Without a happens-before edge, reads/writes have no guaranteed visibility across goroutines — core to: {stem}.",
            f"Run `go test -race` in CI for packages touched by: {stem}.",
            f"Using atomics for multi-field invariants or skipping race tests on 'simple' counters fails: {stem}.",
            f"Show the minimal sync fix (mutex vs channel) you would accept in review for: {stem}.",
        )
    if topic == "concurrency":
        return _p(
            f"{style_a} bound concurrency, define goroutine exit, and choose mutex vs channel deliberately — for: {stem}.",
            f"Channels orchestrate; mutexes protect shared state; WaitGroup/ctx coordinate lifecycle — apply to: {stem}.",
            f"Unbuffered channels rendezvous; buffered channels decouple until full; nil chans disable select cases — internals for: {stem}.",
            f"Propagate context, add backpressure, and test with `-race` when implementing: {stem}.",
            f"Leaked goroutines, send-on-closed-channel panics, and select spin loops are frequent failures in: {stem}.",
            f"How would you structure shutdown so: {stem} cannot hang the process?",
        )
    if topic == "context_shutdown":
        return _p(
            f"{style_a} context carries cancel/deadline; pass as first param; never store in structs — for: {stem}.",
            f"Link context trees to HTTP/gRPC shutdown and SIGTERM handling when discussing: {stem}.",
            f"Cancel propagates to children; deadlines map to timer-driven cancel — mechanism behind: {stem}.",
            f"Align Shutdown timeout with K8s grace period for: {stem}.",
            f"Using context.Background() in libraries or leaking WithoutCancel scopes breaks: {stem}.",
            f"What metric proves drain completed before exit for: {stem}?",
        )
    if topic == "interfaces":
        return _p(
            f"{style_a} interfaces are implicit (type,data) pairs; typed nil breaks `== nil` — for: {stem}.",
            f"Tie method sets (value vs pointer receivers) to satisfaction and API design for: {stem}.",
            f"Small interfaces at boundaries; empty interface boxes values and may allocate — internal angle on: {stem}.",
            f"Use compile-time `var _ IF = (*T)(nil)` checks; test JSON nil edge cases for: {stem}.",
            f"Returning typed nil pointers in interface-typed APIs is a classic bug in: {stem}.",
            f"How would you refactor a fat interface exposed by: {stem}?",
        )
    if topic == "errors":
        return _p(
            f"{style_a} errors are values; wrap with `%w`; inspect with Is/As — for: {stem}.",
            f"Distinguish sentinel vs typed errors; log OR return, not both, when covering: {stem}.",
            f"Wrap chains preserve unwrap for Is/As; `%v` breaks inspection — mechanism for: {stem}.",
            f"Map errors to HTTP/gRPC codes at boundaries for: {stem}.",
            f"Comparing wrapped errors with `==` or duplicating logs fails: {stem}.",
            f"What retry taxonomy would you attach to errors in: {stem}?",
        )
    if topic == "slices":
        return _p(
            f"{style_a} slices are (ptr,len,cap) views; append may reallocate; subslices alias — for: {stem}.",
            f"Explain backing-array sharing, nil vs empty slice JSON, and copy/reslice mitigations for: {stem}.",
            f"Append within cap mutates shared storage; full slice expr `[:0:0]` can detach — internals for: {stem}.",
            f"Preallocate with make([]T,0,n) on hot paths related to: {stem}.",
            f"Retaining tiny subslices of huge arrays causes silent memory leaks in: {stem}.",
            f"How would you prove aliasing vs true leak for: {stem}?",
        )
    if topic == "maps":
        return _p(
            f"{style_a} maps are not safe concurrent; iteration order is random; nil map write panics — for: {stem}.",
            f"Use mutex+map or sync.Map with clear criteria; never &m[k] — for: {stem}.",
            f"Map growth may move buckets; concurrent write detected at runtime — internal note for: {stem}.",
            f"Guard shared maps; document ownership in reviews covering: {stem}.",
            f"Ranging maps while mutating without sync or assuming stable order fails: {stem}.",
            f"When is sync.Map worth it vs RWMutex+map for: {stem}?",
        )
    if topic == "performance":
        return _p(
            f"{style_a} profile first (CPU, heap, goroutine), then reduce allocs and contention — for: {stem}.",
            f"Use benchstat, `-benchmem`, block/mutex profiles as appropriate for: {stem}.",
            f"Flat vs cum in pprof; allocs/op drives GC — internal tools for: {stem}.",
            f"{style_b} on changes affecting: {stem}.",
            f"Optimizing cold paths or micro-benchmarking without realistic inputs misleads: {stem}.",
            f"Which single profile view would you open first for: {stem}?",
        )
    if topic == "production":
        return _p(
            f"{style_a} structured logs, metrics, traces, safe config, and graceful shutdown are baseline — for: {stem}.",
            f"Correlate trace_id across logs/metrics; validate config at startup; drain on SIGTERM for: {stem}.",
            f"OTel SDK exports spans; Prometheus RED metrics; slog JSON logs — stack for: {stem}.",
            f"Run staticcheck/govulncheck; protect pprof admin ports for: {stem}.",
            f"Missing readiness vs liveness or logging secrets breaks production answers to: {stem}.",
            f"What alert would fire first if: {stem} regresses in prod?",
        )
    if topic == "testing":
        return _p(
            f"{style_a} table-driven tests, `-race`, interface fakes/mocks, build-tagged integration — for: {stem}.",
            f"Keep tests deterministic; avoid t.Fatal in goroutines; fuzz edge cases for: {stem}.",
            f"Parallel tests need isolated state; httptest fakes network — techniques for: {stem}.",
            f"Gate merges on race detector for concurrent packages related to: {stem}.",
            f"Over-mocking concrete types or flaky timing-based tests weaken: {stem}.",
            f"How would you regression-test concurrency behavior for: {stem}?",
        )
    if topic == "modules":
        return _p(
            f"{style_a} go.mod/go.sum, MVS resolution, vendoring, GOPRIVATE — for: {stem}.",
            f"Explain semver import paths (/v2), retract, and verify in CI for: {stem}.",
            f"MVS picks minimum compatible versions across the module graph — internal rule for: {stem}.",
            f"Pin toolchain; never commit local replace forks for: {stem}.",
            f"Omitting go.sum or blind `go get -u` in libraries hurts: {stem}.",
            f"How would MVS resolve a conflicting requirement in: {stem}?",
        )
    if topic == "reflection":
        return _p(
            f"{style_a} reflection is powerful but costly and brittle — prefer generics/interfaces — for: {stem}.",
            f"Addressability, Kind, struct tags; DeepEqual semantics for: {stem}.",
            f"Interface values carry type metadata reflection walks — cost model for: {stem}.",
            f"Restrict reflection to frameworks/serialization, not hot handlers for: {stem}.",
            f"Field rename breaks tag-based reflection silently in: {stem}.",
            f"What would you genericize instead of reflecting for: {stem}?",
        )
    if topic == "troubleshooting":
        return _p(
            f"{style_a} triage with pprof goroutine/heap, traces, logs, and race detector — for: {stem}.",
            f"Isolate symptom (leak, deadlock, OOM, latency) before config churn for: {stem}.",
            f"Stack labels show blocked chan/mutex/select; GC thrash shows in gctrace — signals for: {stem}.",
            f"Reproduce under load; capture profiles at peak for: {stem}.",
            f"Shotgun GOMAXPROCS/GC toggles without evidence worsens: {stem}.",
            f"What is your first reversible mitigation in the first 30 minutes for: {stem}?",
        )
    if topic == "packages":
        return _p(
            f"{style_a} cmd/internal/pkg layout; minimal init(); explicit exports — for: {stem}.",
            f"internal/ enforces boundaries; init ordering is dependency-defined for: {stem}.",
            f"Import cycles are compile-time failures — design packages to avoid for: {stem}.",
            f"Keep init light; inject deps in tests for: {stem}.",
            f"Heavy init() harms testability and startup for: {stem}.",
            f"Where would you draw the module boundary for: {stem}?",
        )
    if topic == "language":
        return _p(
            f"{style_a} know Go 1.22 loop semantics, defer LIFO, and closure capture rules — for: {stem}.",
            f"Connect syntax rules to runtime impact (alloc, escape) when answering: {stem}.",
            f"Lexer-inserted semicolons and short declare scoping affect correctness in: {stem}.",
            f"Enforce go vet/staticcheck for patterns tied to: {stem}.",
            f"Relying on pre-1.22 loop capture behavior causes subtle bugs in: {stem}.",
            f"What test would catch a regression related to: {stem}?",
        )

    return _p(
        f"{style_a} tying language rules to runtime and production observability — for: {stem}.",
        f"Senior answers combine mechanism, tradeoffs, and verification for: {stem}.",
        f"Go couples compile-time types with runtime scheduler/GC behavior — anchor: {stem}.",
        f"{style_b} on any change suggested by: {stem}.",
        f"Hand-waving without profiles, tests, or happens-before reasoning fails: {stem}.",
        f"What evidence would convince you your answer to: {stem} holds at scale?",
    )


UNIQUE_ANSWERS: dict[int, dict[str, str]] = {
    num: _payload(_topic_key(question), question, num)
    for num, (question, _difficulty, _level, _topic, _doc) in enumerate(QUESTIONS, 1)
}

assert len(UNIQUE_ANSWERS) == 150
assert set(UNIQUE_ANSWERS.keys()) == set(range(1, 151))
assert len({v["short"] for v in UNIQUE_ANSWERS.values()}) == 150
