---
title: "Kafka vs Pulsar"
date: 2026-07-03T10:00:00+00:00
draft: false
description: "Multi-tenant streaming, BookKeeper storage, and geo-replication trade-offs."
tags: ["kafka-handbook", "kafka", "messaging", "streaming", "interview"]
categories: ["Kafka Handbook"]
shortTitle: "vs Pulsar"
module: 3
moduleTitle: "Broker Comparisons"
sectionRef: "3.2"
weight: 302
interviewHandbook: true
---

{{< comparison-table caption="Kafka vs Pulsar" >}}
| Dimension | Kafka | Pulsar |
| :--- | :--- | :--- |
| **Throughput** | Very high (batching) | Very high |
| **Latency** | Tunable; batching adds tail | Comparable |
| **Ordering** | Per partition | Per partition |
| **Replay** | Native offset reset | Native |
| **Multi-tenancy** | Cluster + ACLs | Built-in multi-tenant |
| **Scalability** | Partitions + brokers | Brokers + BookKeeper |
| **Operations** | Partitions, ISR, rebalance | BookKeeper + broker tiers |
| **Cost** | TCO staffing + infra | Higher operational surface |
| **Reliability** | RF + ISR + acks | Quorum storage |
| **Kubernetes** | Operators / Strimzi | Pulsar Helm |
| **Best use cases** | Event streaming, CDC, analytics | Multi-tenant, geo-replication |
{{< /comparison-table >}}

## Quick Revision

- Pulsar: **unified queue + log**, strong **multi-tenancy** and **geo-replication**.
- Kafka: larger ecosystem; simpler mental model for many teams.

## Core Concepts

Pulsar separates **serving** (brokers) from **storage** (BookKeeper).

## Internal Working

Geo-replication built-in vs Kafka MirrorMaker 2 add-on.

## Architecture

Choose Pulsar when **tenant isolation** and **geo** are first-class ADR requirements.

## Design Tradeoffs

Pulsar ops learning curve vs Kafka talent pool.

## Production Patterns

Evaluate Pulsar for SaaS event platforms with per-customer namespaces.

## Scalability

Both scale horizontally; Pulsar bookie tier adds planning dimension.

## Reliability

BookKeeper quorum vs Kafka ISR — different failure models.

## Security

Pulsar namespace policies vs Kafka ACLs.

## Observability

Comparable metrics; different tooling.

## Troubleshooting

BookKeeper ensemble issues ≠ Kafka ISR issues — runbooks differ.

## Common Mistakes

Picking Pulsar without BookKeeper ops experience.

## Interview Questions

- When does Pulsar beat Kafka for multi-tenant streaming?
- How does geo-replication compare to MirrorMaker?

## Architect Notes

[Queue vs Stream](/kafka-handbook/01-fundamentals/queue-vs-stream/)
