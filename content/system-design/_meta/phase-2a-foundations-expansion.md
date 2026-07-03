---
title: "System Design Phase 2A — Foundations Expansion Plan"
date: 2026-07-03T22:30:00+00:00
draft: true
description: "P0 gap expansion plan — per-topic strategy, reuse sources, implementation waves, and page/link estimates. Planning only."
tags: ["system-design", "meta", "planning", "foundations", "p0"]
---

# Phase 2A — Foundations Expansion Plan (P0 Only)

**Status:** Planning complete  
**Scope:** All **14 P0** gaps from [Phase 2 Gap Analysis](phase-2-gap-analysis.md)  
**Constraints:** No content created · No file moves · No aliases · No navigation YAML changes

---

## Strategy Legend

| Code | Meaning | When to use |
| :---: | :--- | :--- |
| **A** | New canonical System Design page | No adequate reuse source; SD must own the concept |
| **B** | Reuse from Microservices only | Link to MS as primary; **no** new SD page (not recommended for P0 — breaks SD learning path) |
| **C** | Reuse from Technology Playbook only | Link to TP as primary; **no** new SD page (not recommended for P0) |
| **D** | Create SD summary page + deep-dive link | **Default for P0** — SD overview + interview lens; MS/TP own depth |

**Phase 2A recommendation:** Use **D** for 11 topics, **A** for 3 topics with no external primer. Never use **B** or **C** alone for P0 — architects entering via System Design need an in-curriculum entry point.

---

## P0 Topic Register

### Wave 1 — Foundations (Module 1)

| Topic | Why Missing | Target Module | New Page Required | Reuse Existing Content | Source Handbook | Strategy |
| :--- | :--- | :--- | :---: | :--- | :--- | :---: |
| **What is System Design** | `_index.md` is 9 lines; no scope, constraints, or deliverables defined for the curriculum | 1 Foundations | **Yes** — `what-is-system-design` | None (greenfield) | — | **A** |
| **System Design Process** | No structured flow (requirements → HLD → components → trade-offs → deep dive); case studies jump straight to solutions | 1 Foundations | **Yes** — `system-design-process` | Partial patterns in every case study §1–§3; MS `architecture-decision-records` (ADR format only) | MS (partial) | **A** |
| **Non-Functional Requirements (NFRs)** | Case studies assume NFR literacy (latency, throughput, durability) without defining categories or how to elicit them | 1 Foundations | **Yes** — `non-functional-requirements` | MS `10-production-playbook/architecture-review-checklist` (PRR NFR checklist); case study requirement tables (e.g. `urlshortner` §1) | MS + SD case studies | **D** |
| **Capacity Estimation & Back-of-Envelope** | Math is embedded in §9 of 25+ case studies; no standalone primer teaching DAU→QPS→storage→bandwidth | 1 Foundations | **Yes** — `capacity-estimation` | SD `urlshortner` (canonical BOE walkthrough); any case study §"Traffic Estimates" / §9 | SD (extract patterns) | **D** |

#### Wave 1 — Per-topic detail

**What is System Design**

| Field | Value |
| :--- | :--- |
| Target Module | `1 Foundations` |
| Reuse | — |
| Strategy | **A** — New canonical SD page |
| SD page outline | Definition · SD vs architecture vs detailed design · constraints (scale, budget, team) · deliverables (diagram, APIs, data model, bottlenecks) · link to case studies |
| Deep-dive links | MS `12-learning-paths/architect-path` (progression only) |
| Cross-links out | 2 (case studies index, system-design-process) |

---

**System Design Process**

| Field | Value |
| :--- | :--- |
| Target Module | `1 Foundations` |
| Reuse | MS `10-production-playbook/architecture-decision-records` (ADR section only) |
| Strategy | **A** — New canonical SD page |
| SD page outline | 45-min interview timeline · Step 1 requirements · Step 2 capacity · Step 3 API/data model · Step 4 HLD diagram · Step 5 deep dives · Step 6 trade-offs · anti-patterns |
| Deep-dive links | MS ADRs · SD `capacity-estimation` · SD `non-functional-requirements` |
| Cross-links out | 4 |

