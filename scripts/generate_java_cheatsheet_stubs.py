"""Generate Java Engineering Cheat Sheet stubs from data/java_engineering_modules.yaml."""
from __future__ import annotations

import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SKIP = {
    "primitive-data-types",
    "hashmap",
    "lambda",
    "virtual-threads",
    "collections-complexity",
    "java-8-features",
}

TITLES: dict[str, tuple[str, str, str]] = {
    "primitive-data-types": ("Primitive Data Types", "Primitives", "Eight built-in value types — sizes, defaults, and when to prefer primitives over wrappers."),
    "wrapper-classes": ("Wrapper Classes", "Wrappers", "Object shells for primitives — boxing, unboxing, and autoboxing pitfalls."),
    "variables": ("Variables", "Variables", "Local, instance, static, and final variables — scope, lifetime, and naming."),
    "operators": ("Operators", "Operators", "Arithmetic, relational, logical, bitwise, and assignment operators in Java."),
    "control-statements": ("Control Statements", "Control Flow", "if-else, switch, for, while, do-while, break, continue, and labeled break."),
    "methods": ("Methods", "Methods", "Declaration, parameters, varargs, overloading, and return semantics."),
    "arrays": ("Arrays", "Arrays", "Fixed-size sequences — declaration, initialization, multi-dimensional arrays, and Arrays utility."),
    "strings": ("Strings", "Strings", "Immutable character sequences — literals, interning, comparison, and common APIs."),
    "stringbuilder": ("StringBuilder", "StringBuilder", "Mutable, non-thread-safe string builder for single-threaded concatenation."),
    "stringbuffer": ("StringBuffer", "StringBuffer", "Mutable, synchronized string builder — legacy thread-safe alternative."),
    "enums": ("Enums", "Enums", "Type-safe constants with fields, methods, and switch integration."),
    "class": ("Class", "Class", "Blueprint for objects — fields, methods, static members, and access modifiers."),
    "object": ("Object", "Object", "Runtime instances — state, identity, and reference semantics."),
    "constructor": ("Constructor", "Constructor", "Object initialization — default, parameterized, chaining, and private constructors."),
    "inheritance": ("Inheritance", "Inheritance", "is-a relationships — extends, super, and method hiding."),
    "polymorphism": ("Polymorphism", "Polymorphism", "Compile-time overloading and runtime overriding — dynamic dispatch."),
    "abstraction": ("Abstraction", "Abstraction", "Hiding implementation detail behind essential behavior."),
    "encapsulation": ("Encapsulation", "Encapsulation", "Bundling data with controlled access via getters and setters."),
    "interface": ("Interface", "Interface", "Contracts — default methods, static methods, and functional interfaces."),
    "abstract-class": ("Abstract Class", "Abstract Class", "Partial implementations — abstract methods vs concrete shared code."),
    "object-class": ("Object Class", "Object Class", "Root of the class hierarchy — universal methods every type inherits."),
    "equals-method": ("equals()", "equals()", "Value equality contract — consistency with hashCode and symmetry rules."),
    "hashcode-method": ("hashCode()", "hashCode()", "Hash bucket distribution — contract with equals and collision handling."),
    "tostring-method": ("toString()", "toString()", "Human-readable representation for logging and debugging."),
    "collections-framework-overview": ("Collections Framework Overview", "Overview", "Hierarchy of List, Set, Queue, Map — choosing the right collection."),
    "arraylist": ("ArrayList", "ArrayList", "Resizable array-backed list — fast random access, costly middle inserts."),
    "linkedlist": ("LinkedList", "LinkedList", "Doubly-linked list — efficient head/tail ops, poor indexed access."),
    "vector": ("Vector", "Vector", "Legacy synchronized resizable array — prefer ArrayList + external sync."),
    "hashset": ("HashSet", "HashSet", "Hash table-backed unique elements — O(1) average add/contains."),
    "linkedhashset": ("LinkedHashSet", "LinkedHashSet", "HashSet with predictable iteration order."),
    "treeset": ("TreeSet", "TreeSet", "Red-black tree sorted set — O(log n) ops with natural or Comparator order."),
    "hashmap": ("HashMap", "HashMap", "Hash table map — default choice for key-value storage in single-threaded code."),
    "linkedhashmap": ("LinkedHashMap", "LinkedHashMap", "HashMap with insertion-order or LRU access-order iteration."),
    "treemap": ("TreeMap", "TreeMap", "Sorted map on red-black tree — navigable key operations."),
    "concurrenthashmap": ("ConcurrentHashMap", "ConcurrentHashMap", "Thread-safe segmented hash map — lock striping and CAS."),
    "weakhashmap": ("WeakHashMap", "WeakHashMap", "Keys held by weak references — useful for caches keyed by short-lived objects."),
    "identityhashmap": ("IdentityHashMap", "IdentityHashMap", "Reference equality (==) keys — not equals()."),
    "priorityqueue": ("PriorityQueue", "PriorityQueue", "Heap-based priority queue — O(log n) insert and poll."),
    "arraydeque": ("ArrayDeque", "ArrayDeque", "Resizable array deque — efficient stack and queue without synchronization."),
    "collections-util": ("Collections Utility", "Collections", "java.util.Collections — sort, shuffle, unmodifiable wrappers, synchronized views."),
    "arrays-util": ("Arrays Utility", "Arrays", "java.util.Arrays — sort, binary search, copy, stream, and parallel helpers."),
    "comparable-vs-comparator": ("Comparable vs Comparator", "Comparable vs Comparator", "Natural ordering vs external comparison strategies."),
    "hashmap-internals": ("HashMap Internals", "HashMap Internals", "Buckets, hash spread, resize, treeify threshold, and load factor."),
    "concurrenthashmap-internals": ("ConcurrentHashMap Internals", "CHM Internals", "Segments, bins, CAS, and sizeCtl in modern JDK implementations."),
    "checked-exception": ("Checked Exception", "Checked Exception", "Compile-time enforced handling — IOException, SQLException, and subclasses."),
    "unchecked-exception": ("Unchecked Exception", "Unchecked Exception", "RuntimeException hierarchy — programming errors and optional handling."),
    "error": ("Error", "Error", "Serious JVM problems — OutOfMemoryError, StackOverflowError — generally not caught."),
    "try-catch": ("try-catch", "try-catch", "Exception handling blocks — multi-catch and exception type ordering."),
    "finally": ("finally", "finally", "Guaranteed cleanup — runs after try/catch even when return or throw."),
    "try-with-resources": ("try-with-resources", "try-with-resources", "Automatic resource management for AutoCloseable since Java 7."),
    "custom-exceptions": ("Custom Exceptions", "Custom Exceptions", "Domain-specific checked and unchecked exception design."),
    "exception-handling-best-practices": ("Exception Handling Best Practices", "Exception Best Practices", "When to catch, wrap, log, and fail fast in production code."),
    "generic-classes": ("Generic Classes", "Generic Classes", "Type-parameterized classes — T, E, K, V conventions."),
    "generic-methods": ("Generic Methods", "Generic Methods", "Method-level type parameters independent of class generics."),
    "wildcards": ("Wildcards", "Wildcards", "? extends and ? super — PECS producer/consumer guidance."),
    "bounded-types": ("Bounded Types", "Bounded Types", "Upper bounds on type parameters — <T extends Comparable<T>>."),
    "type-erasure": ("Type Erasure", "Type Erasure", "Compile-time generics removed at runtime — bridges and raw types."),
    "functional-interface": ("Functional Interface", "Functional Interface", "@FunctionalInterface — single abstract method types for lambdas."),
    "lambda": ("Lambda Expressions", "Lambda", "Concise anonymous functions — syntax, captures, and effective final."),
    "method-reference": ("Method Reference", "Method Reference", "Shorthand :: syntax — static, instance, and constructor references."),
    "optional": ("Optional", "Optional", "Explicit absence container — avoid null in return types."),
    "supplier": ("Supplier", "Supplier", "T get() — lazy value provision with no arguments."),
    "consumer": ("Consumer", "Consumer", "void accept(T) — side-effect operations on a value."),
    "predicate": ("Predicate", "Predicate", "boolean test(T) — filtering and conditional logic."),
    "function": ("Function", "Function", "T apply(R) — one-argument transformation."),
    "bifunction": ("BiFunction", "BiFunction", "Two-argument transformation R apply(T, U)."),
    "unaryoperator": ("UnaryOperator", "UnaryOperator", "Function<T, T> specialization — same-type mapping."),
    "binaryoperator": ("BinaryOperator", "BinaryOperator", "BiFunction<T, T, T> — reduction and aggregation."),
    "creating-streams": ("Creating Streams", "Creating Streams", "From collections, arrays, generate, iterate, and builders."),
    "intermediate-operations": ("Intermediate Operations", "Intermediate Ops", "Lazy transforms — filter, map, flatMap, sorted, distinct."),
    "terminal-operations": ("Terminal Operations", "Terminal Ops", "Eager consumers — collect, reduce, forEach, count, findFirst."),
    "collectors": ("Collectors", "Collectors", "Built-in collectors — toList, toMap, joining, summarizing."),
    "grouping": ("Grouping", "Grouping", "Collectors.groupingBy — multi-level aggregation."),
    "partitioning": ("Partitioning", "Partitioning", "Collectors.partitioningBy — boolean split into two lists."),
    "parallel-streams": ("Parallel Streams", "Parallel Streams", "ForkJoin common pool — when parallel helps and hurts."),
    "streams-best-practices": ("Streams Best Practices", "Stream Best Practices", "Readability, side effects, boxing, and primitive streams."),
    "thread": ("Thread", "Thread", "Platform thread lifecycle — start, join, interrupt, and thread states."),
    "runnable": ("Runnable", "Runnable", "void run() task unit — functional interface for threads and executors."),
    "callable": ("Callable", "Callable", "V call() with checked exceptions — Future-based results."),
    "executorservice": ("ExecutorService", "ExecutorService", "Thread pool abstraction — submit, shutdown, and lifecycle."),
    "forkjoinpool": ("ForkJoinPool", "ForkJoinPool", "Work-stealing pool for divide-and-conquer and parallel streams."),
    "future": ("Future", "Future", "Async result handle — get, cancel, isDone."),
    "completablefuture": ("CompletableFuture", "CompletableFuture", "Composable async pipelines — thenApply, thenCompose, allOf."),
    "synchronization": ("Synchronization", "Synchronization", "synchronized methods and blocks — intrinsic locks and reentrancy."),
    "volatile": ("volatile", "volatile", "Visibility guarantee — not atomic compound operations."),
    "atomic-classes": ("Atomic Classes", "Atomic Classes", "java.util.concurrent.atomic — lock-free CAS counters and references."),
    "locks": ("Locks", "Locks", "ReentrantLock — explicit lock, tryLock, and fairness."),
    "readwritelock": ("ReadWriteLock", "ReadWriteLock", "Concurrent reads, exclusive writes — ReentrantReadWriteLock."),
    "semaphore": ("Semaphore", "Semaphore", "Permit-based throttling — bounded resource access."),
    "countdownlatch": ("CountDownLatch", "CountDownLatch", "One-shot gate — await until count reaches zero."),
    "cyclicbarrier": ("CyclicBarrier", "CyclicBarrier", "Reusable barrier — threads meet at a synchronization point."),
    "phaser": ("Phaser", "Phaser", "Flexible phased coordination — dynamic party registration."),
    "threadlocal": ("ThreadLocal", "ThreadLocal", "Per-thread variable isolation — context propagation patterns."),
    "virtual-threads": ("Virtual Threads", "Virtual Threads", "Lightweight threads (Java 21+) — massive concurrency with blocking code."),
    "structured-concurrency": ("Structured Concurrency", "Structured Concurrency", "Scoped task trees — JEP 453 preview API for structured lifetimes."),
    "stack-vs-heap": ("Stack vs Heap", "Stack vs Heap", "Thread stacks vs shared heap — where locals and objects live."),
    "jvm-memory-layout": ("JVM Memory Layout", "JVM Memory", "Heap regions, thread stacks, code cache, and native memory."),
    "object-creation": ("Object Creation", "Object Creation", "new, allocation, initialization order, and constructor chaining."),
    "garbage-collection": ("Garbage Collection", "Garbage Collection", "Reachability, GC roots, and collection cycles."),
    "gc-algorithms": ("GC Algorithms", "GC Algorithms", "Serial, Parallel, G1, ZGC, Shenandoah — trade-off overview."),
    "young-generation": ("Young Generation", "Young Gen", "Eden, Survivor spaces, minor GC, and object promotion."),
    "old-generation": ("Old Generation", "Old Gen", "Tenured space, major GC, and fragmentation."),
    "metaspace": ("Metaspace", "Metaspace", "Class metadata storage replacing PermGen since Java 8."),
    "reference-types": ("Reference Types", "Reference Types", "Strong, soft, weak, phantom — java.lang.ref hierarchy."),
    "strong-reference": ("Strong Reference", "Strong Reference", "Default references — objects unreachable when no strong refs remain."),
    "weak-reference": ("Weak Reference", "Weak Reference", "Collected eagerly at next GC — WeakHashMap keys."),
    "soft-reference": ("Soft Reference", "Soft Reference", "Collected under memory pressure — soft caches."),
    "phantom-reference": ("Phantom Reference", "Phantom Reference", "Post-mortem cleanup — ReferenceQueue and cleaner patterns."),
    "memory-leak": ("Memory Leak", "Memory Leak", "Retained unreachable objects — static collections, listeners, ThreadLocal."),
    "outofmemoryerror": ("OutOfMemoryError", "OutOfMemoryError", "Heap, metaspace, and direct buffer OOM — diagnosis."),
    "escape-analysis": ("Escape Analysis", "Escape Analysis", "JIT optimization — stack allocation and lock elision."),
    "jvm-architecture": ("JVM Architecture", "JVM Architecture", "Class loader, runtime data areas, execution engine overview."),
    "class-loader": ("Class Loader", "Class Loader", "Bootstrap, platform, application loaders and delegation model."),
    "class-loading-process": ("Class Loading Process", "Class Loading", "Loading, linking, initialization — when static blocks run."),
    "bytecode": ("Bytecode", "Bytecode", "JVM instruction set — opcodes, stack machine, and verification."),
    "jit-compiler": ("JIT Compiler", "JIT Compiler", "HotSpot C1/C2 — profiling, inlining, and deoptimization."),
    "interpreter": ("Interpreter", "Interpreter", "Bytecode interpretation before JIT compilation kicks in."),
    "garbage-collector-jvm": ("Garbage Collector (JVM)", "GC (JVM View)", "Collector interface from JVM subsystem perspective."),
    "jvm-startup": ("JVM Startup", "JVM Startup", "java launcher, classpath, module path, and main class loading."),
    "jvm-parameters": ("JVM Parameters", "JVM Parameters", "-Xmx, -Xms, GC flags, and diagnostic switches."),
    "performance-tuning-basics": ("Performance Tuning Basics", "Perf Tuning", "Profiling-first tuning — heap, GC logs, and latency targets."),
    "java-8-features": ("Java 8 Features", "Java 8", "Lambda, Streams, Optional, and java.time — the modern baseline."),
    "java-9-features": ("Java 9 Features", "Java 9", "JPMS modules, JShell, factory methods for collections."),
    "java-10-var": ("Java 10 — var", "Java 10 var", "Local variable type inference — limits and readability."),
    "java-11-features": ("Java 11 Features", "Java 11", "LTS — HTTP Client, String methods, nest-based access."),
    "java-12-13-switch-improvements": ("Java 12–13 Switch Improvements", "Switch (12–13)", "Switch expressions preview and yield."),
    "java-14-switch-expressions": ("Java 14 — Switch Expressions", "Switch Expr", "Standard switch expressions and arrow syntax."),
    "java-15-text-blocks": ("Java 15 — Text Blocks", "Text Blocks", "Multi-line string literals with triple-quote syntax."),
    "java-16-records": ("Java 16 — Records", "Records", "Immutable data carriers — compact constructors and components."),
    "java-17-sealed-classes": ("Java 17 — Sealed Classes", "Sealed Classes", "Restricted inheritance — permits and exhaustive switch."),
    "java-18-20-incubator-features": ("Java 18–20 Incubator Features", "Java 18–20", "Foreign API, vector API, pattern matching refinements."),
    "java-21-features": ("Java 21 Features", "Java 21 LTS", "Virtual threads, sequenced collections, record patterns."),
    "java-22-features": ("Java 22 Features", "Java 22", "Stable features — unnamed variables, stream gatherers (preview)."),
    "java-23-features": ("Java 23 Features", "Java 23", "Primitive types in patterns (preview), module import."),
    "java-24-features": ("Java 24 Features", "Java 24", "Flexible constructor bodies, stream gatherers evolution."),
    "java-25-features": ("Java 25 Features", "Java 25", "Latest stable language and API additions — check preview flags."),
    "file": ("File", "File", "java.io.File — legacy path representation and pitfalls."),
    "path": ("Path", "Path", "java.nio.file.Path — modern path abstraction."),
    "files": ("Files", "Files", "Static NIO.2 utilities — read, write, walk, copy."),
    "inputstream": ("InputStream", "InputStream", "Byte-oriented input — read, skip, mark/reset."),
    "outputstream": ("OutputStream", "OutputStream", "Byte-oriented output — write and flush."),
    "reader": ("Reader", "Reader", "Character-oriented input — encoding-aware text."),
    "writer": ("Writer", "Writer", "Character-oriented output — buffering and encoding."),
    "buffered-streams": ("Buffered Streams", "Buffered Streams", "BufferedInputStream/Reader — reducing system calls."),
    "serialization-basics-io": ("Serialization Basics (IO)", "Serialization IO", "Object streams — ObjectInputStream and ObjectOutputStream."),
    "nio": ("NIO", "NIO", "Channels, buffers, selectors — non-blocking IO overview."),
    "reflection-api": ("Reflection API", "Reflection", "Runtime class introspection — fields, methods, constructors."),
    "custom-annotation": ("Custom Annotation", "Custom Annotation", "Defining and documenting your own annotations."),
    "built-in-annotations": ("Built-in Annotations", "Built-in Annotations", "@Override, @Deprecated, @SuppressWarnings, @FunctionalInterface."),
    "annotation-processing": ("Annotation Processing", "Annotation Processing", "Compile-time processors — APT and code generation."),
    "serializable": ("Serializable", "Serializable", "Marker interface — default Java serialization mechanics."),
    "externalizable": ("Externalizable", "Externalizable", "Custom read/write control — Externalizable vs Serializable."),
    "serialversionuid": ("serialVersionUID", "serialVersionUID", "Version compatibility for serialized classes."),
    "serialization-best-practices": ("Serialization Best Practices", "Serialization Practices", "Prefer JSON/Protobuf; security and evolution rules."),
    "collections-complexity": ("Collections Complexity", "Collections Complexity", "Big-O cheat sheet for List, Set, Map operations."),
    "stream-operations-interview": ("Stream Operations (Interview)", "Stream Ops", "Lazy vs eager, common ops, and parallel caveats."),
    "concurrent-collections-interview": ("Concurrent Collections (Interview)", "Concurrent Collections", "CHM, CopyOnWriteArrayList, BlockingQueue summary."),
    "gc-summary-interview": ("GC Summary (Interview)", "GC Summary", "Collector selection and generational GC one-pager."),
    "java-version-features-interview": ("Java Version Features (Interview)", "Version Features", "LTS timeline and headline features per release."),
    "memory-diagram-interview": ("Memory Diagram (Interview)", "Memory Diagram", "Stack, heap, metaspace — interview whiteboard layout."),
    "thread-lifecycle-interview": ("Thread Lifecycle (Interview)", "Thread Lifecycle", "NEW → RUNNABLE → TERMINATED state diagram."),
}


