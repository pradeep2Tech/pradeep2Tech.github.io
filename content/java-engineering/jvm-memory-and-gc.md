---
title: "JVM Memory & GC"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Heap regions, collectors (G1, ZGC, Shenandoah), allocation, and GC logs."
tags: ["java", "java-engineering", "handbook"]
categories: ["Java Engineering Handbook"]
shortTitle: "Memory & GC"
module: 7
moduleTitle: "Memory & GC"
sectionRef: "7.1"
ShowToc: true
cheatSheet: true
---

## At a Glance

- Heap: young (Eden + Survivors) + old gen; all Java objects (except off-heap/direct).
- Non-heap: Metaspace (class metadata), CodeCache, thread stacks, direct buffers.
- Default collector (17+ server): G1; low-latency options: ZGC, Shenandoah.
- GC logs: unified `-Xlog:gc*` (9+).

---

## Reference Tables

| Region | Holds | GC event |
| :--- | :--- | :--- |
| Eden | New objects | Minor GC |
| Survivor | Copied young | Minor GC |
| Old | Tenured | Major / mixed |
| Metaspace | Class metadata | Metaspace GC trigger |

| Collector | Pause goal | Heap scale |
| :--- | :--- | :--- |
| G1 | Configurable target | General purpose |
| ZGC | Sub-ms typical | Large heaps |
| Shenandoah | Concurrent compact | Large heaps |
| Parallel | Throughput | Batch |

| Flag (11+) | Effect |
| :--- | :--- |
| `-XX:+UseG1GC` | G1 (often default) |
| `-XX:MaxGCPauseMillis` | G1 pause target |
| `-XX:+UseZGC` | ZGC |
| `-Xlog:gc*:file=gc.log:time,uptime,level,tags` | Logging |

---

## Snippets

```bash
# Container-aware heap (10+)
java -XX:MaxRAMPercentage=75.0 -XX:+UseG1GC -jar app.jar
```

---

## Internals & Gotchas

- TLAB: per-thread Eden allocation buffer — reduces CAS contention.
- Card table / remembered set for cross-gen references.
- Humongous objects (G1): >50% region size → special handling.

---

## Production Notes

- Set heap max in containers — never rely on default ergonomics alone.
- Tune after metrics: GC pause P99, allocation rate, promotion failure.
- `-XX:+HeapDumpOnOutOfMemoryError` with path on persistent volume.

---

## Interview Probes


{< interview-answer >}
**Q:** Minor vs major GC?

**A:** Minor: young gen collection, frequent, stop-the-world usually short. Major/old: tenured collection — longer pauses unless mostly concurrent collector.
{< /interview-answer >}

{< interview-answer >}
**Q:** When ZGC over G1?

**A:** Very large heaps, strict pause SLAs, willing to trade some CPU. Measure — not default for all services.
{< /interview-answer >}

---

## See Also

- [Previous: Virtual Threads](/java-engineering/virtual-threads-structured-concurrency/)
- [Next: Leaks & OOM](/java-engineering/memory-leaks-and-oom/)
- [Leaks & OOM](/java-engineering/memory-leaks-and-oom/)
- [GC Interview](/java-engineering/gc-summary-interview/)
- [JVM Flags](/java-engineering/jvm-flags-and-tuning/)
- [Java Engineering Handbook Index](/java-engineering/)
