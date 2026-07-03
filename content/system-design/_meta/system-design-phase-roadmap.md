---
title: "System Design Curriculum — Phase Roadmap (Phase C)"
date: 2026-07-03T16:00:00+00:00
draft: true
description: "Phased implementation roadmap with goals, files affected, risks, and rollback per phase."
tags: ["system-design", "meta", "planning"]
---

# Phase C — Implementation Roadmap

**Status:** Planning only — execute phases sequentially after Phase B approval.

**Principle:** Incremental, reversible, alias-safe. No big-bang rewrite.

---

## Roadmap Overview

| Phase | Name | Duration | Risk |
| :---: | :--- | :---: | :---: |
| **1** | Navigation only | 1–2 days | Low |
| **2** | Create missing folders | 1 day | Low |
| **3** | Move microservice concepts | 1–2 weeks | Medium |
| **4** | Create canonical pages | 3–5 days | Low |
| **5** | Deduplicate | 2 weeks | Medium |
| **6** | Interview guide | 1 week | Medium |
| **7** | Learning paths | 2–3 days | Low |

---

## Phase 1 — Navigation Only

### Goals

- Introduce 12-module yaml for System Design **without moving content**
- Sidebar shows future curriculum map on `_index.md` only
- Zero URL changes

### Files Affected

| File | Action |
| :--- | :--- |
| `data/system_design_modules.yaml` | **Create** — module definitions pointing to **existing flat slugs** |
| `data/system_design_order.yaml` | **Update** — group existing 48 topics under module IDs |
| `data/curriculum_sidebar.yaml` | **Update** — `system-design.modules: system_design_modules` |
| `content/system-design/_index.md` | **Update** — 12-module table (links to current flat URLs) |
| `layouts/system-design/list.html` | **Verify** — module list partial works |

### Risks

- Sidebar regression if yaml paths don't resolve — **mitigate:** point topics to existing slugs only

### Rollback

- Revert yaml + `_index.md`; flat `system_design_order.yaml` still valid

### Exit Criteria

- `hugo --minify` passes
- All 48 existing SD URLs unchanged
- Sidebar shows 12 modules with working links

---

## Phase 2 — Create Missing Folders

### Goals

- Create `01-foundations/` … `12-learning-paths/` directory scaffold
- Add section `_index.md` stubs (`draft: true` optional)
- **No topic file moves yet**

### Files Affected

| Path | Action |
| :--- | :--- |
| `content/system-design/01-foundations/_index.md` | Create (12 section indexes) |
| `content/system-design/02-distributed-systems/_index.md` | Create |
| … | … |
| `content/system-design/12-learning-paths/_index.md` | Create |

### Risks

- Hugo may expose empty sections in sitemap — **mitigate:** `draft: true` on section indexes until populated

### Rollback

- Delete new empty folders

### Exit Criteria

- Folder scaffold exists
- No topic content moved
- Build passes

---

## Phase 3 — Move Microservice Concepts

### Goals

- Copy MS canonical pattern pages to System Design module paths
- Add Hugo aliases on **new SD pages** pointing to all MS URLs (including legacy flat aliases)
- MS pages remain live (duplicate period) OR MS pages become stub pointers (configurable)

### Files Affected (38 MS topic pages → SD)

| Source (MS) | Destination (SD) |
| :--- | :--- |
| `04-distributed-systems/cap-and-pacelc.md` | `02-distributed-systems/cap-and-pacelc.md` |
| `03-data-management/cqrs-and-event-sourcing.md` | `03-data-management/cqrs-and-event-sourcing.md` |
| `05-resilience-patterns/resilience-patterns.md` | `06-reliability/resilience-patterns.md` |
| `08-observability/observability.md` | `07-observability/observability.md` |
| … | *(full table in migration-plan §6.1)* |

| Also update |
| :--- |
| `data/system_design_modules.yaml` — topic paths → nested slugs |
| `data/system_design_order.yaml` |
| `scripts/phase_c_system_design_curriculum.py` — automation |