def iter_module_topics(modules: list) -> list[tuple[int, str, str, list[str]]]:
    """Yield (mod_id, mod_title, slug, topic_index_within_module)."""
    result: list[tuple[int, str, str, int]] = []
    for mod in modules:
        mod_id = mod["id"]
        mod_title = mod["focus"]
        slugs: list[str] = []
        if mod.get("groups"):
            for group in mod["groups"]:
                slugs.extend(group["topics"])
        else:
            slugs = list(mod["topics"])
        for idx, slug in enumerate(slugs):
            result.append((mod_id, mod_title, slug, idx + 1))
    return result


def write_order_yaml(modules: list, path: Path) -> None:
    topics: list[str] = []
    for mod in modules:
        if mod.get("groups"):
            for group in mod["groups"]:
                topics.extend(group["topics"])
        else:
            topics.extend(mod["topics"])
    content = (
        "# Flat topic order — derived from java_cheatsheet_modules.yaml.\n"
        "# Prefer editing data/java_engineering_modules.yaml for module structure.\n"
        "topics:\n"
    )
    content += "".join(f"  - {s}\n" for s in topics)
    path.write_text(content, encoding="utf-8")


def related_links(slug: str, ordered: list[str]) -> str:
    idx = ordered.index(slug) if slug in ordered else -1
    links: list[str] = []
    if idx > 0:
        prev = ordered[idx - 1]
        title = TITLES[prev][1]
        links.append(f"- [Previous: {title}](/java-engineering/{prev}/)")
    if 0 <= idx < len(ordered) - 1:
        nxt = ordered[idx + 1]
        title = TITLES[nxt][1]
        links.append(f"- [Next: {title}](/java-engineering/{nxt}/)")
    links.append("- [Java Engineering Handbook Index](/java-engineering/)")
    return "\n".join(links)


