# Architecture Discovery Framework — Gap Analysis

**Status:** Phase 4 analysis  
**Date:** 2026-08-04  
**Scope:** Content boundaries and gaps only; no handbook articles were generated.

## 1. Executive conclusion

The repository has strong coverage of **solution design and implementation**, but no coherent handbook for the work that precedes those decisions: establishing engagement scope, gathering evidence, discovering business and operational context, assessing the current estate, resolving uncertainty, and converting findings into governed architecture deliverables.

The Architecture Discovery Framework should fill that workflow gap. It should not become another System Design, Microservices, Security Architecture, or Technology Decisions handbook.

The governing content rule is:

> Architecture Discovery owns **what to discover, who to involve, which evidence to collect, how to validate it, and which artifact records the outcome**. Existing domain handbooks remain canonical for **how the resulting architecture is designed and implemented**.

## 2. Analysis method

The assessment used the repository's curated indexes and targeted sources rather than a full repository scan:

- `docs/ai-index/SECTION-REGISTRY.md`
- relevant `data/*_modules.yaml` and `data/*_order.yaml` files
- representative pages from System Design, Microservices, Technology Decisions, Security Architecture, and Interview Preparation
- the Phase 3 Architecture Discovery navigation scaffold

Terms checked included discovery, requirements, NFRs, stakeholders, capabilities, domains, processes, modernization, migration, risks, ADRs, trust boundaries, data, integration, operations, governance, workshops, questionnaires, roadmaps, and deliverables.

## 3. Existing canonical coverage

| Concern | Existing canonical source | What it already covers | Architecture Discovery boundary |
|---|---|---|---|
| Design workflow | [System Design Process](/system-design/system-design-process/) | Interview and production design flow, requirements, HLD, APIs, data, scale, reliability, observability | Cover enterprise discovery before solution design: engagement scope, stakeholders, evidence, current state, validation, and handoff |
| Quality attributes | [Non-Functional Requirements](/system-design/non-functional-requirements/) | NFR catalog, prioritization, architecture levers, interview elicitation | Cover evidence-based NFR discovery, measurable acceptance criteria, conflicts, owners, and sign-off; link to the catalog |
| Modernization execution | [Microservices Migration & Modernization](/microservices/09-migration-modernization/) | Strangler migration, decomposition, database separation, zero-downtime deployment | Cover estate assessment, modernization drivers, option scoring, sequencing, dependencies, and readiness |
| Service boundaries | [Monolith Decomposition](/microservices/09-migration-modernization/monolith-decomposition/) | Domain-driven extraction and implementation tradeoffs | Cover domain discovery inputs and boundary evidence, then link to decomposition guidance |
| Architecture decisions | [Architecture Decision Records](/microservices/10-production-playbook/architecture-decision-records/) | ADR process and governance | Explain when discovery creates a decision candidate and how evidence feeds an ADR; do not reproduce the ADR guide |
| Technology selection | [Technology Decisions](/technology-playbook/) | Architecture patterns and technology decision matrices | Produce requirements, constraints, workload characteristics, and evaluation criteria; delegate selection detail |
| Database selection | [How to Choose a Database](/technology-playbook/how-to-choose-database/) | Workload framing, option comparison, validation, ADR checklist, production concerns | Discover data ownership, semantics, volume, access patterns, residency, lifecycle, and recovery needs |
| Security design | [Security Architecture](/security-architecture/) | Trust, identity, authorization, API/browser/service security, secrets, platforms, supply chain, operations | Discover assets, actors, trust boundaries, obligations, threats, control gaps, risk owners, and required reviews |
| Threat modeling | [Trust Boundaries and Threat Models](/security-architecture/trust-boundaries-and-threat-models/) | Detailed trust and control-placement architecture | Establish when threat modeling is required, collect its inputs, and link to the canonical method |
| Observability | [Microservices Observability](/microservices/08-observability/observability/) | Signals, telemetry, SLOs, tooling, diagnostics, and implementation | Discover operational outcomes, current signals, ownership, incident evidence, audit needs, and observability gaps |
| Product implementation | Engineering handbooks | Databases, cloud, Kubernetes, Kafka, language, and framework implementation | Record estate facts and constraints; link to product guidance rather than duplicating it |
| General interviews | [Interview Preparation](/interview-prep/) and section interview guides | Technology comparisons and architecture questions | Own discovery workshops, ambiguous customer scenarios, stakeholder probes, and evidence-based architecture exercises |

## 4. Duplicate-risk assessment

### High risk — cross-reference, do not restate

