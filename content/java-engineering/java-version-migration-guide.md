---
title: "Modern Java Interview Refresh"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Java 8 to 25 feature and migration refresh for experienced engineers."
tags: ["java", "modern-java", "migration", "interview", "cheatsheet"]
categories: ["Java Engineering Handbook"]
shortTitle: "Modern Java"
module: 5
moduleTitle: "Modern Java"
sectionRef: "5.1"
cheatSheet: true
aliases: ["java-lts-release-matrix", "java-recent-features", "java-version-features-interview"]
---

## At a Glance

- Discuss features by business/codebase impact, not by reciting every JEP.
- For upgrades, emphasize support, security, dependencies, observability, rollout, and rollback.
- Know whether a feature is final, preview, or incubating before recommending it.

---

## LTS Refresh

| Release | Features worth mentioning | Practical impact |
| :--: | :--- | :--- |
| 8 | Lambdas, streams, `Optional`, `java.time`, `CompletableFuture` | Functional baseline still present in legacy estates |
| 11 | Standard HTTP client, runtime/JDK cleanup | Common first step away from Java 8 |
| 17 | Records, sealed classes, pattern matching for `instanceof`, stronger encapsulation | Cleaner domain models; old reflective libraries may break |
| 21 | Virtual threads, record patterns, pattern `switch`, sequenced collections | Simpler high-concurrency blocking services and expressive domain code |
| 25 | Current LTS; confirm final feature set and vendor support for your estate | Upgrade target depends on framework and platform certification |

## Feature Decisions

| Feature | Use when | Watch for |
| :--- | :--- | :--- |
| Record | Immutable data carrier/value | Not a shortcut for every entity or behavior-rich aggregate |
| Sealed type | Domain has a deliberately closed set of outcomes | Cross-module extensibility requirements |
| Pattern `switch` | Exhaustive branching over a known hierarchy | Keep business rules cohesive, not scattered switches |
| Virtual thread | Many mostly-blocking tasks | Downstream limits, `ThreadLocal` usage, pinning, observability |
| `HttpClient` | Standard synchronous/async HTTP needs | Resilience, pooling, telemetry, and policy still need design |
| Text block | Multi-line JSON/SQL/templates | It improves syntax, not query safety |

## Upgrade Playbook

1. Inventory JDK, framework, libraries, build plugins, agents, base images, and removed APIs.
2. Upgrade dependencies and build tooling before changing application code style.
3. Compile/test with the target JDK; run compatibility, integration, load, and startup tests.
4. Compare latency, CPU, memory, GC, and error baselines under representative traffic.
5. Canary one service/cohort, keep rollback simple, then roll out gradually.
6. Adopt new language/concurrency features separately from the runtime migration when possible.

## Interview Prompts

| Prompt | Strong answer direction |
| :--- | :--- |
| Why leave Java 8? | Security/support, ecosystem compatibility, performance, developer productivity—not novelty |
| Biggest migration risk? | Framework/agent compatibility, illegal reflection, removed modules/APIs, container assumptions |
| Upgrade runtime and refactor together? | Usually separate them to reduce variables and rollback risk |
| Why LTS? | Predictable vendor support and estate standardization; LTS is an operational policy, not superior semantics |
| Adopt virtual threads everywhere? | No; select by workload, load-test, and retain downstream concurrency limits |

## Quick Gotchas

- Do not claim every feature arrived in an LTS release just because teams adopted it there.
- Preview features require an explicit lifecycle and compatibility decision.
- New JDK performance does not remove the need for application benchmarks.
- Strong encapsulation failures should usually be fixed by upgrading libraries, not permanent `--add-opens` sprawl.

---

## See Also

[← JVM in Production](/java-engineering/jvm-memory-gc-oom-guide/) · [Interview Sprint →](/java-engineering/top-100-java-interview-questions/)