---

**Non-Functional Requirements (NFRs)**

| Field | Value |
| :--- | :--- |
| Target Module | `1 Foundations` |
| Reuse | MS `architecture-review-checklist` · SD `urlshortner` requirements table |
| Strategy | **D** — Summary + deep dive |
| SD page outline | Functional vs non-functional · Categories (performance, availability, reliability, scalability, consistency, security, operability, cost) · How to prioritize · mapping NFRs → architecture choices |
| Deep-dive links | MS `architecture-review-checklist` · MS `reliability-engineering` (SLO section) · TP `module-architecture-patterns` |
| Cross-links out | 5 |

---

**Capacity Estimation & Back-of-Envelope**

| Field | Value |
| :--- | :--- |
| Target Module | `1 Foundations` |
| Reuse | SD `urlshortner` §Traffic Estimates + §9 Capacity Planning (canonical example) |
| Strategy | **D** — Summary + deep dive |
| SD page outline | Powers of 2 · DAU/MAU → QPS · read/write ratio · storage growth · bandwidth · cache sizing · "good enough" precision · worked example (URL shortener) |
| Deep-dive links | SD `urlshortner` (full walkthrough) · MS `scalability-patterns` (hot-key section) |
| Cross-links out | 4 |

---

### Wave 2 — Distributed Systems (Module 2)

| Topic | Why Missing | Target Module | New Page Required | Reuse Existing Content | Source Handbook | Strategy |
| :--- | :--- | :--- | :---: | :--- | :--- | :---: |
| **CAP Theorem** | CRDT page mentions CAP in passing; no SD interview-level treatment | 2 Distributed Systems | **Yes** — merge with PACELC → `cap-and-pacelc` | MS `04-distributed-systems/cap-and-pacelc` | MS | **D** |
| **PACELC** | Same as CAP — no SD entry; MS owns combined page | 2 Distributed Systems | **Merged** into `cap-and-pacelc` (not a separate page) | MS `04-distributed-systems/cap-and-pacelc` | MS | **D** |
| **Consistency Models** | Strong/eventual/causal scattered across 15+ case studies; no comparison table in fundamentals | 2 Distributed Systems | **Yes** — `consistency-models` | MS `cap-and-pacelc` · MS `concurrency-control` · SD `database-transactions-and-acid-isolation` · SD `crdts-and-multi-master-conflict-resolution` | MS + SD | **D** |
| **Consistent Hashing** | LB page mentions hashing skew; 10+ case studies embed ring logic without fundamentals entry | 2 Distributed Systems | **Yes** — `consistent-hashing` | MS `04-distributed-systems/consistent-hashing` · SD `load-balancers-and-routing-algorithms` (skew) · SD `database-sharding-provisioning-and-chunk-routing` | MS + SD | **D** |

#### Wave 2 — Per-topic detail

**CAP Theorem + PACELC** *(consolidated — one SD page)*

| Field | Value |
| :--- | :--- |
| Target Module | `2 Distributed Systems` |
| Reuse | MS `04-distributed-systems/cap-and-pacelc` |
| Strategy | **D** — Summary + deep dive |
| SD page outline | CAP during partition (CP vs AP) · common misconceptions · PACELC in normal operation · when to pick C vs A vs L · interview one-liners · datastore examples (not engine deep dives) |
| Deep-dive links | MS `cap-and-pacelc` (canonical) · SD `consistency-models` · SD `crdts-and-multi-master-conflict-resolution` |
| Cross-links out | 4 |
| **Consolidation note** | Treat CAP and PACELC as **one** SD page to avoid duplication; matches MS structure |

---

**Consistency Models**

