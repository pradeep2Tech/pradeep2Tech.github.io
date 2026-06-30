---
title: "Spring Boot Cheat Sheet"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Spring Boot quick reference — annotations, config, REST, JPA, security, actuator, and production snippets. Boot 2.x and 3.x."
tags: ["spring-boot", "spring", "cheatsheet", "handbook"]
ShowPageNums: true
---

Dense **cheat sheets** for engineers who already know Spring Boot — tables and copy-paste snippets, not tutorials. Pairs with [Java Engineering](/java-engineering/) for language fundamentals and [Microservices](/microservices/) for distributed architecture.

**Target:** Spring Boot 2.x / 3.x · **21 pages** · **9 modules**

{{% note %}}
This is a **quick recap** section. No "how to create a project" walkthroughs — bootstrap commands live on the [Quick Reference](/spring-boot/spring-boot-quick-ref/) page only.
{{% /note %}}

---

## Module Map

| # | Module | Start here |
| :--: | :--- | :--- |
| 1 | Bootstrap & Core | [Quick Ref](/spring-boot/spring-boot-quick-ref/) · [Annotations](/spring-boot/annotations-stereotypes/) · [DI](/spring-boot/dependency-injection-ref/) |
| 2 | Configuration | [Config](/spring-boot/configuration-ref/) |
| 3 | REST & Validation | [REST](/spring-boot/rest-api-ref/) · [Validation](/spring-boot/validation-ref/) · [Exceptions](/spring-boot/exception-handling-ref/) |
| 4 | Data & Transactions | [JPA](/spring-boot/jpa-quick-ref/) · [Queries](/spring-boot/jpa-queries-ref/) · [Transactions](/spring-boot/transactions-ref/) |
| 5 | Security | [Security](/spring-boot/security-quick-ref/) · [JWT/OAuth](/spring-boot/jwt-oauth-ref/) |
| 6 | Cross-Cutting | [Caching](/spring-boot/caching-ref/) · [Schedule/Async](/spring-boot/scheduling-async-ref/) · [Events](/spring-boot/events-ref/) |
| 7 | Production | [Actuator](/spring-boot/actuator-ref/) · [Observability](/spring-boot/observability-ref/) · [Testing](/spring-boot/testing-ref/) · [Deploy](/spring-boot/production-deployment-ref/) |
| 8 | Distributed | [Spring Cloud](/spring-boot/spring-cloud-ref/) · [Messaging](/spring-boot/messaging-ref/) |
| 9 | Interview | [Interview Ref](/spring-boot/spring-boot-interview-ref/) |

---

## Page Format

Every sheet uses the same scan-friendly layout:

| Section | Purpose |
| :--- | :--- |
| **At a Glance** | 3–5 bullets |
| **Reference Tables** | Main content |
| **Snippets** | Copy-paste Java / YAML |
| **Internals & Gotchas** | Short pitfalls |
| **Production Notes** | Ops-focused tips |
| **Interview Probes** | 1–2 max on key pages |

Use **Previous / Next** at the bottom of each page to walk the curriculum.

---

## Out of Scope

Core Java → [Java Engineering](/java-engineering/) · Design patterns → [Design Patterns](/design-patterns/) · K8s deep dive → [Kubernetes Handbook](/kubernetes-handbook/) · Kafka internals → [Kafka Handbook](/kafka-handbook/)

---

## Regenerate

```bash
python scripts/build_spring_boot_handbook.py
```
