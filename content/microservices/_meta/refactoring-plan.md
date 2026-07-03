---
title: "Microservices Architecture Playbook — Refactoring Plan"
date: 2026-07-03T15:00:00+00:00
draft: true
description: "Phase A inventory — quality, duplication, gaps, and recommended actions."
tags: ["microservices", "meta", "planning"]
---

# Phase A — Repository Inventory

**Scope:** `content/microservices/` (32 markdown files)  
**Audience:** Senior Engineers, Technical Leads, Architects (6+ years)  
**Status:** Planning only — **no content rewritten in Phase A**

**Target title:** Microservices Architecture Playbook  
**Target structure:** 12 numbered modules (`01-architecture-styles` … `12-learning-paths`) + `_meta/`

---

## Executive Summary

| Metric | Assessment |
| :--- | :--- |
| **Structure** | **Flat** — 30 topics in 6 modules via `data/microservices_modules.yaml`; no numbered folders |
| **Template compliance** | **Split** — 1/30 pages (`circuit-breaker-pattern.md`) use Playbook v2 (11 numbered sections + code tabs); 29/30 use legacy `### Core Microservices Pattern` skeleton (~6 sections) |
| **Average page depth** | ~120 lines — solid interview framing; **thin** on Security, Observability instrumentation, and production runbooks |
| **Duplication** | **High** — outbox/CDC/idempotent consumer in 5+ files; sidecar/mesh overlap; CAP/PACELC combined; gateway/BFF combined; tracing/logging combined |
| **Canonical discipline** | **None** — no concept registry enforced; outbox defers to `database-handbook` while user spec assigns ownership here |
| **Interview Layer 1** | **Missing** — no `11-interview-guide/`; per-page "Interview Failure Modes" ≠ question bank |
| **Learning paths** | **Missing** — inline table on `_index.md` only |
| **Cross-handbook overlap** | Docker/K8s duplicates [Kubernetes Handbook](/kubernetes-handbook/); broker queue depth duplicates [Kafka Handbook](/kafka-handbook/); polyglot DB matrix duplicates [Technology Playbook](/technology-playbook/how-to-choose-database/) |
| **Missing architect topics** | SOA, standalone fallback, deployment strategies, reliability engineering, scalability patterns, messaging patterns, event streaming (split), kubernetes patterns (architect lens), metrics/logging (split), top-200 questions |
| **Build scripts** | None — hand migration safe |

**Recommended Phase B focus:** Restructure into 12 modules, enforce concept registry, split 8 combined pages, migrate all pages to architect template, create 22 missing canonical pages, add interview + learning paths, set Hugo aliases — **not** broker/DB/cache selection deep dives.

---

## Scoring Guide

| Dimension | 1 | 10 |
| :--- | :--- | :--- |
| **Quality** | Inaccurate or trivial | Accurate, production-grade, maintainable |
| **Duplication** | Unique (1) | Heavily repeated elsewhere (10) |
| **Interview Value** | Not useful in senior interviews | High architect-panel value |

**Quality subscores:** Architecture Depth · Production Relevance · Scalability · Reliability · Interview Usefulness · Maintainability (composite 1–10).

---

## Dimension Averages (Current Corpus)

| Dimension | Score | Notes |
| :---: | :---: | :--- |
| Architecture Depth | 6.5 | Strong trade-off tables; weak on security/observability sections |
| Production Relevance | 6.0 | Failure modes present; few runbooks or SLO examples |
| Scalability Coverage | 5.5 | Sharding/replication exist; no holistic scalability-patterns page |
| Reliability Coverage | 6.5 | Resilience cluster solid; no reliability-engineering hub |
| Interview Usefulness | 7.5 | "Junior vs Senior" blocks excellent; no centralized Q bank |
| Maintainability | 4.5 | Two templates, combined concepts, no registry |

---

## File Inventory

