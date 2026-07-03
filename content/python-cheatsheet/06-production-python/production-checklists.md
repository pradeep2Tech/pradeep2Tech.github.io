---
title: "Production Checklists"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "Pre-deploy: pinned deps, health endpoints, structured logging, config audit. Incident: metrics → logs → profile."
tags: ["python", "python-cheatsheet", "handbook", "interview"]
categories: ["Python Handbook"]
shortTitle: "Checklists"
module: 6
moduleTitle: "Production Python"
sectionRef: "6.5"
weight: 605
ShowToc: true
interviewHandbook: true
---

## Quick Revision

Pre-deploy and incident checklists for Python services in production.

## Core Concepts

### Pre-deploy

| Check | Done |
| :--- | :---: |
| `requires-python` tested in CI matrix | ☐ |
| Lock file or pinned deps for apps | ☐ |
| Structured logging configured | ☐ |
| Health + readiness endpoints | ☐ |
| Secrets from vault/env — not repo | ☐ |
| Timeouts on outbound HTTP/DB | ☐ |
| Profiling baseline for hot paths | ☐ |

### Incident (first hour)

| Step | Action |
| :--- | :--- |
| 1 | Confirm scope — error rate, latency, which endpoints |
| 2 | Check recent deploys and config changes |
| 3 | Inspect logs with correlation ID |
| 4 | Metrics: CPU, memory, event-loop lag, pool exhaustion |
| 5 | Roll back or scale if clear regression |
| 6 | Profile if CPU/memory anomaly — [Profiling](/python-cheatsheet/05-performance/profiling/) |

## Production Usage

- Run tabletop exercises on checklists quarterly.
- Link runbooks from alerts.



## Interview Questions

See [Top 150](/python-cheatsheet/09-interview-guide/top-150-interview-questions/).

---

## See Also

- [Previous: Error Handling](/python-cheatsheet/06-production-python/error-handling/)
- [Next: Packaging](/python-cheatsheet/07-packaging-distribution/packaging/)
- [Python Handbook Index](/python-cheatsheet/)
- [Top 150 Interview Questions](/python-cheatsheet/09-interview-guide/top-150-interview-questions/)
