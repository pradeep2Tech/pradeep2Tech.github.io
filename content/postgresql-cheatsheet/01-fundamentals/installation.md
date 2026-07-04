---
title: "Installation"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "Install PostgreSQL — initdb, psql, first connection."
tags: ["postgresql-cheatsheet", "postgresql", "handbook", "interview"]
categories: ["PostgreSQL Handbook"]
shortTitle: "Install"
module: 1
moduleTitle: "Fundamentals"
sectionRef: "1.7"
weight: 107
interviewHandbook: true
aliases:
  - /postgresql-cheatsheet/installation/
---

## Quick Revision

**PostgreSQL** installs as a server (`postgres`) plus client tools (`psql`, `pg_dump`). Use packages or Docker for dev; production needs tuned `postgresql.conf` and persistent data directory.

---

## Core Concepts

| Platform | Install |
| :--- | :--- |
| **Debian/Ubuntu** | `apt install postgresql postgresql-contrib` |
| **RHEL/Fedora** | `dnf install postgresql-server postgresql-contrib` |
| **macOS** | `brew install postgresql@16` |
| **Docker** | Official `postgres` image — mount `/var/lib/postgresql/data` |
| **Windows** | EDB installer or `choco install postgresql` |

---

## Quick Reference

```bash
# Linux — initialize cluster (distro-specific)
sudo postgresql-setup --initdb    # RHEL
sudo pg_ctlcluster 16 main start  # Debian

# Connect
psql -U postgres -h localhost -p 5432

# Create role + database
createuser -P appuser
createdb -O appuser appdb
psql -U appuser -d appdb
```

---

## Snippets

```bash
# Docker (dev)
docker run -d --name pg \
  -e POSTGRES_PASSWORD=secret \
  -e POSTGRES_USER=app \
  -e POSTGRES_DB=appdb \
  -p 5432:5432 \
  -v pgdata:/var/lib/postgresql/data \
  postgres:16-alpine
```

---

## Common Gotchas

- Default port **5432**; change in `postgresql.conf` + firewall.
- `peer` auth on local sockets vs `scram-sha-256` for TCP — check `pg_hba.conf`.
- Extensions: `CREATE EXTENSION IF NOT EXISTS pg_stat_statements;`

---

## See Also

- [Previous: Windows](/postgresql-cheatsheet/01-fundamentals/window-functions/)
- [Next: Architecture](/postgresql-cheatsheet/02-core-postgresql/architecture/)
- [PostgreSQL Handbook](/postgresql-cheatsheet/)
- [Database Handbook — PostgreSQL](/database-handbook/postgresql/)