| File | Category | Quality | Duplication | Interview Value | Problems | Action |
| :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| `_index.md` | Landing | 7 | 3 | 6 | Tutorial tone ("What is microservices?"); 6-module map; no learning paths or registry link | **Rewrite** — architect playbook positioning; 12-module map; link `_meta/` + learning paths |
| `code-tabs-example.md` | Internal meta | 5 | 1 | 1 | Not in yaml; dev reference only | **Move** → `_meta/code-tabs-example.md` or delete after template migration |
| `event-driven-architecture-log-streaming.md` | Event-driven | 7 | 8 | 8 | Deep outbox/CDC/idempotency duplicates saga, comm-topologies, DB-per-service; broker internals overlap Kafka HB | **Split** → `06-event-driven/event-driven-architecture.md` + `event-streaming.md`; trim outbox/CDC to ≤2 sentences + links |
| `point-to-point-message-queues.md` | Event-driven | 6 | 7 | 6 | RabbitMQ/AMQP depth belongs in Kafka HB comparisons; overlaps EDA pub/sub table | **Merge** into `06-event-driven/messaging-patterns.md`; link [Kafka messaging models](/kafka-handbook/01-fundamentals/messaging-models/) |
| `saga-pattern-distributed-transactions.md` | Data | 7 | 5 | 9 | Choreography/orchestration good; outbox mention duplicates | **Move** → `03-data-management/saga.md`; link canonical outbox |
| `cqrs-event-sourcing.md` | Data | 7 | 6 | 9 | Combined CQRS+ES; projection lag duplicated in EDA | **Split** → `03-data-management/cqrs.md` + `event-sourcing.md` |
| `microservices-communication-topologies.md` | Communication | 7 | 7 | 8 | Sync/async + outbox diagram duplicates EDA + gateway | **Move** → `02-service-communication/communication-topologies.md`; strip outbox deep dive |
| `api-gateway-bff-pattern.md` | Communication | 7 | 6 | 8 | Gateway+BFF combined; fan-out latency duplicated in comm-topologies | **Split** → `02-service-communication/api-gateway.md` + `bff.md` |
| `dynamic-service-discovery-registry.md` | Communication | 7 | 4 | 8 | K8s DNS section overlaps K8s HB | **Move** → `02-service-communication/service-discovery.md`; link [K8s Services](/kubernetes-handbook/services/) |
| `circuit-breaker-pattern.md` | Resilience | 8 | 4 | 9 | **Only Playbook v2 page**; fallback content should be canonical elsewhere | **Move** → `05-resilience-patterns/circuit-breaker.md`; migrate template to others from this |
| `transient-fault-handling-timeouts-retries.md` | Resilience | 7 | 5 | 8 | Retry+timeout combined; fallback mentioned not canonical | **Split** → `05-resilience-patterns/retry.md` + `timeout.md`; extract fallback to new page |
| `bulkhead-isolation-pattern.md` | Resilience | 7 | 5 | 8 | Overlaps circuit-breaker stack diagram | **Move** → `05-resilience-patterns/bulkhead.md` |
| `database-per-microservice.md` | Data | 7 | 6 | 8 | Polyglot selection matrix = Technology Playbook territory | **Move** → `03-data-management/database-per-service.md`; replace matrix with link |
| `monolithic-database-decomposition.md` | Migration | 7 | 5 | 9 | CDC phases overlap `database-decomposition` target | **Move** → `09-migration-modernization/database-decomposition.md` |
| `database-replication-scaling.md` | Data / Prod | 6 | 8 | 6 | Primary-replica mechanics = PostgreSQL/MongoDB handbooks | **Trim** → reference only; relocate scalability angle to `10-production-playbook/scalability-patterns.md` |
| `database-sharding-horizontal-partitioning.md` | Data / Prod | 6 | 7 | 7 | Consistent hashing section duplicates dedicated page | **Trim** → link `04-distributed-systems/consistent-hashing.md`; shard ops → scalability-patterns |
| `database-isolation-levels-concurrency-control.md` | Distributed systems | 7 | 4 | 8 | Correct MVCC content; fits concurrency-control | **Move** → `04-distributed-systems/concurrency-control.md` |
| `application-containerization-docker.md` | Platform | 6 | 9 | 4 | Full Docker tutorial = [Kubernetes Handbook](/kubernetes-handbook/docker/) | **Deprecate** — replace with link hub in `07-platform-patterns/kubernetes-patterns.md` |
| `declarative-container-orchestration-kubernetes.md` | Platform | 6 | 9 | 5 | K8s primitives = K8s HB; keep only microservices-on-K8s patterns | **Replace** → `07-platform-patterns/kubernetes-patterns.md` (architect lens) |
| `externalized-configuration-management.md` | Platform | 6 | 5 | 6 | Vault/GitOps useful; not in target structure | **Relocate** → appendix in `kubernetes-patterns.md` or `10-production-playbook/` sidebar note |
| `zero-downtime-deployment-topologies.md` | Migration / Prod | 7 | 4 | 8 | Blue-green/canary good; belongs under deployment strategies | **Merge** → `09-migration-modernization/zero-downtime-deployments.md` + `10-production-playbook/deployment-strategies.md` |
| `strangler-fig-application-pattern.md` | Migration | 8 | 3 | 9 | Strong migration content | **Move** → `09-migration-modernization/strangler-pattern.md` |
| `distributed-tracing-log-aggregation.md` | Observability | 7 | 7 | 8 | Tracing+logging combined; sampling duplicated in three-pillars | **Split** → `08-observability/distributed-tracing.md` + `logging.md` |
| `three-pillars-observability.md` | Observability | 7 | 5 | 8 | RED/USE good; overlaps tracing page | **Move** → `08-observability/three-pillars-observability.md`; link metrics/tracing/logging |
| `sidecar-integration-pattern.md` | Platform | 7 | 7 | 7 | Heavy overlap with service-mesh page | **Move** → `07-platform-patterns/sidecar.md`; mesh page links here |
| `service-mesh-architecture.md` | Platform | 7 | 6 | 8 | Ambient mesh good; control plane depth thin | **Move** → `07-platform-patterns/service-mesh.md`; link [Istio](/kubernetes-handbook/istio/) |
| `distributed-rate-limiting-throttling.md` | Production | 6 | 6 | 7 | Redis Lua detail = Redis HB; gateway rate limit overlaps API gateway | **Trim** → `10-production-playbook/scalability-patterns.md` §ingress; link Redis HB |
| `distributed-caching-invalidation.md` | Production | 6 | 7 | 6 | Cache-aside/CDC = system-design + Redis HB | **Replace** → `10-production-playbook/caching-patterns.md` (architect patterns only) |
| `consistent-hashing-rings-virtual-nodes.md` | Distributed systems | 7 | 5 | 8 | Sloppy quorum niche but valuable | **Move** → `04-distributed-systems/consistent-hashing.md` |
| `consumer-driven-contract-testing-cdct.md` | Quality gate | 6 | 3 | 7 | Valuable but not in target 12-module tree | **Keep** as `10-production-playbook/` appendix or `_meta` cross-link; not canonical architect pattern |
| `cap-theorem-pacelc-framework.md` | Distributed systems | 7 | 6 | 9 | CAP+PACELC combined; CRDT section duplicates system-design | **Split** → `04-distributed-systems/cap-theorem.md` + `pacelc.md` |
| `architectural-pragmatist-monolith-vs-microservices.md` | Architecture styles | 8 | 5 | 9 | Comparison only; missing SOA, standalone monolith/modular pages | **Split** → `01-architecture-styles/monolith.md`, `modular-monolith.md`, `microservices.md`; comparison content preserved on `microservices.md` |

