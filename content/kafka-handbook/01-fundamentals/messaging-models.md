---
title: "Messaging Models"
date: 2026-07-03T10:00:00+00:00
draft: false
description: "Queue versus log mental models, offsets, and consumer progress."
tags: ["kafka-handbook", "kafka", "messaging", "streaming", "interview"]
categories: ["Kafka Handbook"]
shortTitle: "Models"
module: 1
moduleTitle: "Fundamentals"
sectionRef: "1.2"
weight: 102
ShowToc: true
interviewHandbook: true
---

## Quick Revision

- **Queue mental model**: message removed after ack; work distribution.
- **Log mental model**: append-only, retained, replayable; consumers track offsets.
- **Stream processing**: continuous consumption over the log.
- **Broker vs log**: RabbitMQ routes to queues; Kafka appends to partitions.

## Core Concepts

| Model | State | Consumer progress |
| :--- | :--- | :--- |
| Classic queue | Ephemeral per queue | Ack removes message |
| Durable log | Retained by policy | Offset per group |
| Stream table | Compacted changelog | Latest key wins |
| Cloud queue (SQS) | Managed, limited retention | Visibility timeout |

## Internal Working

Kafka brokers assign **monotonic offsets** per partition. Consumer groups commit offsets to `__consumer_offsets` (internal compacted topic).

## Architecture

Brokers are **dumb logs, smart clients** — routing and batching logic lives in producers/consumers and client libraries.

## Design Tradeoffs

| Dimension | Queue | Log |
| :--- | :--- | :--- |
| Replay | Manual / DLQ | Native offset reset |
| Retention | Until ack | Time or compaction |
| Fan-out | Bindings / topics | Consumer groups |
| Ops focus | Broker HA | Partitions + ISR |

## Production Patterns

- Pick log semantics when events are a **durable product asset** (analytics, audit, CDC).
- Pick queue semantics for **task ladders** (retry TTL, priority routing).

## Scalability

Logs scale via partition count; queues scale via competing consumers (with ordering trade-offs).

## Reliability

Define delivery semantics explicitly: at-most-once, at-least-once, exactly-once (usually bounded to Kafka pipeline, not end-to-end DB).

## Security

Encryption in transit mandatory; consider payload encryption for PII fields in shared clusters.

## Observability

Model-specific metrics: queue **depth** vs Kafka **consumer lag**.

## Troubleshooting

Misaligned mental model causes teams to expect queue behavior (message disappearance) from a retained log.

## Common Mistakes

- Treating Kafka like a job queue without retention planning.
- Expecting global ordering on a distributed log.

## Interview Questions

- Why is Kafka described as a commit log rather than a message queue?
- How does offset-based progress differ from per-message acknowledgement?
- When does a cloud managed queue replace a self-hosted log?

## Architect Notes

Align stakeholders on **mental model** before technology selection — most integration failures are expectation mismatches.

## See Also

- [Queue vs Stream](/kafka-handbook/01-fundamentals/queue-vs-stream/)
- [Kafka Core](/kafka-handbook/02-kafka/kafka-core/)