def stub_body(title: str, related: str, interview: bool = False) -> str:
    if interview:
        return f"""## Executive Summary

_One-page interview reference for **{title}** — no coding problems._

---

## Why It Exists

| Need | How this page helps |
| :--- | :--- |
| Last-minute revision | Scannable tables and diagrams |
| Whiteboard interviews | Canonical facts without tutorial depth |
| Senior probes | Trade-offs in one screen |

---

## Key Concepts

```mermaid
flowchart TD
  topic["{title}"]
  topic --> fact1["Core fact 1"]
  topic --> fact2["Core fact 2"]
  topic --> fact3["Core fact 3"]
```

| Concept | Summary |
| :--- | :--- |
| _TODO_ | _TODO_ |

---

## Syntax

| Item | Reference |
| :--- | :--- |
| _TODO_ | _TODO_ |

---

## Example

```java
// TODO: minimal illustrative snippet
public class Example {{
    public static void main(String[] args) {{
        System.out.println("TODO");
    }}
}}
```

---

## Internal Working

- _TODO: behind-the-scenes behavior in 3–5 bullets_

---

## Common Mistakes

- _TODO: typical interview wrong answers_

---

## Best Practices

- _TODO: what seniors expect you to say_

---

## Interview Questions

{{< interview-answer >}}
**Q:** _TODO interview question_

**A:** _TODO concise answer_
{{< /interview-answer >}}

---

## Related Topics

{related}
"""
    return f"""## Executive Summary

_TODO: Explain **{title}** in simple English — one short paragraph._

---

## Why It Exists

| Problem | How {title} helps |
| :--- | :--- |
| _TODO_ | _TODO_ |

---

## Key Concepts

```mermaid
flowchart LR
  A["Concept A"] --> B["Concept B"]
  B --> C["Concept C"]
```

| Concept | Description |
| :--- | :--- |
| _TODO_ | _TODO_ |

{{% note %}}
_TODO: important note for readers._
{{% /note %}}

---

## Syntax

```java
// TODO: canonical syntax pattern
```

| Element | Meaning |
| :--- | :--- |
| _TODO_ | _TODO_ |

---

## Example

```java
public class Example {{
    public static void main(String[] args) {{
        // TODO: small runnable example
        System.out.println("TODO");
    }}
}}
```

{{% tip %}}
_TODO: practical tip._
{{% /tip %}}

---

## Internal Working

- _TODO: JVM / compiler / runtime behavior_
- _TODO: performance characteristic_

```mermaid
sequenceDiagram
    participant App
    participant JVM
    App->>JVM: operation
    JVM-->>App: result
```

---

## Common Mistakes

{{% warning %}}
_TODO: pitfall that causes bugs in production._
{{% /warning %}}

- _TODO: mistake 1_
- _TODO: mistake 2_

---

## Best Practices

- _TODO: production-ready recommendation_
- _TODO: readability or performance guidance_

---

## Interview Questions

{{< interview-answer >}}
**Q:** _TODO frequently asked question_

**A:** _TODO answer in 2–4 sentences_
{{< /interview-answer >}}

{{< interview-answer >}}
**Q:** _TODO follow-up probe_

**A:** _TODO answer_
{{< /interview-answer >}}

---

## Related Topics

{related}
"""