---

## Missing Canonical Pages (Phase B Create)

| Target page | Priority | Source / Notes |
| :--- | :---: | :--- |
| `01-architecture-styles/soa.md` | P0 | Net-new; distinguish from microservices |
| `03-data-management/outbox.md` | P0 | Extract from EDA; **architect canonical**; link [DB handbook relay](/database-handbook/transactional-outbox-pattern/) for schema |
| `03-data-management/cdc.md` | P0 | Extract from EDA + monolithic-db-decomposition |
| `05-resilience-patterns/fallback.md` | P0 | Extract from circuit-breaker + gateway partial-response |
| `06-event-driven/messaging-patterns.md` | P0 | Merge point-to-point + EDA pub/sub table |
| `06-event-driven/event-streaming.md` | P0 | Architect streaming patterns; link Kafka HB |
| `07-platform-patterns/kubernetes-patterns.md` | P0 | Replace docker+k8s pages; K8s HB for primitives |
| `08-observability/metrics.md` | P1 | Extract from three-pillars |
| `09-migration-modernization/monolith-decomposition.md` | P1 | Team/domain decomposition; complement strangler |
| `10-production-playbook/scalability-patterns.md` | P0 | Holistic scale: horizontal, sharding, caching, rate limit |
| `10-production-playbook/caching-patterns.md` | P1 | Pattern-level only; link Redis HB |
| `10-production-playbook/deployment-strategies.md` | P0 | Blue-green, canary, rolling; merge zero-downtime |
| `10-production-playbook/reliability-engineering.md` | P0 | SLOs, error budgets, chaos, incident patterns |
| `11-interview-guide/top-200-microservices-questions.md` | P0 | Exactly 200 questions; no answers |
| `11-interview-guide/architect-questions.md` | P0 | Subset of top-200 |
| `11-interview-guide/troubleshooting-questions.md` | P0 | Min 25 |
| `11-interview-guide/scalability-questions.md` | P0 | Min 30 |
| `12-learning-paths/senior-engineer-path.md` | P1 | Net-new |
| `12-learning-paths/lead-engineer-path.md` | P1 | Net-new |
| `12-learning-paths/architect-path.md` | P1 | Net-new |
| `12-learning-paths/interview-revision-path.md` | P1 | Net-new |
| 12 × `_index.md` section landings | P1 | Module overviews |

