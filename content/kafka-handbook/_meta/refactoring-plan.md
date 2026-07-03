---
title: "Kafka Handbook Refactoring Plan"
date: 2026-07-03T12:00:00+00:00
draft: true
description: "Phase A inventory — quality, duplication, gaps, and recommended actions."
tags: ["kafka-handbook", "meta", "planning"]
---

# Phase A — Repository Inventory

**Scope:** `content/kafka-handbook/` (27 markdown files)  
**Audience:** Senior Engineers, Leads, Architects (6+ years)  
**Status:** Planning only — **no content rewritten in Phase A**

Supersedes root-level `refactoring-plan.md` (pre-migration artifact). Delete root copy in Phase B.

---

## Executive Summary

| Metric | Assessment |
| :--- | :--- |
| **Structure** | Sound — 4 modules (`01`–`04`) already in place |
| **Template compliance** | All topic pages use 14-section skeleton; sections are **thin** (~5–15 bullets each) |
| **Duplication** | **High** — ISR, rebalance, lag, acks, poison messages repeated across 6+ files |
| **Canonical discipline** | **None** — no concept registry enforced yet |
| **Interview Layer 1** | Top 150 exists; **missing** `performance-questions.md` |
| **Interview Layer 2** | **Missing** — no Short Answer / Detailed Explanation per question |
| **Deep Dive links** | File paths, not Hugo URLs; no `##` answer anchors |
| **Learning paths** | Inline table on `_index.md` only; `05-learning-paths/` not created |
| **Broker comparisons** | Consolidated correctly; **broken Hugo shortcode** in `kafka-vs-rabbitmq.md` |
| **Missing Kafka topics** | Transactions, exactly-once, idempotent producer, schema registry, Connect, Streams, compaction deep dive, MirrorMaker |

**Recommended Phase B focus:** Enforce concept registry, split 2–3 canonical pages, add answer layer (batched), fix navigation yaml, add learning paths — **not** a new folder hierarchy.

---

## File Inventory

