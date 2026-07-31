---
title: "Java Interview Sprint"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "A high-signal Java interview checklist for experienced engineers, leads, and architects."
tags: ["java", "interview", "architect", "cheatsheet"]
categories: ["Java Engineering Handbook"]
shortTitle: "Interview Sprint"
module: 6
moduleTitle: "Interview Sprint"
sectionRef: "6.1"
cheatSheet: true
---

## At a Glance

- These are the high-value questions distilled from the supplied 245-question sheet.
- Practice a 60-second answer: decision → trade-off → production example → failure mode.
- If an interviewer asks internals, answer the specific probe; do not volunteer a lecture.

---

## Core Java

| Question | Your answer must include |
| :--- | :--- |
| Composition or inheritance? | Coupling, substitution, testability, stable IS-A relationship |
| How do you design an immutable class? | Final state, no mutation, defensive copies, safe publication |
| Why must `equals` and `hashCode` agree? | Hash lookup correctness and mutable-key failure |
| Checked or unchecked exception? | Caller recovery, API boundary, translation, preserved cause |
| `extends` vs `super` in generics? | PECS and API flexibility |
| Stream or loop? | Readability, allocation/boxing, side effects, measured performance |
| Good use of `Optional`? | Return absence; avoid fields/parameters/`get()` |

## Collections

| Question | Your answer must include |
| :--- | :--- |
| How do you select a collection? | Access pattern, order, uniqueness, complexity, mutation, concurrency |
| `ArrayList` or `LinkedList`? | Real workload, locality, memory, indexed access—not theory alone |
| `HashMap`, `TreeMap`, or `LinkedHashMap`? | Lookup vs sorted/range vs stable/access order |
| Concurrent shared map? | `ConcurrentHashMap`, atomic methods, compound invariant limits |
| Read-mostly concurrent list? | `CopyOnWriteArrayList` and write-copy cost |
| Queue under peak load? | Bounded capacity, backpressure, rejection, metrics |

## Concurrency

| Question | Your answer must include |
| :--- | :--- |
| What does `volatile` solve? | Visibility/order, not compound atomicity |
| How do you make a class thread-safe? | State ownership, invariants, publication, locking/immutability, tests |
| How do you size a pool? | CPU vs blocking work, downstream capacity, queueing, measurement |
| `synchronized` or `ReentrantLock`? | Simplicity vs timeout/interruptibility/conditions |
| How do you diagnose a deadlock? | Repeated thread dumps, lock cycle, consistent ordering/ownership fix |
| `thenApply` or `thenCompose`? | Transform vs dependent async flattening |
| When use virtual threads? | Blocking I/O at scale, simpler code, downstream limits, load test |

## JVM and Production

| Question | Your answer must include |
| :--- | :--- |
| Is rising heap a leak? | Post-GC live set, workload/caches, heap dump retained paths |
| Heap dump vs thread dump vs GC log? | Retention vs execution/waits vs collection/pause behavior |
| G1 or ZGC? | Latency/throughput goal, heap, CPU, JDK, benchmark |
| High CPU with normal memory? | JFR/profiling, hot threads, contention, retry loops, workload |
| Process killed despite safe `-Xmx`? | Native/direct/thread/metaspace memory and container limit |
| How do you handle an OOM? | Exact type, stabilize, capture evidence, root cause, canary fix |

## Modern Java

| Question | Your answer must include |
| :--- | :--- |
| Most useful Java 17/21 changes? | Records/sealed/patterns/virtual threads tied to actual use cases |
| How would you upgrade an estate? | Inventory, compatibility, test, baseline, canary, rollback |
| Would you refactor during a JDK upgrade? | Separate risk where possible |
| Why LTS? | Support and standardization policy |

## Architect Scenarios

Use this answer structure: **clarify → constrain → decide → failure modes → observe → evolve**.

1. A service creates thousands of threads and CPU rises. How do you distinguish blocking, contention, overload, and legitimate CPU work?
2. A pool rejects tasks at peak. What do you measure before changing pool or queue sizes?
3. Duplicate payments appear under concurrency. Where should idempotency be enforced across service instances?
4. Heap grows continuously. How do you distinguish a leak, an unbounded cache, and traffic growth?
5. GC pauses break the latency SLO. What evidence drives heap, collector, or allocation changes?
6. A shared cache is read-heavy with occasional writes. Which local structure fits, and when must it become a distributed cache?
7. A parallel stream is slower. How do workload size, splitting, ordering, boxing, common-pool contention, and blocking affect it?
8. A `ThreadLocal` leaks request data in a pool. How do you contain it and redesign context propagation?
9. A JDK upgrade breaks reflective access. How do you migrate without permanent flag exceptions?
10. A virtual-thread service overwhelms its database. Where do you enforce concurrency limits and backpressure?

## Optional Internals—Only If Asked

Be ready for a short follow-up on:

- Hash-based lookup: hash → bucket → equality; collision handling exists, but thresholds are trivia.
- `ConcurrentHashMap`: non-blocking reads plus fine-grained coordination/atomic methods; exact fields are trivia.
- Java Memory Model: visibility, ordering, atomicity, and happens-before; hardware details only on request.
- GC: roots, reachability, generational behavior, pause vs throughput; collector phase details only on request.
- Class loading/JIT: delegation and runtime optimization at a conceptual level; deep mechanics only for JVM-specialist roles.

---

## Final 30-Minute Drill

1. Pick any five questions above and answer each in 60 seconds.
2. Pick two scenarios and give a three-minute production answer.
3. Add one real incident or decision from your own work to each major area.
4. Revisit only the sheet where your answer became vague.

---

## See Also

[← Modern Java](/java-engineering/java-version-migration-guide/) · [Java Refresh Home](/java-engineering/)