def main() -> None:
    modules_path = ROOT / "data" / "java_cheatsheet_modules.yaml"
    with open(modules_path, encoding="utf-8") as f:
        modules = yaml.safe_load(f)["modules"]

    write_order_yaml(modules, ROOT / "data" / "java_cheatsheet_order.yaml")

    ordered: list[str] = []
    for mod in modules:
        if mod.get("groups"):
            for group in mod["groups"]:
                ordered.extend(group["topics"])
        else:
            ordered.extend(mod["topics"])

    out_dir = ROOT / "content" / "java-cheatsheet"
    out_dir.mkdir(parents=True, exist_ok=True)

    interview_module_id = 15

    for mod_id, mod_title, slug, topic_idx in iter_module_topics(modules):
        if slug in SKIP:
            print(f"skip {slug}")
            continue
        if slug not in TITLES:
            raise KeyError(f"Missing TITLES entry for {slug}")
        title, short, desc = TITLES[slug]
        section_ref = f"{mod_id}.{topic_idx}"
        is_interview = mod_id == interview_module_id
        related = related_links(slug, ordered)
        front_matter = f"""---
title: "{title}"
date: 2026-06-30T10:00:00+00:00
draft: true
description: "{desc}"
tags: ["java", "java-cheatsheet", "handbook"]
categories: ["Java Engineering Handbook"]
shortTitle: "{short}"
module: {mod_id}
moduleTitle: "{mod_title}"
sectionRef: "{section_ref}"
javaVersions: ["8", "11", "17", "21", "25"]
---

"""
        path = out_dir / f"{slug}.md"
        path.write_text(
            front_matter + stub_body(title, related, interview=is_interview),
            encoding="utf-8",
        )
        print(f"wrote {path.name}")

    print("done")


if __name__ == "__main__":
    main()
