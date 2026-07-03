"""Python answer engine for Top 150 interview questions."""

from __future__ import annotations

import re
from typing import Callable

from python_questions_data import QUESTIONS

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
        short=f"Anchor the answer in CPython behavior, measurable production constraints, and the canonical handbook page for {topic.lower()}.",
        detailed="Senior Python interviews expect tradeoff reasoning — not syntax recall. Tie mechanism (how CPython does it) to symptom (what breaks in prod) and mitigation (what you would change in architecture or code).",
        internal="CPython couples language semantics with refcounting, the GIL, and ceval bytecode dispatch. Performance and concurrency answers should reference which layer owns the bottleneck.",
        production="Validate claims with profilers (`cProfile`, `tracemalloc`), structured logs, and reproducible benchmarks before changing architecture.",
        mistakes="Hand-waving 'async is faster' or 'threads parallelize CPU' fails senior bars. Another miss is optimizing without measuring import time, memory RSS, or event-loop blocking.",
        followup=f"What metric would prove your answer in production for this {topic.lower()} scenario?",
    )


def _runtime_imports(question: str) -> dict:
    return _pack(
        short="Startup runs interpreter init, then loads `__main__`; imports walk `sys.meta_path` finders → loaders → `sys.modules`.",
        detailed="`python script.py` bootstraps the runtime, configures `sys.path`, imports encodings/site, then executes the main module. Each `import` resolves a module spec, executes the module body once, and caches the module object.",
        internal="Importlib consults meta path hooks, then path-based finders. Loaders produce code objects executed in a fresh module namespace. Partial initialization during circular imports explains many startup bugs.",
        production="Keep import side effects out of module top-level on hot paths; use lazy imports for CLI cold start. In containers, verify `WORKDIR`, `PYTHONPATH`, and installed package layout (src vs flat).",
        mistakes="Mutating `sys.path` in libraries; heavy work at import time; assuming relative imports work when a script is run as `python path/to/script.py`.",
        followup="How would you profile and reduce import-time cost for a CLI with a 2-second cold start SLO?",
    )


def _bytecode_ceval(question: str) -> dict:
    return _pack(
        short="Source compiles to code objects; ceval dispatches bytecode opcodes in per-call frames on the value stack.",
        detailed="CPython parses to AST, compiles to bytecode attached to a code object (constants, names, varnames), then the eval loop executes opcodes. Locals and fast paths matter for tight loops.",
        internal="Frames hold the instruction pointer, stack, locals, and globals. `LOAD_FAST` beats `LOAD_GLOBAL`; attribute access compiles to `LOAD_ATTR` chains you can inspect with `dis`.",
        production="Use `dis` and profilers on hot functions before rewriting in Cython/Rust. Measure after compiler optimizations (`-O`) if relevant.",
        mistakes="Micro-optimizing bytecode without algorithmic wins; trusting `sys.getsizeof` for total memory of object graphs.",
        followup="Which opcode pattern in `dis` output would make you cache a global or attribute in a local variable?",
    )


def _object_model(question: str) -> dict:
    return _pack(
        short="Objects have refcounted headers; attribute lookup walks instance dict, class MRO, and descriptors.",
        detailed="Python uses call-by-object-reference: names bind to objects. Equality (`==`) differs from identity (`is`). Defining `__eq__` without a consistent `__hash__` makes instances unhashable.",
        internal="Data descriptors on the class override instance `__dict__` entries. `__new__` allocates; `__init__` initializes. `__slots__` replaces per-instance dict with fixed slots.",
        production="Use `@property` for invariants; apply `__slots__` only after memory profiling at scale. Document hashability contracts for dict keys in domain models.",
        mistakes="Using `is` for value comparison; expecting `__eq__` alone to preserve `set`/`dict` key behavior; storing mutable objects in `frozen` dataclass fields.",
        followup="Walk through descriptor lookup for `@property` versus a plain instance attribute.",
    )


def _gc_memory(question: str) -> dict:
    return _pack(
        short="Refcount frees acyclic objects immediately; generational GC breaks reference cycles; RSS includes off-heap C allocations.",
        detailed="Most objects die when refcount hits zero. Cycles need the cyclic GC (gen0/1/2). Memory leaks in production are often global caches, accidental cycles, or C extensions — not 'Python is slow'.",
        internal="GC tracks container objects with potential cycles. Thresholds trigger collections; `gc` module exposes introspection. pymalloc manages small object arenas.",
        production="Use `tracemalloc` snapshots, bound caches (`maxsize`, TTL), and `weakref` for registries. Treat `gc.collect()` as diagnostic, not a steady-state fix.",
        mistakes="Calling `gc.collect()` in request paths; unbounded `lru_cache`; holding references in module-level lists.",
        followup="How would you prove whether growth is a true leak versus expected caching?",
    )


