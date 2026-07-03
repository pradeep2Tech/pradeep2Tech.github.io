---
title: "Kafka Performance"
date: 2026-07-03T10:00:00+00:00
draft: false
description: "Throughput, latency, batching, compression, and capacity planning."
tags: ["kafka-handbook", "kafka", "messaging", "streaming", "interview"]
categories: ["Kafka Handbook"]
shortTitle: "Performance"
module: 2
moduleTitle: "Apache Kafka"
sectionRef: "2.5"
weight: 205
ShowToc: true
interviewHandbook: true
---

## Quick Revision

- **Batching** (`linger.ms`, `batch.size`) trades latency for throughput.
- **Compression** on producer reduces network; broker may recompress.
- **Partition count** caps parallel consumers per group.
- **Page cache** drives read performance for recent data.

## Core Concepts

| Knob | Effect |
| :--- | :--- |
| `linger.ms` | Wait to fill batch |
| `batch.size` | Upper batch bytes |
| `compression.type` | lz4 / zstd / snappy |
| `fetch.min.bytes` | Consumer batching |
| `num.io.threads` | Broker disk parallelism |

## Internal Working

Producers pipeline batches per partition. Brokers append sequentially — random writes are the enemy.

## Architecture

Capacity plan: peak RPS × payload × retention × RF = disk; ingress/egress bandwidth per broker.

## Design Tradeoffs

| Goal | Tuning |
| :--- | :--- |
| Throughput | Larger batches, lz4/zstd |
| Low latency | `linger.ms=0`, smaller batches |
| Cost | Tiered storage / shorter retention |

## Production Patterns

- Load-test **producer and consumer** independently before campaigns.
- Right-size brokers: network + NVMe; avoid CPU-bound GC pauses.

## Scalability

Adding consumers stops helping when `consumers >= partitions`.

## Reliability

Performance tuning must not drop `acks=all` on critical paths without explicit risk acceptance.

## Security

Compression does not replace encryption.

## Observability

p99 produce/fetch latency, broker disk %util, consumer `records-lag-max`.

## Troubleshooting

GC pauses → producer timeouts. Disk saturation → fetch latency spikes.

## Common Mistakes

- Optimizing throughput until latency SLO breaks.
- Hot partition from poor key choice.

## Interview Questions

- How do batch size and linger interact?
- When does partition count stop helping lag?
- What capacity math for 30-day retention RF=3?

## Architect Notes

State **SLOs first** (p99 latency vs MB/s), then tune — not the reverse.

## See Also

- [Kafka Internals](/kafka-handbook/02-kafka/kafka-internals/)
- [Consumer Groups](/kafka-handbook/02-kafka/kafka-consumer-groups/)
- [Performance Questions](/kafka-handbook/04-interview-guide/performance-questions/)
