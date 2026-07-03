---
title: "System Design Curriculum Migration Plan — Phase A Inventory"
date: 2026-07-03T16:00:00+00:00
draft: true
description: "Phase A inventory — overlap analysis between system-design and microservices, concept registry, duplication report, navigation and alias proposals."
tags: ["system-design", "meta", "planning", "migration"]
---

# Phase A — Inventory & Overlap Analysis

**Scope:** `content/system-design/` + `content/microservices/` (read-only analysis)  
**Audience:** Principal architects, documentation maintainers  
**Status:** Planning only — **no content, navigation, or file changes in Phase A**

**Goal:** Converge toward a unified **Architect-Level System Design Curriculum** without destructive rewrite. Microservices pattern depth migrates into System Design; case studies remain in System Design; Technology Playbook retains selection ADRs only.

---

## Executive Summary

| Metric | System Design | Microservices (active) |
| :--- | :---: | :---: |
| **Content files** | 66 (+ `_index`) | 38 topic pages (+ 12 section `_index`, `_index`) |
| **Structure** | Flat; 2 sidebar groups (Fundamentals / Case Studies) | 12 numbered modules (post Phase B) |
| **Template** | 11-section case-study playbook | 16-section architect playbook v3 |
| **Dedicated pattern pages** | ~19 fundamentals (partial overlap) | ~25 pattern/production pages |
| **Interview content** | 19 case-study Q&A companions | Top 300 + 5 subsets |
| **Concept overlap** | **High** — patterns embedded in case studies | **High** — canonical pattern pages |

**Recommended canonical owner:** **System Design** (unified curriculum).  
**Microservices section:** Gradual deprecation via aliases → System Design paths (Phase 3+).  
**Technology Playbook:** Trim pattern deep-dives over time; keep selection matrices only.

---

## 1. Complete Inventory — System Design

**Scoring:** Duplication score 1 (unique) – 10 (heavily duplicated with microservices or technology-playbook).

### 1.1 Foundations (Networking, Protocols, Ingress)

| File | Current Category | Suggested Target | Dup | Priority | Notes |
| :--- | :--- | :--- | :---: | :---: | :--- |
| `networking-essentials-ip-dns-firewalls.md` | Fundamentals | `01-foundations/networking-essentials.md` | 2 | P3 | Keep; no MS duplicate |
| `transport-layer-mechanics-tcp-vs-udp.md` | Fundamentals | `01-foundations/transport-tcp-udp.md` | 2 | P3 | Keep |
| `http3-quic-and-websocket-transports.md` | Fundamentals | `01-foundations/http-quic-websockets.md` | 3 | P3 | MS mentions mesh transport |
| `application-layer-protocols-rest-grpc.md` | Fundamentals | `04-communication/rest-vs-grpc.md` | 6 | P2 | Overlap TP `how-to-choose-api-protocol` — SD owns concept; TP owns selection ADR |
| `proxy-servers-forward-vs-reverse.md` | Fundamentals | `04-communication/proxy-forward-reverse.md` | 4 | P2 | MS API gateway references |
| `layer4-layer7-multi-tier-ingress-routing.md` | Fundamentals | `04-communication/ingress-routing.md` | 5 | P2 | Overlap MS `api-gateway-and-bff` |
| `load-balancers-and-routing-algorithms.md` | Fundamentals | `05-scalability/load-balancing.md` | 4 | P2 | Partial MS scalability |
| `hands-on-load-balancing-setup.md` | Fundamentals | `01-foundations/load-balancing-lab.md` | 1 | P4 | Optional lab; low migration priority |

### 1.2 Caching & CDN

| File | Current Category | Suggested Target | Dup | Priority | Notes |
| :--- | :--- | :--- | :---: | :---: | :--- |
| `caching-and-cdns-hierarchical-arrays.md` | Fundamentals | `05-scalability/caching-fundamentals.md` | 5 | P2 | MS `caching-patterns` |
| `cache-eviction-and-mutation-policies.md` | Fundamentals | `05-scalability/cache-eviction-policies.md` | 5 | P2 | MS caching-patterns |
| `cache-stampede-and-penetration-mitigation.md` | Fundamentals | `05-scalability/cache-stampede.md` | 5 | P2 | MS caching-patterns |
| `cdc-based-cache-invalidation.md` | Fundamentals | `03-data-management/cdc.md` §cache | 7 | P1 | Near-dup MS `outbox-and-cdc` + caching |

