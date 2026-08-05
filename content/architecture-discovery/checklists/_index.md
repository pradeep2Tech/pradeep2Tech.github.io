---
title: "Enterprise Discovery Questionnaire"
date: 2026-08-05T00:00:00+05:30
draft: true
description: "A reusable, evidence-oriented question bank spanning business, domain, functional, quality, integration, data, security, technology, operations, compliance, risk, modernization, and handoff."
tags: ["architecture-discovery", "questionnaire", "checklist", "reference"]
categories: ["Architecture Discovery"]
shortTitle: "Enterprise Discovery Questionnaire"
module: 4
moduleTitle: "Applied Resources"
contentType: "reference"
difficulty: "advanced"
estimatedReadingTime: 45
interviewImportance: "critical"
enterpriseImportance: "critical"
prerequisites: ["Questionnaire Operating Guide", "Core Discovery Domains", "Architecture Risk and Synthesis"]
dependencies: ["discovery-questionnaire", "business-discovery", "domain-discovery", "functional-discovery", "non-functional-discovery", "integration", "data", "security", "technology", "operational", "risk"]
---

This questionnaire is a routing library, not a form. Select questions that can change a decision, ask them of people who own the fact or evidence, and follow contradictions. Record source, confidence, owner, action, and decision impact with every material answer.

Use the [Questionnaire Operating Guide](/architecture-discovery/discovery-questionnaire/) for tailoring, facilitation, and evidence discipline.

## Engagement and Decision Context

- What decision must this discovery enable, by whom, and by when?
- What business outcome or exposure justifies the work?
- What is explicitly inside and outside scope, and who may change it?
- Which commitments have already been made, and with what authority?
- What would make the engagement stop, pause, expand, or succeed?
- Which decisions are reversible, expensive, or deadline constrained?
- Who owns value, architecture, data, security, operations, funding, and residual risk?
- Which stakeholders can provide evidence rather than opinion?
- What current initiatives, contracts, or organizational changes intersect the scope?
- Which terms or assumptions are already disputed?

## Business Context and Outcomes

- Which customer, market, policy, regulatory, financial, or operational forces require change?
- Which outcomes matter, to which actors, over what time horizon?
- What baseline demonstrates the current state?
- Which leading and lagging measures prove improvement?
- Who owns each measure and benefits realization?
- What is the cost of delay or continued exposure?
- Which outcomes conflict, and who accepts the tradeoff?
- Which capability gaps prevent the outcome?
- Which value streams, funding mechanisms, and operating-model constraints shape delivery?
- What business scenario would invalidate the proposed scope?

## Domain and Business Rules

- Which terms have different meanings across teams or systems?
- What are the core concepts, invariants, policies, calculations, and exceptions?
- Who owns each definition and rule?
- Which source prevails when policy, procedure, code, and practice disagree?
- What bounded contexts or ownership seams are visible?
- Where does shared data conceal conflicting authority?
- Which domain events represent completed facts, and who owns them?
- Which cross-domain interactions are commands, events, or queries?
- Which consistency and ordering expectations protect business invariants?
- How are rule versions, effective dates, overrides, and corrections evidenced?

## Actors, Journeys, and Functional Behavior

- Who initiates, participates in, supports, governs, or is affected by the outcome?
- What goals, authority, channels, accessibility needs, and operating conditions differ by actor?
- Where does the end-to-end journey begin and finish?
- Which handoffs, waits, abandonment points, and workarounds occur?
- What is the normal scenario and the success guarantee?
- Which alternate, failure, timeout, duplicate, concurrency, and recovery scenarios matter?
- What remains outside the solution boundary, and under whose responsibility?
- Which validations, permissions, calculations, state transitions, and exceptions apply?
- Can every consequential decision be reproduced later?
- What positive, negative, boundary, and recovery evidence defines acceptance?

## Business Process

