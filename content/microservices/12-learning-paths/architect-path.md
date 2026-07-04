---
title: "Architect Path"
date: 2026-07-03T15:00:00+00:00
draft: false
description: "8-week architect curriculum — platform topology, migration at scale, governance, and cross-domain integration."
tags: ["microservices", "architecture-playbook", "distributed-systems", "learning-path"]
categories: ["Microservices Architecture Playbook"]
shortTitle: "Architect Path"
module: 12
moduleTitle: "Learning Paths"
sectionRef: "12.3"
weight: 1203
playbookVersion: 3
---

# Architect Path

**Audience:** Staff/principal architects and senior tech leads shaping **multi-team** platforms.

**Prerequisite:** [Lead Engineer Path](/microservices/12-learning-paths/lead-engineer-path/) + strong [System Design](/system-design/) case study fluency.

**Outcome:** Defend platform topology, reject bad decomposition proposals, and align org + technology.

---

## Phase 1 — Strategic fit (Weeks 1–2)

| Topic | Read | Architect decision |
| :--- | :--- | :--- |
| Style selection | [Architecture Styles](/microservices/01-architecture-styles/architecture-styles/) | Approve/reject microservices for new initiative |
| Org alignment | [Monolith Decomposition](/microservices/09-migration-modernization/monolith-decomposition/) | Conway's Law workshop with engineering managers |
| Integration style | [Communication Topologies](/microservices/02-service-communication/communication-topologies/) | Platform-wide sync vs async policy |
| Comparison | [Technology Playbook](/technology-playbook/module-architecture-patterns/) | ADR: monolith vs services for new domain |

**Exercise:** Write a **2-page architecture position** for one product line (stay monolith vs decompose).

---

## Phase 2 — Platform topology (Weeks 3–4)

| Topic | Read | Architect decision |
| :--- | :--- | :--- |
| Edge | [API Gateway & BFF](/microservices/02-service-communication/api-gateway-and-bff/) | Shared gateway vs per-product BFFs |
| Runtime | [Sidecar & Mesh](/microservices/07-platform-patterns/sidecar-and-service-mesh/) | Mesh yes/no — justify operational tax |
| K8s | [Kubernetes Patterns](/microservices/07-platform-patterns/kubernetes-patterns/) | Baseline chart / golden path for teams |
| Data platform | [DB per service](/microservices/03-data-management/database-per-service/) + [Saga](/microservices/03-data-management/saga/) | Cross-domain transaction policy |

**Exercise:** Draw **platform reference architecture** (ingress → mesh → services → data).

---

## Phase 3 — Migration at scale (Weeks 5–6)

| Topic | Read | Architect decision |
| :--- | :--- | :--- |
| Strangler | [Strangler](/microservices/09-migration-modernization/strangler-pattern/) | Multi-year migration roadmap |
| Data | [Database Decomposition](/microservices/09-migration-modernization/database-decomposition/) | CDC tooling and cutover governance |
| Zero downtime | [Zero-Downtime Deployments](/microservices/09-migration-modernization/zero-downtime-deployments/) | Expand-contract enforcement |
| Risk | [Failure Scenarios](/microservices/10-production-playbook/failure-scenarios/) | Top 10 platform risks register |

**Exercise:** Phase plan for **one bounded context** with rollback at every step.

---

## Phase 4 — Governance (Weeks 7–8)

| Topic | Read | Architect decision |
| :--- | :--- | :--- |
| ADRs | [Architecture Decision Records](/microservices/10-production-playbook/architecture-decision-records/) | ADR template + review forum |
| Reviews | [Architecture Review Checklist](/microservices/10-production-playbook/architecture-review-checklist/) | Gate for new services |
| Reliability | [Reliability Engineering](/microservices/10-production-playbook/reliability-engineering/) | SLO/error budget policy |
| Interview depth | [Architect Questions](/microservices/11-interview-guide/architect-questions/) | Self-test all scenario prompts |

**Capstone:** 60-minute board presentation: "Microservices strategy for [your domain]" — include **when not to** decompose.

---

## Cross-curriculum

- [System Design](/system-design/) — capacity and case studies for board-level narrative
- [Design Patterns](/design-patterns/) — code-level structure inside services
- [Kafka](/kafka-handbook/) / [Postgres](/postgresql-cheatsheet/) — technology depth behind ADRs