| Field | Value |
| :--- | :--- |
| Target Module | `2 Distributed Systems` |
| Reuse | MS `concurrency-control` · SD `database-transactions-and-acid-isolation` |
| Strategy | **D** — Summary + deep dive |
| SD page outline | Strong · sequential · causal · eventual · read-your-writes · monotonic reads · comparison table · client-visible anomalies · pick model by use case |
| Deep-dive links | MS `concurrency-control` · MS `cap-and-pacelc` · SD `replication-lag-read-replica-topology` |
| Cross-links out | 5 |

---

**Consistent Hashing**

| Field | Value |
| :--- | :--- |
| Target Module | `2 Distributed Systems` |
| Reuse | MS `consistent-hashing` |
| Strategy | **D** — Summary + deep dive |
| SD page outline | Problem (modulo N) · hash ring · virtual nodes · minimal key migration · hot spots · use cases (cache, shard routing, rate limiter) |
| Deep-dive links | MS `consistent-hashing` · SD `distributed-kv-store` · SD `distributed-lru-cache` · SD `distributed-rate-limiter` |
| Cross-links out | 5 |

---

### Wave 3 — Architecture Styles (Module 8)

| Topic | Why Missing | Target Module | New Page Required | Reuse Existing Content | Source Handbook | Strategy |
| :--- | :--- | :--- | :---: | :--- | :--- | :---: |
| **Architecture Styles Overview** | Module 8 is **empty**; no SD comparison of monolith, modular monolith, microservices, SOA, event-driven | 8 Architecture Styles | **Yes** — `architecture-styles-overview` | MS `01-architecture-styles/architecture-styles` · TP `monolith-architecture` · TP `modular-monolith-architecture` · TP `microservices-architecture` · TP `soa-architecture` · TP `event-driven-architecture` · TP `module-architecture-patterns` | MS + TP | **D** |

#### Wave 3 — Per-topic detail

**Architecture Styles Overview**

| Field | Value |
| :--- | :--- |
| Target Module | `8 Architecture Styles` |
| Reuse | MS `architecture-styles` (primary deep dive) · TP style ADRs (selection lens) |
| Strategy | **D** — Summary + deep dive |
| SD page outline | Style comparison matrix (team size, consistency, deploy independence, ops tax) · decomposition triggers · Conway's Law · when **not** to microservice · interview framing |
| Deep-dive links | MS `architecture-styles` · TP `monolith-architecture` · TP `microservices-architecture` · TP `modular-monolith-architecture` · TP `soa-architecture` · TP `event-driven-architecture` |
| Cross-links out | 7 |

---

### Wave 4 — Reliability, Observability & Scalability (Modules 5, 6, 7)

| Topic | Why Missing | Target Module | New Page Required | Reuse Existing Content | Source Handbook | Strategy |
| :--- | :--- | :--- | :---: | :--- | :--- | :---: |
| **Availability** (nines, uptime math) | SLO tables in case studies without defining availability or calculating nines | 6 Reliability | **Yes** — `availability-and-nines` | SD `multi-region-topologies-and-availability-zones` · SD `single-point-of-failure-elimination-redundancy` · MS `reliability-engineering` (partial) · MS `failure-scenarios` | SD + MS | **D** |
| **Resilience Patterns Overview** | Circuit breaker, bulkhead, retry embedded in case studies; no SD pattern catalog | 6 Reliability | **Yes** — `resilience-patterns-overview` | MS `05-resilience-patterns/resilience-patterns` · TP `circuit-breaker-pattern` · TP `bulkhead-pattern` | MS + TP | **D** |
| **Observability Pillars** | Only logging *case study* in SD; no metrics/logs/traces primer | 7 Observability | **Yes** — `observability-fundamentals` | MS `08-observability/observability` · SD `distributed-logging-system` (contrast: logging ≠ full observability) | MS + SD | **D** |
| **Horizontal vs Vertical Scaling** | Mentioned in 10+ pages; no dedicated comparison or when-to-use | 5 Scalability | **Yes** — `horizontal-vs-vertical-scaling` | MS `10-production-playbook/scalability-patterns` · SD `replication-lag-read-replica-topology` · SD `database-sharding-provisioning-and-chunk-routing` | MS + SD | **D** |
| **Latency vs Throughput** | Critical interview trade-off; almost no dedicated treatment anywhere | 5 Scalability | **Yes** — `latency-vs-throughput` | MS `scalability-patterns` (tangential) · SD `transport-layer-mechanics-tcp-vs-udp` (TCP windows) · case study SLO tables | SD + MS (partial) | **A** |