| Proposed subject | Collision | Required treatment |
|---|---|---|
| NFR reference catalog | System Design NFR guide | Create an elicitation and validation workflow; reuse the existing catalog by link |
| Strangler, decomposition, and migration mechanics | Microservices modernization module and Technology Decisions | Limit discovery content to assessment and option selection |
| Architecture patterns | Technology Decisions and Microservices | Record decision drivers and constraints only |
| Database, broker, cache, API, workflow, and platform selection | Technology Decisions | Feed structured criteria into canonical decision guides |
| OAuth, JWT, IAM, mTLS, secrets, API gateway, Kubernetes security | Security Architecture | Ask discovery questions and identify evidence/control gaps; never re-explain protocols or controls |
| Observability implementation | Microservices observability module | Discover operating requirements and current capability; link to implementation guidance |
| Cloud/Kubernetes/database internals | Engineering handbooks | Maintain inventory and constraint views only |

### Medium risk — narrow the architectural question

| Proposed subject | Potential overlap | Safe discovery question |
|---|---|---|
| System context diagram | System Design HLD diagrams | “What is inside the engagement boundary, and which external actors and systems constrain it?” |
| Domain model | DDD and decomposition discussions | “Which business concepts, rules, ownership boundaries, and language must the architecture preserve?” |
| API and integration catalog | API design and microservice communication | “What interfaces exist, who owns them, what contracts apply, and how critical are they?” |
| Data model | Database and system-design pages | “Which data domains, meanings, owners, flows, classifications, and lifecycle obligations exist?” |
| Architecture review | Microservices production checklist | “Is discovery evidence sufficient to authorize a decision or delivery stage?” |
| Security questionnaire | Security Architecture | “Which assets, actors, obligations, threats, and trust transitions require deeper security design?” |
| Modernization roadmap | Migration implementation pages | “How should change be sequenced by value, risk, dependency, and organizational readiness?” |

### Low risk — net-new repository capability

- discovery engagement charter and scope
- stakeholder map, decision rights, RACI, and escalation path
- workshop planning, facilitation, and follow-up
- evidence register, source reliability, confidence scoring, and contradiction handling
- business outcome and success-measure discovery
- capability map and value-stream discovery
- current-state estate inventory and dependency mapping
- assumptions, constraints, issues, risks, and decisions as distinct records
- discovery exit criteria and architecture sign-off
- deliverable selection based on decision need
- discovery backlog, unanswered questions, and evidence debt

## 5. Missing topics

No relevant navigation entries were found for stakeholder mapping, business capability mapping, discovery workshops, questionnaires, current-state assessment, evidence management, assumption logs, risk registers, integration catalogs, API catalogs, operating models, value streams, user journeys, or modernization roadmaps.

### P0 — foundational gaps

These topics are required before domain chapters can be used consistently.

| Gap | Architectural question answered | Expected output |
|---|---|---|
| Discovery charter | Why is discovery being performed, what is in scope, and who can decide? | Charter, scope boundary, objectives, decision calendar |
| Stakeholder and decision-rights analysis | Who owns outcomes, knowledge, risk, funding, and approval? | Stakeholder map, RACI, escalation path |
| Discovery lifecycle | How does evidence move from questions to decisions and deliverables? | Stages, entry/exit criteria, governance flow |
| Workshop operating model | How are sessions prepared, facilitated, recorded, and validated? | Workshop plan, participant matrix, follow-up backlog |
| Evidence and confidence management | Which claims are facts, assumptions, opinions, or unresolved conflicts? | Evidence register, confidence score, source and validation state |
| Current-state architecture baseline | What exists today and where are the critical dependencies and pain points? | Context, estate inventory, dependency map, baseline risks |
| Findings-to-decisions traceability | Why was a decision made and which evidence supports it? | Traceability from finding to requirement, risk, ADR, and roadmap item |

### P1 — discovery-domain gaps

| Domain | Missing coverage |
|---|---|
| Business | Outcomes, KPIs, strategic drivers, capabilities, value streams, funding constraints, regulatory drivers |
| Domain | Ubiquitous language, business rules, bounded-context candidates, ownership conflicts, domain events |
| Functional | Personas, journeys, use cases, exception paths, business rules, scope and acceptance boundaries |
| Process | As-is/to-be flows, handoffs, manual work, controls, bottlenecks, failure and compensation paths |
| NFR | Evidence sources, measurable targets, operating conditions, priority conflicts, acceptance and ownership |
| Integration | System/interface inventory, ownership, protocols, contracts, volumes, criticality, failure handling, change constraints |
| Data | Semantics, ownership, lineage, quality, classification, residency, retention, access, reconciliation, recovery |
| Security | Assets, actors, trust boundaries, abuse cases, compliance obligations, control evidence, exceptions and risk acceptance |
| Technology | Estate inventory, lifecycle status, standards, licensing, skills, vendor constraints, supportability, technical debt |
| Operations | Service ownership, SLOs, support model, incidents, observability maturity, deployment, DR, capacity, cost and FinOps |