def _gil(question: str) -> dict:
    return _pack(
        short="The GIL lets one thread run Python bytecode at a time per process — use processes or native code for CPU parallelism.",
        detailed="The GIL protects CPython's refcounted object model without per-object locks. I/O and many C extensions release it, so threads still help for blocking I/O. CPU-bound Python loops do not scale across threads.",
        internal="Bytecode execution holds the GIL; periodic ticks and I/O operations release it. NumPy-style C work can release the GIL during compute-heavy regions.",
        production="Model thread pools for I/O; process pools or task queues for CPU-bound Python. Document GIL assumptions in concurrency ADRs; evaluate free-threading builds explicitly.",
        mistakes="Expecting 8 threads to speed a pure-Python numeric loop 8×; blocking the event loop with sync I/O in asyncio.",
        followup="For a mixed HTTP + image-processing service, where would you place asyncio, threads, and processes?",
    )


def _asyncio(question: str) -> dict:
    return _pack(
        short="Asyncio schedules coroutines on one thread; `await` yields control until I/O completes — blocking calls stall the whole loop.",
        detailed="Coroutines are awaitable objects driven by an event loop. `TaskGroup` provides structured concurrency with sibling cancellation on failure. Use async-native libraries or `asyncio.to_thread` for blocking work.",
        internal="The loop polls ready futures/sockets and resumes coroutines at `await` points. Un-awaited coroutines warn and do no work. Cancellation injects `CancelledError` at `await` boundaries.",
        production="Reuse connection pools; cap concurrency with semaphores; propagate `contextvars` for tracing. Never call `time.sleep` or sync HTTP in the loop.",
        mistakes="Creating coroutines without awaiting; sharing blocking DB drivers; unbounded `create_task` without backpressure.",
        followup="How does `TaskGroup` change error propagation versus `gather(return_exceptions=True)`?",
    )


def _threading_mp(question: str) -> dict:
    return _pack(
        short="Use threads for blocking I/O with shared memory; use processes to bypass the GIL for CPU-bound Python work.",
        detailed="Threads share an address space — protect mutable state with locks or queues. Processes isolate memory; IPC via queues/pipes with pickling overhead. Windows requires `spawn` and import guards.",
        internal="`queue.Queue` is thread-safe; `multiprocessing.Queue` crosses processes. `fork` with existing threads is unsafe; prefer `spawn` on macOS/Windows.",
        production="Size thread pools to downstream limits; chunk large payloads for process pools; name threads for debugging.",
        mistakes="Daemon threads for required cleanup; unbounded thread creation; shipping huge objects to process workers every task.",
        followup="Why is `if __name__ == '__main__'` required for `ProcessPoolExecutor` on Windows?",
    )


def _concurrency_patterns(question: str) -> dict:
    return _pack(
        short="Use bounded queues and semaphores for backpressure; pick thread vs process pools from I/O vs CPU dominance.",
        detailed="Producer-consumer with `maxsize` blocks producers when consumers lag — preventing memory blowups. `asyncio.Semaphore` limits in-flight coroutines. `concurrent.futures` unifies pool submission and completion.",
        internal="Backpressure is explicit flow control — without it, unbounded buffers hide overload until OOM. Pool workers should be idempotent and picklable (processes).",
        production="Derive pool size from DB pool, API rate limits, and file descriptors. Monitor queue depth and task latency as scaling signals.",
        mistakes="Unbounded `asyncio.create_task`; ignoring `Queue.join` shutdown deadlocks; process pools for tiny tasks where IPC dominates.",
        followup="How would you implement graceful shutdown for thread pool workers draining a queue?",
    )


def _profiling_perf(question: str) -> dict:
    return _pack(
        short="Profile before optimizing: `cProfile` for call graph, `line_profiler` for hotspots, `tracemalloc` for memory.",
        detailed="Start with cumulative time in `cProfile`, then drill into lines. Benchmark with warmup and report median/p95. Algorithm and data structure choices beat micro-opts.",
        internal="Deterministic profilers add overhead; sampling (`py-spy`) suits production. Memory profilers track allocations by line/site, not just object counts.",
        production="Set performance budgets; gate regressions with `pytest-benchmark` on critical paths. Compare RSS and allocations, not only wall time.",
        mistakes="Optimizing cold paths; single-run `timeit`; ignoring allocation churn in tight loops.",
        followup="Which profiler would you run first for a 3× latency regression after a deploy?",
    )


def _production_ops(question: str) -> dict:
    return _pack(
        short="Production Python needs structured logs, typed config, metrics/traces, and boundary exception mapping.",
        detailed="Use JSON logs with correlation IDs; load config from env with explicit precedence; export RED metrics and traces with OpenTelemetry. Map domain errors to HTTP/status at the outer boundary only.",
        internal="`logging` hierarchy can duplicate handlers if misconfigured. `contextvars` carry request scope across asyncio tasks. Secrets never belong in source control.",
        production="Checklists: pinned deps, health/readiness probes, log sampling under load, alert on error rate and p99 latency.",
        mistakes="Logging the same exception in every middleware layer; printf-style logs without structure; secrets in env without rotation.",
        followup="Which three metrics and one trace span would you require before declaring a service production-ready?",
    )


