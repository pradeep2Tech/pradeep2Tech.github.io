"""Build PostgreSQL Cheatsheet pages from data/postgresql_cheatsheet_modules.yaml."""
from __future__ import annotations

import re
import textwrap
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
CONTENT = ROOT / "content" / "postgresql-cheatsheet"
DATE = "2026-06-30T10:00:00+00:00"
SECTION = "postgresql-cheatsheet"

# slug -> (title, shortTitle, description)
TOPIC_META: dict[str, tuple[str, str, str]] = {
    "installation": (
        "Installation",
        "Install",
        "Install PostgreSQL on Linux, macOS, and Docker — initdb, psql, and first connection.",
    ),
    "sql-basics": (
        "SQL Basics",
        "SQL Basics",
        "SELECT, WHERE, ORDER BY, LIMIT, DISTINCT, and psql essentials.",
    ),
    "most-common-sql-commands": (
        "Most Common SQL Commands",
        "Common SQL",
        "Day-to-day PostgreSQL commands — CRUD, meta-queries, and session helpers.",
    ),
    "ddl": (
        "DDL",
        "DDL",
        "CREATE/ALTER/DROP — schemas, tables, constraints, and types.",
    ),
    "dml": (
        "DML",
        "DML",
        "INSERT, UPDATE, DELETE, UPSERT, and RETURNING patterns.",
    ),
    "joins": (
        "Joins",
        "Joins",
        "INNER, LEFT, RIGHT, FULL, CROSS, and LATERAL join cheat sheet.",
    ),
    "indexes": (
        "Indexes",
        "Indexes",
        "B-tree, GIN, GiST, BRIN, partial, and covering index patterns.",
    ),
    "explain": (
        "EXPLAIN",
        "EXPLAIN",
        "EXPLAIN, ANALYZE, BUFFERS — read plans, costs, and node types.",
    ),
    "performance-tuning": (
        "Performance Tuning",
        "Perf Tuning",
        "work_mem, shared_buffers, connection pooling, and query tuning knobs.",
    ),
    "transactions": (
        "Transactions",
        "Transactions",
        "BEGIN, COMMIT, ROLLBACK, SAVEPOINT, and ACID recap.",
    ),
    "isolation-levels": (
        "Isolation Levels",
        "Isolation",
        "READ COMMITTED, REPEATABLE READ, SERIALIZABLE — anomalies and defaults.",
    ),
    "mvcc": (
        "MVCC",
        "MVCC",
        "Tuple visibility, xmin/xmax, snapshots, and vacuum interaction.",
    ),
    "locks": (
        "Locks",
        "Locks",
        "Row/table/advisory locks, deadlocks, and pg_locks diagnostics.",
    ),
    "partitioning": (
        "Partitioning",
        "Partitioning",
        "Declarative RANGE, LIST, HASH partitioning and partition pruning.",
    ),
    "sharding": (
        "Sharding",
        "Sharding",
        "Citus, foreign data wrappers, and application-level sharding patterns.",
    ),
    "replication": (
        "Replication",
        "Replication",
        "Streaming replication, logical replication, slots, and failover basics.",
    ),
    "views": (
        "Views",
        "Views",
        "CREATE VIEW, updatable views, security_barrier, and dependencies.",
    ),
    "materialized-views": (
        "Materialized Views",
        "Mat Views",
        "REFRESH, CONCURRENTLY, indexes on mat views, and staleness trade-offs.",
    ),
    "ctes": (
        "CTEs",
        "CTEs",
        "WITH, recursive CTEs, MATERIALIZED hint, and readability vs optimization.",
    ),
    "window-functions": (
        "Window Functions",
        "Windows",
        "ROW_NUMBER, RANK, LAG/LEAD, PARTITION BY, and frame clauses.",
    ),
    "json": (
        "JSON & JSONB",
        "JSON",
        "json vs jsonb, operators, indexing with GIN, and path queries.",
    ),
    "functions": (
        "Functions",
        "Functions",
        "PL/pgSQL and SQL functions — parameters, volatility, and security.",
    ),
    "triggers": (
        "Triggers",
        "Triggers",
        "BEFORE/AFTER, ROW/STATEMENT, NEW/OLD, and WHEN clauses.",
    ),
    "stored-procedures": (
        "Stored Procedures",
        "Procedures",
        "CREATE PROCEDURE, CALL, transactions inside procedures (PG 11+).",
    ),
    "vacuum": (
        "VACUUM",
        "VACUUM",
        "VACUUM, ANALYZE, autovacuum, bloat, and freeze visibility.",
    ),
    "backup-restore": (
        "Backup & Restore",
        "Backup",
        "pg_dump, pg_restore, base backup, PITR, and logical vs physical.",
    ),
    "interview-questions": (
        "Interview Questions",
        "Interview",
        "PostgreSQL interview probes — MVCC, indexes, replication, and tuning.",
    ),
}

