---
title: "Reliability & Resilience Interviews"
date: 2026-07-03T15:00:00+00:00
draft: false
description: "Resilience under failure: retries, circuit breakers, bulkheads, sagas, SLOs, chaos, and disaster recovery."
tags: ["microservices", "architecture-playbook", "distributed-systems"]
categories: ["Microservices Architecture Playbook"]
shortTitle: "Reliability"
module: 11
moduleTitle: "Interview Guide"
sectionRef: "11.5"
weight: 1105
playbookVersion: 3
interviewHandbook: true
---

# Reliability & Resilience Interviews

Resilience under failure: retries, circuit breakers, bulkheads, sagas, SLOs, chaos, and disaster recovery.

Complements the [Top 300 master index](/microservices/11-interview-guide/top-300-microservices-questions/) with **reliability-only** prompts not repeated there.

Questions only — no answers. Strong responses discuss tradeoffs, failure modes, production behavior, operational impact, cost, scaling, reliability, observability, and migration.

1. **Senior Engineer · Medium** — How would you design retries for a payment authorize call that sometimes succeeds on the provider but times out to you?
2. **Senior Engineer · Medium** — Walk me through circuit breaker thresholds when downstream p99 varies 10× by time of day.
3. **Senior Engineer · Medium** — How would you implement idempotency for refund APIs that partners expose as at-most-once?
4. **Senior Engineer · Hard** — Design graceful degradation when loyalty points cannot be calculated but the order must still complete.
5. **Senior Engineer · Hard** — How would you test saga compensation paths without contaminating production finance data?
6. **Staff Engineer · Hard** — Walk me through SLO design for an async fulfillment workflow with no user-facing HTTP endpoint.
7. **Staff Engineer · Hard** — How would you coordinate timeout budgets when each team owns only their hop in a seven-service chain?
8. **Staff Engineer · Hard** — Design bulkheads when a shared thread pool serves both checkout and low-priority batch exports.
9. **Principal Architect · Hard** — How would you define error budget policy when multiple services contribute to one customer journey SLO?
10. **Senior Engineer · Medium** — Walk me through fallback strategies for currency conversion when the rates API is stale or down.
11. **Senior Engineer · Hard** — How would you make at-least-once Kafka consumers safe for balance adjustments without exactly-once fantasy?
12. **Staff Engineer · Hard** — Design chaos experiments that validate failover without breaching vendor rate limits.
13. **Staff Engineer · Hard** — How would you handle a circuit breaker stuck open because health checks probe the wrong dependency?
14. **Principal Architect · Hard** — Walk me through disaster recovery when RPO is minutes but cross-region replication lag is hours.
15. **Senior Engineer · Medium** — How would you implement adaptive retries that back off when the downstream is clearly overloaded?
16. **Senior Engineer · Hard** — Design compensation for a saga step that cannot be undone automatically and needs human approval.
17. **Staff Engineer · Hard** — How would you validate that client timeouts always exceed server-side breaker plus retry budgets?
18. **Staff Engineer · Hard** — Walk me through graceful shutdown when Kubernetes gives you 30 seconds but sagas need two minutes.
19. **Principal Architect · Hard** — How would you prioritize reliability investments across 40 services with one shared platform team?
20. **Senior Engineer · Medium** — How would you design health endpoints that reflect downstream readiness, not just process liveness?
21. **Senior Engineer · Hard** — Design idempotent webhook processing when partners retry for 72 hours with the same payload.
22. **Staff Engineer · Hard** — How would you run a game day for database failover when apps cache DNS for five minutes?
23. **Staff Engineer · Hard** — Walk me through error budget burn during a deploy-induced incident vs a dependency outage.
24. **Principal Architect · Hard** — How would you architect resilience when a critical vendor has no SLA and no staging environment?
25. **Senior Engineer · Hard** — How would you prevent retry storms when a gateway and three services each implement their own retry policy?
26. **Senior Engineer · Hard** — Design dead-letter handling that preserves ordering for payment settlement events.
27. **Staff Engineer · Hard** — How would you tune half-open probe rates so recovery is detected without re-overloading the service?
28. **Staff Engineer · Hard** — Walk me through contract testing that catches breaking changes before they trip breakers in production.
29. **Principal Architect · Hard** — How would you align product expectations with partial failure UX during regional outages?
30. **Senior Engineer · Medium** — How would you design outbox relay monitoring so silent stalls page before business impact?
31. **Senior Engineer · Hard** — Design hedged reads for search suggestions without doubling load during normal conditions.
32. **Staff Engineer · Hard** — How would you validate saga orchestrator durability across DB failover and pod rescheduling?
33. **Staff Engineer · Hard** — Walk me through incident response when error budgets are exhausted mid-quarter.
34. **Principal Architect · Hard** — How would you choose between active-active and active-passive DR for tier-1 checkout?
35. **Senior Engineer · Hard** — How would you design queue-based load leveling when spikes are predictable but amplitude is not?
36. **Senior Engineer · Hard** — Design fallback content policies that never misrepresent payment or inventory state.
37. **Staff Engineer · Hard** — How would you measure whether resilience patterns actually reduced customer-visible incidents?
38. **Staff Engineer · Hard** — Walk me through tuning bulkhead pool sizes using production saturation metrics.
39. **Principal Architect · Hard** — How would you govern org-wide retry defaults so local optimizations do not create global failure?
40. **Senior Engineer · Hard** — How would you design safe manual overrides during incidents without bypassing audit requirements?