def _testing(question: str) -> dict:
    return _pack(
        short="Pyramid: many fast unit tests, fewer integration tests, minimal e2e; isolate with mocks at boundaries.",
        detailed="pytest fixtures share setup via `conftest.py`; parametrize edge cases. Patch where the name is **used**, not where defined. CI runs lint, typecheck, unit, then integration.",
        internal="Mocks replace collaborators; over-mocking domain logic hides regressions. Property-based tests (`hypothesis`) find edge cases in parsers and serializers.",
        production="Flaky tests often mean shared global state or timing assumptions — fix isolation before increasing retries.",
        mistakes="Patching the wrong import path; no tests for `requires-python` lower bound; integration tests that hit prod APIs.",
        followup="How do you decide what to mock versus use real fakes for a repository layer?",
    )


def _packaging(question: str) -> dict:
    return _pack(
        short="Apps pin with lock files; libraries declare ranges; src layout prevents accidental imports from repo root.",
        detailed="`pyproject.toml` is canonical metadata. Wheels speed installs; editable installs for dev. uv/poetry/pip-tools solve reproducibility for applications.",
        internal="Build backends produce wheel/sdist artifacts; entry points wire CLI commands. Namespace packages allow split installs on `sys.path`.",
        production="Multi-stage Docker: install deps before copying source; matrix-test minimum Python version; OIDC trusted publishing to PyPI.",
        mistakes="Committing `.venv`; pinning libraries like applications; flat layout import bugs in CI only.",
        followup="When would you choose Poetry over hatchling + uv for a new service repo?",
    )


def _core_language(question: str) -> dict:
    return _pack(
        short="Prefer idiomatic Python — closures, decorators, context managers, and typing — with clear ownership of side effects.",
        detailed="Language features encode intent: decorators for cross-cutting behavior, context managers for resource scope, Protocol for structural interfaces. Exceptions are for exceptional paths, not control flow in hot loops.",
        internal="Decorators run at function definition time. Closures capture variables by reference — mind the loop late-binding trap. Context manager `__exit__` runs on exceptions unless suppressed.",
        production="Type public APIs; run pyright/mypy in CI on libraries; keep domain exceptions meaningful at boundaries.",
        mistakes="Mutable default arguments; catching bare `except:`; decorator stacks without `wraps` losing metadata.",
        followup="How would you test a parametrized retry decorator without flaking on timing?",
    )


INTENT_RULES: list[tuple[str, Callable[[str], dict]]] = [
    (r"(import|sys\.path|meta_path|finder|loader|__main__|interpreter startup|python script)", _runtime_imports),
    (r"(bytecode|dis\.|code object|ceval|opcode|compile|ast|frame)", _bytecode_ceval),
    (r"(descriptor|__new__|__eq__|__hash__|__slots__|attribute lookup|object model|is versus|identity|mro|super\(\)|inheritance)", _object_model),
    (r"(refcount|garbage|gc\.|cycle|weakref|tracemalloc|memory leak|rss|pymalloc)", _gc_memory),
    (r"(gil|global interpreter|free-threading|nogil)", _gil),
    (r"(asyncio|async/await|coroutine|taskgroup|event loop|await)", _asyncio),
    (r"(thread|multiprocess|process pool|spawn|fork|pickl|queue\.queue|daemon thread|lock|rlock)", _threading_mp),
    (r"(backpressure|producer.consumer|thread pool|semaphore|concurrent\.futures|pool size)", _concurrency_patterns),
    (r"(cprofile|profile|benchmark|line_profiler|memory_profiler|py-spy|timeit|optimiz|performance)", _profiling_perf),
    (r"(log|observability|metric|trace|opentelemetry|config|secret|health|checklist|production)", _production_ops),
    (r"(pytest|mock|patch|fixture|test strateg|hypothesis|coverage|integration test)", _testing),
    (r"(pyproject|wheel|poetry|venv|lock file|entry point|src layout|packaging|pypi)", _packaging),
    (r"(decorator|closure|context manager|dataclass|protocol|typing|exception|comprehension|generator|iterator)", _core_language),
]


def _intent_answer(question: str, topic: str) -> dict:
    q = question.lower()
    for pattern, handler in INTENT_RULES:
        if re.search(pattern, q):
            return handler(question)
    return _topic_default(question, topic)


def craft_answer(num: int, question: str, topic: str, doc: str) -> dict:
    return _intent_answer(question, topic)


__all__ = ["QUESTIONS", "craft_answer", "format_answer_block", "slug_anchor"]
