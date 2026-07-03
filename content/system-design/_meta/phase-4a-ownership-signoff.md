---
title: "System Design Phase 4A — Ownership Sign-Off"
date: 2026-07-03T23:30:00+00:00
draft: true
description: "Governance sign-off — PRIMARY canonical owners and handbook roles for 52 concepts across System Design, Microservices, and Technology Playbook."
tags: ["system-design", "meta", "planning", "governance", "ownership"]
---

# Phase 4A — Ownership Sign-Off (Governance Only)

**Status:** Approved for planning  
**Scope:** Finalize PRIMARY ownership and handbook roles for all **52** concepts in [Phase 3 Concept Registry](phase-3-concept-registry.md)  
**Constraints:** No content · No file moves · No navigation · No aliases · No frontmatter · No redirects

**Effective:** Upon Phase 4B execution approval. This document is the governance contract for all future authoring and deduplication.

---

## 1. Ownership Principles

### 1.1 Role definitions

| Role | Definition | Typical handbook |
| :--- | :--- | :--- |
| **PRIMARY** | Canonical source of truth; deepest maintained explanation; owns updates when the concept evolves | Exactly **one** per concept |
| **OVERVIEW** | High-level explanation; interview framing; trade-off tables; links to PRIMARY | System Design |
| **DECISION GUIDE** | Technology or pattern **selection**; ADR-style “when to adopt”; comparison matrices | Technology Playbook |
| **REFERENCE** | Brief mention (≤2 sentences); cross-link only; no standalone deep sections | Any handbook |
| **DEEP DIVE** | Production implementation detail **under** a PRIMARY owner elsewhere; not a second PRIMARY | Microservices only (supplementary label) |
| **APPLICATION** | End-to-end design demonstrating concepts; not a pattern textbook | System Design case studies |

### 1.2 Handbook mandates

| Handbook | Mandate | Must NOT |
| :--- | :--- | :--- |
| **System Design** | Overview · interview lens · conceptual understanding · case-study application | Reproduce MS implementation playbooks; duplicate TP selection matrices |
| **Microservices** | Implementation · production architecture · operational deep dives | Replace SD interview primers; own technology product comparisons |
| **Technology Playbook** | Technology selection · trade-offs · ADR guidance | Teach pattern mechanics (delegate to MS); teach interview fundamentals (delegate to SD) |

### 1.3 PRIMARY selection rules

1. **Exactly one PRIMARY** per concept — no exceptions.
2. **No concept may have two deep-dive owners** — MS “DEEP DIVE” is permitted only when another handbook is PRIMARY.
3. **Interview preparation** is owned by **System Design** (OVERVIEW or PRIMARY as signed below).
4. **Implementation and production operations** default to **Microservices** PRIMARY when both SD and MS cover the same pattern.
5. **Technology or style selection** defaults to **Technology Playbook** DECISION GUIDE when a `how-to-choose-*` or style ADR exists.
6. **Case studies** are APPLICATION — they reference concepts but must not become PRIMARY or deep-dive owners.
7. **Planned SD pages** (Phase 2A) are signed as OVERVIEW until authored; they do not change PRIMARY ownership.

### 1.4 Role column notation

| SD Role / MS Role / TP Role | Meaning |
| :--- | :--- |
| **Primary** | This handbook is the **Canonical Owner** (PRIMARY) |
| **Overview** | SD interview/conceptual entry; links to PRIMARY |
| **Deep Dive** | MS implementation extension; PRIMARY is elsewhere |
| **Decision Guide** | TP selection ADR |
| **Reference** | Cross-link only |
| **Application** | Case-study demonstration (SD only) |
| **—** | No ownership responsibility |

---

## 2. Approved Ownership Matrix

All concepts: **Status = Approved** unless noted in §4.

### 2.1 Foundations & process

| Concept | SD Role | MS Role | TP Role | Canonical Owner | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| What is System Design | **Primary** | — | — | **System Design** | Approved |
| System design process (interview flow) | **Primary** | Reference | — | **System Design** | Approved |
| Non-functional requirements (NFRs) | Overview | Reference | Decision Guide | **System Design** | Approved |
| Capacity estimation / back-of-envelope | Overview | Reference | — | **System Design** | Approved |
| Architecture decision records (ADR) | Reference | **Primary** | Decision Guide | **Microservices** | Approved |
| Architecture review checklist (PRR) | Reference | **Primary** | — | **Microservices** | Approved |

### 2.2 Distributed systems

