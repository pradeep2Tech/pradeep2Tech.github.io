---
title: "System Design Phase 2 — Architect Curriculum Gap Analysis"
date: 2026-07-03T22:00:00+00:00
draft: true
description: "Missing architect-level topics, suggested module locations, and P0/P1/P2 priorities. Planning only — no content created."
tags: ["system-design", "meta", "planning", "gap-analysis"]
---

# Phase 2 — Gap Analysis (Planning Only)

**Status:** Complete  
**Scope:** Identify missing architect-level topics for the System Design curriculum  
**Constraints:** No content created, no file moves, no URL changes, Microservices remains independent

**Inputs:** 66 existing SD pages (Phase 1 module map), Microservices playbook (38 topics), Technology Playbook (47 pages), case-study embedded concept scan.

---

## Executive Summary

| Metric | Value |
| :--- | :---: |
| SD topic pages today | 66 |
| SD dedicated fundamentals | 19 |
| SD case studies | 27 |
| SD interview companions | 19 |
| **Empty modules** | 1 (Architecture Styles) |
| **P0 gaps** (no SD overview; blocks learning path) | **14** |
| **P1 gaps** (partial / embedded only; interview-critical) | **18** |
| **P2 gaps** (deep dive owned elsewhere; SD stub or link sufficient) | **12** |

**Core finding:** System Design is **case-study rich** but **fundamentals thin**. Architects can learn *how to design Twitter*, but there is no structured on-ramp for *how to think about system design*, *NFRs*, *CAP/PACELC*, *consistency models*, *resilience*, *architecture styles*, or *observability pillars* without diving into a 3,000-line case study or leaving SD for Microservices.

**Recommended content strategy (aligned with Phase 4 intent):**

| Handbook | Role |
| :--- | :--- |
| **System Design** | Overview + interview lens (2–4 pages per concept, trade-off tables, links outward) |
| **Microservices** | Deep implementation patterns (16-section architect playbook) |
| **Technology Playbook** | Selection ADRs (“which broker / cache / protocol”) |

Phase 2 does **not** author pages — it prioritizes what to add and where.

---

## Methodology

1. **Module audit** — Each Phase 1 module scored against a reference architect curriculum (FAANG interview rubric + production architecture fundamentals).
2. **Coverage classification:**

   | Class | Meaning |
   | :--- | :--- |
   | **Dedicated** | Standalone SD fundamentals page exists |
   | **Embedded** | Discussed inside case studies only (no fundamentals entry point) |
   | **External** | Canonical page lives in Microservices or Technology Playbook |
   | **Missing** | No dedicated SD page; not adequately embedded |

3. **Priority rubric:**

   | Priority | Criteria |
   | :--- | :--- |
   | **P0** | Empty module slot, top-10 interview frequency, or prerequisite for reading case studies |
   | **P1** | Embedded in ≥3 case studies but no overview; architects ask this in every loop |
   | **P2** | Specialist depth; SD one-paragraph + cross-link is enough |

---

## Current Coverage by Module

| Module | Pages | Strength | Gap |
| :--- | :---: | :--- | :--- |
| **1 Foundations** | 4 | Strong networking/transport stack | No SD process, NFRs, or capacity math |
| **2 Distributed Systems** | 2 | CRDTs, ACID/isolation | No CAP, PACELC, consistency models, consensus, distributed transactions overview |
| **3 Data Management** | 3 | Storage internals, sharding, CDC | No CQRS, saga, outbox, event sourcing overviews |
| **4 Communication** | 4 | Proxies, ingress, REST/gRPC, LB algorithms | No API gateway, service discovery, backpressure, idempotency overview |
| **5 Scalability** | 4 | Caching depth, read replicas | No horizontal vs vertical scaling, latency vs throughput primer |
| **6 Reliability** | 2 | SPOF, multi-region | No availability primer, resilience patterns, SLO/error budgets |
| **7 Observability** | 1 | Logging *case study* | No metrics/logs/traces pillars page (only MS canonical) |
| **8 Architecture Styles** | **0** | — | **Entire module empty** |
| **9 Case Studies** | 27 | Excellent breadth | Patterns buried; no learning path |
| **10 Interview Guide** | 19 | Per-case-study Q&A | No cross-cutting SD interview framework |

---

## Gap Register — Missing Topics

Suggested locations use **Phase 1 module IDs** (flat slug TBD at content time).  
**Elsewhere** = where canonical deep dive exists today.

