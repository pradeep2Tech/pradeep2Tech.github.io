---
title: "Production & Deployment Reference"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Fat JAR, Docker, graceful shutdown, externalized config."
tags: ["spring-boot", "spring", "cheatsheet", "handbook"]
categories: ["Spring Boot Cheat Sheet"]
shortTitle: "Production"
module: 7
moduleTitle: "Production"
sectionRef: "7.4"
ShowToc: true
cheatSheet: true
---

## At a Glance

- Fat JAR via `spring-boot-maven-plugin` / `bootJar`.
- Layered JAR for Docker cache.
- `server.shutdown=graceful` for K8s preStop.

---

## Reference Tables

| Topic | Setting / pattern |
| :--- | :--- |
| Graceful shutdown | `server.shutdown=graceful` |
| External config | env, ConfigMap, Spring Cloud Config |
| Health probes | actuator health groups |
| JVM in container | respect cgroup memory |
| DevTools | dev scope only |

---

## Snippets

```dockerfile
FROM eclipse-temurin:17-jre AS run
COPY target/app.jar /app.jar
ENTRYPOINT ["java","-jar","/app.jar"]
```

---

## Internals & Gotchas

- Thin JAR without repackage won't run.
- DevTools in prod image causes unexpected restarts.

---

## Production Notes

- 12-factor config: store in environment.
- Set resource limits matching JVM heap.

---

## Interview Probes


{< interview-answer >}
**Q:** Why layered JAR?

**A:** Docker layer cache — dependencies change less often than app code.
{< /interview-answer >}

---

## See Also

- [Previous: Testing](/spring-boot/testing-ref/)
- [Next: Spring Cloud](/spring-boot/spring-cloud-ref/)
- [Spring Boot Cheat Sheet Index](/spring-boot/)
- [Java Engineering](/java-engineering/)
- [Microservices Playbook](/microservices/)
