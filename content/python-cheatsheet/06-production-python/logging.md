---
title: "Logging"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "Structured JSON logs; `logging` handlers/formatters; correlation IDs via `contextvars`. Avoid duplicate handlers."
tags: ["python", "python-cheatsheet", "handbook", "interview"]
categories: ["Python Handbook"]
shortTitle: "Logging"
module: 6
moduleTitle: "Production Python"
sectionRef: "6.1"
weight: 601
ShowToc: true
interviewHandbook: true
---

## Quick Revision

- One configured root hierarchy — avoid duplicate handlers.
- **Structured JSON** logs for search/alerting; include `trace_id`, `level`, `message`.
- Log once at boundary with `exc_info=True` on errors.

## Core Concepts

| Piece | Role |
| :--- | :--- |
| `Logger` | Named channel (`logging.getLogger(__name__)`) |
| `Handler` | Where records go (stdout, file, HTTP) |
| `Formatter` | Layout (JSON vs text) |
| `Filter` | Sampling, PII redaction |

## Internal Working

```mermaid
flowchart LR
  LOG[Logger] --> H[Handler]
  H --> F[Formatter]
  F --> OUT[stdout / aggregator]
```

Use `contextvars` to inject correlation IDs into log records across [asyncio](/python-cheatsheet/04-concurrency/asyncio/) tasks.

## Production Usage

```python
import logging
import json
import contextvars

request_id = contextvars.ContextVar("request_id", default="-")

class JsonFormatter(logging.Formatter):
    def format(self, record):
        return json.dumps({
            "level": record.levelname,
            "msg": record.getMessage(),
            "request_id": request_id.get(),
            "logger": record.name,
        })

logger = logging.getLogger("app")
handler = logging.StreamHandler()
handler.setFormatter(JsonFormatter())
logger.addHandler(handler)
logger.setLevel(logging.INFO)
```

## Troubleshooting

| Symptom | Fix |
| :--- | :--- |
| Duplicate log lines | Multiple handlers on root + child |
| Missing context | Set `ContextVar` in middleware |
| Log volume cost | INFO in hot path → DEBUG behind flag |

## Common Mistakes

- `logging.basicConfig` in libraries.
- Logging full payloads with PII.



## Interview Questions

See [Top 150](/python-cheatsheet/09-interview-guide/top-150-interview-questions/).

---

## See Also

- [Previous: Memory Optimization](/python-cheatsheet/05-performance/memory-optimization/)
- [Next: Configuration Management](/python-cheatsheet/06-production-python/configuration-management/)
- [Python Handbook Index](/python-cheatsheet/)
- [Top 150 Interview Questions](/python-cheatsheet/09-interview-guide/top-150-interview-questions/)
