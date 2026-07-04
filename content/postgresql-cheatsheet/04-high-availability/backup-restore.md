---
title: "Backup & Restore"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "pg_dump, pg_restore, base backup, PITR overview."
tags: ["postgresql-cheatsheet", "postgresql", "handbook", "interview"]
categories: ["PostgreSQL Handbook"]
shortTitle: "Backup"
module: 4
moduleTitle: "High Availability"
sectionRef: "4.3"
weight: 403
interviewHandbook: true
aliases:
  - /postgresql-cheatsheet/backup-restore/
---

## Quick Revision

Choose **logical** (`pg_dump`) for portability and selective restore; **physical** (base backup + WAL) for PITR and large DBs.

---

## Core Concepts

| Method | Granularity | PITR |
| :--- | :--- | :--- |
| `pg_dump` / `pg_restore` | DB/schema/table | No |
| `pg_dumpall` | Cluster globals + DBs | No |
| Base backup + WAL archive | Whole cluster | Yes |
| `COPY` | Table CSV/binary | No |

---

## Quick Reference

```bash
pg_dump -Fc -f app.dump appdb
pg_restore -d appdb_new -j 4 app.dump

pg_dump -t orders appdb > orders.sql
```

---

## Snippets

```bash
# Physical backup (simplified)
pg_basebackup -D /backup/base -Ft -z -P
# WAL archive → [WAL](/postgresql-cheatsheet/02-core-postgresql/wal/) and [Disaster Recovery](/postgresql-cheatsheet/04-high-availability/disaster-recovery/)
```

---

## Common Gotchas

- Test restores regularly — an untested backup is a wish.
- `-j` parallel restore only with directory/custom format.
- Cloud managed PG: use vendor snapshots + PITR — still verify RPO/RTO.

---


## Interview Answers

## Question {#q-98}

What is pg_basebackup used for in HA bootstrap?

### Short Answer

Logical dumps for portability; physical for PITR. This directly answers: what is pg_basebackup used for in ha bootstrap?

### Detailed Explanation

Parallel pg_restore with directory/custom format. For **Reliability** depth, reason about failure modes and measurable signals before changing configuration.

### Internal Working

Canonical internals live on `/postgresql-cheatsheet/04-high-availability/backup-restore/` — cite xmin/xmax, WAL, or planner nodes as appropriate.

### Production Notes

Confirm with metrics and staged tests; document rollback for HA and DDL changes.

### Common Mistakes

Applying generic blog tuning without workload evidence; ignoring pooler and replica lag.

### Follow-up Questions

- What metric would disprove your hypothesis?
- Which handbook page is the canonical source?

---

## Question {#q-99}

When is pg_dump preferable to physical backup?

### Short Answer

Logical dumps for portability; physical for PITR. This directly answers: when is pg_dump preferable to physical backup?

### Detailed Explanation

Parallel pg_restore with directory/custom format. For **Reliability** depth, reason about failure modes and measurable signals before changing configuration.

### Internal Working

Canonical internals live on `/postgresql-cheatsheet/04-high-availability/backup-restore/` — cite xmin/xmax, WAL, or planner nodes as appropriate.

### Production Notes

Confirm with metrics and staged tests; document rollback for HA and DDL changes.

### Common Mistakes

Applying generic blog tuning without workload evidence; ignoring pooler and replica lag.

### Follow-up Questions

- What metric would disprove your hypothesis?
- Which handbook page is the canonical source?


## See Also

- [Previous: Failover](/postgresql-cheatsheet/04-high-availability/failover/)
- [Next: DR](/postgresql-cheatsheet/04-high-availability/disaster-recovery/)
- [PostgreSQL Handbook](/postgresql-cheatsheet/)
- [Database Handbook — PostgreSQL](/database-handbook/postgresql/)
