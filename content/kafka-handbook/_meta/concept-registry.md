---
title: "Kafka Concept Registry"
date: 2026-07-03T12:00:00+00:00
draft: true
description: "Canonical source mapping — one authoritative page per Kafka concept."
tags: ["kafka-handbook", "meta", "planning"]
---

# Kafka Concept Registry

**Rule:** Full explanation lives on the canonical page only. All other pages: **≤ 2 sentences** + link.

**Status:** Phase A — registry defined; enforcement in Phase B/C.

---

## Core Platform

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| Commit log mental model | `01-fundamentals/messaging-models.md` | Exists | Link from all Kafka pages |
| Queue vs stream paradigm | `01-fundamentals/queue-vs-stream.md` | Exists | Not for ISR/storage depth |
| Integration patterns (fan-out, saga) | `01-fundamentals/messaging-patterns.md` | Exists | |
| Broker selection / ADR | `01-fundamentals/broker-selection-guide.md` | Exists | |

---

## Kafka API & Semantics

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| Topics | `02-kafka/kafka-core.md` | Exists | |
| Partitions | `02-kafka/kafka-core.md` | Exists | |
| Partition keys / ordering scope | `02-kafka/kafka-core.md` | Exists | Hot-partition → link performance |
| Producers | `02-kafka/kafka-core.md` | Exists | |
| `acks` configuration | `02-kafka/kafka-core.md` | Exists | |
| Consumers (pull model) | `02-kafka/kafka-core.md` | Exists | |
| Offsets (concept) | `02-kafka/kafka-core.md` | Exists | Storage → internals |
| Consumer groups | `02-kafka/kafka-consumer-groups.md` | **Planned** | Split from core/internals |
| Rebalancing | `02-kafka/kafka-consumer-groups.md` | **Planned** | |
| `session.timeout.ms` / `max.poll.interval.ms` | `02-kafka/kafka-consumer-groups.md` | **Planned** | |
| Cooperative sticky rebalance | `02-kafka/kafka-consumer-groups.md` | **Planned** | |
| Delivery semantics (at-most/least/exactly-once) | `02-kafka/kafka-delivery-semantics.md` | **Planned** | |
| Idempotent producer | `02-kafka/kafka-delivery-semantics.md` | **Planned** | |
| Kafka transactions | `02-kafka/kafka-delivery-semantics.md` | **Planned** | |
| End-to-end exactly-once (Kafka + DB) | `02-kafka/kafka-delivery-semantics.md` | **Planned** | Outbox/CDC refs |

---

## Storage & Replication

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| Log segments (`.log`, `.index`) | `02-kafka/kafka-internals.md` | Exists | |
| Sparse offset index | `02-kafka/kafka-internals.md` | Exists | |
| Page cache / sequential I/O | `02-kafka/kafka-internals.md` | Exists | Performance links here |
| Replication factor | `02-kafka/kafka-internals.md` | Exists | |
| ISR (In-Sync Replicas) | `02-kafka/kafka-internals.md` | Exists | **Primary** ISR source |
| High watermark | `02-kafka/kafka-internals.md` | Exists | |
| Leader election | `02-kafka/kafka-internals.md` | Exists | |
| Unclean leader election | `02-kafka/kafka-internals.md` | Exists | |
| Under-replicated partitions (URP) | `02-kafka/kafka-internals.md` | Exists | Troubleshooting links |
| `min.insync.replicas` | `02-kafka/kafka-internals.md` | Exists | |
| Log compaction / tombstones | `02-kafka/kafka-internals.md` | Exists | Expand in Phase C |
| `__consumer_offsets` topic | `02-kafka/kafka-internals.md` | Exists | |
| Controller / metadata | `02-kafka/kafka-internals.md` | Exists | KRaft detail → operations |
| KRaft vs ZooKeeper | `02-kafka/kafka-operations.md` | Exists | Expand internals cross-link |

---

## Performance & Capacity

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| Producer batching (`linger.ms`, `batch.size`) | `02-kafka/kafka-performance.md` | Exists | |
| Compression codecs | `02-kafka/kafka-performance.md` | Exists | |
| Consumer fetch tuning | `02-kafka/kafka-performance.md` | Exists | |
| Hot partition / skew | `02-kafka/kafka-performance.md` | Exists | |
| Partition count planning | `02-kafka/kafka-performance.md` | Exists | |
| Capacity planning (disk/bandwidth) | `02-kafka/kafka-performance.md` | Exists | |
| Broker JVM / thread tuning | `02-kafka/kafka-performance.md` | Exists | |
| Tiered storage | `02-kafka/kafka-performance.md` | **Planned** | Add section Phase C |

