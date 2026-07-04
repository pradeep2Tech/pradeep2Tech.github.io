---
title: "Interview Revision Path"
date: 2026-07-03T15:00:00+00:00
draft: false
description: "2-week microservices interview cram — topic order, daily drills, and answer sources mapped to playbook pages."
tags: ["microservices", "architecture-playbook", "distributed-systems", "learning-path", "interview"]
categories: ["Microservices Architecture Playbook"]
shortTitle: "Interview Revision"
module: 12
moduleTitle: "Learning Paths"
sectionRef: "12.4"
weight: 1204
playbookVersion: 3
---

# Interview Revision Path

**Audience:** 6+ years — interview in **7–14 days**.

**Format:** Read topic page → answer 10 linked questions aloud → note gaps.

**Do not** start from interview questions alone — answers live in topic pages.

---

## Week 1 — Core patterns (read + drill)

| Day | Topic pages (read fully) | Questions (answer aloud) |
| :---: | :--- | :--- |
| 1 | [Architecture Styles](/microservices/01-architecture-styles/architecture-styles/) | [Architect Q1–8](/microservices/11-interview-guide/architect-questions/) |
| 2 | [API Gateway](/microservices/02-service-communication/api-gateway-and-bff/) + [Comm Topologies](/microservices/02-service-communication/communication-topologies/) | [Architect Q9–13](/microservices/11-interview-guide/architect-questions/) |
| 3 | [Database Per Service](/microservices/03-data-management/database-per-service/) + [Outbox](/microservices/03-data-management/outbox-and-cdc/) | [Architect Q14–18](/microservices/11-interview-guide/architect-questions/) |
| 4 | [Saga](/microservices/03-data-management/saga/) + [CQRS](/microservices/03-data-management/cqrs-and-event-sourcing/) | [Architect Q16–20](/microservices/11-interview-guide/architect-questions/) |
| 5 | [Resilience](/microservices/05-resilience-patterns/resilience-patterns/) + [CAP](/microservices/04-distributed-systems/cap-and-pacelc/) | [Reliability questions](/microservices/11-interview-guide/reliability-questions/) |
| 6 | [Event-Driven](/microservices/06-event-driven/event-driven-architecture/) | [Scalability questions](/microservices/11-interview-guide/scalability-questions/) |
| 7 | **Mock** | 45 min: "Design food delivery microservices" — use [System Design food delivery](/system-design/food-delivery/) for self-grade |

---

## Week 2 — Depth + scenarios

| Day | Activity |
| :---: | :--- |
| 8 | [Migration module](/microservices/09-migration-modernization/) — strangler + DB decomposition |
| 9 | [Production playbook](/microservices/10-production-playbook/) — deployment + failure scenarios |
| 10 | [Top 300](/microservices/11-interview-guide/top-300-microservices-questions/) rows 1–100 |
| 11 | [Troubleshooting questions](/microservices/11-interview-guide/troubleshooting-questions/) — all |
| 12 | [Observability questions](/microservices/11-interview-guide/observability-questions/) |
| 13 | **Mock** | Whiteboard: payment orchestration with saga + outbox |
| 14 | **Review** | Re-read weak pages only; 60-sec answers from each page's interview block |

---

## High-yield 60-second answers

Memorize the **interview block** at the bottom of these pages:

- [Saga](/microservices/03-data-management/saga/) — orchestration vs choreography
- [API Gateway & BFF](/microservices/02-service-communication/api-gateway-and-bff/)
- [Monolith Decomposition](/microservices/09-migration-modernization/monolith-decomposition/)
- [Resilience Patterns](/microservices/05-resilience-patterns/resilience-patterns/)

---

## If coming from System Design only

You likely already know capacity and components. Interviewers will probe **what changes with distribution**:

1. Consistency → saga / eventual
2. Deploy → independent services + schema compat
3. Debug → traces + correlation IDs
4. Org → Conway's Law and bounded contexts

Bridge: [System Design process](/system-design/system-design-process/) + [Microservices fast path](/microservices/#fast-path-6-years-system-design-background).