### 1.3 Data & Storage Fundamentals

| File | Current Category | Suggested Target | Dup | Priority | Notes |
| :--- | :--- | :--- | :---: | :---: | :--- |
| `relational-database-fundamentals-and-b-trees.md` | Fundamentals | `03-data-management/relational-storage-internals.md` | 3 | P3 | PostgreSQL HB owns engine depth |
| `database-transactions-and-acid-isolation.md` | Fundamentals | `02-distributed-systems/concurrency-control.md` | 6 | P1 | MS `concurrency-control` |
| `replication-lag-read-replica-topology.md` | Fundamentals | `05-scalability/read-replica-scaling.md` | 6 | P1 | MS `scalability-patterns` |
| `database-sharding-provisioning-and-chunk-routing.md` | Fundamentals | `05-scalability/sharding-routing.md` | 6 | P1 | MS consistent-hashing + scalability |
| `crdts-and-multi-master-conflict-resolution.md` | Fundamentals | `02-distributed-systems/cap-theorem.md` §conflicts | 5 | P2 | MS CAP page links here |

### 1.4 Reliability & Topology

| File | Current Category | Suggested Target | Dup | Priority | Notes |
| :--- | :--- | :--- | :---: | :---: | :--- |
| `single-point-of-failure-elimination-redundancy.md` | Fundamentals | `06-reliability/redundancy-and-spof.md` | 4 | P2 | MS failure-scenarios |
| `multi-region-topologies-and-availability-zones.md` | Fundamentals | `06-reliability/multi-region-topologies.md` | 4 | P2 | MS failure-scenarios §region |

### 1.5 Case Studies (29 designs)

| File | Current Category | Suggested Target | Dup | Priority | Notes |
| :--- | :--- | :--- | :---: | :---: | :--- |
| `urlshortner.md` | Case Study | `10-case-studies/url-shortener.md` | 2 | P3 | Reference implementation |
| `distributed-rate-limiter.md` | Case Study | `10-case-studies/distributed-rate-limiter.md` | 5 | P2 | Embeds circuit breaker, consistent hash |
| `leaderboard.md` | Case Study | `10-case-studies/leaderboard.md` | 4 | P3 | Circuit breaker, observability |
| `distributed-lru-cache.md` | Case Study | `10-case-studies/distributed-lru-cache.md` | 6 | P2 | Overlap MS caching + consistent hash |
| `distributed-kv-store.md` | Case Study | `10-case-studies/distributed-kv-store.md` | 4 | P3 | |
| `notification-system.md` | Case Study | `10-case-studies/notification-system.md` | 3 | P3 | |
| `chat-application.md` | Case Study | `10-case-studies/chat-application.md` | 5 | P2 | Consistent hash, tracing |
| `social-feed.md` | Case Study | `10-case-studies/social-feed.md` | 3 | P3 | |
| `email-delivery.md` | Case Study | `10-case-studies/email-delivery.md` | 7 | P1 | Deep outbox/CDC — link canonical |
| `cloud-storage.md` | Case Study | `10-case-studies/cloud-storage.md` | 2 | P3 | |
| `distributed-message-queue.md` | Case Study | `10-case-studies/distributed-message-queue.md` | 5 | P2 | Kafka HB owns broker |
| `distributed-job-scheduler.md` | Case Study | `10-case-studies/distributed-job-scheduler.md` | 3 | P3 | |
| `distributed-logging-system.md` | Case Study | `10-case-studies/distributed-logging.md` | 6 | P2 | MS observability |
| `distributed-web-crawler.md` | Case Study | `10-case-studies/distributed-web-crawler.md` | 3 | P3 | |
| `proximity-search.md` | Case Study | `10-case-studies/proximity-search.md` | 6 | P2 | Embeds CQRS — link canonical |
| `linkedin-job-search.md` | Case Study | `10-case-studies/linkedin-job-search.md` | 3 | P3 | |
| `food-delivery.md` | Case Study | `10-case-studies/food-delivery.md` | 3 | P3 | |
| `ride-sharing.md` | Case Study | `10-case-studies/ride-sharing.md` | 3 | P3 | |
| `ticket-booking.md` | Case Study | `10-case-studies/ticket-booking.md` | 4 | P3 | |
| `hotel-booking.md` | Case Study | `10-case-studies/hotel-booking.md` | 7 | P1 | CQRS + outbox embedded |
| `ecommerce.md` | Case Study | `10-case-studies/ecommerce.md` | 3 | P3 | |
| `payment-gateway-orchestration.md` | Case Study | `10-case-studies/payment-gateway.md` | 6 | P2 | CQRS, bulkhead, circuit breaker |
| `stock-broker-trading.md` | Case Study | `10-case-studies/stock-broker-trading.md` | 6 | P2 | Outbox embedded |
| `sponsored-ads.md` | Case Study | `10-case-studies/sponsored-ads.md` | 3 | P3 | |
| `ott.md` | Case Study | `10-case-studies/ott-streaming.md` | 3 | P3 | |
| `online-learning-platform.md` | Case Study | `10-case-studies/online-learning.md` | 3 | P3 | |
| `fleet-vending-iot.md` | Case Study | `10-case-studies/fleet-vending-iot.md` | 4 | P3 | Observability |
| `collaborative-text-editor.md` | Case Study | `10-case-studies/collaborative-editor.md` | 5 | P2 | Consistent hashing |

