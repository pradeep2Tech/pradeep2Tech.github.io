---
title: "Backup & Restore"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "pg_dump, pg_restore, base backup, PITR, and logical vs physical."
tags: ["postgresql-cheatsheet", "postgresql", "cheatsheet", "handbook"]
categories: ["PostgreSQL Cheatsheet"]
shortTitle: "Backup"
module: 8
moduleTitle: "Operations & Maintenance"
sectionRef: "8.2"
ShowToc: true
---

## Executive Summary

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
# archive_command in postgresql.conf ships WAL segments
```

---

## Common Gotchas

- Test restores regularly — an untested backup is a wish.
- `-j` parallel restore only with directory/custom format.
- Cloud managed PG: use vendor snapshots + PITR — still verify RPO/RTO.

---

## Related Topics

- [Previous: VACUUM](/postgresql-cheatsheet/vacuum/)
- [Next: Interview](/postgresql-cheatsheet/interview-questions/)
- [PostgreSQL Cheatsheet Index](/postgresql-cheatsheet/)
- [Database Handbook — PostgreSQL](/database-handbook/postgresql/)
