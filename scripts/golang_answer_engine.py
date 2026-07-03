"""Go answer engine for top-150 interview questions."""

from __future__ import annotations

import re
from typing import Callable

from golang_questions_data import QUESTIONS
from golang_top150_unique_answers import UNIQUE_ANSWERS

SECTIONS = ("short", "detailed", "internal", "production", "mistakes", "followup")


def slug_anchor(question: str) -> str:
    base = question.lower().strip()
    base = re.sub(r"[^\w\s-]", "", base)
    base = re.sub(r"[\s_]+", "-", base)
    base = re.sub(r"-{2,}", "-", base).strip("-")
    return base[:80].rstrip("-")


def format_answer_block(question: str, sections: dict) -> str:
    return (
        f"## {question}\n\n"
        f"### Short Answer\n{sections['short']}\n\n"
        f"### Detailed Explanation\n{sections['detailed']}\n\n"
        f"### Internal Working\n{sections['internal']}\n\n"
        f"### Production Notes\n{sections['production']}\n\n"
        f"### Common Mistakes\n{sections['mistakes']}\n\n"
        f"### Follow-up Questions\n{sections['followup']}\n\n"
        "---\n"
    )


def _pack(short, detailed, internal, production, mistakes, followup) -> dict:
    return {
        "short": short,
        "detailed": detailed,
        "internal": internal,
        "production": production,
        "mistakes": mistakes,
        "followup": followup,
    }


def _topic_default(question: str, topic: str) -> dict:
    return _pack(
        short=f"Anchor the answer in Go runtime semantics, observable behavior, and production tradeoffs for {topic.lower()}.",
        detailed="Senior interviews expect mechanism-first reasoning: what the language/runtime guarantees, what it does not, and how that shows up under load or failure.",
        internal="Go couples language rules (types, interfaces, concurrency primitives) with a runtime scheduler, GC, and memory model. Correct answers connect API behavior to these subsystems.",
        production="Validate assumptions with `go test -race`, benchmarks, and pprof before changing architecture. Pin Go versions and document SLO impact of concurrency/GC choices.",
        mistakes="Hand-waving 'Go is fast' without allocation, scheduling, or cancellation analysis. Copying patterns without bounding goroutines or defining shutdown behavior.",
        followup=f"What observable metric or test would prove your design handles this {topic.lower()} concern in production?",
    )


def _scheduler_runtime(question: str) -> dict:
    return _pack(
        short="Goroutines are M:N scheduled on GOMAXPROCS logical processors (Ps); Ms map to OS threads; work stealing balances load.",
        detailed="A goroutine (G) is cheap user-space work. Ps own local run queues and require an M to execute. When a G blocks on syscall or channel, the scheduler parks it and runs other Gs. Idle Ps steal work from busy peers.",
        internal="The netpoller integrates network I/O with scheduling — blocked Gs on poller fds do not pin an M forever. Go 1.14+ added asynchronous preemption for tight CPU loops that never hit safe points.",
        production="Set GOMAXPROCS to match CPU quota in containers. Watch runnable goroutine count, scheduling latency (trace), and avoid unbounded goroutine creation.",
        mistakes="Equating goroutines with OS threads. Ignoring syscall-heavy workloads that need more Ms. Setting GOMAXPROCS=1 on multi-core without a documented reason.",
        followup="Where would you use runtime/trace to prove scheduler delay versus lock contention?",
    )


def _gc_memory(question: str) -> dict:
    return _pack(
        short="Go uses concurrent tri-color mark-sweep GC; GOGC controls pacing; allocation rate often dominates pause and CPU cost.",
        detailed="The collector marks reachable objects while mutators run with write barriers. STW phases exist but are short. High alloc rate increases mark work and GC CPU even if live heap is modest.",
        internal="Escape analysis and stack allocation reduce heap objects. uintptr is not a GC root — keeping memory alive requires a pointer the GC can trace.",
        production="Use `GODEBUG=gctrace=1` sparingly in incidents. Reduce allocations (pools, prealloc) before tuning GOGC. Profile heap with pprof allocs.",
        mistakes="Calling runtime.GC() routinely. Using finalizers for resource cleanup. Optimizing live heap size while ignoring alloc/op in hot paths.",
        followup="Which pprof view would you use to separate alloc rate from live heap growth?",
    )


def _memory_model(question: str) -> dict:
    return _pack(
        short="Visibility across goroutines is defined by happens-before; data races are undefined behavior — use channels, mutex, or atomic.",
        detailed="The memory model lists synchronization events that establish ordering: channel ops, sync primitives, Once, atomic. Without such an edge, reads/writes may race.",
        internal="Compiler and CPU may reorder within a goroutine but must respect happens-before. The race detector instruments memory accesses at runtime in test builds.",
        production="Run `go test -race` in CI for concurrent packages. Treat race failures as release blockers for services with shared mutable state.",
        mistakes="Assuming 'it works on my machine' means no race. Using atomics for compound invariants that need mutex protection.",
        followup="Show a minimal happens-before fix for a racy counter versus a channel-based design.",
    )


