---
title: "System Design Phase 4B — Implementation Roadmap"
date: 2026-07-04T00:00:00+00:00
draft: true
description: "Executable implementation plan — seven waves, page estimates, cross-links, duplicate cleanup, risks, and coverage targets. Planning only."
tags: ["system-design", "meta", "planning", "implementation", "roadmap"]
---

# Phase 4B — Implementation Roadmap (Planning Only)

**Status:** Ready for execution approval  
**Governance:** [Phase 4A Ownership Sign-Off](phase-4a-ownership-signoff.md) (approved)  
**Inputs:** [Phase 2A Expansion Plan](phase-2a-foundations-expansion.md) · [Phase 3 Concept Registry](phase-3-concept-registry.md) · [Phase 1 Navigation](phase-1-navigation.md)

**Constraints (this document):** Planning only — no content, file moves, renames, navigation YAML changes, aliases, or markdown page generation.

---

## Executive Overview

| Metric | Value |
| :--- | :---: |
| **Implementation waves** | 7 |
| **New SD pages (total)** | **18** |
| **Existing pages updated (total)** | **~55** |
| **Cross-links added (total)** | **~110** |
| **Duplicate sections removed (Wave 7)** | **~95** |
| **Estimated effort** | **28–38 person-days** |
| **Curriculum coverage lift** | 19 fundamentals → **37** (+95%) |

---

## Effort Scale

| Label | Meaning |
| :--- | :--- |
| **S** | 0.5 day — link-only update or light trim |
| **M** | 1 day — new OVERVIEW page (~1,000 words) or moderate refactor |
| **L** | 1.5–2 days — new PRIMARY page (~1,800 words) or multi-section case study trim |
| **XL** | 2–3 days — wave with 4+ new pages + YAML + MS/TP back-links |

---

## Wave 1 — Foundations

### Goal

Establish the System Design on-ramp: scope, interview process, NFR vocabulary, and back-of-envelope math — before any case study or distributed-systems theory.

### Scope

| In scope | Out of scope |
| :--- | :--- |
| 4 new SD PRIMARY/OVERVIEW pages | Networking fundamentals (already exist) |
| `_index.md` pointer update | MS ADR content rewrite |
| Navigation YAML prepend (Module 1) | Interview companion content rewrites |
| Cross-links to MS PRR + TP module patterns | |

### New Pages (4)

| Slug | Module | Owner role | Strategy | Effort |
| :--- | :---: | :--- | :--- | :---: |
| `what-is-system-design` | 1 Foundations | SD **Primary** | A | M |
| `system-design-process` | 1 Foundations | SD **Primary** | A | L |
| `non-functional-requirements` | 1 Foundations | SD **Primary** (overview) | D | M |
| `capacity-estimation` | 1 Foundations | SD **Primary** (overview) | D | M |

### Existing Pages Updated (5)

| Page | Change |
| :--- | :--- |
| `content/system-design/_index.md` | Replace minimal body with curriculum map + links to 4 new pages |
| `networking-essentials-ip-dns-firewalls` | Add “Prerequisites” link to `what-is-system-design` |
| `urlshortner` | Add inbound link from `capacity-estimation` (canonical BOE example) |
| `data/system_design_modules.yaml` | Prepend 4 slugs to Module 1 |
| `data/system_design_order.yaml` | Insert 4 slugs at start of topic list |

### Cross-links Added (18)

| From | To | Count |
| :--- | :--- | :---: |
| `what-is-system-design` | `system-design-process`, case studies index, Module 9 slugs (sample) | 4 |
| `system-design-process` | `non-functional-requirements`, `capacity-estimation`, MS `architecture-decision-records` | 4 |
| `non-functional-requirements` | MS `architecture-review-checklist`, MS `reliability-engineering`, TP `module-architecture-patterns` | 3 |
| `capacity-estimation` | `urlshortner`, MS `scalability-patterns` | 2 |
| MS `architecture-decision-records` | `system-design-process` (back-link) | 1 |
| `_index.md` | All 4 new pages | 4 |

### Interview Companion References

Add **“Interview prep”** block on `system-design-process` and `capacity-estimation`:

| Companion | Why |
| :--- | :--- |
| `distributed-rate-limiter-interview-questions` | BOE + QPS math |
| `urlshortner` (case study, not companion) | Canonical capacity walkthrough |
| `payment-gateway-orchestration-interview-questions` | NFR / SLA framing |
| `linkedin-job-search-interview-questions` | Latency SLO + trade-offs |

No changes to companion file bodies in Wave 1 — links only.

### Duplicate Sections Removed

**0** — greenfield pages.

### Estimated Effort

**5–6 person-days** (4 new pages + YAML + index + MS back-link)

### Exit Criteria

- [ ] Module 1 sidebar shows 8 topics (4 new + 4 existing)
- [ ] Reader can start any case study after reading Wave 1 sequence
- [ ] `hugo --minify` passes; all 4 slugs resolve

---

## Wave 2 — Distributed Systems

### Goal

Deliver interview-ready distributed trade-offs (CAP/PACELC, consistency spectrum, consistent hashing) with MS as PRIMARY deep dive.

### Scope

3 new OVERVIEW pages; trim overlap on 2 existing SD fundamentals; MS back-links on 3 PRIMARY pages.

### New Pages (3)

| Slug | Module | MS PRIMARY link | Effort |
| :--- | :---: | :--- | :---: |
| `cap-and-pacelc` | 2 Distributed Systems | `04-distributed-systems/cap-and-pacelc` | M |
| `consistency-models` | 2 Distributed Systems | `concurrency-control`, `cap-and-pacelc` | M |
| `consistent-hashing` | 2 Distributed Systems | `consistent-hashing` | M |

### Existing Pages Updated (6)

| Page | Change |
| :--- | :--- |
| `crdts-and-multi-master-conflict-resolution` | Trim CAP prose → ≤2 sentences + link `cap-and-pacelc` |
| `database-transactions-and-acid-isolation` | Reframe as OVERVIEW; link MS `concurrency-control` |
| `load-balancers-and-routing-algorithms` | Hash-skew section → link `consistent-hashing` |
| `database-sharding-provisioning-and-chunk-routing` | Shard routing → link `consistent-hashing` |
| `system_design_modules.yaml` | Prepend 3 slugs to Module 2 |
| `system_design_order.yaml` | Insert after Wave 1 block |

### Cross-links Added (16)

| From | To | Count |
| :--- | :--- | :---: |
| New pages (3) | MS deep dives (5 links) | 5 |
| New pages | SD `crdts-*`, `database-transactions-*`, case studies (`distributed-kv-store`, `distributed-lru-cache`, `distributed-rate-limiter`) | 6 |
| MS `cap-and-pacelc` | SD `cap-and-pacelc`, `crdts-*` | 2 |
| MS `consistent-hashing` | SD `consistent-hashing`, `distributed-kv-store` | 2 |
| MS `concurrency-control` | SD `consistency-models`, `database-transactions-*` | 2 |

### Duplicate Sections Removed

| Location | Sections | Strategy |
| :--- | :---: | :--- |
| `crdts-and-multi-master-conflict-resolution` | 1 CAP explainer block | Replace with link |
| `database-transactions-and-acid-isolation` | ~2 isolation deep-dive subsections | Trim to OVERVIEW depth |

**Total: ~3 sections**

### Estimated Effort

**4–5 person-days**

### Exit Criteria

- [ ] KV store / LRU cache / rate limiter case studies link to `consistent-hashing` before deep read
- [ ] CAP interview answer lives on SD; MS owns extended framework

---

## Wave 3 — Architecture Styles

### Goal

Fill empty Module 8 with a single comparison hub covering monolith, modular monolith, SOA, microservices, and event-driven architecture — linking TP decision ADRs and MS PRIMARY.

### Scope

1 new OVERVIEW page with **architecture comparison matrix**; TP + MS back-links; no new per-style SD pages (styles are rows in the matrix, not separate slugs).

### New Pages (1)

| Slug | Module | Contents | Effort |
| :--- | :---: | :--- | :---: |
| `architecture-styles-overview` | 8 Architecture Styles | 5×5 comparison matrix (team size, consistency, deploy independence, ops tax, when to use) + interview framing | L |

