---
title: "JSON & JSONB"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "json vs jsonb, operators, indexing with GIN, and path queries."
tags: ["postgresql-cheatsheet", "postgresql", "cheatsheet", "handbook"]
categories: ["PostgreSQL Cheatsheet"]
shortTitle: "JSON"
module: 6
moduleTitle: "Advanced SQL"
sectionRef: "6.5"
ShowToc: true
---

## Executive Summary

PostgreSQL offers **json** (text storage) and **jsonb** (binary, indexable). Prefer **jsonb** for querying; **json** preserves exact formatting.

---

## Core Concepts

| Operator | Meaning |
| :--- | :--- |
| `->` | Get JSON object field (as json) |
| `->>` | Get field as text |
| `#>` | Path array |
| `@>` | Contains |
| `?` | Key exists |
| `jsonb_set` | Update nested value |

---

## Quick Reference

```sql
SELECT payload->>'kind' AS kind,
       payload->'meta'->>'ip' AS ip
FROM events
WHERE payload @> '{"kind":"login"}';

UPDATE settings
SET body = jsonb_set(body, '{theme}', '"dark"')
WHERE user_id = 1;
```

---

## Snippets

```sql
CREATE TABLE events (
  id bigserial PRIMARY KEY,
  payload jsonb NOT NULL DEFAULT '{}'
);
CREATE INDEX idx_events_kind ON events ((payload->>'kind'));
CREATE INDEX idx_events_gin ON events USING gin (payload jsonb_path_ops);
```

---

## Common Gotchas

- `jsonb` deduplicates keys and does not preserve key order.
- Cast with `::jsonb` — invalid JSON throws error.
- For heavy JSON analytics consider generated columns + B-tree index.

---

## Related Topics

- [Previous: Windows](/postgresql-cheatsheet/window-functions/)
- [Next: Functions](/postgresql-cheatsheet/functions/)
- [PostgreSQL Cheatsheet Index](/postgresql-cheatsheet/)
- [Database Handbook — PostgreSQL](/database-handbook/postgresql/)