# slug -> (summary, concepts_table, quick_ref, snippets, gotchas)
TOPIC_BODIES: dict[str, tuple[str, str, str, str, str]] = {
    "installation": (
        "**PostgreSQL** installs as a server (`postgres`) plus client tools (`psql`, `pg_dump`). Use packages or Docker for dev; production needs tuned `postgresql.conf` and persistent data directory.",
        """| Platform | Install |
| :--- | :--- |
| **Debian/Ubuntu** | `apt install postgresql postgresql-contrib` |
| **RHEL/Fedora** | `dnf install postgresql-server postgresql-contrib` |
| **macOS** | `brew install postgresql@16` |
| **Docker** | Official `postgres` image — mount `/var/lib/postgresql/data` |
| **Windows** | EDB installer or `choco install postgresql` |""",
        """```bash
# Linux — initialize cluster (distro-specific)
sudo postgresql-setup --initdb    # RHEL
sudo pg_ctlcluster 16 main start  # Debian

# Connect
psql -U postgres -h localhost -p 5432

# Create role + database
createuser -P appuser
createdb -O appuser appdb
psql -U appuser -d appdb
```""",
        """```bash
# Docker (dev)
docker run -d --name pg \\
  -e POSTGRES_PASSWORD=secret \\
  -e POSTGRES_USER=app \\
  -e POSTGRES_DB=appdb \\
  -p 5432:5432 \\
  -v pgdata:/var/lib/postgresql/data \\
  postgres:16-alpine
```""",
        "- Default port **5432**; change in `postgresql.conf` + firewall.\n- `peer` auth on local sockets vs `scram-sha-256` for TCP — check `pg_hba.conf`.\n- Extensions: `CREATE EXTENSION IF NOT EXISTS pg_stat_statements;`",
    ),
    "sql-basics": (
        "PostgreSQL speaks standard SQL with rich types and operators. Master **SELECT** filtering, sorting, and limits before joins and aggregates.",
        """| Clause | Purpose |
| :--- | :--- |
| `SELECT` | Project columns or expressions |
| `FROM` | Source table(s) |
| `WHERE` | Filter rows before grouping |
| `GROUP BY` | Aggregate buckets |
| `HAVING` | Filter groups |
| `ORDER BY` | Sort result |
| `LIMIT` / `OFFSET` | Paginate (prefer keyset pagination at scale) |""",
        """```sql
SELECT id, email, created_at
FROM users
WHERE status = 'active'
  AND created_at >= '2026-01-01'
ORDER BY created_at DESC
LIMIT 50;

SELECT DISTINCT country FROM customers;
SELECT count(*) FROM orders WHERE total > 100;
```""",
        """```sql
-- psql meta
\\l          -- databases
\\dt         -- tables
\\d users    -- describe table
\\x          -- expanded display
\\timing on  -- query timing
```""",
        "- `NULL` comparisons need `IS NULL` / `IS NOT NULL`, not `= NULL`.\n- Double quotes = identifiers; single quotes = string literals.\n- `SELECT *` is fine in psql; avoid in application code.",
    ),
    "most-common-sql-commands": (
        "A single-page recap of commands you reach for daily — CRUD, catalog queries, and session management.",
        """| Task | Command |
| :--- | :--- |
| List tables | `\\dt` or `SELECT * FROM pg_tables WHERE schemaname = 'public';` |
| Table size | `pg_total_relation_size('tablename')` |
| Active queries | `pg_stat_activity` |
| Kill query | `SELECT pg_cancel_backend(pid);` or `pg_terminate_backend(pid)` |
| Current user/db | `SELECT current_user, current_database();` |""",
        """```sql
-- CRUD
INSERT INTO products (sku, name, price) VALUES ('A1', 'Widget', 9.99);
UPDATE products SET price = 10.99 WHERE sku = 'A1';
DELETE FROM products WHERE sku = 'A1';

-- Upsert (see DML page)
INSERT INTO products (sku, name, price) VALUES ('A1', 'Widget', 9.99)
ON CONFLICT (sku) DO UPDATE SET name = EXCLUDED.name, price = EXCLUDED.price;

-- Grants
GRANT SELECT ON ALL TABLES IN SCHEMA public TO readonly;
```""",
        """```sql
-- Find duplicate keys
SELECT email, count(*) FROM users GROUP BY email HAVING count(*) > 1;

-- Explain last query cost
EXPLAIN (ANALYZE, BUFFERS) SELECT * FROM orders WHERE user_id = 42;
```""",
        "- Use `RETURNING` on INSERT/UPDATE/DELETE to avoid a second round-trip.\n- `TRUNCATE` is DDL-fast but cannot be rolled back in some cases — locks table.\n- Prefer parameterized queries from apps — never string-concat SQL.",
    ),
    "ddl": (
        "**DDL** defines structure: schemas, tables, constraints, indexes, and types. Changes are transactional in PostgreSQL.",
        """| Statement | Use |
| :--- | :--- |
| `CREATE TABLE` | New relation with columns + constraints |
| `ALTER TABLE` | Add/drop column, constraint, rename |
| `CREATE INDEX` | Speed lookups (see Indexes) |
| `DROP` | Remove object — `CASCADE` drops dependents |
| `TRUNCATE` | Fast empty table — resets identity optionally |""",
        """```sql
CREATE SCHEMA IF NOT EXISTS billing;

CREATE TABLE billing.invoices (
  id          bigserial PRIMARY KEY,
  customer_id bigint NOT NULL REFERENCES customers(id),
  amount      numeric(12,2) NOT NULL CHECK (amount >= 0),
  status      text NOT NULL DEFAULT 'draft',
  issued_at   timestamptz NOT NULL DEFAULT now(),
  UNIQUE (customer_id, issued_at)
);

ALTER TABLE billing.invoices ADD COLUMN notes text;
ALTER TABLE billing.invoices RENAME COLUMN notes TO memo;
```""",
        """```sql
-- Common types
-- serial/bigserial, uuid, text, varchar(n), boolean, int, bigint,
-- numeric(p,s), real/double precision, date, time, timestamptz, jsonb

CREATE TYPE order_status AS ENUM ('pending', 'paid', 'shipped', 'cancelled');
```""",
        "- `ALTER ... ADD COLUMN ... DEFAULT` may rewrite table on older PG — plan maintenance window.\n- Use `IF NOT EXISTS` / `IF EXISTS` in migrations for idempotency.\n- `DEFERRABLE` constraints allow batch loads within a transaction.",
    ),
    "dml": (
        "**DML** mutates rows: INSERT, UPDATE, DELETE. PostgreSQL supports powerful `RETURNING` and `ON CONFLICT` upserts.",
        """| Statement | Notes |
| :--- | :--- |
| `INSERT` | Single/multi-row; `DEFAULT` for omitted columns |
| `UPDATE` | Always add `WHERE` unless intentional full-table update |
| `DELETE` | Same — missing `WHERE` deletes all rows |
| `ON CONFLICT` | Upsert — requires unique index/constraint |
| `RETURNING` | Return inserted/updated rows to client |""",
        """```sql
INSERT INTO events (user_id, kind, payload)
VALUES (1, 'login', '{"ip":"10.0.0.1"}'::jsonb)
RETURNING id, created_at;

UPDATE accounts SET balance = balance - 100
WHERE id = 5 AND balance >= 100
RETURNING balance;

DELETE FROM sessions WHERE expires_at < now() RETURNING id;
```""",
        """```sql
-- Upsert
INSERT INTO inventory (sku, qty)
VALUES ('X', 10)
ON CONFLICT (sku) DO UPDATE
  SET qty = inventory.qty + EXCLUDED.qty;

-- Bulk insert from SELECT
INSERT INTO archive_orders SELECT * FROM orders WHERE created_at < '2024-01-01';
```""",
        "- `ON CONFLICT DO NOTHING` silently skips — log or count if you need visibility.\n- Large updates: batch by primary key range to reduce lock duration.\n- `COPY` beats INSERT for bulk loads — see Backup page for `COPY` format.",
    ),
    "joins": (
        "Joins combine rows from multiple relations. PostgreSQL optimizes join order; explicit join syntax beats comma-FROM for readability.",
        """| Join | Keeps |
| :--- | :--- |
| `INNER JOIN` | Matching rows only |
| `LEFT JOIN` | All left + matches (NULLs on right miss) |
| `RIGHT JOIN` | Mirror of LEFT |
| `FULL OUTER` | All from both sides |
| `CROSS JOIN` | Cartesian product |
| `LATERAL` | Subquery per left row — great for top-N per group |""",
        """```sql
SELECT o.id, o.total, c.email
FROM orders o
INNER JOIN customers c ON c.id = o.customer_id
WHERE o.status = 'paid';

SELECT c.name, o.id AS order_id
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id AND o.created_at > now() - interval '30 days';
```""",
        """```sql
-- Top 3 orders per customer (LATERAL)
SELECT c.id, recent.*
FROM customers c
CROSS JOIN LATERAL (
  SELECT id, total FROM orders
  WHERE customer_id = c.id
  ORDER BY created_at DESC LIMIT 3
) recent;
```""",
        "- `LEFT JOIN ... WHERE right.col = x` filters NULLs — often becomes INNER join semantics.\n- Join on indexed columns — avoid functions on join keys.\n- `USING (id)` shorthand when column names match.",
    ),
    "indexes": (
        "Indexes accelerate reads at write/storage cost. Default **B-tree** suits most equality/range queries; specialized indexes for JSON, text search, and geospatial.",
        """| Type | Best for |
| :--- | :--- |
| **B-tree** (default) | `=`, `<`, `>`, `BETWEEN`, `ORDER BY` |
| **Hash** | Equality only — rarely needed vs B-tree |
| **GIN** | jsonb, arrays, full-text |
| **GiST** | Geometric, range types, full-text |
| **BRIN** | Very large, naturally ordered tables |
| **Partial** | `WHERE active = true` — smaller, targeted |""",
        """```sql
CREATE INDEX idx_orders_user_created ON orders (user_id, created_at DESC);
CREATE INDEX idx_users_email_lower ON users (lower(email));
CREATE UNIQUE INDEX idx_products_sku ON products (sku);

-- Covering index (INCLUDE — PG 11+)
CREATE INDEX idx_orders_cover ON orders (user_id) INCLUDE (total, status);
```""",
        """```sql
-- JSONB GIN
CREATE INDEX idx_events_payload ON events USING gin (payload jsonb_path_ops);

-- Partial index
CREATE INDEX idx_active_users ON users (last_login) WHERE status = 'active';
```""",
        "- Unused indexes waste write amplification — check `pg_stat_user_indexes`.\n- `REINDEX CONCURRENTLY` rebuilds without blocking reads (PG 12+).\n- Too many indexes on hot write tables hurts INSERT/UPDATE throughput.",
    ),
    "explain": (
        "`EXPLAIN` shows the planner's chosen path. Add **ANALYZE** to execute and show actual row counts and timing; **BUFFERS** reveals cache hits.",
        """| Node | Meaning |
| :--- | :--- |
| `Seq Scan` | Full table read — OK for small tables |
| `Index Scan` | Index lookup + heap fetch |
| `Index Only Scan` | Satisfied from index — ideal |
| `Bitmap Heap Scan` | Index bitmap then heap visit |
| `Nested Loop` | Good for small outer sets |
| `Hash Join` | Build hash on inner — equality joins |
| `Merge Join` | Pre-sorted inputs |""",
        """```sql
EXPLAIN SELECT * FROM orders WHERE user_id = 42;

EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT)
SELECT * FROM orders WHERE user_id = 42;

EXPLAIN (ANALYZE, BUFFERS, VERBOSE, SETTINGS)
SELECT o.* FROM orders o JOIN users u ON u.id = o.user_id WHERE u.email = 'a@b.com';
```""",
        """```sql
-- Compare estimated vs actual rows — big gaps mean stale stats
-- Run: ANALYZE orders;

-- Force plan for testing only (session-local)
SET enable_seqscan = off;
```""",
        "- High **actual** vs **estimated** rows → run `ANALYZE` or increase `default_statistics_target`.\n- `EXPLAIN` without `ANALYZE` is cheap but can mislead on row estimates.\n- Use `pg_stat_statements` for production workload — not ad-hoc EXPLAIN everywhere.",
    ),
    "performance-tuning": (
        "Tune at three layers: **query/SQL**, **indexes**, and **server config**. Measure with `pg_stat_statements`, `EXPLAIN (ANALYZE)`, and OS metrics before cranking knobs.",
        """| Parameter | Starting guidance |
| :--- | :--- |
| `shared_buffers` | ~25% RAM (cap ~8GB on large boxes — test) |
| `effective_cache_size` | ~50–75% RAM — planner hint |
| `work_mem` | Per sort/hash operation — don't set globally huge |
| `maintenance_work_mem` | VACUUM, CREATE INDEX builds |
| `max_connections` | Prefer pooler (PgBouncer) over thousands |""",
        """```sql
-- Session knobs
SET work_mem = '64MB';  -- careful — per operation per query
SET random_page_cost = 1.1;  -- SSD/NVMe

-- Find slow queries (extension)
SELECT query, calls, mean_exec_time, total_exec_time
FROM pg_stat_statements
ORDER BY total_exec_time DESC LIMIT 20;
```""",
        """```ini
# postgresql.conf snippets
shared_buffers = 4GB
effective_cache_size = 12GB
work_mem = 32MB
maintenance_work_mem = 1GB
wal_compression = on
```""",
        "- Raising `max_connections` without a pooler increases memory and context switching.\n- Connection pooling (transaction mode) is almost always required in microservices.\n- Partition pruning and partial indexes often beat raw parameter tuning.",
    ),
    "transactions": (
        "PostgreSQL is fully **ACID**. Default autocommit wraps each statement; explicit transactions group work atomically.",
        """| Command | Effect |
| :--- | :--- |
| `BEGIN` / `START TRANSACTION` | Open transaction |
| `COMMIT` | Persist changes |
| `ROLLBACK` | Discard since BEGIN |
| `SAVEPOINT sp` | Nested rollback point |
| `ROLLBACK TO sp` | Undo to savepoint |""",
        """```sql
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;

BEGIN;
SAVEPOINT before_transfer;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
-- oops
ROLLBACK TO before_transfer;
COMMIT;
```""",
        """```sql
-- Serializable retry pattern (app layer)
BEGIN ISOLATION LEVEL SERIALIZABLE;
-- business logic
COMMIT;  -- on 40001 serialization_failure, retry
```""",
        "- DDL inside a transaction is allowed — `BEGIN; CREATE TABLE ...; ROLLBACK;` works.\n- Long transactions block vacuum and bloat tables.\n- Use `SET TRANSACTION READ ONLY` for reporting replicas routing.",
    ),
    "isolation-levels": (
        "Isolation controls what concurrent transactions see. PostgreSQL default is **READ COMMITTED**; **REPEATABLE READ** and **SERIALIZABLE** use snapshot isolation.",
        """| Level | Dirty read | Non-repeatable read | Phantom |
| :--- | :---: | :---: | :---: |
| READ UNCOMMITTED | — | — | — (acts as READ COMMITTED) |
| **READ COMMITTED** (default) | No | Yes | Yes |
| **REPEATABLE READ** | No | No | No* |
| **SERIALIZABLE** | No | No | No |

*PostgreSQL RR prevents phantoms via snapshot — stricter than SQL standard minimum.""",
        """```sql
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
BEGIN ISOLATION LEVEL SERIALIZABLE;

SHOW transaction_isolation;
```""",
        """```sql
-- Serializable conflict
BEGIN ISOLATION LEVEL SERIALIZABLE;
SELECT sum(balance) FROM accounts WHERE user_id = 1;
-- concurrent writer commits conflicting update
COMMIT;  -- may raise SQLSTATE 40001
```""",
        "- READ COMMITTED sees **new** rows committed after each statement in the txn.\n- REPEATABLE READ holds one snapshot for the whole transaction.\n- SERIALIZABLE adds predicate locking — retry on `serialization_failure`.",
    ),
    "mvcc": (
        "**Multi-Version Concurrency Control** keeps old row versions for in-flight transactions. Readers don't block writers; **VACUUM** reclaims dead tuples.",
        """| Concept | Role |
| :--- | :--- |
| `xmin` | Inserting transaction ID |
| `xmax` | Deleting/updating transaction ID |
| **Snapshot** | Visible tuple set for a transaction |
| **Dead tuple** | Old version no longer visible to any snapshot |
| **VACUUM** | Marks space reusable; **FREEZE** prevents wraparound |""",
        """```sql
-- Tuple metadata (extension)
CREATE EXTENSION IF NOT EXISTS pageinspect;
-- heap_page_items, tuple headers — advanced debugging

SELECT relname, n_live_tup, n_dead_tup, last_vacuum, last_autovacuum
FROM pg_stat_user_tables
ORDER BY n_dead_tup DESC;
```""",
        """```mermaid
flowchart LR
  write[UPDATE row] --> new[New tuple version]
  write --> old[Old tuple dead]
  old --> vacuum[VACUUM reclaims]
  read[SELECT snapshot] --> visible[Sees live version only]
```""",
        "- High churn tables need healthy autovacuum — watch `n_dead_tup`.\n- Long transactions prevent vacuum from reclaiming space → bloat.\n- `SELECT ... FOR UPDATE` locks current row version.",
    ),
    "locks": (
        "Locks serialize conflicting access. Row-level locks are default for DML; DDL takes stronger locks. **Advisory locks** coordinate app-level mutexes.",
        """| Lock | Typical cause |
| :--- | :--- |
| `RowExclusive` | INSERT/UPDATE/DELETE |
| `ShareRowExclusive` | CREATE TRIGGER, some ALTER |
| `AccessExclusive` | DROP, TRUNCATE, VACUUM FULL — blocks all |
| `Advisory` | `pg_advisory_lock(key)` app mutex |""",
        """```sql
SELECT pid, wait_event_type, wait_event, query
FROM pg_stat_activity
WHERE state != 'idle';

SELECT l.pid, l.mode, l.granted, a.query
FROM pg_locks l
JOIN pg_stat_activity a ON a.pid = l.pid
WHERE NOT l.granted;

SELECT pg_cancel_backend(pid);      -- polite
SELECT pg_terminate_backend(pid);   -- force
```""",
        """```sql
-- Advisory lock (session-level)
SELECT pg_advisory_lock(42);
-- critical section
SELECT pg_advisory_unlock(42);

-- Row lock
SELECT * FROM accounts WHERE id = 1 FOR UPDATE;
```""",
        "- Deadlock → PostgreSQL aborts one transaction — app should retry.\n- `LOCK TABLE` in migrations — schedule off-peak.\n- `NOWAIT` / `SKIP LOCKED` for queue workers.",
    ),
    "partitioning": (
        "**Declarative partitioning** splits one logical table into physical children. Pruning skips irrelevant partitions at plan time.",
        """| Method | Key |
| :--- | :--- |
| **RANGE** | Dates, numeric ranges |
| **LIST** | Discrete values (region, status) |
| **HASH** | Even spread when no natural key |""",
        """```sql
CREATE TABLE measurements (
  id bigserial,
  device_id int NOT NULL,
  recorded_at timestamptz NOT NULL,
  value double precision
) PARTITION BY RANGE (recorded_at);

CREATE TABLE measurements_2026_01 PARTITION OF measurements
  FOR VALUES FROM ('2026-01-01') TO ('2026-02-01');

CREATE INDEX ON measurements (device_id, recorded_at);
```""",
        """```sql
-- Attach existing table as partition
CREATE TABLE measurements_old (LIKE measurements INCLUDING ALL);
ALTER TABLE measurements ATTACH PARTITION measurements_old
  FOR VALUES FROM ('2025-01-01') TO ('2026-01-01');
```""",
        "- Partition key must appear in PK/unique constraints (include partition key).\n- Create future partitions before data arrives — or use `DEFAULT` partition.\n- Global uniqueness across partitions requires careful constraint design.",
    ),
    "sharding": (
        "PostgreSQL single-node scales vertically; **sharding** spreads data across nodes. Options: **Citus**, **FDW**, or app-level routing.",
        """| Approach | Trade-off |
| :--- | :--- |
| **Citus** | Native distributed PG — colocation, rebalance |
| **Foreign Data Wrapper** | Federated queries — not true shard autonomy |
| **App routing** | Full control — you own cross-shard queries |
| **Read replicas** | Scale reads, not writes — not sharding |""",
        """```sql
-- Citus (extension) sketch
SELECT create_distributed_table('events', 'tenant_id');

-- postgres_fdw
CREATE EXTENSION postgres_fdw;
CREATE SERVER shard1 FOREIGN DATA WRAPPER postgres_fdw
  OPTIONS (host 'shard1.internal', dbname 'app');
```""",
        """```sql
-- App-level: tenant_id in every query + connection per shard
-- Avoid cross-shard JOINs in hot paths — aggregate in app or OLAP layer
```""",
        "- Choose shard key early — resharding is painful.\n- Co-locate related tables on same shard (Citus `colocate_with`).\n- Global sequences and FK across shards need application patterns.",
    ),
    "replication": (
        "**Streaming replication** ships WAL to standbys for HA. **Logical replication** publishes table changes for migrations and fan-out.",
        """| Mode | Use |
| :--- | :--- |
| Physical / streaming | Hot standby, failover |
| Logical | Selective tables, upgrades, CDC |
| Replication slot | Prevents WAL removal until consumed |""",
        """```sql
-- On primary
CREATE ROLE replicator WITH REPLICATION LOGIN PASSWORD 'secret';

-- pg_hba.conf: host replication replicator 10.0.0.0/24 scram-sha-256

-- Logical publication
CREATE PUBLICATION app_pub FOR TABLE orders, customers;
```""",
        """```bash
# Standby base backup
pg_basebackup -h primary -D /var/lib/postgresql/data -U replicator -Fp -Xs -P -R
```""",
        "- Async replication → potential data loss on failover — know RPO.\n- Replication slots on idle subscribers can fill disk with WAL.\n- `pg_switch_wal()` before promotion in orchestrated failover.",
    ),
    "views": (
        "Views store a query definition — no data duplication. **Updatable views** need simple single-table rules or `INSTEAD OF` triggers.",
        """| Feature | Notes |
| :--- | :--- |
| `CREATE VIEW` | Named saved query |
| `CREATE OR REPLACE VIEW` | Swap definition |
| `security_barrier` | Row-level security helper |
| Updatable | Simple views — one base table, no aggregates |""",
        """```sql
CREATE VIEW active_customers AS
SELECT id, email, name
FROM customers
WHERE status = 'active';

CREATE OR REPLACE VIEW order_summary AS
SELECT customer_id, count(*) AS order_count, sum(total) AS revenue
FROM orders
GROUP BY customer_id;
```""",
        """```sql
-- Check if updatable
SELECT table_name, is_insertable_into
FROM information_schema.views
WHERE table_schema = 'public';
```""",
        "- Complex views with joins/aggregates are read-only unless triggers added.\n- `WITH CHECK OPTION` enforces inserts/updates match view predicate.\n- Views hide columns — not a security boundary without RLS/grants.",
    ),
    "materialized-views": (
        "Materialized views **cache** query results on disk. Refresh synchronously or **CONCURRENTLY** (requires unique index).",
        """| Command | Blocks reads? |
| :--- | :--- |
| `REFRESH MATERIALIZED VIEW` | Yes — exclusive lock |
| `REFRESH ... CONCURRENTLY` | No — needs UNIQUE index |""",
        """```sql
CREATE MATERIALIZED VIEW daily_revenue AS
SELECT date_trunc('day', created_at) AS day, sum(total) AS revenue
FROM orders
GROUP BY 1;

CREATE UNIQUE INDEX ON daily_revenue (day);

REFRESH MATERIALIZED VIEW CONCURRENTLY daily_revenue;
```""",
        """```sql
-- Staleness acceptable? Schedule via pg_cron or external job
-- For real-time dashboards prefer regular view + proper indexes
```""",
        "- CONCURRENTLY refresh can fail if unique constraint violated mid-refresh.\n- Mat views don't auto-update — plan refresh cadence vs freshness SLA.\n- Large refreshes: consider incremental patterns or summary tables.",
    ),
    "ctes": (
        "**Common Table Expressions** (`WITH`) improve readability and support recursion. PostgreSQL 12+ inlines non-recursive CTEs by default — use `MATERIALIZED` to force optimization barrier when needed.",
        """| Form | Use |
| :--- | :--- |
| Simple CTE | Named subquery upfront |
| Recursive | Graphs, hierarchies, bill of materials |
| `MATERIALIZED` | Force materialization (PG 12+) |
| `NOT MATERIALIZED` | Hint inline (PG 12+) |""",
        """```sql
WITH regional_sales AS (
  SELECT region, sum(amount) AS total FROM sales GROUP BY region
),
top_regions AS (
  SELECT region FROM regional_sales WHERE total > 1000000
)
SELECT * FROM customers WHERE region IN (SELECT region FROM top_regions);
```""",
        """```sql
-- Recursive org chart
WITH RECURSIVE org AS (
  SELECT id, name, manager_id, 1 AS depth
  FROM employees WHERE manager_id IS NULL
  UNION ALL
  SELECT e.id, e.name, e.manager_id, org.depth + 1
  FROM employees e JOIN org ON e.manager_id = org.id
)
SELECT * FROM org ORDER BY depth, name;
```""",
        "- Recursive CTE needs `UNION` (not `UNION ALL`) for cycle safety unless you track visited.\n- Overusing CTEs where a subquery suffices can confuse planner — verify with EXPLAIN.\n- `WITH ... INSERT` enables writable CTE pipelines.",
    ),
    "window-functions": (
        "Window functions compute over a **partition** without collapsing rows like `GROUP BY`. Essential for rankings, running totals, and LAG/LEAD analytics.",
        """| Function | Purpose |
| :--- | :--- |
| `ROW_NUMBER()` | Unique rank 1..n |
| `RANK()` / `DENSE_RANK()` | Ties handled differently |
| `LAG` / `LEAD` | Previous/next row in partition |
| `SUM() OVER` | Running total |
| `NTILE(n)` | Bucket into n groups |""",
        """```sql
SELECT
  employee_id,
  department,
  salary,
  ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS rn,
  AVG(salary) OVER (PARTITION BY department) AS dept_avg
FROM employees;
```""",
        """```sql
-- Running total
SELECT order_date, amount,
  SUM(amount) OVER (ORDER BY order_date
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total
FROM daily_sales;

-- Dedupe keep latest
SELECT * FROM (
  SELECT *, ROW_NUMBER() OVER (PARTITION BY email ORDER BY updated_at DESC) rn
  FROM users
) t WHERE rn = 1;
```""",
        "- Frame clause defaults differ: `RANGE` vs `ROWS` — off-by-one bugs are common.\n- Window functions run after `WHERE` but before final `ORDER BY` in SELECT.\n- Index on `(partition_cols, order_cols)` helps only if planner uses sort optimization.",
    ),
    "json": (
        "PostgreSQL offers **json** (text storage) and **jsonb** (binary, indexable). Prefer **jsonb** for querying; **json** preserves exact formatting.",
        """| Operator | Meaning |
| :--- | :--- |
| `->` | Get JSON object field (as json) |
| `->>` | Get field as text |
| `#>` | Path array |
| `@>` | Contains |
| `?` | Key exists |
| `jsonb_set` | Update nested value |""",
        """```sql
SELECT payload->>'kind' AS kind,
       payload->'meta'->>'ip' AS ip
FROM events
WHERE payload @> '{"kind":"login"}';

UPDATE settings
SET body = jsonb_set(body, '{theme}', '"dark"')
WHERE user_id = 1;
```""",
        """```sql
CREATE TABLE events (
  id bigserial PRIMARY KEY,
  payload jsonb NOT NULL DEFAULT '{}'
);
CREATE INDEX idx_events_kind ON events ((payload->>'kind'));
CREATE INDEX idx_events_gin ON events USING gin (payload jsonb_path_ops);
```""",
        "- `jsonb` deduplicates keys and does not preserve key order.\n- Cast with `::jsonb` — invalid JSON throws error.\n- For heavy JSON analytics consider generated columns + B-tree index.",
    ),
    "functions": (
        "User-defined functions encapsulate logic in the database. Mark **volatility** correctly — wrong labels break indexes and optimization.",
        """| Volatility | Meaning |
| :--- | :--- |
| `IMMUTABLE` | Same in/out always — safe in indexes |
| `STABLE` | Same within one scan/statement |
| `VOLATILE` (default) | Can change anytime — side effects OK |""",
        """```sql
CREATE OR REPLACE FUNCTION full_name(first text, last text)
RETURNS text
LANGUAGE sql
IMMUTABLE
AS $$ SELECT first || ' ' || last $$;

SELECT full_name(first_name, last_name) FROM users;
```""",
        """```sql
CREATE OR REPLACE FUNCTION apply_discount(price numeric, pct numeric)
RETURNS numeric
LANGUAGE plpgsql
STABLE
AS $$
BEGIN
  IF pct < 0 OR pct > 100 THEN
    RAISE EXCEPTION 'invalid pct %', pct;
  END IF;
  RETURN round(price * (1 - pct/100), 2);
END;
$$;
```""",
        "- `SECURITY DEFINER` runs as owner — tighten `search_path` to prevent hijacking.\n- Prefer SQL functions when possible — inlinable.\n- Heavy logic in DB vs app — team skill and deploy cadence matter.",
    ),
    "triggers": (
        "Triggers run functions automatically on DML events. Use for audit, denormalization, and enforcement — avoid hiding business logic that belongs in services.",
        """| Timing | Level |
| :--- | :--- |
| `BEFORE` / `AFTER` | `ROW` or `STATEMENT` |
| `INSERT` / `UPDATE` / `DELETE` | Combine in one trigger or split |
| `WHEN (condition)` | Filter fired rows |""",
        """```sql
CREATE OR REPLACE FUNCTION set_updated_at()
RETURNS trigger LANGUAGE plpgsql AS $$
BEGIN
  NEW.updated_at := now();
  RETURN NEW;
END;
$$;

CREATE TRIGGER trg_users_updated
BEFORE UPDATE ON users
FOR EACH ROW EXECUTE FUNCTION set_updated_at();
```""",
        """```sql
-- Audit trigger sketch
CREATE TABLE users_audit (LIKE users);
CREATE TRIGGER trg_users_audit
AFTER UPDATE ON users
FOR EACH ROW EXECUTE FUNCTION audit_row();
```""",
        "- `BEFORE` triggers can modify `NEW`; `AFTER` cannot.\n- Statement-level triggers see no `NEW`/`OLD` row variables.\n- Triggers add latency and complicate bulk loads — disable for migrations if needed.",
    ),
    "stored-procedures": (
        "PostgreSQL **procedures** (PG 11+) support transactions inside the routine via `COMMIT`/`ROLLBACK` — unlike functions.",
        """| Object | Returns | Transactions inside |
| :--- | :--- | :--- |
| **Function** | Value(s) | No — single txn |
| **Procedure** | Optional via OUT | Yes — `CALL` |""",
        """```sql
CREATE OR REPLACE PROCEDURE archive_old_orders(cutoff date)
LANGUAGE plpgsql
AS $$
BEGIN
  INSERT INTO orders_archive SELECT * FROM orders WHERE created_at < cutoff;
  DELETE FROM orders WHERE created_at < cutoff;
  COMMIT;
END;
$$;

CALL archive_old_orders('2024-01-01');
```""",
        """```sql
-- Function returns set
CREATE FUNCTION active_users()
RETURNS SETOF users
LANGUAGE sql STABLE
AS $$ SELECT * FROM users WHERE status = 'active'; $$;
```""",
        "- Procedures called with `CALL`; functions in expressions.\n- Prefer idempotent migration scripts over procedural DDL in prod.\n- Test error paths — unhandled exceptions abort calling transaction.",
    ),
    "vacuum": (
        "**VACUUM** reclaims dead tuple space and updates visibility maps. **ANALYZE** refreshes planner statistics. **Autovacuum** runs both automatically.",
        """| Command | Purpose |
| :--- | :--- |
| `VACUUM` | Reclaim space (often reusable in-place) |
| `VACUUM ANALYZE` | Vacuum + stats |
| `VACUUM FULL` | Rewrites table — exclusive lock — last resort |
| Autovacuum | Background — tune `autovacuum_vacuum_scale_factor` |""",
        """```sql
VACUUM (VERBOSE, ANALYZE) orders;

SELECT schemaname, relname, n_dead_tup, last_autovacuum, autovacuum_count
FROM pg_stat_user_tables
ORDER BY n_dead_tup DESC;
```""",
        """```sql
-- Bloat estimate (simplified — use pgstattuple extension for detail)
SELECT relname, pg_size_pretty(pg_total_relation_size(oid))
FROM pg_class WHERE relkind = 'r' ORDER BY pg_total_relation_size(oid) DESC;
```""",
        "- `VACUUM FULL` blocks writes — use `pg_repack` extension for online reclaim when needed.\n- Freeze protects against transaction ID wraparound — monitor `age(datfrozenxid)`.\n- Aggressive autovacuum on append-mostly tables may be wasteful — tune per-table.",
    ),
    "backup-restore": (
        "Choose **logical** (`pg_dump`) for portability and selective restore; **physical** (base backup + WAL) for PITR and large DBs.",
        """| Method | Granularity | PITR |
| :--- | :--- | :--- |
| `pg_dump` / `pg_restore` | DB/schema/table | No |
| `pg_dumpall` | Cluster globals + DBs | No |
| Base backup + WAL archive | Whole cluster | Yes |
| `COPY` | Table CSV/binary | No |""",
        """```bash
pg_dump -Fc -f app.dump appdb
pg_restore -d appdb_new -j 4 app.dump

pg_dump -t orders appdb > orders.sql
```""",
        """```bash
# Physical backup (simplified)
pg_basebackup -D /backup/base -Ft -z -P
# archive_command in postgresql.conf ships WAL segments
```""",
        "- Test restores regularly — an untested backup is a wish.\n- `-j` parallel restore only with directory/custom format.\n- Cloud managed PG: use vendor snapshots + PITR — still verify RPO/RTO.",
    ),
    "interview-questions": (
        "Common PostgreSQL interview themes: **MVCC**, **indexes**, **isolation**, **replication**, **VACUUM**, and practical SQL tuning.",
        """| Topic | Probe |
| :--- | :--- |
| MVCC | Why UPDATE creates a new row version |
| Indexes | When GIN beats B-tree |
| Isolation | Difference READ COMMITTED vs REPEATABLE READ |
| Locks | `FOR UPDATE` vs `FOR SHARE` |
| Replication | Streaming vs logical — use cases |
| Performance | How you'd debug a slow query |""",
        """```sql
-- "Find missing index" pattern
EXPLAIN (ANALYZE, BUFFERS) SELECT ...;
-- Seq Scan on huge table + high filter selectivity → candidate for index
```""",
        """{{< interview-answer question="Why does PostgreSQL need VACUUM?" >}}
Updates and deletes leave **dead tuples**. MVCC keeps old versions visible to open transactions. VACUUM marks dead space reusable and prevents transaction ID wraparound. Without it, tables bloat and eventually the cluster risks shutdown for wraparound protection.
{{< /interview-answer >}}

{{< interview-answer question="Explain partial vs covering index." >}}
A **partial** index indexes a subset of rows (`WHERE active`) — smaller and faster for targeted queries. A **covering** index includes extra columns via `INCLUDE` so an **Index Only Scan** can satisfy the query without heap visits, reducing I/O.
{{< /interview-answer >}}

{{< interview-answer question="How does PostgreSQL implement REPEATABLE READ?" >}}
The transaction takes a **snapshot** at first statement (or transaction start depending on version/config). All reads see the same snapshot; concurrent commits by others are invisible for reads. Writes can still conflict — serialization failures possible on conflicting updates.
{{< /interview-answer >}}""",
        "- Tie answers to production: connection pooling, `pg_stat_statements`, replication lag.\n- Mention trade-offs, not buzzwords — interviewers probe depth.\n- Cross-link handbook pages for MVCC, indexes, and EXPLAIN.",
    ),
}


