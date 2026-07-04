---
title: "Production Troubleshooting Questions"
date: 2026-07-03T10:00:00+00:00
draft: false
description: "Curated production troubleshooting questions from the Kafka handbook question bank."
tags: ["kafka-handbook", "kafka", "messaging", "streaming", "interview"]
categories: ["Kafka Handbook"]
shortTitle: "Production"
module: 4
moduleTitle: "Interview Guide"
sectionRef: "4.3"
weight: 403
interviewHandbook: true
---

Questions only — no answers. Sourced from [Top 150](/kafka-handbook/04-interview-guide/top-150-interview-questions/).

# Top 25 Production Troubleshooting Questions

1. How would you design a dead-letter topic and replay runbook for poison messages that block partition progress?
2. How does temporal decoupling in event-driven architectures complicate end-to-end debugging compared to sync RPC?
3. How would you troubleshoot a single partition falling behind while others remain healthy?
4. What failure modes appear during broker patching when partition leadership moves across the cluster?
5. What compatibility risks remain when migrating clients from Apache Kafka to Redpanda in production?
6. What happens during an unclean leader election, and when would you allow it in production?
7. How would you troubleshoot under-replicated partitions after a broker network partition?
8. What tombstone records and compaction lag issues break compacted topic consumers?
9. What causes rebalance loops when session.timeout.ms and max.poll.interval.ms are misconfigured?
10. How do you troubleshoot a producer receiving NOT_LEADER_FOR_PARTITION errors during cluster maintenance?
11. What steps isolate whether lag is producer-side, broker-side, or consumer-side?
12. How would you handle a topic accidentally created with replication factor one in production?
13. What is your incident runbook when all consumers in a critical group stop committing offsets?
14. How would you diagnose metadata request storms after a large-scale topic creation event?
15. How do Kafka Connect offset topics and connector failures affect CDC pipeline continuity?
16. How do Kafka Streams state stores recover after application redeploy or rebalance?
17. How does increasing retention without storage planning cause emergency disk expansion?
18. What happens when a compacted topic's disk usage grows because compaction cannot keep pace?
19. How would you recover from accidental topic deletion in a production cluster?
20. What quorum loss symptoms appear in KRaft or ZooKeeper during a zone outage?
21. How would you reset offsets safely to replay a topic after a downstream bug without corrupting idempotent state?
22. What symptoms indicate broker disk saturation, and how do log segments contribute?
23. What GC pauses on brokers correlate with request timeout spikes on producers?
24. What is the first check when consumer lag alerts fire during normal business hours?
25. How would you throttle misbehaving clients flooding a shared cluster?