### 1.6 Case Study Interview Companions (19 files)

| File | Current Category | Suggested Target | Dup | Priority | Notes |
| :--- | :--- | :--- | :---: | :---: | :--- |
| `*-interview-questions.md` (19) | Interview | `11-interview-guide/case-studies/<slug>-questions.md` | 3 | P3 | Keep paired with case study; merge into unified interview module later |

---

## 2. Complete Inventory — Microservices (Active Pages Only)

Exclude `_legacy_flat/`, `_meta/`. These are **migration sources** into System Design.

| File | Current Module | Suggested SD Target | Dup | Priority | Action |
| :--- | :--- | :--- | :---: | :---: | :--- |
| `01-architecture-styles/architecture-styles.md` | Architecture | `08-architecture-styles/architecture-styles.md` | 5 | P1 | **Migrate** — canonical styles |
| `02-service-communication/api-gateway-and-bff.md` | Communication | `04-communication/api-gateway-and-bff.md` | 6 | P1 | **Migrate** |
| `02-service-communication/service-discovery.md` | Communication | `04-communication/service-discovery.md` | 5 | P1 | **Migrate** |
| `02-service-communication/communication-topologies.md` | Communication | `04-communication/communication-topologies.md` | 5 | P1 | **Migrate** |
| `03-data-management/database-per-service.md` | Data | `03-data-management/database-per-service.md` | 4 | P1 | **Migrate** |
| `03-data-management/cqrs-and-event-sourcing.md` | Data | `03-data-management/cqrs-and-event-sourcing.md` | 8 | P0 | **Migrate** — high overlap case studies |
| `03-data-management/saga.md` | Data | `03-data-management/saga-pattern.md` | 7 | P0 | **Migrate**; trim TP `saga-pattern` |
| `03-data-management/outbox-and-cdc.md` | Data | `03-data-management/outbox-and-cdc.md` | 8 | P0 | **Migrate**; trim SD `cdc-based-cache-invalidation` depth |
| `04-distributed-systems/cap-and-pacelc.md` | Distributed | `02-distributed-systems/cap-and-pacelc.md` | 7 | P0 | **Migrate** |
| `04-distributed-systems/consistent-hashing.md` | Distributed | `02-distributed-systems/consistent-hashing.md` | 7 | P0 | **Migrate**; case studies link here |
| `04-distributed-systems/concurrency-control.md` | Distributed | `02-distributed-systems/concurrency-control.md` | 6 | P1 | **Migrate**; merge SD `database-transactions-and-acid-isolation` |
| `05-resilience-patterns/resilience-patterns.md` | Resilience | `06-reliability/resilience-patterns.md` | 8 | P0 | **Migrate**; trim TP circuit/bulkhead |
| `06-event-driven/event-driven-architecture.md` | Event-driven | `09-microservices-patterns/event-driven-architecture.md` | 5 | P1 | **Migrate** |
| `06-event-driven/messaging-and-streaming-patterns.md` | Event-driven | `09-microservices-patterns/messaging-streaming.md` | 6 | P1 | Link Kafka HB |
| `07-platform-patterns/sidecar-and-service-mesh.md` | Platform | `09-microservices-patterns/sidecar-and-service-mesh.md` | 7 | P0 | **Migrate**; trim TP service-mesh |
| `07-platform-patterns/kubernetes-patterns.md` | Platform | `09-microservices-patterns/kubernetes-patterns.md` | 4 | P2 | Link K8s HB |
| `08-observability/observability.md` | Observability | `07-observability/observability.md` | 7 | P0 | **Migrate** |
| `09-migration-modernization/strangler-pattern.md` | Migration | `08-architecture-styles/strangler-pattern.md` | 6 | P1 | **Migrate**; trim TP strangler |
| `09-migration-modernization/monolith-decomposition.md` | Migration | `08-architecture-styles/monolith-decomposition.md` | 4 | P1 | **Migrate** |
| `09-migration-modernization/database-decomposition.md` | Migration | `03-data-management/database-decomposition.md` | 5 | P1 | **Migrate** |
| `09-migration-modernization/zero-downtime-deployments.md` | Migration | `06-reliability/zero-downtime-deployments.md` | 5 | P2 | **Migrate** |
| `10-production-playbook/scalability-patterns.md` | Production | `05-scalability/scalability-patterns.md` | 6 | P1 | **Migrate**; merge SD fundamentals |
| `10-production-playbook/caching-patterns.md` | Production | `05-scalability/caching-patterns.md` | 6 | P1 | **Migrate** |
| `10-production-playbook/deployment-strategies.md` | Production | `06-reliability/deployment-strategies.md` | 4 | P2 | **Migrate** |
| `10-production-playbook/reliability-engineering.md` | Production | `06-reliability/reliability-engineering.md` | 4 | P2 | **Migrate** |
| `10-production-playbook/architecture-decision-records.md` | Production | `01-foundations/architecture-decision-records.md` | 2 | P2 | **Migrate** |
| `10-production-playbook/failure-scenarios.md` | Production | `06-reliability/failure-scenarios.md` | 3 | P2 | **Migrate** |
| `10-production-playbook/architecture-review-checklist.md` | Production | `01-foundations/architecture-review-checklist.md` | 2 | P2 | **Migrate** |
| `11-interview-guide/top-300-microservices-questions.md` | Interview | `11-interview-guide/top-300-system-design-questions.md` | 5 | P1 | **Merge** with case-study Q&A |
| `11-interview-guide/architect-questions.md` | Interview | `11-interview-guide/architect-questions.md` | 4 | P2 | Subset |
| `11-interview-guide/*-questions.md` (4 more) | Interview | `11-interview-guide/` | 4 | P2 | Subsets |
| `12-learning-paths/*.md` (4) | Learning | `12-learning-paths/` | 3 | P2 | **Migrate** |

