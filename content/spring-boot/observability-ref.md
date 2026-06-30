---
title: "Observability Reference"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Logging, MDC, Micrometer, OpenTelemetry, tracing hooks."
tags: ["spring-boot", "spring", "cheatsheet", "handbook"]
categories: ["Spring Boot Cheat Sheet"]
shortTitle: "Observability"
module: 7
moduleTitle: "Production"
sectionRef: "7.2"
ShowToc: true
cheatSheet: true
---

## At a Glance

- SLF4J + Logback default; config via `logback-spring.xml`.
- MDC for trace/correlation IDs.
- Micrometer → Prometheus / OTLP.

---

## Reference Tables

| Concern | Tool |
| :--- | :--- |
| Logs | Logback JSON appenders |
| Correlation | MDC `traceId` |
| Metrics | Micrometer counters/timers |
| Traces | Micrometer tracing / OTel |
| Dashboards | Grafana + Prometheus |

---

## Snippets

```java
// MDC in filter
MDC.put("traceId", traceId);
try { chain.doFilter(req, res); }
finally { MDC.clear(); }
```

---

## Internals & Gotchas

- Clear MDC in `finally` — thread pool leaks context.
- Don't log PII/secrets.

---

## Production Notes

- Structured JSON logs in prod.
- RED/USE metrics for services.

---

## Interview Probes


{< interview-answer >}
**Q:** Metrics vs logs vs traces?

**A:** Metrics = aggregates; logs = events; traces = request path across services.
{< /interview-answer >}

---

## See Also

- [Previous: Actuator](/spring-boot/actuator-ref/)
- [Next: Testing](/spring-boot/testing-ref/)
- [Spring Boot Cheat Sheet Index](/spring-boot/)
- [Java Engineering](/java-engineering/)
- [Microservices Playbook](/microservices/)
