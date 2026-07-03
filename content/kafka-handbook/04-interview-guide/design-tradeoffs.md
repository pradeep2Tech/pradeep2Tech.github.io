---
title: "Design & Architecture Questions"
date: 2026-07-03T10:00:00+00:00
draft: false
description: "Curated design & architecture questions from the Kafka handbook question bank."
tags: ["kafka-handbook", "kafka", "messaging", "streaming", "interview"]
categories: ["Kafka Handbook"]
shortTitle: "Design"
module: 4
moduleTitle: "Interview Guide"
sectionRef: "4.5"
weight: 405
ShowToc: true
interviewHandbook: true
---

Questions only — no answers. Sourced from [Top 150](/kafka-handbook/04-interview-guide/top-150-interview-questions/).

# Top 25 Design & Architecture Questions

1. Why is global ordering across an entire topic expensive in a distributed log architecture?
2. When would you isolate real-time and batch consumers using separate consumer groups on the same topic?
3. What ordering guarantees can you realistically promise to product teams when partition count exceeds one?
4. When does synchronous cross-service consistency make Kafka a poor primary integration choice without sagas?
5. How do you decide between log/stream platforms and classic queue brokers for a new microservice integration?
6. What ADR criteria from the handbook would you use to justify Kafka as the enterprise event backbone?
7. When would you pick Kafka over RabbitMQ for high-volume event fan-out with replay requirements?
8. What hybrid architecture uses Kafka for event streaming and RabbitMQ for task distribution in the same platform?
9. When would Apache Pulsar's unified queue-and-log model beat Kafka for multi-tenant streaming?
10. How does built-in geo-replication in Pulsar influence multi-datacenter architecture decisions versus MirrorMaker?
11. How would you design SNS fan-out to multiple SQS queues versus a single Kafka topic with consumer groups?
12. How would you map the handbook's log versus queue versus cloud pub/sub taxonomy to a retail order platform?
13. When would you choose log compaction over time-based retention for a topic?
14. How does exactly-once stream processing differ from end-to-end exactly-once across Kafka and a database?
15. How would you design Kafka for multi-region active-active deployment with conflict resolution?
16. What role does MirrorMaker 2 play in disaster recovery versus real-time dual writes?
17. How does the transactional outbox pattern pair with Kafka to avoid dual-write inconsistencies?
18. When is CDC preferable to application-published domain events for Kafka ingestion?
19. How would you design event versioning so multiple consumer versions coexist during rollout?
20. What saga orchestration patterns map cleanly to Kafka topics versus choreographed events?
21. How do you enforce ordering per customer entity across multiple event types?
22. What anti-patterns appear when microservices share one consumer group across different services?
23. How would you blueprint an event-driven architecture ADR using the handbook's selection criteria?
24. How does replication factor interact with rack awareness and cross-AZ fault tolerance?
25. When is Kafka Streams preferable to an external stream processor for aggregations?
