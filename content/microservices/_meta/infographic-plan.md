---
title: "Microservices Architecture Playbook — Infographic Plan"
date: 2026-07-03T15:00:00+00:00
draft: true
description: "Visual asset backlog — revision sheets, decision trees, comparison one-pagers."
tags: ["microservices", "meta", "planning"]
---

# Infographic Plan

**Note:** This site is Markdown/Hugo-first. "Infographics" = **structured one-page visual tables**, Mermaid diagrams, ASCII decision flows, and optional future static images — not separate image assets unless generated later.

**Meta file:** `draft: true` — planning backlog only.

---

## Format Strategy

| Asset type | Implementation | Location |
| :--- | :--- | :--- |
| Architect decision tree | Mermaid `flowchart TD` | Canonical topic page §Design Decisions |
| Comparison one-pager | Markdown table (4–8 rows) | Comparison template pages (01, 02 gateway vs BFF) |
| Resilience cheat sheet | Single-page table | `05-resilience-patterns/` hub or revision path |
| Troubleshooting flowchart | Mermaid `flowchart TD` | `10-production-playbook/reliability-engineering.md` |
| Interview revision poster | Module checklist table | `12-learning-paths/interview-revision-path.md` |
| Tradeoff quadrant | Table or `quadrantChart` | Architecture styles, CAP/PACELC |
| Production failure matrix | Symptom → cause → fix table | Each canonical page §Common Failures |

---

## By Module

### 01 Architecture Styles

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Monolith vs modular vs microservices | 3-column comparison card | `microservices.md` | P0 |
| SOA vs microservices | ESB hub vs decentralized | `soa.md` | P1 |
| Decomposition checklist | When to split flowchart | `microservices.md` | P0 |
| Conway's Law | Org structure → architecture map | `microservices.md` | P2 |

### 02 Service Communication

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Gateway vs BFF responsibilities | Side-by-side table | `api-gateway.md` + `bff.md` | P0 |
| Sync vs async decision tree | Command/query fork | `communication-topologies.md` | P0 |
| Discovery modes | Client-side vs server-side vs K8s DNS | `service-discovery.md` | P1 |

### 03 Data Management

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Database per service | Data ownership boundaries | `database-per-service.md` | P0 |
| CQRS write/read split | Responsibility matrix | `cqrs.md` | P0 |
| Saga orchestration vs choreography | Comparison table | `saga.md` | P0 |
| Outbox vs dual-write | Anti-pattern vs pattern card | `outbox.md` | P0 |
| CDC pipeline | Source → relay → consumer | `cdc.md` | P0 |
| Event sourcing snapshot | Replay cost timeline | `event-sourcing.md` | P1 |

### 04 Distributed Systems

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| CAP during partition | CP vs AP behavior card | `cap-theorem.md` | P0 |
| PACELC normal operation | PC/EL vs PA/EL matrix | `pacelc.md` | P0 |
| Domain consistency map | Ledger=CP, Feed=AP | `pacelc.md` | P0 |
| Consistent hashing | Ring + vnode load balance | `consistent-hashing.md` | P1 |
| Isolation levels | Anomaly prevention table | `concurrency-control.md` | P1 |

### 05 Resilience Patterns

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Circuit breaker states | CLOSED/OPEN/HALF-OPEN card | `circuit-breaker.md` | — Exists |
| Resilience stack poster | Breaker + bulkhead + retry + timeout + fallback | `12-learning-paths/interview-revision-path.md` | P0 |
| Retry eligibility | Idempotent vs non-idempotent ops | `retry.md` | P1 |
| Fallback read vs write | Degrade policy matrix | `fallback.md` | P1 |

### 06 Event-Driven

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Pub/Sub vs log stream | 6-row comparison | `messaging-patterns.md` | — Exists |
| Delivery semantics | at-most / at-least / effectively-once | `messaging-patterns.md` | P0 |
| Consumer lag runbook | Symptom → scale → retention | `event-streaming.md` | P1 |
| EDA failure modes | Poison pill, dual-write, lag | `event-driven-architecture.md` | P1 |

