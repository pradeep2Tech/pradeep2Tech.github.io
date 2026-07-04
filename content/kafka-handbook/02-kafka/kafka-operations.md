---
title: "Kafka Operations"
date: 2026-07-03T10:00:00+00:00
draft: false
description: "Upgrades, KRaft, Kubernetes, rolling restarts, and production runbooks."
tags: ["kafka-handbook", "kafka", "messaging", "streaming", "interview"]
categories: ["Kafka Handbook"]
shortTitle: "Operations"
module: 2
moduleTitle: "Apache Kafka"
sectionRef: "2.7"
weight: 207
interviewHandbook: true
---

## Quick Revision

- **Rolling broker restarts** trigger leader election — plan maintenance windows.
- **KRaft** replaces ZooKeeper for metadata quorum.
- **K8s**: StatefulSets/operators, PDBs, persistent volumes.
- Document **replay** and **failover** procedures before incidents.

## Core Concepts

| Operation | Risk |
| :--- | :--- |
| Broker upgrade | Rebalance / leader churn |
| Topic expand partitions | Ordering scope changes |
| Offset reset | Duplicate or skipped processing |
| Cluster expand | Reassignment traffic |

## Internal Working

Controller broker manages partition leadership. Metadata propagates to all brokers and clients.

## Architecture

MSK / Confluent Cloud / Event Hubs reduce day-2 ops; self-hosted needs 24/7 on-call for critical platforms.

## Design Tradeoffs

| Model | Ops ownership |
| :--- | :--- |
| Self-hosted | Full |
| MSK | AWS patches brokers |
| Event Hubs | Kafka protocol subset |

## Production Patterns

- Pre-upgrade compatibility matrix (broker vs client vs connect).
- Failure drills: broker kill, AZ loss, controller failover.

## Scalability

Broker count and partition leadership balance — avoid hotspot leaders.

## Reliability

PDB + RF≥3 + rack awareness for K8s broker upgrades.

## Security

Rotate credentials on schedule; audit topic creation.

## Observability

Runbooks tied to alerts: ISR shrink, offline partitions, controller moves.

## Troubleshooting

Metadata storms after mass topic creation — throttle admin API.

## Common Mistakes

- Upgrading all brokers simultaneously.
- No tested backup for topic configs and ACLs.

## Interview Questions

- What happens during rolling broker restart?
- How do you migrate ZooKeeper to KRaft safely?
- What K8s patterns apply to Kafka at scale?

## Architect Notes

Staff the **operational model** you choose — managed is not zero ops for clients, topics, and ACLs.
