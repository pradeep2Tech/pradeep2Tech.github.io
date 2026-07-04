---
title: "Lead Engineer Path"
date: 2026-07-03T15:00:00+00:00
draft: false
description: "6-week path for tech leads — team boundaries, migration, production governance, and architecture reviews."
tags: ["microservices", "architecture-playbook", "distributed-systems", "learning-path"]
categories: ["Microservices Architecture Playbook"]
shortTitle: "Lead Engineer Path"
module: 12
moduleTitle: "Learning Paths"
sectionRef: "12.2"
weight: 1202
playbookVersion: 3
---

# Lead Engineer Path

**Audience:** Tech leads (8–12 years) owning a **squad or platform** running microservices.

**Prerequisite:** Complete [Senior Engineer Path](/microservices/12-learning-paths/senior-engineer-path/) or equivalent on-the-job experience.

**Outcome:** Run migrations, govern APIs, lead incident response, and write ADRs your team actually follows.

---

## Weeks 1–2 — Team and boundaries

| Focus | Pages | Lead action |
| :--- | :--- | :--- |
| Conway's Law | [Architecture Styles](/microservices/01-architecture-styles/architecture-styles/) | Map squads → services; identify coupling |
| API contracts | [Gateway](/microservices/02-service-communication/api-gateway-and-bff/) + [Discovery](/microservices/02-service-communication/service-discovery/) | Define versioning and deprecation policy |
| Data ownership | [DB per service](/microservices/03-data-management/database-per-service/) | Ban cross-schema access in code review |
| Distributed monolith smell | [Monolith Decomposition](/microservices/09-migration-modernization/monolith-decomposition/) | Audit: shared DB? shared library entities? |

**Deliverable:** One-page **service ownership map** with public APIs per bounded context.

---

## Weeks 3–4 — Reliability and events

| Focus | Pages | Lead action |
| :--- | :--- | :--- |
| Resilience standards | [Resilience](/microservices/05-resilience-patterns/resilience-patterns/) | Mandate timeout/breaker on all outbound clients |
| Event standards | [Event-Driven](/microservices/06-event-driven/) + [Outbox](/microservices/03-data-management/outbox-and-cdc/) | Pick outbox vs CDC for new services |
| Observability | [Observability](/microservices/08-observability/observability/) | Require `trace_id` in PR checklist |
| On-call | [Failure Scenarios](/microservices/10-production-playbook/failure-scenarios/) | Run one game day per month |

**Deliverable:** Squad **resilience checklist** (timeouts, idempotency, dashboards).

---

## Weeks 5–6 — Migration and governance

| Focus | Pages | Lead action |
| :--- | :--- | :--- |
| Strangler | [Strangler Pattern](/microservices/09-migration-modernization/strangler-pattern/) | Pick first extraction candidate |
| DB split | [Database Decomposition](/microservices/09-migration-modernization/database-decomposition/) | Plan CDC cutover with lag gates |
| Releases | [Deployment Strategies](/microservices/10-production-playbook/deployment-strategies/) | Expand-contract for next schema change |
| ADRs | [Architecture Decision Records](/microservices/10-production-playbook/architecture-decision-records/) | Write ADR for one contentious choice |
| Review | [Architecture Review Checklist](/microservices/10-production-playbook/architecture-review-checklist/) | Facilitate one cross-team review |

**Deliverable:** **Migration phase plan** (logical schema → CDC → read flip → write flip).

---

## Next step

[Architect Path](/microservices/12-learning-paths/architect-path/) for multi-team platform decisions.
