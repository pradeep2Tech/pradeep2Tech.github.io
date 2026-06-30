---
title: "Actuator Reference"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Health, metrics, info, Prometheus, K8s probes."
tags: ["spring-boot", "spring", "cheatsheet", "handbook"]
categories: ["Spring Boot Cheat Sheet"]
shortTitle: "Actuator"
module: 7
moduleTitle: "Production"
sectionRef: "7.1"
ShowToc: true
cheatSheet: true
---

## At a Glance

- Add `spring-boot-starter-actuator`.
- Expose endpoints via `management.endpoints.web.exposure.include`.
- K8s: separate liveness vs readiness.

---

## Reference Tables

| Endpoint | Path |
| :--- | :--- |
| health | `/actuator/health` |
| metrics | `/actuator/metrics` |
| prometheus | `/actuator/prometheus` |
| info | `/actuator/info` |

| Probe | Checks |
| :--- | :--- |
| liveness | JVM up — restart if fail |
| readiness | DB/upstream OK — remove from LB |

---

## Snippets

```yaml
management:
  endpoints:
    web:
      exposure:
        include: health,info,prometheus
  endpoint:
    health:
      probes:
        enabled: true
```

---

## Internals & Gotchas

- Don't expose all actuator endpoints publicly.
- Secure with Spring Security or network policy.

---

## Production Notes

- Custom `HealthIndicator` for DB, broker, downstream HTTP.

---

## Interview Probes


{< interview-answer >}
**Q:** Liveness vs readiness?

**A:** Liveness = process alive; readiness = can serve traffic.
{< /interview-answer >}

---

## See Also

- [Previous: Events](/spring-boot/events-ref/)
- [Next: Observability](/spring-boot/observability-ref/)
- [Observability](/spring-boot/observability-ref/)
- [Production](/spring-boot/production-deployment-ref/)
- [Spring Boot Cheat Sheet Index](/spring-boot/)
- [Java Engineering](/java-engineering/)
- [Microservices Playbook](/microservices/)