| File | Purpose | Quality | Duplication | Interview Value | Problems | Action |
| :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| `_index.md` | Handbook landing + inline learning paths | 7 | 2 | 6 | Learning paths not dedicated pages; no link to concept registry | **Keep** — expand in Phase B; link `05-learning-paths/` |
| `refactoring-plan.md` (root) | Old migration plan | 4 | N/A | 1 | Stale (references deleted files); wrong location | **Delete** in Phase B — superseded by `_meta/` |
| `module-messaging-streaming.md` | Technology Playbook module index | 6 | 3 | 3 | Meta index, not handbook depth; Q26 still points here | **Keep** — update links only |
| `01-fundamentals/_index.md` | Section landing | 4 | 1 | 2 | Placeholder only | **Rewrite** — add module overview + links |
| `01-fundamentals/messaging-patterns.md` | Integration patterns | 6 | 5 | 6 | Overlaps models + core fan-out diagram | **Keep** — trim duplicate troubleshooting; link canonical |
| `01-fundamentals/messaging-models.md` | Queue vs log mental model | 6 | 6 | 7 | Offsets/groups overlap internals + core | **Keep** — reduce Internal Working; link to `kafka-core` |
| `01-fundamentals/queue-vs-stream.md` | Architect queue/stream comparison | 7 | 7 | 8 | ISR/leader mention duplicates internals | **Keep** — canonical for **broker paradigm** only; remove ISR deep dive |
| `01-fundamentals/broker-selection-guide.md` | ADR / selection framework | 7 | 4 | 8 | Overlaps comparisons + cloud page | **Keep** — canonical for **selection ADR** |
| `02-kafka/_index.md` | Section landing | 4 | 1 | 2 | Placeholder | **Rewrite** — reading order + concept map |
| `02-kafka/kafka-core.md` | Topics, partitions, groups, acks | 6 | 8 | 8 | Duplicates ISR, HW, lag, idempotency with internals/troubleshooting | **Keep** — **canonical** for core API concepts; **strip** ISR/replication depth |
| `02-kafka/kafka-internals.md` | Segments, ISR, election, offsets | 6 | 7 | 9 | Also covers rebalance, compaction, page cache | **Keep** — **canonical** for storage + replication; split rebalance to new page (Phase B) |
| `02-kafka/kafka-performance.md` | Tuning, capacity | 6 | 5 | 8 | Hot partition repeated; page cache overlaps internals | **Keep** — **canonical** for performance |
| `02-kafka/kafka-security.md` | TLS, SASL, ACLs | 6 | 3 | 8 | Thin on audit/compliance | **Keep** — **canonical** for security |
| `02-kafka/kafka-operations.md` | Upgrades, KRaft, K8s | 6 | 5 | 8 | KRaft depth insufficient; observability overlaps troubleshooting | **Keep** — **canonical** for operations |
| `02-kafka/kafka-troubleshooting.md` | Runbooks, lag, poison | 7 | 6 | 9 | Best troubleshooting content but repeats rebalance/URP from internals | **Keep** — **canonical** for troubleshooting |
| `02-kafka/kafka-interview-guide.md` | Interview framing | 5 | 8 | 6 | Duplicates summary of all `02-kafka/*` pages; one shortcode answer only | **Merge** into `04-interview-guide/` or reduce to hub linking Top 150 |
| `03-broker-comparisons/_index.md` | Section landing | 4 | 1 | 2 | Placeholder | **Rewrite** |
| `03-broker-comparisons/kafka-vs-rabbitmq.md` | RabbitMQ comparison | 6 | 6 | 8 | **Broken** comparison-table shortcode syntax; hybrid example duplicates fundamentals | **Fix** shortcode; trim duplicated Kafka internals |
| `03-broker-comparisons/kafka-vs-pulsar.md` | Pulsar comparison | 6 | 5 | 7 | BookKeeper/geo shallow | **Keep** — deepen geo-replication in Phase C |
| `03-broker-comparisons/kafka-vs-nats.md` | NATS comparison | 6 | 4 | 6 | JetStream vs core NATS needs clarity | **Keep** |
| `03-broker-comparisons/kafka-vs-redpanda.md` | Redpanda comparison | 6 | 4 | 7 | Migration risks thin | **Keep** |
| `03-broker-comparisons/cloud-messaging-services.md` | Cloud + legacy JMS | 7 | 3 | 8 | Correct consolidation; Event Hubs/MSK shallow | **Keep** — **canonical** for cloud messaging |
| `04-interview-guide/_index.md` | Section landing | 4 | 1 | 3 | Placeholder | **Rewrite** |
| `04-interview-guide/top-150-interview-questions.md` | Question index | 7 | 2 | 9 | `Related Document` = file paths; **no answers**; Q26 points to module index | **Rewrite** column → Hugo Deep Dive; batch answer links |
| `04-interview-guide/architect-questions.md` | Top 25 subset | 6 | 1 | 8 | Questions only — correct for Layer 1 | **Keep** |
| `04-interview-guide/troubleshooting-questions.md` | Top 25 subset | 6 | 1 | 8 | Questions only | **Keep** |
| `04-interview-guide/design-tradeoffs.md` | Top 25 subset | 6 | 1 | 8 | Questions only | **Keep** |
| `04-interview-guide/performance-questions.md` | Top 25 subset | — | — | — | **Missing** | **Create** in Phase B from Top 150 |

**Scoring guide:** Quality = accuracy + production depth + maintainability. Duplication = 1 (unique) – 10 (heavily repeated). Interview Value = usefulness in senior/architect interviews.

---

## Duplicate Content (Semantic Overlap > 60%)

| Concept cluster | Appears in | Canonical target (Phase B) |
| :--- | :--- | :--- |
| ISR, leader, HW, URP | `kafka-core`, `kafka-internals`, `kafka-operations`, `kafka-troubleshooting`, `queue-vs-stream`, comparisons | `02-kafka/kafka-internals.md` |
| Consumer groups + rebalance | `kafka-core`, `kafka-internals`, `kafka-troubleshooting`, `messaging-patterns` | **New:** `02-kafka/kafka-consumer-groups.md` |
| Consumer lag | `kafka-core`, `kafka-performance`, `kafka-troubleshooting`, `kafka-operations` | `02-kafka/kafka-troubleshooting.md` |
| `acks` / durability | `kafka-core`, `kafka-internals`, `kafka-performance`, `kafka-interview-guide` | `02-kafka/kafka-core.md` (+ delivery semantics page) |
| Poison / DLT / schema drift | `kafka-core`, `kafka-troubleshooting`, `messaging-patterns`, fundamentals | `02-kafka/kafka-troubleshooting.md` |
| Partition keys / hot partition | `kafka-core`, `kafka-performance`, `queue-vs-stream`, comparisons | `02-kafka/kafka-performance.md` |
| Hybrid Kafka+RabbitMQ examples | `messaging-patterns`, `queue-vs-stream`, `broker-selection`, `kafka-vs-rabbitmq` | `03-broker-comparisons/kafka-vs-rabbitmq.md` |
| 14-section boilerplate | All `01`–`03` topic pages | Keep structure; **omit empty sections** per template rule |

