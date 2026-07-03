---
title: "System Design Phase 3 — Cross-Handbook Concept Registry"
date: 2026-07-03T23:00:00+00:00
draft: true
description: "Canonical ownership, duplicate locations, and cross-link recommendations across System Design, Microservices, and Technology Playbook. Analysis only."
tags: ["system-design", "meta", "planning", "concept-registry", "deduplication"]
---

# Phase 3 — Concept Registry (Analysis Only)

**Status:** Complete  
**Scope:** Overlap analysis across **System Design**, **Microservices**, and **Technology Playbook**  
**Constraints:** No content moves · No aliases · No rewrites · Microservices remains independent

**Inputs:** [Phase 1 Navigation](phase-1-navigation.md) · [Phase 2 Gap Analysis](phase-2-gap-analysis.md) · [Phase 2A Expansion Plan](phase-2a-foundations-expansion.md) · [Migration Plan §3](system-design-migration-plan.md) · [MS Concept Registry](/microservices/_meta/concept-registry/)

---

## Executive Summary

| Metric | Value |
| :--- | :---: |
| **Concepts registered** | **52** |
| **High-severity duplicates** (≥3 locations, full sections) | **12 clusters** |
| **SD-unique concepts** (no MS/TP pattern overlap) | **11** |
| **Planned SD overview pages** (Phase 2A, not yet authored) | **13** |
| **Recommended cross-links** (net new, when P0 pages exist) | **~65 outbound** |

### Ownership model (approved strategy)

| Handbook | Role | Content depth |
| :--- | :--- | :--- |
| **System Design** | Overview + interview lens + case-study application | ~800–1,200 words per concept; trade-off tables; ≤2 sentences in case studies after dedup |
| **Microservices** | Deep-dive implementation patterns | 16-section architect playbook; production code patterns |
| **Technology Playbook** | Decision framework (ADR) | When to adopt; product/style comparison; link to SD overview + MS deep dive |

**Rule:** One **deep-dive owner** (MS) + one **overview owner** (SD, existing or planned) + optional **selection owner** (TP). Never three full textbooks for the same concept.

---

## Registry Legend

| Column | Meaning |
| :--- | :--- |
| **SD Owner** | `Existing` = flat slug today · `Planned` = Phase 2A slug · `Embedded` = case-study sections only · `—` = none |
| **MS Owner** | Active topic path under `content/microservices/` |
| **TP Owner** | Pattern ADR or `how-to-choose-*` page · `—` = none |
| **Dup Score** | 1 (unique) – 10 (severe fragmentation) |
| **Cross-link** | Recommended link direction after overview pages exist |

---

## 1. Foundations & Process

| Concept | SD Owner | MS Owner | TP Owner | Duplicate Locations (SD) | Dup | Cross-link Recommendation |
| :--- | :--- | :--- | :--- | :--- | :---: | :--- |
| What is System Design | **Planned** `what-is-system-design` | — | — | `_index.md` (minimal) | 1 | SD index → planned page |
| System design process (interview flow) | **Planned** `system-design-process` | `10-production-playbook/architecture-decision-records` (ADR format only) | — | Case studies §1–§3 (implicit) | 2 | SD process → MS ADRs for documentation |
| Non-functional requirements | **Planned** `non-functional-requirements` | `architecture-review-checklist` | `module-architecture-patterns` | All case study requirement tables | 4 | SD NFRs → MS PRR checklist |
| Capacity estimation / back-of-envelope | **Planned** `capacity-estimation` | `scalability-patterns` (partial) | — | `urlshortner` §Traffic + §9; 25+ case studies §9 | 5 | SD primer → `urlshortner` worked example |
| Architecture decision records | — | `architecture-decision-records` | `module-architecture-patterns` | — | 3 | MS ADRs ← SD process page |
| Architecture review checklist | — | `architecture-review-checklist` | — | — | 2 | MS checklist ← SD NFRs page |

---

## 2. Distributed Systems

