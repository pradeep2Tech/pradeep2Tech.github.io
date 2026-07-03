---
title: "Production Deployment"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Fat JAR, Docker layers, graceful shutdown, externalized config — production deployment."
tags: ["spring-boot", "spring", "handbook", "interview"]
categories: ["Spring Boot Handbook"]
shortTitle: "Production"
module: 9
moduleTitle: "Production"
sectionRef: "9.1"
ShowToc: true
interviewHandbook: true
aliases:
  - production-deployment-ref
---

## Graceful shutdown in Spring Boot?

**Difficulty:** Medium  
**Expected Answer Time:** 1 min

### Short Answer

`server.shutdown=graceful` + `spring.lifecycle.timeout-per-shutdown-phase` stops accepting new requests, completes in-flight, then closes context.

### Detailed Explanation

K8s `preStop` hook + adequate `terminationGracePeriodSeconds`. Tomcat pauses connector; reactive Netty drains connections. `@PreDestroy` and `SmartLifecycle.stop()` run during shutdown phase.

### Internal Working

Shutdown hook registered by `SpringApplication`.

### Production Notes

Align K8s probe timeouts with shutdown duration. Drain message listeners before kill.

### Common Mistakes

Immediate SIGKILL without grace — truncated transactions. DevTools in prod image.

### Follow-up Questions

- Kubernetes preStop sleep?
- How to drain Kafka consumers?

---
## Layered JAR and Docker best practices?

**Difficulty:** Medium  
**Expected Answer Time:** 1 min

### Short Answer

Spring Boot layered JAR splits dependencies, resources, and app code for Docker layer cache; use JRE not JDK in runtime image.

### Detailed Explanation

`spring-boot-maven-plugin` `layers.enabled=true`. Dockerfile copies layers separately. Set JVM container flags: `-XX:MaxRAMPercentage`, respect cgroup limits.

### Internal Working

Layertools extract in build pipeline.

### Production Notes

Multi-stage build; non-root user; read-only root FS where possible.

### Common Mistakes

Fat JAR COPY without layers — slow deploys. JDK image bloat.

### Follow-up Questions

- CDS/AppCDS for faster startup?
- Native image trade-offs?

---

## See Also

- [Previous: Observability](/spring-boot/observability/)
- [Next: Testing](/spring-boot/testing/)
- [100+ Interview Questions](/spring-boot/interview-questions/)
- [Spring Boot Handbook Index](/spring-boot/)
- [Java Engineering](/java-engineering/)
- [Microservices Playbook](/microservices/) — Saga, Outbox, CQRS, API Gateway
- [Kafka Handbook](/kafka-handbook/)
- [Security Architecture](/security-architecture/)
