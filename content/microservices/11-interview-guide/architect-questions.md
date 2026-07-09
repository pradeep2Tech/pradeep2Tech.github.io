---
title: "Architecture & Design Interviews"
date: 2026-07-03T15:00:00+00:00
draft: false
description: "Architectural decision-making for decomposition, technology selection, tradeoffs, migration, governance, and platform engineering."
tags: ["microservices", "architecture-playbook", "distributed-systems"]
categories: ["Microservices Architecture Playbook"]
shortTitle: "Architecture & Design"
module: 11
moduleTitle: "Interview Guide"
sectionRef: "11.2"
weight: 1102
playbookVersion: 3
interviewHandbook: true
---

# Architecture & Design Interviews

Architectural decision-making for decomposition, technology selection, tradeoffs, migration, governance, and platform engineering.

Complements the [Top 300 master index](/microservices/11-interview-guide/top-300-microservices-questions/) with **architecture-only** prompts not repeated there.

Questions only — no answers. Strong responses discuss tradeoffs, failure modes, production behavior, operational impact, cost, scaling, reliability, observability, and migration.

1. **Senior Engineer · Medium** — How would you evaluate whether a new integration belongs inside an existing service vs a new microservice?
2. **Senior Engineer · Medium** — Walk me through defining API contracts before teams commit to separate deployment pipelines.
3. **Senior Engineer · Medium** — How would you decide sync REST vs async events for a fraud-check that must complete before payment capture?
4. **Senior Engineer · Medium** — Design a reference deployment topology for stateless services on Kubernetes across two availability zones.
5. **Senior Engineer · Hard** — How would you structure platform capabilities so product teams get self-service without bypassing governance?
6. **Staff Engineer · Hard** — Walk me through an architecture review when the proposal solves today's pain but creates a distributed monolith in 18 months.
7. **Staff Engineer · Hard** — How would you set technology selection criteria for message brokers across five business units with different SLAs?
8. **Staff Engineer · Hard** — Design service boundaries for a marketplace where sellers, buyers, payments, and logistics evolve at different speeds.
9. **Staff Engineer · Hard** — How would you reason about centralizing observability vs mandating standards and letting teams own tooling?
10. **Principal Architect · Hard** — Walk me through a multi-year architecture evolution plan when the monolith still ships 80% of revenue features.
11. **Principal Architect · Hard** — How would you design governance that accelerates delivery instead of becoming an approval bottleneck?
12. **Principal Architect · Hard** — Design a data ownership model when analytics, ML, and operations all need the same customer events.
13. **Senior Engineer · Medium** — How would you choose between database-per-service and shared read replicas for cross-domain reporting?
14. **Senior Engineer · Hard** — Walk me through decomposition criteria when two teams fight over ownership of the customer aggregate.
15. **Staff Engineer · Hard** — How would you architect an internal API marketplace with discovery, versioning, and deprecation policy?
16. **Staff Engineer · Hard** — Design multi-region active-active boundaries when checkout must stay strongly consistent for inventory holds.
17. **Principal Architect · Hard** — How would you decide build-vs-buy for workflow orchestration across payments, shipping, and refunds?
18. **Senior Engineer · Medium** — Walk me through when a modular monolith should gain an anti-corruption layer before any service extraction.
19. **Staff Engineer · Hard** — How would you align architecture principles with actual on-call pain from the last six incidents?
20. **Principal Architect · Hard** — Design a platform engineering operating model that does not become the bottleneck for every team.
21. **Senior Engineer · Hard** — How would you evaluate event-carried state transfer vs event notification for catalog price updates?
22. **Staff Engineer · Hard** — Walk me through ADR documentation when leadership mandates Kafka but your team prefers RabbitMQ.
23. **Principal Architect · Hard** — How would you structure architecture decision forums so dissent is recorded, not buried?
24. **Senior Engineer · Medium** — Design API versioning when mobile clients cannot force-upgrade for 12 months.
25. **Staff Engineer · Hard** — How would you prevent shared protobuf packages from recreating monolith coupling?
26. **Principal Architect · Hard** — Walk me through choosing edge aggregation vs domain-owned BFFs for a global product with regional compliance.
27. **Senior Engineer · Hard** — How would you model blast radius when extracting payments from a shared runtime cluster?
28. **Staff Engineer · Hard** — Design a service maturity rubric that teams respect because it reflects production reality.
29. **Principal Architect · Hard** — How would you sequence platform investments when reliability debt and feature pressure compete for the same quarter?
30. **Senior Engineer · Medium** — Walk me through when to introduce a service mesh vs strengthening library-based resilience first.
31. **Staff Engineer · Hard** — How would you architect tenant isolation for regulated healthcare workloads on shared Kubernetes?
32. **Principal Architect · Hard** — Design a migration runway when the strangler target architecture is clear but funding covers only one extraction per year.
33. **Senior Engineer · Hard** — How would you decide whether search indexing is a catalog concern or a platform capability?
34. **Staff Engineer · Hard** — Walk me through technology sunset planning when twelve services still depend on a deprecated broker client.
35. **Principal Architect · Hard** — How would you balance autonomous team velocity with enterprise-wide consistency for identity, billing, and audit?
36. **Senior Engineer · Medium** — Design bounded contexts for a subscription business with trials, upgrades, proration, and dunning.
37. **Staff Engineer · Hard** — How would you evaluate CQRS when the team has never operated separate read and write data stores?
38. **Principal Architect · Hard** — Walk me through architecture tradeoffs when acquiring a company whose stack conflicts with your platform standards.
39. **Senior Engineer · Hard** — How would you prevent the API gateway team from owning business orchestration that belongs in domain services?
40. **Staff Engineer · Hard** — Design a contract-first workflow that still allows rapid prototyping for early product discovery.