### P0 — Must-have for architect learning path

| # | Topic | SD Status | Suggested Module | Suggested Slug (future) | Elsewhere | Rationale |
| :---: | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | **What is System Design** (scope, constraints, deliverables) | Missing | 1 Foundations | `what-is-system-design` | — | No on-ramp; `_index.md` is 9 lines |
| 2 | **System Design Process** (requirements → HLD → deep dive → trade-offs) | Missing | 1 Foundations | `system-design-process` | — | No interview framework page |
| 3 | **Non-Functional Requirements (NFRs)** | Missing | 1 Foundations | `non-functional-requirements` | MS `architecture-review-checklist` (partial) | Every case study assumes NFR literacy |
| 4 | **Capacity Estimation & Back-of-Envelope** | Missing | 1 Foundations | `capacity-estimation` | Embedded in case studies | No standalone primer |
| 5 | **CAP Theorem** | External | 2 Distributed Systems | `cap-theorem` | MS `cap-and-pacelc` | CRDT page references CAP but no CAP overview in SD |
| 6 | **PACELC** | External | 2 Distributed Systems | `pacelc-framework` | MS `cap-and-pacelc` | Same MS page; SD needs interview-level summary |
| 7 | **Consistency Models** (strong, eventual, causal, read-your-writes) | Embedded | 2 Distributed Systems | `consistency-models` | MS `cap-and-pacelc`, case studies | Scattered across 15+ case studies |
| 8 | **Consistent Hashing** | Embedded | 2 Distributed Systems | `consistent-hashing` | MS `consistent-hashing`; SD case studies | No SD fundamentals entry; LB page mentions only |
| 9 | **Architecture Styles Overview** (monolith, modular monolith, μservices, SOA, event-driven) | External | 8 Architecture Styles | `architecture-styles-overview` | MS `architecture-styles`; TP `monolith-architecture`, `microservices-architecture`, `soa-architecture` | **Module 8 is empty** |
| 10 | **Availability** (definition, nines, uptime math) | Embedded | 6 Reliability | `availability-and-nines` | Case study SLO tables | No definitions page |
| 11 | **Resilience Patterns Overview** (circuit breaker, retry, timeout, bulkhead, fallback) | Embedded | 6 Reliability | `resilience-patterns-overview` | MS `resilience-patterns`; TP `circuit-breaker-pattern`, `bulkhead-pattern` | Embedded in payment-gateway, leaderboard, linkedin-job-search |
| 12 | **Observability Pillars** (metrics, logs, traces, RED/USE) | External | 7 Observability | `observability-fundamentals` | MS `observability` | Only logging *case study* in SD |
| 13 | **Horizontal vs Vertical Scaling** | Embedded | 5 Scalability | `horizontal-vs-vertical-scaling` | MS `scalability-patterns` | Mentioned in 10+ pages; no primer |
| 14 | **Latency vs Throughput** | Embedded | 5 Scalability | `latency-vs-throughput` | — | Critical trade-off; almost no dedicated treatment |

### P1 — Interview-critical; embedded today