---

## Duplicate Content (Semantic Overlap > 60%)

| Concept cluster | Appears in | Canonical target (Phase B) |
| :--- | :--- | :--- |
| Transactional outbox | `event-driven-architecture-log-streaming`, `microservices-communication-topologies`, `saga-pattern`, `database-per-microservice`, `_index` | `03-data-management/outbox.md` |
| CDC / Debezium relay | `event-driven-architecture-log-streaming`, `monolithic-database-decomposition`, `distributed-caching-invalidation`, `cqrs-event-sourcing` | `03-data-management/cdc.md` |
| Idempotent consumer | `event-driven-architecture-log-streaming`, `point-to-point-message-queues`, `saga-pattern` | `06-event-driven/messaging-patterns.md` |
| Sidecar vs service mesh | `sidecar-integration-pattern`, `service-mesh-architecture`, `declarative-container-orchestration-kubernetes` | `07-platform-patterns/sidecar.md` + `service-mesh.md` |
| CAP vs PACELC | `cap-theorem-pacelc-framework` (combined) | `04-distributed-systems/cap-theorem.md` + `pacelc.md` |
| API Gateway vs BFF | `api-gateway-bff-pattern` (combined) | `02-service-communication/api-gateway.md` + `bff.md` |
| Tracing vs logging vs metrics | `distributed-tracing-log-aggregation`, `three-pillars-observability` | `08-observability/*` (4 pages) |
| Retry vs timeout vs fallback | `transient-fault-handling-timeouts-retries`, `circuit-breaker-pattern` | `05-resilience-patterns/retry.md`, `timeout.md`, `fallback.md` |
| Consistent hashing | `consistent-hashing-rings-virtual-nodes`, `database-sharding-horizontal-partitioning` | `04-distributed-systems/consistent-hashing.md` |
| Monolith vs microservices | `architectural-pragmatist-monolith-vs-microservices`, `_index` intro table | `01-architecture-styles/*` |
| Docker / K8s runtime | `application-containerization-docker`, `declarative-container-orchestration-kubernetes` | **External:** [Kubernetes Handbook](/kubernetes-handbook/); architect page = `kubernetes-patterns.md` |
| Message broker mechanics | `point-to-point-message-queues`, `event-driven-architecture-log-streaming` | **External:** [Kafka Handbook](/kafka-handbook/); architect = `messaging-patterns.md` |
| Polyglot persistence selection | `database-per-microservice` matrix | **External:** [How to Choose Database](/technology-playbook/how-to-choose-database/) |

---

## Weak Content (Score ≤ 5 on Any Subscore)

| File | Weak area | Remediation |
| :--- | :--- | :--- |
| `application-containerization-docker.md` | Wrong handbook; tutorial depth | Deprecate → link K8s HB |
| `declarative-container-orchestration-kubernetes.md` | Duplicates K8s HB cheat sheets | Replace with kubernetes-patterns (PodDisruptionBudget, HPA for services, mesh ingress) |
| `database-replication-scaling.md` | Generic replication; not microservices-specific | Trim to cross-reference; move scale narrative to scalability-patterns |
| `database-per-microservice.md` | Polyglot matrix = selection guide | Replace matrix with 2-sentence link |
| `code-tabs-example.md` | Non-content | Move to `_meta` |
| All legacy-template pages | Missing Security, Observability sections | Migrate to 14-section architect template in Phase B |

---

## Fragmented Concepts (Split Required)