| Concept | SD Owner | MS Owner | TP Owner | Duplicate Locations (SD) | Dup | Cross-link Recommendation |
| :--- | :--- | :--- | :--- | :--- | :---: | :--- |
| CAP theorem | **Planned** `cap-and-pacelc` | `04-distributed-systems/cap-and-pacelc` | — | `crdts-and-multi-master-conflict-resolution` (mention) | 7 | SD overview → MS `cap-and-pacelc` |
| PACELC | **Planned** `cap-and-pacelc` (merged) | `04-distributed-systems/cap-and-pacelc` | — | — | 7 | Same page as CAP |
| Consistency models | **Planned** `consistency-models` | `cap-and-pacelc`, `concurrency-control` | — | 15+ case studies (implicit) | 6 | SD overview → MS concurrency-control |
| MVCC / isolation levels | **Existing** `database-transactions-and-acid-isolation` | `04-distributed-systems/concurrency-control` | — | Case studies (ticket-booking, stock-broker) | 6 | SD page ↔ MS concurrency-control (mutual ≤2 sentences) |
| CRDT / multi-master merge | **Existing** `crdts-and-multi-master-conflict-resolution` | Link in `cap-and-pacelc` | — | `collaborative-text-editor` (application) | 4 | MS CAP → SD CRDTs for deep conflict resolution |
| Consistent hashing | **Planned** `consistent-hashing` | `04-distributed-systems/consistent-hashing` | — | `distributed-kv-store`, `distributed-lru-cache`, `distributed-rate-limiter`, `chat-application`, `load-balancers-and-routing-algorithms`, + interviews | 8 | SD overview → MS; case studies → SD overview |
| Consensus / leader election | — | `service-discovery` (Raft mention) | — | `distributed-message-queue`, `distributed-kv-store`, `single-point-of-failure-*`, `database-sharding-*` (embedded) | 5 | Phase 2 P1 page; MS service-discovery for ZK/etcd |
| Distributed transactions (2PC / saga) | **Embedded** | `03-data-management/saga` | `saga-pattern` | `hotel-booking`, `ecommerce`, `food-delivery` | 7 | SD P1 `saga-pattern-overview` → MS + TP |

---

## 3. Data Management

| Concept | SD Owner | MS Owner | TP Owner | Duplicate Locations (SD) | Dup | Cross-link Recommendation |
| :--- | :--- | :--- | :--- | :--- | :---: | :--- |
| Relational storage / B-trees | **Existing** `relational-database-fundamentals-and-b-trees` | — | `how-to-choose-database` | — | 2 | SD → TP for engine selection; PostgreSQL HB for depth |
| Database sharding | **Existing** `database-sharding-provisioning-and-chunk-routing` | `scalability-patterns` | — | `distributed-kv-store`, case studies | 6 | SD sharding ↔ MS scalability-patterns |
| Read replicas / replication lag | **Existing** `replication-lag-read-replica-topology` | `scalability-patterns` | — | Multiple case studies | 5 | SD page → MS scalability-patterns |
| CDC (change data capture) | **Existing** `cdc-based-cache-invalidation` | `03-data-management/outbox-and-cdc` | — | `email-delivery`, `stock-broker` (embedded) | 7 | SD CDC cache → MS outbox-and-cdc for full pattern |
| CQRS | **Embedded** | `03-data-management/cqrs-and-event-sourcing` | `cqrs-pattern` | `proximity-search`, `hotel-booking`, `payment-gateway-orchestration`, `distributed-logging-system`, `ecommerce`, `food-delivery` | 9 | SD P1 overview → MS + TP ADR |
| Event sourcing | **Embedded** | `03-data-management/cqrs-and-event-sourcing` | — | `stock-broker-trading`, `payment-gateway-orchestration` | 6 | SD P1 overview → MS |
| Saga pattern | **Embedded** | `03-data-management/saga` | `saga-pattern` | `food-delivery`, `ecommerce` | 6 | TP saga ADR → MS deep dive |
| Transactional outbox | **Embedded** | `03-data-management/outbox-and-cdc` | `outbox-pattern` | `email-delivery`, `notification-system`, `hotel-booking`, `stock-broker-trading`, `ott`, `online-learning-platform` | 9 | SD P1 overview → MS + TP |
| Database per service | — | `03-data-management/database-per-service` | `how-to-choose-database` | — | 4 | MS → TP for polyglot selection |
| Database decomposition | — | `09-migration-modernization/database-decomposition` | — | — | 2 | MS only; SD architecture-styles overview links |

