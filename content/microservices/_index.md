---
title: "Microservices Architecture Playbook"
date: 2026-07-03T15:00:00+00:00
draft: false
description: "Architect playbook for senior engineers — distributed systems, data ownership, resilience, migration, and production operations with clear learning paths."
tags: ["microservices", "architecture-playbook", "distributed-systems"]
categories: ["Microservices Architecture Playbook"]
shortTitle: "Microservices Playbook"
module: 0
moduleTitle: "Microservices Architecture Playbook"
sectionRef: "0"
weight: 0
microservicesTocPageSize: 50
playbookVersion: 3
---

# Microservices Architecture Playbook

Handbook for **senior engineers (6+ years), tech leads, and architects** who already design systems but need a **structured map** of how distributed services fit together in production.

> **If system design clicks but microservices feels scattered:** start with the [2-week fast path](#fast-path-6-years-system-design-background) below. This playbook assumes you understand load balancers, databases, and caching from [System Design](/system-design/) — it focuses on **what changes when you split a monolith across the network**.

---

## Fast path (6+ years, system design background)

Read in this order — each page builds on the previous:

| Step | Read | You will understand |
| :---: | :--- | :--- |
| 1 | [Architecture Styles](/microservices/01-architecture-styles/architecture-styles/) | Monolith vs modular monolith vs microservices — **when** to split |
| 2 | [Communication Topologies](/microservices/02-service-communication/communication-topologies/) | Sync vs async — **where** to draw the boundary |
| 3 | [API Gateway & BFF](/microservices/02-service-communication/api-gateway-and-bff/) | Edge ingress vs client-specific aggregation |
| 4 | [Database Per Service](/microservices/03-data-management/database-per-service/) | Why shared DB = distributed monolith |
| 5 | [Saga Pattern](/microservices/03-data-management/saga/) | Multi-service transactions without 2PC |
| 6 | [Outbox & CDC](/microservices/03-data-management/outbox-and-cdc/) | Reliable events after local DB commit |
| 7 | [Resilience Patterns](/microservices/05-resilience-patterns/resilience-patterns/) | Breaker, bulkhead, timeout, retry stack |
| 8 | [Observability](/microservices/08-observability/observability/) | Traces across service hops |

**Time:** ~6–8 hours focused reading. Then pick your depth path in [Learning Paths](/microservices/12-learning-paths/).

---

## How this relates to System Design

| System Design teaches | Microservices playbook adds |
| :--- | :--- |
| Capacity, NFRs, component boxes | **Team boundaries** and deploy independence |
| Load balancers, caches, databases | **Service-to-service** auth, discovery, sagas |
| Case studies (URL shortener, feed) | **Operational patterns** (outbox, mesh, strangler) |
| Interview whiteboard flow | **Production migration** and on-call failure modes |

Use [System Design](/system-design/) for *designing a system from requirements*. Use this playbook for *running and evolving a distributed service fleet*.

---

## Modules

| Module | Focus | Start here if… |
| :---: | :--- | :--- |
| 1 | [Architecture Styles](/microservices/01-architecture-styles/) | You need the monolith vs microservices decision |
| 2 | [Service Communication](/microservices/02-service-communication/) | You own API ingress or service integration |
| 3 | [Data Management](/microservices/03-data-management/) | You split databases or design cross-service writes |
| 4 | [Distributed Systems](/microservices/04-distributed-systems/) | You need CAP, hashing, isolation theory |
| 5 | [Resilience Patterns](/microservices/05-resilience-patterns/) | You debug cascades and timeouts |
| 6 | [Event-Driven](/microservices/06-event-driven/) | You choose Kafka vs sync APIs |
| 7 | [Platform Patterns](/microservices/07-platform-patterns/) | You deploy on Kubernetes / mesh |
| 8 | [Observability](/microservices/08-observability/) | You need traces across 10+ services |
| 9 | [Migration](/microservices/09-migration-modernization/) | You extract from a monolith |
| 10 | [Production Playbook](/microservices/10-production-playbook/) | You run releases and architecture reviews |
| 11 | [Interview Guide](/microservices/11-interview-guide/) | You prep for architect / lead interviews |
| 12 | [Learning Paths](/microservices/12-learning-paths/) | You want a multi-week curriculum |

---

## Paths by goal

| Goal | Path |
| :--- | :--- |
| **First time here (6+ yrs)** | [Fast path](#fast-path-6-years-system-design-background) → [Senior Engineer Path](/microservices/12-learning-paths/senior-engineer-path/) |
| **Interview in 2 weeks** | [Interview Revision Path](/microservices/12-learning-paths/interview-revision-path/) + [Top 300](/microservices/11-interview-guide/top-300-microservices-questions/) |
| **Monolith migration** | Module 9 → [Failure Scenarios](/microservices/10-production-playbook/failure-scenarios/) |
| **On-call / incidents** | [Resilience](/microservices/05-resilience-patterns/resilience-patterns/) + [Observability](/microservices/08-observability/observability/) + [Troubleshooting Questions](/microservices/11-interview-guide/troubleshooting-questions/) |
| **Tech lead / architect** | [Lead Engineer Path](/microservices/12-learning-paths/lead-engineer-path/) → [Architect Path](/microservices/12-learning-paths/architect-path/) |

---

## Cross-handbook references

Deep dives live in sibling handbooks — this playbook links out instead of duplicating engine internals:

- [System Design](/system-design/) — case studies, capacity, NFRs
- [Kafka Handbook](/kafka-handbook/) — broker tuning, partitions
- [Kubernetes Handbook](/kubernetes-handbook/) — probes, HPA, RBAC
- [Database Handbook](/database-handbook/) — outbox relay schema
- [Design Patterns](/design-patterns/) — SOLID, GoF for service code structure
- [Technology Playbook](/technology-playbook/) — ADR templates and technology selection

---

## Reading tips

1. **Read one module at a time** — do not jump randomly; data patterns (Module 3) need communication context (Module 2).
2. **Skim diagrams first** — each topic page opens with architecture mermaid; read prose after the picture makes sense.
3. **Use System Design as prerequisite** — if CAP or load balancing is fuzzy, read [CAP & PACELC](/system-design/cap-and-pacelc/) and [Load Balancers](/system-design/load-balancers-and-routing-algorithms/) first.
4. **Interview pages are questions-only** — pair with topic pages for answers; do not start from interview guides alone.