---

## Missing Topics (Not Canonical Anywhere)

| Topic | Interview priority | Proposed canonical page (Phase B) |
| :--- | :---: | :--- |
| Delivery semantics (at-most/least/exactly-once) | High | `02-kafka/kafka-delivery-semantics.md` |
| Idempotent producer + transactions | High | `02-kafka/kafka-delivery-semantics.md` |
| Schema Registry + compatibility modes | High | `02-kafka/kafka-schema-registry.md` |
| Log compaction + tombstones | Medium | `02-kafka/kafka-internals.md` (section) or split |
| Kafka Connect / CDC | Medium | `02-kafka/kafka-connect.md` |
| Kafka Streams + state stores | Medium | `02-kafka/kafka-streams.md` |
| KRaft internals (vs ZK) | Medium | `02-kafka/kafka-operations.md` (expand) |
| MirrorMaker / multi-region | High | `02-kafka/kafka-multi-region.md` or architect section |
| Cooperative sticky rebalance (deep) | High | `02-kafka/kafka-consumer-groups.md` |
| Tiered storage | Low | `02-kafka/kafka-performance.md` |

---

## Weak Files (Quality < 6 or Interview Value < 6)

| File | Issue |
| :--- | :--- |
| `01-fundamentals/_index.md`, `02-kafka/_index.md`, `03-broker-comparisons/_index.md`, `04-interview-guide/_index.md` | Placeholder stubs |
| `02-kafka/kafka-interview-guide.md` | Redundant hub; no unique depth |
| `refactoring-plan.md` (root) | Obsolete |
| `03-broker-comparisons/kafka-vs-rabbitmq.md` | Broken comparison-table shortcode |

---

## Fragmented Concepts (Need Split or Consolidate)

| Concept | Current state | Phase B action |
| :--- | :--- | :--- |
| Replication / ISR / election | Partially in internals + scattered | Consolidate in `kafka-internals.md`; others link only |
| Consumer groups / rebalance | Split across core, internals, troubleshooting | **Split** `kafka-consumer-groups.md` |
| Delivery / transactions | Scattered bullets in core + interview guide | **Create** `kafka-delivery-semantics.md` |
| Interview answers | 150 questions, ~0 structured answers | Add `## Question` blocks on canonical pages (batched) |

---

## Outdated Content

| Item | Issue |
| :--- | :--- |
| Root `refactoring-plan.md` | References deleted broker stubs |
| Top 150 Q26 | Points to `module-messaging-streaming.md` |
| Top 150 `Related Document` column | Repo paths, not Hugo links |
| `kafka-vs-rabbitmq.md` line 19–33 | Invalid shortcode delimiters (single brace) instead of proper Hugo syntax |

---

## Phase B Action Summary (Pending Approval)

| Priority | Action |
| :---: | :--- |
| P0 | Create `_meta/concept-registry.md` enforcement — trim duplicates per registry |
| P0 | Fix `kafka-vs-rabbitmq.md` shortcode |
| P0 | Top 150: `Deep Dive` Hugo links + `performance-questions.md` |
| P1 | Create `02-kafka/kafka-consumer-groups.md`, `kafka-delivery-semantics.md` |
| P1 | Create `05-learning-paths/` (4 files) |
| P1 | Update `kafka_handbook_modules.yaml` + `kafka_handbook_order.yaml` |
| P2 | Answer layer batch 1 (40 highest-priority questions) |
| P2 | Delete root `refactoring-plan.md`; rewrite section `_index.md` pages |
| P2 | Reduce or merge `kafka-interview-guide.md` |
| P3 | Answer layer batch 2 (remaining 110 questions) |

---

## Phase A Deliverables Checklist

- [x] `_meta/refactoring-plan.md` (this file)
- [x] `_meta/concept-registry.md`
- [x] `_meta/navigation-plan.md`
- [x] `_meta/mermaid-plan.md`
- [x] `_meta/infographic-plan.md`

**STOP — Await approval before Phase B execution.**
