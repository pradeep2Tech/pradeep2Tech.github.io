---
title: "Performance & Scalability Questions"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "Top 25 performance and scalability questions from the Kafka handbook question bank."
tags: ["kafka-handbook", "kafka", "messaging", "streaming", "interview"]
categories: ["Kafka Handbook"]
shortTitle: "Performance"
module: 4
moduleTitle: "Interview Guide"
sectionRef: "4.4"
weight: 404
interviewHandbook: true
---

Questions only — no answers. Sourced from [Top 150](/kafka-handbook/04-interview-guide/top-150-interview-questions/).

# Top 25 Performance & Scalability Questions

1. Why does the handbook recommend sizing partitions for peak traffic rather than average load?
2. How does Kafka buffer producer bursts without dropping users when downstream processing is slower?
3. How would you auto-scale consumers in response to sustained consumer lag during traffic spikes?
4. How do you size topic partition count for peak throughput versus maximum consumer parallelism?
5. What happens to message ordering when you increase partition count on an existing high-traffic topic?
6. What symptoms indicate broker disk saturation, and how do log segments contribute?
7. How would you tune producer batch size and linger.ms for throughput without breaching latency SLOs?
8. What compression codec tradeoffs apply at high throughput — lz4, snappy, zstd, gzip?
9. How does fetch.min.bytes and max.wait.ms on consumers affect end-to-end latency?
10. What JVM and OS tuning would you apply on Kafka brokers serving millions of messages per day?
11. How do page cache and sequential disk writes explain Kafka's throughput on spinning disks versus NVMe?
12. What network and disk capacity math would you use for 30-day retention with replication factor three?
13. How do you plan broker count and partition leadership distribution to avoid hotspot brokers?
14. When does adding consumers stop reducing lag because partition count is the bottleneck?
15. What is the upper bound on useful partition count for a topic, and what metadata overhead grows?
16. What load-test scenarios validate partition and consumer sizing before Black Friday traffic?
17. How do you benchmark producer throughput separately from consumer processing capacity?
18. What GC pauses on brokers correlate with request timeout spikes on producers?
19. How would you throttle misbehaving clients flooding a shared cluster?
20. What quotas and ACL policies protect multi-team clusters from noisy neighbors?
21. How do you right-size `num.network.threads` and `num.io.threads` under heavy fetch load?
22. When does cross-datacenter replication latency dominate end-to-end event freshness SLOs?
23. How does choosing random UUID partition keys destroy ordering and create hot spots?
24. How do partition keys preserve ordering, and what hot-partition failure mode does poor key choice create?
25. What handbook guidance applies when peak traffic exceeds synchronous processing capacity?