### Matrix rows (in-page, not separate files)

| Style | TP Decision Guide | MS PRIMARY |
| :--- | :--- | :--- |
| Monolith | `monolith-architecture` | `architecture-styles` §monolith |
| Modular monolith | `modular-monolith-architecture` | `architecture-styles` §modular |
| SOA | `soa-architecture` | `architecture-styles` §SOA |
| Microservices | `microservices-architecture` | `architecture-styles` §microservices |
| Event-driven architecture | `event-driven-architecture` | `event-driven-architecture` |

### Existing Pages Updated (8)

| Page | Change |
| :--- | :--- |
| `system_design_modules.yaml` | Add `architecture-styles-overview` to Module 8 |
| `system_design_order.yaml` | Insert in Module 8 position |
| MS `01-architecture-styles/architecture-styles` | Architect Notes → SD overview |
| MS `06-event-driven/event-driven-architecture` | Link SD overview + TP ADR |
| TP `monolith-architecture` | Trim mechanics → link SD + MS |
| TP `microservices-architecture` | Trim mechanics → link SD + MS |
| TP `soa-architecture` | Trim mechanics → link SD + MS |
| TP `modular-monolith-architecture` | Trim mechanics → link SD + MS |

### Cross-links Added (14)

| From | To | Count |
| :--- | :--- | :---: |
| `architecture-styles-overview` | 4 TP style ADRs + MS `architecture-styles` + MS `event-driven-architecture` + SD `distributed-message-queue` case | 7 |
| TP style pages (4) | SD overview + MS PRIMARY | 4 |
| MS `architecture-styles` | SD overview | 1 |
| `system-design-process` | `architecture-styles-overview` | 1 |
| TP `event-driven-architecture` | SD overview + MS EDA | 1 |

### Duplicate Sections Removed

**0** in SD (no prior Module 8 content). TP trim deferred partial prose reduction (~4 sections across 4 TP pages) — counted in updated pages, not as SD duplicate removal.

### Estimated Effort

**3–4 person-days**

### Exit Criteria

- [ ] Module 8 sidebar no longer empty
- [ ] Interview question “monolith vs microservices” answerable from SD page alone

---

## Wave 4 — Reliability

### Goal

Cover availability, reliability, resilience, fault tolerance, and failure patterns as SD OVERVIEW pages linking MS PRIMARY (reliability engineering, resilience patterns, failure scenarios).

### Scope

4 new OVERVIEW pages. Fault tolerance is taught inside `resilience-patterns-overview` (not a separate slug). Failure patterns link to MS `failure-scenarios`.

### New Pages (4)

| Slug | Module | Topics covered | MS PRIMARY | Effort |
| :--- | :---: | :--- | :--- | :---: |
| `availability-and-nines` | 6 Reliability | Availability, nines math, uptime budget | `reliability-engineering` | M |
| `reliability-vs-availability` | 6 Reliability | Reliability vs availability, fault vs failure | `reliability-engineering` | M |
| `resilience-patterns-overview` | 6 Reliability | CB, bulkhead, retry, timeout, fallback, **fault tolerance stack** | `resilience-patterns` | M |
| `failure-patterns-overview` | 6 Reliability | Cascade, partition, dependency, region failures | `failure-scenarios` | M |

### Existing Pages Updated (6)

| Page | Change |
| :--- | :--- |
| `single-point-of-failure-elimination-redundancy` | Link `availability-and-nines`, `resilience-patterns-overview` |
| `multi-region-topologies-and-availability-zones` | Link `failure-patterns-overview` |
| `system_design_modules.yaml` | Prepend 4 slugs to Module 6 |
| `system_design_order.yaml` | Insert Module 6 block |
| MS `resilience-patterns` | Architect Notes → SD `resilience-patterns-overview` |
| MS `failure-scenarios` | Link SD `failure-patterns-overview` |

### Cross-links Added (20)

