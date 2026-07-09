---
title: "System Design Case Studies"
date: 2026-07-03T15:00:00+00:00
draft: false
description: "Full system-design loops: requirements, architecture, data model, APIs, scaling, reliability, observability, and operations."
tags: ["microservices", "architecture-playbook", "distributed-systems"]
categories: ["Microservices Architecture Playbook"]
shortTitle: "Case Studies"
module: 11
moduleTitle: "Interview Guide"
sectionRef: "11.8"
weight: 1108
playbookVersion: 3
interviewHandbook: true
---

# System Design Case Studies

Full system-design loops: requirements, architecture, data model, APIs, scaling, reliability, observability, and operations.

Questions only — no answers. Strong responses discuss tradeoffs, failure modes, production behavior, operational impact, cost, scaling, reliability, observability, and migration.

1. **Staff Engineer · Hard** — Design an e-commerce checkout platform for flash sales where inventory, payment, coupon, and tax services fail independently.
2. **Staff Engineer · Hard** — Design a marketplace order lifecycle with seller acceptance, payment capture, shipment tracking, cancellation, and dispute resolution.
3. **Principal Architect · Hard** — Design a multi-region banking notification system with strict audit, replay, and customer preference requirements.
4. **Staff Engineer · Hard** — Design a food-delivery dispatch workflow where restaurants, drivers, payments, and refunds are asynchronous and failure-prone.
5. **Principal Architect · Hard** — Design a SaaS tenant provisioning platform supporting shared, isolated, and regulated deployment modes.
6. **Staff Engineer · Hard** — Design a global product catalog with regional pricing, inventory freshness, search indexing, and campaign traffic spikes.
7. **Staff Engineer · Hard** — Design a developer API platform with onboarding, OAuth, rate limits, idempotency, quotas, analytics, and partner support.
8. **Staff Engineer · Hard** — Design a notification platform that chooses vendors dynamically, honors opt-outs, deduplicates sends, and supports incident replay.
9. **Staff Engineer · Hard** — Design an inventory reservation system for stores, warehouses, and online carts with oversell prevention and compensation.
10. **Staff Engineer · Hard** — Design a streaming analytics pipeline handling late events, schema evolution, replay, and customer-facing dashboards.
11. **Principal Architect · Hard** — Design a payment payout platform with risk review, idempotency, settlement, reconciliation, and delayed callbacks.
12. **Staff Engineer · Hard** — Design a feature-flag control plane safe during partial outages and resistant to global bad-config incidents.
13. **Principal Architect · Hard** — Design zero-downtime migration from a shared customer database to domain-owned stores across billing, support, and identity.
14. **Staff Engineer · Hard** — Design a resilient search experience where indexing is asynchronous and source systems may be unavailable.
15. **Principal Architect · Hard** — Design a production incident management system linking alerts, ownership, runbooks, timelines, and post-incident actions.
16. **Staff Engineer · Hard** — Design a service-dependency map that helps teams understand blast radius before deployment and during incidents.
17. **Principal Architect · Hard** — Design regional data residency for a global SaaS with shared analytics and customer support operations.
18. **Principal Architect · Hard** — Design a microservices workflow orchestration platform supporting retries, human approval, compensation, and audit.
19. **Staff Engineer · Hard** — Design an observability onboarding standard for new services: logs, metrics, traces, dashboards, SLOs, and runbooks.
20. **Principal Architect · Hard** — Design a cost-aware multi-tenant platform where noisy-neighbor isolation and efficient shared infrastructure both matter.
