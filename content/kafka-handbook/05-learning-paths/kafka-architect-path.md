---
title: "Architect Path"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "Kafka path for architects — broker selection, platform ADRs, comparisons, and enterprise trade-offs."
tags: ["kafka-handbook", "kafka", "messaging", "streaming", "interview", "learning-path"]
categories: ["Kafka Handbook"]
shortTitle: "Architect"
module: 5
moduleTitle: "Learning Paths"
sectionRef: "5.3"
weight: 503
ShowToc: true
interviewHandbook: true
---

# Architect Path

**Audience:** Solution and platform architects evaluating event backbones and multi-broker estates.  
**Time:** ~6–8 hours focused on ADRs and comparisons.  
**Outcome:** Defend Kafka (or alternatives) in ADRs with ordering, ops, cost, and cloud trade-offs.

## Reading Order

1. [Messaging Patterns](/kafka-handbook/01-fundamentals/messaging-patterns/) — pub/sub, event-carried state, CDC
2. [Broker Selection Guide](/kafka-handbook/01-fundamentals/broker-selection-guide/) — ADR criteria
3. [Kafka Core](/kafka-handbook/02-kafka/kafka-core/) — platform capabilities and limits
4. [Kafka vs RabbitMQ](/kafka-handbook/03-broker-comparisons/kafka-vs-rabbitmq/)
5. [Kafka vs Pulsar](/kafka-handbook/03-broker-comparisons/kafka-vs-pulsar/)
6. [Kafka vs NATS](/kafka-handbook/03-broker-comparisons/kafka-vs-nats/)
7. [Kafka vs Redpanda](/kafka-handbook/03-broker-comparisons/kafka-vs-redpanda/)
8. [Cloud Messaging Services](/kafka-handbook/03-broker-comparisons/cloud-messaging-services/) — MSK, Confluent Cloud, SQS/Pub/Sub
9. [Kafka Internals](/kafka-handbook/02-kafka/kafka-internals/) — ISR, compaction for CDC topics
10. [Delivery Semantics](/kafka-handbook/02-kafka/kafka-delivery-semantics/) — EOS boundaries across services

## Practice

- [Architect-Level Questions](/kafka-handbook/04-interview-guide/architect-questions/)
- [Design & Architecture Questions](/kafka-handbook/04-interview-guide/design-tradeoffs/)

## ADR Prompts

| Decision | Handbook anchors |
| :--- | :--- |
| Event backbone | Broker selection guide + cloud comparison |
| Ordering SLO | Core + performance (partition keys) |
| Multi-region | Operations + internals (RF, min ISR) |
| Managed vs self-hosted | Cloud messaging + operations cost |

## See Also

- [How to Choose a Message Broker](/technology-playbook/how-to-choose-message-broker/)
- [Event-Driven Architecture](/microservices/event-driven-architecture-log-streaming/)