---

## Reliability & Data Integrity

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| At-least-once + idempotent consumers | `02-kafka/kafka-delivery-semantics.md` | **Planned** | |
| Rack awareness / AZ placement | `02-kafka/kafka-internals.md` | Exists | |
| Schema Registry | `02-kafka/kafka-schema-registry.md` | **Planned** | |
| Schema compatibility modes | `02-kafka/kafka-schema-registry.md` | **Planned** | |
| Poison messages / DLT | `02-kafka/kafka-troubleshooting.md` | Exists | |
| Offset reset / replay | `02-kafka/kafka-troubleshooting.md` | Exists | |
| Disaster recovery / backup | `02-kafka/kafka-operations.md` | Exists | Expand Phase C |

---

## Security

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| mTLS | `02-kafka/kafka-security.md` | Exists | |
| SASL (SCRAM, OAuth) | `02-kafka/kafka-security.md` | Exists | |
| ACLs | `02-kafka/kafka-security.md` | Exists | |
| Encryption at rest | `02-kafka/kafka-security.md` | Exists | |
| Multi-tenant isolation | `02-kafka/kafka-security.md` | Exists | Pulsar comparison refs security |

---

## Observability

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| Consumer lag | `02-kafka/kafka-troubleshooting.md` | Exists | Metric definition |
| ISR shrink alerts | `02-kafka/kafka-operations.md` | Exists | |
| Produce/fetch latency SLOs | `02-kafka/kafka-performance.md` | Exists | |
| Distributed tracing (headers) | `02-kafka/kafka-operations.md` | Exists | |

---

## Operations

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| Rolling broker upgrades | `02-kafka/kafka-operations.md` | Exists | |
| KRaft migration | `02-kafka/kafka-operations.md` | Exists | |
| Kubernetes (operators, PDB, PV) | `02-kafka/kafka-operations.md` | Exists | |
| MSK / Confluent Cloud / Event Hubs | `02-kafka/kafka-operations.md` | Exists | Cloud detail → cloud-messaging |
| Topic expansion | `02-kafka/kafka-operations.md` | Exists | |
| Multi-region / MirrorMaker | `02-kafka/kafka-multi-region.md` | **Planned** | |

---

## Ecosystem

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| Kafka Connect / CDC | `02-kafka/kafka-connect.md` | **Planned** | |
| Kafka Streams / state stores | `02-kafka/kafka-streams.md` | **Planned** | |
| Transactional outbox | `02-kafka/kafka-delivery-semantics.md` | **Planned** | Link microservices externally |

---

## Troubleshooting (Symptom → Runbook)

| Concept | Canonical Page | Status | Notes |
| :--- | :--- | :--- | :--- |
| Lag spike isolation | `02-kafka/kafka-troubleshooting.md` | Exists | |
| Rebalance loops | `02-kafka/kafka-troubleshooting.md` | Exists | Root cause → consumer-groups |
| NOT_LEADER_FOR_PARTITION | `02-kafka/kafka-troubleshooting.md` | Exists | |
| Disk full / retention emergencies | `02-kafka/kafka-troubleshooting.md` | Exists | |
| Metadata request storms | `02-kafka/kafka-troubleshooting.md` | Exists | |
| Authorization failures | `02-kafka/kafka-troubleshooting.md` | Exists | Link security |

---

## Broker Comparisons (Non-Kafka Canonical)

| Concept | Canonical Page | Status |
| :--- | :--- | :--- |
| Kafka vs RabbitMQ | `03-broker-comparisons/kafka-vs-rabbitmq.md` | Exists |
| Kafka vs Pulsar | `03-broker-comparisons/kafka-vs-pulsar.md` | Exists |
| Kafka vs NATS | `03-broker-comparisons/kafka-vs-nats.md` | Exists |
| Kafka vs Redpanda | `03-broker-comparisons/kafka-vs-redpanda.md` | Exists |
| Kafka vs cloud messaging | `03-broker-comparisons/cloud-messaging-services.md` | Exists |

---

## Interview Layer

| Concept | Canonical Page | Status |
| :--- | :--- | :--- |
| Question index (150) | `04-interview-guide/top-150-interview-questions.md` | Exists — needs Deep Dive links |
| Structured answers | Canonical topic pages (`## Question` headings) | **Not started** |

---

## Enforcement Checklist (Phase B)

1. Grep handbook for each concept keyword; verify ≤ 2 sentences outside canonical page.
2. Add **See also** link to canonical page from non-canonical mentions.
3. Top 150 `Deep Dive` column must resolve to canonical page `##` anchor.
4. New pages require registry row before merge.
