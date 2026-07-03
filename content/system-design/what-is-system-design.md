---
title: "What Is System Design?"
date: 2026-07-04T10:00:00+00:00
draft: false
description: "Architect-level definition of system design — functional vs non-functional requirements, core components, quality attributes, and what interviewers evaluate."
tags: ["system-design", "foundations", "architecture", "interview"]
categories: ["System Design"]
shortTitle: "What Is System Design?"
module: 1
moduleTitle: "Foundations"
sectionRef: "1.1"
ShowToc: true
---

## Overview

**System design** is the discipline of defining how software components, data stores, networks, and operational practices work together to meet product requirements at target scale. It sits between product requirements and implementation: you decide *what* to build, *how* pieces connect, and *which* trade-offs are acceptable before writing production code.

For senior engineers and architects, system design means answering four questions under constraints:

1. **What** must the system do? (functional requirements)
2. **How well** must it do it? (non-functional requirements)
3. **At what scale** must it operate? (capacity and growth)
4. **What fails first** when load or faults increase? (bottlenecks and blast radius)

In interviews, system design evaluates whether you can structure ambiguity, quantify scale, draw a coherent architecture, and defend trade-offs — not whether you memorized a single “correct” diagram.

---

## Why It Matters

| Stakeholder | Why system design matters |
| :--- | :--- |
| **Product** | Wrong architecture delays features for quarters |
| **Engineering** | Poor boundaries create rewrite cycles |
| **Operations** | Missing reliability/observability design drives pager pain |
| **Business** | Cost and compliance failures show up at scale, not in POCs |

Architects use system design to **reduce irreversible decisions early**. Choosing a monolith vs microservices, SQL vs event log, or sync vs async has multi-year cost. System design makes those choices explicit and measurable.

---

## Core Concepts

### Functional vs non-functional requirements

| Type | Definition | Examples |
| :--- | :--- | :--- |
| **Functional** | What the system must do | “User can shorten a URL”, “Send OTP in < 2s” |
| **Non-functional** | How well it must do it | Latency p99, 99.9% availability, 10× peak burst |

Functional requirements define features. Non-functional requirements (NFRs) define **quality attributes** and drive architecture. See [Non-Functional Requirements](/system-design/non-functional-requirements/) for the full NFR catalog.

### System components (typical production stack)

| Layer | Responsibility | Common technologies |
| :--- | :--- | :--- |
| **Clients** | Web, mobile, partner APIs | Browsers, SDKs |
| **Edge / CDN** | TLS termination, caching, DDoS scrubbing | CloudFront, Akamai |
| **Ingress** | Load balancing, routing, rate limits | ALB, NGINX, Envoy |
| **Application** | Business logic, orchestration | Stateless services |
| **Data** | Persistence, search, cache | PostgreSQL, Redis, OpenSearch |
| **Async** | Decoupling, buffering, fan-out | Kafka, SQS, RabbitMQ |
| **Observability** | Metrics, logs, traces, alerts | Prometheus, ELK, OpenTelemetry |

### Quality attributes architects optimize

| Attribute | One-line definition | Typical tension |
| :--- | :--- | :--- |
| **Scalability** | Handle more load by adding resources | vs cost and operational complexity |
| **Reliability** | Correct behavior over time | vs latency (retries, fsync) |
| **Availability** | System is reachable when needed | vs consistency (CAP) |
| **Maintainability** | Teams can change system safely | vs delivery speed |
| **Security** | Confidentiality, integrity, availability | vs UX and performance |
| **Cost** | Infra + engineering TCO | vs all other NFRs |

```mermaid
flowchart LR
    REQ[Requirements]
    CAP[Capacity Planning]
    ARCH[Architecture]
    DATA[Data Design]
    SCALE[Scaling]
    REL[Reliability]
    OBS[Observability]

    REQ --> CAP --> ARCH --> DATA --> SCALE --> REL --> OBS
```

This pipeline is the backbone of production design and the [System Design Process](/system-design/system-design-process/) interview framework.

---

## Architect Perspective

### How architects think

Architects do not start with microservices or Kubernetes. They start with **constraints and failure modes**:

