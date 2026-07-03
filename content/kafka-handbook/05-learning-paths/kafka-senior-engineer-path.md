---
title: "Senior Engineer Path"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "Production-ready Kafka path for senior engineers — producers, consumers, semantics, and ops basics."
tags: ["kafka-handbook", "kafka", "messaging", "streaming", "interview", "learning-path"]
categories: ["Kafka Handbook"]
shortTitle: "Senior Engineer"
module: 5
moduleTitle: "Learning Paths"
sectionRef: "5.1"
weight: 501
ShowToc: true
interviewHandbook: true
---

# Senior Engineer Path

**Audience:** Senior engineers (5–8 years) shipping Kafka producers and consumers in production.  
**Time:** ~6–8 hours across multiple sessions.  
**Outcome:** Design correct partition keys, delivery semantics, consumer groups, and basic lag triage.

## Reading Order

1. [Messaging Models](/kafka-handbook/01-fundamentals/messaging-models/) — log vs queue mental model
2. [Queue vs Stream](/kafka-handbook/01-fundamentals/queue-vs-stream/) — when Kafka fits
3. [Kafka Core](/kafka-handbook/02-kafka/kafka-core/) — producers, consumers, topics, partitions
4. [Kafka Internals](/kafka-handbook/02-kafka/kafka-internals/) — ISR, replication, segments
5. [Consumer Groups](/kafka-handbook/02-kafka/kafka-consumer-groups/) — rebalance, parallelism
6. [Delivery Semantics](/kafka-handbook/02-kafka/kafka-delivery-semantics/) — at-least-once, idempotency, EOS boundaries
7. [Kafka Performance](/kafka-handbook/02-kafka/kafka-performance/) — partition sizing, batching, hot partitions
8. [Kafka Operations](/kafka-handbook/02-kafka/kafka-operations/) — lag metrics, retention, capacity

## Practice

- Work through [Top 150](/kafka-handbook/04-interview-guide/top-150-interview-questions/) rows tagged **Senior Engineer**
- Drill [Performance Questions](/kafka-handbook/04-interview-guide/performance-questions/) after step 7

## Skip for Now

- Broker comparison matrices (architect path)
- Security hardening depth (lead path adds ACLs/mTLS)

## See Also

- [Interview Revision Path](/kafka-handbook/05-learning-paths/kafka-interview-revision-path/)
- [Lead Path](/kafka-handbook/05-learning-paths/kafka-lead-path/)