---

## 4. Communication & Ingress

| Concept | SD Owner | MS Owner | TP Owner | Duplicate Locations (SD) | Dup | Cross-link Recommendation |
| :--- | :--- | :--- | :--- | :--- | :---: | :--- |
| Forward / reverse proxy | **Existing** `proxy-servers-forward-vs-reverse` | `api-gateway-and-bff` (partial) | `api-gateway` | — | 4 | SD proxy → MS gateway for unified ingress |
| L4 / L7 ingress routing | **Existing** `layer4-layer7-multi-tier-ingress-routing` | `api-gateway-and-bff` | `api-gateway` | — | 5 | SD ingress → MS gateway |
| REST vs gRPC | **Existing** `application-layer-protocols-rest-grpc` | `communication-topologies` | `how-to-choose-api-protocol` | Case studies (API sections) | 6 | SD concept → TP selection ADR |
| Load balancing algorithms | **Existing** `load-balancers-and-routing-algorithms` | `scalability-patterns` | — | `hands-on-load-balancing-setup` | 4 | SD ↔ MS; lab stays in SD |
| API Gateway | — | `02-service-communication/api-gateway-and-bff` | `api-gateway` | `layer4-layer7-*`, `proxy-servers-*` (overlap) | 7 | SD P1 `api-gateway-and-bff-overview` → MS + TP |
| BFF | — | `02-service-communication/api-gateway-and-bff` | `bff-pattern` | — | 5 | TP BFF ADR → MS |
| Service discovery | — | `02-service-communication/service-discovery` | — | `multi-region-topologies-*` (mention) | 4 | SD P1 overview → MS |
| Sync vs async topologies | — | `02-service-communication/communication-topologies` | `how-to-choose-message-broker` | Case studies (implicit) | 5 | MS topologies → TP broker ADR |
| Backpressure / flow control | **Partial** `transport-layer-mechanics-tcp-vs-udp` | `messaging-and-streaming-patterns` | — | `distributed-message-queue`, `notification-system`, `stock-broker-trading` | 5 | SD P1 dedicated page |
| Idempotency | **Partial** `application-layer-protocols-rest-grpc` | `resilience-patterns`, `messaging-and-streaming-patterns` | — | `payment-gateway-*`, `ticket-booking`, `notification-system` | 6 | SD P1 page → MS resilience |

---

## 5. Scalability & Performance

| Concept | SD Owner | MS Owner | TP Owner | Duplicate Locations (SD) | Dup | Cross-link Recommendation |
| :--- | :--- | :--- | :--- | :--- | :---: | :--- |
| Caching hierarchy / CDN | **Existing** `caching-and-cdns-hierarchical-arrays` | `caching-patterns` | `how-to-choose-cache` | Case studies (cache tiers) | 7 | SD fundamentals → MS patterns → TP selection |
| Cache eviction policies | **Existing** `cache-eviction-and-mutation-policies` | `caching-patterns` | — | `distributed-lru-cache` | 5 | SD → MS |
| Cache stampede / bloom filter | **Existing** `cache-stampede-and-penetration-mitigation` | `caching-patterns` | — | `distributed-lru-cache`, `urlshortner` | 5 | SD → MS |
| Horizontal vs vertical scaling | **Planned** `horizontal-vs-vertical-scaling` | `scalability-patterns` | — | 10+ pages (mentions) | 6 | SD overview → MS |
| Latency vs throughput | **Planned** `latency-vs-throughput` | `scalability-patterns` (tangential) | — | Case study SLO tables only | 4 | SD owns (no MS canonical) |
| Rate limiting / throttling | **Case study** `distributed-rate-limiter` | `scalability-patterns` | — | Interview companion | 6 | SD P1 `rate-limiting-fundamentals` → case study + MS |
| Hot key / hot partition | **Embedded** | `scalability-patterns` | — | `distributed-kv-store`, `sponsored-ads`, `leaderboard` | 5 | MS → SD case studies |

---

## 6. Reliability & Resilience