### 07 Platform Patterns

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Sidecar use cases | Proxy, agent, adapter table | `sidecar.md` | P1 |
| Mesh vs no-mesh decision | When mesh earns its tax | `service-mesh.md` | P0 |
| K8s microservices primitives | Deploy/Service/Ingress/PDB/HPA | `kubernetes-patterns.md` | P0 |

### 08 Observability

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Three pillars | Metrics / logs / traces roles | `three-pillars-observability.md` | P0 |
| RED vs USE | Method selection guide | `metrics.md` | P1 |
| Trace-log correlation | `trace_id` injection contract | `logging.md` | P1 |
| Sampling strategies | Head vs tail tradeoff | `distributed-tracing.md` | P1 |

### 09 Migration & Modernization

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Strangler phases | Route % migration timeline | `strangler-pattern.md` | P0 |
| DB decomposition phases | 5-phase cutover table | `database-decomposition.md` | P0 |
| Expand-contract migration | 5-step schema evolution | `zero-downtime-deployments.md` | P1 |
| Monolith decomposition order | Bounded context priority | `monolith-decomposition.md` | P1 |

### 10 Production Playbook

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Scalability axes | Stateless / read scale / shard | `scalability-patterns.md` | P0 |
| Cache patterns | cache-aside, write-through, CDC evict | `caching-patterns.md` | P1 |
| Deployment strategy picker | Rolling vs blue-green vs canary | `deployment-strategies.md` | P0 |
| SLO / error budget | Release gate formula | `reliability-engineering.md` | P0 |
| Cascading failure triage | Flowchart: timeout → pool → breaker | `reliability-engineering.md` | P1 |

### 11 Interview Guide

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Top 200 topic index | Category × count table | `top-200-microservices-questions.md` | P0 |
| Question distribution | Architecture 50 / DS 40 / … | `top-200-microservices-questions.md` | P0 |
| Architect rapid-fire | 25-question checklist | `architect-questions.md` | P1 |

### 12 Learning Paths

| Topic | Infographic | Canonical page | Priority |
| :--- | :--- | :--- | :---: |
| Senior engineer path | 4-week module schedule | `senior-engineer-path.md` | P1 |
| Lead engineer path | Team/platform focus map | `lead-engineer-path.md` | P1 |
| Architect path | Full playbook traversal | `architect-path.md` | P0 |
| Interview revision | 2-week drill plan | `interview-revision-path.md` | P0 |

---

## Cross-Handbook Visual Boundaries

Do **not** create infographics for:

| Topic | Use instead |
| :--- | :--- |
| Kafka ISR / replication | Link Kafka HB diagrams |
| PostgreSQL WAL internals | Link PostgreSQL cheatsheet |
| Redis Lua rate limit script | Link system-design / Redis HB |
| Docker layer anatomy | Link Kubernetes HB |

Microservices infographics show **architect decisions and boundaries** only.

---

## Hugo Shortcode Opportunities

| Shortcode | Use case | Pages |
| :--- | :--- | :--- |
| `comparison-table` | Gateway vs BFF, orchestration vs choreography | 02, 03 |
| `code-tabs` | Resilience4j, gRPC deadline examples | 05 (circuit-breaker reference) |
| `note` / `warning` | Anti-patterns (dual-write, fake fallback on writes) | 03, 05, 06 |

---

## Revision Sheet (Single Page — Phase C)

Consolidate on `12-learning-paths/interview-revision-path.md`:

| Section | Rows |
| :--- | :---: |
| Architecture styles one-liners | 4 |
| Data patterns one-liners | 6 |
| Resilience stack | 5 |
| CAP/PACELC domain map | 2 |
| Migration patterns | 4 |
| Observability pillars | 3 |
| Top 20 failure modes | 20 |

---

## Priority Summary

| Phase | Deliverable |
| :--- | :--- |
| **B** | P0 infographics on all new canonical pages; migrate existing tables; resilience + CAP posters |
| **C** | P1 troubleshooting flowcharts, revision sheet, learning path schedules |
| **D** | Optional static PNG exports from Mermaid (if brand assets added) |

---

**Phase A complete. Asset creation deferred to Phase B/C.**