#### Wave 4 — Per-topic detail

**Availability (nines & uptime math)**

| Field | Value |
| :--- | :--- |
| Target Module | `6 Reliability` |
| Reuse | SD `single-point-of-failure-elimination-redundancy` · SD `multi-region-topologies-and-availability-zones` |
| Strategy | **D** — Summary + deep dive |
| SD page outline | Availability definition · downtime budget · 99.9 vs 99.99 vs 99.999 · serial vs parallel components · dependency availability multiplication · link to redundancy patterns |
| Deep-dive links | MS `reliability-engineering` · MS `failure-scenarios` · SD SPOF page · SD multi-region page |
| Cross-links out | 5 |

---

**Resilience Patterns Overview**

| Field | Value |
| :--- | :--- |
| Target Module | `6 Reliability` |
| Reuse | MS `resilience-patterns` |
| Strategy | **D** — Summary + deep dive |
| SD page outline | Pattern stack (timeout → bulkhead → breaker → fallback → retry) · state machine sketch · when retry is safe · interview examples from payment/search cases |
| Deep-dive links | MS `resilience-patterns` · TP `circuit-breaker-pattern` · TP `bulkhead-pattern` · SD `payment-gateway-orchestration` · SD `linkedin-job-search` |
| Cross-links out | 6 |

---

**Observability Pillars**

| Field | Value |
| :--- | :--- |
| Target Module | `7 Observability` |
| Reuse | MS `observability` |
| Strategy | **D** — Summary + deep dive |
| SD page outline | Metrics · logs · traces · RED/USE · correlation IDs · sampling · alerting loop · logging case study as applied example |
| Deep-dive links | MS `observability` · SD `distributed-logging-system` · Kafka HB (streaming metrics — link only) |
| Cross-links out | 4 |

---

**Horizontal vs Vertical Scaling**

| Field | Value |
| :--- | :--- |
| Target Module | `5 Scalability` |
| Reuse | MS `scalability-patterns` |
| Strategy | **D** — Summary + deep dive |
| SD page outline | Scale-up vs scale-out · stateless vs stateful tiers · DB vertical limits · when sharding beats bigger machine · cost curve · interview traps |
| Deep-dive links | MS `scalability-patterns` · SD `replication-lag-read-replica-topology` · SD `database-sharding-provisioning-and-chunk-routing` · SD `caching-and-cdns-hierarchical-arrays` |
| Cross-links out | 5 |

---

**Latency vs Throughput**

| Field | Value |
| :--- | :--- |
| Target Module | `5 Scalability` |
| Reuse | No single canonical page in MS or TP |
| Strategy | **A** — New canonical SD page (SD must own this interview staple) |
| SD page outline | Definitions · inverse relationship under fixed resources · tail latency (p99) · batching trade-off · Little's Law intro · queueing · when to optimize which · case study references |
| Deep-dive links | MS `scalability-patterns` (hot path) · SD `load-balancers-and-routing-algorithms` · SD `transport-layer-mechanics-tcp-vs-udp` |
| Cross-links out | 4 |

---

## Strategy Summary (All P0)

| Strategy | Topics | Count |
| :---: | :--- | :---: |
| **A** — New canonical SD page | What is SD, System Design Process, Latency vs Throughput | **3** |
| **D** — Summary + deep-dive link | NFRs, Capacity Estimation, CAP+PACELC, Consistency Models, Consistent Hashing, Architecture Styles, Availability, Resilience, Observability, Horizontal vs Vertical | **10** |
| **B** — MS reuse only | — | **0** |
| **C** — TP reuse only | — | **0** |

