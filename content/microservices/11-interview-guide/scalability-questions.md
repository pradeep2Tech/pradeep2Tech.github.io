---
title: "Scalability Interviews"
date: 2026-07-03T15:00:00+00:00
draft: false
description: "Production-scale prompts: traffic spikes, autoscaling, sharding, caching, hot keys, rate limiting, and bottlenecks."
tags: ["microservices", "architecture-playbook", "distributed-systems"]
categories: ["Microservices Architecture Playbook"]
shortTitle: "Scalability"
module: 11
moduleTitle: "Interview Guide"
sectionRef: "11.4"
weight: 1104
playbookVersion: 3
interviewHandbook: true
---

# Scalability Interviews

Production-scale prompts: traffic spikes, autoscaling, sharding, caching, hot keys, rate limiting, and bottlenecks.

Complements the [Top 300 master index](/microservices/11-interview-guide/top-300-microservices-questions/) with **scalability-only** prompts not repeated there.

Questions only — no answers. Strong responses discuss tradeoffs, failure modes, production behavior, operational impact, cost, scaling, reliability, observability, and migration.

1. **Senior Engineer · Medium** — Traffic to your product detail API spiked 8× in ten minutes — how would you scale each tier without masking a DB bottleneck?
2. **Senior Engineer · Medium** — Walk me through autoscaling rules when CPU is low but request queue depth is climbing.
3. **Senior Engineer · Medium** — How would you fix uneven shard load when tenant_id hashing concentrates Fortune 500 accounts on two nodes?
4. **Senior Engineer · Hard** — Design a caching strategy for a homepage that mixes personalized and public content during a live event.
5. **Senior Engineer · Hard** — How would you scale Kafka producers when broker ingress saturates before consumer lag appears?
6. **Staff Engineer · Hard** — Walk me through capacity planning when peak is 20× baseline but finance will not fund year-round over-provisioning.
7. **Staff Engineer · Hard** — How would you scale a PostgreSQL read path when ORM N+1 queries hide behind acceptable average latency?
8. **Staff Engineer · Hard** — Design partition keys for an orders stream that must preserve per-customer ordering at 50K orders/sec.
9. **Principal Architect · Hard** — How would you architect global traffic steering when one region loses 60% of egress capacity during a cable cut?
10. **Senior Engineer · Medium** — Walk me through scaling Redis Cluster when a single hot key dominates 35% of QPS.
11. **Senior Engineer · Hard** — How would you tune connection pool sizes when pod count doubles but database max_connections is fixed?
12. **Staff Engineer · Hard** — Design CDN cache invalidation for flash sales without collapsing origin under purge storms.
13. **Staff Engineer · Hard** — How would you scale outbound webhooks when partners respond at wildly different latencies?
14. **Principal Architect · Hard** — Walk me through sharding a payments ledger when regulatory audit requires cross-shard reporting.
15. **Senior Engineer · Medium** — How would you prevent HPA from scaling into a database that is already IO-saturated?
16. **Senior Engineer · Hard** — Design rate limiting for internal batch jobs that share the same APIs as customer traffic.
17. **Staff Engineer · Hard** — How would you scale Elasticsearch for typeahead search when indexing falls behind catalog updates?
18. **Staff Engineer · Hard** — Walk me through load test design that reveals bottlenecks production metrics currently hide.
19. **Principal Architect · Hard** — How would you choose between vertical scale, read replicas, and sharding for a 4TB orders table?
20. **Senior Engineer · Medium** — How would you scale websocket connections when sticky sessions pin users to overloaded nodes?
21. **Senior Engineer · Hard** — Design autoscaling for GPU inference pods tied to bursty image-upload traffic.
22. **Staff Engineer · Hard** — How would you fix thundering herd when a popular cache key expires during prime time?
23. **Staff Engineer · Hard** — Walk me through scaling a GraphQL gateway whose p99 grows linearly with downstream fan-out.
24. **Principal Architect · Hard** — How would you architect multi-tenant noisy-neighbor isolation on shared Kafka and shared Redis?
25. **Senior Engineer · Medium** — How would you scale batch ETL without starving online transaction processing on the same cluster?
26. **Senior Engineer · Hard** — Design request coalescing for a product availability API hit by checkout, search, and ads simultaneously.
27. **Staff Engineer · Hard** — How would you scale cross-region replication when inter-AZ bandwidth becomes the hidden limit?
28. **Staff Engineer · Hard** — Walk me through diagnosing autoscaling lag when traffic ramps faster than cloud APIs provision nodes.
29. **Principal Architect · Hard** — How would you plan capacity for a launch when marketing will not share expected traffic shape?
30. **Senior Engineer · Hard** — How would you scale a sidecar-heavy mesh deployment when proxy CPU exceeds app CPU?
31. **Senior Engineer · Hard** — Design partition strategy for time-series metrics storage approaching retention limits.
32. **Staff Engineer · Hard** — How would you scale idempotency key storage when TTL and cardinality both grow with traffic?
33. **Staff Engineer · Hard** — Walk me through fixing slow scatter-gather queries after a bad shard key migration.
34. **Principal Architect · Hard** — How would you trade cost vs headroom when reserved capacity contracts lock you in for three years?
35. **Senior Engineer · Medium** — How would you scale file upload ingestion when object storage throughput is fine but metadata DB is not?
36. **Senior Engineer · Hard** — Design edge caching for API responses that include per-user entitlements.
37. **Staff Engineer · Hard** — How would you scale consumer groups when partition count is politically capped by another team?
38. **Staff Engineer · Hard** — Walk me through scaling a rate limiter itself when Redis becomes the choke point.
39. **Principal Architect · Hard** — How would you design elastic scale-to-zero for dev/stage without teaching teams bad production habits?
40. **Senior Engineer · Hard** — How would you handle a viral social post that creates a hot partition and a hot cache key simultaneously?
