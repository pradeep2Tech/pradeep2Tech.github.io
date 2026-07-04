---
title: "Architect Questions"
date: 2026-07-03T15:00:00+00:00
draft: false
description: "Architect Questions subset from Top 300."
tags: ["microservices", "architecture-playbook", "distributed-systems"]
categories: ["Microservices Architecture Playbook"]
shortTitle: "Architect"
module: 11
moduleTitle: "Interview Guide"
sectionRef: "11.x"
weight: 1102
playbookVersion: 3
interviewHandbook: true
---

# Architect Questions

Questions only — no answers.

Sourced from [Top 300](/microservices/11-interview-guide/top-300-microservices-questions/).

1. When does a modular monolith outperform a microservices fleet for a 12-person product team?
2. How does Conway's Law influence your decomposition boundaries?
3. What signals indicate you are building a distributed monolith?
4. Compare SOA ESB-centric integration with modern event-driven microservices.
5. When would you reject a microservices migration proposal from leadership?
6. How do you define service boundaries using bounded contexts?
7. What operational tax does microservices impose vs modular monolith?
8. How do API gateway and BFF responsibilities differ at the edge?
9. When should a BFF aggregate five calls vs delegate to a domain service?
10. How do you prevent the API gateway from becoming a distributed monolith?
11. Design service discovery for multi-cluster Kubernetes without hardcoded IPs.
12. When is client-side discovery preferable to server-side load balancing?
13. How do you choose sync gRPC vs async events for a new integration?
14. What is database-per-service and why forbid cross-schema JOINs?
15. When is CQRS worth the operational cost over simple CRUD?
16. Orchestration vs choreography saga — decision criteria?
17. Why is dual-write an anti-pattern and what replaces it?
18. How does outbox differ from CDC for event publication?
19. When would you use event sourcing vs event-carried state transfer?
20. How do you model cross-domain reporting without shared operational databases?
21. How do you align team topology with service ownership?
22. What is the strangler fig pattern and when is it preferred over rewrite?
23. How do you phase database decomposition without big-bang cutover?
24. What anti-corruption layer responsibilities exist at legacy boundaries?
25. When is a service mesh operational tax not justified?
26. What Kubernetes primitives are mandatory for stateless microservices?
27. How do PodDisruptionBudgets interact with rolling deployments?
28. What is expand-contract schema migration and why use it?
29. How do you structure ADRs for a contentious broker selection?
30. Differentiate monolith, modular monolith, microservices, and SOA for a fintech platform.
31. What bounded context would you extract first from an e-commerce monolith?
32. How do you measure whether decomposition improved deploy frequency?
33. When does shared library coupling negate microservices benefits?
34. How do you govern API versioning across autonomous teams?
35. What is smart endpoints and dumb pipes in practice today?
36. **E-commerce checkout:** 5 services, payment partner SLA 200ms — design sync/async split and fallback when payment is down.
37. **Banking ledger:** Strong consistency for balances — can you use choreography saga? Defend orchestration choice.
38. **Multi-tenant SaaS:** Noisy neighbor on shared Kafka cluster — isolation options at platform level.
39. **Global deployment:** EU data residency — how do service boundaries and databases align to regions?
40. **Legacy ERP integration:** SOAP monolith + new microservices — strangler vs dual-write risks.
41. **Black Friday scale:** 10× traffic on catalog only — which services scale independently?
42. **Observability gap:** P99 spikes but all services green — how do you find the tail dependency?
43. **Mesh adoption:** 40 teams, only 3 want Istio — when is mesh tax not justified?
44. **Shared library drift:** DTO JAR shared by 15 services — governance model.
45. **Event schema evolution:** Add field to `OrderCreated` — compatibility rules for 12 consumers.
46. **On-call incident:** Circuit breaker stuck OPEN on recommendations — business impact vs fail-fast tradeoff.
47. **Database decomposition:** Orders still JOIN customers cross-schema — extraction blocked — remediation plan.
48. **API versioning:** Mobile clients lag 6 months — breaking change policy.
49. **Saga stuck:** Compensation failed on inventory release — ops playbook.
50. **Cost review:** 80 microservices, 12 actually deploy independently — rationalization approach.
