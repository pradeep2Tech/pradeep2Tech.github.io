---
title: "System Design Phase 1 — Navigation-Only Restructure"
date: 2026-07-03T18:00:00+00:00
draft: true
description: "Phase 1 deliverable — module mapping, YAML changes, impacted files, rollback plan. No file moves, no URL changes."
tags: ["system-design", "meta", "planning", "navigation"]
---

# Phase 1 — Navigation & Curriculum Structure (Executed)

**Status:** Complete  
**Scope:** Navigation YAML only — no content moves, renames, aliases, or rewrites  
**Microservices:** Unchanged and independent

---

## Objective

Expose a 10-module architect learning path in the System Design sidebar while preserving every existing flat URL under `/system-design/<slug>/`.

---

## Proposed Module Mapping

All **66** topic pages mapped. Every slug appears **exactly once** in `system_design_modules.yaml`.

| Module | ID | Pages | Rationale |
| :--- | :---: | :---: | :--- |
| **Foundations** | 1 | 4 | Networking, transport, and hands-on ingress lab |
| **Distributed Systems** | 2 | 2 | Conflict resolution, transactions / isolation in distributed context |
| **Data Management** | 3 | 3 | Storage internals, CDC invalidation, sharding |
| **Communication** | 4 | 4 | Proxies, ingress, REST/gRPC, load balancing |
| **Scalability** | 5 | 4 | Caching tiers, eviction, stampede mitigation, read replicas |
| **Reliability** | 6 | 2 | SPOF elimination, multi-region / AZ topologies |
| **Observability** | 7 | 1 | Distributed logging design (moved from Case Studies grouping only) |
| **Architecture Styles** | 8 | 0 | **Empty** — no standalone SD pages today (Phase 2 gap) |
| **Case Studies** | 9 | 27 | Full-system design walkthroughs |
| **Interview Guide** | 10 | 19 | Case-study interview companions |

### Page-level mapping

#### 1 — Foundations (4)

| Slug | File |
| :--- | :--- |
| `networking-essentials-ip-dns-firewalls` | `networking-essentials-ip-dns-firewalls.md` |
| `transport-layer-mechanics-tcp-vs-udp` | `transport-layer-mechanics-tcp-vs-udp.md` |
| `http3-quic-and-websocket-transports` | `http3-quic-and-websocket-transports.md` |
| `hands-on-load-balancing-setup` | `hands-on-load-balancing-setup.md` |

#### 2 — Distributed Systems (2)

| Slug | File |
| :--- | :--- |
| `crdts-and-multi-master-conflict-resolution` | `crdts-and-multi-master-conflict-resolution.md` |
| `database-transactions-and-acid-isolation` | `database-transactions-and-acid-isolation.md` |

#### 3 — Data Management (3)

| Slug | File |
| :--- | :--- |
| `relational-database-fundamentals-and-b-trees` | `relational-database-fundamentals-and-b-trees.md` |
| `cdc-based-cache-invalidation` | `cdc-based-cache-invalidation.md` |
| `database-sharding-provisioning-and-chunk-routing` | `database-sharding-provisioning-and-chunk-routing.md` |

#### 4 — Communication (4)

| Slug | File |
| :--- | :--- |
| `proxy-servers-forward-vs-reverse` | `proxy-servers-forward-vs-reverse.md` |
| `layer4-layer7-multi-tier-ingress-routing` | `layer4-layer7-multi-tier-ingress-routing.md` |
| `application-layer-protocols-rest-grpc` | `application-layer-protocols-rest-grpc.md` |
| `load-balancers-and-routing-algorithms` | `load-balancers-and-routing-algorithms.md` |

#### 5 — Scalability (4)

| Slug | File |
| :--- | :--- |
| `caching-and-cdns-hierarchical-arrays` | `caching-and-cdns-hierarchical-arrays.md` |
| `cache-eviction-and-mutation-policies` | `cache-eviction-and-mutation-policies.md` |
| `cache-stampede-and-penetration-mitigation` | `cache-stampede-and-penetration-mitigation.md` |
| `replication-lag-read-replica-topology` | `replication-lag-read-replica-topology.md` |

#### 6 — Reliability (2)

| Slug | File |
| :--- | :--- |
| `single-point-of-failure-elimination-redundancy` | `single-point-of-failure-elimination-redundancy.md` |
| `multi-region-topologies-and-availability-zones` | `multi-region-topologies-and-availability-zones.md` |

#### 7 — Observability (1)

| Slug | File | Note |
| :--- | :--- | :--- |
| `distributed-logging-system` | `distributed-logging-system.md` | Curriculum lens = observability; file unchanged |

#### 8 — Architecture Styles (0)

No existing standalone pages. Deep architecture-style content lives in **Microservices** (`01-architecture-styles/`) — intentionally not merged in Phase 1.

#### 9 — Case Studies (27)