1. **Clarify scope** — MVP vs 5-year horizon; read vs write ratio; consistency needs
2. **Quantify** — Back-of-envelope QPS, storage, bandwidth ([Capacity Estimation](/system-design/capacity-estimation/))
3. **Identify the hot path** — What request must be fastest? What data is contended?
4. **Draw boundaries** — Services, data ownership, sync vs async edges
5. **Design for failure** — SPOFs, retries, degradation, multi-AZ/region
6. **Make trade-offs explicit** — Document what you optimize and what you sacrifice

### What interviewers evaluate

| Dimension | Strong signal | Weak signal |
| :--- | :--- | :--- |
| **Requirements** | Asks clarifying questions; separates MVP from nice-to-have | Jumps to diagram without scope |
| **Estimation** | Reasonable orders of magnitude | Random numbers or no math |
| **Architecture** | Clear components and data flow | Buzzword soup |
| **Deep dive** | Explains bottleneck and mitigation | Stays shallow on hard parts |
| **Trade-offs** | Names alternatives and why rejected | Single “best” answer |
| **Operations** | Monitoring, rollout, failure recovery | Ignores observability and ops |

### Common system design workflow

| Phase | Output |
| :--- | :--- |
| 1. Requirements | Functional list + NFR table |
| 2. Capacity | QPS, storage, bandwidth estimates |
| 3. High-level design | Boxes-and-arrows diagram |
| 4. API + data model | Key endpoints and entities |
| 5. Deep dives | 2–3 hard problems (scaling, consistency, fan-out) |
| 6. Reliability + observability | SPOF removal, SLOs, metrics |

---

## Common Mistakes

| Mistake | Why it fails | Fix |
| :--- | :--- | :--- |
| Starting with technology | Locks in wrong tool before requirements | Requirements → estimation → design |
| Ignoring write path on read-heavy systems | Caches hide write bottlenecks | Size writes and consistency explicitly |
| Treating availability = reliability | Different metrics and designs | Define both — [Reliability vs Availability](/system-design/reliability-vs-availability/) |
| No failure discussion | Interviewers test production thinking | Name 2–3 failure modes per component |
| Over-engineering MVP | Wastes time in 45-min interviews | State phased rollout |

---

## Interview Questions

1. **What is system design, and how is it different from detailed design or coding?**
2. **How do functional and non-functional requirements drive architecture differently?**
3. **Name five quality attributes and give a trade-off between two of them.**
4. **What would you clarify first in a “design Twitter” interview?**
5. **How do you know when a monolith is sufficient vs when to decompose?** See [Architecture Styles Overview](/system-design/architecture-styles-overview/).

---

## Related Topics

- [System Design Process](/system-design/system-design-process/) — step-by-step interview framework
- [Non-Functional Requirements](/system-design/non-functional-requirements/) — NFR catalog and matrix
- [Capacity Estimation](/system-design/capacity-estimation/) — QPS, storage, bandwidth math
- [URL Shortener](/system-design/urlshortner/) — end-to-end case study applying this workflow
- [Networking Essentials](/system-design/networking-essentials-ip-dns-firewalls/) — transport and perimeter fundamentals

---

## Deep Dive References

| Topic | Handbook | Page |
| :--- | :--- | :--- |
| Architecture decision records | Microservices | [Architecture Decision Records](/microservices/10-production-playbook/architecture-decision-records/) |
| Production readiness checklist | Microservices | [Architecture Review Checklist](/microservices/10-production-playbook/architecture-review-checklist/) |
| Architecture pattern selection | Technology Playbook | [Module Architecture Patterns](/technology-playbook/module-architecture-patterns/) |

**Distributed Systems:** [CAP & PACELC](/system-design/cap-and-pacelc/) · [Consistency Models](/system-design/consistency-models/) · [Consistent Hashing](/system-design/consistent-hashing/)

**Architecture Styles:** [Architecture Styles Overview](/system-design/architecture-styles-overview/)

**Observability:** [Observability Fundamentals](/system-design/observability-fundamentals/)

**Reliability:** [Availability & Nines](/system-design/availability-and-nines/) · [Reliability vs Availability](/system-design/reliability-vs-availability/) · [Resilience Patterns Overview](/system-design/resilience-patterns-overview/)