| Current file | Split into |
| :--- | :--- |
| `cap-theorem-pacelc-framework.md` | `cap-theorem.md`, `pacelc.md` |
| `api-gateway-bff-pattern.md` | `api-gateway.md`, `bff.md` |
| `cqrs-event-sourcing.md` | `cqrs.md`, `event-sourcing.md` |
| `transient-fault-handling-timeouts-retries.md` | `retry.md`, `timeout.md` (+ `fallback.md` new) |
| `distributed-tracing-log-aggregation.md` | `distributed-tracing.md`, `logging.md` |
| `architectural-pragmatist-monolith-vs-microservices.md` | `monolith.md`, `modular-monolith.md`, `microservices.md` (+ `soa.md` new) |
| `event-driven-architecture-log-streaming.md` | `event-driven-architecture.md`, `event-streaming.md` |
| `point-to-point-message-queues.md` | Absorbed into `messaging-patterns.md` |

---

## Outdated / Risky Examples

| Location | Issue | Action |
| :--- | :--- | :--- |
| `database-per-microservice.md` | Neo4j "social networks" generic example | Replace with bounded-context example (orders/inventory) |
| `cap-theorem-pacelc-framework.md` | "MongoDB configured CP" oversimplified | Clarify per-operation read/write concern on split pages |
| `distributed-rate-limiting-throttling.md` | Redis as only backend | Link Redis HB; mention gateway-local token bucket |
| `event-driven-architecture-log-streaming.md` | Kafka-specific `min.insync.replicas` | Move to Kafka HB link; keep broker-agnostic EDA |
| Multiple pages | YouTube video links as primary reference | Keep as optional; add canonical text-first |

---

## Cross-Handbook Boundary (Do Not Duplicate)

| Topic | Owner handbook | Microservices playbook role |
| :--- | :--- | :--- |
| Kafka internals, consumer groups, acks | Kafka Handbook | Link from `event-streaming.md` |
| RabbitMQ / broker selection ADR | Kafka HB + Technology Playbook | Link from `messaging-patterns.md` |
| Redis caching implementation | Redis Handbook (if present) / system-design | Link from `caching-patterns.md` |
| PostgreSQL replication, isolation | PostgreSQL Cheatsheet / DB Handbook | Link from `concurrency-control.md` |
| Docker, K8s primitives | Kubernetes Handbook | Link from `kubernetes-patterns.md` |
| Outbox schema, relay tuning | Database Handbook | Link from `outbox.md` |
| Circuit breaker (design pattern) | Design Patterns HB | Link optional; microservices owns **production** circuit breaker |
| Saga (pattern catalog) | Design Patterns HB | Microservices owns **distributed transaction** saga |

---

## Interview Question Plan (Phase B — Not Written in Phase A)

| File | Target count | Min distribution |
| :--- | :---: | :--- |
| `top-200-microservices-questions.md` | 200 | Architecture 50 · Distributed Systems 40 · Scalability 30 · Reliability 30 · Troubleshooting 25 · Observability 25 |
| `architect-questions.md` | ~50 | Subset: tradeoffs, migration, CAP/PACELC, mesh |
| `troubleshooting-questions.md` | ~25 | Cascades, lag, split-brain, poison messages |
| `scalability-questions.md` | ~30 | Sharding, hot keys, fan-out, cache stampede |

**Model:** Layer 1 — questions only, no answers. Deep dives link to canonical pages.

---

## Phase B Execution Order (Recommended)

1. Create `_meta/` enforcement + `data/microservices_modules.yaml` v2 (12 modules)
2. Add Hugo aliases for all 30 existing slugs → new paths
3. Split combined pages (CAP/PACELC, gateway/BFF, CQRS/ES, retry/timeout)
4. Create missing P0 pages (outbox, cdc, fallback, scalability, reliability, interview)
5. Migrate template: use `circuit-breaker-pattern.md` as reference for 14-section skeleton
6. Strip duplication per concept registry
7. Deprecate docker/k8s tutorial pages → kubernetes-patterns + external links
8. Rewrite `_index.md` + 12 section `_index.md` files
9. Generate top-200 questions (distribution validated)
10. Add learning paths

---

## Success Criteria Checklist (Full Project)

| Criterion | Phase A | Phase B+ |
| :--- | :---: | :---: |
| One canonical source per concept | Registry drafted | Enforce |
| No duplicate explanations | Overlap mapped | Trim |
| Strong distributed systems coverage | Gaps identified | Split CAP/PACELC |
| Strong architect interview coverage | Plan only | Top 200 |
| Learning paths | Planned | Create |
| Mermaid plan | **Done** | Implement |
| Infographic plan | **Done** | Implement |
| GitHub Pages optimized | Nav plan drafted | Aliases + yaml |

---

**Phase A complete. Awaiting approval before content modification.**
