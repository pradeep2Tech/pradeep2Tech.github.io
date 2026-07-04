---
title: "VACUUM"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "VACUUM, autovacuum, bloat, freeze."
tags: ["postgresql-cheatsheet", "postgresql", "handbook", "interview"]
categories: ["PostgreSQL Handbook"]
shortTitle: "VACUUM"
module: 6
moduleTitle: "Production Operations"
sectionRef: "6.1"
weight: 601
interviewHandbook: true
aliases:
  - /postgresql-cheatsheet/vacuum/
---

## Quick Revision

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



## Interview Answers

## Question {#q-47}

How do idle-in-transaction sessions cause vacuum starvation?

### Short Answer

Idle in transaction holds a snapshot open, preventing vacuum from reclaiming dead tuples those transactions could still see.

### Detailed Explanation

Autovacuum cannot remove row versions still visible to any active snapshot. ORMs leaving transactions open after SELECT, or pgbouncer session pooling with forgotten BEGIN, are common causes.

### Production Notes

Alert on `state = 'idle in transaction'` duration; set `idle_in_transaction_session_timeout`.

### Common Mistakes

Blaming autovacuum without finding the long snapshot holder.

### Follow-up Questions

- What columns show bloat risk?
- When is VACUUM FULL OK?

---

## Question {#q-48}

What pg_stat_user_tables columns signal bloat risk?

### Short Answer

Vacuum marks dead space reusable and freezes xids. This directly answers: what pg_stat_user_tables columns signal bloat risk?

### Detailed Explanation

Autovacuum is essential on churn tables. For **Troubleshooting** depth, reason about failure modes and measurable signals before changing configuration.

### Internal Working

Canonical internals live on `/postgresql-cheatsheet/06-production-operations/vacuum/` — cite xmin/xmax, WAL, or planner nodes as appropriate.

### Production Notes

Confirm with metrics and staged tests; document rollback for HA and DDL changes.

### Common Mistakes

Applying generic blog tuning without workload evidence; ignoring pooler and replica lag.

### Follow-up Questions

- What metric would disprove your hypothesis?
- Which handbook page is the canonical source?

---

## Question {#q-49}

When is VACUUM FULL acceptable versus pg_repack?

### Short Answer

Vacuum marks dead space reusable and freezes xids. This directly answers: when is vacuum full acceptable versus pg_repack?

### Detailed Explanation

Autovacuum is essential on churn tables. For **Troubleshooting** depth, reason about failure modes and measurable signals before changing configuration.

### Internal Working

Canonical internals live on `/postgresql-cheatsheet/06-production-operations/vacuum/` — cite xmin/xmax, WAL, or planner nodes as appropriate.

### Production Notes

Confirm with metrics and staged tests; document rollback for HA and DDL changes.

### Common Mistakes

Applying generic blog tuning without workload evidence; ignoring pooler and replica lag.

### Follow-up Questions

- What metric would disprove your hypothesis?
- Which handbook page is the canonical source?

---

## Question {#q-50}

How does transaction ID wraparound threaten cluster availability?

### Short Answer

Vacuum marks dead space reusable and freezes xids. This directly answers: how does transaction id wraparound threaten cluster availability?

### Detailed Explanation

Autovacuum is essential on churn tables. For **Troubleshooting** depth, reason about failure modes and measurable signals before changing configuration.

### Internal Working

Canonical internals live on `/postgresql-cheatsheet/06-production-operations/vacuum/` — cite xmin/xmax, WAL, or planner nodes as appropriate.

### Production Notes

Confirm with metrics and staged tests; document rollback for HA and DDL changes.

### Common Mistakes

Applying generic blog tuning without workload evidence; ignoring pooler and replica lag.

### Follow-up Questions

- What metric would disprove your hypothesis?
- Which handbook page is the canonical source?

---

## Question {#q-52}

How do you tune per-table autovacuum settings for append-mostly versus churn-heavy tables?

### Short Answer

Vacuum marks dead space reusable and freezes xids. This directly answers: how do you tune per-table autovacuum settings for append-mostly versus churn-heavy tables?

### Detailed Explanation

Autovacuum is essential on churn tables. For **Troubleshooting** depth, reason about failure modes and measurable signals before changing configuration.

### Internal Working

Canonical internals live on `/postgresql-cheatsheet/06-production-operations/vacuum/` — cite xmin/xmax, WAL, or planner nodes as appropriate.

### Production Notes

Confirm with metrics and staged tests; document rollback for HA and DDL changes.

### Common Mistakes

Applying generic blog tuning without workload evidence; ignoring pooler and replica lag.

### Follow-up Questions

- What metric would disprove your hypothesis?
- Which handbook page is the canonical source?

---

## Question {#q-107}

What is the impact of unvacuumed tables on crash recovery duration?

### Short Answer

Vacuum marks dead space reusable and freezes xids. This directly answers: what is the impact of unvacuumed tables on crash recovery duration?

### Detailed Explanation

Autovacuum is essential on churn tables. For **Reliability** depth, reason about failure modes and measurable signals before changing configuration.

### Internal Working

Canonical internals live on `/postgresql-cheatsheet/06-production-operations/vacuum/` — cite xmin/xmax, WAL, or planner nodes as appropriate.

### Production Notes

Confirm with metrics and staged tests; document rollback for HA and DDL changes.

### Common Mistakes

Applying generic blog tuning without workload evidence; ignoring pooler and replica lag.

### Follow-up Questions

- What metric would disprove your hypothesis?
- Which handbook page is the canonical source?

---

## Question {#q-108}

How does freeze protect against transaction ID wraparound?

### Short Answer

Vacuum marks dead space reusable and freezes xids. This directly answers: how does freeze protect against transaction id wraparound?

### Detailed Explanation

Autovacuum is essential on churn tables. For **Reliability** depth, reason about failure modes and measurable signals before changing configuration.

### Internal Working

Canonical internals live on `/postgresql-cheatsheet/06-production-operations/vacuum/` — cite xmin/xmax, WAL, or planner nodes as appropriate.

### Production Notes

Confirm with metrics and staged tests; document rollback for HA and DDL changes.

### Common Mistakes

Applying generic blog tuning without workload evidence; ignoring pooler and replica lag.

### Follow-up Questions

- What metric would disprove your hypothesis?
- Which handbook page is the canonical source?


## See Also

- [Previous: Views](/postgresql-cheatsheet/05-advanced-features/views/)
- [Next: Monitoring](/postgresql-cheatsheet/06-production-operations/monitoring/)
- [PostgreSQL Handbook](/postgresql-cheatsheet/)
- [Database Handbook — PostgreSQL](/database-handbook/postgresql/)