### Risks

| Risk | Mitigation |
| :--- | :--- |
| Duplicate content in search | `canonicalUrl` front matter or MS stub pages with `noindex` |
| Broken MS sidebar | Keep `microservices_order.yaml` until Phase 7 |
| Alias chain too long | Max 2-hop: legacy flat → MS path → SD path |

### Rollback

- Remove SD nested copies
- MS pages unchanged if copy-only approach used

### Exit Criteria

- P0 concepts accessible at SD paths
- All MS URLs still resolve (alias or original)
- Concept registry §3 satisfied for P0 concepts

---

## Phase 4 — Create Canonical Pages

### Goals

- Fill gaps where SD fundamentals and MS pages don't cover target registry
- Merge paired pages (e.g. `database-transactions-and-acid-isolation` + MS `concurrency-control`)

### Files Affected

| Page | Action |
| :--- | :--- |
| `02-distributed-systems/concurrency-control.md` | Merge SD + MS content |
| `05-scalability/scalability-patterns.md` | Merge SD replication/sharding + MS |
| `05-scalability/caching-patterns.md` | Merge SD cache fundamentals + MS |
| `04-communication/rest-vs-grpc.md` | Rename/refactor from `application-layer-protocols-rest-grpc` |
| `01-foundations/architecture-decision-records.md` | Copy from MS production playbook |

### Risks

- Merge conflicts in prose style (case-study vs architect template) — **mitigate:** architect template for pattern pages only

### Rollback

- Keep pre-merge files via git; aliases to old slugs

### Exit Criteria

- All 42 concepts in registry have SD canonical page
- No empty architect template sections

---

## Phase 5 — Deduplicate

### Goals

- Case studies: replace pattern deep-dives with ≤2 sentences + link to canonical SD page
- Technology Playbook: trim pattern pages to selection ADR + link to SD
- Remove duplicate MS pages (optional) after alias bake period

### Files Affected

| Category | Files | Change type |
| :--- | :--- | :--- |
| Case studies | 29 design posts | **Link-only** edits in §7–§10 |
| Case study interviews | 19 Q&A files | Update answers to reference SD canonical |
| Technology Playbook | ~15 pattern pages | Trim to comparison + link |
| MS duplicates | 38 pages | Convert to stub: "Moved to [System Design](...)" |
| SD fundamentals superseded | ~8 flat files | Alias to module path; trim body |

### High-Impact Dedup Targets (do first)

1. `email-delivery.md` — outbox section → link `03-data-management/outbox-and-cdc`
2. `hotel-booking.md` — CQRS + outbox → links
3. `proximity-search.md` — CQRS → link
4. `payment-gateway-orchestration.md` — bulkhead/circuit breaker → link `06-reliability/resilience-patterns`
5. `distributed-lru-cache.md` — consistent hashing → link `02-distributed-systems/consistent-hashing`
6. `cdc-based-cache-invalidation.md` — merge into outbox-and-cdc §cache invalidation

### Risks

| Risk | Mitigation |
| :--- | :--- |
| Over-trimming case study pedagogical value | Keep **applied** pattern paragraphs; remove **textbook** repeats only |
| Interview answer staleness | Batch update with script + manual review |
| TP broken inbound links | Redirect table in TP `_index` |

### Rollback

- Link-only commits are revertible per file

### Exit Criteria

- No concept in registry appears with >2 sentences deep dive outside canonical page
- Grep audit: `outbox pattern guarantees` appears once at depth

---

## Phase 6 — Interview Guide

### Goals

- Merge MS Top 300 into `11-interview-guide/top-300-system-design-questions.md`
- Relocate 19 case-study interview files under `11-interview-guide/case-studies/`
- Update all `Deep Dive` links to SD canonical paths
- Add pattern questions for fundamentals not in MS bank

### Files Affected

| File | Action |
| :--- | :--- |
| `11-interview-guide/top-300-system-design-questions.md` | Create from MS top-300 + expansions |
| `11-interview-guide/architect-questions.md` | Migrate from MS |
| `11-interview-guide/case-studies/*.md` | Move from flat `*-interview-questions.md` with aliases |
| `content/microservices/11-interview-guide/*` | Stub or alias |

