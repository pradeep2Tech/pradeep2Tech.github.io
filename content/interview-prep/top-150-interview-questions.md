---
title: "Top 150 Interview Questions"
date: 2026-07-03T10:00:00+00:00
draft: false
description: "Interview-first knowledge base — 150 senior-level questions across Git, Go, Kafka, Kubernetes, MongoDB, PostgreSQL, Python, and cross-topic architecture."
tags: ["interview-prep", "interview", "architecture", "senior-engineer"]
categories: ["Interview Preparation"]
shortTitle: "Top 150"
ShowToc: true
interviewHandbook: true
---

Curated questions for **6+ year** engineers, senior engineers, tech leads, and architects. Questions only — no answers. Each row links to the most relevant handbook document.

| # | Question | Difficulty | Level | Topic | Related Document |
|---|----------|------------|--------|-------|------------------|
| 1 | Why does rebasing rewrite commit SHAs even when file content is unchanged? | Medium | Senior Engineer | Internals | `content/git-cheatsheet/git-internals.md` |
| 2 | How would you recover a branch deleted after a mistaken `git reset --hard`? | Hard | Lead | Troubleshooting | `content/git-cheatsheet/git-internals.md` |
| 3 | When is `git rebase` safe versus when does it corrupt shared team history? | Medium | Senior Engineer | Design Tradeoffs | `content/git-cheatsheet/rebase.md` |
| 4 | What is the difference between `git merge` and `git rebase` in terms of history graph and conflict resolution? | Medium | Senior Engineer | Fundamentals | `content/git-cheatsheet/merge.md` |
| 5 | How do you resolve a conflict during an interactive rebase without losing the intended commit order? | Hard | Lead | Troubleshooting | `content/git-cheatsheet/interactive-rebase.md` |
| 6 | When would you use `git cherry-pick` instead of merging an entire feature branch? | Medium | Senior Engineer | Operations | `content/git-cheatsheet/cherry-pick.md` |
| 7 | What is the operational difference between `git revert` and `git reset` on a commit already pushed to `main`? | Medium | Lead | Operations | `content/git-cheatsheet/revert.md` |
| 8 | How does the reflog help debug "lost" commits, and what are its retention limits? | Medium | Senior Engineer | Internals | `content/git-cheatsheet/git-internals.md` |
| 9 | What pre-commit and pre-push hooks would you enforce in a production engineering org? | Medium | Lead | Operations | `content/git-cheatsheet/git-hooks.md` |
| 10 | How do you safely force-push a rebased feature branch without overwriting a teammate's work? | Hard | Lead | Troubleshooting | `content/git-cheatsheet/rebase.md` |
| 11 | What causes a merge conflict on unrelated histories, and how do you prevent recurring conflicts on hot files? | Medium | Senior Engineer | Troubleshooting | `content/git-cheatsheet/conflict-resolution.md` |
| 12 | How does `git stash` interact with untracked files, and when does `git stash pop` fail in CI-like workflows? | Medium | Senior Engineer | Operations | `content/git-cheatsheet/stash.md` |
| 13 | What is the difference between `git fetch`, `git pull`, and `git pull --rebase` in a trunk-based workflow? | Easy | Senior Engineer | Fundamentals | `content/git-cheatsheet/remote.md` |
| 14 | How do packfiles and `git gc` affect repository clone size and fetch performance at scale? | Hard | Architect | Performance | `content/git-cheatsheet/git-internals.md` |
| 15 | What branching model would you recommend for a team shipping multiple times per day with required code review? | Medium | Architect | Architecture | `content/git-cheatsheet/pull-request-workflow.md` |
| 16 | Why does a typed-nil pointer assigned to an interface make `w == nil` evaluate to false? | Hard | Senior Engineer | Internals | `content/golang-cheatsheet/interfaces.md` |
| 17 | How does the Go scheduler's M:N model differ from OS threads, and what does `GOMAXPROCS` control? | Medium | Senior Engineer | Internals | `content/golang-cheatsheet/goroutines.md` |
| 18 | When should you prefer a mutex over a channel for shared state in production Go services? | Medium | Lead | Design Tradeoffs | `content/golang-cheatsheet/channels.md` |
| 19 | What happens when you send on a closed channel, and who should close a channel? | Medium | Senior Engineer | Internals | `content/golang-cheatsheet/channels.md` |
| 20 | How do buffered versus unbuffered channels change back-pressure and goroutine leak risk? | Medium | Senior Engineer | Performance | `content/golang-cheatsheet/channels.md` |
| 21 | How would you structure graceful shutdown so in-flight goroutines complete before process exit? | Hard | Lead | Reliability | `content/golang-cheatsheet/goroutines.md` |
| 22 | What is the difference between `errors.Is`, `errors.As`, and wrapping with `%w`? | Medium | Senior Engineer | Fundamentals | `content/golang-cheatsheet/error-handling.md` |
| 23 | How does `context.Context` propagate cancellation, and what are common context leak patterns? | Medium | Lead | Reliability | `content/golang-cheatsheet/context.md` |
| 24 | Why are maps not safe for concurrent access, and when is `sync.Map` appropriate? | Medium | Senior Engineer | Concurrency | `content/golang-cheatsheet/sync-package.md` |
| 25 | How does `append` affect slice length, capacity, and backing-array aliasing between slices? | Medium | Senior Engineer | Internals | `content/golang-cheatsheet/slices.md` |
| 26 | What triggers a goroutine leak, and how would you detect one in a long-running service? | Hard | Lead | Troubleshooting | `content/golang-cheatsheet/goroutines.md` |
| 27 | How does Go's escape analysis influence heap allocation, and when does a value escape? | Hard | Architect | Performance | `content/golang-cheatsheet/memory-model.md` |
| 28 | What does `GOGC` control, and how would you reduce GC pause impact on a latency-sensitive API? | Medium | Lead | Performance | `content/golang-cheatsheet/garbage-collection.md` |
| 29 | How do `RWMutex` read locks behave under write contention, and when is `RWMutex` a bad choice? | Medium | Senior Engineer | Performance | `content/golang-cheatsheet/rwmutex.md` |
| 30 | How would you implement fan-in/fan-out with channels without deadlocking on shutdown? | Hard | Architect | Architecture | `content/golang-cheatsheet/channels.md` |
| 31 | When would you choose Kafka over RabbitMQ for an order-processing platform? | Medium | Architect | Design Tradeoffs | `content/interview-prep/kafka-vs-rabbitmq.md` |
| 32 | How does Kafka's commit-log model enable replay and multiple independent consumer groups? | Medium | Senior Engineer | Internals | `content/kafka-handbook/kafka.md` |
| 33 | What delivery semantics does at-least-once processing imply for consumer design? | Medium | Senior Engineer | Reliability | `content/kafka-handbook/kafka.md` |
| 34 | How do partition keys affect ordering guarantees and hot-partition risk? | Hard | Lead | Scalability | `content/interview-prep/kafka-vs-rabbitmq.md` |
| 35 | Why is idempotent consumer design mandatory in Kafka-based microservices? | Medium | Lead | Reliability | `content/kafka-handbook/kafka.md` |
| 36 | How would you design a dead-letter topic and replay runbook for poison messages? | Hard | Lead | Troubleshooting | `content/kafka-handbook/kafka.md` |
| 37 | What happens during a consumer group rebalance, and how do you minimize duplicate processing? | Hard | Architect | Operations | `content/interview-prep/kafka-vs-rabbitmq.md` |
| 38 | How do you size topic partition count for peak throughput versus maximum consumer parallelism? | Hard | Architect | Scalability | `content/kafka-handbook/kafka.md` |
| 39 | What is consumer lag, and what operational alerts would you set before a marketing campaign? | Medium | Lead | Observability | `content/kafka-handbook/kafka.md` |
| 40 | How does the transactional outbox pattern eliminate the dual-write problem with a database? | Hard | Architect | Architecture | `content/database-handbook/transactional-outbox-pattern.md` |
| 41 | When would you use CDC (Debezium) versus polling the outbox table to publish events? | Hard | Architect | Design Tradeoffs | `content/database-handbook/transactional-outbox-pattern.md` |
| 42 | How do you propagate distributed trace context through Kafka message headers? | Medium | Lead | Observability | `content/kafka-handbook/kafka.md` |
| 43 | What failure modes appear during a Kafka cluster upgrade or broker rolling restart? | Hard | Lead | Troubleshooting | `content/interview-prep/kafka-vs-rabbitmq.md` |
| 44 | How does schema drift break downstream consumers, and what governance would you enforce? | Medium | Lead | Reliability | `content/kafka-handbook/kafka.md` |
| 45 | When is Redpanda a credible alternative to self-hosted Apache Kafka for an event platform? | Medium | Architect | Design Tradeoffs | `content/kafka-handbook/redpanda.md` |
| 46 | What is the role of etcd in Kubernetes, and what breaks if etcd quorum is lost? | Hard | Architect | Internals | `content/kubernetes-handbook/kubernetes-architecture.md` |
| 47 | How do liveness, readiness, and startup probes differ, and what happens when each fails? | Medium | Senior Engineer | Reliability | `content/kubernetes-handbook/probes.md` |
| 48 | Why can an aggressive liveness probe cause CrashLoopBackOff during JVM GC spikes? | Hard | Lead | Troubleshooting | `content/kubernetes-handbook/probes.md` |
| 49 | What is your systematic debug flow for a pod stuck in `ImagePullBackOff`? | Medium | Senior Engineer | Troubleshooting | `content/kubernetes-handbook/troubleshooting.md` |
| 50 | What scheduling constraints commonly leave a pod in `Pending` state? | Medium | Senior Engineer | Troubleshooting | `content/kubernetes-handbook/troubleshooting.md` |
| 51 | How do resource requests and limits interact with the scheduler and OOMKilled behavior? | Medium | Lead | Performance | `content/kubernetes-handbook/resource-limits.md` |
| 52 | Why is HPA ineffective when CPU requests are not set on pod specs? | Medium | Lead | Scalability | `content/kubernetes-handbook/hpa.md` |
| 53 | How would you scale a deployment on custom metrics such as Kafka consumer lag? | Hard | Architect | Scalability | `content/kubernetes-handbook/hpa.md` |
| 54 | What is the difference between a Deployment and a StatefulSet for running databases? | Hard | Architect | Design Tradeoffs | `content/kubernetes-handbook/statefulsets.md` |
| 55 | What split-brain risks exist when running stateful databases inside Kubernetes? | Hard | Architect | Reliability | `content/microservices/declarative-container-orchestration-kubernetes.md` |
| 56 | How do NetworkPolicies change default pod-to-pod connectivity, and what CNI is required? | Medium | Lead | Security | `content/kubernetes-handbook/network-policies.md` |
| 57 | What is a PodDisruptionBudget, and how does it interact with node drains during upgrades? | Medium | Lead | Reliability | `content/kubernetes-handbook/production-best-practices.md` |
| 58 | How do taints, tolerations, and affinity rules affect pod placement under load? | Medium | Lead | Operations | `content/kubernetes-handbook/taints-and-tolerations.md` |
| 59 | What production checklist items would you audit before promoting a namespace to production? | Medium | Architect | Operations | `content/kubernetes-handbook/production-best-practices.md` |
| 60 | How do rolling updates, maxUnavailable, and maxSurge affect availability during deploys? | Medium | Lead | Deployment | `content/kubernetes-handbook/rolling-updates.md` |
| 61 | When would you choose MongoDB over PostgreSQL for a new product domain? | Medium | Architect | Design Tradeoffs | `content/mongodb-cheatsheet/interview-questions.md` |
| 62 | How does replica set failover work, and what happens to writes not replicated to a majority? | Hard | Lead | Reliability | `content/mongodb-cheatsheet/replication.md` |
| 63 | What is the oplog, and how does its size affect secondary catch-up after maintenance? | Medium | Senior Engineer | Internals | `content/mongodb-cheatsheet/replication.md` |
| 64 | How do you choose a shard key to avoid hot shards on monotonic timestamps? | Hard | Architect | Scalability | `content/mongodb-cheatsheet/sharding.md` |
| 65 | What is the difference between a targeted query and scatter-gather in a sharded cluster? | Medium | Senior Engineer | Performance | `content/mongodb-cheatsheet/sharding.md` |
| 66 | When should you embed documents versus reference them in MongoDB schema design? | Medium | Senior Engineer | Architecture | `content/mongodb-cheatsheet/schema-design.md` |
| 67 | What is the ESR rule for compound index key ordering? | Medium | Senior Engineer | Performance | `content/mongodb-cheatsheet/indexes.md` |
| 68 | How do `readConcern`, `writeConcern`, and read preference interact during a regional outage? | Hard | Architect | Reliability | `content/mongodb-cheatsheet/replication.md` |
| 69 | When are multi-document transactions justified versus overkill in MongoDB? | Medium | Lead | Design Tradeoffs | `content/mongodb-cheatsheet/transactions.md` |
| 70 | How would you debug a COLLSCAN surfaced by `explain("executionStats")`? | Medium | Lead | Troubleshooting | `content/mongodb-cheatsheet/performance.md` |
| 71 | What causes chunk migration storms during sharding, and how does zone sharding help? | Hard | Architect | Operations | `content/mongodb-cheatsheet/sharding.md` |
| 72 | What prerequisites and consistency guarantees apply to MongoDB change streams? | Medium | Senior Engineer | Internals | `content/mongodb-cheatsheet/collections.md` |
| 73 | Why should `$match` precede `$lookup` in aggregation pipelines, and what breaks without a foreign index? | Hard | Lead | Performance | `content/mongodb-cheatsheet/aggregation-pipeline.md` |
| 74 | What conditions must a query satisfy to become a covered query, and why exclude `_id` in projection? | Medium | Senior Engineer | Performance | `content/mongodb-cheatsheet/indexes.md` |
| 75 | How does the bucketing pattern prevent unbounded document growth in high-cardinality time-series data? | Hard | Lead | Architecture | `content/mongodb-cheatsheet/schema-design.md` |
| 76 | How does PostgreSQL MVCC implement non-blocking reads while writers update rows? | Hard | Senior Engineer | Internals | [Answer](/postgresql-cheatsheet/02-core-postgresql/mvcc/#q-16) |
| 77 | Why does PostgreSQL require VACUUM, and what happens if autovacuum falls behind? | Medium | Lead | Operations | [Answer](/postgresql-cheatsheet/06-production-operations/vacuum/#q-47) |
| 78 | How do `xmin` and `xmax` determine tuple visibility for a transaction snapshot? | Hard | Senior Engineer | Internals | [Answer](/postgresql-cheatsheet/02-core-postgresql/mvcc/#q-17) |
| 79 | What is the difference between READ COMMITTED and REPEATABLE READ in PostgreSQL? | Medium | Senior Engineer | Fundamentals | [Answer](/postgresql-cheatsheet/02-core-postgresql/isolation-levels/#q-21) |
| 80 | When would you choose a partial index versus a covering index with `INCLUDE`? | Medium | Lead | Performance | [Answer](/postgresql-cheatsheet/03-query-performance/indexes/#q-72) |
| 81 | How do you interpret `EXPLAIN (ANALYZE, BUFFERS)` to find a missing index? | Medium | Lead | Troubleshooting | [Answer](/postgresql-cheatsheet/03-query-performance/explain/#q-43) |
| 82 | Why is raising `max_connections` often the wrong fix for connection exhaustion? | Medium | Lead | Performance | [Answer](/postgresql-cheatsheet/06-production-operations/connection-pooling/#q-38) |
| 83 | How does PgBouncer transaction pooling change application semantics around prepared statements? | Hard | Architect | Architecture | [Answer](/postgresql-cheatsheet/06-production-operations/connection-pooling/#q-73) |
| 84 | What is the difference between streaming replication and logical replication? | Medium | Lead | Reliability | [Answer](/postgresql-cheatsheet/04-high-availability/replication/#q-32) |
| 85 | How do long-running transactions cause table bloat and block vacuum progress? | Hard | Lead | Troubleshooting | [Answer](/postgresql-cheatsheet/02-core-postgresql/mvcc/#q-20) |
| 86 | How does `SELECT ... FOR UPDATE` differ from `SKIP LOCKED` for job-queue worker design? | Medium | Senior Engineer | Internals | [Answer](/postgresql-cheatsheet/02-core-postgresql/locks/#q-24) |
| 87 | How would you partition a large time-series table for prune-friendly queries? | Hard | Architect | Scalability | [Answer](/postgresql-cheatsheet/03-query-performance/partitioning/#q-28) |
| 88 | What parameters would you tune first on an NVMe-backed OLTP instance (`work_mem`, `shared_buffers`)? | Medium | Lead | Performance | [Answer](/postgresql-cheatsheet/03-query-performance/performance-tuning/#q-80) |
| 89 | How does transaction ID wraparound protection work, and why can it force cluster shutdown? | Hard | Architect | Reliability | [Answer](/postgresql-cheatsheet/06-production-operations/vacuum/#q-59) |
| 90 | How would you design a zero-downtime migration adding a `NOT NULL` column to a billion-row table? | Hard | Architect | Deployment | `content/database-handbook/zero-downtime-migration-frameworks.md` |
| 91 | What is the GIL, and why do threads not parallelize CPU-bound Python workloads? | Medium | Senior Engineer | Internals | `content/python-cheatsheet/concurrency.md` |
| 92 | When would you choose asyncio versus threads versus multiprocessing? | Medium | Lead | Design Tradeoffs | `content/python-cheatsheet/concurrency.md` |
| 93 | What happens when a blocking call runs inside an asyncio event loop? | Medium | Senior Engineer | Troubleshooting | `content/python-cheatsheet/asyncio.md` |
| 94 | How does Python's call-by-object-reference semantics affect mutable default arguments? | Medium | Senior Engineer | Internals | `content/python-cheatsheet/functions.md` |
| 95 | What is the descriptor protocol, and how does it power `@property`? | Hard | Senior Engineer | Internals | `content/python-cheatsheet/classes.md` |
| 96 | How does C3 linearization determine MRO in multiple inheritance? | Hard | Senior Engineer | Internals | `content/python-cheatsheet/oop.md` |
| 97 | What is the difference between a generator and a list comprehension in memory terms? | Medium | Senior Engineer | Performance | `content/python-cheatsheet/generators.md` |
| 98 | How do context managers guarantee resource cleanup on exceptions? | Medium | Senior Engineer | Reliability | `content/python-cheatsheet/context-managers.md` |
| 99 | Why prefer `asyncio.TaskGroup` over bare `gather` for structured concurrency? | Medium | Lead | Reliability | `content/python-cheatsheet/asyncio.md` |
| 100 | How would you size a thread pool when downstream is a database with limited connections? | Medium | Lead | Performance | `content/python-cheatsheet/multithreading.md` |
| 101 | What causes reference cycles in CPython, and how does the cyclic GC interact with `__del__`? | Hard | Lead | Internals | `content/python-cheatsheet/memory-management.md` |
| 102 | When should you use `__slots__` or `slots=True` on dataclasses in production? | Medium | Senior Engineer | Performance | `content/python-cheatsheet/dataclasses.md` |
| 103 | What are common asyncio production pitfalls around task cancellation and `CancelledError`? | Hard | Lead | Troubleshooting | `content/python-cheatsheet/asyncio.md` |
| 104 | How does `functools.lru_cache` interact with mutable arguments and memory growth? | Medium | Senior Engineer | Performance | `content/python-cheatsheet/decorators.md` |
| 105 | Why is `spawn` the required multiprocessing start method on Windows, and what breaks with `fork` plus threads? | Medium | Lead | Operations | `content/python-cheatsheet/multiprocessing.md` |
| 106 | How would you mitigate a cache stampede when a hot key expires under flash traffic? | Hard | Architect | Performance | `content/system-design/cache-stampede-and-penetration-mitigation.md` |
| 107 | What is cache penetration, and how do Bloom filters and negative caching differ as defenses? | Hard | Architect | Security | `content/system-design/cache-stampede-and-penetration-mitigation.md` |
| 108 | Orchestration versus choreography — which fits a payment saga with branching compensations? | Hard | Architect | Architecture | `content/microservices/saga-pattern-distributed-transactions.md` |
| 109 | Why does the saga pattern sacrifice ACID isolation, and how does semantic locking help? | Hard | Architect | Design Tradeoffs | `content/microservices/saga-pattern-distributed-transactions.md` |
| 110 | How does a circuit breaker prevent cascading failure in a microservices mesh? | Medium | Lead | Reliability | `content/microservices/circuit-breaker-pattern.md` |
| 111 | What is the PACELC extension of CAP, and how does it apply to DynamoDB versus Cassandra? | Hard | Architect | Fundamentals | `content/microservices/cap-theorem-pacelc-framework.md` |
| 112 | How would you design distributed rate limiting when the Redis cluster partitions? | Hard | Architect | Reliability | `content/microservices/distributed-rate-limiting-throttling.md` |
| 113 | What are the trade-offs between REST and gRPC for internal service-to-service APIs? | Medium | Architect | Design Tradeoffs | `content/interview-prep/rest-vs-grpc.md` |
| 114 | How do you choose between GraphQL and REST for a mobile client with varied data needs? | Medium | Architect | Architecture | `content/interview-prep/graphql-vs-rest.md` |
| 115 | When is event-driven architecture the wrong default for a new bounded context? | Medium | Architect | Design Tradeoffs | `content/technology-playbook/event-driven-architecture.md` |
| 116 | How do PersistentVolume reclaim policies and storage class provisioning affect stateful workload failover? | Hard | Architect | Reliability | `content/kubernetes-handbook/persistent-volumes.md` |
| 117 | What is the transactional inbox pattern's role in exactly-once-ish consumption? | Hard | Architect | Reliability | `content/database-handbook/transactional-inbox-pattern.md` |
| 118 | How do you prevent double-charging when a payment webhook is delivered more than once? | Hard | Lead | Troubleshooting | `content/microservices/saga-pattern-distributed-transactions.md` |
| 119 | What failure modes appear when decomposing a monolithic database into per-service stores? | Hard | Architect | Architecture | `content/microservices/monolithic-database-decomposition.md` |
| 120 | How would you design idempotency keys for a public REST API under at-least-once retries? | Medium | Lead | Reliability | `content/spring-boot/rest-api-design.md` |
| 121 | What observability signals would you require before running Kafka consumers in production? | Medium | Lead | Observability | `content/spring-boot/observability.md` |
| 122 | How do you choose between ClickHouse and Elasticsearch for log analytics at scale? | Hard | Architect | Design Tradeoffs | `content/database-handbook/clickhouse-vs-elasticsearch.md` |
| 123 | What are the operational differences between EKS, AKS, and GKE for a multi-region SaaS? | Hard | Architect | Operations | `content/interview-prep/eks-vs-aks-vs-gke.md` |
| 124 | How does Kubernetes differ from OpenShift for enterprise platform teams? | Medium | Architect | Design Tradeoffs | `content/interview-prep/kubernetes-vs-openshift.md` |
| 125 | When would you pick Temporal over Airflow for long-running business workflows? | Hard | Architect | Architecture | `content/interview-prep/temporal-vs-airflow.md` |
| 126 | How do Spark and Flink differ for stateful stream processing with late-arriving events? | Hard | Architect | Performance | `content/interview-prep/spark-vs-flink.md` |
| 127 | What API gateway capabilities matter for zero-trust ingress in a Kubernetes platform? | Hard | Architect | Security | `content/interview-prep/kong-vs-nginx-vs-aws-api-gateway.md` |
| 128 | How would you design a sponsored-ads system to survive a viral ad click storm? | Hard | Architect | Scalability | `content/system-design/sponsored-ads.md` |
| 129 | What is the difference between cache-aside and write-through under write-heavy load? | Medium | Lead | Performance | `content/spring-boot/caching-performance.md` |
| 130 | How do you enforce least-privilege RBAC for CI/CD deploy roles in Kubernetes? | Medium | Lead | Security | `content/kubernetes-handbook/rbac.md` |
| 131 | What database isolation level would you pick for a financial ledger microservice? | Hard | Architect | Reliability | `content/microservices/database-isolation-levels-concurrency-control.md` |
| 132 | How would you debug cross-service latency when sync calls replaced an event-driven flow? | Medium | Lead | Troubleshooting | `content/kafka-handbook/kafka.md` |
| 133 | What is the thundering herd problem in connection pools during regional failover? | Hard | Lead | Troubleshooting | `content/system-design/cache-stampede-and-penetration-mitigation.md` |
| 134 | How would you design a proximity search system for 1M writes/sec location telemetry? | Hard | Architect | Architecture | `content/system-design/proximity-search-interview-questions.md` |
| 135 | What secrets management approach would you use instead of committing Kubernetes Secrets to Git? | Medium | Architect | Security | `content/kubernetes-handbook/secrets.md` |
| 136 | How do `--ours` and `--theirs` semantics invert during a rebase conflict? | Medium | Senior Engineer | Troubleshooting | `content/git-cheatsheet/conflict-resolution.md` |
| 137 | In a saga with choreography over Kafka, how do you trace and compensate a failed multi-step flow? | Hard | Architect | Architecture | `content/microservices/saga-pattern-distributed-transactions.md` |
| 138 | How do you run blue/green or canary deploys without breaking Kafka consumer offset continuity? | Hard | Lead | Deployment | `content/spring-boot/production-deployment.md` |
| 139 | What data model choices prevent hot partitions in DynamoDB for viral entity traffic? | Hard | Architect | Scalability | `content/system-design/sponsored-ads.md` |
| 140 | How would you design a distributed logging pipeline with back-pressure and retention tiers? | Hard | Architect | Architecture | `content/system-design/distributed-logging-system-interview-questions.md` |
| 141 | When would you use ClusterIP versus LoadBalancer versus Ingress for external HTTP exposure? | Medium | Lead | Architecture | `content/kubernetes-handbook/ingress.md` |
| 142 | How do you choose between Oracle and PostgreSQL for a legacy migration program? | Medium | Architect | Design Tradeoffs | `content/database-handbook/oracle-vs-postgresql.md` |
| 143 | What failure handling would you build into an async order pipeline using Spring and Kafka? | Hard | Lead | Reliability | `content/spring-boot/messaging-events.md` |
| 144 | How do network partitions affect consensus-based leader election in distributed systems? | Hard | Architect | Reliability | `content/system-design/proximity-search-interview-questions.md` |
| 145 | What is the cordon → drain → upgrade → uncordon sequence, and how do PDBs constrain it? | Medium | Lead | Operations | `content/kubernetes-handbook/production-best-practices.md` |
| 146 | How would you detect and remediate silent data corruption in cross-region replication? | Hard | Architect | Troubleshooting | [Answer](/postgresql-cheatsheet/04-high-availability/replication/#q-115) |
| 147 | What testing strategy validates saga compensations before production cutover? | Medium | Lead | Operations | `content/spring-boot/testing.md` |
| 148 | How do you prevent PII leakage in centralized logging and tracing pipelines? | Medium | Architect | Security | `content/spring-boot/observability.md` |
| 149 | How do multi-stage Docker builds and layer cache ordering reduce image size and deploy time? | Medium | Lead | Deployment | `content/kubernetes-handbook/multi-stage-builds.md` |
| 150 | How does CQRS with event sourcing change recovery after a corrupted read model projection? | Hard | Architect | Architecture | `content/microservices/cqrs-event-sourcing.md` |

---

# Top 25 Frequently Asked Questions

1. When would you choose Kafka over RabbitMQ for an order-processing platform?
2. How does PostgreSQL MVCC implement non-blocking reads while writers update rows?
3. What is the GIL, and why do threads not parallelize CPU-bound Python workloads?
4. How do liveness, readiness, and startup probes differ, and what happens when each fails?
5. When would you choose MongoDB over PostgreSQL for a new product domain?
6. Why does a typed-nil pointer assigned to an interface make `w == nil` evaluate to false?
7. What delivery semantics does at-least-once processing imply for consumer design?
8. When is `git rebase` safe versus when does it corrupt shared team history?
9. How do partition keys affect ordering guarantees and hot-partition risk?
10. What is the difference between READ COMMITTED and REPEATABLE READ in PostgreSQL?
11. When would you choose asyncio versus threads versus multiprocessing?
12. How does replica set failover work, and what happens to writes not replicated to a majority?
13. How does the Go scheduler's M:N model differ from OS threads, and what does `GOMAXPROCS` control?
14. Why is idempotent consumer design mandatory in Kafka-based microservices?
15. What is consumer lag, and what operational alerts would you set before a marketing campaign?
16. How do you choose a shard key to avoid hot shards on monotonic timestamps?
17. Orchestration versus choreography — which fits a payment saga with branching compensations?
18. What are the trade-offs between REST and gRPC for internal service-to-service APIs?
19. How does a circuit breaker prevent cascading failure in a microservices mesh?
20. When should you embed documents versus reference them in MongoDB schema design?
21. How would you mitigate a cache stampede when a hot key expires under flash traffic?
22. What is the operational difference between `git revert` and `git reset` on a commit already pushed to `main`?
23. How do `readConcern`, `writeConcern`, and read preference interact during a regional outage?
24. What happens during a consumer group rebalance, and how do you minimize duplicate processing?
25. How would you debug a COLLSCAN surfaced by `explain("executionStats")`?

# Top 25 Architect-Level Questions

1. When would you choose Kafka over RabbitMQ for an order-processing platform?
2. How does the transactional outbox pattern eliminate the dual-write problem with a database?
3. What is the role of etcd in Kubernetes, and what breaks if etcd quorum is lost?
4. How do you choose a shard key to avoid hot shards on monotonic timestamps?
5. Orchestration versus choreography — which fits a payment saga with branching compensations?
6. What is the PACELC extension of CAP, and how does it apply to DynamoDB versus Cassandra?
7. How would you design distributed rate limiting when the Redis cluster partitions?
8. When would you use CDC (Debezium) versus polling the outbox table to publish events?
9. What failure modes appear when decomposing a monolithic database into per-service stores?
10. How would you design a proximity search system for 1M writes/sec location telemetry?
11. When is Redpanda a credible alternative to self-hosted Apache Kafka for an event platform?
12. How do you run blue/green or canary deploys without breaking Kafka consumer offset continuity?
13. What data model choices prevent hot partitions in DynamoDB for viral entity traffic?
14. How would you design a distributed logging pipeline with back-pressure and retention tiers?
15. How do network partitions affect consensus-based leader election in distributed systems?
16. What API gateway capabilities matter for zero-trust ingress in a Kubernetes platform?
17. How do you size topic partition count for peak throughput versus maximum consumer parallelism?
18. How does CQRS with event sourcing change recovery after a corrupted read model projection?
19. How does PgBouncer transaction pooling change application semantics around prepared statements?
20. How would you design a zero-downtime migration adding a `NOT NULL` column to a billion-row table?
21. In a saga with choreography over Kafka, how do you trace and compensate a failed multi-step flow?
22. How would you design a sponsored-ads system to survive a viral ad click storm?
23. What secrets management approach would you use instead of committing Kubernetes Secrets to Git?
24. What are the operational differences between EKS, AKS, and GKE for a multi-region SaaS?
25. What production checklist items would you audit before promoting a namespace to production?

# Top 25 Production Troubleshooting Questions

1. How would you recover a branch deleted after a mistaken `git reset --hard`?
2. How do `--ours` and `--theirs` semantics invert during a rebase conflict?
3. How do you safely force-push a rebased feature branch without overwriting a teammate's work?
4. What is the operational difference between `git revert` and `git reset` on a commit already pushed to `main`?
5. What triggers a goroutine leak, and how would you detect one in a long-running service?
6. How would you structure graceful shutdown so in-flight goroutines complete before process exit?
7. How would you design a dead-letter topic and replay runbook for poison messages?
8. Why can an aggressive liveness probe cause CrashLoopBackOff during JVM GC spikes?
9. What is your systematic debug flow for a pod stuck in `ImagePullBackOff`?
10. What scheduling constraints commonly leave a pod in `Pending` state?
11. How would you debug a COLLSCAN surfaced by `explain("executionStats")`?
12. How do long-running transactions cause table bloat and block vacuum progress?
13. What happens when a blocking call runs inside an asyncio event loop?
14. What are common asyncio production pitfalls around task cancellation and `CancelledError`?
15. How do you prevent double-charging when a payment webhook is delivered more than once?
16. How would you debug cross-service latency when sync calls replaced an event-driven flow?
17. What is the thundering herd problem in connection pools during regional failover?
18. How would you detect and remediate silent data corruption in cross-region replication?
19. What causes chunk migration storms during sharding, and how does zone sharding help?
20. What happens during a consumer group rebalance, and how do you minimize duplicate processing?
21. Why is raising `max_connections` often the wrong fix for connection exhaustion?
22. How do you interpret `EXPLAIN (ANALYZE, BUFFERS)` to find a missing index?
23. Why should `$match` precede `$lookup` in aggregation pipelines, and what breaks without a foreign index?
24. What failure modes appear during a Kafka cluster upgrade or broker rolling restart?
25. How do you resolve a conflict during an interactive rebase without losing the intended commit order?

# Top 25 Performance & Scalability Questions

1. How do partition keys affect ordering guarantees and hot-partition risk?
2. How do you size topic partition count for peak throughput versus maximum consumer parallelism?
3. How would you scale a deployment on custom metrics such as Kafka consumer lag?
4. How do resource requests and limits interact with the scheduler and OOMKilled behavior?
5. Why is HPA ineffective when CPU requests are not set on pod specs?
6. How does `append` affect slice length, capacity, and backing-array aliasing between slices?
7. What does `GOGC` control, and how would you reduce GC pause impact on a latency-sensitive API?
8. How do `RWMutex` read locks behave under write contention, and when is `RWMutex` a bad choice?
9. How would you mitigate a cache stampede when a hot key expires under flash traffic?
10. What is the difference between a targeted query and scatter-gather in a sharded cluster?
11. What is the ESR rule for compound index key ordering?
12. What conditions must a query satisfy to become a covered query, and why exclude `_id` in projection?
13. When would you choose a partial index versus a covering index with `INCLUDE`?
14. What parameters would you tune first on an NVMe-backed OLTP instance (`work_mem`, `shared_buffers`)?
15. How would you size a thread pool when downstream is a database with limited connections?
16. How does `functools.lru_cache` interact with mutable arguments and memory growth?
17. How do Spark and Flink differ for stateful stream processing with late-arriving events?
18. What data model choices prevent hot partitions in DynamoDB for viral entity traffic?
19. How would you design a sponsored-ads system to survive a viral ad click storm?
20. How would you design a proximity search system for 1M writes/sec location telemetry?
21. What is the difference between cache-aside and write-through under write-heavy load?
22. How do packfiles and `git gc` affect repository clone size and fetch performance at scale?
23. How would you partition a large time-series table for prune-friendly queries?
24. What is the difference between a generator and a list comprehension in memory terms?
25. How do multi-stage Docker builds and layer cache ordering reduce image size and deploy time?

# Top 25 Design & Architecture Questions

1. When would you choose Kafka over RabbitMQ for an order-processing platform?
2. How does the transactional outbox pattern eliminate the dual-write problem with a database?
3. When would you use CDC (Debezium) versus polling the outbox table to publish events?
4. Orchestration versus choreography — which fits a payment saga with branching compensations?
5. Why does the saga pattern sacrifice ACID isolation, and how does semantic locking help?
6. When would you choose MongoDB over PostgreSQL for a new product domain?
7. What is the difference between a Deployment and a StatefulSet for running databases?
8. When should you embed documents versus reference them in MongoDB schema design?
9. How does PgBouncer transaction pooling change application semantics around prepared statements?
10. What are the trade-offs between REST and gRPC for internal service-to-service APIs?
11. How do you choose between GraphQL and REST for a mobile client with varied data needs?
12. When is event-driven architecture the wrong default for a new bounded context?
13. What failure modes appear when decomposing a monolithic database into per-service stores?
14. What is the transactional inbox pattern's role in exactly-once-ish consumption?
15. How do you choose between ClickHouse and Elasticsearch for log analytics at scale?
16. When would you pick Temporal over Airflow for long-running business workflows?
17. What API gateway capabilities matter for zero-trust ingress in a Kubernetes platform?
18. When is Redpanda a credible alternative to self-hosted Apache Kafka for an event platform?
19. How would you design a distributed logging pipeline with back-pressure and retention tiers?
20. What branching model would you recommend for a team shipping multiple times per day with required code review?
21. In a saga with choreography over Kafka, how do you trace and compensate a failed multi-step flow?
22. How do you choose between Oracle and PostgreSQL for a legacy migration program?
23. How does CQRS with event sourcing change recovery after a corrupted read model projection?
24. When would you use ClusterIP versus LoadBalancer versus Ingress for external HTTP exposure?
25. How would you design idempotency keys for a public REST API under at-least-once retries?