| Concept | SD Role | MS Role | TP Role | Canonical Owner | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| CAP theorem | Overview | **Primary** | — | **Microservices** | Approved |
| PACELC | Overview | **Primary** | — | **Microservices** | Approved |
| Consistency models | Overview | **Primary** | — | **Microservices** | Approved |
| MVCC / isolation levels | Overview | **Primary** | — | **Microservices** | Approved |
| CRDT / multi-master conflict resolution | **Primary** | Reference | — | **System Design** | Approved |
| Consistent hashing | **Primary** | Deep Dive | — | **System Design** | Approved |
| Consensus / leader election | Reference | **Primary** | — | **Microservices** | Approved |
| Distributed transactions / saga | Overview | **Primary** | Decision Guide | **Microservices** | Approved |

### 2.3 Data management

| Concept | SD Role | MS Role | TP Role | Canonical Owner | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Relational storage / B-trees | **Primary** | — | Decision Guide | **System Design** | Approved |
| Database sharding | **Primary** | Deep Dive | — | **System Design** | Approved |
| Read replicas / replication lag | **Primary** | Deep Dive | — | **System Design** | Approved |
| CDC (change data capture) | Reference | **Primary** | — | **Microservices** | Approved |
| CQRS | Overview | **Primary** | Decision Guide | **Microservices** | Approved |
| Event sourcing | Overview | **Primary** | — | **Microservices** | Approved |
| Saga pattern | Overview | **Primary** | Decision Guide | **Microservices** | Approved |
| Transactional outbox | Overview | **Primary** | Decision Guide | **Microservices** | Approved |
| Database per service | — | **Primary** | Decision Guide | **Microservices** | Approved |
| Database decomposition | — | **Primary** | — | **Microservices** | Approved |

### 2.4 Communication & ingress

| Concept | SD Role | MS Role | TP Role | Canonical Owner | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Forward / reverse proxy | **Primary** | Reference | Reference | **System Design** | Approved |
| L4 / L7 ingress routing | **Primary** | Reference | Reference | **System Design** | Approved |
| REST vs gRPC (concept) | **Primary** | Reference | Decision Guide | **System Design** | Approved |
| Load balancing algorithms | **Primary** | Reference | — | **System Design** | Approved |
| API Gateway | Overview | **Primary** | Decision Guide | **Microservices** | Approved |
| BFF (Backend for Frontend) | — | **Primary** | Decision Guide | **Microservices** | Approved |
| Service discovery | — | **Primary** | — | **Microservices** | Approved |
| Sync vs async topologies | — | **Primary** | Decision Guide | **Microservices** | Approved |
| Backpressure / flow control | Overview | **Primary** | — | **Microservices** | Approved |
| Idempotency / delivery semantics | Overview | **Primary** | — | **Microservices** | Approved |

### 2.5 Scalability & performance

| Concept | SD Role | MS Role | TP Role | Canonical Owner | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Caching hierarchy / CDN | **Primary** | Deep Dive | Decision Guide | **System Design** | Approved |
| Cache eviction policies | **Primary** | Deep Dive | — | **System Design** | Approved |
| Cache stampede / bloom filter | **Primary** | Deep Dive | — | **System Design** | Approved |
| Horizontal vs vertical scaling | Overview | **Primary** | — | **Microservices** | Approved |
| Latency vs throughput | **Primary** | Reference | — | **System Design** | Approved |
| Rate limiting / throttling | Application | **Primary** | — | **Microservices** | Approved |
| Hot key / hot partition | Reference | **Primary** | — | **Microservices** | Approved |

### 2.6 Reliability & resilience

| Concept | SD Role | MS Role | TP Role | Canonical Owner | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| SPOF elimination / redundancy | **Primary** | Reference | — | **System Design** | Approved |
| Multi-region / AZ topologies | **Primary** | Deep Dive | — | **System Design** | Approved |
| Availability / nines (uptime math) | Overview | **Primary** | — | **Microservices** | Approved |
| SLO / SLI / SLA / error budgets | Overview | **Primary** | — | **Microservices** | Approved |
| Resilience patterns (stack) | Overview | **Primary** | Decision Guide | **Microservices** | Approved |
| Circuit breaker | Reference | **Primary** | Decision Guide | **Microservices** | Approved |
| Bulkhead | Reference | **Primary** | Decision Guide | **Microservices** | Approved |
| Deployment strategies | — | **Primary** | — | **Microservices** | Approved |
| Failure scenarios / chaos | — | **Primary** | — | **Microservices** | Approved |
| Zero-downtime deployments | — | **Primary** | — | **Microservices** | Approved |

