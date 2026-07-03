---
title: "Kafka Handbook Navigation Plan"
date: 2026-07-03T12:00:00+00:00
draft: true
description: "Hugo sidebar, yaml, aliases, and cross-link strategy for Phase B."
tags: ["kafka-handbook", "meta", "planning"]
---

# Navigation Plan

**Target:** GitHub Pages / Hugo curriculum sidebar via `data/kafka_handbook_modules.yaml` and `kafka_handbook_order.yaml`.

**Constraint:** Preserve existing 4-module structure; add optional Module 5 (Learning Paths). No 10+ folder explosion.

---

## Current Navigation State

| Module | ID | Topics in yaml | In repo |
| :--- | :---: | :---: | :---: |
| Fundamentals | 1 | 4 | 4 |
| Apache Kafka | 2 | 7 | 7 |
| Broker Comparisons | 3 | 5 | 5 |
| Interview Guide | 4 | 4 | 3 (+1 missing) |

**Sidebar resolution:** `site.GetPage "kafka-handbook/<slug>"` where slug = nested path (e.g. `02-kafka/kafka-core`).

---

## Proposed Module Structure (Phase B)

```yaml
modules:
  - id: 1
    focus: "Fundamentals"
    topics:
      - 01-fundamentals/messaging-patterns
      - 01-fundamentals/messaging-models
      - 01-fundamentals/queue-vs-stream
      - 01-fundamentals/broker-selection-guide

  - id: 2
    focus: "Apache Kafka"
    topics:
      - 02-kafka/kafka-core
      - 02-kafka/kafka-internals
      - 02-kafka/kafka-consumer-groups          # NEW
      - 02-kafka/kafka-delivery-semantics       # NEW
      - 02-kafka/kafka-performance
      - 02-kafka/kafka-security
      - 02-kafka/kafka-operations
      - 02-kafka/kafka-troubleshooting
      - 02-kafka/kafka-schema-registry          # NEW (Phase C)
      - 02-kafka/kafka-connect                  # NEW (Phase C)
      - 02-kafka/kafka-streams                  # NEW (Phase C)
      - 02-kafka/kafka-multi-region             # NEW (Phase C)

  - id: 3
    focus: "Broker Comparisons"
  # unchanged

  - id: 4
    focus: "Interview Guide"
    topics:
      - 04-interview-guide/top-150-interview-questions
      - 04-interview-guide/architect-questions
      - 04-interview-guide/troubleshooting-questions
      - 04-interview-guide/performance-questions   # NEW
      - 04-interview-guide/design-tradeoffs

  - id: 5
    focus: "Learning Paths"
    topics:
      - 05-learning-paths/kafka-senior-engineer-path
      - 05-learning-paths/kafka-lead-path
      - 05-learning-paths/kafka-architect-path
      - 05-learning-paths/kafka-interview-revision-path
```

**Phase B minimum yaml change:** Add `performance-questions` + Module 5 learning paths.  
**Phase C:** Add new `02-kafka/*` canonical pages as created.

---

## Landing Page (`_index.md`)

| Section | Phase B update |
| :--- | :--- |
| Learning paths table | Link to `05-learning-paths/` files instead of inline only |
| Modules list | Add Module 5; note new Kafka depth pages |
| Meta links | Link to `_meta/concept-registry.md` (draft, optional for maintainers) |
| Quick links | Top 150, Troubleshooting canonical, Broker selection |

---

## Section Index Pages

Rewrite stubs (`01-fundamentals/_index.md`, etc.) with:

- Module purpose (2–3 sentences)
- Recommended reading order (numbered list)
- Link to learning path file for role
- Link to concept registry (maintainer)

---

## Hugo Aliases (Preserve URLs)

| Old URL | Alias on | Status |
| :--- | :--- | :--- |
| `/kafka-handbook/kafka/` | `02-kafka/kafka-core.md` | Active |
| `/kafka-handbook/rabbitmq/` | `03-broker-comparisons/kafka-vs-rabbitmq.md` | Active |

**Phase B — add if splitting pages:**

| Potential old anchor | New target |
| :--- | :--- |
| `/kafka-handbook/02-kafka/kafka-core/` | Keep |
| Future `/kafka-handbook/02-kafka/kafka-consumer-groups/` | N/A (new) |

---

## Top 150 Deep Dive Column Migration

| Current | Target |
| :--- | :--- |
| `Related Document` column | Rename to `Deep Dive` |
| `` `content/kafka-handbook/02-kafka/kafka-internals.md` `` | `[ISR shrink](/kafka-handbook/02-kafka/kafka-internals/#what-is-the-in-sync-replica-set)` |
| File paths | Hugo `RelPermalink` + `#` slug from question heading |

**Slug rule:** Question text → kebab-case anchor on answer page (Phase C when answers added).

**Interim Phase B:** Deep Dive links to canonical **page** (no anchor) until answer headings exist.

---

## Cross-Link Strategy

Every published topic page ends with **## See Also** (max 6 links):

| Link type | Example |
| :--- | :--- |
| Upstream concept | Fundamentals → Core |
| Downstream detail | Core → Internals |
| Canonical sibling | Performance → Troubleshooting (lag) |
| Comparison | Core → vs RabbitMQ |
| Interview | → Top 150 filtered by topic |
| External | Technology Playbook broker ADR |

**Remove:** Duplicate 14-section content used only to pad cross-links.

---

## Breadcrumb Recommendations

Hugo path mirrors breadcrumbs:

```
Kafka Handbook > Apache Kafka > Kafka Internals
Kafka Handbook > Interview Guide > Top 150
```

Ensure `moduleTitle` + `sectionRef` front matter stays consistent for sidebar numbering (`2.3`, etc.).

---

## Files Outside Handbook Navigation

| File | Nav treatment |
| :--- | :--- |
| `_meta/*.md` | `draft: true` — exclude from sidebar |
| `module-messaging-streaming.md` | Technology Playbook; not in `kafka_handbook_order.yaml` |
| Root `refactoring-plan.md` | Delete Phase B |

---

## Sidebar QA Checklist (Phase B)

- [ ] Every `kafka_handbook_order.yaml` entry resolves via `hugo server`
- [ ] No orphan pages (all content pages in order yaml)
- [ ] `performance-questions.md` appears under Interview Guide
- [ ] Module 5 learning paths appear after Interview Guide
- [ ] Prev/next navigation works on nested slugs
- [ ] Aliases redirect old `/kafka/` and `/rabbitmq/` URLs

---

## `module-messaging-streaming.md` Updates

| Item | Action |
| :--- | :--- |
| Q26 Top 150 reference | Point to `03-broker-comparisons/` or `broker-selection-guide` |
| Topic table | Already updated — verify in Phase B |

---

**STOP — Implement navigation changes in Phase B after approval.**