| From | To | Count |
| :--- | :--- | :---: |
| 4 new pages | MS PRIMARY (4) | 4 |
| 4 new pages | SD SPOF + multi-region (2) | 2 |
| `resilience-patterns-overview` | TP `circuit-breaker-pattern`, `bulkhead-pattern` | 2 |
| `resilience-patterns-overview` | Case studies: `payment-gateway-orchestration`, `linkedin-job-search`, `leaderboard` | 3 |
| `availability-and-nines` | `non-functional-requirements` | 1 |
| MS `reliability-engineering` | SD `availability-and-nines`, `reliability-vs-availability` | 2 |
| Intra-wave (4 new pages) | Sequential prev/next | 3 |
| `system-design-process` | `availability-and-nines` | 1 |
| TP circuit/bulkhead ADRs | SD `resilience-patterns-overview` | 2 |

### Duplicate Sections Removed

**0** — greenfield. Case study resilience trims deferred to **Wave 7**.

### Estimated Effort

**5–6 person-days**

### Exit Criteria

- [ ] Resilience interview answer on SD ≤ 1,200 words with MS deep-dive link
- [ ] Fault tolerance taught as pattern stack, not duplicated in case studies (Wave 7)

---

## Wave 5 — Observability

### Goal

Single observability hub covering logs, metrics, traces, monitoring, and alerting — distinguishing APPLICATION (`distributed-logging-system`) from pillars OVERVIEW.

### Scope

1 new OVERVIEW page; contextualize existing logging case study; MS + platform handbook links.

### New Pages (1)

| Slug | Module | Subtopics (H2 sections) | MS PRIMARY | Effort |
| :--- | :---: | :--- | :--- | :---: |
| `observability-fundamentals` | 7 Observability | Logs · Metrics · Traces · Monitoring · Alerting · RED/USE · correlation IDs | `08-observability/observability` | L |

### Existing Pages Updated (5)

| Page | Change |
| :--- | :--- |
| `distributed-logging-system` | Header callout: “APPLICATION example — see `observability-fundamentals` for pillars” |
| `distributed-logging-system-interview-questions` | Link observability fundamentals |
| `system_design_modules.yaml` | Prepend slug to Module 7 |
| `system_design_order.yaml` | Insert before logging case study |
| MS `observability` | Architect Notes → SD `observability-fundamentals`, SD logging case |

### Cross-links Added (12)

| From | To | Count |
| :--- | :--- | :---: |
| `observability-fundamentals` | MS `observability` | 1 |
| `observability-fundamentals` | SD `distributed-logging-system` | 1 |
| `observability-fundamentals` | Case studies: `chat-application`, `linkedin-job-search`, `notification-system`, `fleet-vending-iot` | 4 |
| `observability-fundamentals` | K8s HB OpenTelemetry (platform — link only) | 1 |
| MS `observability` | SD overview + logging case | 2 |
| `resilience-patterns-overview` | `observability-fundamentals` (ops loop) | 1 |
| `failure-patterns-overview` | `observability-fundamentals` (detection) | 1 |
| `non-functional-requirements` | `observability-fundamentals` | 1 |

### Duplicate Sections Removed

**0** — greenfield OVERVIEW. Case study inline observability trims → **Wave 7**.

### Estimated Effort

**2–3 person-days**

### Exit Criteria

- [ ] Reader understands logging case study ≠ full observability curriculum
- [ ] Metrics/traces/monitoring/alerting interview answer on one SD page

---

## Wave 6 — Scalability

### Goal

Cover horizontal vs vertical scaling, throughput, latency, and scaling strategies with SD PRIMARY on latency/throughput and OVERVIEW on scaling dimensions.

### Scope

3 new pages; link existing caching/replication/sharding fundamentals.

### New Pages (3)

| Slug | Module | Topics | Owner | Effort |
| :--- | :---: | :--- | :--- | :---: |
| `latency-vs-throughput` | 5 Scalability | Latency, throughput, p99, Little's Law, batching trade-offs | SD **Primary** | L |
| `horizontal-vs-vertical-scaling` | 5 Scalability | Scale-up vs scale-out, stateless tiers, DB limits | SD overview → MS PRIMARY | M |
| `scaling-strategies-overview` | 5 Scalability | Read replicas, sharding, caching, partitioning, auto-scale triggers | SD overview → MS `scalability-patterns` | M |

### Existing Pages Updated (7)

