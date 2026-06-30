---
title: "Caching Reference"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "@Cacheable, CacheManager, Redis, eviction."
tags: ["spring-boot", "spring", "cheatsheet", "handbook"]
categories: ["Spring Boot Cheat Sheet"]
shortTitle: "Caching"
module: 6
moduleTitle: "Cross-Cutting"
sectionRef: "6.1"
ShowToc: true
cheatSheet: true
---

## At a Glance

- `@EnableCaching` + `CacheManager` bean.
- `@Cacheable` on method — key from SpEL.
- Redis for distributed cache.

---

## Reference Tables

| Annotation | Effect |
| :--- | :--- |
| `@Cacheable` | Return cached value on hit |
| `@CachePut` | Always run + update cache |
| `@CacheEvict` | Remove entries |

| Manager | Backend |
| :--- | :--- |
| `CaffeineCacheManager` | In-process |
| `RedisCacheManager` | Distributed |

---

## Snippets

```java
@Cacheable(value = "orders", key = "#id")
public OrderDto findById(Long id) { ... }

@CacheEvict(value = "orders", key = "#id")
public void invalidate(Long id) { ... }
```

---

## Internals & Gotchas

- Cache nulls carefully (`unless`).
- TTL + key design prevents stale reads.

---

## Production Notes

- `@Cacheable` on self-call doesn't work — proxy issue.

---

## Interview Probes


{< interview-answer >}
**Q:** Cache stampede?

**A:** Sync cache load, random TTL jitter, or single-flight pattern.
{< /interview-answer >}

---

## See Also

- [Previous: JWT/OAuth](/spring-boot/jwt-oauth-ref/)
- [Next: Schedule/Async](/spring-boot/scheduling-async-ref/)
- [Spring Boot Cheat Sheet Index](/spring-boot/)
- [Java Engineering](/java-engineering/)
- [Microservices Playbook](/microservices/)