### P1 — modernization and governance gaps

- modernization driver and outcome definition
- application and component assessment scorecards
- retain, retire, replace, rehost, replatform, refactor, and rebuild disposition criteria
- technical-debt classification tied to business impact
- dependency-aware migration waves
- coexistence and transition architecture
- organizational readiness, skills, funding, and change constraints
- benefit, risk, and architecture fitness measures
- risk, assumption, issue, dependency, and decision registers
- roadmap governance and reassessment triggers

### P2 — applied-learning gaps

- facilitated banking, healthcare, insurance, retail, telecom, government, manufacturing, and ERP scenarios
- incomplete and contradictory stakeholder evidence exercises
- architecture review simulations
- whiteboard exercises focused on discovery rather than solution recall
- reusable one-page checklists and workshop canvases
- architect interview questions about ambiguity, governance, and tradeoffs

## 6. Deliverable gaps

The repository contains examples of architecture artifacts inside solution pages, but it does not provide a cohesive guide for choosing, producing, validating, and governing enterprise discovery deliverables.

The new handbook should cover these artifact families without duplicating domain implementation content:

| Artifact family | Discovery-specific emphasis |
|---|---|
| Business | Purpose, audience, decision enabled, evidence, ownership, acceptance |
| Context and domain | Scope boundary, actors, capabilities, language, ownership, dependencies |
| Functional and journey | Behavior, scenarios, exceptions, rules, traceability |
| Quality attributes | Scenario, stimulus, environment, measurable response, owner, validation method |
| Data and integration | Catalog ownership, criticality, contracts, lineage, lifecycle, unresolved gaps |
| Security | Assets, trust boundaries, threats, obligations, controls, exceptions, risk owner |
| Solution and deployment | Decisions supported by discovery evidence, not generic design tutorials |
| Governance | Risks, assumptions, decisions, dependencies, approvals, review dates |
| Roadmap | Outcomes, transition states, dependencies, risks, measures, reassessment triggers |

## 7. Recommended content boundaries

Every future Architecture Discovery page should answer one of these questions:

1. What must the architect learn?
2. Who has the knowledge or decision authority?
3. Which questions expose the relevant facts and uncertainty?
4. What evidence proves or disproves the claims?
5. Which diagram, register, catalog, or decision record captures the result?
6. What is the completion or quality criterion?
7. Which existing handbook provides the deeper design or implementation guidance?

A page should be merged, redirected, or replaced with a cross-reference when its primary purpose is to explain:

- a solution pattern
- a product or protocol
- implementation code
- platform configuration
- a security control in depth
- system-design interview mechanics already covered elsewhere

## 8. Cross-reference policy

Use contextual links at the decision boundary, not generic “further reading” lists.

Examples:

- After an NFR discovery matrix identifies availability targets, link to the System Design NFR guide.
- After data discovery captures workload and consistency needs, link to the database decision framework.
- After a trust-boundary workshop identifies threats, link to Security Architecture for control design.
- After modernization assessment selects incremental replacement, link to the Microservices strangler guidance.
- After observability discovery establishes SLO and diagnostic gaps, link to the Microservices observability module.

## 9. Recommended roadmap implications

Phase 5 should prioritize the handbook in this order:

1. Discovery charter, lifecycle, stakeholders, workshops, evidence, and current-state baseline
2. Business, domain, functional, process, NFR, integration, data, security, technology, and operations discovery
3. Modernization assessment, risk governance, traceability, and roadmap design
4. Deliverable selection and quality criteria
5. Templates and checklists
6. Case studies, cheat sheets, and interview material

The roadmap should favor fewer integrated pages over separate pages for every artifact or question. Templates, questionnaires, and checklists should be reusable assets linked from domain chapters.

## 10. Phase 4 decision

Proceed to roadmap design with these constraints:

- The new section is a discovery workflow and evidence system, not another solution-design encyclopedia.
- Existing handbooks remain canonical for patterns, products, protocols, controls, and implementation.
- High-risk duplicate subjects must be handled through short discovery-specific framing and explicit cross-links.
- Foundational discovery mechanics must be written before domain chapters.
- No content-generation phase should begin until the roadmap and reusable content templates are approved.