### Target Distribution (350+ total after merge)

| Category | Count |
| :--- | :---: |
| Architecture | 60 |
| Distributed Systems | 50 |
| Scalability | 40 |
| Reliability | 40 |
| Troubleshooting | 35 |
| Observability | 35 |
| Security | 20 |
| Migration | 20 |
| Case study specific | 19×50 probes (companion files) |

### Risks

- Question duplication across MS and case-study companions — **mitigate:** case-study Q&A stays design-specific; Top 300 stays pattern-focused

### Rollback

- Keep MS interview URLs via aliases

### Exit Criteria

- Single entry point: Top 300 system design questions
- All Deep Dive links resolve to SD canonical pages

---

## Phase 7 — Learning Paths

### Goals

- Migrate MS learning paths to SD `12-learning-paths/`
- Rewrite paths for unified 12-module curriculum
- MS `_index.md` becomes redirect hub to System Design

### Files Affected

| File | Action |
| :--- | :--- |
| `12-learning-paths/senior-engineer-path.md` | Migrate + update module links |
| `12-learning-paths/lead-engineer-path.md` | Migrate |
| `12-learning-paths/architect-path.md` | Migrate |
| `12-learning-paths/interview-revision-path.md` | Migrate |
| `content/microservices/_index.md` | Redirect banner + module map links to SD |
| `data/curriculum_sections.yaml` | Update MS `menuLabel` → "Microservices (→ System Design)" |

### Risks

- User bookmark confusion — **mitigate:** prominent redirect on MS landing for 6 months

### Rollback

- Restore MS learning paths from git

### Exit Criteria

- Four learning paths reference SD module paths only
- MS section documents migration status

---

## Phase 8 (Optional) — Technology Playbook Alignment

*Not in original 7 phases but recommended immediately after Phase 5.*

### Goals

- TP pattern pages (`cqrs-pattern`, `saga-pattern`, `circuit-breaker-pattern`, etc.) → selection stub + SD link
- TP retains: `how-to-choose-*`, broker/cache comparisons, workflow engine ADRs

### Files Affected

~15 files in `content/technology-playbook/`

---

## CI / Validation Checklist (Every Phase)

```bash
hugo --minify
# Alias audit script (to create):
python scripts/audit_hugo_aliases.py --section system-design --section microservices
# Link check:
python scripts/verify_internal_links.py content/system-design content/microservices
```

| Check | Phase |
| :--- | :--- |
| Build passes | All |
| Legacy URL list returns 200 | 3+ |
| Concept registry grep audit | 5 |
| Top 300 deep dive links | 6 |
| curriculum_sections.yaml valid | 1, 7 |

---

## Recommended Migration Sequence (Executive)

1. **Phase 1** — Navigation yaml (immediate, zero risk)  
2. **Phase 3a** — P0 concepts only: CAP, CQRS, Outbox, Resilience, Observability (highest duplication ROI)  
3. **Phase 5 (partial)** — Link-only dedup on top 6 case studies  
4. **Phase 3b** — Remaining MS pages  
5. **Phase 4** — Merge SD fundamentals  
6. **Phase 5 (complete)** — TP trim + MS stubs  
7. **Phase 6** — Interview merge  
8. **Phase 7** — Learning paths + MS redirect  
9. **Phase 2** — Can run in parallel with Phase 1 (scaffold only)  

---

## Success Metrics

| Metric | Target |
| :--- | :--- |
| Concepts with single canonical SD page | 42/42 |
| Legacy URLs broken | 0 |
| Case studies rewritten | 0 (link-only) |
| Final SD topic pages | ~72–78 canonical + 29 case studies |
| Interview questions | 300+ pattern + 19 case companions |
| MS section status | Redirect hub within 6 months of Phase 7 |

---

**Phase C planning complete. No implementation until explicit approval per phase.**