| Concept | SD Owner | MS Owner | TP Owner | Duplicate Locations (SD) | Dup | Cross-link Recommendation |
| :--- | :--- | :--- | :--- | :--- | :---: | :--- |
| SPOF elimination / redundancy | **Existing** `single-point-of-failure-elimination-redundancy` | `failure-scenarios` | — | All case studies §reliability | 4 | SD owns fundamentals; MS owns runbooks |
| Multi-region / AZ topologies | **Existing** `multi-region-topologies-and-availability-zones` | `failure-scenarios` | — | Case studies (region tables) | 4 | SD ↔ MS failure-scenarios |
| Availability / nines | **Planned** `availability-and-nines` | `reliability-engineering` | — | 25+ case study SLO tables | 5 | SD overview → MS reliability-engineering |
| SLO / SLI / SLA / error budgets | — | `reliability-engineering` | — | Case studies (embedded targets) | 5 | SD P1 page → MS |
| Resilience patterns (CB, bulkhead, retry, timeout, fallback) | **Planned** `resilience-patterns-overview` | `05-resilience-patterns/resilience-patterns` | `circuit-breaker-pattern`, `bulkhead-pattern` | `payment-gateway-orchestration`, `linkedin-job-search`, `leaderboard`, `distributed-rate-limiter`, `notification-system`, `urlshortner`, `ecommerce`, `food-delivery`, `ride-sharing`, + interviews | 8 | SD overview → MS; TP ADRs → SD overview |
| Circuit breaker | **Embedded** | `resilience-patterns` | `circuit-breaker-pattern` | 14+ SD files | 8 | TP trim to ADR + links |
| Bulkhead | **Embedded** | `resilience-patterns` | `bulkhead-pattern` | `payment-gateway-orchestration` | 7 | Same cluster |
| Deployment strategies | — | `deployment-strategies` | — | — | 3 | MS only |
| Failure scenarios / chaos | — | `failure-scenarios`, `reliability-engineering` | — | Case study §10 tables | 4 | MS runbooks; SD case studies link |
| Zero-downtime deployments | — | `zero-downtime-deployments` | — | — | 2 | MS only |

---

## 7. Observability

| Concept | SD Owner | MS Owner | TP Owner | Duplicate Locations (SD) | Dup | Cross-link Recommendation |
| :--- | :--- | :--- | :--- | :--- | :---: | :--- |
| Observability pillars (metrics, logs, traces) | **Planned** `observability-fundamentals` | `08-observability/observability` | — | 20+ case studies (OpenTelemetry mentions) | 7 | SD overview → MS |
| Distributed logging (system design) | **Existing** `distributed-logging-system` | `observability` §logging | — | — | 5 | SD case study → SD observability fundamentals → MS |
| Distributed tracing | **Embedded** | `observability` | — | `chat-application`, `linkedin-job-search`, `notification-system`, `fleet-vending-iot`, +15 | 7 | Case studies → SD observability fundamentals |
| RED / USE metrics | — | `observability` | — | Case studies (metrics tables) | 5 | MS canonical |
| Structured logging / log aggregation | **Case study** `distributed-logging-system` | `observability` | — | Overlaps with tracing in cases | 6 | Distinguish: logging design vs pillars |

---

## 8. Architecture Styles & Platform

| Concept | SD Owner | MS Owner | TP Owner | Duplicate Locations (SD) | Dup | Cross-link Recommendation |
| :--- | :--- | :--- | :--- | :--- | :---: | :--- |
| Monolith | — | `01-architecture-styles/architecture-styles` | `monolith-architecture` | — | 5 | SD planned overview → MS + TP |
| Modular monolith | — | `architecture-styles` | `modular-monolith-architecture` | — | 5 | TP ADR → MS |
| Microservices | — | `architecture-styles` | `microservices-architecture` | — | 6 | TP ADR → MS deep dive |
| SOA | — | `architecture-styles` | `soa-architecture` | — | 5 | TP → MS |
| Architecture styles comparison | **Planned** `architecture-styles-overview` | `01-architecture-styles/architecture-styles` | `module-architecture-patterns` | — | 6 | SD hub page linking MS + 4 TP ADRs |
| Event-driven architecture | — | `06-event-driven/event-driven-architecture` | `event-driven-architecture` | `distributed-message-queue` (case) | 6 | SD case study → MS + TP |
| Messaging / streaming patterns | **Case study** `distributed-message-queue` | `messaging-and-streaming-patterns` | `how-to-choose-message-broker` | Interview companion | 6 | SD case → Kafka HB for broker depth |
| Strangler fig | — | `09-migration-modernization/strangler-pattern` | `strangler-pattern` | — | 6 | TP ADR → MS |
| Monolith decomposition | — | `monolith-decomposition` | — | — | 3 | MS only |
| Service mesh / sidecar | — | `07-platform-patterns/sidecar-and-service-mesh` | `service-mesh`, `sidecar-pattern` | Interview mentions only | 7 | TP ADRs → MS |
| Kubernetes patterns (architect) | — | `07-platform-patterns/kubernetes-patterns` | — | — | 3 | MS → K8s HB for primitives |

