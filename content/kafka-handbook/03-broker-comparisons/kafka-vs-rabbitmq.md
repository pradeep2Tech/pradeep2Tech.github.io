---
title: "Kafka vs RabbitMQ"
date: 2026-07-03T10:00:00+00:00
draft: false
description: "Log vs queue — throughput, ordering, replay, and operational complexity."
tags: ["kafka-handbook", "kafka", "messaging", "streaming", "interview"]
categories: ["Kafka Handbook"]
shortTitle: "vs RabbitMQ"
module: 3
moduleTitle: "Broker Comparisons"
sectionRef: "3.1"
weight: 301
aliases:
  - /kafka-handbook/rabbitmq/
ShowToc: true
interviewHandbook: true
---

{{< comparison-table caption="Kafka vs RabbitMQ" >}}
| Dimension | Kafka | RabbitMQ |
| :--- | :--- | :--- |
| **Throughput** | Very high (batching) | High |
| **Latency** | Tunable; batching adds tail | Lower per-message |
| **Ordering** | Per partition | Per queue (single consumer) |
| **Replay** | Native offset reset | DLQ / manual |
| **Multi-tenancy** | Cluster + ACLs | vhost isolation |
| **Scalability** | Partitions + brokers | Queues + consumers |
| **Operations** | Partitions, ISR, rebalance | Moderate broker HA |
| **Cost** | TCO staffing + infra | Lower at small scale |
| **Reliability** | RF + ISR + acks | Ack + mirrors |
| **Kubernetes** | Operators / Strimzi | Helm charts |
| **Best use cases** | Event streaming, CDC, analytics | Task queues, routing, RPC |
{{< /comparison-table >}}

## Quick Revision

- Kafka = **log**; RabbitMQ = **broker routing to queues**.
- Kafka for fan-out + replay; RabbitMQ for task distribution + complex routing.
- Hybrid platforms are normal.

## Core Concepts

| Pain | Kafka | RabbitMQ |
| :--- | :--- | :--- |
| Massive fan-out | Consumer groups | Exchanges + bindings |
| Replay | Offset reset | DLQ patterns |
| Task routing | Awkward | Native |
| Per-entity order | Partition key | Single active consumer |

## Internal Working

RabbitMQ removes messages on ack. Kafka retains per policy.

## Architecture

```mermaid
flowchart LR
  subgraph kafkaPath [Kafka streaming]
    p1[Order Service] --> log[(Topic)]
    log --> c1[Inventory Group]
    log --> c2[Analytics Group]
  end
  subgraph rabbitPath [RabbitMQ tasks]
    p2[Payment Service] --> ex{Exchange}
    ex --> q1[Retry Queue]
    ex --> w1[Worker]
  end
```

## Design Tradeoffs

See matrix above. Anti-pattern: RabbitMQ as analytics source of truth without retention.

## Production Patterns

| Flow | Choice |
| :--- | :--- |
| Order events to warehouse + CRM + lake | Kafka |
| Payment retry TTL ladder | RabbitMQ |
| Fraud priority dispatch | RabbitMQ |

## Scalability

Kafka wins extreme throughput; RabbitMQ wins flexible routing at moderate scale.

## Reliability

Both: at-least-once + idempotent consumers + DLQ.

## Security

AMQP TLS + vhosts vs Kafka TLS + ACLs.

## Observability

Queue depth vs consumer lag.

## Troubleshooting

| Failure | Kafka | RabbitMQ |
| :--- | :--- | :--- |
| Poison message | Stuck offset / DLT | DLQ fills |
| Upgrade | Rebalance storm | Mirror queue migration |

## Common Mistakes

- Forcing one broker for everything.

## Interview Questions

- When pick Kafka over RabbitMQ?
- How does replay differ?
- Describe a hybrid architecture.

## Architect Notes

[Broker Selection Guide](/kafka-handbook/01-fundamentals/broker-selection-guide/)