| Slug |
| :--- |
| `urlshortner` |
| `distributed-rate-limiter` |
| `leaderboard` |
| `distributed-lru-cache` |
| `distributed-kv-store` |
| `notification-system` |
| `chat-application` |
| `social-feed` |
| `email-delivery` |
| `cloud-storage` |
| `distributed-message-queue` |
| `distributed-job-scheduler` |
| `distributed-web-crawler` |
| `proximity-search` |
| `linkedin-job-search` |
| `food-delivery` |
| `ride-sharing` |
| `ticket-booking` |
| `hotel-booking` |
| `ecommerce` |
| `payment-gateway-orchestration` |
| `stock-broker-trading` |
| `sponsored-ads` |
| `ott` |
| `online-learning-platform` |
| `fleet-vending-iot` |
| `collaborative-text-editor` |

#### 10 — Interview Guide (19)

All `*-interview-questions.md` companions, ordered to mirror their parent case study sequence.

---

## Categorization decisions

| Page | Previous sidebar group | New module | Why |
| :--- | :--- | :--- | :--- |
| `distributed-logging-system` | Case Studies | Observability | Only observability-focused design page in SD today |
| `database-transactions-and-acid-isolation` | Fundamentals | Distributed Systems | Concurrency / consistency in distributed stores |
| `replication-lag-read-replica-topology` | Fundamentals | Scalability | Read scaling and lag trade-offs |
| `load-balancers-and-routing-algorithms` | Fundamentals | Communication | Request routing and protocol termination |
| `cdc-based-cache-invalidation` | Fundamentals | Data Management | Data-change propagation to cache |

---

## YAML changes

### Created

| File | Purpose |
| :--- | :--- |
| `data/system_design_modules.yaml` | 10-module sidebar structure (flat slugs) |

### Updated

| File | Change |
| :--- | :--- |
| `data/curriculum_sidebar.yaml` | Replaced `flatGroups` + `splitAfter: 19` with `modules: system_design_modules` |
| `data/system_design_order.yaml` | Reordered 66 topics by module; added 19 interview pages to prev/next chain |

### Unchanged

- All files under `content/system-design/` (paths, slugs, front matter)
- `content/microservices/` — fully independent
- `layouts/` — existing `modules` branch in `curriculum-sidebar.html` already supports this pattern
- No Hugo aliases added or removed

---

## Impacted files

| Path | Impact |
| :--- | :--- |
| `data/system_design_modules.yaml` | **New** — module definitions |
| `data/system_design_order.yaml` | **Modified** — curriculum sequence |
| `data/curriculum_sidebar.yaml` | **Modified** — sidebar config for `system-design` |
| `layouts/partials/curriculum-sidebar.html` | **Read-only** — uses existing `modules` code path |
| `layouts/system-design/single.html` | **Read-only** — prev/next via `system_design_order` |
| `content/system-design/**` | **No changes** |

---

## Sidebar behavior notes

1. **Module badges** — Sidebar shows numbered modules 1–10 (same pattern as Microservices, Kafka Handbook, etc.).
2. **Interview nesting** — Case studies with companions still show nested “Interview Questions” sub-links under the parent in **Case Studies** (layout auto-discovers `*-interview-questions` suffix). The same pages also appear in **Interview Guide** — intentional duplication until a future layout tweak (optional Phase 4).
3. **Empty Architecture Styles module** — Renders as a collapsible group with no topics. Signals Phase 2 content gap without hiding the curriculum slot.
4. **Prev/next navigation** — Interview companions are now in the linear order chain (previously excluded).

---

## Rollback plan

Fully reversible in one commit. No content or URL recovery needed.

```bash
# 1. Restore previous sidebar config
git checkout HEAD~1 -- data/curriculum_sidebar.yaml

# 2. Remove modules file
git rm data/system_design_modules.yaml

# 3. Restore flat topic order (pre-Phase-1)
git checkout HEAD~1 -- data/system_design_order.yaml

# 4. Verify
hugo --minify
```

**Pre-rollback state preserved in git history:**

- `curriculum_sidebar.yaml`: `flatGroups` with `splitAfter: 19` (Fundamentals / Case Studies)
- `system_design_order.yaml`: 47 topics (fundamentals + case studies, no interview chain)

**Rollback risk:** Low. Only navigation data changes; zero content files touched.

---

## Verification

```bash
hugo --minify
```

Confirm:

- [ ] Build succeeds with no missing `site.GetPage` warnings for system-design slugs
- [ ] Sidebar shows 10 modules under System Design
- [ ] Sample URLs unchanged (e.g. `/system-design/urlshortner/`, `/system-design/caching-and-cdns-hierarchical-arrays/`)
- [ ] Prev/next follows new module order on a fundamentals page and a case study page

---

## Phase 2+ (not started)

| Phase | Scope | Status |
| :--- | :--- | :--- |
| **Phase 2** | Gap analysis — missing architect topics (NFRs, CAP, backpressure, etc.) | Awaiting approval |
| **Phase 3** | Concept registry — SD vs Microservices vs Technology Playbook overlap | Awaiting approval |
| **Phase 4** | Ownership recommendations (overview vs deep dive vs ADR) | Future |

**Do not proceed beyond Phase 1 without explicit approval.**