def _escape_analysis(question: str) -> dict:
    return _pack(
        short="The compiler decides stack vs heap via escape analysis; escaped values become GC-managed heap objects.",
        detailed="Locals that outlive their frame (returned pointers, captured by closures escaping scope, assigned to interfaces) typically move to the heap. `-gcflags=-m` prints decisions.",
        internal="Stack allocation is cheaper and avoids GC mark work. Heap objects increase pointer density and GC scan cost.",
        production="Profile before micro-optimizing. Target hot paths with high allocs/op from escape or string/slice conversions.",
        mistakes="Assuming `new` always means heap (compiler may still optimize). Returning pointers to large structs without measuring cost.",
        followup="What does `-m` output show for a closure that captures a loop variable?",
    )


def _concurrency(question: str) -> dict:
    return _pack(
        short="Prefer clear ownership: channels for orchestration, mutex for shared state; always bound concurrency and propagate context.",
        detailed="Go encourages sharing memory by communicating, but mutexes are often simpler for caches and counters. Combine WaitGroup, context, and buffered channels for backpressure.",
        internal="Unbuffered channels synchronize; buffered channels decouple up to capacity. nil channels block forever in select — useful for disabling cases.",
        production="Define goroutine lifecycle: who starts, who stops, how errors return. Implement graceful shutdown with context cancel and server drain.",
        mistakes="Leaked goroutines blocked on channels. Closing channels from the receiver side. select+default spin loops.",
        followup="When would you choose errgroup with context over a raw WaitGroup?",
    )


def _interfaces_errors(question: str) -> dict:
    return _pack(
        short="Interfaces are implicit (type, data) pairs; typed nil breaks `== nil`. Errors use wrapping with `%w` and `errors.Is/As`.",
        detailed="An interface value is nil only when both type and data are nil. A nil pointer inside a non-nil interface type is a classic API bug. Error chains preserve cause for inspection.",
        internal="Method sets determine satisfaction — pointer vs value receivers matter. Error wrapping builds an unwrap chain inspected by Is/As.",
        production="Keep interfaces small at boundaries. Never log and return the same error. Use sentinel errors sparingly with documented semantics.",
        mistakes="Comparing wrapped errors with `==`. Returning typed nil pointers in interfaces. Giant interfaces that hinder testing.",
        followup="How would you test `errors.Is` through three layers of `%w` wrapping?",
    )


def _slices_maps(question: str) -> dict:
    return _pack(
        short="Slices are views (ptr,len,cap); subslices alias backing arrays. Maps are not safe for concurrent use without sync.",
        detailed="append may reallocate and copy when cap exhausted. Subslices of large arrays can leak memory if a small slice is retained. Map growth and iteration have defined but subtle semantics.",
        internal="Map writes are not atomic across goroutines — runtime detects concurrent map writes and panics. Slice headers are small but point to shared storage.",
        production="Preallocate slices when size is known. Copy or reslice with full slice expression to detach from large backing arrays. Protect maps with mutex or sync.Map.",
        mistakes="Assuming append never mutates other slices sharing backing array. Using maps from multiple goroutines without synchronization.",
        followup="How would you prove a memory leak is slice aliasing versus a true goroutine leak?",
    )


def _performance(question: str) -> dict:
    return _pack(
        short="Profile first (CPU, heap, goroutine); reduce allocations; validate with benchmarks and benchstat.",
        detailed="Performance work starts with measurement: pprof for hot paths, allocs/op for GC pressure, trace for scheduling delays. Optimize the dominant cost, not assumed bottlenecks.",
        internal="CPU profile samples on-CPU stacks. Heap profile shows in-use or allocated objects. Block/mutex profiles expose contention.",
        production="Expose pprof on admin interfaces only. Compare benchmarks across Go versions with benchstat. Set GOMAXPROCS to CPU limit in K8s.",
        mistakes="Optimizing cold paths. Disabling GC instead of reducing allocations. Trusting micro-benchmarks without realistic input sizes.",
        followup="What regression guard would you add in CI for alloc/op on critical handlers?",
    )


def _production_eng(question: str) -> dict:
    return _pack(
        short="Production Go services need structured logs, metrics, traces, safe config loading, and graceful shutdown on SIGTERM.",
        detailed="Operate with correlation IDs across logs and traces. Load config from env with validation at startup. On shutdown, stop accepting, drain in-flight work, then release resources.",
        internal="context cancellation propagates to downstream calls. net/http Server.Shutdown uses context timeout. OTel SDK exports spans/metrics to collectors.",
        production="Align shutdown timeout with K8s terminationGracePeriodSeconds. Run govulncheck/staticcheck in CI. Never log secrets.",
        mistakes="Ignoring SIGTERM until kill. Storing context in structs. Missing health vs readiness separation.",
        followup="How do you verify graceful shutdown under load in a staging environment?",
    )