---

## 3. Concept Registry (Canonical Owner → Future System Design Path)

**Rule:** One canonical page per concept. Case studies and handbooks link with ≤2 sentences.

| Concept | Canonical Owner Page (Target) | Current SD Location | Current MS Location | TP Overlap |
| :--- | :--- | :--- | :--- | :--- |
| CAP theorem | `02-distributed-systems/cap-and-pacelc.md` | `crdts-and-multi-master-conflict-resolution.md` (mention) | `cap-and-pacelc.md` | — |
| PACELC | `02-distributed-systems/cap-and-pacelc.md` | — | `cap-and-pacelc.md` | — |
| Consistent hashing | `02-distributed-systems/consistent-hashing.md` | Embedded in 8+ case studies | `consistent-hashing.md` | — |
| MVCC / isolation / concurrency | `02-distributed-systems/concurrency-control.md` | `database-transactions-and-acid-isolation.md` | `concurrency-control.md` | — |
| CRDT conflict resolution | `02-distributed-systems/cap-and-pacelc.md` §CRDT | `crdts-and-multi-master-conflict-resolution.md` | Link only | — |
| Database per service | `03-data-management/database-per-service.md` | — | `database-per-service.md` | `how-to-choose-database` (selection) |
| CQRS | `03-data-management/cqrs-and-event-sourcing.md` | `proximity-search`, `hotel-booking`, `payment-gateway` (embedded) | `cqrs-and-event-sourcing.md` | `cqrs-pattern.md` (trim) |
| Event sourcing | `03-data-management/cqrs-and-event-sourcing.md` | — | `cqrs-and-event-sourcing.md` | — |
| Saga | `03-data-management/saga-pattern.md` | — | `saga.md` | `saga-pattern.md` (trim) |
| Transactional outbox | `03-data-management/outbox-and-cdc.md` | `email-delivery`, `hotel-booking`, `stock-broker` (embedded) | `outbox-and-cdc.md` | `outbox-pattern.md` (trim) |
| CDC | `03-data-management/outbox-and-cdc.md` | `cdc-based-cache-invalidation.md` | `outbox-and-cdc.md` | — |
| Database decomposition | `03-data-management/database-decomposition.md` | — | `database-decomposition.md` | — |
| API Gateway | `04-communication/api-gateway-and-bff.md` | `layer4-layer7-*`, `proxy-servers-*` | `api-gateway-and-bff.md` | `api-gateway.md` (trim) |
| BFF | `04-communication/api-gateway-and-bff.md` | — | `api-gateway-and-bff.md` | `bff-pattern.md` (trim) |
| Service discovery | `04-communication/service-discovery.md` | `multi-region-topologies` (mention) | `service-discovery.md` | — |
| REST vs gRPC (concept) | `04-communication/rest-vs-grpc.md` | `application-layer-protocols-rest-grpc.md` | `communication-topologies` | `how-to-choose-api-protocol` (selection) |
| Sync/async topologies | `04-communication/communication-topologies.md` | Case studies (implicit) | `communication-topologies.md` | — |
| Load balancing | `05-scalability/load-balancing.md` | `load-balancers-and-routing-algorithms.md` | `scalability-patterns` (partial) | — |
| Caching patterns | `05-scalability/caching-patterns.md` | 4 cache fundamental pages + `distributed-lru-cache` | `caching-patterns.md` | `how-to-choose-cache` (selection) |
| Sharding / read replicas | `05-scalability/scalability-patterns.md` | `database-sharding-*`, `replication-lag-*` | `scalability-patterns.md` | — |
| Circuit breaker | `06-reliability/resilience-patterns.md` | Embedded in 10+ case studies | `resilience-patterns.md` | `circuit-breaker-pattern.md` (trim) |
| Bulkhead | `06-reliability/resilience-patterns.md` | `payment-gateway` (embedded) | `resilience-patterns.md` | `bulkhead-pattern.md` (trim) |
| Retry / timeout / fallback | `06-reliability/resilience-patterns.md` | Case studies (partial) | `resilience-patterns.md` | — |
| Redundancy / SPOF | `06-reliability/redundancy-and-spof.md` | `single-point-of-failure-*` | `failure-scenarios` | — |
| Multi-region | `06-reliability/multi-region-topologies.md` | `multi-region-topologies-*` | `failure-scenarios` | — |
| Deployment strategies | `06-reliability/deployment-strategies.md` | — | `deployment-strategies.md` | — |
| Failure scenarios runbook | `06-reliability/failure-scenarios.md` | Case study §10 tables | `failure-scenarios.md` | — |
| Observability (3 pillars) | `07-observability/observability.md` | Embedded in 15+ case studies | `observability.md` | — |
| Distributed tracing | `07-observability/observability.md` §tracing | Case studies | `observability.md` | K8s HB OTel |
| Monolith / modular / MS / SOA | `08-architecture-styles/architecture-styles.md` | — | `architecture-styles.md` | `monolith`, `modular-monolith`, `microservices-architecture`, `soa` (trim) |
| Strangler pattern | `08-architecture-styles/strangler-pattern.md` | — | `strangler-pattern.md` | `strangler-pattern.md` (trim) |
| Monolith decomposition | `08-architecture-styles/monolith-decomposition.md` | — | `monolith-decomposition.md` | — |
| Event-driven architecture | `09-microservices-patterns/event-driven-architecture.md` | `distributed-message-queue` (case) | `event-driven-architecture.md` | `event-driven-architecture.md` (trim) |
| Messaging patterns | `09-microservices-patterns/messaging-streaming.md` | `distributed-message-queue` | `messaging-and-streaming-patterns.md` | `how-to-choose-message-broker` |
| Service mesh / sidecar | `09-microservices-patterns/sidecar-and-service-mesh.md` | Interview mentions | `sidecar-and-service-mesh.md` | `service-mesh`, `sidecar-pattern` (trim) |
| Kubernetes patterns (architect) | `09-microservices-patterns/kubernetes-patterns.md` | — | `kubernetes-patterns.md` | K8s HB (primitives) |
| ADR process | `01-foundations/architecture-decision-records.md` | — | `architecture-decision-records.md` | `module-architecture-patterns` |
| Architecture review checklist | `01-foundations/architecture-review-checklist.md` | — | `architecture-review-checklist.md` | — |

