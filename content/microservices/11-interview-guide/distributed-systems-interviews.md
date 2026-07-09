---
title: "Distributed Systems Interviews"
date: 2026-07-03T15:00:00+00:00
draft: false
description: "Distributed systems interview prompts for senior microservices roles."
tags: ["microservices", "architecture-playbook", "distributed-systems"]
categories: ["Microservices Architecture Playbook"]
shortTitle: "Distributed Systems"
module: 11
moduleTitle: "Interview Guide"
sectionRef: "11.3"
weight: 1103
playbookVersion: 3
interviewHandbook: true
---

# Distributed Systems Interviews

Correctness under partial failure: ordering, idempotency, consistency, partitions, leases, replication, replay, distributed workflows, and recovery.

Complements the [Top 300 master index](/microservices/11-interview-guide/top-300-microservices-questions/) with **distributed-systems** depth not repeated there.

Questions only — no answers. Strong responses discuss tradeoffs, failure modes, production behavior, operational impact, cost, scaling, reliability, observability, and migration.

1. **Senior Engineer · Medium** — How would you design order state transitions when payment callbacks arrive late, duplicated, or out of order?
2. **Senior Engineer · Medium** — How would you preserve per-customer ordering when one customer becomes a hot Kafka partition?
3. **Senior Engineer · Medium** — How would you reason about a Redis-based lock when the lock holder pauses under GC longer than the lease?
4. **Senior Engineer · Medium** — How would you design idempotency across an API gateway, order service, database, message broker, and payment provider?
5. **Senior Engineer · Medium** — How would you recover a workflow after a worker crashes immediately after calling an external provider?
6. **Senior Engineer · Medium** — How would you decide between strong consistency, eventual consistency, and compensating actions for inventory reservations?
7. **Senior Engineer · Medium** — How would you handle a multi-region write conflict for customer profile updates without losing user trust?
8. **Senior Engineer · Medium** — How would you design event replay so historical events do not resend customer notifications or duplicate provider calls?
9. **Senior Engineer · Medium** — How would you migrate a topic partitioning strategy without breaking ordering guarantees for existing consumers?
10. **Senior Engineer · Medium** — How would you design a read model when freshness varies by region and users can immediately refresh after writes?
11. **Senior Engineer · Medium** — How would you reason about CAP and PACELC for a checkout workflow during a regional network partition?
12. **Senior Engineer · Medium** — How would you build fencing into a leader-elected scheduler so two leaders cannot execute the same job?
13. **Staff Engineer · Hard** — How would you detect and repair divergent derived balances across wallet, ledger, and reporting services?
14. **Staff Engineer · Hard** — How would you handle an event committed to the database but never published to the broker?
15. **Staff Engineer · Hard** — How would you design a saga when compensation itself can fail and must be retried days later?
16. **Staff Engineer · Hard** — How would you guarantee at-least-once processing without pretending the system is exactly-once end to end?
17. **Staff Engineer · Hard** — How would you design backpressure when one slow consumer threatens a shared broker and many upstream producers?
18. **Staff Engineer · Hard** — How would you propagate causality through HTTP calls, Kafka events, scheduled jobs, and provider callbacks?
19. **Staff Engineer · Hard** — How would you decide whether a workflow step should be a command, event, or state machine transition?
20. **Staff Engineer · Hard** — How would you handle a broker outage where producers can still accept user writes but consumers cannot progress?
21. **Staff Engineer · Hard** — How would you design conflict resolution when mobile clients replay offline writes after reconnecting?
22. **Staff Engineer · Hard** — How would you reason about clock skew when services use timestamps for expiry, ordering, and reconciliation?
23. **Staff Engineer · Hard** — How would you design a distributed rate limiter that remains useful during cross-region partitions?
24. **Staff Engineer · Hard** — How would you keep a feature-flag control plane safe when data-plane services cannot reach it?
25. **Staff Engineer · Hard** — How would you handle CDC lag during a cutover when lag is low on average but spikes under peak writes?
26. **Staff Engineer · Hard** — How would you design a projection rebuild that takes hours while live traffic keeps changing the source data?
27. **Staff Engineer · Hard** — How would you prevent a poison message from blocking all progress for a partition without losing ordering forever?
28. **Staff Engineer · Hard** — How would you design a globally available API when a small subset of operations requires regional data residency?
29. **Principal Architect · Hard** — How would you choose producer acknowledgements, replication factor, and min in-sync replicas for a tier-1 topic?
30. **Principal Architect · Hard** — How would you design an idempotent sink when a stream processor writes to a non-idempotent external API?
31. **Principal Architect · Hard** — How would you recover from split-brain leadership in a service that schedules payments?
32. **Principal Architect · Hard** — How would you make distributed transaction boundaries explicit to product teams asking for all-or-nothing behavior?
33. **Principal Architect · Hard** — How would you reason about snapshotting, compaction, and replay for long-running event-sourced aggregates?
34. **Principal Architect · Hard** — How would you test distributed failure modes locally and in staging without depending on luck in production?
35. **Principal Architect · Hard** — How would you walk an interviewer through where your design chooses correctness, availability, latency, and operator repairability?
