---
title: "Production Troubleshooting"
date: 2026-07-03T15:00:00+00:00
draft: false
description: "Incident-first troubleshooting: latency spikes, broker lag, pool exhaustion, mesh failures, and rollback decisions."
tags: ["microservices", "architecture-playbook", "distributed-systems"]
categories: ["Microservices Architecture Playbook"]
shortTitle: "Troubleshooting"
module: 11
moduleTitle: "Interview Guide"
sectionRef: "11.7"
weight: 1107
playbookVersion: 3
interviewHandbook: true
---

# Production Troubleshooting

Incident-first troubleshooting: latency spikes, broker lag, pool exhaustion, mesh failures, and rollback decisions.

Complements the [Top 300 master index](/microservices/11-interview-guide/top-300-microservices-questions/) with **incident scenarios** not repeated there.

Questions only — no answers. Strong responses discuss tradeoffs, failure modes, production behavior, operational impact, cost, scaling, reliability, observability, and migration.

1. **Senior Engineer · Medium** — At 09:14 UTC checkout p99 jumped from 180ms to 3.2s while error rate stayed flat — walk me through triage.
2. **Senior Engineer · Medium** — Kafka consumer lag on `order-events` grew from 2K to 200K in 40 minutes — what do you check first and why?
3. **Senior Engineer · Medium** — Redis Cluster entered FAIL state after a node replacement — how would you restore service without cold-cache collapse?
4. **Senior Engineer · Hard** — PostgreSQL failover completed but apps still write to the old primary — how do you detect and fix split-brain?
5. **Senior Engineer · Hard** — After a deploy, `payment-service` pods OOMKilled every 8 minutes — walk me through memory investigation.
6. **Staff Engineer · Hard** — CrashLoopBackOff across three AZs after a ConfigMap change — how would you isolate bad config vs bad image?
7. **Staff Engineer · Hard** — HikariCP pool exhausted on order-service while CPU is 30% — how would you prove leak vs traffic vs slow queries?
8. **Staff Engineer · Hard** — API gateway TLS handshake failures spike — certificate expires in 30 days; what else do you investigate?
9. **Principal Architect · Hard** — Internal DNS intermittently returns NXDOMAIN for `inventory.svc` — walk me through cross-team root cause analysis.
10. **Senior Engineer · Hard** — Tomcat thread pool maxed out but downstream latency looks normal — how would you find the hidden blocker?
11. **Senior Engineer · Hard** — G1 GC pause times exceed 1.5s on checkout pods during the same window as latency SLO breach — next steps?
12. **Staff Engineer · Hard** — Istio routes 25% of traffic to pods marked Terminating — how would you debug endpoint propagation?
13. **Staff Engineer · Hard** — Canary at 5% traffic shows 4× 500 rate — what signals determine rollback vs continue?
14. **Principal Architect · Hard** — Event replay re-sent 12K duplicate charge emails — how do you stop damage and design safer replay?
15. **Senior Engineer · Medium** — Memory usage on notification-consumer climbs 2% per hour — how would you profile in production safely?
16. **Senior Engineer · Hard** — All API requests return 401 after JWKS endpoint latency exceeds 10s — immediate mitigation and durable fix?
17. **Staff Engineer · Hard** — Debezium lag is 38 minutes at strangler cutover gate — go/no-go criteria and stakeholder communication?
18. **Staff Engineer · Hard** — Read model projection is 9 hours behind — users see paid orders as pending; triage and customer comms?
19. **Principal Architect · Hard** — Istiod is unavailable — which data plane behavior continues and what must you disable manually?
20. **Senior Engineer · Hard** — Partial outage ended but retry storms keep dependency error rate at 40% — containment playbook?
21. **Senior Engineer · Hard** — One Kafka partition on `payments` carries 70% of traffic — symptoms, hotfix, and long-term fix?
22. **Staff Engineer · Hard** — Pods pass liveness but fail readiness after DB migration — how would you debug startup dependency chains?
23. **Staff Engineer · Hard** — Certificate pinning in mobile apps breaks after gateway cert rotation — ops vs client fix decision?
24. **Principal Architect · Hard** — Cross-region network blip caused cascading saga timeouts — how would you reconstruct the failure timeline?
25. **Senior Engineer · Medium** — Elasticsearch cluster yellow for 2 hours — indexing backlog growing; walk me through stabilization.
26. **Senior Engineer · Hard** — DNS TTL caching causes stale endpoints after emergency scale-up — how would you flush pain safely?
27. **Staff Engineer · Hard** — Feature flag service outage defaults all flags to off — how would you design safer failure modes retroactively?
28. **Staff Engineer · Hard** — Outbox relay process died silently 3 hours ago — how would detection and backfill work?
29. **Principal Architect · Hard** — Vendor webhook delivery delayed 6 hours then arrived out of order — how would you reconcile payment state?
30. **Senior Engineer · Hard** — Node disk pressure evicts pods randomly during log rotation misconfiguration — triage steps?
31. **Senior Engineer · Hard** — gRPC UNAVAILABLE spikes only from one client version — how would you narrow release correlation?
32. **Staff Engineer · Hard** — Connection storm after DB restart — how would you stagger pool reconnection across 400 pods?
33. **Staff Engineer · Hard** — Mesh mTLS handshake failures after SPIFFE bundle rotation — walk me through cert trust debugging.
34. **Principal Architect · Hard** — Blue-green switch left 0.1% traffic on old stack writing to deprecated schema — detection and repair?
35. **Senior Engineer · Medium** — Prometheus scrape timeouts cause 'no data' alerts while the service is healthy — what is actually broken?
36. **Senior Engineer · Hard** — Thread deadlock in pricing-service under promotion load — what observability proves the diagnosis?
37. **Staff Engineer · Hard** — S3 upload latency spike causes checkout timeouts — how would you separate network from SDK retry behavior?
38. **Staff Engineer · Hard** — Kubernetes API server latency causes HPA and deployments to stall — incident command priorities?
39. **Principal Architect · Hard** — Multi-team incident with conflicting root-cause theories — how would you facilitate evidence-based resolution?
40. **Senior Engineer · Hard** — Poison pill message on partition 7 blocks settlement for 6 hours — mitigation without losing ordering forever?
41. **Senior Engineer · Hard** — DNS-based multi-cluster failover sends traffic to a cluster that cannot reach the shared database — next steps?
42. **Staff Engineer · Hard** — JVM metaspace OOM after hot-deploying plugins — how would you reproduce and fix under fire?
43. **Staff Engineer · Hard** — Rate limiter misconfiguration blocks internal health probes and amplifies outage — how did you miss it?
44. **Principal Architect · Hard** — Customer reports payment succeeded but order missing — walk me through cross-service reconciliation under pressure.
45. **Senior Engineer · Hard** —  etcd quorum loss during control plane upgrade — which workloads keep running and what do you stop?
46. **Senior Engineer · Hard** — Async worker queue depth doubled after clock skew on scheduled jobs — how would you verify and correct?
47. **Staff Engineer · Hard** — Load balancer health checks pass while application returns 500 for real traffic — design better probes?
48. **Staff Engineer · Hard** — Terraform-applied security group change blocked east-west traffic — how would you rollback cloud networking fast?
49. **Principal Architect · Hard** — Incident commander asks for ETA in minute 10 of a novel failure — how would you communicate uncertainty honestly?
50. **Senior Engineer · Hard** — Database connection wait time p99 at 8s but query time p99 at 40ms — pool sizing or leak?