| # | Topic | SD Status | Suggested Module | Suggested Slug (future) | Elsewhere | Rationale |
| :---: | :--- | :--- | :--- | :--- | :--- | :--- |
| 15 | **Reliability vs Availability** | Missing | 6 Reliability | `reliability-vs-availability` | MS `reliability-engineering` | Distinct concepts; often conflated in interviews |
| 16 | **SLI / SLO / SLA / Error Budgets** | Embedded | 6 Reliability | `slo-sli-sla-error-budgets` | MS `reliability-engineering` | Case studies cite SLOs without teaching them |
| 17 | **Distributed Transactions Overview** (2PC limits, saga vs outbox) | Embedded | 2 Distributed Systems | `distributed-transactions` | MS `saga`, `outbox-and-cdc`; TP `saga-pattern`, `outbox-pattern` | hotel-booking, stock-broker, email-delivery embed deep dives |
| 18 | **Backpressure & Flow Control** | Embedded | 4 Communication | `backpressure-and-flow-control` | `transport-layer-mechanics-tcp-vs-udp` (TCP window); case studies | No architect-level overview |
| 19 | **Idempotency & Exactly-Once Semantics** | Partial | 4 Communication | `idempotency-and-delivery-semantics` | REST page (brief); case studies | Payment, notification, email cases assume it |
| 20 | **CQRS Overview** | Embedded | 3 Data Management | `cqrs-overview` | MS `cqrs-and-event-sourcing`; TP `cqrs-pattern` | proximity-search, hotel-booking embed |
| 21 | **Event Sourcing Overview** | Embedded | 3 Data Management | `event-sourcing-overview` | MS `cqrs-and-event-sourcing` | stock-broker, payment-gateway |
| 22 | **Saga Pattern Overview** | Embedded | 3 Data Management | `saga-pattern-overview` | MS `saga`; TP `saga-pattern` | ecommerce, food-delivery references |
| 23 | **Transactional Outbox Overview** | Embedded | 3 Data Management | `transactional-outbox-overview` | MS `outbox-and-cdc`; TP `outbox-pattern` | email-delivery, notification-system |
| 24 | **Consensus & Leader Election** (Raft, Paxos, ZK/etcd) | Embedded | 2 Distributed Systems | `consensus-and-leader-election` | Case studies (MQ, KV store, scheduler) | Mentioned in SPOF, sharding, MQ case studies |
| 25 | **API Gateway & BFF** | External | 4 Communication | `api-gateway-and-bff-overview` | MS `api-gateway-and-bff`; TP `api-gateway`, `bff-pattern` | Ingress page covers L4/L7 but not gateway pattern |
| 26 | **Service Discovery** | External | 4 Communication | `service-discovery-overview` | MS `service-discovery` | Not in SD fundamentals |
| 27 | **Event-Driven Architecture Overview** | External | 8 Architecture Styles | `event-driven-architecture-overview` | MS `event-driven-architecture`; TP `event-driven-architecture` | No SD entry point |
| 28 | **Rate Limiting & Throttling** (algorithms) | Case study only | 5 Scalability | `rate-limiting-fundamentals` | MS `scalability-patterns`; SD `distributed-rate-limiter` case study | Case study is full design; no algorithm primer |
| 29 | **Disaster Recovery (RPO/RTO)** | Embedded | 6 Reliability | `disaster-recovery-rpo-rto` | MS `failure-scenarios` | multi-region page touches AZs not DR math |
| 30 | **System Design Interview Guide** (cross-cutting) | Missing | 10 Interview Guide | `system-design-interview-framework` | MS `top-300-microservices-questions` (different scope) | 19 case Q&A files; no general framework |
| 31 | **Architect Learning Paths** | Missing | 10 Interview Guide or new module | `learning-paths` (section) | MS `12-learning-paths/*` | SD has no senior → architect progression |
| 32 | **Architecture Decision Records (ADRs)** | External | 8 Architecture Styles | `architecture-decision-records` | MS `architecture-decision-records` | Architects need ADR literacy in SD curriculum |

### P2 — Link-out sufficient; optional SD stub

| # | Topic | SD Status | Suggested Module | Suggested Slug (future) | Elsewhere | Rationale |
| :---: | :--- | :--- | :--- | :--- | :--- | :--- |
| 33 | **Database-per-Service** | External | 3 Data Management | `database-per-service-overview` | MS `database-per-service` | Microservices-specific decomposition |
| 34 | **Service Mesh & Sidecar** | External | 4 Communication | `service-mesh-overview` | MS `sidecar-and-service-mesh`; TP `service-mesh` | Platform pattern; K8s HB depth |
| 35 | **Strangler Fig Pattern** | External | 8 Architecture Styles | `strangler-pattern-overview` | MS `strangler-pattern`; TP `strangler-pattern` | Migration pattern |
| 36 | **Monolith Decomposition** | External | 8 Architecture Styles | `monolith-decomposition-overview` | MS `monolith-decomposition` | Migration playbook |
| 37 | **Deployment Strategies** (blue/green, canary) | External | 6 Reliability | `deployment-strategies-overview` | MS `deployment-strategies` | Ops-heavy; MS canonical |
| 38 | **Zero-Downtime Deployments** | External | 6 Reliability | `zero-downtime-deployments-overview` | MS `zero-downtime-deployments` | Same |
| 39 | **Messaging & Streaming Patterns** | Case study + External | 4 Communication | `messaging-patterns-overview` | MS `messaging-and-streaming-patterns`; Kafka HB | MQ case study is full design |
| 40 | **Kubernetes Platform Patterns** | External | 8 Architecture Styles | `kubernetes-patterns-overview` | MS `kubernetes-patterns`; K8s HB | Specialist handbook owns depth |
| 41 | **Chaos Engineering & Failure Injection** | External | 6 Reliability | `chaos-engineering-overview` | MS `failure-scenarios`, `reliability-engineering` | Production/SRE topic |
| 42 | **Cost & FinOps in Architecture** | Embedded | 1 Foundations | `cost-aware-architecture` | Cloud HB (future) | Mentioned in some case studies |
| 43 | **Security in System Design** (threat modeling, zero trust) | Embedded | 1 Foundations | `security-in-system-design` | Security Architecture section | Case studies mention PCI/auth ad hoc |
| 44 | **Multi-Tenancy Patterns** | Embedded | 3 Data Management | `multi-tenancy-patterns` | online-learning-platform case study | Single case study coverage |

