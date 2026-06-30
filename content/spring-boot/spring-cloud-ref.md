---
title: "Spring Cloud Reference"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Config, discovery, Gateway, OpenFeign, Resilience4j."
tags: ["spring-boot", "spring", "cheatsheet", "handbook"]
categories: ["Spring Boot Cheat Sheet"]
shortTitle: "Spring Cloud"
module: 8
moduleTitle: "Distributed"
sectionRef: "8.1"
ShowToc: true
cheatSheet: true
---

## At a Glance

- Spring Cloud — config, discovery, gateway, resilience on top of Boot.
- OpenFeign for declarative HTTP clients.
- Resilience4j for circuit breaker / retry / bulkhead.

---

## Reference Tables

| Component | Role |
| :--- | :--- |
| Config Server | Central Git-backed config |
| Eureka / Consul | Service discovery |
| Spring Cloud Gateway | Edge routing, filters |
| OpenFeign | `@FeignClient` REST |
| Resilience4j | `@CircuitBreaker`, `@Retry` |

| Pattern | Annotation |
| :--- | :--- |
| Circuit breaker | `@CircuitBreaker(name, fallbackMethod)` |
| Retry | `@Retry(name)` |
| Bulkhead | `@Bulkhead(name)` |

---

## Snippets

```java
@FeignClient(name = "inventory")
public interface InventoryClient {
  @GetMapping("/api/stock/{sku}")
  StockDto getStock(@PathVariable String sku);
}
```

---

## Internals & Gotchas

- Deep distributed patterns → [Microservices Playbook](/microservices/).

---

## Production Notes

- Timeouts on every Feign client.

---

## Interview Probes


{< interview-answer >}
**Q:** Gateway vs BFF?

**A:** Gateway = platform edge; BFF = per-client API aggregation.
{< /interview-answer >}

---

## See Also

- [Previous: Production](/spring-boot/production-deployment-ref/)
- [Next: Messaging](/spring-boot/messaging-ref/)
- [Spring Boot Cheat Sheet Index](/spring-boot/)
- [Java Engineering](/java-engineering/)
- [Microservices Playbook](/microservices/)