- How does a recent real case move from trigger to verified outcome?
- How does observed behavior differ from documented procedure?
- Where are manual queues, spreadsheets, email, batch windows, or direct data corrections used?
- What are volume, touch time, elapsed time, backlog age, rework, and exception distributions?
- Where does ownership change or work become orphaned?
- Which steps are controls, and what risk do they address?
- What happens under missing information, dependency failure, partial success, or late arrival?
- Which actions retry, resume, reverse, compensate, reconcile, escalate, or abandon?
- Which activities should be eliminated, simplified, assisted, automated, or retained?
- How will the target process preserve control intent and human judgment?

## Quality Attributes

- Which actor-visible stimulus, environment, response, and measure define each critical quality scenario?
- What current baseline and evidence support the target?
- What workload mix, volume, concurrency, burst, growth, and data shape apply?
- Which percentile, window, population, or exclusion determines acceptance?
- Which operations require availability, consistency, or safe degradation?
- What are business-level RTO, RPO, maximum uncertainty, and backlog-clearance needs?
- Which security, accessibility, operability, modifiability, interoperability, and cost scenarios govern design?
- Where do quality attributes conflict?
- What end-to-end budgets and dependency contracts are feasible?
- Which test, exercise, telemetry, and accountable owner will prove each scenario?

## Integration and Dependencies

- Which external fact or action is required for each outcome?
- Who owns provider semantics, operation, and consumer use?
- What direct, transitive, shared-platform, and control-plane dependencies exist?
- What are interaction intent, contract, timing, data, security, and lifecycle?
- How do consumers interpret, cache, retry, or depend on undocumented behavior?
- What does a timeout mean for business state?
- What stable key prevents duplicate business effects?
- What loss, duplication, delay, ordering, replay, and staleness are tolerable?
- How are ambiguous outcomes, partial success, and poison data reconciled?
- How do contracts evolve, consumers migrate, and obsolete versions retire?

## Data

- Which material data concepts drive outcomes, decisions, money, safety, or reporting?
- What does each concept mean in each domain context?
- Who owns semantics, authoritative state, stewardship, controls, and consumer fitness?
- Which source is authoritative for each attribute and lifecycle stage?
- What identifiers, matching, merge/split, and conflict rules apply?
- Which consumers use the data for which purpose and quality threshold?
- How is data created, transformed, moved, derived, corrected, and deleted?
- What business, system, dataset, field, or runtime lineage is required?
- How are quality failures quarantined, owned, corrected, and propagated?
- How are independently recorded states reconciled?
- What effective-time, event-time, version, and restatement semantics apply?
- What migration, coexistence, and decommission evidence is required?

## Security, Privacy, and Compliance

- Which assets and business actions would create material harm if misused?
- Which human, workload, device, partner, support, and privileged actors exist?
- How are identity assurance, authentication, delegation, authorization, and lifecycle handled?
- Where do ownership, control, assurance, tenancy, or data-handling assumptions change?
- What abuse paths cross those trust boundaries?
- Which preventive, detective, responsive, and recovery controls have operating evidence?
- Which laws, regulations, contracts, policies, and standards actually apply to this scope?
- How do obligations map to control intent, owner, implementation, and evidence?
- What purpose, minimization, consent, residency, retention, deletion, and subject-right rules apply?
- Which control gaps remain, what compensates, and who may accept residual risk?

## Technology Estate and Constraints

- Which runtime, platform, SaaS, open-source, delivery, and control-plane assets enable the outcome?
- What are their versions, owners, lifecycle, support, contracts, and skills?
- Which deployed/runtime facts contradict declared inventory?
- How well does each technology fit workload, data, quality, operations, and change?
- Where are common-mode, supplier, license, or specialist concentrations?
- Which conditions are obligations, constraints, standards, paved roads, preferences, assumptions, or debt?
- What business consequence and trajectory does technical debt create?
- Which exception processes and expiry rules apply?
- What decision gates and weighted criteria should distinguish target options?
- Which consequential uncertainty requires an architecture experiment?

## Operations and Delivery