### 2.7 Observability

| Concept | SD Role | MS Role | TP Role | Canonical Owner | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Observability pillars (metrics, logs, traces) | Overview | **Primary** | — | **Microservices** | Approved |
| Distributed logging (system design) | **Application** | Deep Dive | — | **System Design** | Approved |
| Distributed tracing | Reference | **Primary** | — | **Microservices** | Approved |
| RED / USE metrics | — | **Primary** | — | **Microservices** | Approved |
| Structured logging / aggregation | Reference | **Primary** | — | **Microservices** | Approved |

### 2.8 Architecture styles & platform

| Concept | SD Role | MS Role | TP Role | Canonical Owner | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Monolith (style) | — | **Primary** | Decision Guide | **Microservices** | Approved |
| Modular monolith | — | **Primary** | Decision Guide | **Microservices** | Approved |
| Microservices (style) | — | **Primary** | Decision Guide | **Microservices** | Approved |
| SOA | — | **Primary** | Decision Guide | **Microservices** | Approved |
| Architecture styles comparison | Overview | **Primary** | Decision Guide | **Microservices** | Approved |
| Event-driven architecture | Reference | **Primary** | Decision Guide | **Microservices** | Approved |
| Messaging / streaming patterns | Application | **Primary** | Decision Guide | **Microservices** | Approved |
| Strangler fig pattern | — | **Primary** | Decision Guide | **Microservices** | Approved |
| Monolith decomposition | — | **Primary** | — | **Microservices** | Approved |
| Service mesh / sidecar | — | **Primary** | Decision Guide | **Microservices** | Approved |
| Kubernetes patterns (architect) | — | **Primary** | — | **Microservices** | Approved |

### 2.9 Networking & transport (SD-unique)

| Concept | SD Role | MS Role | TP Role | Canonical Owner | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| IP, DNS, firewalls | **Primary** | — | — | **System Design** | Approved |
| TCP vs UDP | **Primary** | — | — | **System Design** | Approved |
| HTTP/3, QUIC, WebSockets | **Primary** | — | Reference | **System Design** | Approved |
| Hands-on load balancing lab | **Primary** | — | — | **System Design** | Approved |

### 2.10 Case studies & interview

| Concept | SD Role | MS Role | TP Role | Canonical Owner | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| End-to-end system designs (27 case studies) | **Application** | — | — | **System Design** | Approved |
| Case-study interview Q&A (19 companions) | **Primary** | — | — | **System Design** | Approved |
| System design interview framework | **Primary** | Reference | — | **System Design** | Approved |
| Microservices interview corpus (Top 300 + subsets) | — | **Primary** | — | **Microservices** | Approved |
| Architect learning paths | Reference | **Primary** | — | **Microservices** | Approved |

---

## 3. Canonical Owners by Module

Summary of **PRIMARY** ownership mapped to Phase 1 System Design modules.

| SD Module | SD PRIMARY count | MS PRIMARY count | TP DECISION GUIDE count | Notes |
| :--- | :---: | :---: | :---: | :--- |
| **1 Foundations** | 4 | 2 | 1 | SD owns on-ramp; MS owns ADR + PRR checklist |
| **2 Distributed Systems** | 2 | 6 | 1 | MS owns CAP/consistency/concurrency; SD owns CRDTs + consistent hashing |
| **3 Data Management** | 3 | 7 | 4 | MS owns CQRS/saga/outbox/CDC; SD owns storage/sharding/replicas |
| **4 Communication** | 4 | 6 | 5 | SD owns transport/proxy/LB; MS owns gateway/discovery/topologies |
| **5 Scalability** | 4 | 3 | 1 | SD owns caching trilogy + latency/throughput; MS owns scale dimensions + rate limit |
| **6 Reliability** | 2 | 8 | 2 | SD owns SPOF/multi-region; MS owns SRE/resilience/deploy |
| **7 Observability** | 1 (application) | 4 | — | MS owns pillars; SD logging case study is APPLICATION |
| **8 Architecture Styles** | — | 11 | 8 | MS PRIMARY for all styles; TP owns per-style ADRs |
| **9 Case Studies** | 27 (application) | — | — | SD only |
| **10 Interview Guide** | 20 | 5 | — | Parallel corpora; different scope |

### PRIMARY owner tally (all 56 registry rows incl. sub-concepts)

| Canonical Owner | Concepts |
| :--- | :---: |
| **System Design** | **22** |
| **Microservices** | **34** |
| **Technology Playbook** | **0** *(TP never PRIMARY — selection only)* |