**Total distinct concepts registered:** **42**

---

## 4. Duplication Report

### 4.1 Exact / Near-Exact Duplicates (Priority P0–P1)

| Concept cluster | System Design copies | Microservices canonical | Technology Playbook copies | Severity |
| :--- | :--- | :--- | :--- | :---: |
| **CAP / PACELC** | CRDT page (partial) | `cap-and-pacelc.md` | — | 7 |
| **CQRS** | 3 case studies (full sections) | `cqrs-and-event-sourcing.md` | `cqrs-pattern.md` | 9 |
| **Outbox + CDC** | 4 pages (email, hotel, stock, cdc-cache) | `outbox-and-cdc.md` | `outbox-pattern.md` | 9 |
| **Saga** | — | `saga.md` | `saga-pattern.md` | 6 |
| **Circuit breaker + bulkhead** | 10+ case studies + rate limiter | `resilience-patterns.md` | `circuit-breaker`, `bulkhead` | 8 |
| **Consistent hashing** | 8 case studies + LRU cache design | `consistent-hashing.md` | — | 8 |
| **Observability / tracing** | 15+ case studies | `observability.md` | — | 7 |
| **Caching** | 4 fundamentals + LRU case study | `caching-patterns.md` | — | 7 |
| **API Gateway / ingress** | proxy + layer4/7 pages | `api-gateway-and-bff.md` | `api-gateway`, `bff` | 7 |
| **Service mesh / sidecar** | Interview Q only | `sidecar-and-service-mesh.md` | `service-mesh`, `sidecar` | 7 |
| **Architecture styles** | — | `architecture-styles.md` | 4 architecture pages | 6 |
| **Concurrency / isolation** | `database-transactions-and-acid-isolation` | `concurrency-control.md` | — | 6 |