| Page | Change |
| :--- | :--- |
| `caching-and-cdns-hierarchical-arrays` | Link `scaling-strategies-overview` |
| `replication-lag-read-replica-topology` | Link `horizontal-vs-vertical-scaling` |
| `database-sharding-provisioning-and-chunk-routing` | Link `scaling-strategies-overview` |
| `capacity-estimation` | Link `latency-vs-throughput` |
| `system_design_modules.yaml` | Prepend 3 slugs to Module 5 |
| `system_design_order.yaml` | Insert Module 5 block |
| MS `scalability-patterns` | Back-links to 3 new SD pages + 4 SD cache/replica/shard pages |

### Cross-links Added (15)

| From | To | Count |
| :--- | :--- | :---: |
| 3 new pages | MS `scalability-patterns` | 3 |
| 3 new pages | SD cache/replica/shard pages (6 links) | 6 |
| `latency-vs-throughput` | `load-balancers-*`, `transport-layer-*` | 2 |
| `capacity-estimation` | `latency-vs-throughput` | 1 |
| Case study `distributed-rate-limiter` | `latency-vs-throughput` | 1 |
| MS `scalability-patterns` | 3 SD new pages | 2 |

### Duplicate Sections Removed

**0** — greenfield.

### Estimated Effort

**4–5 person-days**

### Exit Criteria

- [ ] Latency vs throughput interview answer owned by SD PRIMARY
- [ ] Scaling strategy questions route through `scaling-strategies-overview` → MS

---

## Wave 7 — Duplicate Cleanup

### Goal

Reduce embedded pattern deep-dives in case studies, interviews, SD fundamentals, and TP ADRs per Phase 4A §4–§5 — without URL changes or PRIMARY ownership changes.

### Scope

**0 new pages.** 2 optional P1 OVERVIEW pages may be authored if cleanup exposes gaps:

| Optional slug | Trigger |
| :--- | :--- |
| `cqrs-overview` | If case study trims need a link target |
| `transactional-outbox-overview` | If outbox trims need a link target |

Included below as **cleanup targets**; author only if trim leaves broken references.

---

### 7.1 CQRS

| Field | Value |
| :--- | :--- |
| **Current locations** | `proximity-search`, `hotel-booking`, `payment-gateway-orchestration`, `distributed-logging-system`, `ecommerce`, `food-delivery`; MS `cqrs-and-event-sourcing`; TP `cqrs-pattern` |
| **Target owner** | MS **Primary**; SD **Overview** (`cqrs-overview` optional); TP **Decision Guide** |
| **Cleanup strategy** | Replace `## CQRS` / full sections with ≤2 sentences + link MS PRIMARY; TP trim to adoption matrix; add optional SD overview |
| **Pages impacted** | 6 SD case studies + 1 TP + 1 MS (back-link only) = **8** |
| **Sections removed** | ~**12** |

---

### 7.2 Outbox (+ CDC cluster)

| Field | Value |
| :--- | :--- |
| **Current locations** | `email-delivery`, `notification-system`, `hotel-booking`, `stock-broker-trading`, `ott`, `online-learning-platform`; SD `cdc-based-cache-invalidation`; MS `outbox-and-cdc`; TP `outbox-pattern` |
| **Target owner** | MS **Primary**; SD `cdc-based-cache-invalidation` → **Reference** subset; TP **Decision Guide** |
| **Cleanup strategy** | Case studies: outbox sections → link MS; reframe CDC page as “cache invalidation angle” only; TP trim |
| **Pages impacted** | 6 case studies + 1 SD fundamental + 1 TP = **8** |
| **Sections removed** | ~**14** |

---

### 7.3 Circuit Breaker / Resilience

| Field | Value |
| :--- | :--- |
| **Current locations** | `payment-gateway-orchestration`, `linkedin-job-search`, `leaderboard`, `distributed-rate-limiter`, `notification-system`, `urlshortner`, `ecommerce`, `food-delivery`, `ride-sharing`, `stock-broker-trading` + 6 interview companions; MS `resilience-patterns`; TP `circuit-breaker-pattern`, `bulkhead-pattern` |
| **Target owner** | MS **Primary**; SD `resilience-patterns-overview` (Wave 4) **Overview** |
| **Cleanup strategy** | Pattern prose → ≤2 sentences + link SD overview → MS PRIMARY; interviews: shorten pattern answers |
| **Pages impacted** | ~**18** SD (12 case + 6 interview) + 2 TP = **20** |
| **Sections removed** | ~**35** |

