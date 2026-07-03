---
title: "Queue vs Stream"
date: 2026-07-03T10:00:00+00:00
draft: false
description: "Architect comparison of queue and log/stream messaging semantics."
tags: ["kafka-handbook", "kafka", "messaging", "streaming", "interview"]
categories: ["Kafka Handbook"]
shortTitle: "Queue vs Stream"
module: 1
moduleTitle: "Fundamentals"
sectionRef: "1.3"
weight: 103
ShowToc: true
interviewHandbook: true
---

## Quick Revision

- **Queue**: compete for messages; typically delete on ack.
- **Stream/log**: append, retain, replay; partition-scoped ordering.
- **Throughput**: logs win at extreme fan-out and replay.
- **Routing**: queues win on flexible AMQP-style bindings.

## Core Concepts

{{< comparison-table caption="Queue vs stream — architect view" >}}
| Dimension | Queue (AMQP/SQS) | Stream (Kafka) |
| :--- | :--- | :--- |
| Throughput | High | Very high with batching |
| Latency | Low per message | Tunable; batching adds tail latency |
| Ordering | Per queue (single consumer) | Per partition |
| Replay | DLQ / manual | Offset reset |
| Retention | Short / until ack | Days to forever (compacted) |
| Multi-subscriber | Exchanges / SNS fan-out | Consumer groups |
| Ops complexity | Moderate | Higher (partitions, ISR, rebalance) |
{{< /comparison-table >}}

## Internal Working

Streams use **partition leaders + ISR replication**. Queues use **broker routing tables** and per-queue ack state.

## Architecture

Use streams as **system of record for events**; use queues as **work distributors** with complex routing.

## Design Tradeoffs

Hybrid architectures are normal: Kafka for `OrderPlaced` fan-out; RabbitMQ for payment retry ladders.

## Production Patterns

- Partition keys: `customerId`, `orderId` — never random UUID when order matters.
- DLQ + replay runbooks on both models.

## Scalability

Stream scale ceiling = partitions × broker I/O. Queue scale = consumers × broker capacity.

## Reliability

At-least-once + idempotent consumers on both sides.

## Security

Managed queues reduce ops burden but limit replay and fine-grained ACL models.

## Observability

Queue depth alerts vs Kafka lag alerts — different SLOs.

## Troubleshooting

| Symptom | Queue likely cause | Stream likely cause |
| :--- | :--- | :--- |
| Backlog | Slow workers | Lag / hot partition |
| Duplicates | Redelivery after visibility timeout | Rebalance / retry |
| Lost messages | Ack before process | acks=1 + leader failure |

## Common Mistakes

- Forcing one broker for all integration shapes.
- Using RabbitMQ as analytics source of truth without retention.

## Interview Questions

- Why is global ordering expensive on a stream platform?
- When would you choose retention over disappearance after ack?
- How does replay change incident response for downstream bugs?

## Architect Notes

Document **which flows are log-shaped vs queue-shaped** in your platform map — interviewers probe hybrid fluency.

## See Also

- [Messaging Models](/kafka-handbook/01-fundamentals/messaging-models/)
- [Broker Selection](/kafka-handbook/01-fundamentals/broker-selection-guide/)