def flatten_topics(modules: list[dict]) -> list[str]:
    ordered: list[str] = []
    for mod in modules:
        ordered.extend(mod["topics"])
    return ordered


def write_order_yaml(topics: list[str], path: Path) -> None:
    path.write_text(
        "# Flat topic order — derived from postgresql_cheatsheet_modules.yaml.\n"
        "topics:\n"
        + "".join(f"  - {t}\n" for t in topics),
        encoding="utf-8",
    )


def iter_module_topics(modules: list[dict]):
    for mod in modules:
        mod_id = mod["id"]
        mod_title = mod["focus"]
        for idx, slug in enumerate(mod["topics"], start=1):
            yield mod_id, mod_title, slug, idx


def see_also_links(slug: str, ordered: list[str]) -> str:
    links: list[str] = []
    idx = ordered.index(slug)
    if idx > 0:
        prev = ordered[idx - 1]
        links.append(f"- [Previous: {TOPIC_META[prev][1]}](/{SECTION}/{prev}/)")
    if idx < len(ordered) - 1:
        nxt = ordered[idx + 1]
        links.append(f"- [Next: {TOPIC_META[nxt][1]}](/{SECTION}/{nxt}/)")
    links.append(f"- [PostgreSQL Cheatsheet Index](/{SECTION}/)")
    links.append("- [Database Handbook — PostgreSQL](/database-handbook/postgresql/)")
    return "\n".join(links)


