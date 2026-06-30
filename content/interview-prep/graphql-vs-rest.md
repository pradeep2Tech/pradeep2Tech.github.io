---
title: "GraphQL vs REST"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Client-driven queries vs resource-oriented endpoints."
tags: ["technology-playbook", "comparison", "graphql"]
categories: ["Technology Playbook"]
shortTitle: "GraphQL vs REST"
module: 8
moduleTitle: "Interview Preparation"
sectionRef: "8.6"
weight: 805
ShowToc: true
---
## 1. Executive Summary

**GraphQL vs REST** — Client-driven queries vs resource-oriented endpoints. Use this comparison in architecture reviews and interviews to justify a choice with trade-offs, not slogans.

---

## 2. What Problem It Solves

Architects face **option overload** — vendors, cloud defaults, and team familiarity pull in different directions. A structured comparison prevents **resume-driven architecture**.

---

## 3. Where It Fits in Architecture

```mermaid
flowchart TD
  need[Integration / Data Need] --> eval{"GraphQL vs REST"}
  eval --> pickA[Graphql]
  eval --> pickB[Rest]
```

---

## 4. When to Choose Graphql

- Workload characteristics align with its sweet spot (see table below)
- Team operational maturity matches the product
- Enterprise support, licensing, or cloud bundle favors it

---

## 5. When Not to Choose / Choose Alternative

- Non-functional requirements (latency, ordering, cost) clearly favor the other side
- Existing platform standard or skill pool points elsewhere
- Managed service removes ops burden you cannot staff

---

## 6. Popular Tools / Products

See detailed topic pages for each option in the [Technology Playbook index](/technology-playbook/).

---

## 7. Trade-offs

{{< comparison-table caption="GraphQL vs REST" >}}
| Capability | Graphql | Rest |
| :--- | :--- | :--- |
| Primary model | See product docs | See product docs |
| Ops burden | Team-dependent | Team-dependent |
| Best fit | Match to access pattern | Match to access pattern |
{{< /comparison-table >}}

{{< pros-cons pros="<ul><li>Left option: strengths for its primary use case</li><li>Right option: strengths for its primary use case</li></ul>" cons="<ul><li>Left option: operational or model limitations</li><li>Right option: operational or model limitations</li></ul>" >}}

---

## 8. Real-World Example

**Notification platform:** High fan-out and replay → log-oriented broker. **Task queue with routing keys and priority** → classic AMQP. **Serverless glue** → cloud-native queue with pay-per-use.

---

## 9. Failure Scenarios

- Choosing based on **brand** without load testing representative traffic
- Ignoring **egress/ licensing** cost at scale
- **Hybrid** deployment without clear ownership of upgrades and security patches

---

## 10. Best Practices

1. Run a **two-week POC** with production-like volume skew (not happy-path only).
2. Document decision in an **ADR** with rejected alternatives.
3. Revisit when **scale doubles** or team skills shift.

---

## 11. Interview Answer

{{< interview-answer >}}
"There is no universal winner in **GraphQL vs REST**. I compare delivery semantics, ops model, ordering, replay, and team skills. I give a concrete scenario — for example peak checkout events vs nightly batch — and map each option to that scenario before recommending one."
{{< /interview-answer >}}

---

## 12. Related Topics

- [Technology Decision Matrix](/technology-playbook/how-to-choose-database/)
- [Interview Preparation module](/technology-playbook/)