---

## Adequately Covered — No New Page Needed (Phase 2)

These topics have **dedicated SD fundamentals pages** sufficient for interview + production entry:

| Topic | SD Page | Module |
| :--- | :--- | :---: |
| Networking (IP, DNS, firewalls) | `networking-essentials-ip-dns-firewalls` | 1 |
| TCP vs UDP | `transport-layer-mechanics-tcp-vs-udp` | 1 |
| HTTP/3, QUIC, WebSockets | `http3-quic-and-websocket-transports` | 1 |
| Load balancing (hands-on) | `hands-on-load-balancing-setup` | 1 |
| CRDTs & multi-master merge | `crdts-and-multi-master-conflict-resolution` | 2 |
| ACID & isolation levels | `database-transactions-and-acid-isolation` | 2 |
| Relational storage / B-trees | `relational-database-fundamentals-and-b-trees` | 3 |
| CDC cache invalidation | `cdc-based-cache-invalidation` | 3 |
| Sharding & chunk routing | `database-sharding-provisioning-and-chunk-routing` | 3 |
| Forward vs reverse proxy | `proxy-servers-forward-vs-reverse` | 4 |
| L4/L7 ingress | `layer4-layer7-multi-tier-ingress-routing` | 4 |
| REST vs gRPC | `application-layer-protocols-rest-grpc` | 4 |
| Load balancer algorithms | `load-balancers-and-routing-algorithms` | 4 |
| Caching hierarchy & CDN | `caching-and-cdns-hierarchical-arrays` | 5 |
| Cache eviction policies | `cache-eviction-and-mutation-policies` | 5 |
| Cache stampede & bloom filters | `cache-stampede-and-penetration-mitigation` | 5 |
| Read replicas & replication lag | `replication-lag-read-replica-topology` | 5 |
| SPOF elimination & redundancy | `single-point-of-failure-elimination-redundancy` | 6 |
| Multi-region & availability zones | `multi-region-topologies-and-availability-zones` | 6 |
| Distributed logging (design) | `distributed-logging-system` | 7 |
| 27 end-to-end designs | Case study slugs | 9 |
| 19 case-study Q&A companions | `*-interview-questions` | 10 |

---

## Embedded-Only Concepts (Case Study Scatter Map)

High-frequency patterns **without** SD fundamentals — candidates for P1 overview pages:

| Concept | Case Studies Embedding It (sample) | Occurrences |
| :--- | :--- | :---: |
| Circuit breaker | `payment-gateway-orchestration`, `linkedin-job-search`, `leaderboard` | 8+ |
| CQRS | `proximity-search`, `hotel-booking`, `payment-gateway-orchestration` | 6+ |
| Outbox pattern | `email-delivery`, `notification-system`, `stock-broker-trading` | 5+ |
| Consistent hashing | `distributed-kv-store`, `distributed-lru-cache`, `chat-application`, `distributed-rate-limiter` | 10+ |
| Kafka / streaming | `leaderboard`, `sponsored-ads`, `social-feed`, `stock-broker-trading` | 12+ |
| SLO / latency targets | Nearly all case studies | 25+ |
| Idempotency keys | `payment-gateway-orchestration`, `ticket-booking`, `notification-system` | 8+ |

**Risk:** Readers learn patterns *in situ* but cannot compare trade-offs across designs without reading multiple 3,000-line posts.

---

## Module Fill Plan (Recommended Sequence)

When content creation is approved, add pages in this order to maximize learning-path coherence **without moving existing files**:

### Wave 1 — Unlock empty module + on-ramp (P0)

