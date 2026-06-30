---
title: "Dependency Injection Reference"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Constructor injection, scopes, @Bean, lifecycle callbacks — recap only."
tags: ["spring-boot", "spring", "cheatsheet", "handbook"]
categories: ["Spring Boot Cheat Sheet"]
shortTitle: "DI"
module: 1
moduleTitle: "Bootstrap & Core"
sectionRef: "1.3"
ShowToc: true
cheatSheet: true
---

## At a Glance

- Constructor injection is default when one constructor exists.
- Singleton scope unless `@Scope` specified.
- Avoid field `@Autowired` in new code.

---

## Reference Tables

| Injection | When |
| :--- | :--- |
| Constructor | **Preferred** — required deps, immutable |
| Setter | Rare — optional deps |
| Field | Legacy — hard to test |

| Scope | Instances |
| :--- | :--- |
| singleton | One per context (default) |
| prototype | New per injection / getBean |
| request / session | Web-scoped (needs proxy into singleton) |

| Lifecycle | Hook |
| :--- | :--- |
| After inject | `@PostConstruct` |
| Before destroy | `@PreDestroy` |
| Programmatic | `InitializingBean` / `DisposableBean` |

---

## Snippets

```java
@Service
public class OrderService {
  private final OrderRepository repo;
  public OrderService(OrderRepository repo) { this.repo = repo; }
}
```

---

## Internals & Gotchas

- Circular deps fail at startup — refactor or `@Lazy` (last resort).
- Prototype into singleton needs scoped proxy.

---

## Production Notes

- No request state in singleton beans.

---

## Interview Probes


{< interview-answer >}
**Q:** Why constructor injection?

**A:** Explicit, immutable, unit-testable without Spring.
{< /interview-answer >}

---

## See Also

- [Previous: Annotations](/spring-boot/annotations-stereotypes/)
- [Next: Config](/spring-boot/configuration-ref/)
- [Spring Boot Cheat Sheet Index](/spring-boot/)
- [Java Engineering](/java-engineering/)
- [Microservices Playbook](/microservices/)