---

### 7.4 Consistent Hashing

| Field | Value |
| :--- | :--- |
| **Current locations** | `distributed-kv-store`, `distributed-lru-cache`, `distributed-rate-limiter`, `chat-application`, `load-balancers-*`, `ecommerce`, `food-delivery`, `ott`, `collaborative-text-editor` + 4 interview companions; SD `consistent-hashing` (Wave 2); MS `consistent-hashing` |
| **Target owner** | SD **Primary**; MS **Deep Dive** |
| **Cleanup strategy** | Ring tutorials in cases → link SD `consistent-hashing`; LB page keeps skew mention only |
| **Pages impacted** | ~**13** SD |
| **Sections removed** | ~**18** |

---

### 7.5 Observability / Tracing

| Field | Value |
| :--- | :--- |
| **Current locations** | 20+ case studies (OpenTelemetry, trace_id, metrics tables); MS `observability`; SD `distributed-logging-system` |
| **Target owner** | MS **Primary**; SD `observability-fundamentals` (Wave 5) **Overview** |
| **Cleanup strategy** | Inline pillar tutorials → ≤2 sentences + link SD overview; logging case keeps APPLICATION depth for pipeline design only |
| **Pages impacted** | ~**20** SD case studies + 3 interview companions |
| **Sections removed** | ~**26** |

---

### Wave 7 Summary

| Metric | Value |
| :--- | :---: |
| **Pages impacted** | **~55** (unique; overlap across clusters) |
| **Duplicate sections removed** | **~95** |
| **Optional new pages** | 0–2 (CQRS/outbox overviews) |
| **Cross-links added** | ~**40** (inbound from trimmed pages to Wave 2–5 overviews) |
| **Estimated effort** | **8–10 person-days** |

### Exit Criteria

- [ ] No case study contains >2 sentences of CQRS/outbox/CB/consistent-hash/pillars prose without link
- [ ] Grep audit: `## CQRS` absent or ≤3 lines in case studies
- [ ] Duplication severity scores drop from 7–9 to ≤3 per Phase 3 matrix

---

## Final Wave Summary

| Wave | New Pages | Updated Pages | Cross-links | Duplicate Sections Removed | Priority | Effort |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1 — Foundations** | 4 | 5 | 18 | 0 | **P0** | 5–6 d |
| **2 — Distributed Systems** | 3 | 6 | 16 | 3 | **P0** | 4–5 d |
| **3 — Architecture Styles** | 1 | 8 | 14 | 0 | **P0** | 3–4 d |
| **4 — Reliability** | 4 | 6 | 20 | 0 | **P0** | 5–6 d |
| **5 — Observability** | 1 | 5 | 12 | 0 | **P0** | 2–3 d |
| **6 — Scalability** | 3 | 7 | 15 | 0 | **P0** | 4–5 d |
| **7 — Duplicate Cleanup** | 0–2 | ~55 | 40 | ~95 | **P1** | 8–10 d |
| **Total** | **16–18** | **~55** | **~110** | **~95** | | **28–38 d** |

*Navigation YAML updates (2 files) counted inside each wave’s updated pages.*

---

## 1. Recommended Execution Order

```
Wave 1 → Wave 2 → Wave 3 → Wave 6 → Wave 4 → Wave 5 → Wave 7
```

| Order | Wave | Rationale |
| :---: | :--- | :--- |
| 1 | **Wave 1** | On-ramp required by all later waves |
| 2 | **Wave 2** | Distributed concepts before case-study pattern links |
| 3 | **Wave 3** | Architecture framing before reliability/EDA case reads |
| 4 | **Wave 6** | Latency/throughput needed for reliability SLO pages |
| 5 | **Wave 4** | Resilience links to Wave 6 latency + Wave 1 NFRs |
| 6 | **Wave 5** | Observability links to Wave 4 failure/resilience loop |
| 7 | **Wave 7** | Cleanup requires Wave 2–5 link targets to exist |

