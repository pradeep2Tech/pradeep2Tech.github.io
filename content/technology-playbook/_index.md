---
title: "Enterprise Technology Decision Playbook"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Architecture pattern ADRs and technology decision frameworks — when to choose monolith vs microservices, databases, brokers, workflow engines, and batch platforms."
tags: ["technology-playbook", "architecture", "decision-guide"]
ShowPageNums: true
---

Slim **technology choice guide** for staff engineers and architects — architecture pattern summaries, decision matrices, and workflow/batch platform selection. Product deep-dives live in domain handbooks ([Kafka](/kafka-handbook/), [Kubernetes](/kubernetes-handbook/), [Database](/database-handbook/), [Cloud](/cloud-handbook/)).

---

## How This Differs from Domain Handbooks

| Focus | Technology Decisions | Domain Handbooks |
| :--- | :--- | :--- |
| **Goal** | Which pattern or category to pick | How a specific product fits and operates |
| **Audience** | Architects writing ADRs | Platform engineers implementing |
| **Depth** | Decision criteria + interview answers | Product architecture + trade-offs |

---

## Curriculum Overview

| Module | Focus Area |
| :----: | :--- |
| **1** | [Architecture Patterns](/technology-playbook/module-architecture-patterns/) |
| **2** | [Technology Decision Matrix](/technology-playbook/module-technology-decision-matrix/) |
| **3** | [Workflow, Batch, Rules & Schedulers](/technology-playbook/module-workflow-batch-rules-schedulers/) |

---

## Cross-References

| Topic | Implementation deep dive |
| :--- | :--- |
| Event-Driven Architecture | [Microservices](/microservices/event-driven-architecture-log-streaming/) |
| CQRS & Event Sourcing | [Microservices](/microservices/cqrs-event-sourcing/) |
| Saga Pattern | [Microservices](/microservices/saga-pattern-distributed-transactions/) |
| Circuit Breaker | [Microservices](/microservices/circuit-breaker-pattern/) |
| Kafka selection | [Kafka Handbook](/kafka-handbook/02-kafka/kafka-core/) |
| Database internals | [Database Handbook](/database-handbook/) |
