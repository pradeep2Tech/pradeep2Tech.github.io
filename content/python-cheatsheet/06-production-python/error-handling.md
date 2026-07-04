---
title: "Error Handling"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "Map domain exceptions at boundaries; log once with `exc_info=True`; retries for transient errors only."
tags: ["python", "python-cheatsheet", "handbook", "interview"]
categories: ["Python Handbook"]
shortTitle: "Errors"
module: 6
moduleTitle: "Production Python"
sectionRef: "6.4"
weight: 604
interviewHandbook: true
---

## Quick Revision

- Catch **specific** exceptions; map to HTTP/status at **outer boundary** only.
- `raise ... from e` preserves chains for debugging.
- Retry transient errors with backoff — not all exceptions.

## Core Concepts

| Layer | Responsibility |
| :--- | :--- |
| Domain | Raise meaningful `AppError` types |
| Service | Translate infrastructure failures |
| API boundary | Map to status codes, log once |

## Production Usage

- Log with `logger.exception` or `exc_info=True` once at handler.
- Use idempotency keys for safe retries on 5xx paths.
- Distinguish client errors (4xx) from server errors (5xx).

## Common Mistakes

- Bare `except:` swallowing `KeyboardInterrupt`.
- Returning stack traces to clients in production.



## Interview Questions

See [Top 150](/python-cheatsheet/09-interview-guide/top-150-interview-questions/).

---

## See Also

- [Previous: Observability](/python-cheatsheet/06-production-python/observability/)
- [Next: Production Checklists](/python-cheatsheet/06-production-python/production-checklists/)
- [Python Handbook Index](/python-cheatsheet/)
- [Top 150 Interview Questions](/python-cheatsheet/09-interview-guide/top-150-interview-questions/)
