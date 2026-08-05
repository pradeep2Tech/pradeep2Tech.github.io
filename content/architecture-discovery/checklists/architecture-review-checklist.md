---
title: "Architecture Review Checklist"
date: 2026-08-05T00:00:00+05:30
draft: true
description: "Validate decision context, evidence, alternatives, quality attributes, data, security, operations, transition, economics, risks, authority, and follow-up."
tags: ["architecture-discovery", "checklist", "architecture-review"]
categories: ["Architecture Discovery"]
shortTitle: "Architecture Review Checklist"
module: 4
moduleTitle: "Applied Resources"
contentType: "checklist"
difficulty: "advanced"
estimatedReadingTime: 12
interviewImportance: "critical"
enterpriseImportance: "critical"
prerequisites: ["Architecture Reviews and Reassessment Triggers", "Architecture Risk and Synthesis"]
dependencies: ["risk/architecture-reviews-and-reassessment-triggers", "risk/from-discovery-findings-to-architecture-options", "risk/option-evaluation-and-recommendation", "risk/discovery-closure-and-architecture-handoff"]
---

Use this checklist for option, decision, readiness, transition, and post-implementation reviews. Tailor depth to consequence and reversibility. Record **pass**, **condition**, **evidence required**, **not applicable**, or **reject** with owner and authority.

## Decision Context

- [ ] The decision, scope, authority, deadline, and reversible/irreversible aspects are clear.
- [ ] Outcomes, baselines, measures, and benefits owners are explicit.
- [ ] Current state and reason for change are evidenced.
- [ ] Obligations, constraints, standards, assumptions, and exclusions are classified.
- [ ] The review type and permitted outcomes are known.

## Evidence and Traceability

- [ ] Findings cite credible, current, scoped evidence and confidence.
- [ ] Contradictions and missing evidence are visible.
- [ ] Requirements and quality scenarios trace to outcomes and acceptance.
- [ ] Material decisions and risks trace to evidence.
- [ ] Experiments state representative conditions, thresholds, results, and limitations.

## Options and Recommendation

- [ ] At least the plausible materially different alternatives were considered.
- [ ] Options are complete operating and transition architectures, not product names alone.
- [ ] Mandatory gates are separate from weighted preferences.
- [ ] Evaluation covers value, fit, quality, risk, cost, skills, operations, transition, and exit.
- [ ] Sensitivity, uncertainty, rejected options, and dissent are recorded.
- [ ] Recommendation states decisive rationale, conditions, consequences, and triggers.

## Architecture Coverage

- [ ] Capability, domain, responsibility, and service boundaries are coherent.
- [ ] Functional rules, states, exceptions, and acceptance are addressed.
- [ ] Quality scenarios and end-to-end budgets are feasible.
- [ ] Integration intent, contracts, dependencies, consistency, and recovery are explicit.
- [ ] Data meaning, authority, flow, lifecycle, quality, and migration are addressed.
- [ ] Assets, identities, trust boundaries, abuse cases, obligations, and controls are addressed.
- [ ] Deployment, environment, capacity, continuity, cost, and sustainability are addressed.

## Delivery and Operations

- [ ] Services have accountable owners, support, SLOs, telemetry, runbooks, and escalation.
- [ ] Change types have delivery, compatibility, verification, and recovery paths.
- [ ] Dependency and supplier responsibilities are explicit.
- [ ] Incident, degraded operation, restore, reconciliation, and backlog recovery are credible.
- [ ] Skills, staffing, platform, and business adoption readiness are evidenced.

## Transition and Modernization

- [ ] Dispositions and assessment units are evidence-backed.
- [ ] Intermediate states define routing, data authority, controls, operations, and duration.
- [ ] Rollback limits and forward recovery are understood.
- [ ] Migration waves respect dependencies, capacity, and learning.
- [ ] Legacy retirement has positive consumer, data, control, and operational evidence.

## Risk, Authority, and Follow-Up

- [ ] Risks use clear scenarios with owners, treatment, residual exposure, and triggers.
- [ ] Assumptions affecting the decision have validation or explicit acceptance.
- [ ] Risk acceptors have delegated authority for the consequence.
- [ ] Conditions and waivers have scope, evidence, owners, due dates, expiry, and monitoring.
- [ ] Review outcome, rationale, dissent, actions, and next gate are recorded.
- [ ] Fitness measures and context-change triggers cause reassessment.

## Review Outcome

Choose one explicit result:

- **Approve:** evidence supports proceeding within stated scope.
- **Approve with conditions:** bounded progress is permitted with governed actions.
- **Request evidence:** targeted analysis or experiment is required before decision.
- **Reject/reframe:** an option fails a gate or the decision context is unsound.
- **Supersede/retire:** post-implementation evidence changes or closes the decision.

Review quality is demonstrated by a defensible decision and follow-through—not the number of attendees or checklist ticks.

Continue with the one-page [Architecture Discovery cheat sheets](/architecture-discovery/cheat-sheets/).