def front_matter(slug: str, mod_id: int, mod_title: str, topic_idx: int) -> str:
    title, short, desc = TOPIC_META[slug]
    return f"""---
title: "{title}"
date: {DATE}
draft: false
description: "{desc}"
tags: ["postgresql-cheatsheet", "postgresql", "cheatsheet", "handbook"]
categories: ["PostgreSQL Cheatsheet"]
shortTitle: "{short}"
module: {mod_id}
moduleTitle: "{mod_title}"
sectionRef: "{mod_id}.{topic_idx}"
ShowToc: true
---

"""


def page_body(slug: str, see_also: str) -> str:
    summary, concepts, quick_ref, snippets, gotchas = TOPIC_BODIES[slug]
    parts = [
        "## Executive Summary",
        "",
        summary,
        "",
        "---",
        "",
        "## Core Concepts",
        "",
        concepts.strip(),
        "",
        "---",
        "",
        "## Quick Reference",
        "",
        quick_ref.strip(),
    ]
    if snippets.strip():
        parts.extend(["", "---", "", "## Snippets", "", snippets.strip()])
    parts.extend(
        [
            "",
            "---",
            "",
            "## Common Gotchas",
            "",
            gotchas.strip(),
            "",
            "---",
            "",
            "## Related Topics",
            "",
            see_also.strip(),
            "",
        ]
    )
    return "\n".join(parts)


