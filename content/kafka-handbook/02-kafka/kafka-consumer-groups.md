---
title: "Kafka Consumer Groups"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "Consumer groups, partition assignment, rebalancing, and cooperative protocols."
tags: ["kafka-handbook", "kafka", "messaging", "streaming", "interview"]
categories: ["Kafka Handbook"]
shortTitle: "Consumer Groups"
module: 2
moduleTitle: "Apache Kafka"
sectionRef: "2.3"
weight: 203
interviewHandbook: true
---

## Quick Revision

- A **consumer group** is a scaled pool sharing one logical subscription to a topic.
- Each partition is consumed by **at most one** consumer in the group at a time.
- **Rebalance** redistributes partitions when members join, leave, or miss heartbeats.
- Max parallelism per group = **partition count**.

## Core Concepts

| Term | Meaning |
| :--- | :--- |
| Group coordinator | Broker managing group membership |
| Group leader | Consumer driving partition assignment (not partition leader) |
| Assignment | Which consumer owns which partition |
| Rebalance | Stop-the-world or cooperative partition handoff |
| Static membership | `group.instance.id` reduces rebalance churn |

## Internal Working

On join, consumers send `JoinGroup`; the group leader receives partition metadata and runs an **assignor** (range, round-robin, sticky, cooperative sticky). Assignment is written to the coordinator; consumers receive new partitions and may need to **reset fetch positions** from committed offsets in `__consumer_offsets`.

```mermaid
flowchart TB
  T[Topic: 4 partitions] --> G[Consumer Group]
  G --> C1[Consumer A: P0, P1]
  G --> C2[Consumer B: P2, P3]
  G --> C3[Consumer C: idle]
```

**Rebalance triggers:** consumer join/leave, subscription change, `session.timeout.ms` expiry, `max.poll.interval.ms` exceeded (poll loop blocked).

```mermaid
sequenceDiagram
    participant C1 as Consumer 1
    participant C2 as Consumer 2
    participant Coord as Group Coordinator
    C1->>Coord: JoinGroup
    C2->>Coord: JoinGroup
    Coord-->>C1: Assignment: P0,P1
    Coord-->>C2: Assignment: P2,P3
    Note over C1,C2: Revoke → commit offsets → assign → resume fetch
```

## Architecture

Separate groups on the same topic enable **fan-out** (inventory vs analytics). Never share one group across unrelated microservices — coupling scaling and failure domains.

## Design Tradeoffs

| Strategy | Upside | Downside |
| :--- | :--- | :--- |
| More consumers | Higher throughput | Useless beyond partition count |
| Cooperative sticky | Less duplicate processing | Client/broker version requirements |
| Static membership | Fewer rebalances on restart | Ops discipline on instance IDs |
| Long `max.poll.interval` | Slow handlers tolerated | Slower failure detection |

## Production Patterns

- Size consumers ≤ partitions; scale partitions before consumers for campaigns.
- Use **cooperative-sticky** assignor for rolling deploys.
- Commit offsets **after** side effects succeed (at-least-once).

## Scalability

Adding a 5th consumer to a 4-partition topic leaves one consumer idle.

## Reliability

Rebalance causes **duplicate delivery** window — handlers must be idempotent. See [Delivery Semantics](/kafka-handbook/02-kafka/kafka-delivery-semantics/).

## Security

ACLs on `GROUP` resource per service principal.

## Observability

`records-lag-max`, rebalance rate metric, consumer group state (`Stable`, `PreparingRebalance`).

## Troubleshooting

Rebalance loops → `max.poll.interval.ms` too low for handler duration. See [Kafka Troubleshooting](/kafka-handbook/02-kafka/kafka-troubleshooting/).

## Common Mistakes

- Long synchronous DB calls inside poll loop without raising `max.poll.interval.ms`.
- Multiple services in one group name.

## Interview Questions

- How do consumer groups divide partition ownership?
- What triggers a rebalance storm?
- How does cooperative sticky rebalancing differ from eager?

## Architect Notes

Partition plan and consumer group boundaries are **architecture decisions**, not afterthoughts.

## Checklists

- [ ] Group name encodes service + environment
- [ ] `max.poll.interval.ms` validated under P99 handler time
- [ ] Idempotent handlers verified under forced rebalance test