*CAP and PACELC count as one consolidated topic (one new page).*

---

## Page & Link Estimates

### New System Design pages

| Wave | Module(s) | New Pages | Slugs |
| :---: | :--- | :---: | :--- |
| **Wave 1** | 1 Foundations | **4** | `what-is-system-design`, `system-design-process`, `non-functional-requirements`, `capacity-estimation` |
| **Wave 2** | 2 Distributed Systems | **3** | `cap-and-pacelc`, `consistency-models`, `consistent-hashing` |
| **Wave 3** | 8 Architecture Styles | **1** | `architecture-styles-overview` |
| **Wave 4** | 5, 6, 7 | **5** | `horizontal-vs-vertical-scaling`, `latency-vs-throughput`, `availability-and-nines`, `resilience-patterns-overview`, `observability-fundamentals` |
| **Total** | | **13** | *(14 P0 topics → 13 pages after CAP/PACELC merge)* |

### Reusable pages (link targets — not copied)

| Handbook | Pages referenced | Count |
| :--- | :--- | :---: |
| **Microservices** | `cap-and-pacelc`, `consistent-hashing`, `concurrency-control`, `architecture-styles`, `resilience-patterns`, `observability`, `scalability-patterns`, `architecture-review-checklist`, `reliability-engineering`, `failure-scenarios`, `architecture-decision-records` | **11** |
| **Technology Playbook** | `monolith-architecture`, `modular-monolith-architecture`, `microservices-architecture`, `soa-architecture`, `event-driven-architecture`, `circuit-breaker-pattern`, `bulkhead-pattern`, `module-architecture-patterns` | **8** |
| **System Design (existing)** | `urlshortner`, `database-transactions-and-acid-isolation`, `crdts-and-multi-master-conflict-resolution`, `replication-lag-read-replica-topology`, `database-sharding-provisioning-and-chunk-routing`, `single-point-of-failure-elimination-redundancy`, `multi-region-topologies-and-availability-zones`, `distributed-logging-system`, `load-balancers-and-routing-algorithms`, `transport-layer-mechanics-tcp-vs-udp`, `caching-and-cdns-hierarchical-arrays`, case studies (payment-gateway, linkedin-job-search, distributed-kv-store, distributed-lru-cache, distributed-rate-limiter) | **15+** |
| **Total unique reuse targets** | | **~30** |

### Cross-link estimates

| Link type | Estimated count | Notes |
| :--- | :---: | :--- |
| SD new page → MS deep dive | **~22** | ~1.7 MS links per D-strategy page |
| SD new page → TP ADR | **~10** | Architecture styles + resilience pages |
| SD new page → existing SD page | **~25** | Case studies + fundamentals |
| SD new page → SD new page (intra-wave) | **~8** | e.g. process → NFRs → capacity |
| **Total outbound cross-links** | **~65** | Across 13 new pages (~5 per page avg) |
| Inbound links (future) | **~40** | Case studies linking back after Phase 5 dedup (not in 2A scope) |

---

## Implementation Waves (Recommended)

### Wave 1 — Foundations

**Goal:** Unlock the architect on-ramp before any distributed-systems theory.

| Order | Slug | Strategy | Depends on |
| :---: | :--- | :---: | :--- |
| 1.1 | `what-is-system-design` | A | — |
| 1.2 | `system-design-process` | A | 1.1 |
| 1.3 | `non-functional-requirements` | D | 1.1 |
| 1.4 | `capacity-estimation` | D | 1.2, 1.3 |

**Exit criteria:** Reader can start any case study with shared vocabulary for requirements and BOE math.

**Navigation impact (future):** Prepend 4 slugs to Module 1 in `system_design_modules.yaml` — not executed in 2A.

---

### Wave 2 — Distributed Systems

**Goal:** Core distributed trade-offs before data-sharding and case-study pattern depth.