### 4.2 Concepts Appearing in 3+ Pages (Fragmentation)

| Concept | Page count (approx.) | Pages |
| :--- | :---: | :--- |
| Consistent hashing | 12+ | SD case studies + MS page |
| Circuit breaker | 14+ | SD designs + MS + TP |
| Observability / OpenTelemetry | 18+ | SD case studies + MS |
| CQRS | 5 | SD ×3 + MS + TP |
| Outbox | 6 | SD ×4 + MS + TP |
| Transactional patterns in interviews | 8+ | SD interview companions |

### 4.3 Safe to Keep Unique (Low Duplication)

- System Design **case studies** (application of patterns, not pattern textbooks)
- SD **networking fundamentals** (TCP, DNS, QUIC)
- SD **hands-on load balancing lab**
- MS **migration modernization** (strangler, decomposition) — unique depth
- MS **production playbook** (ADR, failure scenarios, review checklist)

---

## 5. Navigation Proposal

### 5.1 Target Hierarchy (System Design Unified Curriculum)

```
system-design/
├── 01-foundations/
├── 02-distributed-systems/
├── 03-data-management/
├── 04-communication/
├── 05-scalability/
├── 06-reliability/
├── 07-observability/
├── 08-architecture-styles/
├── 09-microservices-patterns/
├── 10-case-studies/
├── 11-interview-guide/
└── 12-learning-paths/
```

### 5.2 Sidebar Strategy (Non-Breaking Transition)

| Phase | Sidebar behavior |
| :--- | :--- |
| **Now** | `curriculum_sidebar.yaml`: SD flat groups + MS 12 modules (unchanged) |
| **Phase 1** | Add `system_design_modules.yaml`; SD sidebar reads modules; **flat slugs unchanged** |
| **Phase 3** | MS sidebar shows "Moved to System Design" stubs with links |
| **Phase 5** | `curriculum_sections.yaml`: MS → redirect landing or merge label |

### 5.3 Reading Order

1. Foundations → Distributed Systems → Data Management  
2. Communication → Scalability → Reliability → Observability  
3. Architecture Styles → Microservices Patterns  
4. Case Studies (apply patterns)  
5. Interview Guide → Learning Paths  

### 5.4 Curriculum Sections YAML (Future)

Keep `slug: system-design` as primary. Options for `microservices`:

