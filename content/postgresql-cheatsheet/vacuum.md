---
title: "VACUUM"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "VACUUM, ANALYZE, autovacuum, bloat, and freeze visibility."
tags: ["postgresql-cheatsheet", "postgresql", "cheatsheet", "handbook"]
categories: ["PostgreSQL Cheatsheet"]
shortTitle: "VACUUM"
module: 8
moduleTitle: "Operations & Maintenance"
sectionRef: "8.1"
ShowToc: true
---

## Executive Summary

**VACUUM** reclaims dead tuple space and updates visibility maps. **ANALYZE** refreshes planner statistics. **Autovacuum** runs both automatically.

---

## Core Concepts

| Command | Purpose |
| :--- | :--- |
| `VACUUM` | Reclaim space (often reusable in-place) |
| `VACUUM ANALYZE` | Vacuum + stats |
| `VACUUM FULL` | Rewrites table — exclusive lock — last resort |
| Autovacuum | Background — tune `autovacuum_vacuum_scale_factor` |

---

## Quick Reference

```sql
VACUUM (VERBOSE, ANALYZE) orders;

SELECT schemaname, relname, n_dead_tup, last_autovacuum, autovacuum_count
FROM pg_stat_user_tables
ORDER BY n_dead_tup DESC;
```

---

## Snippets

```sql
-- Bloat estimate (simplified — use pgstattuple extension for detail)
SELECT relname, pg_size_pretty(pg_total_relation_size(oid))
FROM pg_class WHERE relkind = 'r' ORDER BY pg_total_relation_size(oid) DESC;
```

---

## Common Gotchas

- `VACUUM FULL` blocks writes — use `pg_repack` extension for online reclaim when needed.
- Freeze protects against transaction ID wraparound — monitor `age(datfrozenxid)`.
- Aggressive autovacuum on append-mostly tables may be wasteful — tune per-table.

---

## Related Topics

- [Previous: Procedures](/postgresql-cheatsheet/stored-procedures/)
- [Next: Backup](/postgresql-cheatsheet/backup-restore/)
- [PostgreSQL Cheatsheet Index](/postgresql-cheatsheet/)
- [Database Handbook — PostgreSQL](/database-handbook/postgresql/)