---

## 9. Networking & Transport (SD-Unique)

| Concept | SD Owner | MS Owner | TP Owner | Duplicate Locations | Dup | Cross-link Recommendation |
| :--- | :--- | :--- | :--- | :--- | :---: | :--- |
| IP, DNS, firewalls | **Existing** `networking-essentials-ip-dns-firewalls` | — | — | — | 1 | SD owns; no MS duplication |
| TCP vs UDP | **Existing** `transport-layer-mechanics-tcp-vs-udp` | — | — | — | 1 | SD owns |
| HTTP/3, QUIC, WebSockets | **Existing** `http3-quic-and-websocket-transports` | — | `how-to-choose-api-protocol` (partial) | `chat-application`, `collaborative-text-editor` (application) | 2 | SD → case studies |
| Hands-on load balancing lab | **Existing** `hands-on-load-balancing-setup` | — | — | — | 1 | SD owns |

---

## 10. Case Studies & Interview (SD-Unique Application Layer)

| Concept | SD Owner | MS Owner | TP Owner | Notes |
| :--- | :--- | :--- | :--- | :--- |
| End-to-end system designs (27) | **Existing** case study slugs | — | — | Application of patterns; not pattern textbooks |
| Case-study interview Q&A (19) | **Existing** `*-interview-questions` | `11-interview-guide/*` (μservices scope) | — | Parallel corpora; different scope |
| System design interview framework | **Planned** (P1) | `top-300-microservices-questions` | — | Do not merge; cross-link at end |
| Learning paths | — | `12-learning-paths/*` | — | MS owns; SD may add SD-specific path later (P1) |

---

## Duplication Severity Matrix

| Rank | Concept cluster | Locations (approx.) | SD | MS | TP | Severity | Remediation phase |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| 1 | **CQRS** | 8 | 6 embedded | 1 | 1 | **9** | Phase 2A P1 page + Phase 5 case trim |
| 2 | **Outbox + CDC** | 9 | 5 embedded + 1 fundamental | 1 | 1 | **9** | Merge SD CDC page intent with MS; trim case studies |
| 3 | **Circuit breaker / resilience** | 16+ | 12+ embedded | 1 | 2 | **8** | Phase 2A `resilience-patterns-overview` + Phase 5 |
| 4 | **Consistent hashing** | 14+ | 11 embedded | 1 | — | **8** | Phase 2A `consistent-hashing` + Phase 5 |
| 5 | **Observability / tracing** | 22+ | 20 embedded + 1 case | 1 | — | **7** | Phase 2A `observability-fundamentals` |
| 6 | **Caching** | 8 | 4 fundamentals + cases | 1 | 1 | **7** | SD keeps fundamentals; MS owns production patterns |
| 7 | **CAP / PACELC** | 3 | 1 mention | 1 | — | **7** | Phase 2A `cap-and-pacelc` |
| 8 | **API Gateway / ingress** | 6 | 2 fundamentals | 1 | 2 | **7** | Clarify: SD = transport; MS = gateway pattern |
| 9 | **Service mesh** | 4 | interviews | 1 | 2 | **7** | Link only from SD |
| 10 | **Architecture styles** | 6 | — | 1 | 4 | **6** | Phase 2A `architecture-styles-overview` |
| 11 | **Saga** | 4 | 2 embedded | 1 | 1 | **6** | P1 overview page |
| 12 | **Concurrency / isolation** | 4 | 1 fundamental | 1 | — | **6** | Mutual cross-link; no merge |

