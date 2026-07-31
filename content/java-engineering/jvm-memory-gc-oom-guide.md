---
title: "JVM Production Interview Refresh"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "JVM memory, GC, OOM, and production diagnosis for senior interviews."
tags: ["java", "jvm", "production", "interview", "cheatsheet"]
categories: ["Java Engineering Handbook"]
shortTitle: "JVM Production"
module: 4
moduleTitle: "JVM in Production"
sectionRef: "4.1"
cheatSheet: true
aliases: ["jvm-memory-and-gc", "memory-leaks-and-oom", "memory-diagram-interview", "gc-summary-interview"]
---

## At a Glance

- For architects, JVM knowledge means diagnosing capacity, latency, leaks, and upgrade risk.
- Tune from evidence: service-level latency, allocation rate, GC logs, JFR, dumps, and container limits.
- Explain collector internals only if the interviewer asks a follow-up.

---

## Memory Map

| Area | Holds | Common failure signal |
| :--- | :--- | :--- |
| Heap | Objects and arrays | `Java heap space`, rising live set, GC pressure |
| Thread stacks | Frames and local variables | `StackOverflowError`, native-thread pressure |
| Metaspace | Class metadata | Class-loader leak, `Metaspace` OOM |
| Direct/native memory | Buffers, JNI, JVM structures | Process memory high while heap looks normal |
| Code cache | Compiled methods | Compilation disabled/full-code-cache warnings |

## Collector Choice

| Goal | Typical starting point | Decision evidence |
| :--- | :--- | :--- |
| Balanced general service | G1 | Pause percentiles, throughput, heap size |
| Very low pauses / large heap | ZGC | Latency target, CPU headroom, supported JDK |
| Batch throughput | Parallel GC | Total completion time matters more than pauses |

Do not promise that changing collectors fixes allocation churn, leaks, undersized containers, or downstream latency.

## Production Diagnosis

| Symptom | First evidence | Likely directions |
| :--- | :--- | :--- |
| Heap keeps rising | GC log + post-GC live set + heap histogram | Retention leak, cache growth, workload growth |
| Long pauses | GC log/JFR, allocation and promotion rate | Heap sizing, allocation churn, collector fit |
| High CPU, normal heap | JFR/profiler + repeated thread dumps | Hot loop, serialization, contention, excessive retries |
| Process memory > heap | Native memory tracking / container metrics | Direct buffers, threads, JNI, metaspace |
| Service frozen | Thread dumps several seconds apart | Deadlock, pool starvation, blocking dependency |
| OOM restart | Exact OOM type + dump + container events | Heap, metaspace, native threads, direct memory, cgroup kill |

## Artifact to Use

| Artifact | Answers |
| :--- | :--- |
| Heap dump | What retains memory and along which reference path? |
| Thread dump | What are threads waiting on, and is progress occurring? |
| GC log | How often, how long, how much memory reclaimed? |
| JFR | Where are CPU, allocation, locks, I/O, and pauses spent over time? |
| Application metrics/traces | Which user path and dependency correlate with the JVM symptom? |

## Strong Scenario Answer

1. Confirm user impact and stabilize with a safe operational action.
2. Capture evidence before restart when feasible.
3. Separate leak from load by checking the post-GC live-set trend.
4. Correlate JVM evidence with releases, traffic, caches, and downstream latency.
5. Fix the cause, canary it, and add a regression alert/load test.

## Quick Gotchas

- “GC exists, so Java cannot leak” is false; reachable objects can be retained forever.
- A bigger heap can delay an OOM and lengthen recovery without fixing retention.
- Container memory includes more than `-Xmx`.
- A single thread dump is a snapshot; compare several for progress.
- Avoid memorizing flags without explaining the metric and risk they address.

---

## See Also

[← Concurrency](/java-engineering/java-threading-interview-guide/) · [Modern Java →](/java-engineering/java-version-migration-guide/)