def _testing(question: str) -> dict:
    return _pack(
        short="Table-driven unit tests, race detector in CI, interface mocks/fakes, build-tagged integration tests.",
        detailed="Tests should be deterministic, fast, and parallel-safe where possible. Use interfaces at boundaries for test doubles. Integration tests hit real deps with tags.",
        internal="t.Parallel requires isolated state. Fuzzing (testing.F) finds edge cases. httptest records HTTP without network.",
        production="Gate merges on `-race` for concurrent code. Use `-cover` for critical packages. Mock codegen for large interfaces only when hand fakes hurt maintenance.",
        mistakes="t.Fatal inside goroutines. Shared global state across parallel tests. Over-mocking internal concrete types.",
        followup="How would you structure a concurrency regression test for a worker pool?",
    )


def _modules(question: str) -> dict:
    return _pack(
        short="go.mod defines module path and requirements; MVS picks minimum compatible versions; commit go.sum for reproducibility.",
        detailed="Modules replaced GOPATH for dependency management. replace is for local dev; retract withdraws bad versions. Vendoring supports hermetic CI.",
        internal="The module graph is resolved with minimal version selection — not latest-wins. Major versions v2+ require /v2 in module path.",
        production="Pin Go toolchain in go.mod and Docker. Use GOPRIVATE for internal modules. Run go mod verify in CI.",
        mistakes="Committing replace directives meant for local forks. Using go get -u blindly in libraries. Omitting go.sum from VCS.",
        followup="How does MVS behave when two modules require different minimum versions of the same dependency?",
    )


def _reflection(question: str) -> dict:
    return _pack(
        short="Reflection inspects types at runtime; costly and brittle — prefer generics and compile-time interfaces when possible.",
        detailed="reflect.Value must be addressable to mutate. Field access by string breaks on refactor. Generics cover many serializer/utility cases reflection used to solve.",
        internal="Interface values carry type metadata; reflection walks struct tags and kinds. DeepEqual handles nested structures with defined semantics.",
        production="Restrict reflection to frameworks (JSON, ORM, DI) not business hot paths. Fuzz and test tag contracts.",
        mistakes="Reflection in request handlers. Assuming zero values via reflection without handling pointers.",
        followup="What would you refactor to generics instead of reflect for this use case?",
    )


INTENT_RULES: list[tuple[str, Callable[[str], dict]]] = [
    (r"(gmp|scheduler|gomaxprocs|work steal|preempt|netpoller|os thread|goroutine stack)", _scheduler_runtime),
    (r"(runtime|linker|startup|main\.)", _scheduler_runtime),
    (r"(gc|gctrace|gogc|tri-color|mark-sweep|finalizer|uintptr|stw|write barrier)", _gc_memory),
    (r"(escape analysis|stack vs heap|-gcflags=-m|heap alloc)", _escape_analysis),
    (r"(happens-before|data race|atomic|memory model)", _memory_model),
    (r"(channel|select|mutex|waitgroup|worker pool|fan-out|fan-in|pipeline|backpressure|goroutine leak|semaphore)", _concurrency),
    (r"(context|cancellation|deadline)", _concurrency),
    (r"(interface|nil interface|type assert|method set|receiver)", _interfaces_errors),
    (r"(error|errors\.is|errors\.as|%w|sentinel)", _interfaces_errors),
    (r"(slice|append|backing array|subslice|map|sync\.map)", _slices_maps),
    (r"(pprof|benchmark|benchstat|alloc|profil|performance|optimization|padding|struct field)", _performance),
    (r"(log|observability|opentelemetry|prometheus|metric|trace|sigterm|shutdown|config|secret|production checklist)", _production_eng),
    (r"(test|mock|fuzz|httptest|integration|t\.parallel)", _testing),
    (r"(go\.mod|go get|mvs|vendor|goprivate|module|retract)", _modules),
    (r"(reflect|generics|deepequal)", _reflection),
    (r"(troubleshoot|triage|panic|oom|pprof/goroutine|debug)", _performance),
]


def _intent_answer(question: str, topic: str) -> dict:
    q = question.lower()
    for pattern, handler in INTENT_RULES:
        if re.search(pattern, q):
            return handler(question)
    return _topic_default(question, topic)


def craft_answer(num: int, question: str, topic: str, doc: str) -> dict:
    if num in UNIQUE_ANSWERS:
        return UNIQUE_ANSWERS[num]
    return _intent_answer(question, topic)


__all__ = ["QUESTIONS", "UNIQUE_ANSWERS", "craft_answer", "format_answer_block", "slug_anchor"]
