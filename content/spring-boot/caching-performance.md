---
title: "Caching & Performance"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Cache strategies, Redis, @Async, thread pools, connection pools — performance tuning."
tags: ["spring-boot", "spring", "handbook", "interview"]
categories: ["Spring Boot Handbook"]
shortTitle: "Cache & Perf"
module: 6
moduleTitle: "Caching & Performance"
sectionRef: "6.1"
ShowToc: true
interviewHandbook: true
aliases:
  - caching-ref
  - scheduling-async-ref
---

## Cache Aside vs Write Through?

**Difficulty:** Medium  
**Expected Answer Time:** 1 min

### Short Answer

Cache Aside: app reads cache, on miss loads DB and populates cache; writes go to DB then invalidate cache. Write Through: write to cache and cache synchronously writes to DB.

### Detailed Explanation

Spring `@Cacheable` is cache-aside on reads. `@CachePut` updates cache after method. `@CacheEvict` on mutations. Write-through needs custom `CacheWriter` or application logic. Write-behind: async DB write — consistency risk.

### Internal Working

AOP proxy intercepts `@Cacheable` — self-invocation bypasses cache.

### Production Notes

Redis for distributed; Caffeine for local L1. TTL + jitter against stampede. Don't cache nulls without `unless`.

### Common Mistakes

Caching mutable objects — stale references. No TTL on config data.

### Follow-up Questions

- Cache stampede mitigation?
- Redis vs Caffeine two-tier?

---
## How does @Async work internally?

**Difficulty:** Hard  
**Expected Answer Time:** 3 min

### Short Answer

`@EnableAsync` registers `AsyncAnnotationBeanPostProcessor` which wraps `@Async` methods to submit `Runnable`/`Callable` to `TaskExecutor` instead of running on caller thread.

### Detailed Explanation

Default executor: `SimpleAsyncTaskExecutor` (new thread per task — dangerous in prod). Provide `@Bean TaskExecutor` with bounded pool. Return `CompletableFuture` for composition. Exception handling: `AsyncUncaughtExceptionHandler`.

### Internal Working

Proxy-based — public methods only. `SecurityContext` and `MDC` don't propagate unless `TaskDecorator` configured.

### Production Notes

Size pool from metrics: queue depth, rejection count. Use virtual threads (Boot 3.2+) for IO-bound `@Async` with caution on pinning.

### Common Mistakes

Unbounded thread creation. Missing `TaskDecorator` — lost trace IDs.

### Follow-up Questions

- @Async vs CompletableFuture supplyAsync?
- Virtual thread executor for @Async?

---
## Thread pool sizing for Spring Boot?

**Difficulty:** Medium  
**Expected Answer Time:** 1 min

### Short Answer

Separate pools for HTTP (Tomcat threads), `@Async`, and `@Scheduled`; size from load testing — CPU-bound ≈ cores; blocking IO needs higher or virtual threads.

### Detailed Explanation

Tomcat: `server.tomcat.threads.max`. Custom `ThreadPoolTaskExecutor` with `corePoolSize`, `maxPoolSize`, `queueCapacity`, named threads. RejectedExecutionPolicy: `CallerRunsPolicy` for backpressure.

### Internal Working

HikariCP pool separate from thread pool — don't conflate.

### Production Notes

Monitor pool saturation via Micrometer. Graceful shutdown: `waitForTasksToCompleteOnShutdown`.

### Common Mistakes

One giant pool for everything. `queueCapacity` Integer.MAX_VALUE hiding overload.

### Follow-up Questions

- Tomcat vs reactive Netty thread model?
- HikariCP pool size formula?

---
## @Scheduled and connection pool tuning?

**Difficulty:** Medium  
**Expected Answer Time:** 1 min

### Short Answer

`@Scheduled` uses single-threaded executor by default — configure `TaskScheduler` pool for parallel jobs. HikariCP: `maximumPoolSize` ≈ concurrent DB users, not thread count.

### Detailed Explanation

`fixedDelay` waits after completion; `fixedRate` can overlap. Clustered schedules need ShedLock or Quartz. Hikari: `connectionTimeout`, `maxLifetime` < DB idle timeout, `leakDetectionThreshold` in dev.

### Internal Working

Spring Boot auto-configures Hikari when JDBC on classpath.

### Production Notes

Don't schedule long jobs on default single thread. Align `maxLifetime` with DB/proxy timeouts.

### Common Mistakes

Pool size = thread count myth. `@Scheduled` blocking all cron jobs.

### Follow-up Questions

- ShedLock pattern?
- Read replica routing?

---

## See Also

- [Previous: Security](/spring-boot/security/)
- [Next: Messaging](/spring-boot/messaging-events/)
- [100+ Interview Questions](/spring-boot/interview-questions/)
- [Spring Boot Handbook Index](/spring-boot/)
- [Java Engineering](/java-engineering/)
- [Microservices Playbook](/microservices/) — Saga, Outbox, CQRS, API Gateway
- [Kafka Handbook](/kafka-handbook/)
- [Security Architecture](/security-architecture/)