| Order | Slug | Strategy | Depends on |
| :---: | :--- | :---: | :--- |
| 2.1 | `cap-and-pacelc` | D | Wave 1 NFRs |
| 2.2 | `consistency-models` | D | 2.1 |
| 2.3 | `consistent-hashing` | D | Wave 1 capacity |

**Exit criteria:** Reader understands CP/AP, consistency spectrum, and hash-ring routing before KV cache / rate limiter case studies.

---

### Wave 3 — Architecture Styles

**Goal:** Fill the empty Module 8 slot; frame *how* to structure systems before style-specific case studies.

| Order | Slug | Strategy | Depends on |
| :---: | :--- | :---: | :--- |
| 3.1 | `architecture-styles-overview` | D | Wave 1 process |

**Exit criteria:** Reader can justify monolith vs microservices in an interview without opening MS playbook.

---

### Wave 4 — Reliability, Observability & Scalability

**Goal:** Production operability primitives — availability math, resilience catalog, observability pillars, scaling dimensions.

| Order | Slug | Module | Strategy | Depends on |
| :---: | :--- | :---: | :---: | :--- |
| 4.1 | `latency-vs-throughput` | 5 Scalability | A | Wave 1 NFRs |
| 4.2 | `horizontal-vs-vertical-scaling` | 5 Scalability | D | 4.1 |
| 4.3 | `availability-and-nines` | 6 Reliability | D | Wave 1 NFRs |
| 4.4 | `resilience-patterns-overview` | 6 Reliability | D | 4.3 |
| 4.5 | `observability-fundamentals` | 7 Observability | D | 4.4 |

**Exit criteria:** Modules 5–7 have interview-ready entry pages; logging case study contextualized as one observability implementation.

---

## SD Page Template (for implementation phase)

All **D**-strategy pages should follow a consistent **System Design Overview** template (~800–1,200 words):

1. **One-paragraph definition** (interview answer)
2. **When it matters** (symptoms / triggers)
3. **Comparison table** (trade-offs)
4. **Worked example** (small, not a full case study)
5. **Common mistakes** (interview traps)
6. **Deep dive** — single prominent link block to MS canonical page
7. **Related** — 2–3 SD fundamentals or case studies
8. **Selection ADR** (optional) — link to TP when adoption decision is relevant

**A**-strategy pages (What is SD, Process, Latency vs Throughput) may run longer (~1,500–2,000 words) — SD owns the concept.

---

## Explicit Non-Actions (Phase 2A)

| Action | Status |
| :--- | :---: |
| Create `.md` content files | ❌ Not done |
| Modify `system_design_modules.yaml` | ❌ Not done |
| Modify `system_design_order.yaml` | ❌ Not done |
| Create Hugo aliases | ❌ Not done |
| Copy MS/TP body text into SD | ❌ Prohibited |
| Merge Microservices into System Design | ❌ Out of scope |

---

## Relationship to Later Phases

| Phase | Relationship to 2A |
| :--- | :--- |
| **Phase 2** (complete) | Identified 14 P0 gaps — 2A plans their resolution |
| **Phase 3** (next) | Concept registry — confirm MS/TP remain deep-dive owners for D-strategy topics |
| **Phase 4** | Ownership sign-off — A vs D strategy per concept |
| **Phase 5** | Case study dedup — add inbound links from 25+ designs to these 13 new pages |

---

## Exit Criteria — Phase 2A

| Criterion | Status |
| :--- | :---: |
| Every P0 topic analyzed | ✅ |
| Target module assigned | ✅ |
| Strategy A/B/C/D recommended | ✅ |
| Reuse sources documented | ✅ |
| New page count estimated (13) | ✅ |
| Reusable page count estimated (~30) | ✅ |
| Cross-link count estimated (~65 outbound) | ✅ |
| Four implementation waves defined | ✅ |
| No content or navigation changes | ✅ |

**Do not proceed to content authoring or navigation updates without explicit approval.**