**Parallelization option:** Waves 4 + 5 + 6 can run in parallel **after** Waves 1–3 if three authors coordinate YAML merges.

---

## 2. Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
| :--- | :---: | :---: | :--- |
| YAML merge conflicts (`system_design_modules.yaml`) | Medium | Medium | Single PR per wave; scripted slug insertion |
| Broken `site.GetPage` after new slugs | Low | High | `hugo --minify` gate per wave |
| Case study trim breaks interview answer quality | Medium | Medium | Wave 7 trims interviews last; keep links to MS PRIMARY |
| TP trim removes useful selection content | Medium | Low | Trim mechanics only; preserve decision matrices per G3 |
| MS Architect Notes back-links inconsistent | Medium | Low | Checklist of 11 MS pages per Phase 3 |
| Scope creep (authoring P1 pages in Wave 7) | High | Medium | Gate optional `cqrs-overview` / `outbox-overview` behind trim audit |
| Reader confusion (SD overview vs MS primary) | Medium | Medium | Mandatory “Deep dive” link block template from Phase 2A |
| Effort underestimate on Wave 7 | High | Medium | Budget 8–10 days; triage top-5 case studies first |

---

## 3. Expected Reduction in Duplication

| Metric | Before | After Wave 7 | Change |
| :--- | :---: | :---: | :---: |
| Concepts with ≥3 duplicate deep-dive locations | 12 clusters | 0 | **−100%** |
| Approximate duplicate sections (full pattern prose) | ~120 | ~25 (APPLICATION only) | **−79%** |
| Phase 3 dup severity score (avg top-12) | 7.8 | ≤3.0 | **−62%** |
| TP pattern pages with mechanics >40% | 5 | 0 | **−100%** |
| Case studies with embedded CQRS/outbox/CB tutorial | 18 | 0 | **−100%** |

---

## 4. Expected Curriculum Coverage Improvement

| Module | Before (Phase 1) | After Wave 6 | Gap closed |
| :--- | :---: | :---: | :--- |
| 1 Foundations | 4 | **8** | On-ramp, NFRs, BOE |
| 2 Distributed Systems | 2 | **5** | CAP, consistency, hashing |
| 5 Scalability | 4 | **7** | Latency, scale dimensions, strategies |
| 6 Reliability | 2 | **6** | Availability, reliability, resilience, failures |
| 7 Observability | 1 (case only) | **2** | Pillars overview + logging case |
| 8 Architecture Styles | **0** | **1** | Full style comparison matrix |
| **Fundamentals total** | **19** | **37** | **+95%** |
| Empty modules | 1 | **0** | Module 8 filled |

**Interview readiness:** Reader can answer top-20 system design interview topics from SD OVERVIEW/PRIMARY pages alone, with MS linked for follow-up depth.

---

## Per-Wave Deliverables Checklist (Execution)

When a wave moves from planning to execution, each PR must include:

- [ ] New `.md` files (if any) with front matter matching existing SD conventions
- [ ] `data/system_design_modules.yaml` slug insertion
- [ ] `data/system_design_order.yaml` slug insertion
- [ ] MS Architect Notes back-links (if MS PRIMARY touched)
- [ ] TP ADR trims (if TP touched — Wave 3, 4, 7)
- [ ] `hugo --minify` CI pass
- [ ] Update this roadmap wave row to **Executed** with PR link

---

## Explicit Non-Actions (Phase 4B Planning)

| Action | Status |
| :--- | :---: |
| Create markdown content | ❌ |
| Modify any repository files | ❌ |
| Move / rename files | ❌ |
| Navigation / alias / redirect changes | ❌ |

---

## Exit Criteria — Phase 4B Planning

| Criterion | Status |
| :--- | :---: |
| Seven waves defined with goals and scope | ✅ |
| New / updated / cross-link / dedup estimates per wave | ✅ |
| Wave 7 cleanup table per concept | ✅ |
| Final summary table | ✅ |
| Execution order + risks + coverage metrics | ✅ |

**Next step:** Approve wave-by-wave execution beginning with **Wave 1 — Foundations**.

**Do not execute content or YAML changes until explicit wave approval.**