---

## 4. Concepts Requiring Refactoring

These are **approved ownership** but **current content violates** governance. Remediation is Phase 4B / Phase 5 — not Phase 4A.

| Concept | Violation | Current location | Target state | Phase |
| :--- | :--- | :--- | :--- | :--- |
| **CQRS** | Case studies are deep-dive owners | `proximity-search`, `hotel-booking`, `payment-gateway-orchestration`, `distributed-logging-system`, `ecommerce`, `food-delivery` | ≤2 sentences + link to MS PRIMARY; SD OVERVIEW when `cqrs-overview` exists | 4B / 5 |
| **Transactional outbox** | Case studies duplicate MS PRIMARY | `email-delivery`, `notification-system`, `hotel-booking`, `stock-broker-trading`, `ott`, `online-learning-platform` | Trim to APPLICATION; link MS `outbox-and-cdc` | 5 |
| **CDC** | SD page `cdc-based-cache-invalidation` competes with MS PRIMARY | SD fundamentals | Reframe as OVERVIEW subset linking MS PRIMARY | 4B |
| **Circuit breaker / bulkhead** | 14+ SD files embed full pattern sections | Case studies + interviews | REFERENCE only; link MS `resilience-patterns` | 5 |
| **Consistent hashing** | 11 SD pages embed ring tutorials | Case studies + LB page | REFERENCE; link SD PRIMARY `consistent-hashing` (planned) | 4B / 5 |
| **Observability / tracing** | 20+ case studies teach pillars inline | Case studies | REFERENCE; link MS `observability` + SD `observability-fundamentals` (planned) | 4B / 5 |
| **MVCC / isolation** | SD `database-transactions-and-acid-isolation` overlaps MS PRIMARY | SD Module 2 | SD becomes OVERVIEW; trim duplicate depth | 4B |
| **API Gateway** | SD proxy/ingress pages overlap MS PRIMARY boundary | `proxy-servers-*`, `layer4-layer7-*` | Clarify SD = transport layer; MS = gateway pattern | 4B |
| **Caching** | MS `caching-patterns` may duplicate SD PRIMARY fundamentals | MS production playbook | MS DEEP DIVE only; link SD 4 pages | 4B |
| **CAP / PACELC** | SD CRDT page mentions CAP without OVERVIEW page | `crdts-and-multi-master-conflict-resolution` | Add SD OVERVIEW `cap-and-pacelc` (planned); CRDT stays PRIMARY | 4B |
| **TP pattern pages** | TP teaches mechanics, not just selection | `cqrs-pattern`, `saga-pattern`, `outbox-pattern`, `circuit-breaker-pattern`, `bulkhead-pattern` | Trim to DECISION GUIDE; link MS PRIMARY + SD OVERVIEW | 4B |
| **Rate limiting** | Case study `distributed-rate-limiter` is full design (valid APPLICATION) but lacks OVERVIEW primer | SD Module 5 gap | Add SD OVERVIEW `rate-limiting-fundamentals` (P1); case study stays APPLICATION | 4B |
| **Distributed logging** | Dual role: APPLICATION case + observability confusion | `distributed-logging-system` | Label APPLICATION; distinguish from MS observability PRIMARY | 4B |

**Status key:** All rows **Approved** for ownership; refactoring **Pending** until Phase 4B.

---

## 5. Duplicate Reduction Opportunities

Ordered by Phase 3 duplication severity. Each row states the **approved end state** — no second PRIMARY.

| Priority | Concept cluster | Current duplicate count | Reduction action | Est. pages affected | PRIMARY preserved |
| :---: | :--- | :---: | :--- | :---: | :--- |
| 1 | **CQRS** | 8 | Case studies → REFERENCE; TP → DECISION GUIDE trim | 6 SD + 1 TP | Microservices |
| 2 | **Outbox + CDC** | 9 | SD CDC page → OVERVIEW; cases → REFERENCE; TP trim | 7 SD + 1 TP | Microservices |
| 3 | **Resilience / CB / bulkhead** | 16+ | SD OVERVIEW page; cases → REFERENCE; TP ADRs trim | 12+ SD + 2 TP | Microservices |
| 4 | **Consistent hashing** | 14+ | SD OVERVIEW (planned); cases → REFERENCE | 11 SD | System Design |
| 5 | **Observability / tracing** | 22+ | SD OVERVIEW (planned); cases → REFERENCE | 20 SD | Microservices |
| 6 | **Caching** | 8 | MS → DEEP DIVE label; link SD PRIMARY 4 pages | 1 MS + cases | System Design |
| 7 | **CAP / PACELC** | 3 | SD OVERVIEW (planned); CRDT → REFERENCE for CAP | 2 SD | Microservices |
| 8 | **API Gateway / ingress** | 6 | Boundary docs; SD transport vs MS gateway | 2 SD + 1 MS | Split: SD transport, MS gateway |
| 9 | **Service mesh** | 4 | TP → DECISION GUIDE only; SD interviews → REFERENCE | 2 TP + SD interviews | Microservices |
| 10 | **Architecture styles** | 6 | SD OVERVIEW hub; TP per-style ADRs; MS PRIMARY | 1 SD + 4 TP | Microservices |
| 11 | **Saga** | 4 | SD OVERVIEW (P1); cases → REFERENCE | 2 SD + 1 TP | Microservices |
| 12 | **MVCC / isolation** | 4 | SD page → OVERVIEW; MS stays PRIMARY | 1 SD | Microservices |