- What is the service boundary, critical journey, tier, and accountable owner?
- Who may declare severity, degrade service, fail over, restore, replay, correct, or communicate?
- What support hours, on-call, skills, escalation, supplier, and shared responsibilities apply?
- Which outcome indicators, incidents, blind spots, and recurring causes define the baseline?
- Can operators detect, diagnose, contain, restore, reconcile, and verify the outcome?
- Which alerts are actionable, and what do error budgets govern?
- How do code, data, schema, configuration, policy, and infrastructure changes reach production?
- Which environments, approvals, coordination, compatibility, and rollback constraints exist?
- What deployment strategy and production verification are safe?
- Which runbooks and recovery exercises demonstrate readiness?

## Capacity, Continuity, and Economics

- What normal, peak, burst, seasonal, failure, and recovery demand must be supported?
- Where are saturation, quota, queue, data, dependency, and human-capacity limits?
- What headroom covers scaling lead time and uncertainty?
- Which journeys continue, degrade, queue, or stop during each disruption?
- What recovery order and capacity clear backlog within the objective?
- How are cost and consumption attributed to service, workload, tenant, and outcome?
- What are fixed, variable, transfer, license, support, observability, migration, and exit costs?
- Which unit economics and forecast ranges support decisions?
- What optimization would increase reliability, security, delivery, or lock-in risk?
- Which commercial commitments constrain future options?

## Modernization and Transition

- Which outcomes justify modernization rather than targeted remediation?
- What capability, domain, application, component, data, and dependency units are assessed?
- What value, fit, risk, cost, and readiness evidence supports each disposition?
- Should each unit be retained, retired, consolidated, replaced, rehosted, replatformed, refactored, or rebuilt?
- What current strengths should be preserved?
- Which interim production states are required?
- How are routing, authority, synchronization, compatibility, controls, and in-flight work handled?
- When does rollback cease to be safe?
- Which dependency sequence and wave delivers useful learning and outcome earliest?
- What entry, exit, retirement, readiness, and fitness evidence governs each wave?

## Risk, Options, and Decision

- Which statements are findings, risks, assumptions, issues, dependencies, constraints, or decisions?
- What cause–event–effect scenario and evidence define each risk?
- Which assumptions are decision-sensitive and when must they be tested?
- What treatment changes likelihood, impact, detection, or recovery?
- Who owns response, action, control operation, and residual acceptance?
- Which decision themes emerge from the findings?
- What genuinely different viable architecture options exist?
- Which mandatory gates eliminate an option?
- How do value, fit, quality, risk, cost, transition, and uncertainty compare?
- What sensitivity, dissent, conditions, residual risk, and trigger accompany the recommendation?

## Closure and Handoff

- Has every chartered architectural question reached an accepted state or governed open action?
- Are evidence gaps and contradictions visible?
- Are outcomes, requirements, measures, decisions, and deliverables traceable?
- Which unresolved items block the next decision, and which can continue with conditions?
- Have delivery, operations, data, security, risk, and benefit owners accepted responsibility?
- Which artifacts are authoritative, current, owned, and lifecycle-managed?
- What conditions, waivers, experiments, and due dates carry forward?
- Which fitness measures and production signals validate the architecture?
- What context change or threshold triggers reassessment?
- What evidence will prove legacy retirement and benefit realization?

## Recording Template

For each material answer record:

| Field | Value |
|---|---|
| Question ID/domain | Stable reference |
| Answer/finding | Precise statement |
| Source/evidence | Link, observation, data, interview |
| Confidence/contradiction | High/medium/low and competing claims |
| Owner | Accountable fact or action owner |
| Decision impact | Requirement, risk, option, scope, measure |
| Follow-up | Action, due date, validation, review gate |

## Quality Check

The questionnaire has succeeded when answers change or validate decisions, evidence is distinguishable from assertion, contradictions are governed, owners accept follow-up, and the team can stop asking questions that do not affect scope, requirements, risk, options, or acceptance.

Next use the [Discovery Engagement Checklist](/architecture-discovery/checklists/discovery-engagement-checklist/) before starting a new engagement.