| Order | Module | New Pages |
| :---: | :---: | :--- |
| 1 | 1 Foundations | `what-is-system-design`, `system-design-process`, `non-functional-requirements`, `capacity-estimation` |
| 2 | 2 Distributed Systems | `cap-theorem`, `pacelc-framework`, `consistency-models`, `consistent-hashing` |
| 3 | 8 Architecture Styles | `architecture-styles-overview` |
| 4 | 5 Scalability | `horizontal-vs-vertical-scaling`, `latency-vs-throughput` |
| 5 | 6 Reliability | `availability-and-nines`, `resilience-patterns-overview` |
| 6 | 7 Observability | `observability-fundamentals` |

**Wave 1 total:** 14 pages (matches 14 P0 gaps).

### Wave 2 — Pattern overviews + interview (P1)

| Order | Module | New Pages |
| :---: | :---: | :--- |
| 7 | 3 Data Management | `cqrs-overview`, `event-sourcing-overview`, `saga-pattern-overview`, `transactional-outbox-overview` |
| 8 | 2 Distributed Systems | `distributed-transactions`, `consensus-and-leader-election` |
| 9 | 4 Communication | `backpressure-and-flow-control`, `idempotency-and-delivery-semantics`, `api-gateway-and-bff-overview`, `service-discovery-overview` |
| 10 | 6 Reliability | `reliability-vs-availability`, `slo-sli-sla-error-budgets`, `disaster-recovery-rpo-rto` |
| 11 | 5 Scalability | `rate-limiting-fundamentals` |
| 12 | 8 Architecture Styles | `event-driven-architecture-overview`, `architecture-decision-records` |
| 13 | 10 Interview Guide | `system-design-interview-framework` + learning path index |

**Wave 2 total:** 18 pages (P1 gaps).

### Wave 3 — Optional stubs (P2)

One-page overviews with **prominent cross-links** to Microservices / Technology Playbook — only if Phase 4 ownership model approves.

---

## Cross-Handbook Ownership Preview (for Phase 3/4)

Phase 2 identifies gaps; Phase 3 will map duplicates. Preview for planning:

| Concept | SD (future) | MS (keep deep) | TP (keep ADR) |
| :--- | :--- | :--- | :--- |
| CAP / PACELC | Interview summary | Full framework + examples | — |
| CQRS / Saga / Outbox | When-to-use + diagram | Implementation playbook | Selection matrix |
| Circuit breaker / bulkhead | Pattern catalog + failure modes | Resilience playbook | When to adopt ADR |
| Architecture styles | Comparison table | Decomposition triggers | Monolith vs μservices ADR |
| Observability | Three pillars + correlation | Production instrumentation | — |

**Do not copy MS bodies into SD.** SD pages should be ≤40% the length of MS counterparts.

---

## Suggested YAML Impact (Future — Not Executed)

When P0 pages are authored, append slugs to `data/system_design_modules.yaml` only — still **no file moves**:

```yaml
# Example future entries (illustrative)
- id: 1
  focus: "Foundations"
  topics:
    - what-is-system-design          # NEW
    - system-design-process            # NEW
    - non-functional-requirements      # NEW
    - capacity-estimation              # NEW
    - networking-essentials-ip-dns-firewalls
    # ... existing slugs unchanged
```

Prev/next order in `system_design_order.yaml` updated in same commit as new pages.

---

## What Phase 2 Does Not Recommend

| Action | Reason |
| :--- | :--- |
| Merge Microservices into System Design | User strategy: independent until Phase 4 approval |
| Move or rename existing SD files | Phase 1 constraint preserved |
| Create Hugo aliases | Explicitly excluded |
| Rewrite case studies to deduplicate | Phase 5 scope |
| Duplicate MS playbook content | Maintenance burden; link instead |

---

## Exit Criteria — Phase 2

| Criterion | Status |
| :--- | :---: |
| Missing topics identified | ✅ |
| Suggested module locations assigned | ✅ |
| P0 / P1 / P2 priorities assigned | ✅ |
| No content files created | ✅ |
| Microservices untouched | ✅ |

---

## Next Step

**Phase 3 (awaiting approval):** Concept registry — for every overlapping concept, document canonical owner, duplicate locations, and recommended cross-links across System Design, Microservices, and Technology Playbook.

**Do not proceed to Phase 3 without explicit approval.**
