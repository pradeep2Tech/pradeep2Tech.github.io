---
title: "Top 150 Redis Interview Questions"
date: 2026-07-03T13:00:00+00:00
draft: false
description: "150 production-oriented Redis interview questions mapped to canonical handbook pages."
tags: ["redis-cheatsheet", "redis-handbook", "redis", "interview"]
categories: ["Redis Handbook"]
shortTitle: "Top 150"
module: 8
moduleTitle: "Interview Guide"
sectionRef: "8.1"
weight: 801
ShowToc: true
interviewHandbook: true

aliases:
  - "/redis-cheatsheet/interview-questions/"
---

Curated questions for **6+ year** engineers, leads, and architects. Question index with **inline answers** below. **Deep Dive** links point to canonical handbook pages for extended context.

**Distribution:** Architecture 40 · Troubleshooting 30 · Performance 25 · Reliability 20 · Scalability 15 · Patterns 20

| # | Question | Difficulty | Level | Topic | Deep Dive |
|---|----------|------------|--------|-------|-----------|
| 1 | Why does Redis use a single-threaded command execution model, and when do I/O threads change that picture? | Medium | Senior Engineer | Architecture | [Architecture — Q1](/redis-cheatsheet/01-fundamentals/architecture/#why-does-redis-use-a-single-threaded-command-execution-model-and-when-do-io-thre) |
| 2 | How would you choose between standalone Redis, Sentinel, and Cluster for a new payment-adjacent cache? | Hard | Architect | Architecture | [Architecture — Q2](/redis-cheatsheet/01-fundamentals/architecture/#how-would-you-choose-between-standalone-redis-sentinel-and-cluster-for-a-new-pay) |
| 3 | What architectural role does Redis play when it is cache versus when it is the primary data store? | Medium | Architect | Architecture | [Architecture — Q3](/redis-cheatsheet/01-fundamentals/architecture/#what-architectural-role-does-redis-play-when-it-is-cache-versus-when-it-is-the-p) |
| 4 | How does the global keyspace dictionary influence hot-key and big-key failure modes at scale? | Hard | Senior Engineer | Architecture | [Architecture — Q4](/redis-cheatsheet/01-fundamentals/architecture/#how-does-the-global-keyspace-dictionary-influence-hot-key-and-big-key-failure-mo) |
| 5 | When would you shard with Redis Cluster instead of vertical scaling a single primary? | Hard | Architect | Architecture | [Cluster — Q5](/redis-cheatsheet/03-redis-internals/cluster/#when-would-you-shard-with-redis-cluster-instead-of-vertical-scaling-a-single-pri) |
| 6 | How do hash tags change your key design when you need multi-key atomicity in Cluster? | Hard | Lead | Architecture | [Cluster — Q6](/redis-cheatsheet/03-redis-internals/cluster/#how-do-hash-tags-change-your-key-design-when-you-need-multi-key-atomicity-in-clu) |
| 7 | What is the mental model for 16384 hash slots, and why not more or fewer? | Medium | Senior Engineer | Architecture | [Cluster — Q7](/redis-cheatsheet/03-redis-internals/cluster/#what-is-the-mental-model-for-16384-hash-slots-and-why-not-more-or-fewer) |
| 8 | How do MOVED and ASK redirects differ in client architecture during normal ops versus resharding? | Hard | Lead | Architecture | [Redis Protocol — Q8](/redis-cheatsheet/03-redis-internals/redis-protocol/#how-do-moved-and-ask-redirects-differ-in-client-architecture-during-normal-ops-v) |
| 9 | When is Sentinel the right HA layer versus managed cloud failover you do not operate? | Medium | Architect | Architecture | [Sentinel — Q9](/redis-cheatsheet/03-redis-internals/sentinel/#when-is-sentinel-the-right-ha-layer-versus-managed-cloud-failover-you-do-not-ope) |
| 10 | How would you diagram request flow from application through connection pool to Redis command thread? | Medium | Senior Engineer | Architecture | [Redis Protocol — Q10](/redis-cheatsheet/03-redis-internals/redis-protocol/#how-would-you-diagram-request-flow-from-application-through-connection-pool-to-r) |
| 11 | What data type would you pick for a user profile with frequent single-field updates, and why not a JSON string? | Medium | Senior Engineer | Architecture | [Data Structures — Q11](/redis-cheatsheet/01-fundamentals/data-structures/#what-data-type-would-you-pick-for-a-user-profile-with-frequent-single-field-upda) |
| 12 | When are Redis Streams architecturally appropriate versus an external log like Kafka? | Hard | Architect | Architecture | [Redis Vs Kafka — Q12](/redis-cheatsheet/07-comparisons/redis-vs-kafka/#when-are-redis-streams-architecturally-appropriate-versus-an-external-log-like-k) |
| 13 | When are Redis lists or Streams appropriate versus RabbitMQ for task distribution? | Hard | Architect | Architecture | [Redis Vs Rabbitmq — Q13](/redis-cheatsheet/07-comparisons/redis-vs-rabbitmq/#when-are-redis-lists-or-streams-appropriate-versus-rabbitmq-for-task-distributio) |
| 14 | How does Pub/Sub fit into cache invalidation architecture without becoming a system of record? | Medium | Lead | Architecture | [Pub Sub — Q14](/redis-cheatsheet/04-distributed-systems/pub-sub/#how-does-pubsub-fit-into-cache-invalidation-architecture-without-becoming-a-syst) |
| 15 | What tradeoffs does Redis offer versus Memcached for a pure session cache layer? | Medium | Architect | Architecture | [Redis Vs Memcached — Q15](/redis-cheatsheet/07-comparisons/redis-vs-memcached/#what-tradeoffs-does-redis-offer-versus-memcached-for-a-pure-session-cache-layer) |
| 16 | How would you isolate tenant traffic on a shared Redis cluster without cross-tenant key collisions? | Hard | Architect | Architecture | [Cluster — Q16](/redis-cheatsheet/03-redis-internals/cluster/#how-would-you-isolate-tenant-traffic-on-a-shared-redis-cluster-without-cross-ten) |
| 17 | When do Redis modules (RedisJSON, RediSearch) change your storage architecture versus plain hashes? | Medium | Lead | Architecture | [Data Structures — Q17](/redis-cheatsheet/01-fundamentals/data-structures/#when-do-redis-modules-redisjson-redisearch-change-your-storage-architecture-vers) |
| 18 | How does TTL-at-key-level architecture affect session design versus field-level expiry needs? | Medium | Senior Engineer | Architecture | [Data Structures — Q18](/redis-cheatsheet/01-fundamentals/data-structures/#how-does-ttl-at-key-level-architecture-affect-session-design-versus-field-level) |
| 19 | What signals indicate a workload has outgrown a single primary before ops teams admit it? | Hard | Architect | Architecture | [Capacity Planning — Q19](/redis-cheatsheet/06-performance-operations/capacity-planning/#what-signals-indicate-a-workload-has-outgrown-a-single-primary-before-ops-teams) |
| 20 | How would you place Redis relative to the database in a read-heavy catalog service? | Medium | Senior Engineer | Architecture | [Caching Patterns — Q20](/redis-cheatsheet/05-production-patterns/caching-patterns/#how-would-you-place-redis-relative-to-the-database-in-a-read-heavy-catalog-servi) |
| 21 | When is replica read scaling architecturally safe, and when does it violate freshness requirements? | Hard | Lead | Architecture | [Replication — Q21](/redis-cheatsheet/03-redis-internals/replication/#when-is-replica-read-scaling-architecturally-safe-and-when-does-it-violate-fresh) |
| 22 | How do persistence settings change the architecture story when Redis is marketed as a cache only? | Medium | Architect | Architecture | [Persistence — Q22](/redis-cheatsheet/03-redis-internals/persistence/#how-do-persistence-settings-change-the-architecture-story-when-redis-is-marketed) |
| 23 | What is the architectural impact of running Redis in Kubernetes with ephemeral versus persistent volumes? | Hard | Architect | Architecture | [Persistence — Q23](/redis-cheatsheet/03-redis-internals/persistence/#what-is-the-architectural-impact-of-running-redis-in-kubernetes-with-ephemeral-v) |
| 24 | How would you design key namespaces for microservices sharing one cluster without coupling? | Medium | Lead | Architecture | [Data Structures — Q24](/redis-cheatsheet/01-fundamentals/data-structures/#how-would-you-design-key-namespaces-for-microservices-sharing-one-cluster-withou) |
| 25 | When does colocating rate limiting, sessions, and entity cache in one cluster create blast-radius risk? | Hard | Architect | Architecture | [Rate Limiter — Q25](/redis-cheatsheet/05-production-patterns/rate-limiter/#when-does-colocating-rate-limiting-sessions-and-entity-cache-in-one-cluster-crea) |
| 26 | How does active-active multi-region Redis differ architecturally from single-region Cluster plus replication? | Hard | Architect | Architecture | [Cluster — Q26](/redis-cheatsheet/03-redis-internals/cluster/#how-does-active-active-multi-region-redis-differ-architecturally-from-single-reg) |
| 27 | What client topology changes when applications must be Sentinel-aware versus Cluster-aware? | Medium | Senior Engineer | Architecture | [Sentinel — Q27](/redis-cheatsheet/03-redis-internals/sentinel/#what-client-topology-changes-when-applications-must-be-sentinel-aware-versus-clu) |
| 28 | How would you justify Redis as a delay queue using sorted sets versus a dedicated scheduler? | Medium | Lead | Architecture | [Sorted Sets — Q28](/redis-cheatsheet/02-core-redis/sorted-sets/#how-would-you-justify-redis-as-a-delay-queue-using-sorted-sets-versus-a-dedicate) |
| 29 | When is HyperLogLog the correct architectural choice for analytics versus sets or bitmaps? | Medium | Senior Engineer | Architecture | [Hyperloglog — Q29](/redis-cheatsheet/02-core-redis/hyperloglog/#when-is-hyperloglog-the-correct-architectural-choice-for-analytics-versus-sets-o) |
| 30 | How do Lua scripts affect your architecture for atomic inventory decrements? | Hard | Lead | Architecture | [Lua Scripts — Q30](/redis-cheatsheet/04-distributed-systems/lua-scripts/#how-do-lua-scripts-affect-your-architecture-for-atomic-inventory-decrements) |
| 31 | What architecture pitfalls appear when using Redis transactions across many hot keys? | Hard | Senior Engineer | Architecture | [Transactions — Q31](/redis-cheatsheet/04-distributed-systems/transactions/#what-architecture-pitfalls-appear-when-using-redis-transactions-across-many-hot) |
| 32 | How would you blueprint replica count and sentinel quorum in an ADR for 99.95% cache availability? | Hard | Architect | Architecture | [Sentinel — Q32](/redis-cheatsheet/03-redis-internals/sentinel/#how-would-you-blueprint-replica-count-and-sentinel-quorum-in-an-adr-for-9995-cac) |
| 33 | When does TLS termination at proxy versus Redis native TLS change trust boundaries? | Medium | Architect | Architecture | [Redis Protocol — Q33](/redis-cheatsheet/03-redis-internals/redis-protocol/#when-does-tls-termination-at-proxy-versus-redis-native-tls-change-trust-boundari) |
| 34 | How does connection pooling architecture prevent thundering herd on Redis reconnect after failover? | Hard | Lead | Architecture | [Sentinel — Q34](/redis-cheatsheet/03-redis-internals/sentinel/#how-does-connection-pooling-architecture-prevent-thundering-herd-on-redis-reconn) |
| 35 | What architectural constraints does Redis impose on exactly-once processing semantics? | Hard | Architect | Architecture | [Streams — Q35](/redis-cheatsheet/04-distributed-systems/streams/#what-architectural-constraints-does-redis-impose-on-exactly-once-processing-sema) |
| 36 | How would you map cache patterns (aside, through, behind) to team ownership boundaries? | Medium | Architect | Architecture | [Caching Patterns — Q36](/redis-cheatsheet/05-production-patterns/caching-patterns/#how-would-you-map-cache-patterns-aside-through-behind-to-team-ownership-boundari) |
| 37 | When is noeviction the correct maxmemory-policy for a non-cache primary store? | Medium | Lead | Architecture | [Eviction Policies — Q37](/redis-cheatsheet/06-performance-operations/eviction-policies/#when-is-noeviction-the-correct-maxmemory-policy-for-a-non-cache-primary-store) |
| 38 | How do Redis ACLs change multi-tenant architecture compared to shared-password eras? | Medium | Architect | Architecture | [Architecture — Q38](/redis-cheatsheet/01-fundamentals/architecture/#how-do-redis-acls-change-multi-tenant-architecture-compared-to-shared-password-e) |
| 39 | What cross-datacenter replication options would you compare before choosing Redis Cluster only? | Hard | Architect | Architecture | [Replication — Q39](/redis-cheatsheet/03-redis-internals/replication/#what-cross-datacenter-replication-options-would-you-compare-before-choosing-redi) |
| 40 | How would you defend Redis versus a cloud vendor cache in an enterprise architecture review? | Hard | Architect | Architecture | [Redis Vs Memcached — Q40](/redis-cheatsheet/07-comparisons/redis-vs-memcached/#how-would-you-defend-redis-versus-a-cloud-vendor-cache-in-an-enterprise-architec) |
| 41 | How do you triage sudden memory growth when used_memory rises but key count looks stable? | Hard | Lead | Troubleshooting | [Troubleshooting — Q41](/redis-cheatsheet/06-performance-operations/troubleshooting/#how-do-you-triage-sudden-memory-growth-when-used-memory-rises-but-key-count-look) |
| 42 | What steps isolate whether latency spikes are network, slow commands, or fork-related COW pressure? | Hard | Lead | Troubleshooting | [Troubleshooting — Q42](/redis-cheatsheet/06-performance-operations/troubleshooting/#what-steps-isolate-whether-latency-spikes-are-network-slow-commands-or-fork-rela) |
| 43 | How would you diagnose replication lag that only appears during peak write hours? | Hard | Lead | Troubleshooting | [Troubleshooting — Q43](/redis-cheatsheet/06-performance-operations/troubleshooting/#how-would-you-diagnose-replication-lag-that-only-appears-during-peak-write-hours) |
| 44 | What does LATENCY DOCTOR tell you that SLOWLOG alone cannot? | Medium | Senior Engineer | Troubleshooting | [Monitoring — Q44](/redis-cheatsheet/06-performance-operations/monitoring/#what-does-latency-doctor-tell-you-that-slowlog-alone-cannot) |
| 45 | How do you find and remediate hot keys without KEYS or MONITOR in production? | Hard | Lead | Troubleshooting | [Troubleshooting — Q45](/redis-cheatsheet/06-performance-operations/troubleshooting/#how-do-you-find-and-remediate-hot-keys-without-keys-or-monitor-in-production) |
| 46 | What symptoms distinguish a big-key problem from a hot-key problem on a single-threaded primary? | Hard | Senior Engineer | Troubleshooting | [Troubleshooting — Q46](/redis-cheatsheet/06-performance-operations/troubleshooting/#what-symptoms-distinguish-a-big-key-problem-from-a-hot-key-problem-on-a-single-t) |
| 47 | How would you troubleshoot Cluster slot imbalance after adding a new primary? | Hard | Lead | Troubleshooting | [Troubleshooting — Q47](/redis-cheatsheet/06-performance-operations/troubleshooting/#how-would-you-troubleshoot-cluster-slot-imbalance-after-adding-a-new-primary) |
| 48 | What is your runbook when clients report MOVED storms after a resharding operation? | Hard | Lead | Troubleshooting | [Troubleshooting — Q48](/redis-cheatsheet/06-performance-operations/troubleshooting/#what-is-your-runbook-when-clients-report-moved-storms-after-a-resharding-operati) |
| 49 | How do you debug Sentinel failover loops where primaries flap every few minutes? | Hard | Architect | Troubleshooting | [Troubleshooting — Q49](/redis-cheatsheet/06-performance-operations/troubleshooting/#how-do-you-debug-sentinel-failover-loops-where-primaries-flap-every-few-minutes) |
| 50 | What causes writes to fail with OOM errors despite setting maxmemory? | Medium | Senior Engineer | Troubleshooting | [Troubleshooting — Q50](/redis-cheatsheet/06-performance-operations/troubleshooting/#what-causes-writes-to-fail-with-oom-errors-despite-setting-maxmemory) |
| 51 | How would you investigate volatile-lru not evicting keys when memory is full? | Medium | Senior Engineer | Troubleshooting | [Eviction Policies — Q51](/redis-cheatsheet/06-performance-operations/eviction-policies/#how-would-you-investigate-volatile-lru-not-evicting-keys-when-memory-is-full) |
| 52 | What forensic steps follow a partial AOF rewrite failure on restart? | Hard | Lead | Troubleshooting | [Persistence — Q52](/redis-cheatsheet/03-redis-internals/persistence/#what-forensic-steps-follow-a-partial-aof-rewrite-failure-on-restart) |
| 53 | How do you detect and fix replica serving stale reads that break business rules? | Hard | Lead | Troubleshooting | [Replication — Q53](/redis-cheatsheet/03-redis-internals/replication/#how-do-you-detect-and-fix-replica-serving-stale-reads-that-break-business-rules) |
| 54 | What explains consumer group pending entries growing without XPENDING visibility in dashboards? | Hard | Senior Engineer | Troubleshooting | [Streams — Q54](/redis-cheatsheet/04-distributed-systems/streams/#what-explains-consumer-group-pending-entries-growing-without-xpending-visibility) |
| 55 | How would you troubleshoot cache stampede after a popular key expires simultaneously? | Hard | Lead | Troubleshooting | [Cache Avalanche — Q55](/redis-cheatsheet/05-production-patterns/cache-avalanche/#how-would-you-troubleshoot-cache-stampede-after-a-popular-key-expires-simultaneo) |
| 56 | What mitigations apply when cache penetration hammers the database for non-existent IDs? | Hard | Lead | Troubleshooting | [Cache Penetration — Q56](/redis-cheatsheet/05-production-patterns/cache-penetration/#what-mitigations-apply-when-cache-penetration-hammers-the-database-for-non-exist) |
| 57 | How do you debug distributed lock double-execution after TTL expiry? | Hard | Architect | Troubleshooting | [Distributed Lock — Q57](/redis-cheatsheet/04-distributed-systems/distributed-lock/#how-do-you-debug-distributed-lock-double-execution-after-ttl-expiry) |
| 58 | What would you check when BGSAVE consistently fails during memory pressure events? | Hard | Lead | Troubleshooting | [Persistence — Q58](/redis-cheatsheet/03-redis-internals/persistence/#what-would-you-check-when-bgsave-consistently-fails-during-memory-pressure-event) |
| 59 | How do you triage high CPU on Redis when QPS has not increased? | Medium | Senior Engineer | Troubleshooting | [Troubleshooting — Q59](/redis-cheatsheet/06-performance-operations/troubleshooting/#how-do-you-triage-high-cpu-on-redis-when-qps-has-not-increased) |
| 60 | What client-side symptoms indicate connection pool exhaustion versus server maxclients? | Medium | Senior Engineer | Troubleshooting | [Monitoring — Q60](/redis-cheatsheet/06-performance-operations/monitoring/#what-client-side-symptoms-indicate-connection-pool-exhaustion-versus-server-maxc) |
| 61 | How would you debug a Lua script that intermittently fails with CROSSSLOT errors in Cluster? | Hard | Lead | Troubleshooting | [Lua Scripts — Q61](/redis-cheatsheet/04-distributed-systems/lua-scripts/#how-would-you-debug-a-lua-script-that-intermittently-fails-with-crossslot-errors) |
| 62 | What runbook steps apply when one shard in Cluster hits 100% CPU while others are idle? | Hard | Lead | Troubleshooting | [Troubleshooting — Q62](/redis-cheatsheet/06-performance-operations/troubleshooting/#what-runbook-steps-apply-when-one-shard-in-cluster-hits-100-cpu-while-others-are) |
| 63 | How do you identify commands blocking the event loop beyond SLOWLOG threshold tuning? | Hard | Senior Engineer | Troubleshooting | [Performance Tuning — Q63](/redis-cheatsheet/06-performance-operations/performance-tuning/#how-do-you-identify-commands-blocking-the-event-loop-beyond-slowlog-threshold-tu) |
| 64 | What causes mem_fragmentation_ratio to climb and when is active defrag appropriate? | Hard | Lead | Troubleshooting | [Memory Management — Q64](/redis-cheatsheet/03-redis-internals/memory-management/#what-causes-mem-fragmentation-ratio-to-climb-and-when-is-active-defrag-appropria) |
| 65 | How would you troubleshoot session loss after a Sentinel failover during peak traffic? | Hard | Lead | Troubleshooting | [Session Store — Q65](/redis-cheatsheet/05-production-patterns/session-store/#how-would-you-troubleshoot-session-loss-after-a-sentinel-failover-during-peak-tr) |
| 66 | What diagnostics differentiate network partition from overloaded primary during timeout storms? | Hard | Architect | Troubleshooting | [Troubleshooting — Q66](/redis-cheatsheet/06-performance-operations/troubleshooting/#what-diagnostics-differentiate-network-partition-from-overloaded-primary-during) |
| 67 | How do you debug rate limiter drift when counters look correct per key but limits feel wrong? | Medium | Senior Engineer | Troubleshooting | [Rate Limiter — Q67](/redis-cheatsheet/05-production-patterns/rate-limiter/#how-do-you-debug-rate-limiter-drift-when-counters-look-correct-per-key-but-limit) |
| 68 | What steps validate AOF integrity before promoting a rebuilt replica? | Hard | Lead | Troubleshooting | [Persistence — Q68](/redis-cheatsheet/03-redis-internals/persistence/#what-steps-validate-aof-integrity-before-promoting-a-rebuilt-replica) |
| 69 | How would you investigate Pub/Sub subscribers missing invalidation messages intermittently? | Medium | Lead | Troubleshooting | [Pub Sub — Q69](/redis-cheatsheet/04-distributed-systems/pub-sub/#how-would-you-investigate-pubsub-subscribers-missing-invalidation-messages-inter) |
| 70 | What is your incident checklist when Redis latency breaches SLO but INFO shows low ops/sec? | Hard | Architect | Troubleshooting | [Monitoring — Q70](/redis-cheatsheet/06-performance-operations/monitoring/#what-is-your-incident-checklist-when-redis-latency-breaches-slo-but-info-shows-l) |
| 71 | How does pipelining improve throughput without changing Redis single-threaded execution? | Medium | Senior Engineer | Performance | [Performance Tuning — Q71](/redis-cheatsheet/06-performance-operations/performance-tuning/#how-does-pipelining-improve-throughput-without-changing-redis-single-threaded-ex) |
| 72 | What pipeline batch size tradeoffs would you test against a 5ms p99 latency SLO? | Hard | Lead | Performance | [Performance Tuning — Q72](/redis-cheatsheet/06-performance-operations/performance-tuning/#what-pipeline-batch-size-tradeoffs-would-you-test-against-a-5ms-p99-latency-slo) |
| 73 | When does MGET outperform pipelined GET for the same key batch? | Medium | Senior Engineer | Performance | [Performance Tuning — Q73](/redis-cheatsheet/06-performance-operations/performance-tuning/#when-does-mget-outperform-pipelined-get-for-the-same-key-batch) |
| 74 | How do large values in strings affect network and latency more than CPU on the server? | Medium | Senior Engineer | Performance | [Strings — Q74](/redis-cheatsheet/02-core-redis/strings/#how-do-large-values-in-strings-affect-network-and-latency-more-than-cpu-on-the-s) |
| 75 | What command choices turn O(1) expectations into O(N) event-loop blockers? | Hard | Lead | Performance | [Performance Tuning — Q75](/redis-cheatsheet/06-performance-operations/performance-tuning/#what-command-choices-turn-o1-expectations-into-on-event-loop-blockers) |
| 76 | How would you tune io-threads and io-threads-do-reads for a read-heavy workload? | Hard | Lead | Performance | [Architecture — Q76](/redis-cheatsheet/01-fundamentals/architecture/#how-would-you-tune-io-threads-and-io-threads-do-reads-for-a-read-heavy-workload) |
| 77 | What is the performance impact of appendfsync always versus everysec for write-heavy caches? | Hard | Architect | Performance | [Persistence — Q77](/redis-cheatsheet/03-redis-internals/persistence/#what-is-the-performance-impact-of-appendfsync-always-versus-everysec-for-write-h) |
| 78 | How does RDB fork latency interact with memory overcommit and COW during BGSAVE? | Hard | Lead | Performance | [Persistence — Q78](/redis-cheatsheet/03-redis-internals/persistence/#how-does-rdb-fork-latency-interact-with-memory-overcommit-and-cow-during-bgsave) |
| 79 | When does allkeys-lfu outperform allkeys-lru for skewed access patterns? | Medium | Senior Engineer | Performance | [Eviction Policies — Q79](/redis-cheatsheet/06-performance-operations/eviction-policies/#when-does-allkeys-lfu-outperform-allkeys-lru-for-skewed-access-patterns) |
| 80 | How do maxmemory-samples settings affect eviction accuracy and CPU? | Medium | Senior Engineer | Performance | [Eviction Policies — Q80](/redis-cheatsheet/06-performance-operations/eviction-policies/#how-do-maxmemory-samples-settings-affect-eviction-accuracy-and-cpu) |
| 81 | What encoding upgrades cause latency cliffs as small hashes grow past listpack thresholds? | Hard | Lead | Performance | [Memory Management — Q81](/redis-cheatsheet/03-redis-internals/memory-management/#what-encoding-upgrades-cause-latency-cliffs-as-small-hashes-grow-past-listpack-t) |
| 82 | How would you benchmark UNLINK versus DEL for bulk key deletion in production maintenance? | Medium | Senior Engineer | Performance | [Performance Tuning — Q82](/redis-cheatsheet/06-performance-operations/performance-tuning/#how-would-you-benchmark-unlink-versus-del-for-bulk-key-deletion-in-production-ma) |
| 83 | What client connection pool sizing formula avoids Redis maxclients saturation? | Hard | Lead | Performance | [Capacity Planning — Q83](/redis-cheatsheet/06-performance-operations/capacity-planning/#what-client-connection-pool-sizing-formula-avoids-redis-maxclients-saturation) |
| 84 | How does TLS add latency, and where would you terminate TLS for cache workloads? | Medium | Architect | Performance | [Redis Protocol — Q84](/redis-cheatsheet/03-redis-internals/redis-protocol/#how-does-tls-add-latency-and-where-would-you-terminate-tls-for-cache-workloads) |
| 85 | When does sharding with Cluster improve throughput versus larger single-instance hardware? | Hard | Architect | Performance | [Cluster — Q85](/redis-cheatsheet/03-redis-internals/cluster/#when-does-sharding-with-cluster-improve-throughput-versus-larger-single-instance) |
| 86 | How do BITOP and BITCOUNT scale poorly on large sparse bitmaps? | Medium | Senior Engineer | Performance | [Bitmaps — Q86](/redis-cheatsheet/02-core-redis/bitmaps/#how-do-bitop-and-bitcount-scale-poorly-on-large-sparse-bitmaps) |
| 87 | What ZSET range query patterns need LIMIT to protect p99 latency? | Medium | Senior Engineer | Performance | [Sorted Sets — Q87](/redis-cheatsheet/02-core-redis/sorted-sets/#what-zset-range-query-patterns-need-limit-to-protect-p99-latency) |
| 88 | How would you optimize a sliding-window rate limiter implemented with sorted sets? | Hard | Lead | Performance | [Rate Limiter — Q88](/redis-cheatsheet/05-production-patterns/rate-limiter/#how-would-you-optimize-a-sliding-window-rate-limiter-implemented-with-sorted-set) |
| 89 | What latency gains come from switching HGETALL to HMGET or HSCAN on wide hashes? | Medium | Senior Engineer | Performance | [Hashes — Q89](/redis-cheatsheet/02-core-redis/hashes/#what-latency-gains-come-from-switching-hgetall-to-hmget-or-hscan-on-wide-hashes) |
| 90 | How does replication backlog sizing affect partial resync performance after brief outages? | Medium | Lead | Performance | [Replication — Q90](/redis-cheatsheet/03-redis-internals/replication/#how-does-replication-backlog-sizing-affect-partial-resync-performance-after-brie) |
| 91 | What OS-level tuning (transparent huge pages, somaxconn) still matters for Redis in 2026? | Hard | Lead | Performance | [Performance Tuning — Q91](/redis-cheatsheet/06-performance-operations/performance-tuning/#what-os-level-tuning-transparent-huge-pages-somaxconn-still-matters-for-redis-in) |
| 92 | How would you load-test Redis Cluster to find the first bottleneck: CPU, network, or slot skew? | Hard | Architect | Performance | [Capacity Planning — Q92](/redis-cheatsheet/06-performance-operations/capacity-planning/#how-would-you-load-test-redis-cluster-to-find-the-first-bottleneck-cpu-network-o) |
| 93 | When does probabilistic early expiration improve tail latency versus naive TTL refresh? | Hard | Lead | Performance | [Cache Avalanche — Q93](/redis-cheatsheet/05-production-patterns/cache-avalanche/#when-does-probabilistic-early-expiration-improve-tail-latency-versus-naive-ttl-r) |
| 94 | How do Streams MAXLEN approximate trimming trade memory for ingestion throughput? | Medium | Senior Engineer | Performance | [Streams — Q94](/redis-cheatsheet/04-distributed-systems/streams/#how-do-streams-maxlen-approximate-trimming-trade-memory-for-ingestion-throughput) |
| 95 | What metrics prove your cache hit ratio improvements actually reduced database load? | Medium | Lead | Performance | [Monitoring — Q95](/redis-cheatsheet/06-performance-operations/monitoring/#what-metrics-prove-your-cache-hit-ratio-improvements-actually-reduced-database-l) |
| 96 | What data loss window exists with appendfsync everysec if the process crashes mid-second? | Medium | Senior Engineer | Reliability | [Persistence — Q96](/redis-cheatsheet/03-redis-internals/persistence/#what-data-loss-window-exists-with-appendfsync-everysec-if-the-process-crashes-mi) |
| 97 | How do RDB snapshots complement AOF for faster restarts in hybrid persistence? | Medium | Lead | Reliability | [Persistence — Q97](/redis-cheatsheet/03-redis-internals/persistence/#how-do-rdb-snapshots-complement-aof-for-faster-restarts-in-hybrid-persistence) |
| 98 | When would you disable persistence entirely, and what failure modes remain acceptable? | Medium | Architect | Reliability | [Persistence — Q98](/redis-cheatsheet/03-redis-internals/persistence/#when-would-you-disable-persistence-entirely-and-what-failure-modes-remain-accept) |
| 99 | How does min-replicas-to-write protect against write loss during partition events? | Hard | Architect | Reliability | [Replication — Q99](/redis-cheatsheet/03-redis-internals/replication/#how-does-min-replicas-to-write-protect-against-write-loss-during-partition-event) |
| 100 | What is the role of WAIT after a write when clients require stronger durability than async replication? | Hard | Lead | Reliability | [Replication — Q100](/redis-cheatsheet/03-redis-internals/replication/#what-is-the-role-of-wait-after-a-write-when-clients-require-stronger-durability) |
| 101 | How would you design failover testing for Sentinel without corrupting production data? | Hard | Architect | Reliability | [Sentinel — Q101](/redis-cheatsheet/03-redis-internals/sentinel/#how-would-you-design-failover-testing-for-sentinel-without-corrupting-production) |
| 102 | What split-brain scenarios can occur with misconfigured Sentinel quorum? | Hard | Architect | Reliability | [Sentinel — Q102](/redis-cheatsheet/03-redis-internals/sentinel/#what-split-brain-scenarios-can-occur-with-misconfigured-sentinel-quorum) |
| 103 | How do replica-read-only and ACLs combine to prevent accidental writes to secondaries? | Medium | Senior Engineer | Reliability | [Replication — Q103](/redis-cheatsheet/03-redis-internals/replication/#how-do-replica-read-only-and-acls-combine-to-prevent-accidental-writes-to-second) |
| 104 | What happens to in-flight Pub/Sub messages during primary failover? | Medium | Lead | Reliability | [Pub Sub — Q104](/redis-cheatsheet/04-distributed-systems/pub-sub/#what-happens-to-in-flight-pubsub-messages-during-primary-failover) |
| 105 | How do consumer groups provide at-least-once delivery, and what idempotency must apps implement? | Hard | Senior Engineer | Reliability | [Streams — Q105](/redis-cheatsheet/04-distributed-systems/streams/#how-do-consumer-groups-provide-at-least-once-delivery-and-what-idempotency-must) |
| 106 | Why does MULTI/EXEC not provide rollback semantics like a relational transaction? | Medium | Senior Engineer | Reliability | [Transactions — Q106](/redis-cheatsheet/04-distributed-systems/transactions/#why-does-multiexec-not-provide-rollback-semantics-like-a-relational-transaction) |
| 107 | How do fencing tokens prevent stale lock holders from corrupting durable storage? | Hard | Architect | Reliability | [Distributed Lock — Q107](/redis-cheatsheet/04-distributed-systems/distributed-lock/#how-do-fencing-tokens-prevent-stale-lock-holders-from-corrupting-durable-storage) |
| 108 | What correctness gaps remain with SET key token NX PX even when unlock uses Lua? | Hard | Architect | Reliability | [Distributed Lock — Q108](/redis-cheatsheet/04-distributed-systems/distributed-lock/#what-correctness-gaps-remain-with-set-key-token-nx-px-even-when-unlock-uses-lua) |
| 109 | How would you argue for or against Redlock in a multi-datacenter inventory system? | Hard | Architect | Reliability | [Distributed Lock — Q109](/redis-cheatsheet/04-distributed-systems/distributed-lock/#how-would-you-argue-for-or-against-redlock-in-a-multi-datacenter-inventory-syste) |
| 110 | What disaster recovery RPO do you get from hourly RDB plus AOF everysec combined? | Hard | Architect | Reliability | [Persistence — Q110](/redis-cheatsheet/03-redis-internals/persistence/#what-disaster-recovery-rpo-do-you-get-from-hourly-rdb-plus-aof-everysec-combined) |
| 111 | How does Cluster handle primary failure when replicas exist versus when they do not? | Hard | Lead | Reliability | [Cluster — Q111](/redis-cheatsheet/03-redis-internals/cluster/#how-does-cluster-handle-primary-failure-when-replicas-exist-versus-when-they-do) |
| 112 | What reliability risks appear when resharding moves slots during peak traffic? | Hard | Lead | Reliability | [Cluster — Q112](/redis-cheatsheet/03-redis-internals/cluster/#what-reliability-risks-appear-when-resharding-moves-slots-during-peak-traffic) |
| 113 | How do you keep cache and database consistent under write-through versus write-behind? | Hard | Lead | Reliability | [Cache Invalidation — Q113](/redis-cheatsheet/05-production-patterns/cache-invalidation/#how-do-you-keep-cache-and-database-consistent-under-write-through-versus-write-b) |
| 114 | What session durability expectations are realistic when Redis is only a cache? | Medium | Senior Engineer | Reliability | [Session Store — Q114](/redis-cheatsheet/05-production-patterns/session-store/#what-session-durability-expectations-are-realistic-when-redis-is-only-a-cache) |
| 115 | How would you validate backup restores for AOF rewrite corruption edge cases? | Hard | Lead | Reliability | [Persistence — Q115](/redis-cheatsheet/03-redis-internals/persistence/#how-would-you-validate-backup-restores-for-aof-rewrite-corruption-edge-cases) |
| 116 | How do you estimate Redis memory for N keys given average value size and encoding overhead? | Hard | Lead | Scalability | [Capacity Planning — Q116](/redis-cheatsheet/06-performance-operations/capacity-planning/#how-do-you-estimate-redis-memory-for-n-keys-given-average-value-size-and-encodin) |
| 117 | When does adding replicas stop helping read scale because the primary is still the bottleneck? | Hard | Architect | Scalability | [Replication — Q117](/redis-cheatsheet/03-redis-internals/replication/#when-does-adding-replicas-stop-helping-read-scale-because-the-primary-is-still-t) |
| 118 | How many primaries and replicas would you plan for a 500 GB working set with 200k ops/sec? | Hard | Architect | Scalability | [Capacity Planning — Q118](/redis-cheatsheet/06-performance-operations/capacity-planning/#how-many-primaries-and-replicas-would-you-plan-for-a-500-gb-working-set-with-200) |
| 119 | What key design choices cause one Cluster shard to absorb disproportionate traffic? | Hard | Lead | Scalability | [Cache Breakdown — Q119](/redis-cheatsheet/05-production-patterns/cache-breakdown/#what-key-design-choices-cause-one-cluster-shard-to-absorb-disproportionate-traff) |
| 120 | How would you split a hot key across logical shards at the application layer? | Hard | Lead | Scalability | [Cache Breakdown — Q120](/redis-cheatsheet/05-production-patterns/cache-breakdown/#how-would-you-split-a-hot-key-across-logical-shards-at-the-application-layer) |
| 121 | When does horizontal Cluster scaling hit coordination overhead diminishing returns? | Hard | Architect | Scalability | [Cluster — Q121](/redis-cheatsheet/03-redis-internals/cluster/#when-does-horizontal-cluster-scaling-hit-coordination-overhead-diminishing-retur) |
| 122 | How do global rate limit counters scale when a single INCR key becomes hot? | Hard | Lead | Scalability | [Rate Limiter — Q122](/redis-cheatsheet/05-production-patterns/rate-limiter/#how-do-global-rate-limit-counters-scale-when-a-single-incr-key-becomes-hot) |
| 123 | What growth triggers move you from one large instance to Cluster beyond memory alone? | Hard | Architect | Scalability | [Capacity Planning — Q123](/redis-cheatsheet/06-performance-operations/capacity-planning/#what-growth-triggers-move-you-from-one-large-instance-to-cluster-beyond-memory-a) |
| 124 | How does replication factor affect memory and network costs at 10x data growth? | Medium | Lead | Scalability | [Replication — Q124](/redis-cheatsheet/03-redis-internals/replication/#how-does-replication-factor-affect-memory-and-network-costs-at-10x-data-growth) |
| 125 | When do Streams with many consumer groups create memory pressure versus Kafka retention? | Hard | Architect | Scalability | [Redis Vs Kafka — Q125](/redis-cheatsheet/07-comparisons/redis-vs-kafka/#when-do-streams-with-many-consumer-groups-create-memory-pressure-versus-kafka-re) |
| 126 | How would you plan slot migration windows to scale out Cluster without client outages? | Hard | Lead | Scalability | [Cluster — Q126](/redis-cheatsheet/03-redis-internals/cluster/#how-would-you-plan-slot-migration-windows-to-scale-out-cluster-without-client-ou) |
| 127 | What is the scalability ceiling of single-threaded command processing per core? | Medium | Senior Engineer | Scalability | [Architecture — Q127](/redis-cheatsheet/01-fundamentals/architecture/#what-is-the-scalability-ceiling-of-single-threaded-command-processing-per-core) |
| 128 | How do connection counts from thousands of pods affect Redis scalability in Kubernetes? | Hard | Lead | Scalability | [Capacity Planning — Q128](/redis-cheatsheet/06-performance-operations/capacity-planning/#how-do-connection-counts-from-thousands-of-pods-affect-redis-scalability-in-kube) |
| 129 | When does caching null results with short TTL scale better than Bloom filters? | Medium | Senior Engineer | Scalability | [Cache Penetration — Q129](/redis-cheatsheet/05-production-patterns/cache-penetration/#when-does-caching-null-results-with-short-ttl-scale-better-than-bloom-filters) |
| 130 | How would you model year-over-year key growth for finance-approved capacity budgets? | Hard | Architect | Scalability | [Capacity Planning — Q130](/redis-cheatsheet/06-performance-operations/capacity-planning/#how-would-you-model-year-over-year-key-growth-for-finance-approved-capacity-budg) |
| 131 | Walk through cache-aside read and write invalidation for an updated product record. | Medium | Senior Engineer | Patterns | [Caching Patterns — Q131](/redis-cheatsheet/05-production-patterns/caching-patterns/#walk-through-cache-aside-read-and-write-invalidation-for-an-updated-product-reco) |
| 132 | How does write-behind improve write latency while risking data loss on crash? | Hard | Lead | Patterns | [Cache Invalidation — Q132](/redis-cheatsheet/05-production-patterns/cache-invalidation/#how-does-write-behind-improve-write-latency-while-risking-data-loss-on-crash) |
| 133 | What singleflight or lock pattern prevents rebuild stampede on a popular cache miss? | Hard | Lead | Patterns | [Cache Breakdown — Q133](/redis-cheatsheet/05-production-patterns/cache-breakdown/#what-singleflight-or-lock-pattern-prevents-rebuild-stampede-on-a-popular-cache-m) |
| 134 | How would you implement TTL jitter to mitigate synchronized expiry avalanches? | Medium | Senior Engineer | Patterns | [Cache Avalanche — Q134](/redis-cheatsheet/05-production-patterns/cache-avalanche/#how-would-you-implement-ttl-jitter-to-mitigate-synchronized-expiry-avalanches) |
| 135 | When is a Bloom filter worth adding versus caching empty placeholders? | Hard | Lead | Patterns | [Cache Penetration — Q135](/redis-cheatsheet/05-production-patterns/cache-penetration/#when-is-a-bloom-filter-worth-adding-versus-caching-empty-placeholders) |
| 136 | How do you implement a correct distributed lock release with token verification? | Hard | Senior Engineer | Patterns | [Distributed Lock — Q136](/redis-cheatsheet/04-distributed-systems/distributed-lock/#how-do-you-implement-a-correct-distributed-lock-release-with-token-verification) |
| 137 | Why prefer Lua over WATCH/MULTI for contested hot keys? | Hard | Lead | Patterns | [Lua Scripts — Q137](/redis-cheatsheet/04-distributed-systems/lua-scripts/#why-prefer-lua-over-watchmulti-for-contested-hot-keys) |
| 138 | How does XREADGROUP BLOCK behave differently from BLPOP for worker pools? | Medium | Senior Engineer | Patterns | [Streams — Q138](/redis-cheatsheet/04-distributed-systems/streams/#how-does-xreadgroup-block-behave-differently-from-blpop-for-worker-pools) |
| 139 | What is the recovery procedure for poison messages stuck in XPENDING? | Hard | Lead | Patterns | [Streams — Q139](/redis-cheatsheet/04-distributed-systems/streams/#what-is-the-recovery-procedure-for-poison-messages-stuck-in-xpending) |
| 140 | How would you choose fixed-window versus sliding-window rate limits for an API gateway? | Medium | Senior Engineer | Patterns | [Rate Limiter — Q140](/redis-cheatsheet/05-production-patterns/rate-limiter/#how-would-you-choose-fixed-window-versus-sliding-window-rate-limits-for-an-api-g) |
| 141 | What session fields belong in Redis versus only in signed cookies? | Medium | Senior Engineer | Patterns | [Session Store — Q141](/redis-cheatsheet/05-production-patterns/session-store/#what-session-fields-belong-in-redis-versus-only-in-signed-cookies) |
| 142 | How does Pub/Sub-based cache invalidation avoid stale local caches in multi-tier apps? | Medium | Lead | Patterns | [Cache Invalidation — Q142](/redis-cheatsheet/05-production-patterns/cache-invalidation/#how-does-pubsub-based-cache-invalidation-avoid-stale-local-caches-in-multi-tier) |
| 143 | When should lists be retired in favor of Streams for work queues? | Medium | Senior Engineer | Patterns | [Lists — Q143](/redis-cheatsheet/02-core-redis/lists/#when-should-lists-be-retired-in-favor-of-streams-for-work-queues) |
| 144 | How do hash tags enable atomic multi-key updates in Cluster for order line items? | Hard | Lead | Patterns | [Cluster — Q144](/redis-cheatsheet/03-redis-internals/cluster/#how-do-hash-tags-enable-atomic-multi-key-updates-in-cluster-for-order-line-items) |
| 145 | What pipeline patterns reduce round trips in bulk session refresh jobs? | Medium | Senior Engineer | Patterns | [Performance Tuning — Q145](/redis-cheatsheet/06-performance-operations/performance-tuning/#what-pipeline-patterns-reduce-round-trips-in-bulk-session-refresh-jobs) |
| 146 | How would you implement a token bucket refill accurately with Lua? | Hard | Senior Engineer | Patterns | [Lua Scripts — Q146](/redis-cheatsheet/04-distributed-systems/lua-scripts/#how-would-you-implement-a-token-bucket-refill-accurately-with-lua) |
| 147 | What are the tradeoffs of caching entire DTOs versus hash field projections? | Medium | Lead | Patterns | [Hashes — Q147](/redis-cheatsheet/02-core-redis/hashes/#what-are-the-tradeoffs-of-caching-entire-dtos-versus-hash-field-projections) |
| 148 | How do you prevent double consumption when a consumer crashes before XACK? | Hard | Lead | Patterns | [Streams — Q148](/redis-cheatsheet/04-distributed-systems/streams/#how-do-you-prevent-double-consumption-when-a-consumer-crashes-before-xack) |
| 149 | When does Redis Pub/Sub suffice for feature-flag propagation versus polling? | Easy | Senior Engineer | Patterns | [Pub Sub — Q149](/redis-cheatsheet/04-distributed-systems/pub-sub/#when-does-redis-pubsub-suffice-for-feature-flag-propagation-versus-polling) |
| 150 | How would you design negative caching TTL differently for bots versus real users? | Hard | Lead | Patterns | [Cache Penetration — Q150](/redis-cheatsheet/05-production-patterns/cache-penetration/#how-would-you-design-negative-caching-ttl-differently-for-bots-versus-real-users) |


---


---

<!-- interview-guide-answers:start -->

## Answers

### Q1. Why does Redis use a single-threaded command execution model, and when do I/O threads change that picture?

### Short Answer
The production-grade Redis answer is using MULTI/EXEC for simple atomic batches and Lua for contested hot keys where WATCH abort rates would be high for: Why does Redis use a single-threaded command execution model, and when do I/O threads change that picture.

### Detailed Explanation
MULTI queues commands; EXEC runs them serially without interleaving — failed commands do not roll back earlier commands in the batch for: Why does Redis use a single-threaded command execution model, and when do I/O threads change that picture.

### Internal Working
WATCH provides optimistic locking by aborting EXEC if watched keys changed; pipelines batch without atomicity for: Why does Redis use a single-threaded command execution model, and when do I/O threads change that picture.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by keeping transaction blocks short and preferring Lua for compare-and-set on hot keys for: Why does Redis use a single-threaded command execution model, and when do I/O threads change that picture.

### Common Mistakes
Expecting RDBMS-style rollback or long MULTI blocks on hot keys are common production mistakes for: Why does Redis use a single-threaded command execution model, and when do I/O threads change that picture.

### Follow-up Questions
When would Lua replace MULTI/EXEC for: Why does Redis use a single-threaded command execution model, and when do I/O threads change that picture, and what cluster slot constraints apply?

---
### Q2. How would you choose between standalone Redis, Sentinel, and Cluster for a new payment-adjacent cache?

### Short Answer
The senior-level decision is deploying an odd number of sentinels with quorum tuned to avoid flapping while enabling automatic failover for: How would you choose between standalone Redis, Sentinel, and Cluster for a new payment-adjacent cache.

### Detailed Explanation
Sentinel marks subjective/objective down states, elects a new primary, and re-points replicas — clients must discover the new primary via Sentinel-aware drivers for: How would you choose between standalone Redis, Sentinel, and Cluster for a new payment-adjacent cache.

### Internal Working
Failover promotes a replica with `REPLICAOF NO ONE` then reconfigures the fleet; brief write unavailability and client reconnect storms are expected for: How would you choose between standalone Redis, Sentinel, and Cluster for a new payment-adjacent cache.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by running game-day failover tests with connection pool refresh metrics for: How would you choose between standalone Redis, Sentinel, and Cluster for a new payment-adjacent cache.

### Common Mistakes
Split-brain risk rises with even sentinel counts, stale client caches, and missing `min-replicas-to-write` guards for: How would you choose between standalone Redis, Sentinel, and Cluster for a new payment-adjacent cache.

### Follow-up Questions
What quorum and `down-after-milliseconds` values would you defend in an ADR for: How would you choose between standalone Redis, Sentinel, and Cluster for a new payment-adjacent cache?

---
### Q3. What architectural role does Redis play when it is cache versus when it is the primary data store?

### Short Answer
The practical Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: What architectural role does Redis play when it is cache versus when it is the primary data store.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: What architectural role does Redis play when it is cache versus when it is the primary data store.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: What architectural role does Redis play when it is cache versus when it is the primary data store.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by documenting ADR assumptions and exit strategy if load doubles for: What architectural role does Redis play when it is cache versus when it is the primary data store.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: What architectural role does Redis play when it is cache versus when it is the primary data store.

### Follow-up Questions
What requirement in: What architectural role does Redis play when it is cache versus when it is the primary data store is decisive if throughput numbers are similar across options?

---
### Q4. How does the global keyspace dictionary influence hot-key and big-key failure modes at scale?

### Short Answer
For this question, the architecturally correct Redis answer is matching Redis data type to access pattern — not defaulting everything to JSON strings for: How does the global keyspace dictionary influence hot-key and big-key failure modes at scale.

### Detailed Explanation
Pick strings for counters/cache blobs, hashes for field updates, sets/ZSETs for uniqueness/ranking, Streams for durable queues for: How does the global keyspace dictionary influence hot-key and big-key failure modes at scale.

### Internal Working
Encoding upgrades and command complexity (O(N) vs O(1)) follow from type and size choices for: How does the global keyspace dictionary influence hot-key and big-key failure modes at scale.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by validating command complexity and memory per key for: How does the global keyspace dictionary influence hot-key and big-key failure modes at scale.

### Common Mistakes
Using `HGETALL` or `SMEMBERS` on large collections blocks the event loop for: How does the global keyspace dictionary influence hot-key and big-key failure modes at scale.

### Follow-up Questions
Which type would you choose for: How does the global keyspace dictionary influence hot-key and big-key failure modes at scale, and what command path proves it under peak cardinality?

---
### Q5. When would you shard with Redis Cluster instead of vertical scaling a single primary?

### Short Answer
The production-grade Redis answer is designing keys around 16384 hash slots, hash tags for multi-key ops, and cluster-aware clients for: When would you shard with Redis Cluster instead of vertical scaling a single primary.

### Detailed Explanation
Slot = CRC16(key) mod 16384; MOVED is permanent redirect, ASK is temporary during migration — resharding moves slot ownership without changing key names for: When would you shard with Redis Cluster instead of vertical scaling a single primary.

### Internal Working
Multi-key commands, Lua, and transactions require all keys in the same slot — `{tag}` hash tags force colocation for: When would you shard with Redis Cluster instead of vertical scaling a single primary.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by monitoring per-node ops/sec, slot distribution, and MOVED/ASK rates during: When would you shard with Redis Cluster instead of vertical scaling a single primary.

### Common Mistakes
Typical failures: non-cluster clients, cross-slot MGET, and hot slots from poor key choice for: When would you shard with Redis Cluster instead of vertical scaling a single primary.

### Follow-up Questions
How would you rebalance slots or split hot keys if: When would you shard with Redis Cluster instead of vertical scaling a single primary appears in production metrics?

---
### Q6. How do hash tags change your key design when you need multi-key atomicity in Cluster?

### Short Answer
The senior-level decision is using MULTI/EXEC for simple atomic batches and Lua for contested hot keys where WATCH abort rates would be high for: How do hash tags change your key design when you need multi-key atomicity in Cluster.

### Detailed Explanation
MULTI queues commands; EXEC runs them serially without interleaving — failed commands do not roll back earlier commands in the batch for: How do hash tags change your key design when you need multi-key atomicity in Cluster.

### Internal Working
WATCH provides optimistic locking by aborting EXEC if watched keys changed; pipelines batch without atomicity for: How do hash tags change your key design when you need multi-key atomicity in Cluster.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by keeping transaction blocks short and preferring Lua for compare-and-set on hot keys for: How do hash tags change your key design when you need multi-key atomicity in Cluster.

### Common Mistakes
Expecting RDBMS-style rollback or long MULTI blocks on hot keys are common production mistakes for: How do hash tags change your key design when you need multi-key atomicity in Cluster.

### Follow-up Questions
When would Lua replace MULTI/EXEC for: How do hash tags change your key design when you need multi-key atomicity in Cluster, and what cluster slot constraints apply?

---
### Q7. What is the mental model for 16384 hash slots, and why not more or fewer?

### Short Answer
The practical Redis answer is designing keys around 16384 hash slots, hash tags for multi-key ops, and cluster-aware clients for: What is the mental model for 16384 hash slots, and why not more or fewer.

### Detailed Explanation
Slot = CRC16(key) mod 16384; MOVED is permanent redirect, ASK is temporary during migration — resharding moves slot ownership without changing key names for: What is the mental model for 16384 hash slots, and why not more or fewer.

### Internal Working
Multi-key commands, Lua, and transactions require all keys in the same slot — `{tag}` hash tags force colocation for: What is the mental model for 16384 hash slots, and why not more or fewer.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by monitoring per-node ops/sec, slot distribution, and MOVED/ASK rates during: What is the mental model for 16384 hash slots, and why not more or fewer.

### Common Mistakes
Typical failures: non-cluster clients, cross-slot MGET, and hot slots from poor key choice for: What is the mental model for 16384 hash slots, and why not more or fewer.

### Follow-up Questions
How would you rebalance slots or split hot keys if: What is the mental model for 16384 hash slots, and why not more or fewer appears in production metrics?

---
### Q8. How do MOVED and ASK redirects differ in client architecture during normal ops versus resharding?

### Short Answer
For this question, the architecturally correct Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: How do MOVED and ASK redirects differ in client architecture during normal ops versus resharding.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: How do MOVED and ASK redirects differ in client architecture during normal ops versus resharding.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: How do MOVED and ASK redirects differ in client architecture during normal ops versus resharding.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by documenting ADR assumptions and exit strategy if load doubles for: How do MOVED and ASK redirects differ in client architecture during normal ops versus resharding.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: How do MOVED and ASK redirects differ in client architecture during normal ops versus resharding.

### Follow-up Questions
What requirement in: How do MOVED and ASK redirects differ in client architecture during normal ops versus resharding is decisive if throughput numbers are similar across options?

---
### Q9. When is Sentinel the right HA layer versus managed cloud failover you do not operate?

### Short Answer
The production-grade Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: When is Sentinel the right HA layer versus managed cloud failover you do not operate.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: When is Sentinel the right HA layer versus managed cloud failover you do not operate.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: When is Sentinel the right HA layer versus managed cloud failover you do not operate.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by documenting ADR assumptions and exit strategy if load doubles for: When is Sentinel the right HA layer versus managed cloud failover you do not operate.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: When is Sentinel the right HA layer versus managed cloud failover you do not operate.

### Follow-up Questions
What requirement in: When is Sentinel the right HA layer versus managed cloud failover you do not operate is decisive if throughput numbers are similar across options?

---
### Q10. How would you diagram request flow from application through connection pool to Redis command thread?

### Short Answer
The senior-level decision is matching Redis data type to access pattern — not defaulting everything to JSON strings for: How would you diagram request flow from application through connection pool to Redis command thread.

### Detailed Explanation
Pick strings for counters/cache blobs, hashes for field updates, sets/ZSETs for uniqueness/ranking, Streams for durable queues for: How would you diagram request flow from application through connection pool to Redis command thread.

### Internal Working
Encoding upgrades and command complexity (O(N) vs O(1)) follow from type and size choices for: How would you diagram request flow from application through connection pool to Redis command thread.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by validating command complexity and memory per key for: How would you diagram request flow from application through connection pool to Redis command thread.

### Common Mistakes
Using `HGETALL` or `SMEMBERS` on large collections blocks the event loop for: How would you diagram request flow from application through connection pool to Redis command thread.

### Follow-up Questions
Which type would you choose for: How would you diagram request flow from application through connection pool to Redis command thread, and what command path proves it under peak cardinality?

---
### Q11. What data type would you pick for a user profile with frequent single-field updates, and why not a JSON string?

### Short Answer
The practical Redis answer is matching Redis data type to access pattern — not defaulting everything to JSON strings for: What data type would you pick for a user profile with frequent single-field updates, and why not a JSON string.

### Detailed Explanation
Pick strings for counters/cache blobs, hashes for field updates, sets/ZSETs for uniqueness/ranking, Streams for durable queues for: What data type would you pick for a user profile with frequent single-field updates, and why not a JSON string.

### Internal Working
Encoding upgrades and command complexity (O(N) vs O(1)) follow from type and size choices for: What data type would you pick for a user profile with frequent single-field updates, and why not a JSON string.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by validating command complexity and memory per key for: What data type would you pick for a user profile with frequent single-field updates, and why not a JSON string.

### Common Mistakes
Using `HGETALL` or `SMEMBERS` on large collections blocks the event loop for: What data type would you pick for a user profile with frequent single-field updates, and why not a JSON string.

### Follow-up Questions
Which type would you choose for: What data type would you pick for a user profile with frequent single-field updates, and why not a JSON string, and what command path proves it under peak cardinality?

---
### Q12. When are Redis Streams architecturally appropriate versus an external log like Kafka?

### Short Answer
For this question, the architecturally correct Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: When are Redis Streams architecturally appropriate versus an external log like Kafka.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: When are Redis Streams architecturally appropriate versus an external log like Kafka.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: When are Redis Streams architecturally appropriate versus an external log like Kafka.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by documenting ADR assumptions and exit strategy if load doubles for: When are Redis Streams architecturally appropriate versus an external log like Kafka.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: When are Redis Streams architecturally appropriate versus an external log like Kafka.

### Follow-up Questions
What requirement in: When are Redis Streams architecturally appropriate versus an external log like Kafka is decisive if throughput numbers are similar across options?

---
### Q13. When are Redis lists or Streams appropriate versus RabbitMQ for task distribution?

### Short Answer
The production-grade Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: When are Redis lists or Streams appropriate versus RabbitMQ for task distribution.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: When are Redis lists or Streams appropriate versus RabbitMQ for task distribution.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: When are Redis lists or Streams appropriate versus RabbitMQ for task distribution.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by documenting ADR assumptions and exit strategy if load doubles for: When are Redis lists or Streams appropriate versus RabbitMQ for task distribution.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: When are Redis lists or Streams appropriate versus RabbitMQ for task distribution.

### Follow-up Questions
What requirement in: When are Redis lists or Streams appropriate versus RabbitMQ for task distribution is decisive if throughput numbers are similar across options?

---
### Q14. How does Pub/Sub fit into cache invalidation architecture without becoming a system of record?

### Short Answer
The senior-level decision is deleting or updating cache keys on write and broadcasting invalidation when multi-tier caches exist for: How does Pub/Sub fit into cache invalidation architecture without becoming a system of record.

### Detailed Explanation
Write-through updates DB and cache together; write-behind updates cache first with async flush — each shifts consistency risk for: How does Pub/Sub fit into cache invalidation architecture without becoming a system of record.

### Internal Working
Pub/Sub can signal app-local cache eviction, but Redis remains source for shared cache layer for: How does Pub/Sub fit into cache invalidation architecture without becoming a system of record.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by defining who invalidates on partial updates and out-of-order writes for: How does Pub/Sub fit into cache invalidation architecture without becoming a system of record.

### Common Mistakes
Updating DB without cache delete is the most common stale-data bug for: How does Pub/Sub fit into cache invalidation architecture without becoming a system of record.

### Follow-up Questions
How do you invalidate related keys (lists, aggregates) when: How does Pub/Sub fit into cache invalidation architecture without becoming a system of record updates one entity?

---
### Q15. What tradeoffs does Redis offer versus Memcached for a pure session cache layer?

### Short Answer
The practical Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: What tradeoffs does Redis offer versus Memcached for a pure session cache layer.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: What tradeoffs does Redis offer versus Memcached for a pure session cache layer.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: What tradeoffs does Redis offer versus Memcached for a pure session cache layer.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by documenting ADR assumptions and exit strategy if load doubles for: What tradeoffs does Redis offer versus Memcached for a pure session cache layer.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: What tradeoffs does Redis offer versus Memcached for a pure session cache layer.

### Follow-up Questions
What requirement in: What tradeoffs does Redis offer versus Memcached for a pure session cache layer is decisive if throughput numbers are similar across options?

---
### Q16. How would you isolate tenant traffic on a shared Redis cluster without cross-tenant key collisions?

### Short Answer
For this question, the architecturally correct Redis answer is designing keys around 16384 hash slots, hash tags for multi-key ops, and cluster-aware clients for: How would you isolate tenant traffic on a shared Redis cluster without cross-tenant key collisions.

### Detailed Explanation
Slot = CRC16(key) mod 16384; MOVED is permanent redirect, ASK is temporary during migration — resharding moves slot ownership without changing key names for: How would you isolate tenant traffic on a shared Redis cluster without cross-tenant key collisions.

### Internal Working
Multi-key commands, Lua, and transactions require all keys in the same slot — `{tag}` hash tags force colocation for: How would you isolate tenant traffic on a shared Redis cluster without cross-tenant key collisions.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by monitoring per-node ops/sec, slot distribution, and MOVED/ASK rates during: How would you isolate tenant traffic on a shared Redis cluster without cross-tenant key collisions.

### Common Mistakes
Typical failures: non-cluster clients, cross-slot MGET, and hot slots from poor key choice for: How would you isolate tenant traffic on a shared Redis cluster without cross-tenant key collisions.

### Follow-up Questions
How would you rebalance slots or split hot keys if: How would you isolate tenant traffic on a shared Redis cluster without cross-tenant key collisions appears in production metrics?

---
### Q17. When do Redis modules (RedisJSON, RediSearch) change your storage architecture versus plain hashes?

### Short Answer
The production-grade Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: When do Redis modules (RedisJSON, RediSearch) change your storage architecture versus plain hashes.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: When do Redis modules (RedisJSON, RediSearch) change your storage architecture versus plain hashes.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: When do Redis modules (RedisJSON, RediSearch) change your storage architecture versus plain hashes.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by documenting ADR assumptions and exit strategy if load doubles for: When do Redis modules (RedisJSON, RediSearch) change your storage architecture versus plain hashes.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: When do Redis modules (RedisJSON, RediSearch) change your storage architecture versus plain hashes.

### Follow-up Questions
What requirement in: When do Redis modules (RedisJSON, RediSearch) change your storage architecture versus plain hashes is decisive if throughput numbers are similar across options?

---
### Q18. How does TTL-at-key-level architecture affect session design versus field-level expiry needs?

### Short Answer
The senior-level decision is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: How does TTL-at-key-level architecture affect session design versus field-level expiry needs.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: How does TTL-at-key-level architecture affect session design versus field-level expiry needs.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: How does TTL-at-key-level architecture affect session design versus field-level expiry needs.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by documenting ADR assumptions and exit strategy if load doubles for: How does TTL-at-key-level architecture affect session design versus field-level expiry needs.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: How does TTL-at-key-level architecture affect session design versus field-level expiry needs.

### Follow-up Questions
What requirement in: How does TTL-at-key-level architecture affect session design versus field-level expiry needs is decisive if throughput numbers are similar across options?

---
### Q19. What signals indicate a workload has outgrown a single primary before ops teams admit it?

### Short Answer
The practical Redis answer is matching Redis data type to access pattern — not defaulting everything to JSON strings for: What signals indicate a workload has outgrown a single primary before ops teams admit it.

### Detailed Explanation
Pick strings for counters/cache blobs, hashes for field updates, sets/ZSETs for uniqueness/ranking, Streams for durable queues for: What signals indicate a workload has outgrown a single primary before ops teams admit it.

### Internal Working
Encoding upgrades and command complexity (O(N) vs O(1)) follow from type and size choices for: What signals indicate a workload has outgrown a single primary before ops teams admit it.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by validating command complexity and memory per key for: What signals indicate a workload has outgrown a single primary before ops teams admit it.

### Common Mistakes
Using `HGETALL` or `SMEMBERS` on large collections blocks the event loop for: What signals indicate a workload has outgrown a single primary before ops teams admit it.

### Follow-up Questions
Which type would you choose for: What signals indicate a workload has outgrown a single primary before ops teams admit it, and what command path proves it under peak cardinality?

---
### Q20. How would you place Redis relative to the database in a read-heavy catalog service?

### Short Answer
For this question, the architecturally correct Redis answer is matching Redis data type to access pattern — not defaulting everything to JSON strings for: How would you place Redis relative to the database in a read-heavy catalog service.

### Detailed Explanation
Pick strings for counters/cache blobs, hashes for field updates, sets/ZSETs for uniqueness/ranking, Streams for durable queues for: How would you place Redis relative to the database in a read-heavy catalog service.

### Internal Working
Encoding upgrades and command complexity (O(N) vs O(1)) follow from type and size choices for: How would you place Redis relative to the database in a read-heavy catalog service.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by validating command complexity and memory per key for: How would you place Redis relative to the database in a read-heavy catalog service.

### Common Mistakes
Using `HGETALL` or `SMEMBERS` on large collections blocks the event loop for: How would you place Redis relative to the database in a read-heavy catalog service.

### Follow-up Questions
Which type would you choose for: How would you place Redis relative to the database in a read-heavy catalog service, and what command path proves it under peak cardinality?

---
### Q21. When is replica read scaling architecturally safe, and when does it violate freshness requirements?

### Short Answer
The production-grade Redis answer is treating replication as async by default and using `WAIT` or app-level checks only when stronger durability is required for: When is replica read scaling architecturally safe, and when does it violate freshness requirements.

### Detailed Explanation
Replicas tail the replication stream; lag appears when network, disk, or apply speed falls behind write rate — partial resync needs adequate `repl-backlog-size` for: When is replica read scaling architecturally safe, and when does it violate freshness requirements.

### Internal Working
Read-your-writes is not automatic on replicas; clients using replica reads must accept staleness or use primary reads after writes for: When is replica read scaling architecturally safe, and when does it violate freshness requirements.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by correlating `master_repl_offset` with replica offsets and write spikes for: When is replica read scaling architecturally safe, and when does it violate freshness requirements.

### Common Mistakes
Common mistakes include writable replicas, ignoring lag during incidents, and assuming replica reads are fresh for: When is replica read scaling architecturally safe, and when does it violate freshness requirements.

### Follow-up Questions
Which writes in: When is replica read scaling architecturally safe, and when does it violate freshness requirements require synchronous acknowledgment, and how will clients handle failover mid-transaction?

---
### Q22. How do persistence settings change the architecture story when Redis is marketed as a cache only?

### Short Answer
The senior-level decision is matching RDB/AOF hybrid settings to acceptable data-loss window and restart time for: How do persistence settings change the architecture story when Redis is marketed as a cache only.

### Detailed Explanation
RDB gives compact snapshots; AOF gives finer durability with `appendfsync` tradeoffs — `everysec` is common but can lose ~1s on crash for: How do persistence settings change the architecture story when Redis is marketed as a cache only.

### Internal Working
BGSAVE/AOF rewrite forks the process; copy-on-write can double memory pressure during snapshots, affecting latency for: How do persistence settings change the architecture story when Redis is marketed as a cache only.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by testing crash-recovery drills and measuring fork latency under peak write load for: How do persistence settings change the architecture story when Redis is marketed as a cache only.

### Common Mistakes
Dangerous patterns include `SAVE` in production, `appendfsync always` without throughput headroom, and ignoring COW during maintenance for: How do persistence settings change the architecture story when Redis is marketed as a cache only.

### Follow-up Questions
What RPO does your chosen persistence mode actually guarantee for: How do persistence settings change the architecture story when Redis is marketed as a cache only after a hard kill test?

---
### Q23. What is the architectural impact of running Redis in Kubernetes with ephemeral versus persistent volumes?

### Short Answer
The practical Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: What is the architectural impact of running Redis in Kubernetes with ephemeral versus persistent volumes.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: What is the architectural impact of running Redis in Kubernetes with ephemeral versus persistent volumes.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: What is the architectural impact of running Redis in Kubernetes with ephemeral versus persistent volumes.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by documenting ADR assumptions and exit strategy if load doubles for: What is the architectural impact of running Redis in Kubernetes with ephemeral versus persistent volumes.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: What is the architectural impact of running Redis in Kubernetes with ephemeral versus persistent volumes.

### Follow-up Questions
What requirement in: What is the architectural impact of running Redis in Kubernetes with ephemeral versus persistent volumes is decisive if throughput numbers are similar across options?

---
### Q24. How would you design key namespaces for microservices sharing one cluster without coupling?

### Short Answer
For this question, the architecturally correct Redis answer is designing keys around 16384 hash slots, hash tags for multi-key ops, and cluster-aware clients for: How would you design key namespaces for microservices sharing one cluster without coupling.

### Detailed Explanation
Slot = CRC16(key) mod 16384; MOVED is permanent redirect, ASK is temporary during migration — resharding moves slot ownership without changing key names for: How would you design key namespaces for microservices sharing one cluster without coupling.

### Internal Working
Multi-key commands, Lua, and transactions require all keys in the same slot — `{tag}` hash tags force colocation for: How would you design key namespaces for microservices sharing one cluster without coupling.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by monitoring per-node ops/sec, slot distribution, and MOVED/ASK rates during: How would you design key namespaces for microservices sharing one cluster without coupling.

### Common Mistakes
Typical failures: non-cluster clients, cross-slot MGET, and hot slots from poor key choice for: How would you design key namespaces for microservices sharing one cluster without coupling.

### Follow-up Questions
How would you rebalance slots or split hot keys if: How would you design key namespaces for microservices sharing one cluster without coupling appears in production metrics?

---
### Q25. When does colocating rate limiting, sessions, and entity cache in one cluster create blast-radius risk?

### Short Answer
The production-grade Redis answer is designing keys around 16384 hash slots, hash tags for multi-key ops, and cluster-aware clients for: When does colocating rate limiting, sessions, and entity cache in one cluster create blast-radius risk.

### Detailed Explanation
Slot = CRC16(key) mod 16384; MOVED is permanent redirect, ASK is temporary during migration — resharding moves slot ownership without changing key names for: When does colocating rate limiting, sessions, and entity cache in one cluster create blast-radius risk.

### Internal Working
Multi-key commands, Lua, and transactions require all keys in the same slot — `{tag}` hash tags force colocation for: When does colocating rate limiting, sessions, and entity cache in one cluster create blast-radius risk.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by monitoring per-node ops/sec, slot distribution, and MOVED/ASK rates during: When does colocating rate limiting, sessions, and entity cache in one cluster create blast-radius risk.

### Common Mistakes
Typical failures: non-cluster clients, cross-slot MGET, and hot slots from poor key choice for: When does colocating rate limiting, sessions, and entity cache in one cluster create blast-radius risk.

### Follow-up Questions
How would you rebalance slots or split hot keys if: When does colocating rate limiting, sessions, and entity cache in one cluster create blast-radius risk appears in production metrics?

---
### Q26. How does active-active multi-region Redis differ architecturally from single-region Cluster plus replication?

### Short Answer
The senior-level decision is using MULTI/EXEC for simple atomic batches and Lua for contested hot keys where WATCH abort rates would be high for: How does active-active multi-region Redis differ architecturally from single-region Cluster plus replication.

### Detailed Explanation
MULTI queues commands; EXEC runs them serially without interleaving — failed commands do not roll back earlier commands in the batch for: How does active-active multi-region Redis differ architecturally from single-region Cluster plus replication.

### Internal Working
WATCH provides optimistic locking by aborting EXEC if watched keys changed; pipelines batch without atomicity for: How does active-active multi-region Redis differ architecturally from single-region Cluster plus replication.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by keeping transaction blocks short and preferring Lua for compare-and-set on hot keys for: How does active-active multi-region Redis differ architecturally from single-region Cluster plus replication.

### Common Mistakes
Expecting RDBMS-style rollback or long MULTI blocks on hot keys are common production mistakes for: How does active-active multi-region Redis differ architecturally from single-region Cluster plus replication.

### Follow-up Questions
When would Lua replace MULTI/EXEC for: How does active-active multi-region Redis differ architecturally from single-region Cluster plus replication, and what cluster slot constraints apply?

---
### Q27. What client topology changes when applications must be Sentinel-aware versus Cluster-aware?

### Short Answer
The practical Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: What client topology changes when applications must be Sentinel-aware versus Cluster-aware.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: What client topology changes when applications must be Sentinel-aware versus Cluster-aware.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: What client topology changes when applications must be Sentinel-aware versus Cluster-aware.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by documenting ADR assumptions and exit strategy if load doubles for: What client topology changes when applications must be Sentinel-aware versus Cluster-aware.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: What client topology changes when applications must be Sentinel-aware versus Cluster-aware.

### Follow-up Questions
What requirement in: What client topology changes when applications must be Sentinel-aware versus Cluster-aware is decisive if throughput numbers are similar across options?

---
### Q28. How would you justify Redis as a delay queue using sorted sets versus a dedicated scheduler?

### Short Answer
For this question, the architecturally correct Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: How would you justify Redis as a delay queue using sorted sets versus a dedicated scheduler.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: How would you justify Redis as a delay queue using sorted sets versus a dedicated scheduler.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: How would you justify Redis as a delay queue using sorted sets versus a dedicated scheduler.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by documenting ADR assumptions and exit strategy if load doubles for: How would you justify Redis as a delay queue using sorted sets versus a dedicated scheduler.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: How would you justify Redis as a delay queue using sorted sets versus a dedicated scheduler.

### Follow-up Questions
What requirement in: How would you justify Redis as a delay queue using sorted sets versus a dedicated scheduler is decisive if throughput numbers are similar across options?

---
### Q29. When is HyperLogLog the correct architectural choice for analytics versus sets or bitmaps?

### Short Answer
The production-grade Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: When is HyperLogLog the correct architectural choice for analytics versus sets or bitmaps.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: When is HyperLogLog the correct architectural choice for analytics versus sets or bitmaps.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: When is HyperLogLog the correct architectural choice for analytics versus sets or bitmaps.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by documenting ADR assumptions and exit strategy if load doubles for: When is HyperLogLog the correct architectural choice for analytics versus sets or bitmaps.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: When is HyperLogLog the correct architectural choice for analytics versus sets or bitmaps.

### Follow-up Questions
What requirement in: When is HyperLogLog the correct architectural choice for analytics versus sets or bitmaps is decisive if throughput numbers are similar across options?

---
### Q30. How do Lua scripts affect your architecture for atomic inventory decrements?

### Short Answer
The senior-level decision is keeping Lua scripts short, deterministic, and slot-safe in Cluster for atomic server-side logic for: How do Lua scripts affect your architecture for atomic inventory decrements.

### Detailed Explanation
Scripts run atomically — no other commands interleave — making them ideal for compare-and-set, rate limits, and safe unlock for: How do Lua scripts affect your architecture for atomic inventory decrements.

### Internal Working
Non-deterministic calls are restricted; all KEYS must hash to the same slot in Cluster for: How do Lua scripts affect your architecture for atomic inventory decrements.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by preloading with SCRIPT LOAD and monitoring slowlog for long scripts for: How do Lua scripts affect your architecture for atomic inventory decrements.

### Common Mistakes
Long Lua blocks the entire server — avoid O(N) loops and unbounded logic for: How do Lua scripts affect your architecture for atomic inventory decrements.

### Follow-up Questions
How do you version and deploy script changes safely for: How do Lua scripts affect your architecture for atomic inventory decrements across rolling restarts?

---
### Q31. What architecture pitfalls appear when using Redis transactions across many hot keys?

### Short Answer
The practical Redis answer is combining TTL jitter, singleflight locks, and stale-while-revalidate to protect origin during: What architecture pitfalls appear when using Redis transactions across many hot keys.

### Detailed Explanation
Breakdown hits when a hot key expires; avalanche when many keys expire together; penetration when misses flood DB for absent keys for: What architecture pitfalls appear when using Redis transactions across many hot keys.

### Internal Working
Mitigations include probabilistic early refresh, Bloom filters or short negative TTL, and request coalescing for: What architecture pitfalls appear when using Redis transactions across many hot keys.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by load-testing synchronized expiry and hot-key miss scenarios for: What architecture pitfalls appear when using Redis transactions across many hot keys.

### Common Mistakes
Same TTL on all keys and caching null forever are classic self-inflicted outages for: What architecture pitfalls appear when using Redis transactions across many hot keys.

### Follow-up Questions
Which mitigation layer (jitter, lock, Bloom, local cache) is first-line for: What architecture pitfalls appear when using Redis transactions across many hot keys in your architecture?

---
### Q32. How would you blueprint replica count and sentinel quorum in an ADR for 99.95% cache availability?

### Short Answer
For this question, the architecturally correct Redis answer is treating replication as async by default and using `WAIT` or app-level checks only when stronger durability is required for: How would you blueprint replica count and sentinel quorum in an ADR for 99.95% cache availability.

### Detailed Explanation
Replicas tail the replication stream; lag appears when network, disk, or apply speed falls behind write rate — partial resync needs adequate `repl-backlog-size` for: How would you blueprint replica count and sentinel quorum in an ADR for 99.95% cache availability.

### Internal Working
Read-your-writes is not automatic on replicas; clients using replica reads must accept staleness or use primary reads after writes for: How would you blueprint replica count and sentinel quorum in an ADR for 99.95% cache availability.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by correlating `master_repl_offset` with replica offsets and write spikes for: How would you blueprint replica count and sentinel quorum in an ADR for 99.95% cache availability.

### Common Mistakes
Common mistakes include writable replicas, ignoring lag during incidents, and assuming replica reads are fresh for: How would you blueprint replica count and sentinel quorum in an ADR for 99.95% cache availability.

### Follow-up Questions
Which writes in: How would you blueprint replica count and sentinel quorum in an ADR for 99.95% cache availability require synchronous acknowledgment, and how will clients handle failover mid-transaction?

---
### Q33. When does TLS termination at proxy versus Redis native TLS change trust boundaries?

### Short Answer
The production-grade Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: When does TLS termination at proxy versus Redis native TLS change trust boundaries.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: When does TLS termination at proxy versus Redis native TLS change trust boundaries.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: When does TLS termination at proxy versus Redis native TLS change trust boundaries.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by documenting ADR assumptions and exit strategy if load doubles for: When does TLS termination at proxy versus Redis native TLS change trust boundaries.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: When does TLS termination at proxy versus Redis native TLS change trust boundaries.

### Follow-up Questions
What requirement in: When does TLS termination at proxy versus Redis native TLS change trust boundaries is decisive if throughput numbers are similar across options?

---
### Q34. How does connection pooling architecture prevent thundering herd on Redis reconnect after failover?

### Short Answer
The senior-level decision is combining TTL jitter, singleflight locks, and stale-while-revalidate to protect origin during: How does connection pooling architecture prevent thundering herd on Redis reconnect after failover.

### Detailed Explanation
Breakdown hits when a hot key expires; avalanche when many keys expire together; penetration when misses flood DB for absent keys for: How does connection pooling architecture prevent thundering herd on Redis reconnect after failover.

### Internal Working
Mitigations include probabilistic early refresh, Bloom filters or short negative TTL, and request coalescing for: How does connection pooling architecture prevent thundering herd on Redis reconnect after failover.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by load-testing synchronized expiry and hot-key miss scenarios for: How does connection pooling architecture prevent thundering herd on Redis reconnect after failover.

### Common Mistakes
Same TTL on all keys and caching null forever are classic self-inflicted outages for: How does connection pooling architecture prevent thundering herd on Redis reconnect after failover.

### Follow-up Questions
Which mitigation layer (jitter, lock, Bloom, local cache) is first-line for: How does connection pooling architecture prevent thundering herd on Redis reconnect after failover in your architecture?

---
### Q35. What architectural constraints does Redis impose on exactly-once processing semantics?

### Short Answer
The practical Redis answer is matching Redis data type to access pattern — not defaulting everything to JSON strings for: What architectural constraints does Redis impose on exactly-once processing semantics.

### Detailed Explanation
Pick strings for counters/cache blobs, hashes for field updates, sets/ZSETs for uniqueness/ranking, Streams for durable queues for: What architectural constraints does Redis impose on exactly-once processing semantics.

### Internal Working
Encoding upgrades and command complexity (O(N) vs O(1)) follow from type and size choices for: What architectural constraints does Redis impose on exactly-once processing semantics.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by validating command complexity and memory per key for: What architectural constraints does Redis impose on exactly-once processing semantics.

### Common Mistakes
Using `HGETALL` or `SMEMBERS` on large collections blocks the event loop for: What architectural constraints does Redis impose on exactly-once processing semantics.

### Follow-up Questions
Which type would you choose for: What architectural constraints does Redis impose on exactly-once processing semantics, and what command path proves it under peak cardinality?

---
### Q36. How would you map cache patterns (aside, through, behind) to team ownership boundaries?

### Short Answer
For this question, the architecturally correct Redis answer is matching Redis data type to access pattern — not defaulting everything to JSON strings for: How would you map cache patterns (aside, through, behind) to team ownership boundaries.

### Detailed Explanation
Pick strings for counters/cache blobs, hashes for field updates, sets/ZSETs for uniqueness/ranking, Streams for durable queues for: How would you map cache patterns (aside, through, behind) to team ownership boundaries.

### Internal Working
Encoding upgrades and command complexity (O(N) vs O(1)) follow from type and size choices for: How would you map cache patterns (aside, through, behind) to team ownership boundaries.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by validating command complexity and memory per key for: How would you map cache patterns (aside, through, behind) to team ownership boundaries.

### Common Mistakes
Using `HGETALL` or `SMEMBERS` on large collections blocks the event loop for: How would you map cache patterns (aside, through, behind) to team ownership boundaries.

### Follow-up Questions
Which type would you choose for: How would you map cache patterns (aside, through, behind) to team ownership boundaries, and what command path proves it under peak cardinality?

---
### Q37. When is noeviction the correct maxmemory-policy for a non-cache primary store?

### Short Answer
The production-grade Redis answer is setting `maxmemory` below container limit and picking `allkeys-lfu` or `volatile-lru` based on TTL discipline for: When is noeviction the correct maxmemory-policy for a non-cache primary store.

### Detailed Explanation
Eviction is approximate LRU/LFU using sampling (`maxmemory-samples`) — not exact global LRU for: When is noeviction the correct maxmemory-policy for a non-cache primary store.

### Internal Working
`volatile-*` policies only evict keys with TTL; keys without TTL are never evicted under volatile policies for: When is noeviction the correct maxmemory-policy for a non-cache primary store.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by alerting before hit ratio collapses and testing eviction under synthetic fill for: When is noeviction the correct maxmemory-policy for a non-cache primary store.

### Common Mistakes
Using `volatile-lru` without TTL on cache keys leads to OOM despite a policy being set for: When is noeviction the correct maxmemory-policy for a non-cache primary store.

### Follow-up Questions
What percentage of keys have TTL in your deployment, and how does that constrain policy choice for: When is noeviction the correct maxmemory-policy for a non-cache primary store?

---
### Q38. How do Redis ACLs change multi-tenant architecture compared to shared-password eras?

### Short Answer
The senior-level decision is using MULTI/EXEC for simple atomic batches and Lua for contested hot keys where WATCH abort rates would be high for: How do Redis ACLs change multi-tenant architecture compared to shared-password eras.

### Detailed Explanation
MULTI queues commands; EXEC runs them serially without interleaving — failed commands do not roll back earlier commands in the batch for: How do Redis ACLs change multi-tenant architecture compared to shared-password eras.

### Internal Working
WATCH provides optimistic locking by aborting EXEC if watched keys changed; pipelines batch without atomicity for: How do Redis ACLs change multi-tenant architecture compared to shared-password eras.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by keeping transaction blocks short and preferring Lua for compare-and-set on hot keys for: How do Redis ACLs change multi-tenant architecture compared to shared-password eras.

### Common Mistakes
Expecting RDBMS-style rollback or long MULTI blocks on hot keys are common production mistakes for: How do Redis ACLs change multi-tenant architecture compared to shared-password eras.

### Follow-up Questions
When would Lua replace MULTI/EXEC for: How do Redis ACLs change multi-tenant architecture compared to shared-password eras, and what cluster slot constraints apply?

---
### Q39. What cross-datacenter replication options would you compare before choosing Redis Cluster only?

### Short Answer
The practical Redis answer is treating replication as async by default and using `WAIT` or app-level checks only when stronger durability is required for: What cross-datacenter replication options would you compare before choosing Redis Cluster only.

### Detailed Explanation
Replicas tail the replication stream; lag appears when network, disk, or apply speed falls behind write rate — partial resync needs adequate `repl-backlog-size` for: What cross-datacenter replication options would you compare before choosing Redis Cluster only.

### Internal Working
Read-your-writes is not automatic on replicas; clients using replica reads must accept staleness or use primary reads after writes for: What cross-datacenter replication options would you compare before choosing Redis Cluster only.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by correlating `master_repl_offset` with replica offsets and write spikes for: What cross-datacenter replication options would you compare before choosing Redis Cluster only.

### Common Mistakes
Common mistakes include writable replicas, ignoring lag during incidents, and assuming replica reads are fresh for: What cross-datacenter replication options would you compare before choosing Redis Cluster only.

### Follow-up Questions
Which writes in: What cross-datacenter replication options would you compare before choosing Redis Cluster only require synchronous acknowledgment, and how will clients handle failover mid-transaction?

---
### Q40. How would you defend Redis versus a cloud vendor cache in an enterprise architecture review?

### Short Answer
For this question, the architecturally correct Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: How would you defend Redis versus a cloud vendor cache in an enterprise architecture review.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: How would you defend Redis versus a cloud vendor cache in an enterprise architecture review.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: How would you defend Redis versus a cloud vendor cache in an enterprise architecture review.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by documenting ADR assumptions and exit strategy if load doubles for: How would you defend Redis versus a cloud vendor cache in an enterprise architecture review.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: How would you defend Redis versus a cloud vendor cache in an enterprise architecture review.

### Follow-up Questions
What requirement in: How would you defend Redis versus a cloud vendor cache in an enterprise architecture review is decisive if throughput numbers are similar across options?

---
### Q41. How do you triage sudden memory growth when used_memory rises but key count looks stable?

### Short Answer
The production-grade Redis answer is separating logical key growth from allocator overhead using `used_memory`, RSS, and encoding inspection for: How do you triage sudden memory growth when used_memory rises but key count looks stable.

### Detailed Explanation
Redis picks compact encodings (listpack, intset) for small values and upgrades to hashtable/skiplist structures as data grows — memory cliffs often appear at encoding thresholds for: How do you triage sudden memory growth when used_memory rises but key count looks stable.

### Internal Working
`robj` wraps values with type metadata; jemalloc arenas and copy-on-write during persistence amplify RSS beyond `used_memory` for: How do you triage sudden memory growth when used_memory rises but key count looks stable.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention after sampling top keys with `MEMORY USAGE` and reviewing fragmentation ratio trends for: How do you triage sudden memory growth when used_memory rises but key count looks stable.

### Common Mistakes
Teams often optimize value bytes while ignoring metadata overhead, fragmentation, and fork-related RSS spikes for: How do you triage sudden memory growth when used_memory rises but key count looks stable.

### Follow-up Questions
Which encoding upgrade or key-shape change would you test first to reduce memory for: How do you triage sudden memory growth when used_memory rises but key count looks stable?

---
### Q42. What steps isolate whether latency spikes are network, slow commands, or fork-related COW pressure?

### Short Answer
The senior-level decision is matching RDB/AOF hybrid settings to acceptable data-loss window and restart time for: What steps isolate whether latency spikes are network, slow commands, or fork-related COW pressure.

### Detailed Explanation
RDB gives compact snapshots; AOF gives finer durability with `appendfsync` tradeoffs — `everysec` is common but can lose ~1s on crash for: What steps isolate whether latency spikes are network, slow commands, or fork-related COW pressure.

### Internal Working
BGSAVE/AOF rewrite forks the process; copy-on-write can double memory pressure during snapshots, affecting latency for: What steps isolate whether latency spikes are network, slow commands, or fork-related COW pressure.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by testing crash-recovery drills and measuring fork latency under peak write load for: What steps isolate whether latency spikes are network, slow commands, or fork-related COW pressure.

### Common Mistakes
Dangerous patterns include `SAVE` in production, `appendfsync always` without throughput headroom, and ignoring COW during maintenance for: What steps isolate whether latency spikes are network, slow commands, or fork-related COW pressure.

### Follow-up Questions
What RPO does your chosen persistence mode actually guarantee for: What steps isolate whether latency spikes are network, slow commands, or fork-related COW pressure after a hard kill test?

---
### Q43. How would you diagnose replication lag that only appears during peak write hours?

### Short Answer
The practical Redis answer is treating replication as async by default and using `WAIT` or app-level checks only when stronger durability is required for: How would you diagnose replication lag that only appears during peak write hours.

### Detailed Explanation
Replicas tail the replication stream; lag appears when network, disk, or apply speed falls behind write rate — partial resync needs adequate `repl-backlog-size` for: How would you diagnose replication lag that only appears during peak write hours.

### Internal Working
Read-your-writes is not automatic on replicas; clients using replica reads must accept staleness or use primary reads after writes for: How would you diagnose replication lag that only appears during peak write hours.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by correlating `master_repl_offset` with replica offsets and write spikes for: How would you diagnose replication lag that only appears during peak write hours.

### Common Mistakes
Common mistakes include writable replicas, ignoring lag during incidents, and assuming replica reads are fresh for: How would you diagnose replication lag that only appears during peak write hours.

### Follow-up Questions
Which writes in: How would you diagnose replication lag that only appears during peak write hours require synchronous acknowledgment, and how will clients handle failover mid-transaction?

---
### Q44. What does LATENCY DOCTOR tell you that SLOWLOG alone cannot?

### Short Answer
For this question, the architecturally correct Redis answer is correlating INFO sections, slowlog, and latency doctor before changing config during incidents for: What does LATENCY DOCTOR tell you that SLOWLOG alone cannot.

### Detailed Explanation
INFO exposes memory, stats, replication, and cluster state; SLOWLOG captures commands exceeding threshold for: What does LATENCY DOCTOR tell you that SLOWLOG alone cannot.

### Internal Working
Cluster health requires per-node slot coverage and lag metrics, not only primary CPU for: What does LATENCY DOCTOR tell you that SLOWLOG alone cannot.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by defining dashboards for memory, ops/sec, lag, rejected connections, and evictions for: What does LATENCY DOCTOR tell you that SLOWLOG alone cannot.

### Common Mistakes
Running MONITOR in production destroys throughput — use targeted telemetry instead for: What does LATENCY DOCTOR tell you that SLOWLOG alone cannot.

### Follow-up Questions
Which three metrics would page you first for: What does LATENCY DOCTOR tell you that SLOWLOG alone cannot, and what thresholds?

---
### Q45. How do you find and remediate hot keys without KEYS or MONITOR in production?

### Short Answer
The production-grade Redis answer is combining TTL jitter, singleflight locks, and stale-while-revalidate to protect origin during: How do you find and remediate hot keys without KEYS or MONITOR in production.

### Detailed Explanation
Breakdown hits when a hot key expires; avalanche when many keys expire together; penetration when misses flood DB for absent keys for: How do you find and remediate hot keys without KEYS or MONITOR in production.

### Internal Working
Mitigations include probabilistic early refresh, Bloom filters or short negative TTL, and request coalescing for: How do you find and remediate hot keys without KEYS or MONITOR in production.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by load-testing synchronized expiry and hot-key miss scenarios for: How do you find and remediate hot keys without KEYS or MONITOR in production.

### Common Mistakes
Same TTL on all keys and caching null forever are classic self-inflicted outages for: How do you find and remediate hot keys without KEYS or MONITOR in production.

### Follow-up Questions
Which mitigation layer (jitter, lock, Bloom, local cache) is first-line for: How do you find and remediate hot keys without KEYS or MONITOR in production in your architecture?

---
### Q46. What symptoms distinguish a big-key problem from a hot-key problem on a single-threaded primary?

### Short Answer
The senior-level decision is treating Redis as a single-threaded command processor with optional I/O threading, then choosing HA topology to match RPO/RTO for: What symptoms distinguish a big-key problem from a hot-key problem on a single-threaded primary.

### Detailed Explanation
Redis throughput scales vertically per primary until CPU, memory, or hot-key skew dominates; Sentinel and Cluster solve availability and horizontal scale, not magic parallelism on one key for: What symptoms distinguish a big-key problem from a hot-key problem on a single-threaded primary.

### Internal Working
Commands execute serially on the event loop, so long operations block all clients on that node — architecture must keep hot paths O(1) and shard before CPU saturates for: What symptoms distinguish a big-key problem from a hot-key problem on a single-threaded primary.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts when comparing standalone, Sentinel, and Cluster for: What symptoms distinguish a big-key problem from a hot-key problem on a single-threaded primary.

### Common Mistakes
A common mistake is assuming Redis is multi-threaded for commands or colocating unrelated blast-radius workloads on one cluster for: What symptoms distinguish a big-key problem from a hot-key problem on a single-threaded primary.

### Follow-up Questions
What failover time, durability window, and client retry contract would you document before choosing topology for: What symptoms distinguish a big-key problem from a hot-key problem on a single-threaded primary?

---
### Q47. How would you troubleshoot Cluster slot imbalance after adding a new primary?

### Short Answer
The practical Redis answer is designing keys around 16384 hash slots, hash tags for multi-key ops, and cluster-aware clients for: How would you troubleshoot Cluster slot imbalance after adding a new primary.

### Detailed Explanation
Slot = CRC16(key) mod 16384; MOVED is permanent redirect, ASK is temporary during migration — resharding moves slot ownership without changing key names for: How would you troubleshoot Cluster slot imbalance after adding a new primary.

### Internal Working
Multi-key commands, Lua, and transactions require all keys in the same slot — `{tag}` hash tags force colocation for: How would you troubleshoot Cluster slot imbalance after adding a new primary.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by monitoring per-node ops/sec, slot distribution, and MOVED/ASK rates during: How would you troubleshoot Cluster slot imbalance after adding a new primary.

### Common Mistakes
Typical failures: non-cluster clients, cross-slot MGET, and hot slots from poor key choice for: How would you troubleshoot Cluster slot imbalance after adding a new primary.

### Follow-up Questions
How would you rebalance slots or split hot keys if: How would you troubleshoot Cluster slot imbalance after adding a new primary appears in production metrics?

---
### Q48. What is your runbook when clients report MOVED storms after a resharding operation?

### Short Answer
For this question, the architecturally correct Redis answer is designing keys around 16384 hash slots, hash tags for multi-key ops, and cluster-aware clients for: What is your runbook when clients report MOVED storms after a resharding operation.

### Detailed Explanation
Slot = CRC16(key) mod 16384; MOVED is permanent redirect, ASK is temporary during migration — resharding moves slot ownership without changing key names for: What is your runbook when clients report MOVED storms after a resharding operation.

### Internal Working
Multi-key commands, Lua, and transactions require all keys in the same slot — `{tag}` hash tags force colocation for: What is your runbook when clients report MOVED storms after a resharding operation.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by monitoring per-node ops/sec, slot distribution, and MOVED/ASK rates during: What is your runbook when clients report MOVED storms after a resharding operation.

### Common Mistakes
Typical failures: non-cluster clients, cross-slot MGET, and hot slots from poor key choice for: What is your runbook when clients report MOVED storms after a resharding operation.

### Follow-up Questions
How would you rebalance slots or split hot keys if: What is your runbook when clients report MOVED storms after a resharding operation appears in production metrics?

---
### Q49. How do you debug Sentinel failover loops where primaries flap every few minutes?

### Short Answer
The production-grade Redis answer is deploying an odd number of sentinels with quorum tuned to avoid flapping while enabling automatic failover for: How do you debug Sentinel failover loops where primaries flap every few minutes.

### Detailed Explanation
Sentinel marks subjective/objective down states, elects a new primary, and re-points replicas — clients must discover the new primary via Sentinel-aware drivers for: How do you debug Sentinel failover loops where primaries flap every few minutes.

### Internal Working
Failover promotes a replica with `REPLICAOF NO ONE` then reconfigures the fleet; brief write unavailability and client reconnect storms are expected for: How do you debug Sentinel failover loops where primaries flap every few minutes.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by running game-day failover tests with connection pool refresh metrics for: How do you debug Sentinel failover loops where primaries flap every few minutes.

### Common Mistakes
Split-brain risk rises with even sentinel counts, stale client caches, and missing `min-replicas-to-write` guards for: How do you debug Sentinel failover loops where primaries flap every few minutes.

### Follow-up Questions
What quorum and `down-after-milliseconds` values would you defend in an ADR for: How do you debug Sentinel failover loops where primaries flap every few minutes?

---
### Q50. What causes writes to fail with OOM errors despite setting maxmemory?

### Short Answer
The senior-level decision is setting `maxmemory` below container limit and picking `allkeys-lfu` or `volatile-lru` based on TTL discipline for: What causes writes to fail with OOM errors despite setting maxmemory.

### Detailed Explanation
Eviction is approximate LRU/LFU using sampling (`maxmemory-samples`) — not exact global LRU for: What causes writes to fail with OOM errors despite setting maxmemory.

### Internal Working
`volatile-*` policies only evict keys with TTL; keys without TTL are never evicted under volatile policies for: What causes writes to fail with OOM errors despite setting maxmemory.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by alerting before hit ratio collapses and testing eviction under synthetic fill for: What causes writes to fail with OOM errors despite setting maxmemory.

### Common Mistakes
Using `volatile-lru` without TTL on cache keys leads to OOM despite a policy being set for: What causes writes to fail with OOM errors despite setting maxmemory.

### Follow-up Questions
What percentage of keys have TTL in your deployment, and how does that constrain policy choice for: What causes writes to fail with OOM errors despite setting maxmemory?

---
### Q51. How would you investigate volatile-lru not evicting keys when memory is full?

### Short Answer
The practical Redis answer is setting `maxmemory` below container limit and picking `allkeys-lfu` or `volatile-lru` based on TTL discipline for: How would you investigate volatile-lru not evicting keys when memory is full.

### Detailed Explanation
Eviction is approximate LRU/LFU using sampling (`maxmemory-samples`) — not exact global LRU for: How would you investigate volatile-lru not evicting keys when memory is full.

### Internal Working
`volatile-*` policies only evict keys with TTL; keys without TTL are never evicted under volatile policies for: How would you investigate volatile-lru not evicting keys when memory is full.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by alerting before hit ratio collapses and testing eviction under synthetic fill for: How would you investigate volatile-lru not evicting keys when memory is full.

### Common Mistakes
Using `volatile-lru` without TTL on cache keys leads to OOM despite a policy being set for: How would you investigate volatile-lru not evicting keys when memory is full.

### Follow-up Questions
What percentage of keys have TTL in your deployment, and how does that constrain policy choice for: How would you investigate volatile-lru not evicting keys when memory is full?

---
### Q52. What forensic steps follow a partial AOF rewrite failure on restart?

### Short Answer
For this question, the architecturally correct Redis answer is matching RDB/AOF hybrid settings to acceptable data-loss window and restart time for: What forensic steps follow a partial AOF rewrite failure on restart.

### Detailed Explanation
RDB gives compact snapshots; AOF gives finer durability with `appendfsync` tradeoffs — `everysec` is common but can lose ~1s on crash for: What forensic steps follow a partial AOF rewrite failure on restart.

### Internal Working
BGSAVE/AOF rewrite forks the process; copy-on-write can double memory pressure during snapshots, affecting latency for: What forensic steps follow a partial AOF rewrite failure on restart.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by testing crash-recovery drills and measuring fork latency under peak write load for: What forensic steps follow a partial AOF rewrite failure on restart.

### Common Mistakes
Dangerous patterns include `SAVE` in production, `appendfsync always` without throughput headroom, and ignoring COW during maintenance for: What forensic steps follow a partial AOF rewrite failure on restart.

### Follow-up Questions
What RPO does your chosen persistence mode actually guarantee for: What forensic steps follow a partial AOF rewrite failure on restart after a hard kill test?

---
### Q53. How do you detect and fix replica serving stale reads that break business rules?

### Short Answer
The production-grade Redis answer is treating replication as async by default and using `WAIT` or app-level checks only when stronger durability is required for: How do you detect and fix replica serving stale reads that break business rules.

### Detailed Explanation
Replicas tail the replication stream; lag appears when network, disk, or apply speed falls behind write rate — partial resync needs adequate `repl-backlog-size` for: How do you detect and fix replica serving stale reads that break business rules.

### Internal Working
Read-your-writes is not automatic on replicas; clients using replica reads must accept staleness or use primary reads after writes for: How do you detect and fix replica serving stale reads that break business rules.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by correlating `master_repl_offset` with replica offsets and write spikes for: How do you detect and fix replica serving stale reads that break business rules.

### Common Mistakes
Common mistakes include writable replicas, ignoring lag during incidents, and assuming replica reads are fresh for: How do you detect and fix replica serving stale reads that break business rules.

### Follow-up Questions
Which writes in: How do you detect and fix replica serving stale reads that break business rules require synchronous acknowledgment, and how will clients handle failover mid-transaction?

---
### Q54. What explains consumer group pending entries growing without XPENDING visibility in dashboards?

### Short Answer
The senior-level decision is using consumer groups for at-least-once work queues with explicit XACK and pending reclaim for: What explains consumer group pending entries growing without XPENDING visibility in dashboards.

### Detailed Explanation
Streams append entries with auto IDs; consumer groups track per-consumer progress and pending entries for: What explains consumer group pending entries growing without XPENDING visibility in dashboards.

### Internal Working
Without XACK, messages stay pending; crashed consumers require XCLAIM/XAUTOCLAIM after idle threshold for: What explains consumer group pending entries growing without XPENDING visibility in dashboards.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by monitoring XPENDING depth and trimming with MAXLEN ~ for: What explains consumer group pending entries growing without XPENDING visibility in dashboards.

### Common Mistakes
Treating Streams as exactly-once without idempotent handlers is a common correctness gap for: What explains consumer group pending entries growing without XPENDING visibility in dashboards.

### Follow-up Questions
What idempotency key and poison-message policy would you pair with: What explains consumer group pending entries growing without XPENDING visibility in dashboards?

---
### Q55. How would you troubleshoot cache stampede after a popular key expires simultaneously?

### Short Answer
The practical Redis answer is combining TTL jitter, singleflight locks, and stale-while-revalidate to protect origin during: How would you troubleshoot cache stampede after a popular key expires simultaneously.

### Detailed Explanation
Breakdown hits when a hot key expires; avalanche when many keys expire together; penetration when misses flood DB for absent keys for: How would you troubleshoot cache stampede after a popular key expires simultaneously.

### Internal Working
Mitigations include probabilistic early refresh, Bloom filters or short negative TTL, and request coalescing for: How would you troubleshoot cache stampede after a popular key expires simultaneously.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by load-testing synchronized expiry and hot-key miss scenarios for: How would you troubleshoot cache stampede after a popular key expires simultaneously.

### Common Mistakes
Same TTL on all keys and caching null forever are classic self-inflicted outages for: How would you troubleshoot cache stampede after a popular key expires simultaneously.

### Follow-up Questions
Which mitigation layer (jitter, lock, Bloom, local cache) is first-line for: How would you troubleshoot cache stampede after a popular key expires simultaneously in your architecture?

---
### Q56. What mitigations apply when cache penetration hammers the database for non-existent IDs?

### Short Answer
For this question, the architecturally correct Redis answer is combining TTL jitter, singleflight locks, and stale-while-revalidate to protect origin during: What mitigations apply when cache penetration hammers the database for non-existent IDs.

### Detailed Explanation
Breakdown hits when a hot key expires; avalanche when many keys expire together; penetration when misses flood DB for absent keys for: What mitigations apply when cache penetration hammers the database for non-existent IDs.

### Internal Working
Mitigations include probabilistic early refresh, Bloom filters or short negative TTL, and request coalescing for: What mitigations apply when cache penetration hammers the database for non-existent IDs.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by load-testing synchronized expiry and hot-key miss scenarios for: What mitigations apply when cache penetration hammers the database for non-existent IDs.

### Common Mistakes
Same TTL on all keys and caching null forever are classic self-inflicted outages for: What mitigations apply when cache penetration hammers the database for non-existent IDs.

### Follow-up Questions
Which mitigation layer (jitter, lock, Bloom, local cache) is first-line for: What mitigations apply when cache penetration hammers the database for non-existent IDs in your architecture?

---
### Q57. How do you debug distributed lock double-execution after TTL expiry?

### Short Answer
The production-grade Redis answer is using `SET key token NX PX ttl` plus Lua compare-and-del unlock, with fencing tokens for durable side effects for: How do you debug distributed lock double-execution after TTL expiry.

### Detailed Explanation
Locks auto-expire via TTL to survive client crashes, but TTL expiry before work finishes allows double execution — fencing tokens monotonically guard downstream storage for: How do you debug distributed lock double-execution after TTL expiry.

### Internal Working
Redlock across independent masters is debated; single-instance locks are simpler but fail with primary loss unless fencing compensates for: How do you debug distributed lock double-execution after TTL expiry.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by testing GC pause and clock skew scenarios against lock TTL for: How do you debug distributed lock double-execution after TTL expiry.

### Common Mistakes
Never use `SETNX` without TTL or `DEL` without token check — both cause correctness incidents for: How do you debug distributed lock double-execution after TTL expiry.

### Follow-up Questions
What fencing mechanism protects your storage layer if: How do you debug distributed lock double-execution after TTL expiry outlives the Redis lock TTL?

---
### Q58. What would you check when BGSAVE consistently fails during memory pressure events?

### Short Answer
The senior-level decision is matching RDB/AOF hybrid settings to acceptable data-loss window and restart time for: What would you check when BGSAVE consistently fails during memory pressure events.

### Detailed Explanation
RDB gives compact snapshots; AOF gives finer durability with `appendfsync` tradeoffs — `everysec` is common but can lose ~1s on crash for: What would you check when BGSAVE consistently fails during memory pressure events.

### Internal Working
BGSAVE/AOF rewrite forks the process; copy-on-write can double memory pressure during snapshots, affecting latency for: What would you check when BGSAVE consistently fails during memory pressure events.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by testing crash-recovery drills and measuring fork latency under peak write load for: What would you check when BGSAVE consistently fails during memory pressure events.

### Common Mistakes
Dangerous patterns include `SAVE` in production, `appendfsync always` without throughput headroom, and ignoring COW during maintenance for: What would you check when BGSAVE consistently fails during memory pressure events.

### Follow-up Questions
What RPO does your chosen persistence mode actually guarantee for: What would you check when BGSAVE consistently fails during memory pressure events after a hard kill test?

---
### Q59. How do you triage high CPU on Redis when QPS has not increased?

### Short Answer
The practical Redis answer is classifying the symptom (memory, lag, latency, routing) before applying config changes for: How do you triage high CPU on Redis when QPS has not increased.

### Detailed Explanation
Hot keys skew CPU on one shard; big keys inflate latency and replication cost — diagnose with `--hotkeys`, memory sampling, and slowlog for: How do you triage high CPU on Redis when QPS has not increased.

### Internal Working
Replication lag may be backlog, network, or write spike — not always replica hardware for: How do you triage high CPU on Redis when QPS has not increased.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew with a written runbook and rollback criteria for each remediation step for: How do you triage high CPU on Redis when QPS has not increased.

### Common Mistakes
Using KEYS, FLUSHALL without ASYNC, or failover without client drain worsens many incidents for: How do you triage high CPU on Redis when QPS has not increased.

### Follow-up Questions
What evidence proves root cause versus symptom for: How do you triage high CPU on Redis when QPS has not increased before you close the incident?

---
### Q60. What client-side symptoms indicate connection pool exhaustion versus server maxclients?

### Short Answer
For this question, the architecturally correct Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: What client-side symptoms indicate connection pool exhaustion versus server maxclients.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: What client-side symptoms indicate connection pool exhaustion versus server maxclients.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: What client-side symptoms indicate connection pool exhaustion versus server maxclients.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by documenting ADR assumptions and exit strategy if load doubles for: What client-side symptoms indicate connection pool exhaustion versus server maxclients.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: What client-side symptoms indicate connection pool exhaustion versus server maxclients.

### Follow-up Questions
What requirement in: What client-side symptoms indicate connection pool exhaustion versus server maxclients is decisive if throughput numbers are similar across options?

---
### Q61. How would you debug a Lua script that intermittently fails with CROSSSLOT errors in Cluster?

### Short Answer
The production-grade Redis answer is keeping Lua scripts short, deterministic, and slot-safe in Cluster for atomic server-side logic for: How would you debug a Lua script that intermittently fails with CROSSSLOT errors in Cluster.

### Detailed Explanation
Scripts run atomically — no other commands interleave — making them ideal for compare-and-set, rate limits, and safe unlock for: How would you debug a Lua script that intermittently fails with CROSSSLOT errors in Cluster.

### Internal Working
Non-deterministic calls are restricted; all KEYS must hash to the same slot in Cluster for: How would you debug a Lua script that intermittently fails with CROSSSLOT errors in Cluster.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by preloading with SCRIPT LOAD and monitoring slowlog for long scripts for: How would you debug a Lua script that intermittently fails with CROSSSLOT errors in Cluster.

### Common Mistakes
Long Lua blocks the entire server — avoid O(N) loops and unbounded logic for: How would you debug a Lua script that intermittently fails with CROSSSLOT errors in Cluster.

### Follow-up Questions
How do you version and deploy script changes safely for: How would you debug a Lua script that intermittently fails with CROSSSLOT errors in Cluster across rolling restarts?

---
### Q62. What runbook steps apply when one shard in Cluster hits 100% CPU while others are idle?

### Short Answer
The senior-level decision is designing keys around 16384 hash slots, hash tags for multi-key ops, and cluster-aware clients for: What runbook steps apply when one shard in Cluster hits 100% CPU while others are idle.

### Detailed Explanation
Slot = CRC16(key) mod 16384; MOVED is permanent redirect, ASK is temporary during migration — resharding moves slot ownership without changing key names for: What runbook steps apply when one shard in Cluster hits 100% CPU while others are idle.

### Internal Working
Multi-key commands, Lua, and transactions require all keys in the same slot — `{tag}` hash tags force colocation for: What runbook steps apply when one shard in Cluster hits 100% CPU while others are idle.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by monitoring per-node ops/sec, slot distribution, and MOVED/ASK rates during: What runbook steps apply when one shard in Cluster hits 100% CPU while others are idle.

### Common Mistakes
Typical failures: non-cluster clients, cross-slot MGET, and hot slots from poor key choice for: What runbook steps apply when one shard in Cluster hits 100% CPU while others are idle.

### Follow-up Questions
How would you rebalance slots or split hot keys if: What runbook steps apply when one shard in Cluster hits 100% CPU while others are idle appears in production metrics?

---
### Q63. How do you identify commands blocking the event loop beyond SLOWLOG threshold tuning?

### Short Answer
The practical Redis answer is correlating INFO sections, slowlog, and latency doctor before changing config during incidents for: How do you identify commands blocking the event loop beyond SLOWLOG threshold tuning.

### Detailed Explanation
INFO exposes memory, stats, replication, and cluster state; SLOWLOG captures commands exceeding threshold for: How do you identify commands blocking the event loop beyond SLOWLOG threshold tuning.

### Internal Working
Cluster health requires per-node slot coverage and lag metrics, not only primary CPU for: How do you identify commands blocking the event loop beyond SLOWLOG threshold tuning.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by defining dashboards for memory, ops/sec, lag, rejected connections, and evictions for: How do you identify commands blocking the event loop beyond SLOWLOG threshold tuning.

### Common Mistakes
Running MONITOR in production destroys throughput — use targeted telemetry instead for: How do you identify commands blocking the event loop beyond SLOWLOG threshold tuning.

### Follow-up Questions
Which three metrics would page you first for: How do you identify commands blocking the event loop beyond SLOWLOG threshold tuning, and what thresholds?

---
### Q64. What causes mem_fragmentation_ratio to climb and when is active defrag appropriate?

### Short Answer
For this question, the architecturally correct Redis answer is separating logical key growth from allocator overhead using `used_memory`, RSS, and encoding inspection for: What causes mem_fragmentation_ratio to climb and when is active defrag appropriate.

### Detailed Explanation
Redis picks compact encodings (listpack, intset) for small values and upgrades to hashtable/skiplist structures as data grows — memory cliffs often appear at encoding thresholds for: What causes mem_fragmentation_ratio to climb and when is active defrag appropriate.

### Internal Working
`robj` wraps values with type metadata; jemalloc arenas and copy-on-write during persistence amplify RSS beyond `used_memory` for: What causes mem_fragmentation_ratio to climb and when is active defrag appropriate.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology after sampling top keys with `MEMORY USAGE` and reviewing fragmentation ratio trends for: What causes mem_fragmentation_ratio to climb and when is active defrag appropriate.

### Common Mistakes
Teams often optimize value bytes while ignoring metadata overhead, fragmentation, and fork-related RSS spikes for: What causes mem_fragmentation_ratio to climb and when is active defrag appropriate.

### Follow-up Questions
Which encoding upgrade or key-shape change would you test first to reduce memory for: What causes mem_fragmentation_ratio to climb and when is active defrag appropriate?

---
### Q65. How would you troubleshoot session loss after a Sentinel failover during peak traffic?

### Short Answer
The production-grade Redis answer is deploying an odd number of sentinels with quorum tuned to avoid flapping while enabling automatic failover for: How would you troubleshoot session loss after a Sentinel failover during peak traffic.

### Detailed Explanation
Sentinel marks subjective/objective down states, elects a new primary, and re-points replicas — clients must discover the new primary via Sentinel-aware drivers for: How would you troubleshoot session loss after a Sentinel failover during peak traffic.

### Internal Working
Failover promotes a replica with `REPLICAOF NO ONE` then reconfigures the fleet; brief write unavailability and client reconnect storms are expected for: How would you troubleshoot session loss after a Sentinel failover during peak traffic.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by running game-day failover tests with connection pool refresh metrics for: How would you troubleshoot session loss after a Sentinel failover during peak traffic.

### Common Mistakes
Split-brain risk rises with even sentinel counts, stale client caches, and missing `min-replicas-to-write` guards for: How would you troubleshoot session loss after a Sentinel failover during peak traffic.

### Follow-up Questions
What quorum and `down-after-milliseconds` values would you defend in an ADR for: How would you troubleshoot session loss after a Sentinel failover during peak traffic?

---
### Q66. What diagnostics differentiate network partition from overloaded primary during timeout storms?

### Short Answer
The senior-level decision is matching Redis data type to access pattern — not defaulting everything to JSON strings for: What diagnostics differentiate network partition from overloaded primary during timeout storms.

### Detailed Explanation
Pick strings for counters/cache blobs, hashes for field updates, sets/ZSETs for uniqueness/ranking, Streams for durable queues for: What diagnostics differentiate network partition from overloaded primary during timeout storms.

### Internal Working
Encoding upgrades and command complexity (O(N) vs O(1)) follow from type and size choices for: What diagnostics differentiate network partition from overloaded primary during timeout storms.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by validating command complexity and memory per key for: What diagnostics differentiate network partition from overloaded primary during timeout storms.

### Common Mistakes
Using `HGETALL` or `SMEMBERS` on large collections blocks the event loop for: What diagnostics differentiate network partition from overloaded primary during timeout storms.

### Follow-up Questions
Which type would you choose for: What diagnostics differentiate network partition from overloaded primary during timeout storms, and what command path proves it under peak cardinality?

---
### Q67. How do you debug rate limiter drift when counters look correct per key but limits feel wrong?

### Short Answer
The practical Redis answer is picking fixed, sliding, or token-bucket algorithms based on burst tolerance and accuracy needs for: How do you debug rate limiter drift when counters look correct per key but limits feel wrong.

### Detailed Explanation
INCR + EXPIRE gives fixed windows; sorted sets give sliding windows; Lua gives accurate token refill for: How do you debug rate limiter drift when counters look correct per key but limits feel wrong.

### Internal Working
Global counters can become hot keys — shard counter keys or use local aggregation for: How do you debug rate limiter drift when counters look correct per key but limits feel wrong.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by testing boundary bursts at window edges for: How do you debug rate limiter drift when counters look correct per key but limits feel wrong.

### Common Mistakes
Fixed windows allow 2× burst at boundaries; ignoring atomicity on compound checks causes drift for: How do you debug rate limiter drift when counters look correct per key but limits feel wrong.

### Follow-up Questions
How would you shard a global rate limit key if: How do you debug rate limiter drift when counters look correct per key but limits feel wrong saturates one Redis primary?

---
### Q68. What steps validate AOF integrity before promoting a rebuilt replica?

### Short Answer
For this question, the architecturally correct Redis answer is matching RDB/AOF hybrid settings to acceptable data-loss window and restart time for: What steps validate AOF integrity before promoting a rebuilt replica.

### Detailed Explanation
RDB gives compact snapshots; AOF gives finer durability with `appendfsync` tradeoffs — `everysec` is common but can lose ~1s on crash for: What steps validate AOF integrity before promoting a rebuilt replica.

### Internal Working
BGSAVE/AOF rewrite forks the process; copy-on-write can double memory pressure during snapshots, affecting latency for: What steps validate AOF integrity before promoting a rebuilt replica.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by testing crash-recovery drills and measuring fork latency under peak write load for: What steps validate AOF integrity before promoting a rebuilt replica.

### Common Mistakes
Dangerous patterns include `SAVE` in production, `appendfsync always` without throughput headroom, and ignoring COW during maintenance for: What steps validate AOF integrity before promoting a rebuilt replica.

### Follow-up Questions
What RPO does your chosen persistence mode actually guarantee for: What steps validate AOF integrity before promoting a rebuilt replica after a hard kill test?

---
### Q69. How would you investigate Pub/Sub subscribers missing invalidation messages intermittently?

### Short Answer
The production-grade Redis answer is deleting or updating cache keys on write and broadcasting invalidation when multi-tier caches exist for: How would you investigate Pub/Sub subscribers missing invalidation messages intermittently.

### Detailed Explanation
Write-through updates DB and cache together; write-behind updates cache first with async flush — each shifts consistency risk for: How would you investigate Pub/Sub subscribers missing invalidation messages intermittently.

### Internal Working
Pub/Sub can signal app-local cache eviction, but Redis remains source for shared cache layer for: How would you investigate Pub/Sub subscribers missing invalidation messages intermittently.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by defining who invalidates on partial updates and out-of-order writes for: How would you investigate Pub/Sub subscribers missing invalidation messages intermittently.

### Common Mistakes
Updating DB without cache delete is the most common stale-data bug for: How would you investigate Pub/Sub subscribers missing invalidation messages intermittently.

### Follow-up Questions
How do you invalidate related keys (lists, aggregates) when: How would you investigate Pub/Sub subscribers missing invalidation messages intermittently updates one entity?

---
### Q70. What is your incident checklist when Redis latency breaches SLO but INFO shows low ops/sec?

### Short Answer
The senior-level decision is classifying the symptom (memory, lag, latency, routing) before applying config changes for: What is your incident checklist when Redis latency breaches SLO but INFO shows low ops/sec.

### Detailed Explanation
Hot keys skew CPU on one shard; big keys inflate latency and replication cost — diagnose with `--hotkeys`, memory sampling, and slowlog for: What is your incident checklist when Redis latency breaches SLO but INFO shows low ops/sec.

### Internal Working
Replication lag may be backlog, network, or write spike — not always replica hardware for: What is your incident checklist when Redis latency breaches SLO but INFO shows low ops/sec.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts with a written runbook and rollback criteria for each remediation step for: What is your incident checklist when Redis latency breaches SLO but INFO shows low ops/sec.

### Common Mistakes
Using KEYS, FLUSHALL without ASYNC, or failover without client drain worsens many incidents for: What is your incident checklist when Redis latency breaches SLO but INFO shows low ops/sec.

### Follow-up Questions
What evidence proves root cause versus symptom for: What is your incident checklist when Redis latency breaches SLO but INFO shows low ops/sec before you close the incident?

---
### Q71. How does pipelining improve throughput without changing Redis single-threaded execution?

### Short Answer
The practical Redis answer is using MULTI/EXEC for simple atomic batches and Lua for contested hot keys where WATCH abort rates would be high for: How does pipelining improve throughput without changing Redis single-threaded execution.

### Detailed Explanation
MULTI queues commands; EXEC runs them serially without interleaving — failed commands do not roll back earlier commands in the batch for: How does pipelining improve throughput without changing Redis single-threaded execution.

### Internal Working
WATCH provides optimistic locking by aborting EXEC if watched keys changed; pipelines batch without atomicity for: How does pipelining improve throughput without changing Redis single-threaded execution.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by keeping transaction blocks short and preferring Lua for compare-and-set on hot keys for: How does pipelining improve throughput without changing Redis single-threaded execution.

### Common Mistakes
Expecting RDBMS-style rollback or long MULTI blocks on hot keys are common production mistakes for: How does pipelining improve throughput without changing Redis single-threaded execution.

### Follow-up Questions
When would Lua replace MULTI/EXEC for: How does pipelining improve throughput without changing Redis single-threaded execution, and what cluster slot constraints apply?

---
### Q72. What pipeline batch size tradeoffs would you test against a 5ms p99 latency SLO?

### Short Answer
For this question, the architecturally correct Redis answer is using RESP over TCP with connection pooling and pipelining to cut round trips without expecting multi-command parallelism on the server for: What pipeline batch size tradeoffs would you test against a 5ms p99 latency SLO.

### Detailed Explanation
Pipelining batches many commands in one RTT while Redis still executes them sequentially — throughput gains come from network efficiency, not parallel command threads for: What pipeline batch size tradeoffs would you test against a 5ms p99 latency SLO.

### Internal Working
Cluster clients must handle MOVED/ASK redirects and maintain slot maps; protocol-level retries differ from application idempotency for: What pipeline batch size tradeoffs would you test against a 5ms p99 latency SLO.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by profiling client RTT versus server `slowlog` entries for: What pipeline batch size tradeoffs would you test against a 5ms p99 latency SLO.

### Common Mistakes
A frequent mistake is huge pipelines without backpressure, causing timeouts and memory pressure on both client and server for: What pipeline batch size tradeoffs would you test against a 5ms p99 latency SLO.

### Follow-up Questions
What pipeline batch size and timeout would you cap for: What pipeline batch size tradeoffs would you test against a 5ms p99 latency SLO given your p99 SLO?

---
### Q73. When does MGET outperform pipelined GET for the same key batch?

### Short Answer
The production-grade Redis answer is using RESP over TCP with connection pooling and pipelining to cut round trips without expecting multi-command parallelism on the server for: When does MGET outperform pipelined GET for the same key batch.

### Detailed Explanation
Pipelining batches many commands in one RTT while Redis still executes them sequentially — throughput gains come from network efficiency, not parallel command threads for: When does MGET outperform pipelined GET for the same key batch.

### Internal Working
Cluster clients must handle MOVED/ASK redirects and maintain slot maps; protocol-level retries differ from application idempotency for: When does MGET outperform pipelined GET for the same key batch.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by profiling client RTT versus server `slowlog` entries for: When does MGET outperform pipelined GET for the same key batch.

### Common Mistakes
A frequent mistake is huge pipelines without backpressure, causing timeouts and memory pressure on both client and server for: When does MGET outperform pipelined GET for the same key batch.

### Follow-up Questions
What pipeline batch size and timeout would you cap for: When does MGET outperform pipelined GET for the same key batch given your p99 SLO?

---
### Q74. How do large values in strings affect network and latency more than CPU on the server?

### Short Answer
The senior-level decision is profiling latency as network RTT + command cost on a single thread, then pipelining and command shaping for: How do large values in strings affect network and latency more than CPU on the server.

### Detailed Explanation
O(N) commands (`KEYS`, large `HGETALL`, wide `ZRANGE`) block the event loop — replace with SCAN, field picks, and LIMIT for: How do large values in strings affect network and latency more than CPU on the server.

### Internal Working
I/O threads help socket read/write but do not parallelize command execution for: How do large values in strings affect network and latency more than CPU on the server.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts using slowlog, latency doctor, and before/after benchmarks for: How do large values in strings affect network and latency more than CPU on the server.

### Common Mistakes
Chasing hardware scale before fixing big keys, hot keys, or chatty clients rarely fixes p99 for: How do large values in strings affect network and latency more than CPU on the server.

### Follow-up Questions
What single slowlog entry would convince you to change schema or sharding for: How do large values in strings affect network and latency more than CPU on the server?

---
### Q75. What command choices turn O(1) expectations into O(N) event-loop blockers?

### Short Answer
The practical Redis answer is matching Redis data type to access pattern — not defaulting everything to JSON strings for: What command choices turn O(1) expectations into O(N) event-loop blockers.

### Detailed Explanation
Pick strings for counters/cache blobs, hashes for field updates, sets/ZSETs for uniqueness/ranking, Streams for durable queues for: What command choices turn O(1) expectations into O(N) event-loop blockers.

### Internal Working
Encoding upgrades and command complexity (O(N) vs O(1)) follow from type and size choices for: What command choices turn O(1) expectations into O(N) event-loop blockers.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by validating command complexity and memory per key for: What command choices turn O(1) expectations into O(N) event-loop blockers.

### Common Mistakes
Using `HGETALL` or `SMEMBERS` on large collections blocks the event loop for: What command choices turn O(1) expectations into O(N) event-loop blockers.

### Follow-up Questions
Which type would you choose for: What command choices turn O(1) expectations into O(N) event-loop blockers, and what command path proves it under peak cardinality?

---
### Q76. How would you tune io-threads and io-threads-do-reads for a read-heavy workload?

### Short Answer
For this question, the architecturally correct Redis answer is profiling latency as network RTT + command cost on a single thread, then pipelining and command shaping for: How would you tune io-threads and io-threads-do-reads for a read-heavy workload.

### Detailed Explanation
O(N) commands (`KEYS`, large `HGETALL`, wide `ZRANGE`) block the event loop — replace with SCAN, field picks, and LIMIT for: How would you tune io-threads and io-threads-do-reads for a read-heavy workload.

### Internal Working
I/O threads help socket read/write but do not parallelize command execution for: How would you tune io-threads and io-threads-do-reads for a read-heavy workload.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology using slowlog, latency doctor, and before/after benchmarks for: How would you tune io-threads and io-threads-do-reads for a read-heavy workload.

### Common Mistakes
Chasing hardware scale before fixing big keys, hot keys, or chatty clients rarely fixes p99 for: How would you tune io-threads and io-threads-do-reads for a read-heavy workload.

### Follow-up Questions
What single slowlog entry would convince you to change schema or sharding for: How would you tune io-threads and io-threads-do-reads for a read-heavy workload?

---
### Q77. What is the performance impact of appendfsync always versus everysec for write-heavy caches?

### Short Answer
The production-grade Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: What is the performance impact of appendfsync always versus everysec for write-heavy caches.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: What is the performance impact of appendfsync always versus everysec for write-heavy caches.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: What is the performance impact of appendfsync always versus everysec for write-heavy caches.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by documenting ADR assumptions and exit strategy if load doubles for: What is the performance impact of appendfsync always versus everysec for write-heavy caches.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: What is the performance impact of appendfsync always versus everysec for write-heavy caches.

### Follow-up Questions
What requirement in: What is the performance impact of appendfsync always versus everysec for write-heavy caches is decisive if throughput numbers are similar across options?

---
### Q78. How does RDB fork latency interact with memory overcommit and COW during BGSAVE?

### Short Answer
The senior-level decision is matching RDB/AOF hybrid settings to acceptable data-loss window and restart time for: How does RDB fork latency interact with memory overcommit and COW during BGSAVE.

### Detailed Explanation
RDB gives compact snapshots; AOF gives finer durability with `appendfsync` tradeoffs — `everysec` is common but can lose ~1s on crash for: How does RDB fork latency interact with memory overcommit and COW during BGSAVE.

### Internal Working
BGSAVE/AOF rewrite forks the process; copy-on-write can double memory pressure during snapshots, affecting latency for: How does RDB fork latency interact with memory overcommit and COW during BGSAVE.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by testing crash-recovery drills and measuring fork latency under peak write load for: How does RDB fork latency interact with memory overcommit and COW during BGSAVE.

### Common Mistakes
Dangerous patterns include `SAVE` in production, `appendfsync always` without throughput headroom, and ignoring COW during maintenance for: How does RDB fork latency interact with memory overcommit and COW during BGSAVE.

### Follow-up Questions
What RPO does your chosen persistence mode actually guarantee for: How does RDB fork latency interact with memory overcommit and COW during BGSAVE after a hard kill test?

---
### Q79. When does allkeys-lfu outperform allkeys-lru for skewed access patterns?

### Short Answer
The practical Redis answer is setting `maxmemory` below container limit and picking `allkeys-lfu` or `volatile-lru` based on TTL discipline for: When does allkeys-lfu outperform allkeys-lru for skewed access patterns.

### Detailed Explanation
Eviction is approximate LRU/LFU using sampling (`maxmemory-samples`) — not exact global LRU for: When does allkeys-lfu outperform allkeys-lru for skewed access patterns.

### Internal Working
`volatile-*` policies only evict keys with TTL; keys without TTL are never evicted under volatile policies for: When does allkeys-lfu outperform allkeys-lru for skewed access patterns.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by alerting before hit ratio collapses and testing eviction under synthetic fill for: When does allkeys-lfu outperform allkeys-lru for skewed access patterns.

### Common Mistakes
Using `volatile-lru` without TTL on cache keys leads to OOM despite a policy being set for: When does allkeys-lfu outperform allkeys-lru for skewed access patterns.

### Follow-up Questions
What percentage of keys have TTL in your deployment, and how does that constrain policy choice for: When does allkeys-lfu outperform allkeys-lru for skewed access patterns?

---
### Q80. How do maxmemory-samples settings affect eviction accuracy and CPU?

### Short Answer
For this question, the architecturally correct Redis answer is setting `maxmemory` below container limit and picking `allkeys-lfu` or `volatile-lru` based on TTL discipline for: How do maxmemory-samples settings affect eviction accuracy and CPU.

### Detailed Explanation
Eviction is approximate LRU/LFU using sampling (`maxmemory-samples`) — not exact global LRU for: How do maxmemory-samples settings affect eviction accuracy and CPU.

### Internal Working
`volatile-*` policies only evict keys with TTL; keys without TTL are never evicted under volatile policies for: How do maxmemory-samples settings affect eviction accuracy and CPU.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by alerting before hit ratio collapses and testing eviction under synthetic fill for: How do maxmemory-samples settings affect eviction accuracy and CPU.

### Common Mistakes
Using `volatile-lru` without TTL on cache keys leads to OOM despite a policy being set for: How do maxmemory-samples settings affect eviction accuracy and CPU.

### Follow-up Questions
What percentage of keys have TTL in your deployment, and how does that constrain policy choice for: How do maxmemory-samples settings affect eviction accuracy and CPU?

---
### Q81. What encoding upgrades cause latency cliffs as small hashes grow past listpack thresholds?

### Short Answer
The production-grade Redis answer is separating logical key growth from allocator overhead using `used_memory`, RSS, and encoding inspection for: What encoding upgrades cause latency cliffs as small hashes grow past listpack thresholds.

### Detailed Explanation
Redis picks compact encodings (listpack, intset) for small values and upgrades to hashtable/skiplist structures as data grows — memory cliffs often appear at encoding thresholds for: What encoding upgrades cause latency cliffs as small hashes grow past listpack thresholds.

### Internal Working
`robj` wraps values with type metadata; jemalloc arenas and copy-on-write during persistence amplify RSS beyond `used_memory` for: What encoding upgrades cause latency cliffs as small hashes grow past listpack thresholds.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention after sampling top keys with `MEMORY USAGE` and reviewing fragmentation ratio trends for: What encoding upgrades cause latency cliffs as small hashes grow past listpack thresholds.

### Common Mistakes
Teams often optimize value bytes while ignoring metadata overhead, fragmentation, and fork-related RSS spikes for: What encoding upgrades cause latency cliffs as small hashes grow past listpack thresholds.

### Follow-up Questions
Which encoding upgrade or key-shape change would you test first to reduce memory for: What encoding upgrades cause latency cliffs as small hashes grow past listpack thresholds?

---
### Q82. How would you benchmark UNLINK versus DEL for bulk key deletion in production maintenance?

### Short Answer
The senior-level decision is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: How would you benchmark UNLINK versus DEL for bulk key deletion in production maintenance.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: How would you benchmark UNLINK versus DEL for bulk key deletion in production maintenance.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: How would you benchmark UNLINK versus DEL for bulk key deletion in production maintenance.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by documenting ADR assumptions and exit strategy if load doubles for: How would you benchmark UNLINK versus DEL for bulk key deletion in production maintenance.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: How would you benchmark UNLINK versus DEL for bulk key deletion in production maintenance.

### Follow-up Questions
What requirement in: How would you benchmark UNLINK versus DEL for bulk key deletion in production maintenance is decisive if throughput numbers are similar across options?

---
### Q83. What client connection pool sizing formula avoids Redis maxclients saturation?

### Short Answer
The practical Redis answer is sizing memory as key count × (value + metadata overhead) plus replication and headroom for fork for: What client connection pool sizing formula avoids Redis maxclients saturation.

### Detailed Explanation
Plan growth with key cardinality forecasts, encoding assumptions, and replica factor — Cluster adds coordination overhead for: What client connection pool sizing formula avoids Redis maxclients saturation.

### Internal Working
Connection count from many pods can exhaust `maxclients` before memory fills for: What client connection pool sizing formula avoids Redis maxclients saturation.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew with load tests that include failover and snapshot windows for: What client connection pool sizing formula avoids Redis maxclients saturation.

### Common Mistakes
Sizing only for data bytes without overhead, replicas, or COW margin causes emergency scale events for: What client connection pool sizing formula avoids Redis maxclients saturation.

### Follow-up Questions
At what memory or ops/sec threshold would you trigger horizontal scale for: What client connection pool sizing formula avoids Redis maxclients saturation?

---
### Q84. How does TLS add latency, and where would you terminate TLS for cache workloads?

### Short Answer
For this question, the architecturally correct Redis answer is profiling latency as network RTT + command cost on a single thread, then pipelining and command shaping for: How does TLS add latency, and where would you terminate TLS for cache workloads.

### Detailed Explanation
O(N) commands (`KEYS`, large `HGETALL`, wide `ZRANGE`) block the event loop — replace with SCAN, field picks, and LIMIT for: How does TLS add latency, and where would you terminate TLS for cache workloads.

### Internal Working
I/O threads help socket read/write but do not parallelize command execution for: How does TLS add latency, and where would you terminate TLS for cache workloads.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology using slowlog, latency doctor, and before/after benchmarks for: How does TLS add latency, and where would you terminate TLS for cache workloads.

### Common Mistakes
Chasing hardware scale before fixing big keys, hot keys, or chatty clients rarely fixes p99 for: How does TLS add latency, and where would you terminate TLS for cache workloads.

### Follow-up Questions
What single slowlog entry would convince you to change schema or sharding for: How does TLS add latency, and where would you terminate TLS for cache workloads?

---
### Q85. When does sharding with Cluster improve throughput versus larger single-instance hardware?

### Short Answer
The production-grade Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: When does sharding with Cluster improve throughput versus larger single-instance hardware.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: When does sharding with Cluster improve throughput versus larger single-instance hardware.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: When does sharding with Cluster improve throughput versus larger single-instance hardware.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by documenting ADR assumptions and exit strategy if load doubles for: When does sharding with Cluster improve throughput versus larger single-instance hardware.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: When does sharding with Cluster improve throughput versus larger single-instance hardware.

### Follow-up Questions
What requirement in: When does sharding with Cluster improve throughput versus larger single-instance hardware is decisive if throughput numbers are similar across options?

---
### Q86. How do BITOP and BITCOUNT scale poorly on large sparse bitmaps?

### Short Answer
The senior-level decision is matching Redis data type to access pattern — not defaulting everything to JSON strings for: How do BITOP and BITCOUNT scale poorly on large sparse bitmaps.

### Detailed Explanation
Pick strings for counters/cache blobs, hashes for field updates, sets/ZSETs for uniqueness/ranking, Streams for durable queues for: How do BITOP and BITCOUNT scale poorly on large sparse bitmaps.

### Internal Working
Encoding upgrades and command complexity (O(N) vs O(1)) follow from type and size choices for: How do BITOP and BITCOUNT scale poorly on large sparse bitmaps.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by validating command complexity and memory per key for: How do BITOP and BITCOUNT scale poorly on large sparse bitmaps.

### Common Mistakes
Using `HGETALL` or `SMEMBERS` on large collections blocks the event loop for: How do BITOP and BITCOUNT scale poorly on large sparse bitmaps.

### Follow-up Questions
Which type would you choose for: How do BITOP and BITCOUNT scale poorly on large sparse bitmaps, and what command path proves it under peak cardinality?

---
### Q87. What ZSET range query patterns need LIMIT to protect p99 latency?

### Short Answer
The practical Redis answer is profiling latency as network RTT + command cost on a single thread, then pipelining and command shaping for: What ZSET range query patterns need LIMIT to protect p99 latency.

### Detailed Explanation
O(N) commands (`KEYS`, large `HGETALL`, wide `ZRANGE`) block the event loop — replace with SCAN, field picks, and LIMIT for: What ZSET range query patterns need LIMIT to protect p99 latency.

### Internal Working
I/O threads help socket read/write but do not parallelize command execution for: What ZSET range query patterns need LIMIT to protect p99 latency.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew using slowlog, latency doctor, and before/after benchmarks for: What ZSET range query patterns need LIMIT to protect p99 latency.

### Common Mistakes
Chasing hardware scale before fixing big keys, hot keys, or chatty clients rarely fixes p99 for: What ZSET range query patterns need LIMIT to protect p99 latency.

### Follow-up Questions
What single slowlog entry would convince you to change schema or sharding for: What ZSET range query patterns need LIMIT to protect p99 latency?

---
### Q88. How would you optimize a sliding-window rate limiter implemented with sorted sets?

### Short Answer
For this question, the architecturally correct Redis answer is picking fixed, sliding, or token-bucket algorithms based on burst tolerance and accuracy needs for: How would you optimize a sliding-window rate limiter implemented with sorted sets.

### Detailed Explanation
INCR + EXPIRE gives fixed windows; sorted sets give sliding windows; Lua gives accurate token refill for: How would you optimize a sliding-window rate limiter implemented with sorted sets.

### Internal Working
Global counters can become hot keys — shard counter keys or use local aggregation for: How would you optimize a sliding-window rate limiter implemented with sorted sets.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by testing boundary bursts at window edges for: How would you optimize a sliding-window rate limiter implemented with sorted sets.

### Common Mistakes
Fixed windows allow 2× burst at boundaries; ignoring atomicity on compound checks causes drift for: How would you optimize a sliding-window rate limiter implemented with sorted sets.

### Follow-up Questions
How would you shard a global rate limit key if: How would you optimize a sliding-window rate limiter implemented with sorted sets saturates one Redis primary?

---
### Q89. What latency gains come from switching HGETALL to HMGET or HSCAN on wide hashes?

### Short Answer
The production-grade Redis answer is profiling latency as network RTT + command cost on a single thread, then pipelining and command shaping for: What latency gains come from switching HGETALL to HMGET or HSCAN on wide hashes.

### Detailed Explanation
O(N) commands (`KEYS`, large `HGETALL`, wide `ZRANGE`) block the event loop — replace with SCAN, field picks, and LIMIT for: What latency gains come from switching HGETALL to HMGET or HSCAN on wide hashes.

### Internal Working
I/O threads help socket read/write but do not parallelize command execution for: What latency gains come from switching HGETALL to HMGET or HSCAN on wide hashes.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention using slowlog, latency doctor, and before/after benchmarks for: What latency gains come from switching HGETALL to HMGET or HSCAN on wide hashes.

### Common Mistakes
Chasing hardware scale before fixing big keys, hot keys, or chatty clients rarely fixes p99 for: What latency gains come from switching HGETALL to HMGET or HSCAN on wide hashes.

### Follow-up Questions
What single slowlog entry would convince you to change schema or sharding for: What latency gains come from switching HGETALL to HMGET or HSCAN on wide hashes?

---
### Q90. How does replication backlog sizing affect partial resync performance after brief outages?

### Short Answer
The senior-level decision is treating replication as async by default and using `WAIT` or app-level checks only when stronger durability is required for: How does replication backlog sizing affect partial resync performance after brief outages.

### Detailed Explanation
Replicas tail the replication stream; lag appears when network, disk, or apply speed falls behind write rate — partial resync needs adequate `repl-backlog-size` for: How does replication backlog sizing affect partial resync performance after brief outages.

### Internal Working
Read-your-writes is not automatic on replicas; clients using replica reads must accept staleness or use primary reads after writes for: How does replication backlog sizing affect partial resync performance after brief outages.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by correlating `master_repl_offset` with replica offsets and write spikes for: How does replication backlog sizing affect partial resync performance after brief outages.

### Common Mistakes
Common mistakes include writable replicas, ignoring lag during incidents, and assuming replica reads are fresh for: How does replication backlog sizing affect partial resync performance after brief outages.

### Follow-up Questions
Which writes in: How does replication backlog sizing affect partial resync performance after brief outages require synchronous acknowledgment, and how will clients handle failover mid-transaction?

---
### Q91. What OS-level tuning (transparent huge pages, somaxconn) still matters for Redis in 2026?

### Short Answer
The practical Redis answer is matching Redis data type to access pattern — not defaulting everything to JSON strings for: What OS-level tuning (transparent huge pages, somaxconn) still matters for Redis in 2026.

### Detailed Explanation
Pick strings for counters/cache blobs, hashes for field updates, sets/ZSETs for uniqueness/ranking, Streams for durable queues for: What OS-level tuning (transparent huge pages, somaxconn) still matters for Redis in 2026.

### Internal Working
Encoding upgrades and command complexity (O(N) vs O(1)) follow from type and size choices for: What OS-level tuning (transparent huge pages, somaxconn) still matters for Redis in 2026.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by validating command complexity and memory per key for: What OS-level tuning (transparent huge pages, somaxconn) still matters for Redis in 2026.

### Common Mistakes
Using `HGETALL` or `SMEMBERS` on large collections blocks the event loop for: What OS-level tuning (transparent huge pages, somaxconn) still matters for Redis in 2026.

### Follow-up Questions
Which type would you choose for: What OS-level tuning (transparent huge pages, somaxconn) still matters for Redis in 2026, and what command path proves it under peak cardinality?

---
### Q92. How would you load-test Redis Cluster to find the first bottleneck: CPU, network, or slot skew?

### Short Answer
For this question, the architecturally correct Redis answer is designing keys around 16384 hash slots, hash tags for multi-key ops, and cluster-aware clients for: How would you load-test Redis Cluster to find the first bottleneck: CPU, network, or slot skew.

### Detailed Explanation
Slot = CRC16(key) mod 16384; MOVED is permanent redirect, ASK is temporary during migration — resharding moves slot ownership without changing key names for: How would you load-test Redis Cluster to find the first bottleneck: CPU, network, or slot skew.

### Internal Working
Multi-key commands, Lua, and transactions require all keys in the same slot — `{tag}` hash tags force colocation for: How would you load-test Redis Cluster to find the first bottleneck: CPU, network, or slot skew.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by monitoring per-node ops/sec, slot distribution, and MOVED/ASK rates during: How would you load-test Redis Cluster to find the first bottleneck: CPU, network, or slot skew.

### Common Mistakes
Typical failures: non-cluster clients, cross-slot MGET, and hot slots from poor key choice for: How would you load-test Redis Cluster to find the first bottleneck: CPU, network, or slot skew.

### Follow-up Questions
How would you rebalance slots or split hot keys if: How would you load-test Redis Cluster to find the first bottleneck: CPU, network, or slot skew appears in production metrics?

---
### Q93. When does probabilistic early expiration improve tail latency versus naive TTL refresh?

### Short Answer
The production-grade Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: When does probabilistic early expiration improve tail latency versus naive TTL refresh.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: When does probabilistic early expiration improve tail latency versus naive TTL refresh.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: When does probabilistic early expiration improve tail latency versus naive TTL refresh.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by documenting ADR assumptions and exit strategy if load doubles for: When does probabilistic early expiration improve tail latency versus naive TTL refresh.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: When does probabilistic early expiration improve tail latency versus naive TTL refresh.

### Follow-up Questions
What requirement in: When does probabilistic early expiration improve tail latency versus naive TTL refresh is decisive if throughput numbers are similar across options?

---
### Q94. How do Streams MAXLEN approximate trimming trade memory for ingestion throughput?

### Short Answer
The senior-level decision is using consumer groups for at-least-once work queues with explicit XACK and pending reclaim for: How do Streams MAXLEN approximate trimming trade memory for ingestion throughput.

### Detailed Explanation
Streams append entries with auto IDs; consumer groups track per-consumer progress and pending entries for: How do Streams MAXLEN approximate trimming trade memory for ingestion throughput.

### Internal Working
Without XACK, messages stay pending; crashed consumers require XCLAIM/XAUTOCLAIM after idle threshold for: How do Streams MAXLEN approximate trimming trade memory for ingestion throughput.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by monitoring XPENDING depth and trimming with MAXLEN ~ for: How do Streams MAXLEN approximate trimming trade memory for ingestion throughput.

### Common Mistakes
Treating Streams as exactly-once without idempotent handlers is a common correctness gap for: How do Streams MAXLEN approximate trimming trade memory for ingestion throughput.

### Follow-up Questions
What idempotency key and poison-message policy would you pair with: How do Streams MAXLEN approximate trimming trade memory for ingestion throughput?

---
### Q95. What metrics prove your cache hit ratio improvements actually reduced database load?

### Short Answer
The practical Redis answer is matching Redis data type to access pattern — not defaulting everything to JSON strings for: What metrics prove your cache hit ratio improvements actually reduced database load.

### Detailed Explanation
Pick strings for counters/cache blobs, hashes for field updates, sets/ZSETs for uniqueness/ranking, Streams for durable queues for: What metrics prove your cache hit ratio improvements actually reduced database load.

### Internal Working
Encoding upgrades and command complexity (O(N) vs O(1)) follow from type and size choices for: What metrics prove your cache hit ratio improvements actually reduced database load.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by validating command complexity and memory per key for: What metrics prove your cache hit ratio improvements actually reduced database load.

### Common Mistakes
Using `HGETALL` or `SMEMBERS` on large collections blocks the event loop for: What metrics prove your cache hit ratio improvements actually reduced database load.

### Follow-up Questions
Which type would you choose for: What metrics prove your cache hit ratio improvements actually reduced database load, and what command path proves it under peak cardinality?

---
### Q96. What data loss window exists with appendfsync everysec if the process crashes mid-second?

### Short Answer
For this question, the architecturally correct Redis answer is matching RDB/AOF hybrid settings to acceptable data-loss window and restart time for: What data loss window exists with appendfsync everysec if the process crashes mid-second.

### Detailed Explanation
RDB gives compact snapshots; AOF gives finer durability with `appendfsync` tradeoffs — `everysec` is common but can lose ~1s on crash for: What data loss window exists with appendfsync everysec if the process crashes mid-second.

### Internal Working
BGSAVE/AOF rewrite forks the process; copy-on-write can double memory pressure during snapshots, affecting latency for: What data loss window exists with appendfsync everysec if the process crashes mid-second.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by testing crash-recovery drills and measuring fork latency under peak write load for: What data loss window exists with appendfsync everysec if the process crashes mid-second.

### Common Mistakes
Dangerous patterns include `SAVE` in production, `appendfsync always` without throughput headroom, and ignoring COW during maintenance for: What data loss window exists with appendfsync everysec if the process crashes mid-second.

### Follow-up Questions
What RPO does your chosen persistence mode actually guarantee for: What data loss window exists with appendfsync everysec if the process crashes mid-second after a hard kill test?

---
### Q97. How do RDB snapshots complement AOF for faster restarts in hybrid persistence?

### Short Answer
The production-grade Redis answer is matching RDB/AOF hybrid settings to acceptable data-loss window and restart time for: How do RDB snapshots complement AOF for faster restarts in hybrid persistence.

### Detailed Explanation
RDB gives compact snapshots; AOF gives finer durability with `appendfsync` tradeoffs — `everysec` is common but can lose ~1s on crash for: How do RDB snapshots complement AOF for faster restarts in hybrid persistence.

### Internal Working
BGSAVE/AOF rewrite forks the process; copy-on-write can double memory pressure during snapshots, affecting latency for: How do RDB snapshots complement AOF for faster restarts in hybrid persistence.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by testing crash-recovery drills and measuring fork latency under peak write load for: How do RDB snapshots complement AOF for faster restarts in hybrid persistence.

### Common Mistakes
Dangerous patterns include `SAVE` in production, `appendfsync always` without throughput headroom, and ignoring COW during maintenance for: How do RDB snapshots complement AOF for faster restarts in hybrid persistence.

### Follow-up Questions
What RPO does your chosen persistence mode actually guarantee for: How do RDB snapshots complement AOF for faster restarts in hybrid persistence after a hard kill test?

---
### Q98. When would you disable persistence entirely, and what failure modes remain acceptable?

### Short Answer
The senior-level decision is matching RDB/AOF hybrid settings to acceptable data-loss window and restart time for: When would you disable persistence entirely, and what failure modes remain acceptable.

### Detailed Explanation
RDB gives compact snapshots; AOF gives finer durability with `appendfsync` tradeoffs — `everysec` is common but can lose ~1s on crash for: When would you disable persistence entirely, and what failure modes remain acceptable.

### Internal Working
BGSAVE/AOF rewrite forks the process; copy-on-write can double memory pressure during snapshots, affecting latency for: When would you disable persistence entirely, and what failure modes remain acceptable.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by testing crash-recovery drills and measuring fork latency under peak write load for: When would you disable persistence entirely, and what failure modes remain acceptable.

### Common Mistakes
Dangerous patterns include `SAVE` in production, `appendfsync always` without throughput headroom, and ignoring COW during maintenance for: When would you disable persistence entirely, and what failure modes remain acceptable.

### Follow-up Questions
What RPO does your chosen persistence mode actually guarantee for: When would you disable persistence entirely, and what failure modes remain acceptable after a hard kill test?

---
### Q99. How does min-replicas-to-write protect against write loss during partition events?

### Short Answer
The practical Redis answer is treating replication as async by default and using `WAIT` or app-level checks only when stronger durability is required for: How does min-replicas-to-write protect against write loss during partition events.

### Detailed Explanation
Replicas tail the replication stream; lag appears when network, disk, or apply speed falls behind write rate — partial resync needs adequate `repl-backlog-size` for: How does min-replicas-to-write protect against write loss during partition events.

### Internal Working
Read-your-writes is not automatic on replicas; clients using replica reads must accept staleness or use primary reads after writes for: How does min-replicas-to-write protect against write loss during partition events.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by correlating `master_repl_offset` with replica offsets and write spikes for: How does min-replicas-to-write protect against write loss during partition events.

### Common Mistakes
Common mistakes include writable replicas, ignoring lag during incidents, and assuming replica reads are fresh for: How does min-replicas-to-write protect against write loss during partition events.

### Follow-up Questions
Which writes in: How does min-replicas-to-write protect against write loss during partition events require synchronous acknowledgment, and how will clients handle failover mid-transaction?

---
### Q100. What is the role of WAIT after a write when clients require stronger durability than async replication?

### Short Answer
For this question, the architecturally correct Redis answer is treating replication as async by default and using `WAIT` or app-level checks only when stronger durability is required for: What is the role of WAIT after a write when clients require stronger durability than async replication.

### Detailed Explanation
Replicas tail the replication stream; lag appears when network, disk, or apply speed falls behind write rate — partial resync needs adequate `repl-backlog-size` for: What is the role of WAIT after a write when clients require stronger durability than async replication.

### Internal Working
Read-your-writes is not automatic on replicas; clients using replica reads must accept staleness or use primary reads after writes for: What is the role of WAIT after a write when clients require stronger durability than async replication.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by correlating `master_repl_offset` with replica offsets and write spikes for: What is the role of WAIT after a write when clients require stronger durability than async replication.

### Common Mistakes
Common mistakes include writable replicas, ignoring lag during incidents, and assuming replica reads are fresh for: What is the role of WAIT after a write when clients require stronger durability than async replication.

### Follow-up Questions
Which writes in: What is the role of WAIT after a write when clients require stronger durability than async replication require synchronous acknowledgment, and how will clients handle failover mid-transaction?

---
### Q101. How would you design failover testing for Sentinel without corrupting production data?

### Short Answer
The production-grade Redis answer is deploying an odd number of sentinels with quorum tuned to avoid flapping while enabling automatic failover for: How would you design failover testing for Sentinel without corrupting production data.

### Detailed Explanation
Sentinel marks subjective/objective down states, elects a new primary, and re-points replicas — clients must discover the new primary via Sentinel-aware drivers for: How would you design failover testing for Sentinel without corrupting production data.

### Internal Working
Failover promotes a replica with `REPLICAOF NO ONE` then reconfigures the fleet; brief write unavailability and client reconnect storms are expected for: How would you design failover testing for Sentinel without corrupting production data.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by running game-day failover tests with connection pool refresh metrics for: How would you design failover testing for Sentinel without corrupting production data.

### Common Mistakes
Split-brain risk rises with even sentinel counts, stale client caches, and missing `min-replicas-to-write` guards for: How would you design failover testing for Sentinel without corrupting production data.

### Follow-up Questions
What quorum and `down-after-milliseconds` values would you defend in an ADR for: How would you design failover testing for Sentinel without corrupting production data?

---
### Q102. What split-brain scenarios can occur with misconfigured Sentinel quorum?

### Short Answer
The senior-level decision is deploying an odd number of sentinels with quorum tuned to avoid flapping while enabling automatic failover for: What split-brain scenarios can occur with misconfigured Sentinel quorum.

### Detailed Explanation
Sentinel marks subjective/objective down states, elects a new primary, and re-points replicas — clients must discover the new primary via Sentinel-aware drivers for: What split-brain scenarios can occur with misconfigured Sentinel quorum.

### Internal Working
Failover promotes a replica with `REPLICAOF NO ONE` then reconfigures the fleet; brief write unavailability and client reconnect storms are expected for: What split-brain scenarios can occur with misconfigured Sentinel quorum.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by running game-day failover tests with connection pool refresh metrics for: What split-brain scenarios can occur with misconfigured Sentinel quorum.

### Common Mistakes
Split-brain risk rises with even sentinel counts, stale client caches, and missing `min-replicas-to-write` guards for: What split-brain scenarios can occur with misconfigured Sentinel quorum.

### Follow-up Questions
What quorum and `down-after-milliseconds` values would you defend in an ADR for: What split-brain scenarios can occur with misconfigured Sentinel quorum?

---
### Q103. How do replica-read-only and ACLs combine to prevent accidental writes to secondaries?

### Short Answer
The practical Redis answer is treating replication as async by default and using `WAIT` or app-level checks only when stronger durability is required for: How do replica-read-only and ACLs combine to prevent accidental writes to secondaries.

### Detailed Explanation
Replicas tail the replication stream; lag appears when network, disk, or apply speed falls behind write rate — partial resync needs adequate `repl-backlog-size` for: How do replica-read-only and ACLs combine to prevent accidental writes to secondaries.

### Internal Working
Read-your-writes is not automatic on replicas; clients using replica reads must accept staleness or use primary reads after writes for: How do replica-read-only and ACLs combine to prevent accidental writes to secondaries.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by correlating `master_repl_offset` with replica offsets and write spikes for: How do replica-read-only and ACLs combine to prevent accidental writes to secondaries.

### Common Mistakes
Common mistakes include writable replicas, ignoring lag during incidents, and assuming replica reads are fresh for: How do replica-read-only and ACLs combine to prevent accidental writes to secondaries.

### Follow-up Questions
Which writes in: How do replica-read-only and ACLs combine to prevent accidental writes to secondaries require synchronous acknowledgment, and how will clients handle failover mid-transaction?

---
### Q104. What happens to in-flight Pub/Sub messages during primary failover?

### Short Answer
For this question, the architecturally correct Redis answer is using Pub/Sub only for ephemeral fan-out where message loss during disconnect is acceptable for: What happens to in-flight Pub/Sub messages during primary failover.

### Detailed Explanation
Pub/Sub delivers only to connected subscribers — no persistence, backlog, or acks — unlike Streams or external brokers for: What happens to in-flight Pub/Sub messages during primary failover.

### Internal Working
Slow subscribers are disconnected; dedicated connections are required because SUBSCRIBE blocks the connection for: What happens to in-flight Pub/Sub messages during primary failover.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by pairing invalidation signals with cache TTL and source-of-truth refresh for: What happens to in-flight Pub/Sub messages during primary failover.

### Common Mistakes
Using Pub/Sub as a job queue or on shared pool connections causes lost work and stuck clients for: What happens to in-flight Pub/Sub messages during primary failover.

### Follow-up Questions
What happens to in-flight Pub/Sub messages during failover in: What happens to in-flight Pub/Sub messages during primary failover, and is that acceptable?

---
### Q105. How do consumer groups provide at-least-once delivery, and what idempotency must apps implement?

### Short Answer
The production-grade Redis answer is using consumer groups for at-least-once work queues with explicit XACK and pending reclaim for: How do consumer groups provide at-least-once delivery, and what idempotency must apps implement.

### Detailed Explanation
Streams append entries with auto IDs; consumer groups track per-consumer progress and pending entries for: How do consumer groups provide at-least-once delivery, and what idempotency must apps implement.

### Internal Working
Without XACK, messages stay pending; crashed consumers require XCLAIM/XAUTOCLAIM after idle threshold for: How do consumer groups provide at-least-once delivery, and what idempotency must apps implement.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by monitoring XPENDING depth and trimming with MAXLEN ~ for: How do consumer groups provide at-least-once delivery, and what idempotency must apps implement.

### Common Mistakes
Treating Streams as exactly-once without idempotent handlers is a common correctness gap for: How do consumer groups provide at-least-once delivery, and what idempotency must apps implement.

### Follow-up Questions
What idempotency key and poison-message policy would you pair with: How do consumer groups provide at-least-once delivery, and what idempotency must apps implement?

---
### Q106. Why does MULTI/EXEC not provide rollback semantics like a relational transaction?

### Short Answer
The senior-level decision is using MULTI/EXEC for simple atomic batches and Lua for contested hot keys where WATCH abort rates would be high for: Why does MULTI/EXEC not provide rollback semantics like a relational transaction.

### Detailed Explanation
MULTI queues commands; EXEC runs them serially without interleaving — failed commands do not roll back earlier commands in the batch for: Why does MULTI/EXEC not provide rollback semantics like a relational transaction.

### Internal Working
WATCH provides optimistic locking by aborting EXEC if watched keys changed; pipelines batch without atomicity for: Why does MULTI/EXEC not provide rollback semantics like a relational transaction.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by keeping transaction blocks short and preferring Lua for compare-and-set on hot keys for: Why does MULTI/EXEC not provide rollback semantics like a relational transaction.

### Common Mistakes
Expecting RDBMS-style rollback or long MULTI blocks on hot keys are common production mistakes for: Why does MULTI/EXEC not provide rollback semantics like a relational transaction.

### Follow-up Questions
When would Lua replace MULTI/EXEC for: Why does MULTI/EXEC not provide rollback semantics like a relational transaction, and what cluster slot constraints apply?

---
### Q107. How do fencing tokens prevent stale lock holders from corrupting durable storage?

### Short Answer
The practical Redis answer is using `SET key token NX PX ttl` plus Lua compare-and-del unlock, with fencing tokens for durable side effects for: How do fencing tokens prevent stale lock holders from corrupting durable storage.

### Detailed Explanation
Locks auto-expire via TTL to survive client crashes, but TTL expiry before work finishes allows double execution — fencing tokens monotonically guard downstream storage for: How do fencing tokens prevent stale lock holders from corrupting durable storage.

### Internal Working
Redlock across independent masters is debated; single-instance locks are simpler but fail with primary loss unless fencing compensates for: How do fencing tokens prevent stale lock holders from corrupting durable storage.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by testing GC pause and clock skew scenarios against lock TTL for: How do fencing tokens prevent stale lock holders from corrupting durable storage.

### Common Mistakes
Never use `SETNX` without TTL or `DEL` without token check — both cause correctness incidents for: How do fencing tokens prevent stale lock holders from corrupting durable storage.

### Follow-up Questions
What fencing mechanism protects your storage layer if: How do fencing tokens prevent stale lock holders from corrupting durable storage outlives the Redis lock TTL?

---
### Q108. What correctness gaps remain with SET key token NX PX even when unlock uses Lua?

### Short Answer
For this question, the architecturally correct Redis answer is using `SET key token NX PX ttl` plus Lua compare-and-del unlock, with fencing tokens for durable side effects for: What correctness gaps remain with SET key token NX PX even when unlock uses Lua.

### Detailed Explanation
Locks auto-expire via TTL to survive client crashes, but TTL expiry before work finishes allows double execution — fencing tokens monotonically guard downstream storage for: What correctness gaps remain with SET key token NX PX even when unlock uses Lua.

### Internal Working
Redlock across independent masters is debated; single-instance locks are simpler but fail with primary loss unless fencing compensates for: What correctness gaps remain with SET key token NX PX even when unlock uses Lua.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by testing GC pause and clock skew scenarios against lock TTL for: What correctness gaps remain with SET key token NX PX even when unlock uses Lua.

### Common Mistakes
Never use `SETNX` without TTL or `DEL` without token check — both cause correctness incidents for: What correctness gaps remain with SET key token NX PX even when unlock uses Lua.

### Follow-up Questions
What fencing mechanism protects your storage layer if: What correctness gaps remain with SET key token NX PX even when unlock uses Lua outlives the Redis lock TTL?

---
### Q109. How would you argue for or against Redlock in a multi-datacenter inventory system?

### Short Answer
The production-grade Redis answer is using `SET key token NX PX ttl` plus Lua compare-and-del unlock, with fencing tokens for durable side effects for: How would you argue for or against Redlock in a multi-datacenter inventory system.

### Detailed Explanation
Locks auto-expire via TTL to survive client crashes, but TTL expiry before work finishes allows double execution — fencing tokens monotonically guard downstream storage for: How would you argue for or against Redlock in a multi-datacenter inventory system.

### Internal Working
Redlock across independent masters is debated; single-instance locks are simpler but fail with primary loss unless fencing compensates for: How would you argue for or against Redlock in a multi-datacenter inventory system.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by testing GC pause and clock skew scenarios against lock TTL for: How would you argue for or against Redlock in a multi-datacenter inventory system.

### Common Mistakes
Never use `SETNX` without TTL or `DEL` without token check — both cause correctness incidents for: How would you argue for or against Redlock in a multi-datacenter inventory system.

### Follow-up Questions
What fencing mechanism protects your storage layer if: How would you argue for or against Redlock in a multi-datacenter inventory system outlives the Redis lock TTL?

---
### Q110. What disaster recovery RPO do you get from hourly RDB plus AOF everysec combined?

### Short Answer
The senior-level decision is matching RDB/AOF hybrid settings to acceptable data-loss window and restart time for: What disaster recovery RPO do you get from hourly RDB plus AOF everysec combined.

### Detailed Explanation
RDB gives compact snapshots; AOF gives finer durability with `appendfsync` tradeoffs — `everysec` is common but can lose ~1s on crash for: What disaster recovery RPO do you get from hourly RDB plus AOF everysec combined.

### Internal Working
BGSAVE/AOF rewrite forks the process; copy-on-write can double memory pressure during snapshots, affecting latency for: What disaster recovery RPO do you get from hourly RDB plus AOF everysec combined.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by testing crash-recovery drills and measuring fork latency under peak write load for: What disaster recovery RPO do you get from hourly RDB plus AOF everysec combined.

### Common Mistakes
Dangerous patterns include `SAVE` in production, `appendfsync always` without throughput headroom, and ignoring COW during maintenance for: What disaster recovery RPO do you get from hourly RDB plus AOF everysec combined.

### Follow-up Questions
What RPO does your chosen persistence mode actually guarantee for: What disaster recovery RPO do you get from hourly RDB plus AOF everysec combined after a hard kill test?

---
### Q111. How does Cluster handle primary failure when replicas exist versus when they do not?

### Short Answer
The practical Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: How does Cluster handle primary failure when replicas exist versus when they do not.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: How does Cluster handle primary failure when replicas exist versus when they do not.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: How does Cluster handle primary failure when replicas exist versus when they do not.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by documenting ADR assumptions and exit strategy if load doubles for: How does Cluster handle primary failure when replicas exist versus when they do not.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: How does Cluster handle primary failure when replicas exist versus when they do not.

### Follow-up Questions
What requirement in: How does Cluster handle primary failure when replicas exist versus when they do not is decisive if throughput numbers are similar across options?

---
### Q112. What reliability risks appear when resharding moves slots during peak traffic?

### Short Answer
For this question, the architecturally correct Redis answer is designing keys around 16384 hash slots, hash tags for multi-key ops, and cluster-aware clients for: What reliability risks appear when resharding moves slots during peak traffic.

### Detailed Explanation
Slot = CRC16(key) mod 16384; MOVED is permanent redirect, ASK is temporary during migration — resharding moves slot ownership without changing key names for: What reliability risks appear when resharding moves slots during peak traffic.

### Internal Working
Multi-key commands, Lua, and transactions require all keys in the same slot — `{tag}` hash tags force colocation for: What reliability risks appear when resharding moves slots during peak traffic.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by monitoring per-node ops/sec, slot distribution, and MOVED/ASK rates during: What reliability risks appear when resharding moves slots during peak traffic.

### Common Mistakes
Typical failures: non-cluster clients, cross-slot MGET, and hot slots from poor key choice for: What reliability risks appear when resharding moves slots during peak traffic.

### Follow-up Questions
How would you rebalance slots or split hot keys if: What reliability risks appear when resharding moves slots during peak traffic appears in production metrics?

---
### Q113. How do you keep cache and database consistent under write-through versus write-behind?

### Short Answer
The production-grade Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: How do you keep cache and database consistent under write-through versus write-behind.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: How do you keep cache and database consistent under write-through versus write-behind.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: How do you keep cache and database consistent under write-through versus write-behind.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by documenting ADR assumptions and exit strategy if load doubles for: How do you keep cache and database consistent under write-through versus write-behind.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: How do you keep cache and database consistent under write-through versus write-behind.

### Follow-up Questions
What requirement in: How do you keep cache and database consistent under write-through versus write-behind is decisive if throughput numbers are similar across options?

---
### Q114. What session durability expectations are realistic when Redis is only a cache?

### Short Answer
The senior-level decision is storing minimal session fields in Redis with TTL refresh and cookie holding only opaque session ID for: What session durability expectations are realistic when Redis is only a cache.

### Detailed Explanation
Hash fields allow partial updates; JSON strings simplify serialization but increase rewrite cost for: What session durability expectations are realistic when Redis is only a cache.

### Internal Working
Session loss on failover is acceptable for cache-only sessions but not if Redis is sole session store without replication discipline for: What session durability expectations are realistic when Redis is only a cache.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by rotating session ID on login and bounding payload size for: What session durability expectations are realistic when Redis is only a cache.

### Common Mistakes
Putting PII in session blobs without encryption or TTL is a common compliance mistake for: What session durability expectations are realistic when Redis is only a cache.

### Follow-up Questions
Which session fields must survive failover for: What session durability expectations are realistic when Redis is only a cache, and how do clients handle invalidation?

---
### Q115. How would you validate backup restores for AOF rewrite corruption edge cases?

### Short Answer
The practical Redis answer is matching RDB/AOF hybrid settings to acceptable data-loss window and restart time for: How would you validate backup restores for AOF rewrite corruption edge cases.

### Detailed Explanation
RDB gives compact snapshots; AOF gives finer durability with `appendfsync` tradeoffs — `everysec` is common but can lose ~1s on crash for: How would you validate backup restores for AOF rewrite corruption edge cases.

### Internal Working
BGSAVE/AOF rewrite forks the process; copy-on-write can double memory pressure during snapshots, affecting latency for: How would you validate backup restores for AOF rewrite corruption edge cases.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by testing crash-recovery drills and measuring fork latency under peak write load for: How would you validate backup restores for AOF rewrite corruption edge cases.

### Common Mistakes
Dangerous patterns include `SAVE` in production, `appendfsync always` without throughput headroom, and ignoring COW during maintenance for: How would you validate backup restores for AOF rewrite corruption edge cases.

### Follow-up Questions
What RPO does your chosen persistence mode actually guarantee for: How would you validate backup restores for AOF rewrite corruption edge cases after a hard kill test?

---
### Q116. How do you estimate Redis memory for N keys given average value size and encoding overhead?

### Short Answer
For this question, the architecturally correct Redis answer is separating logical key growth from allocator overhead using `used_memory`, RSS, and encoding inspection for: How do you estimate Redis memory for N keys given average value size and encoding overhead.

### Detailed Explanation
Redis picks compact encodings (listpack, intset) for small values and upgrades to hashtable/skiplist structures as data grows — memory cliffs often appear at encoding thresholds for: How do you estimate Redis memory for N keys given average value size and encoding overhead.

### Internal Working
`robj` wraps values with type metadata; jemalloc arenas and copy-on-write during persistence amplify RSS beyond `used_memory` for: How do you estimate Redis memory for N keys given average value size and encoding overhead.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology after sampling top keys with `MEMORY USAGE` and reviewing fragmentation ratio trends for: How do you estimate Redis memory for N keys given average value size and encoding overhead.

### Common Mistakes
Teams often optimize value bytes while ignoring metadata overhead, fragmentation, and fork-related RSS spikes for: How do you estimate Redis memory for N keys given average value size and encoding overhead.

### Follow-up Questions
Which encoding upgrade or key-shape change would you test first to reduce memory for: How do you estimate Redis memory for N keys given average value size and encoding overhead?

---
### Q117. When does adding replicas stop helping read scale because the primary is still the bottleneck?

### Short Answer
The production-grade Redis answer is treating replication as async by default and using `WAIT` or app-level checks only when stronger durability is required for: When does adding replicas stop helping read scale because the primary is still the bottleneck.

### Detailed Explanation
Replicas tail the replication stream; lag appears when network, disk, or apply speed falls behind write rate — partial resync needs adequate `repl-backlog-size` for: When does adding replicas stop helping read scale because the primary is still the bottleneck.

### Internal Working
Read-your-writes is not automatic on replicas; clients using replica reads must accept staleness or use primary reads after writes for: When does adding replicas stop helping read scale because the primary is still the bottleneck.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by correlating `master_repl_offset` with replica offsets and write spikes for: When does adding replicas stop helping read scale because the primary is still the bottleneck.

### Common Mistakes
Common mistakes include writable replicas, ignoring lag during incidents, and assuming replica reads are fresh for: When does adding replicas stop helping read scale because the primary is still the bottleneck.

### Follow-up Questions
Which writes in: When does adding replicas stop helping read scale because the primary is still the bottleneck require synchronous acknowledgment, and how will clients handle failover mid-transaction?

---
### Q118. How many primaries and replicas would you plan for a 500 GB working set with 200k ops/sec?

### Short Answer
The senior-level decision is treating replication as async by default and using `WAIT` or app-level checks only when stronger durability is required for: How many primaries and replicas would you plan for a 500 GB working set with 200k ops/sec.

### Detailed Explanation
Replicas tail the replication stream; lag appears when network, disk, or apply speed falls behind write rate — partial resync needs adequate `repl-backlog-size` for: How many primaries and replicas would you plan for a 500 GB working set with 200k ops/sec.

### Internal Working
Read-your-writes is not automatic on replicas; clients using replica reads must accept staleness or use primary reads after writes for: How many primaries and replicas would you plan for a 500 GB working set with 200k ops/sec.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by correlating `master_repl_offset` with replica offsets and write spikes for: How many primaries and replicas would you plan for a 500 GB working set with 200k ops/sec.

### Common Mistakes
Common mistakes include writable replicas, ignoring lag during incidents, and assuming replica reads are fresh for: How many primaries and replicas would you plan for a 500 GB working set with 200k ops/sec.

### Follow-up Questions
Which writes in: How many primaries and replicas would you plan for a 500 GB working set with 200k ops/sec require synchronous acknowledgment, and how will clients handle failover mid-transaction?

---
### Q119. What key design choices cause one Cluster shard to absorb disproportionate traffic?

### Short Answer
The practical Redis answer is designing keys around 16384 hash slots, hash tags for multi-key ops, and cluster-aware clients for: What key design choices cause one Cluster shard to absorb disproportionate traffic.

### Detailed Explanation
Slot = CRC16(key) mod 16384; MOVED is permanent redirect, ASK is temporary during migration — resharding moves slot ownership without changing key names for: What key design choices cause one Cluster shard to absorb disproportionate traffic.

### Internal Working
Multi-key commands, Lua, and transactions require all keys in the same slot — `{tag}` hash tags force colocation for: What key design choices cause one Cluster shard to absorb disproportionate traffic.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by monitoring per-node ops/sec, slot distribution, and MOVED/ASK rates during: What key design choices cause one Cluster shard to absorb disproportionate traffic.

### Common Mistakes
Typical failures: non-cluster clients, cross-slot MGET, and hot slots from poor key choice for: What key design choices cause one Cluster shard to absorb disproportionate traffic.

### Follow-up Questions
How would you rebalance slots or split hot keys if: What key design choices cause one Cluster shard to absorb disproportionate traffic appears in production metrics?

---
### Q120. How would you split a hot key across logical shards at the application layer?

### Short Answer
For this question, the architecturally correct Redis answer is combining TTL jitter, singleflight locks, and stale-while-revalidate to protect origin during: How would you split a hot key across logical shards at the application layer.

### Detailed Explanation
Breakdown hits when a hot key expires; avalanche when many keys expire together; penetration when misses flood DB for absent keys for: How would you split a hot key across logical shards at the application layer.

### Internal Working
Mitigations include probabilistic early refresh, Bloom filters or short negative TTL, and request coalescing for: How would you split a hot key across logical shards at the application layer.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by load-testing synchronized expiry and hot-key miss scenarios for: How would you split a hot key across logical shards at the application layer.

### Common Mistakes
Same TTL on all keys and caching null forever are classic self-inflicted outages for: How would you split a hot key across logical shards at the application layer.

### Follow-up Questions
Which mitigation layer (jitter, lock, Bloom, local cache) is first-line for: How would you split a hot key across logical shards at the application layer in your architecture?

---
### Q121. When does horizontal Cluster scaling hit coordination overhead diminishing returns?

### Short Answer
The production-grade Redis answer is designing keys around 16384 hash slots, hash tags for multi-key ops, and cluster-aware clients for: When does horizontal Cluster scaling hit coordination overhead diminishing returns.

### Detailed Explanation
Slot = CRC16(key) mod 16384; MOVED is permanent redirect, ASK is temporary during migration — resharding moves slot ownership without changing key names for: When does horizontal Cluster scaling hit coordination overhead diminishing returns.

### Internal Working
Multi-key commands, Lua, and transactions require all keys in the same slot — `{tag}` hash tags force colocation for: When does horizontal Cluster scaling hit coordination overhead diminishing returns.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by monitoring per-node ops/sec, slot distribution, and MOVED/ASK rates during: When does horizontal Cluster scaling hit coordination overhead diminishing returns.

### Common Mistakes
Typical failures: non-cluster clients, cross-slot MGET, and hot slots from poor key choice for: When does horizontal Cluster scaling hit coordination overhead diminishing returns.

### Follow-up Questions
How would you rebalance slots or split hot keys if: When does horizontal Cluster scaling hit coordination overhead diminishing returns appears in production metrics?

---
### Q122. How do global rate limit counters scale when a single INCR key becomes hot?

### Short Answer
The senior-level decision is picking fixed, sliding, or token-bucket algorithms based on burst tolerance and accuracy needs for: How do global rate limit counters scale when a single INCR key becomes hot.

### Detailed Explanation
INCR + EXPIRE gives fixed windows; sorted sets give sliding windows; Lua gives accurate token refill for: How do global rate limit counters scale when a single INCR key becomes hot.

### Internal Working
Global counters can become hot keys — shard counter keys or use local aggregation for: How do global rate limit counters scale when a single INCR key becomes hot.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by testing boundary bursts at window edges for: How do global rate limit counters scale when a single INCR key becomes hot.

### Common Mistakes
Fixed windows allow 2× burst at boundaries; ignoring atomicity on compound checks causes drift for: How do global rate limit counters scale when a single INCR key becomes hot.

### Follow-up Questions
How would you shard a global rate limit key if: How do global rate limit counters scale when a single INCR key becomes hot saturates one Redis primary?

---
### Q123. What growth triggers move you from one large instance to Cluster beyond memory alone?

### Short Answer
The practical Redis answer is designing keys around 16384 hash slots, hash tags for multi-key ops, and cluster-aware clients for: What growth triggers move you from one large instance to Cluster beyond memory alone.

### Detailed Explanation
Slot = CRC16(key) mod 16384; MOVED is permanent redirect, ASK is temporary during migration — resharding moves slot ownership without changing key names for: What growth triggers move you from one large instance to Cluster beyond memory alone.

### Internal Working
Multi-key commands, Lua, and transactions require all keys in the same slot — `{tag}` hash tags force colocation for: What growth triggers move you from one large instance to Cluster beyond memory alone.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by monitoring per-node ops/sec, slot distribution, and MOVED/ASK rates during: What growth triggers move you from one large instance to Cluster beyond memory alone.

### Common Mistakes
Typical failures: non-cluster clients, cross-slot MGET, and hot slots from poor key choice for: What growth triggers move you from one large instance to Cluster beyond memory alone.

### Follow-up Questions
How would you rebalance slots or split hot keys if: What growth triggers move you from one large instance to Cluster beyond memory alone appears in production metrics?

---
### Q124. How does replication factor affect memory and network costs at 10x data growth?

### Short Answer
For this question, the architecturally correct Redis answer is treating replication as async by default and using `WAIT` or app-level checks only when stronger durability is required for: How does replication factor affect memory and network costs at 10x data growth.

### Detailed Explanation
Replicas tail the replication stream; lag appears when network, disk, or apply speed falls behind write rate — partial resync needs adequate `repl-backlog-size` for: How does replication factor affect memory and network costs at 10x data growth.

### Internal Working
Read-your-writes is not automatic on replicas; clients using replica reads must accept staleness or use primary reads after writes for: How does replication factor affect memory and network costs at 10x data growth.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by correlating `master_repl_offset` with replica offsets and write spikes for: How does replication factor affect memory and network costs at 10x data growth.

### Common Mistakes
Common mistakes include writable replicas, ignoring lag during incidents, and assuming replica reads are fresh for: How does replication factor affect memory and network costs at 10x data growth.

### Follow-up Questions
Which writes in: How does replication factor affect memory and network costs at 10x data growth require synchronous acknowledgment, and how will clients handle failover mid-transaction?

---
### Q125. When do Streams with many consumer groups create memory pressure versus Kafka retention?

### Short Answer
The production-grade Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: When do Streams with many consumer groups create memory pressure versus Kafka retention.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: When do Streams with many consumer groups create memory pressure versus Kafka retention.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: When do Streams with many consumer groups create memory pressure versus Kafka retention.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by documenting ADR assumptions and exit strategy if load doubles for: When do Streams with many consumer groups create memory pressure versus Kafka retention.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: When do Streams with many consumer groups create memory pressure versus Kafka retention.

### Follow-up Questions
What requirement in: When do Streams with many consumer groups create memory pressure versus Kafka retention is decisive if throughput numbers are similar across options?

---
### Q126. How would you plan slot migration windows to scale out Cluster without client outages?

### Short Answer
The senior-level decision is designing keys around 16384 hash slots, hash tags for multi-key ops, and cluster-aware clients for: How would you plan slot migration windows to scale out Cluster without client outages.

### Detailed Explanation
Slot = CRC16(key) mod 16384; MOVED is permanent redirect, ASK is temporary during migration — resharding moves slot ownership without changing key names for: How would you plan slot migration windows to scale out Cluster without client outages.

### Internal Working
Multi-key commands, Lua, and transactions require all keys in the same slot — `{tag}` hash tags force colocation for: How would you plan slot migration windows to scale out Cluster without client outages.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by monitoring per-node ops/sec, slot distribution, and MOVED/ASK rates during: How would you plan slot migration windows to scale out Cluster without client outages.

### Common Mistakes
Typical failures: non-cluster clients, cross-slot MGET, and hot slots from poor key choice for: How would you plan slot migration windows to scale out Cluster without client outages.

### Follow-up Questions
How would you rebalance slots or split hot keys if: How would you plan slot migration windows to scale out Cluster without client outages appears in production metrics?

---
### Q127. What is the scalability ceiling of single-threaded command processing per core?

### Short Answer
The practical Redis answer is treating Redis as a single-threaded command processor with optional I/O threading, then choosing HA topology to match RPO/RTO for: What is the scalability ceiling of single-threaded command processing per core.

### Detailed Explanation
Redis throughput scales vertically per primary until CPU, memory, or hot-key skew dominates; Sentinel and Cluster solve availability and horizontal scale, not magic parallelism on one key for: What is the scalability ceiling of single-threaded command processing per core.

### Internal Working
Commands execute serially on the event loop, so long operations block all clients on that node — architecture must keep hot paths O(1) and shard before CPU saturates for: What is the scalability ceiling of single-threaded command processing per core.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew when comparing standalone, Sentinel, and Cluster for: What is the scalability ceiling of single-threaded command processing per core.

### Common Mistakes
A common mistake is assuming Redis is multi-threaded for commands or colocating unrelated blast-radius workloads on one cluster for: What is the scalability ceiling of single-threaded command processing per core.

### Follow-up Questions
What failover time, durability window, and client retry contract would you document before choosing topology for: What is the scalability ceiling of single-threaded command processing per core?

---
### Q128. How do connection counts from thousands of pods affect Redis scalability in Kubernetes?

### Short Answer
For this question, the architecturally correct Redis answer is matching Redis data type to access pattern — not defaulting everything to JSON strings for: How do connection counts from thousands of pods affect Redis scalability in Kubernetes.

### Detailed Explanation
Pick strings for counters/cache blobs, hashes for field updates, sets/ZSETs for uniqueness/ranking, Streams for durable queues for: How do connection counts from thousands of pods affect Redis scalability in Kubernetes.

### Internal Working
Encoding upgrades and command complexity (O(N) vs O(1)) follow from type and size choices for: How do connection counts from thousands of pods affect Redis scalability in Kubernetes.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by validating command complexity and memory per key for: How do connection counts from thousands of pods affect Redis scalability in Kubernetes.

### Common Mistakes
Using `HGETALL` or `SMEMBERS` on large collections blocks the event loop for: How do connection counts from thousands of pods affect Redis scalability in Kubernetes.

### Follow-up Questions
Which type would you choose for: How do connection counts from thousands of pods affect Redis scalability in Kubernetes, and what command path proves it under peak cardinality?

---
### Q129. When does caching null results with short TTL scale better than Bloom filters?

### Short Answer
The production-grade Redis answer is combining TTL jitter, singleflight locks, and stale-while-revalidate to protect origin during: When does caching null results with short TTL scale better than Bloom filters.

### Detailed Explanation
Breakdown hits when a hot key expires; avalanche when many keys expire together; penetration when misses flood DB for absent keys for: When does caching null results with short TTL scale better than Bloom filters.

### Internal Working
Mitigations include probabilistic early refresh, Bloom filters or short negative TTL, and request coalescing for: When does caching null results with short TTL scale better than Bloom filters.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by load-testing synchronized expiry and hot-key miss scenarios for: When does caching null results with short TTL scale better than Bloom filters.

### Common Mistakes
Same TTL on all keys and caching null forever are classic self-inflicted outages for: When does caching null results with short TTL scale better than Bloom filters.

### Follow-up Questions
Which mitigation layer (jitter, lock, Bloom, local cache) is first-line for: When does caching null results with short TTL scale better than Bloom filters in your architecture?

---
### Q130. How would you model year-over-year key growth for finance-approved capacity budgets?

### Short Answer
The senior-level decision is sizing memory as key count × (value + metadata overhead) plus replication and headroom for fork for: How would you model year-over-year key growth for finance-approved capacity budgets.

### Detailed Explanation
Plan growth with key cardinality forecasts, encoding assumptions, and replica factor — Cluster adds coordination overhead for: How would you model year-over-year key growth for finance-approved capacity budgets.

### Internal Working
Connection count from many pods can exhaust `maxclients` before memory fills for: How would you model year-over-year key growth for finance-approved capacity budgets.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts with load tests that include failover and snapshot windows for: How would you model year-over-year key growth for finance-approved capacity budgets.

### Common Mistakes
Sizing only for data bytes without overhead, replicas, or COW margin causes emergency scale events for: How would you model year-over-year key growth for finance-approved capacity budgets.

### Follow-up Questions
At what memory or ops/sec threshold would you trigger horizontal scale for: How would you model year-over-year key growth for finance-approved capacity budgets?

---
### Q131. Walk through cache-aside read and write invalidation for an updated product record.

### Short Answer
The practical Redis answer is deleting or updating cache keys on write and broadcasting invalidation when multi-tier caches exist for: Walk through cache-aside read and write invalidation for an updated product record..

### Detailed Explanation
Write-through updates DB and cache together; write-behind updates cache first with async flush — each shifts consistency risk for: Walk through cache-aside read and write invalidation for an updated product record..

### Internal Working
Pub/Sub can signal app-local cache eviction, but Redis remains source for shared cache layer for: Walk through cache-aside read and write invalidation for an updated product record..

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by defining who invalidates on partial updates and out-of-order writes for: Walk through cache-aside read and write invalidation for an updated product record..

### Common Mistakes
Updating DB without cache delete is the most common stale-data bug for: Walk through cache-aside read and write invalidation for an updated product record..

### Follow-up Questions
How do you invalidate related keys (lists, aggregates) when: Walk through cache-aside read and write invalidation for an updated product record. updates one entity?

---
### Q132. How does write-behind improve write latency while risking data loss on crash?

### Short Answer
For this question, the architecturally correct Redis answer is deleting or updating cache keys on write and broadcasting invalidation when multi-tier caches exist for: How does write-behind improve write latency while risking data loss on crash.

### Detailed Explanation
Write-through updates DB and cache together; write-behind updates cache first with async flush — each shifts consistency risk for: How does write-behind improve write latency while risking data loss on crash.

### Internal Working
Pub/Sub can signal app-local cache eviction, but Redis remains source for shared cache layer for: How does write-behind improve write latency while risking data loss on crash.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by defining who invalidates on partial updates and out-of-order writes for: How does write-behind improve write latency while risking data loss on crash.

### Common Mistakes
Updating DB without cache delete is the most common stale-data bug for: How does write-behind improve write latency while risking data loss on crash.

### Follow-up Questions
How do you invalidate related keys (lists, aggregates) when: How does write-behind improve write latency while risking data loss on crash updates one entity?

---
### Q133. What singleflight or lock pattern prevents rebuild stampede on a popular cache miss?

### Short Answer
The production-grade Redis answer is combining TTL jitter, singleflight locks, and stale-while-revalidate to protect origin during: What singleflight or lock pattern prevents rebuild stampede on a popular cache miss.

### Detailed Explanation
Breakdown hits when a hot key expires; avalanche when many keys expire together; penetration when misses flood DB for absent keys for: What singleflight or lock pattern prevents rebuild stampede on a popular cache miss.

### Internal Working
Mitigations include probabilistic early refresh, Bloom filters or short negative TTL, and request coalescing for: What singleflight or lock pattern prevents rebuild stampede on a popular cache miss.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by load-testing synchronized expiry and hot-key miss scenarios for: What singleflight or lock pattern prevents rebuild stampede on a popular cache miss.

### Common Mistakes
Same TTL on all keys and caching null forever are classic self-inflicted outages for: What singleflight or lock pattern prevents rebuild stampede on a popular cache miss.

### Follow-up Questions
Which mitigation layer (jitter, lock, Bloom, local cache) is first-line for: What singleflight or lock pattern prevents rebuild stampede on a popular cache miss in your architecture?

---
### Q134. How would you implement TTL jitter to mitigate synchronized expiry avalanches?

### Short Answer
The senior-level decision is combining TTL jitter, singleflight locks, and stale-while-revalidate to protect origin during: How would you implement TTL jitter to mitigate synchronized expiry avalanches.

### Detailed Explanation
Breakdown hits when a hot key expires; avalanche when many keys expire together; penetration when misses flood DB for absent keys for: How would you implement TTL jitter to mitigate synchronized expiry avalanches.

### Internal Working
Mitigations include probabilistic early refresh, Bloom filters or short negative TTL, and request coalescing for: How would you implement TTL jitter to mitigate synchronized expiry avalanches.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by load-testing synchronized expiry and hot-key miss scenarios for: How would you implement TTL jitter to mitigate synchronized expiry avalanches.

### Common Mistakes
Same TTL on all keys and caching null forever are classic self-inflicted outages for: How would you implement TTL jitter to mitigate synchronized expiry avalanches.

### Follow-up Questions
Which mitigation layer (jitter, lock, Bloom, local cache) is first-line for: How would you implement TTL jitter to mitigate synchronized expiry avalanches in your architecture?

---
### Q135. When is a Bloom filter worth adding versus caching empty placeholders?

### Short Answer
The practical Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: When is a Bloom filter worth adding versus caching empty placeholders.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: When is a Bloom filter worth adding versus caching empty placeholders.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: When is a Bloom filter worth adding versus caching empty placeholders.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by documenting ADR assumptions and exit strategy if load doubles for: When is a Bloom filter worth adding versus caching empty placeholders.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: When is a Bloom filter worth adding versus caching empty placeholders.

### Follow-up Questions
What requirement in: When is a Bloom filter worth adding versus caching empty placeholders is decisive if throughput numbers are similar across options?

---
### Q136. How do you implement a correct distributed lock release with token verification?

### Short Answer
For this question, the architecturally correct Redis answer is using `SET key token NX PX ttl` plus Lua compare-and-del unlock, with fencing tokens for durable side effects for: How do you implement a correct distributed lock release with token verification.

### Detailed Explanation
Locks auto-expire via TTL to survive client crashes, but TTL expiry before work finishes allows double execution — fencing tokens monotonically guard downstream storage for: How do you implement a correct distributed lock release with token verification.

### Internal Working
Redlock across independent masters is debated; single-instance locks are simpler but fail with primary loss unless fencing compensates for: How do you implement a correct distributed lock release with token verification.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by testing GC pause and clock skew scenarios against lock TTL for: How do you implement a correct distributed lock release with token verification.

### Common Mistakes
Never use `SETNX` without TTL or `DEL` without token check — both cause correctness incidents for: How do you implement a correct distributed lock release with token verification.

### Follow-up Questions
What fencing mechanism protects your storage layer if: How do you implement a correct distributed lock release with token verification outlives the Redis lock TTL?

---
### Q137. Why prefer Lua over WATCH/MULTI for contested hot keys?

### Short Answer
The production-grade Redis answer is combining TTL jitter, singleflight locks, and stale-while-revalidate to protect origin during: Why prefer Lua over WATCH/MULTI for contested hot keys.

### Detailed Explanation
Breakdown hits when a hot key expires; avalanche when many keys expire together; penetration when misses flood DB for absent keys for: Why prefer Lua over WATCH/MULTI for contested hot keys.

### Internal Working
Mitigations include probabilistic early refresh, Bloom filters or short negative TTL, and request coalescing for: Why prefer Lua over WATCH/MULTI for contested hot keys.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by load-testing synchronized expiry and hot-key miss scenarios for: Why prefer Lua over WATCH/MULTI for contested hot keys.

### Common Mistakes
Same TTL on all keys and caching null forever are classic self-inflicted outages for: Why prefer Lua over WATCH/MULTI for contested hot keys.

### Follow-up Questions
Which mitigation layer (jitter, lock, Bloom, local cache) is first-line for: Why prefer Lua over WATCH/MULTI for contested hot keys in your architecture?

---
### Q138. How does XREADGROUP BLOCK behave differently from BLPOP for worker pools?

### Short Answer
The senior-level decision is using consumer groups for at-least-once work queues with explicit XACK and pending reclaim for: How does XREADGROUP BLOCK behave differently from BLPOP for worker pools.

### Detailed Explanation
Streams append entries with auto IDs; consumer groups track per-consumer progress and pending entries for: How does XREADGROUP BLOCK behave differently from BLPOP for worker pools.

### Internal Working
Without XACK, messages stay pending; crashed consumers require XCLAIM/XAUTOCLAIM after idle threshold for: How does XREADGROUP BLOCK behave differently from BLPOP for worker pools.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by monitoring XPENDING depth and trimming with MAXLEN ~ for: How does XREADGROUP BLOCK behave differently from BLPOP for worker pools.

### Common Mistakes
Treating Streams as exactly-once without idempotent handlers is a common correctness gap for: How does XREADGROUP BLOCK behave differently from BLPOP for worker pools.

### Follow-up Questions
What idempotency key and poison-message policy would you pair with: How does XREADGROUP BLOCK behave differently from BLPOP for worker pools?

---
### Q139. What is the recovery procedure for poison messages stuck in XPENDING?

### Short Answer
The practical Redis answer is using consumer groups for at-least-once work queues with explicit XACK and pending reclaim for: What is the recovery procedure for poison messages stuck in XPENDING.

### Detailed Explanation
Streams append entries with auto IDs; consumer groups track per-consumer progress and pending entries for: What is the recovery procedure for poison messages stuck in XPENDING.

### Internal Working
Without XACK, messages stay pending; crashed consumers require XCLAIM/XAUTOCLAIM after idle threshold for: What is the recovery procedure for poison messages stuck in XPENDING.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by monitoring XPENDING depth and trimming with MAXLEN ~ for: What is the recovery procedure for poison messages stuck in XPENDING.

### Common Mistakes
Treating Streams as exactly-once without idempotent handlers is a common correctness gap for: What is the recovery procedure for poison messages stuck in XPENDING.

### Follow-up Questions
What idempotency key and poison-message policy would you pair with: What is the recovery procedure for poison messages stuck in XPENDING?

---
### Q140. How would you choose fixed-window versus sliding-window rate limits for an API gateway?

### Short Answer
For this question, the architecturally correct Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: How would you choose fixed-window versus sliding-window rate limits for an API gateway.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: How would you choose fixed-window versus sliding-window rate limits for an API gateway.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: How would you choose fixed-window versus sliding-window rate limits for an API gateway.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by documenting ADR assumptions and exit strategy if load doubles for: How would you choose fixed-window versus sliding-window rate limits for an API gateway.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: How would you choose fixed-window versus sliding-window rate limits for an API gateway.

### Follow-up Questions
What requirement in: How would you choose fixed-window versus sliding-window rate limits for an API gateway is decisive if throughput numbers are similar across options?

---
### Q141. What session fields belong in Redis versus only in signed cookies?

### Short Answer
The production-grade Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: What session fields belong in Redis versus only in signed cookies.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: What session fields belong in Redis versus only in signed cookies.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: What session fields belong in Redis versus only in signed cookies.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by documenting ADR assumptions and exit strategy if load doubles for: What session fields belong in Redis versus only in signed cookies.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: What session fields belong in Redis versus only in signed cookies.

### Follow-up Questions
What requirement in: What session fields belong in Redis versus only in signed cookies is decisive if throughput numbers are similar across options?

---
### Q142. How does Pub/Sub-based cache invalidation avoid stale local caches in multi-tier apps?

### Short Answer
The senior-level decision is deleting or updating cache keys on write and broadcasting invalidation when multi-tier caches exist for: How does Pub/Sub-based cache invalidation avoid stale local caches in multi-tier apps.

### Detailed Explanation
Write-through updates DB and cache together; write-behind updates cache first with async flush — each shifts consistency risk for: How does Pub/Sub-based cache invalidation avoid stale local caches in multi-tier apps.

### Internal Working
Pub/Sub can signal app-local cache eviction, but Redis remains source for shared cache layer for: How does Pub/Sub-based cache invalidation avoid stale local caches in multi-tier apps.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by defining who invalidates on partial updates and out-of-order writes for: How does Pub/Sub-based cache invalidation avoid stale local caches in multi-tier apps.

### Common Mistakes
Updating DB without cache delete is the most common stale-data bug for: How does Pub/Sub-based cache invalidation avoid stale local caches in multi-tier apps.

### Follow-up Questions
How do you invalidate related keys (lists, aggregates) when: How does Pub/Sub-based cache invalidation avoid stale local caches in multi-tier apps updates one entity?

---
### Q143. When should lists be retired in favor of Streams for work queues?

### Short Answer
The practical Redis answer is using consumer groups for at-least-once work queues with explicit XACK and pending reclaim for: When should lists be retired in favor of Streams for work queues.

### Detailed Explanation
Streams append entries with auto IDs; consumer groups track per-consumer progress and pending entries for: When should lists be retired in favor of Streams for work queues.

### Internal Working
Without XACK, messages stay pending; crashed consumers require XCLAIM/XAUTOCLAIM after idle threshold for: When should lists be retired in favor of Streams for work queues.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by monitoring XPENDING depth and trimming with MAXLEN ~ for: When should lists be retired in favor of Streams for work queues.

### Common Mistakes
Treating Streams as exactly-once without idempotent handlers is a common correctness gap for: When should lists be retired in favor of Streams for work queues.

### Follow-up Questions
What idempotency key and poison-message policy would you pair with: When should lists be retired in favor of Streams for work queues?

---
### Q144. How do hash tags enable atomic multi-key updates in Cluster for order line items?

### Short Answer
For this question, the architecturally correct Redis answer is using MULTI/EXEC for simple atomic batches and Lua for contested hot keys where WATCH abort rates would be high for: How do hash tags enable atomic multi-key updates in Cluster for order line items.

### Detailed Explanation
MULTI queues commands; EXEC runs them serially without interleaving — failed commands do not roll back earlier commands in the batch for: How do hash tags enable atomic multi-key updates in Cluster for order line items.

### Internal Working
WATCH provides optimistic locking by aborting EXEC if watched keys changed; pipelines batch without atomicity for: How do hash tags enable atomic multi-key updates in Cluster for order line items.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by keeping transaction blocks short and preferring Lua for compare-and-set on hot keys for: How do hash tags enable atomic multi-key updates in Cluster for order line items.

### Common Mistakes
Expecting RDBMS-style rollback or long MULTI blocks on hot keys are common production mistakes for: How do hash tags enable atomic multi-key updates in Cluster for order line items.

### Follow-up Questions
When would Lua replace MULTI/EXEC for: How do hash tags enable atomic multi-key updates in Cluster for order line items, and what cluster slot constraints apply?

---
### Q145. What pipeline patterns reduce round trips in bulk session refresh jobs?

### Short Answer
The production-grade Redis answer is using RESP over TCP with connection pooling and pipelining to cut round trips without expecting multi-command parallelism on the server for: What pipeline patterns reduce round trips in bulk session refresh jobs.

### Detailed Explanation
Pipelining batches many commands in one RTT while Redis still executes them sequentially — throughput gains come from network efficiency, not parallel command threads for: What pipeline patterns reduce round trips in bulk session refresh jobs.

### Internal Working
Cluster clients must handle MOVED/ASK redirects and maintain slot maps; protocol-level retries differ from application idempotency for: What pipeline patterns reduce round trips in bulk session refresh jobs.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by profiling client RTT versus server `slowlog` entries for: What pipeline patterns reduce round trips in bulk session refresh jobs.

### Common Mistakes
A frequent mistake is huge pipelines without backpressure, causing timeouts and memory pressure on both client and server for: What pipeline patterns reduce round trips in bulk session refresh jobs.

### Follow-up Questions
What pipeline batch size and timeout would you cap for: What pipeline patterns reduce round trips in bulk session refresh jobs given your p99 SLO?

---
### Q146. How would you implement a token bucket refill accurately with Lua?

### Short Answer
The senior-level decision is using `SET key token NX PX ttl` plus Lua compare-and-del unlock, with fencing tokens for durable side effects for: How would you implement a token bucket refill accurately with Lua.

### Detailed Explanation
Locks auto-expire via TTL to survive client crashes, but TTL expiry before work finishes allows double execution — fencing tokens monotonically guard downstream storage for: How would you implement a token bucket refill accurately with Lua.

### Internal Working
Redlock across independent masters is debated; single-instance locks are simpler but fail with primary loss unless fencing compensates for: How would you implement a token bucket refill accurately with Lua.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by testing GC pause and clock skew scenarios against lock TTL for: How would you implement a token bucket refill accurately with Lua.

### Common Mistakes
Never use `SETNX` without TTL or `DEL` without token check — both cause correctness incidents for: How would you implement a token bucket refill accurately with Lua.

### Follow-up Questions
What fencing mechanism protects your storage layer if: How would you implement a token bucket refill accurately with Lua outlives the Redis lock TTL?

---
### Q147. What are the tradeoffs of caching entire DTOs versus hash field projections?

### Short Answer
The practical Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: What are the tradeoffs of caching entire DTOs versus hash field projections.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: What are the tradeoffs of caching entire DTOs versus hash field projections.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: What are the tradeoffs of caching entire DTOs versus hash field projections.

### Production Notes
You justify it by measuring p99 latency, memory headroom, and failover behavior under realistic skew by documenting ADR assumptions and exit strategy if load doubles for: What are the tradeoffs of caching entire DTOs versus hash field projections.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: What are the tradeoffs of caching entire DTOs versus hash field projections.

### Follow-up Questions
What requirement in: What are the tradeoffs of caching entire DTOs versus hash field projections is decisive if throughput numbers are similar across options?

---
### Q148. How do you prevent double consumption when a consumer crashes before XACK?

### Short Answer
For this question, the architecturally correct Redis answer is using consumer groups for at-least-once work queues with explicit XACK and pending reclaim for: How do you prevent double consumption when a consumer crashes before XACK.

### Detailed Explanation
Streams append entries with auto IDs; consumer groups track per-consumer progress and pending entries for: How do you prevent double consumption when a consumer crashes before XACK.

### Internal Working
Without XACK, messages stay pending; crashed consumers require XCLAIM/XAUTOCLAIM after idle threshold for: How do you prevent double consumption when a consumer crashes before XACK.

### Production Notes
You justify it by proving behavior with INFO, slowlog, and workload replay before changing topology by monitoring XPENDING depth and trimming with MAXLEN ~ for: How do you prevent double consumption when a consumer crashes before XACK.

### Common Mistakes
Treating Streams as exactly-once without idempotent handlers is a common correctness gap for: How do you prevent double consumption when a consumer crashes before XACK.

### Follow-up Questions
What idempotency key and poison-message policy would you pair with: How do you prevent double consumption when a consumer crashes before XACK?

---
### Q149. When does Redis Pub/Sub suffice for feature-flag propagation versus polling?

### Short Answer
The production-grade Redis answer is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: When does Redis Pub/Sub suffice for feature-flag propagation versus polling.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: When does Redis Pub/Sub suffice for feature-flag propagation versus polling.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: When does Redis Pub/Sub suffice for feature-flag propagation versus polling.

### Production Notes
You justify it by minimizing hot-key blast radius and single-thread CPU contention by documenting ADR assumptions and exit strategy if load doubles for: When does Redis Pub/Sub suffice for feature-flag propagation versus polling.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: When does Redis Pub/Sub suffice for feature-flag propagation versus polling.

### Follow-up Questions
What requirement in: When does Redis Pub/Sub suffice for feature-flag propagation versus polling is decisive if throughput numbers are similar across options?

---
### Q150. How would you design negative caching TTL differently for bots versus real users?

### Short Answer
The senior-level decision is comparing Redis to alternatives on data model, durability, ops model, and failure semantics — not feature checklists for: How would you design negative caching TTL differently for bots versus real users.

### Detailed Explanation
Redis offers rich structures and optional persistence; Memcached is simpler cache; Kafka/RabbitMQ excel at durable messaging scale for: How would you design negative caching TTL differently for bots versus real users.

### Internal Working
Using Redis as a message bus works for moderate throughput with Streams; very large retention or routing complexity may favor dedicated brokers for: How would you design negative caching TTL differently for bots versus real users.

### Production Notes
You justify it by aligning durability settings with business RPO/RTO and client retry contracts by documenting ADR assumptions and exit strategy if load doubles for: How would you design negative caching TTL differently for bots versus real users.

### Common Mistakes
Resume-driven Redis adoption without ops maturity for Sentinel/Cluster causes painful incidents for: How would you design negative caching TTL differently for bots versus real users.

### Follow-up Questions
What requirement in: How would you design negative caching TTL differently for bots versus real users is decisive if throughput numbers are similar across options?

---

<!-- interview-guide-answers:end -->

---

## See Also

- [Architect Questions](/redis-cheatsheet/08-interview-guide/architect-questions/)
- [Troubleshooting Questions](/redis-cheatsheet/08-interview-guide/troubleshooting-questions/)
- [Performance Questions](/redis-cheatsheet/08-interview-guide/performance-questions/)
- [Redis Handbook Index](/redis-cheatsheet/)