**Estimated duplicate reduction:** ~**120 embedded sections** → ~**25 overview pages + cross-links** (13 P0 + 12 P1 overviews).

---

## 6. Governance Rules

### 6.1 Authoring

| # | Rule |
| :---: | :--- |
| G1 | Every new page must map to one concept in this matrix before merge. |
| G2 | A handbook may not publish a **new** deep-dive section for a concept where it is not **PRIMARY** or **DEEP DIVE** (MS only). |
| G3 | **Technology Playbook** pages must not exceed **40%** pattern-mechanics prose — remainder links to MS PRIMARY. |
| G4 | **System Design** OVERVIEW pages target **800–1,200 words**; link to PRIMARY within first 3 screens. |
| G5 | **System Design** case studies: pattern sections **≤ 2 sentences** + link (after Phase 5). |
| G6 | **Microservices** PRIMARY pages include an “SD Overview” link in Architect Notes when SD OVERVIEW exists or is planned. |
| G7 | **Planned** SD OVERVIEW slugs (Phase 2A) are reserved — no other handbook may claim PRIMARY for those interview entry points. |

### 6.2 Cross-linking

| # | Rule |
| :---: | :--- |
| G8 | OVERVIEW → PRIMARY link is **mandatory** (both directions when both pages exist). |
| G9 | DECISION GUIDE → OVERVIEW → PRIMARY is the required reader path from TP. |
| G10 | APPLICATION (case studies) → OVERVIEW (if exists) → PRIMARY (if reader needs depth). |
| G11 | No circular PRIMARY claims — if conflict, this document’s §2 matrix wins. |

### 6.3 Change control

| # | Rule |
| :---: | :--- |
| G12 | Changing PRIMARY ownership requires updating this document and explicit architect approval. |
| G13 | Phase 4B implements links and trims; Phase 5 implements case-study dedup — neither changes PRIMARY without G12. |
| G14 | Microservices remains an **independent** handbook — no merge into System Design. |
| G15 | No URL changes, aliases, or redirects as part of governance sign-off (Phase 4A). |

### 6.4 PRIMARY quick-reference

| If the concept is… | PRIMARY is… |
| :--- | :--- |
| Interview on-ramp, networking, caching fundamentals, CRDTs, consistent hashing, latency/throughput, SPOF, multi-region, case studies | **System Design** |
| CAP, CQRS, saga, outbox, resilience, observability, gateway, mesh, styles, migration, production ops | **Microservices** |
| Which database / cache / broker / protocol / architecture style to adopt | **Technology Playbook** (DECISION GUIDE only) |

---

## Sign-Off Summary

| Item | Value |
| :--- | :--- |
| Concepts signed | **56** (52 Phase 3 + 4 interview/path rows) |
| PRIMARY: System Design | **22** |
| PRIMARY: Microservices | **34** |
| PRIMARY: Technology Playbook | **0** (by design) |
| Concepts pending content refactor | **13** |
| Duplicate clusters queued for reduction | **12** |

---

## Explicit Non-Actions (Phase 4A)

| Action | Status |
| :--- | :---: |
| Create or edit content | ❌ |
| Move / rename files | ❌ |
| Modify navigation YAML | ❌ |
| Create aliases or redirects | ❌ |
| Modify frontmatter | ❌ |

---

## Next Step

**Phase 4B (awaiting approval):** Implement cross-links, OVERVIEW page authoring (Phase 2A waves), TP ADR trims, and content refactors per §4 — still **no URL changes** unless explicitly scoped.

**Do not proceed to Phase 4B without explicit approval.**