---

## Canonical Owner Decision Table (Phase 4 Preview)

Per approved strategy — **not executed in Phase 3**.

| Concept | A) Stay / SD overview | B) MS deep dive | C) TP ADR | D) SD summary + links |
| :--- | :---: | :---: | :---: | :---: |
| CAP / PACELC | ✅ Planned | ✅ Keep | — | ✅ |
| CQRS / saga / outbox | ✅ Planned (P1) | ✅ Keep | ✅ Trim to ADR | ✅ |
| Resilience patterns | ✅ Planned | ✅ Keep | ✅ Trim CB/bulkhead | ✅ |
| Consistent hashing | ✅ Planned | ✅ Keep | — | ✅ |
| Caching | ✅ Keep 4 SD fundamentals | ✅ Keep patterns | ✅ `how-to-choose-cache` | ✅ |
| Observability | ✅ Planned | ✅ Keep | — | ✅ |
| Architecture styles | ✅ Planned | ✅ Keep | ✅ Keep 4 style ADRs | ✅ |
| REST/gRPC | ✅ Keep SD page | Partial in topologies | ✅ `how-to-choose-api-protocol` | ✅ |
| Networking / TCP / QUIC | ✅ SD only | — | — | — |
| Case studies | ✅ SD only | Link out | — | — |
| Sharding / replication | ✅ Keep SD fundamentals | ✅ scalability-patterns | — | ✅ |
| CRDTs | ✅ SD only (deep) | Link only | — | — |
| Message broker internals | Case study only | Messaging patterns | ✅ `how-to-choose-message-broker` | Link Kafka HB |
| K8s primitives | — | K8s patterns (architect) | — | Link K8s HB |

---

## Recommended Cross-Link Wiring

### SD → MS (deep dive) — 22 links when Phase 2A complete

| SD page (existing or planned) | Link to MS |
| :--- | :--- |
| `cap-and-pacelc` (planned) | `04-distributed-systems/cap-and-pacelc` |
| `consistency-models` (planned) | `concurrency-control` |
| `consistent-hashing` (planned) | `consistent-hashing` |
| `database-transactions-and-acid-isolation` | `concurrency-control` |
| `cdc-based-cache-invalidation` | `outbox-and-cdc` |
| `caching-and-cdns-hierarchical-arrays` | `caching-patterns` |
| `replication-lag-read-replica-topology` | `scalability-patterns` |
| `database-sharding-provisioning-and-chunk-routing` | `scalability-patterns` |
| `proxy-servers-forward-vs-reverse` | `api-gateway-and-bff` |
| `application-layer-protocols-rest-grpc` | `communication-topologies` |
| `resilience-patterns-overview` (planned) | `resilience-patterns` |
| `observability-fundamentals` (planned) | `observability` |
| `architecture-styles-overview` (planned) | `architecture-styles` |
| `horizontal-vs-vertical-scaling` (planned) | `scalability-patterns` |
| `availability-and-nines` (planned) | `reliability-engineering` |
| `non-functional-requirements` (planned) | `architecture-review-checklist` |
| `distributed-logging-system` | `observability` |
| `distributed-message-queue` | `messaging-and-streaming-patterns` |
| `distributed-rate-limiter` | `scalability-patterns` + `resilience-patterns` |
| `crdts-and-multi-master-conflict-resolution` | `cap-and-pacelc` |
| `system-design-process` (planned) | `architecture-decision-records` |
| `capacity-estimation` (planned) | `scalability-patterns` |

### SD → TP (selection ADR) — 10 links

| SD page | Link to TP |
| :--- | :--- |
| `architecture-styles-overview` (planned) | `monolith-architecture`, `modular-monolith-architecture`, `microservices-architecture`, `soa-architecture` |
| `application-layer-protocols-rest-grpc` | `how-to-choose-api-protocol` |
| `caching-and-cdns-hierarchical-arrays` | `how-to-choose-cache` |
| `resilience-patterns-overview` (planned) | `circuit-breaker-pattern`, `bulkhead-pattern` |
| `relational-database-fundamentals-and-b-trees` | `how-to-choose-database` |
| `distributed-message-queue` | `how-to-choose-message-broker` |
| `non-functional-requirements` (planned) | `module-architecture-patterns` |

