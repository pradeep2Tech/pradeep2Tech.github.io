---
title: "Architect-Level Questions"
date: 2026-07-03T10:00:00+00:00
draft: false
description: "Curated architect-level questions from the Kafka handbook question bank."
tags: ["kafka-handbook", "kafka", "messaging", "streaming", "interview"]
categories: ["Kafka Handbook"]
shortTitle: "Architect-Level"
module: 4
moduleTitle: "Interview Guide"
sectionRef: "4.2"
weight: 402
ShowToc: true
interviewHandbook: true
---

Questions only — no answers. Sourced from [Top 150](/kafka-handbook/04-interview-guide/top-150-interview-questions/).

# Top 25 Architect-Level Questions

1. Why is global ordering across an entire topic expensive in a distributed log architecture?
2. What ordering guarantees can you realistically promise to product teams when partition count exceeds one?
3. When is a managed cloud queue preferable to self-hosted Kafka despite reduced operational control?
4. What ADR criteria from the handbook would you use to justify Kafka as the enterprise event backbone?
5. How do throughput, ordering, and operational trade-offs differ across brokers listed in the messaging module?
6. What hybrid architecture uses Kafka for event streaming and RabbitMQ for task distribution in the same platform?
7. When would Apache Pulsar's unified queue-and-log model beat Kafka for multi-tenant streaming?
8. How does built-in geo-replication in Pulsar influence multi-datacenter architecture decisions versus MirrorMaker?
9. What tenancy isolation requirements would push you toward Pulsar over a single shared Kafka cluster?
10. How would you design SNS fan-out to multiple SQS queues versus a single Kafka topic with consumer groups?
11. How would you map the handbook's log versus queue versus cloud pub/sub taxonomy to a retail order platform?
12. How do consumer groups divide partition ownership, and what triggers a rebalance storm?
13. How does replication factor interact with rack awareness and cross-AZ fault tolerance?
14. When are Kafka transactions required versus idempotent producers plus idempotent consumers?
15. How does exactly-once stream processing differ from end-to-end exactly-once across Kafka and a database?
16. How would you design Kafka for multi-region active-active deployment with conflict resolution?
17. What role does MirrorMaker 2 play in disaster recovery versus real-time dual writes?
18. What Kubernetes operator patterns apply to running Kafka on Kubernetes at production scale?
19. How do you run a controlled failure drill on a Kafka cluster without customer impact?
20. What SASL mechanisms are appropriate for multi-tenant clusters, and what are their tradeoffs?
21. How do you prevent unauthorized consumers from reading sensitive PII topics?
22. How does the transactional outbox pattern pair with Kafka to avoid dual-write inconsistencies?
23. When is CDC preferable to application-published domain events for Kafka ingestion?
24. What saga orchestration patterns map cleanly to Kafka topics versus choreographed events?
25. How would you blueprint an event-driven architecture ADR using the handbook's selection criteria?
