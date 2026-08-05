---
title: "Discovery Completeness Checklist"
date: 2026-08-05T00:00:00+05:30
draft: true
description: "Test coverage, evidence, contradictions, ownership, traceability, requirements, risks, options, decisions, transition, and closure criteria."
tags: ["architecture-discovery", "checklist", "completeness"]
categories: ["Architecture Discovery"]
shortTitle: "Completeness Checklist"
module: 4
moduleTitle: "Applied Resources"
contentType: "checklist"
difficulty: "advanced"
estimatedReadingTime: 10
interviewImportance: "high"
enterpriseImportance: "critical"
prerequisites: ["Evidence, Assumptions, and Confidence", "Decision Traceability", "Discovery Closure and Architecture Handoff"]
dependencies: ["discovery-framework/evidence-assumptions-and-confidence", "discovery-framework/findings-requirements-decision-traceability", "risk/discovery-closure-and-architecture-handoff"]
---

Completeness is relative to the next authorized decision. Use this checklist at playback, option review, and closure. Mark **sufficient**, **conditional**, **insufficient**, or **not applicable**, citing evidence and consequence.

## Charter and Coverage

- [ ] Every chartered architectural question has an answer, governed open item, or rescope decision.
- [ ] Scope and exclusions remain current and accepted.
- [ ] Priority actors, journeys, capabilities, domains, processes, and outcomes are covered.
- [ ] Current, target, and transition time horizons are distinguishable.
- [ ] Applicable geography, product, tenant, data, environment, and lifecycle variants are represented.

## Evidence Quality

- [ ] Material findings cite evidence, owner, date, scope, and confidence.
- [ ] Observation and runtime data complement stakeholder recollection.
- [ ] Contradictions are visible and assigned for adjudication.
- [ ] Unknown is not treated as compliant or healthy.
- [ ] High-consequence assumptions have validation, owner, and deadline.

## Domain Coverage

- [ ] Business drivers, outcomes, capabilities, value streams, and operating constraints are linked.
- [ ] Domain language, rules, boundaries, authority, and events are explicit.
- [ ] Functional scenarios cover normal, alternate, failure, recovery, and acceptance.
- [ ] Processes include actual handoffs, queues, controls, exceptions, and measures.
- [ ] Quality scenarios are measurable, prioritized, owned, and validated.
- [ ] Integration contracts and direct/transitive dependencies include failure semantics.
- [ ] Data meaning, authority, flow, quality, lifecycle, and recovery are covered.
- [ ] Assets, actors, trust, obligations, control evidence, and security gaps are covered.
- [ ] Technology estate, constraints, debt, workload, and lifecycle are evidenced.
- [ ] Service ownership, incidents, delivery, capacity, continuity, cost, and recovery are addressed.

## Traceability and Decisions

- [ ] Findings trace to requirements, risks, options, decisions, and measures where material.
- [ ] Requirements distinguish behavior, quality, constraint, and solution decision.
- [ ] Risks, assumptions, issues, dependencies, constraints, and decisions are not conflated.
- [ ] Viable options are materially different and consistently evaluated.
- [ ] Mandatory gates, rejected options, dissent, uncertainty, and sensitivity are preserved.
- [ ] Recommendation has authority, conditions, residual risk, and triggers.

## Modernization and Transition

- [ ] Dispositions are evidence-backed below overly broad application labels where necessary.
- [ ] Interim states define routing, data authority, compatibility, controls, operations, and recovery.
- [ ] In-flight work and ambiguous outcomes have treatment.
- [ ] Waves reflect dependencies, capacity, learning, adoption, and retirement.
- [ ] Readiness and fitness measures have owners and response.

## Ownership and Handoff

- [ ] Outcome, requirement, data, service, control, risk, action, and benefit owners are named.
- [ ] Open items state materiality, due date, gate, and consequence.
- [ ] Deliverables have purpose, audience, owner, status, and lifecycle.
- [ ] Delivery and operational recipients have accepted responsibilities.
- [ ] Reassessment triggers connect decisions to production evidence.

## Closure Decision

- [ ] The accountable authority chose close, conditional close, targeted extension, rescope, pause, or stop.
- [ ] Conditions and waivers have scope, owners, evidence, expiry, and monitoring.
- [ ] The artifact index identifies authoritative versions and source evidence.
- [ ] Superseded drafts are clearly marked or archived.
- [ ] Next decision gates and review dates/triggers are scheduled.

Discovery is sufficient when remaining uncertainty is explicitly governed and does not invalidate the next decision. Page count and workshop attendance are not evidence of completeness.

Next use the [Architecture Review Checklist](/architecture-discovery/checklists/architecture-review-checklist/) at a decision gate.