### MS → SD (overview back-links) — 11 links

| MS page | Link to SD |
| :--- | :--- |
| `cap-and-pacelc` | `cap-and-pacelc` (planned) + `crdts-and-multi-master-conflict-resolution` |
| `consistent-hashing` | `consistent-hashing` (planned) + `distributed-kv-store` case study |
| `cqrs-and-event-sourcing` | `proximity-search`, `hotel-booking` case studies |
| `outbox-and-cdc` | `cdc-based-cache-invalidation`, `email-delivery` |
| `resilience-patterns` | `resilience-patterns-overview` (planned) + `payment-gateway-orchestration` |
| `observability` | `observability-fundamentals` (planned) + `distributed-logging-system` |
| `architecture-styles` | `architecture-styles-overview` (planned) |
| `caching-patterns` | SD cache fundamentals (4 pages) |
| `scalability-patterns` | `horizontal-vs-vertical-scaling`, `latency-vs-throughput` (planned) |
| `saga` | `food-delivery`, `ecommerce` case studies |
| `api-gateway-and-bff` | `layer4-layer7-multi-tier-ingress-routing` |

### TP → SD + MS — 8 pattern ADRs to rewire

| TP page | Primary link | Deep dive |
| :--- | :--- | :--- |
| `cqrs-pattern` | SD `cqrs-overview` (P1) | MS `cqrs-and-event-sourcing` |
| `saga-pattern` | SD `saga-pattern-overview` (P1) | MS `saga` |
| `outbox-pattern` | SD `transactional-outbox-overview` (P1) | MS `outbox-and-cdc` |
| `circuit-breaker-pattern` | SD `resilience-patterns-overview` | MS `resilience-patterns` |
| `bulkhead-pattern` | SD `resilience-patterns-overview` | MS `resilience-patterns` |
| `microservices-architecture` | SD `architecture-styles-overview` | MS `architecture-styles` |
| `event-driven-architecture` | SD `distributed-message-queue` | MS `event-driven-architecture` |
| `service-mesh` | — (platform) | MS `sidecar-and-service-mesh` |

---

## Enforcement Rules (Future Content)

1. **Case studies:** Pattern sections > 2 paragraphs → replace with link to SD overview (planned) or MS deep dive.
2. **Technology Playbook pattern pages:** Keep adoption criteria + comparison table; move pattern mechanics to MS; add SD overview link when exists.
3. **Microservices playbook:** Add "System Design overview" link in Architect Notes for all 38 topics.
4. **New SD fundamentals:** Must declare `conceptOwner` in front matter (future) — `overview` | `application` | `unique`.
5. **Grep CI (optional):** Flag `## CQRS` or `### Circuit Breaker` headings in case studies after Phase 5.

---

## Explicit Non-Actions (Phase 3)

| Action | Status |
| :--- | :---: |
| Move content between handbooks | ❌ |
| Create aliases | ❌ |
| Rewrite pages | ❌ |
| Modify navigation YAML | ❌ |
| Merge Microservices into System Design | ❌ |

---

## Relationship to Other Phases

| Phase | Status | Relationship |
| :--- | :--- | :--- |
| **Phase 1** | ✅ Complete | Module structure for SD sidebar |
| **Phase 2** | ✅ Complete | Identified 52 concepts via 14 P0 + 18 P1 + existing |
| **Phase 2A** | ✅ Complete | 13 planned SD overview pages map to registry gaps |
| **Phase 3** | ✅ Complete | This document |
| **Phase 4** | Awaiting approval | Sign off canonical owner table §Canonical Owner Decision |
| **Phase 5** | Future | Case study dedup per Duplication Severity Matrix |

---

## Exit Criteria — Phase 3

| Criterion | Status |
| :--- | :---: |
| Concept registry created (52 concepts) | ✅ |
| Canonical owner role per handbook | ✅ |
| Duplicate locations documented | ✅ |
| Cross-link recommendations documented | ✅ |
| No content or navigation changes | ✅ |

**Do not proceed to Phase 4 without explicit approval.**