- **Option A (recommended):** MS becomes alias hub `_index.md` only — links to SD modules  
- **Option B:** Retain MS slug as "Microservices Patterns" submodule pointing into SD `09-microservices-patterns/`  
- **Option C:** Remove MS from `curriculum_sections.yaml` after 6-month alias period  

---

## 6. Hugo Alias Plan

**Principle:** Never break existing URLs. New paths get aliases from old paths when content moves.

### 6.1 Microservices → System Design (Pattern Pages)

| Current slug | Future slug | Alias on future page |
| :--- | :--- | :--- |
| `/microservices/04-distributed-systems/cap-and-pacelc/` | `/system-design/02-distributed-systems/cap-and-pacelc/` | Yes |
| `/microservices/04-distributed-systems/consistent-hashing/` | `/system-design/02-distributed-systems/consistent-hashing/` | Yes |
| `/microservices/03-data-management/cqrs-and-event-sourcing/` | `/system-design/03-data-management/cqrs-and-event-sourcing/` | Yes |
| `/microservices/03-data-management/saga/` | `/system-design/03-data-management/saga-pattern/` | Yes |
| `/microservices/03-data-management/outbox-and-cdc/` | `/system-design/03-data-management/outbox-and-cdc/` | Yes |
| `/microservices/05-resilience-patterns/resilience-patterns/` | `/system-design/06-reliability/resilience-patterns/` | Yes |
| `/microservices/08-observability/observability/` | `/system-design/07-observability/observability/` | Yes |
| `/microservices/07-platform-patterns/sidecar-and-service-mesh/` | `/system-design/09-microservices-patterns/sidecar-and-service-mesh/` | Yes |
| `/microservices/02-service-communication/api-gateway-and-bff/` | `/system-design/04-communication/api-gateway-and-bff/` | Yes |
| `/microservices/01-architecture-styles/architecture-styles/` | `/system-design/08-architecture-styles/architecture-styles/` | Yes |
| `/microservices/11-interview-guide/top-300-microservices-questions/` | `/system-design/11-interview-guide/top-300-system-design-questions/` | Yes |

**Full alias table:** 38 MS topic paths → SD paths (see Phase B restructure plan).

### 6.2 System Design Fundamentals → Module Paths

| Current slug | Future slug | Alias |
| :--- | :--- | :--- |
| `/system-design/database-transactions-and-acid-isolation/` | `/system-design/02-distributed-systems/concurrency-control/` | Yes — merge content |
| `/system-design/cdc-based-cache-invalidation/` | `/system-design/03-data-management/outbox-and-cdc/` §cache | Yes — trim to link |
| `/system-design/application-layer-protocols-rest-grpc/` | `/system-design/04-communication/rest-vs-grpc/` | Yes |

**Case study slugs:** **No change** — `urlshortner`, `email-delivery`, etc. remain at flat paths with optional `10-case-studies/` duplicate alias only if dual-publish needed.

### 6.3 Legacy Microservices Flat Aliases (Already Exist)

30 flat aliases from Phase B MS refactor (e.g. `/microservices/circuit-breaker-pattern/` → resilience page). When migrating to SD, **chain aliases**:

```yaml
aliases:
  - /microservices/circuit-breaker-pattern/
  - /microservices/05-resilience-patterns/resilience-patterns/
```

---

## 7. Cross-Handbook Boundaries (Enforcement)

| Handbook | Owns | Must NOT duplicate in SD |
| :--- | :--- | :--- |
| **Technology Playbook** | Selection ADRs, product comparison | Pattern textbooks |
| **Kafka Handbook** | Broker internals, consumer groups | Streaming mechanics |
| **Kubernetes Handbook** | kubectl, Pods, Services | K8s primitives tutorials |
| **Database Handbook** | Outbox relay schema tuning | — |
| **Design Patterns** | Gang-of-four catalog | Production resilience ops |

---

## 8. Migration Priority Summary

| Priority | Count | Action |
| :---: | :---: | :--- |
| **P0** | 8 concepts | Establish SD canonical pages from MS; trim SD case-study deep dives to links |
| **P1** | 18 pages | Move MS modules; merge SD fundamentals |
| **P2** | 15 pages | Production playbook, interview merge |
| **P3** | 29 case studies | Add "Patterns used" links only — no moves |
| **P4** | Labs / meta | Defer |

---

**Phase A complete. No content modified. Proceed to Phase B/C planning documents.**