def normalize(body: str) -> str:
    body = textwrap.dedent(body)
    body = re.sub(r"\n {8}", "\n", body)
    return body.strip() + "\n"


def main() -> None:
    modules_path = DATA / "postgresql_cheatsheet_modules.yaml"
    with open(modules_path, encoding="utf-8") as f:
        modules = yaml.safe_load(f)["modules"]

    ordered = flatten_topics(modules)
    write_order_yaml(ordered, DATA / "postgresql_cheatsheet_order.yaml")

    missing_meta = [s for s in ordered if s not in TOPIC_META]
    if missing_meta:
        raise SystemExit(f"Missing TOPIC_META for: {missing_meta}")

    missing_bodies = [s for s in ordered if s not in TOPIC_BODIES]
    if missing_bodies:
        raise SystemExit(f"Missing TOPIC_BODIES for: {missing_bodies}")

    CONTENT.mkdir(parents=True, exist_ok=True)
    written = 0
    for mod_id, mod_title, slug, topic_idx in iter_module_topics(modules):
        see_also = see_also_links(slug, ordered)
        body = normalize(page_body(slug, see_also))
        path = CONTENT / f"{slug}.md"
        path.write_text(front_matter(slug, mod_id, mod_title, topic_idx) + body, encoding="utf-8")
        written += 1
        print(f"Wrote {path.relative_to(ROOT)}")

    keep = {"_index.md"} | {f"{s}.md" for s in ordered}
    deleted = 0
    for path in CONTENT.glob("*.md"):
        if path.name not in keep:
            path.unlink()
            deleted += 1
            print(f"Deleted {path.relative_to(ROOT)}")

    print(f"\nSummary: {written} pages written, {deleted} deleted, {len(ordered)} topics in order.")


if __name__ == "__main__":
    main()
