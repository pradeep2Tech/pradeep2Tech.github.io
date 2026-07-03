---
title: "Cloud Messaging Services"
date: 2026-07-03T10:00:00+00:00
draft: false
description: "Kafka vs SQS, SNS, Pub/Sub, Service Bus, Event Hubs, and legacy JMS platforms."
tags: ["kafka-handbook", "kafka", "messaging", "streaming", "interview"]
categories: ["Kafka Handbook"]
shortTitle: "Cloud Messaging"
module: 3
moduleTitle: "Broker Comparisons"
sectionRef: "3.5"
weight: 305
ShowToc: true
interviewHandbook: true
---

## Quick Revision

- Interview topic: **Kafka vs managed cloud messaging** — not individual SKU trivia.
- AWS: **SQS** (queue), **SNS** (fan-out), **MSK** (Kafka managed).
- Azure: **Event Hubs** (Kafka protocol), **Service Bus** (sessions/DLQ).
- GCP: **Pub/Sub**. Legacy: **ActiveMQ**, **IBM MQ** (JMS enterprise).

## Core Concepts

{{< comparison-table caption="Kafka vs managed cloud messaging" >}}
| Dimension | Self-hosted / MSK Kafka | SQS / Pub/Sub / Service Bus |
| :--- | :--- | :--- |
| **Throughput** | Very high | High; per-service limits |
| **Latency** | Tunable | Low–moderate |
| **Ordering** | Partition keys | FIFO queues / sessions (limited) |
| **Replay** | Full | Limited or none |
| **Multi-tenancy** | ACLs / IAM | Cloud IAM + namespaces |
| **Scalability** | You plan partitions | Elastic managed |
| **Operations** | High (or MSK partial) | Minimal |
| **Cost** | Infra + staffing | Per-request / throughput units |
| **Reliability** | You configure RF/ISR | Provider SLA |
| **Kubernetes** | Strimzi / operators | SDK + IAM |
| **Best use cases** | Event backbone, CDC | Decouple without broker ops |
{{< /comparison-table >}}

## Internal Working

**SNS → SQS fan-out** parallels multiple consumer groups but without long retention replay. **Event Hubs** exposes Kafka protocol for many clients.

## Architecture

| Cloud | Kafka-aligned | Queue / bus |
| :--- | :--- | :--- |
| AWS | MSK, EventBridge+Kinesis | SQS, SNS |
| Azure | Event Hubs | Service Bus |
| GCP | — | Pub/Sub |

## Design Tradeoffs

Choose cloud queues when team cannot run broker HA and **replay is not required**. Choose Event Hubs/MSK when Kafka clients exist but ops must shrink.

## Production Patterns

- Hybrid: Kafka on-prem + Event Hubs bridge for cloud consumers.
- Legacy JMS (ActiveMQ/IBM MQ): migrate via CDC/outbox to Kafka over big-bang.

## Scalability

Cloud quotas and throttling replace partition math — monitor account limits.

## Reliability

DLQ patterns on Service Bus/SQS; not equivalent to offset replay.

## Security

IAM roles per producer/consumer; private link for compliance.

## Observability

Cloud-native metrics (ApproximateAgeOfOldestMessage, subscription backlog).

## Troubleshooting

| Issue | Cloud signal |
| :--- | :--- |
| Backlog | Queue depth / oldest age |
| Duplicates | Visibility timeout too low |
| Ordering break | Not using FIFO/session features |

## Common Mistakes

- Expecting Kafka replay semantics from standard SQS.
- Running IBM MQ **and** Kafka forever without migration map.

## Interview Questions

- When is SQS right over Kafka?
- How does SNS+SQS fan-out differ from consumer groups?
- Event Hubs vs self-hosted Kafka — ops ownership shift?

## Architect Notes

Consolidated comparison for **architect interviews** — depth on trade-offs, not console walkthroughs.
