---
title: "Senior Engineer Path"
date: 2026-07-03T15:00:00+00:00
draft: false
description: "4-week curriculum for senior engineers — communication, data, resilience, and production patterns with daily reading goals."
tags: ["microservices", "architecture-playbook", "distributed-systems", "learning-path"]
categories: ["Microservices Architecture Playbook"]
shortTitle: "Senior Engineer Path"
module: 12
moduleTitle: "Learning Paths"
sectionRef: "12.1"
weight: 1201
playbookVersion: 3
---

# Senior Engineer Path

**Audience:** 6–10 years experience — comfortable with system design interviews, new to **operating** microservices in production.

**Duration:** 4 weeks (~5 hours/week).

**Prerequisite:** Skim [System Design foundations](/system-design/what-is-system-design/) and complete the [playbook fast path](/microservices/#fast-path-6-years-system-design-background) if microservices terminology feels scattered.

**Exit criteria:** You can whiteboard sync/async boundaries, explain saga vs 2PC, and stack resilience patterns on one outbound dependency.

---

## Week 1 — Boundaries and ingress

**Theme:** Where the network starts and how traffic enters.

| Day | Read | Focus question |
| :---: | :--- | :--- |
| 1 | [Architecture Styles](/microservices/01-architecture-styles/architecture-styles/) | When would you *not* choose microservices? |
| 2 | [Communication Topologies](/microservices/02-service-communication/communication-topologies/) | Which flows must be sync vs async? |
| 3 | [API Gateway & BFF](/microservices/02-service-communication/api-gateway-and-bff/) | What belongs in gateway vs BFF vs domain service? |
| 4 | [Service Discovery](/microservices/02-service-communication/service-discovery/) | How do pods get stable names at runtime? |
| 5 | **Practice** | Draw ingress for a mobile checkout app (gateway → BFF → 3 services) |

**Checkpoint:** Explain fan-out latency and why JWT is validated once at the edge.

---

## Week 2 — Data ownership

**Theme:** No shared database; cross-service consistency.

| Day | Read | Focus question |
| :---: | :--- | :--- |
| 1 | [Database Per Service](/microservices/03-data-management/database-per-service/) | Why are cross-schema JOINs forbidden? |
| 2 | [Outbox & CDC](/microservices/03-data-management/outbox-and-cdc/) | Why is dual-write an anti-pattern? |
| 3 | [Saga Pattern](/microservices/03-data-management/saga/) | Orchestration vs choreography for your checkout flow |
| 4 | [CQRS & Event Sourcing](/microservices/03-data-management/cqrs-and-event-sourcing/) | When is CQRS worth the cost? |
| 5 | **Practice** | Design order → payment → inventory with compensations |

**Checkpoint:** Walk through a failed payment and list compensating steps in reverse order.

---

## Week 3 — Failure and events

**Theme:** Things break more often over the network.

| Day | Read | Focus question |
| :---: | :--- | :--- |
| 1 | [CAP & PACELC](/microservices/04-distributed-systems/cap-and-pacelc/) | CP vs AP for inventory vs analytics |
| 2 | [Resilience Patterns](/microservices/05-resilience-patterns/resilience-patterns/) | Order: timeout → bulkhead → breaker → retry |
| 3 | [Event-Driven Architecture](/microservices/06-event-driven/event-driven-architecture/) | Event notification vs event-carried state |
| 4 | [Messaging & Streaming](/microservices/06-event-driven/messaging-and-streaming-patterns/) | Queue vs log — when to use which |
| 5 | [Observability](/microservices/08-observability/observability/) | How `trace_id` propagates sync and async |

**Checkpoint:** Given a slow payment service, list three containment patterns before root-cause fix.

---

## Week 4 — Production reality

**Theme:** Deploy, migrate, and review.

| Day | Read | Focus question |
| :---: | :--- | :--- |
| 1 | [Deployment Strategies](/microservices/10-production-playbook/deployment-strategies/) | Blue-green vs canary vs rolling |
| 2 | [Scalability Patterns](/microservices/10-production-playbook/scalability-patterns/) | Shard vs replicate vs cache |
| 3 | [Failure Scenarios](/microservices/10-production-playbook/failure-scenarios/) | Top 5 on-call scenarios for your stack |
| 4 | [Top 300 — rows 1–50](/microservices/11-interview-guide/top-300-microservices-questions/) | Self-test without peeking at topic pages |
| 5 | **Capstone** | 45-min mock: design notifications service (sync API + async delivery) |

---

## After this path

- **Interview focus:** [Interview Revision Path](/microservices/12-learning-paths/interview-revision-path/)
- **Migration project:** [Monolith Decomposition](/microservices/09-migration-modernization/monolith-decomposition/) + Module 9
- **Leadership track:** [Lead Engineer Path](/microservices/12-learning-paths/lead-engineer-path/)
