---
title: "Kafka vs NATS"
date: 2026-07-03T10:00:00+00:00
draft: false
description: "Low-latency messaging and JetStream versus Kafka log platform."
tags: ["kafka-handbook", "kafka", "messaging", "streaming", "interview"]
categories: ["Kafka Handbook"]
shortTitle: "vs NATS"
module: 3
moduleTitle: "Broker Comparisons"
sectionRef: "3.3"
weight: 303
ShowToc: true
interviewHandbook: true
---

{{< comparison-table caption="Kafka vs NATS" >}}
| Dimension | Kafka | NATS |
| :--- | :--- | :--- |
| **Throughput** | Very high (batching) | High (JetStream) |
| **Latency** | Tunable; batching adds tail | Very low |
| **Ordering** | Per partition | Stream limits |
| **Replay** | Native offset reset | JetStream |
| **Multi-tenancy** | Cluster + ACLs | Accounts |
| **Scalability** | Partitions + brokers | Lightweight nodes |
| **Operations** | Partitions, ISR, rebalance | Low footprint |
| **Cost** | TCO staffing + infra | Lower for edge |
| **Reliability** | RF + ISR + acks | JetStream quorum |
| **Kubernetes** | Operators / Strimzi | NATS operator |
| **Best use cases** | Event streaming, CDC, analytics | Edge, control plane, signaling |
{{< /comparison-table >}}

## Quick Revision

- NATS: **low latency**, lightweight; JetStream adds persistence.
- Kafka: heavy-duty retention, ecosystem, stream processing.

## Core Concepts

NATS core is fire-and-forget; JetStream adds log semantics closer to Kafka.

## Internal Working

Different protocol and persistence layer — not drop-in Kafka replacement.

## Architecture

NATS at **edge** and **control plane**; Kafka as **central event backbone**.

## Design Tradeoffs

JetStream vs Kafka when persistence needed at small/medium scale.

## Production Patterns

IoT telemetry ingress on NATS → aggregate to Kafka for analytics.

## Scalability

NATS excels at connection count; Kafka at retained volume.

## Reliability

Define persistence tier explicitly — core NATS is not Kafka.

## Security

NATS accounts/JWT vs Kafka ACLs.

## Observability

Connection churn vs lag metrics.

## Troubleshooting

Confusing core NATS with durable JetStream semantics.

## Common Mistakes

Using NATS core for durable financial events without JetStream.

## Interview Questions

- When prefer NATS over Kafka at the edge?
- What does JetStream add?

## Architect Notes

Compare **latency SLO** and **retention** requirements first.
