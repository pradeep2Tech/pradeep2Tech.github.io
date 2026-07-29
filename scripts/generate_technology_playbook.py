"""Generate Technology Playbook pages from data/technology_playbook_modules.yaml."""
from __future__ import annotations

import textwrap
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content" / "technology-playbook"
DATA = ROOT / "data"

# Hand-polished pages — generator skips these slugs.
SKIP_SLUGS = frozenset({
    "kafka-vs-rabbitmq",
    "how-to-choose-database",
    "how-to-choose-api-protocol",
})

MICROSERVICES_DEEP_DIVES = {
    "event-driven-architecture": "/microservices/event-driven-architecture-log-streaming/",
    "cqrs-pattern": "/microservices/cqrs-event-sourcing/",
    "saga-pattern": "/microservices/saga-pattern-distributed-transactions/",
    "outbox-pattern": "/database-handbook/transactional-outbox-pattern/",
    "strangler-pattern": "/microservices/strangler-fig-application-pattern/",
    "circuit-breaker-pattern": "/microservices/circuit-breaker-pattern/",
    "bulkhead-pattern": "/microservices/bulkhead-isolation-pattern/",
    "sidecar-pattern": "/microservices/sidecar-integration-pattern/",
    "service-mesh": "/microservices/service-mesh-architecture/",
    "api-gateway": "/microservices/api-gateway-bff-pattern/",
    "bff-pattern": "/microservices/api-gateway-bff-pattern/",
    "microservices-architecture": "/microservices/architectural-pragmatist-monolith-vs-microservices/",
    "monolith-architecture": "/microservices/architectural-pragmatist-monolith-vs-microservices/",
    "docker": "/microservices/application-containerization-docker/",
    "kubernetes": "/microservices/declarative-container-orchestration-kubernetes/",
}

# slug -> (title, shortTitle, description, category tag, db_type optional)
TOPIC_META: dict[str, tuple] = {
    "monolith-architecture": (
        "Monolith Architecture",
        "Monolith",
        "Single deployable unit with shared codebase and database — when simplicity beats distribution.",
        "architecture",
    ),
    "modular-monolith-architecture": (
        "Modular Monolith Architecture",
        "Modular Monolith",
        "Monolith with strict module boundaries — a pragmatic step before microservices.",
        "architecture",
    ),
    "microservices-architecture": (
        "Microservices Architecture",
        "Microservices",
        "Independently deployable services with decentralized data — scale teams and failure domains.",
        "architecture",
    ),
    "soa-architecture": (
        "Service-Oriented Architecture (SOA)",
        "SOA",
        "Enterprise service bus era integration — shared contracts, orchestration, and governance.",
        "architecture",
    ),
    "event-driven-architecture": (
        "Event-Driven Architecture",
        "Event-Driven",
        "Loose coupling via events and async consumers — scale write paths and decouple teams.",
        "architecture",
    ),
    "cqrs-pattern": (
        "CQRS Pattern",
        "CQRS",
        "Separate read and write models — optimize queries without polluting the transactional model.",
        "architecture",
    ),
    "saga-pattern": (
        "Saga Pattern",
        "Saga",
        "Distributed transactions via compensating steps — coordinate long-running business flows.",
        "architecture",
    ),
    "outbox-pattern": (
        "Outbox Pattern",
        "Outbox",
        "Reliable event publishing from the database transaction — no dual-write inconsistency.",
        "architecture",
    ),
    "strangler-pattern": (
        "Strangler Fig Pattern",
        "Strangler",
        "Incrementally replace legacy systems by routing traffic to new services over time.",
        "architecture",
    ),
    "circuit-breaker-pattern": (
        "Circuit Breaker Pattern",
        "Circuit Breaker",
        "Fail fast when dependencies are unhealthy — prevent cascade failures across services.",
        "architecture",
    ),
    "bulkhead-pattern": (
        "Bulkhead Pattern",
        "Bulkhead",
        "Isolate thread pools and resources so one slow dependency cannot sink the whole service.",
        "architecture",
    ),
    "sidecar-pattern": (
        "Sidecar Pattern",
        "Sidecar",
        "Co-locate cross-cutting concerns (proxy, logging, mTLS) in a companion container.",
        "architecture",
    ),
    "service-mesh": (
        "Service Mesh",
        "Service Mesh",
        "Infrastructure layer for service-to-service traffic — mTLS, retries, observability at scale.",
        "architecture",
    ),
    "api-gateway": (
        "API Gateway",
        "API Gateway",
        "Single entry point for clients — routing, auth, rate limiting, and protocol translation.",
        "architecture",
    ),
    "bff-pattern": (
        "Backend for Frontend (BFF)",
        "BFF",
        "Tailored API per client channel — mobile, web, partner — without bloating core services.",
        "architecture",
    ),
    "how-to-choose-database": (
        "How to Choose a Database",
        "Choose Database",
        "Decision framework for relational, document, wide-column, graph, and specialized stores.",
        "decision",
    ),
    "how-to-choose-cache": (
        "How to Choose a Cache",
        "Choose Cache",
        "In-memory vs distributed cache — consistency, TTL, eviction, and session vs object caching.",
        "decision",
    ),
    "how-to-choose-message-broker": (
        "How to Choose a Message Broker",
        "Choose Broker",
        "Queue vs log, ordering guarantees, replay, and cloud-managed vs self-hosted brokers.",
        "decision",
    ),
    "how-to-choose-api-protocol": (
        "How to Choose an API Protocol",
        "Choose API Protocol",
        "REST, gRPC, GraphQL, and async events — match protocol to client and coupling needs.",
        "decision",
    ),
    "how-to-choose-search-engine": (
        "How to Choose a Search Engine",
        "Choose Search",
        "Full-text, faceted search, and log analytics — Elasticsearch vs OpenSearch vs Solr.",
        "decision",
    ),
    "how-to-choose-object-storage": (
        "How to Choose Object Storage",
        "Choose Object Storage",
        "S3-compatible blobs for documents, media, backups, and data lake landing zones.",
        "decision",
    ),
    "how-to-choose-workflow-engine": (
        "How to Choose a Workflow Engine",
        "Choose Workflow",
        "Long-running orchestration vs DAG scheduling — Temporal, Camunda, Airflow trade-offs.",
        "decision",
    ),
    "how-to-choose-rule-engine": (
        "How to Choose a Rule Engine",
        "Choose Rules",
        "Business rules outside code — Drools, decision tables, and low-code rule services.",
        "decision",
    ),
    "how-to-choose-scheduler": (
        "How to Choose a Scheduler",
        "Choose Scheduler",
        "Cron, enterprise batch schedulers, and Kubernetes-native job triggers.",
        "decision",
    ),
    "how-to-choose-batch-engine": (
        "How to Choose a Batch Processing Engine",
        "Choose Batch Engine",
        "Spring Batch vs Spark vs Flink — volume, latency, and team skill fit.",
        "decision",
    ),
    "postgresql": ("PostgreSQL", "PostgreSQL", "Open-source relational database with JSON, extensions, and strong ACID.", "database", "relational"),
    "mysql": ("MySQL", "MySQL", "Widely deployed OLTP relational database — simple ops, read replicas, InnoDB.", "database", "relational"),
    "oracle": ("Oracle Database", "Oracle", "Enterprise RDBMS — RAC, partitioning, and deep ERP/finance footprint.", "database", "relational"),
    "sql-server": ("Microsoft SQL Server", "SQL Server", "Microsoft stack relational database — T-SQL, SSIS, and Azure SQL sibling.", "database", "relational"),
    "mongodb": ("MongoDB", "MongoDB", "Document database with flexible schema — rapid product iteration and horizontal scale.", "database", "document"),
    "couchbase": ("Couchbase", "Couchbase", "Document + key-value with SQL++ — mobile sync and sub-millisecond reads.", "database", "document"),
    "cosmos-db": ("Azure Cosmos DB", "Cosmos DB", "Multi-model global database — SLA-backed latency and turnkey geo-replication.", "database", "document"),
    "cassandra": ("Apache Cassandra", "Cassandra", "Wide-column store for write-heavy, always-on workloads at planet scale.", "database", "wide-column"),
    "hbase": ("Apache HBase", "HBase", "Hadoop ecosystem wide-column store — strong consistency on HDFS.", "database", "wide-column"),
    "scylladb": ("ScyllaDB", "ScyllaDB", "Cassandra-compatible with C++ performance — lower tail latency.", "database", "wide-column"),
    "redis": ("Redis", "Redis", "In-memory data structure store — cache, session, pub/sub, and lightweight queue.", "database", "key-value"),
    "dynamodb": ("Amazon DynamoDB", "DynamoDB", "Managed key-value/document — predictable scale, pay-per-request, global tables.", "database", "key-value"),
    "aerospike": ("Aerospike", "Aerospike", "Flash-optimized key-value — sub-ms reads for ad-tech and fraud scoring.", "database", "key-value"),
    "neo4j": ("Neo4j", "Neo4j", "Native property graph — fraud rings, recommendations, and knowledge graphs.", "database", "graph"),
    "amazon-neptune": ("Amazon Neptune", "Neptune", "Managed graph — Gremlin and SPARQL for AWS-native graph workloads.", "database", "graph"),
    "influxdb": ("InfluxDB", "InfluxDB", "Time-series for metrics and IoT — retention policies and downsampling.", "database", "time-series"),
    "timescaledb": ("TimescaleDB", "TimescaleDB", "PostgreSQL extension for time-series — SQL familiarity plus hypertables.", "database", "time-series"),
    "opentsdb": ("OpenTSDB", "OpenTSDB", "HBase-backed time-series — large-scale metrics on Hadoop stack.", "database", "time-series"),
    "elasticsearch": ("Elasticsearch", "Elasticsearch", "Distributed search and analytics — full-text, aggregations, and ELK stack core.", "database", "search"),
    "opensearch": ("OpenSearch", "OpenSearch", "Elasticsearch fork — open-source search with AWS OpenSearch Service.", "database", "search"),
    "solr": ("Apache Solr", "Solr", "Mature Lucene-based search — faceting and enterprise search integrations.", "database", "search"),
    "clickhouse": ("ClickHouse", "ClickHouse", "Columnar OLAP — fast analytical queries on billions of rows.", "database", "analytics"),
    "snowflake": ("Snowflake", "Snowflake", "Cloud data warehouse — separation of storage and compute, SQL analytics.", "database", "analytics"),
    "bigquery": ("Google BigQuery", "BigQuery", "Serverless analytics warehouse — petabyte scale SQL with minimal ops.", "database", "analytics"),
    "milvus": ("Milvus", "Milvus", "Open-source vector database — similarity search for RAG and recommendations.", "database", "vector"),
    "pinecone": ("Pinecone", "Pinecone", "Managed vector index — low-latency semantic search without infra tuning.", "database", "vector"),
    "pgvector": ("pgvector", "pgvector", "Vector extension for PostgreSQL — combine relational + embeddings in one DB.", "database", "vector"),
    "weaviate": ("Weaviate", "Weaviate", "Vector database with hybrid search — vectors + keywords + GraphQL API.", "database", "vector"),
    "kafka": ("Apache Kafka", "Kafka", "Distributed commit log — high-throughput event streaming and replay.", "messaging"),
    "rabbitmq": ("RabbitMQ", "RabbitMQ", "Flexible AMQP broker — routing, priority queues, and classic enterprise messaging.", "messaging"),
    "activemq": ("Apache ActiveMQ", "ActiveMQ", "JMS broker — Java enterprise integration and legacy bridge.", "messaging"),
    "ibm-mq": ("IBM MQ", "IBM MQ", "Mission-critical mainframe-era messaging — guaranteed delivery in BFSI.", "messaging"),
    "nats": ("NATS", "NATS", "Lightweight pub/sub — cloud-native, low latency, JetStream persistence.", "messaging"),
    "pulsar": ("Apache Pulsar", "Pulsar", "Multi-tenant streaming — unified queue and log with geo-replication.", "messaging"),
    "sqs": ("Amazon SQS", "SQS", "Managed queue — simple decoupling without broker operations.", "messaging"),
    "sns": ("Amazon SNS", "SNS", "Managed pub/sub fan-out — push to queues, Lambda, and HTTP endpoints.", "messaging"),
    "google-pubsub": ("Google Cloud Pub/Sub", "Pub/Sub", "Global async messaging — at-least-once delivery with ordering keys.", "messaging"),
    "azure-service-bus": ("Azure Service Bus", "Service Bus", "Enterprise queues and topics — sessions, dead-letter, and transactions.", "messaging"),
    "redpanda": ("Redpanda", "Redpanda", "Kafka-compatible streaming without ZooKeeper — simpler ops footprint.", "messaging"),
    "temporal": ("Temporal", "Temporal", "Durable workflow orchestration — sagas, timers, and human tasks with code.", "workflow"),
    "camunda": ("Camunda", "Camunda", "BPMN workflow engine — business process visibility and human workflows.", "workflow"),
    "netflix-conductor": ("Netflix Conductor", "Conductor", "Microservice orchestration — JSON-defined workflows over REST workers.", "workflow"),
    "airflow": ("Apache Airflow", "Airflow", "DAG-based data pipeline scheduler — batch ETL and ML prep.", "workflow"),
    "argo-workflows": ("Argo Workflows", "Argo Workflows", "Kubernetes-native workflow engine — containerized step DAGs.", "workflow"),
    "prefect": ("Prefect", "Prefect", "Modern data workflow orchestration — Python-first with observability.", "workflow"),
    "spring-batch": ("Spring Batch", "Spring Batch", "Java batch framework — chunked processing integrated with Spring Boot.", "batch"),
    "apache-spark": ("Apache Spark", "Spark", "Distributed batch and micro-batch analytics — SQL, ML, and large ETL.", "batch"),
    "apache-flink": ("Apache Flink", "Flink", "Stream-first processing — low-latency stateful analytics.", "batch"),
    "apache-beam": ("Apache Beam", "Beam", "Portable pipeline API — run the same logic on Spark, Flink, or Dataflow.", "batch"),
    "databricks": ("Databricks", "Databricks", "Unified Spark platform — notebooks, Delta Lake, and ML lifecycle.", "batch"),
    "drools": ("Drools", "Drools", "Java rule engine — DRL rules, decision tables, and BRMS integration.", "rules"),
    "easy-rules": ("Easy Rules", "Easy Rules", "Lightweight Java rules — simple predicates without a full BRMS.", "rules"),
    "openl-tablets": ("OpenL Tablets", "OpenL Tablets", "Excel-like decision tables compiled to Java — business-owned rules.", "rules"),
    "aws-rule-engine": ("AWS Event-Driven Rules", "AWS Rules", "EventBridge rules and Step Functions — cloud-native conditional routing.", "rules"),
    "azure-logic-apps": ("Azure Logic Apps", "Logic Apps", "Low-code integration and rules — connectors and visual workflows.", "rules"),
    "quartz": ("Quartz Scheduler", "Quartz", "Java cron scheduler — clustered jobs inside application JVM.", "scheduler"),
    "kubernetes-cronjobs": ("Kubernetes CronJobs", "K8s CronJobs", "Native cluster cron — containerized scheduled tasks.", "scheduler"),
    "control-m": ("Control-M", "Control-M", "Enterprise workload automation — cross-system batch dependencies.", "scheduler"),
    "autosys": ("AutoSys", "AutoSys", "CA workload scheduler — mainframe and distributed job chains in large enterprises.", "scheduler"),
    "docker": ("Docker", "Docker", "Container packaging standard — images, registries, and local dev parity.", "cloud-native"),
    "podman": ("Podman", "Podman", "Daemonless containers — rootless-friendly Docker alternative.", "cloud-native"),
    "kubernetes": ("Kubernetes", "Kubernetes", "Container orchestration — scheduling, service discovery, and declarative ops.", "cloud-native"),
    "openshift": ("Red Hat OpenShift", "OpenShift", "Enterprise Kubernetes — built-in CI/CD, routes, and operator ecosystem.", "cloud-native"),
    "eks": ("Amazon EKS", "EKS", "Managed Kubernetes on AWS — control plane ops handled by AWS.", "cloud-native"),
    "aks": ("Azure AKS", "AKS", "Managed Kubernetes on Azure — Azure AD integration and node pools.", "cloud-native"),
    "gke": ("Google GKE", "GKE", "Managed Kubernetes on GCP — autopilot mode and strong networking.", "cloud-native"),
    "istio": ("Istio", "Istio", "Full-featured service mesh — traffic management, security, and telemetry.", "cloud-native"),
    "linkerd": ("Linkerd", "Linkerd", "Lightweight service mesh — minimal overhead, Rust data plane.", "cloud-native"),
    "consul": ("HashiCorp Consul", "Consul", "Service mesh and discovery — multi-platform connectivity.", "cloud-native"),
    "kong": ("Kong Gateway", "Kong", "Extensible API gateway — plugins for auth, rate limit, and transformation.", "cloud-native"),
    "nginx-api-gateway": ("NGINX as API Gateway", "NGINX Gateway", "High-performance reverse proxy — routing, TLS termination, rate limits.", "cloud-native"),
    "traefik": ("Traefik", "Traefik", "Cloud-native edge router — auto-discovery with Kubernetes and Let's Encrypt.", "cloud-native"),
    "ambassador": ("Ambassador (Emissary)", "Ambassador", "Kubernetes-native API gateway built on Envoy.", "cloud-native"),
    "aws-api-gateway": ("AWS API Gateway", "AWS API Gateway", "Managed REST/WebSocket/API — Lambda and VPC integration.", "cloud-native"),
    "nginx-ingress": ("NGINX Ingress Controller", "NGINX Ingress", "Kubernetes ingress — HTTP routing into cluster services.", "cloud-native"),
    "haproxy": ("HAProxy", "HAProxy", "L4/L7 load balancer — high throughput TCP and HTTP routing.", "cloud-native"),
    "traefik-ingress": ("Traefik Ingress", "Traefik Ingress", "Dynamic ingress for Kubernetes — middleware chains and TLS.", "cloud-native"),
    "prometheus": ("Prometheus", "Prometheus", "Metrics collection and alerting — pull model, PromQL, CNCF standard.", "cloud-native"),
    "grafana": ("Grafana", "Grafana", "Visualization and dashboards — Prometheus, Loki, and Tempo integration.", "cloud-native"),
    "elk-stack": ("ELK Stack", "ELK", "Elasticsearch + Logstash + Kibana — classic centralized logging.", "cloud-native"),
    "opensearch-logging": ("OpenSearch for Logging", "OpenSearch Logs", "Open-source logging stack alternative to ELK.", "cloud-native"),
    "loki": ("Grafana Loki", "Loki", "Log aggregation like Prometheus — label-based, cost-efficient storage.", "cloud-native"),
    "jaeger": ("Jaeger", "Jaeger", "Distributed tracing — request flow across microservices.", "cloud-native"),
    "zipkin": ("Zipkin", "Zipkin", "Lightweight tracing — simple span collection and UI.", "cloud-native"),
    "opentelemetry": ("OpenTelemetry", "OpenTelemetry", "Vendor-neutral telemetry SDK — traces, metrics, logs export.", "cloud-native"),
    "vault": ("HashiCorp Vault", "Vault", "Dynamic secrets, encryption, and PKI — central secret lifecycle.", "cloud-native"),
    "aws-secrets-manager": ("AWS Secrets Manager", "Secrets Manager", "Managed rotation for DB and API credentials on AWS.", "cloud-native"),
    "azure-key-vault": ("Azure Key Vault", "Key Vault", "Secrets, keys, and certificates for Azure workloads.", "cloud-native"),
    "cloud-providers-comparison": (
        "Cloud Providers Service Comparison",
        "Cloud Comparison",
        "Side-by-side mapping of AWS, Azure, GCP, and OpenShift/on-prem equivalents.",
        "cloud",
    ),
    "aws-cloud": ("Amazon Web Services (AWS)", "AWS", "Market leader cloud — broadest service catalog and ecosystem.", "cloud"),
    "azure-cloud": ("Microsoft Azure", "Azure", "Enterprise cloud — hybrid, Active Directory, and Microsoft stack integration.", "cloud"),
    "gcp-cloud": ("Google Cloud Platform (GCP)", "GCP", "Data and ML strength — BigQuery, GKE, and strong networking.", "cloud"),
    "openshift-on-prem-kubernetes": (
        "OpenShift & On-Prem Kubernetes",
        "OpenShift / On-Prem",
        "Private cloud Kubernetes — compliance, data residency, and operator-led platforms.",
        "cloud",
    ),
    "kafka-vs-rabbitmq": ("Kafka vs RabbitMQ", "Kafka vs RabbitMQ", "Log vs queue — throughput, ordering, replay, and operational complexity.", "comparison"),
    "redis-vs-memcached": ("Redis vs Memcached", "Redis vs Memcached", "Rich data structures vs pure cache — persistence and pub/sub.", "comparison"),
    "mongodb-vs-postgresql": ("MongoDB vs PostgreSQL", "MongoDB vs PostgreSQL", "Document flexibility vs relational integrity and SQL ecosystem.", "comparison"),
    "cassandra-vs-mongodb": ("Cassandra vs MongoDB", "Cassandra vs MongoDB", "Write-optimized wide rows vs flexible documents.", "comparison"),
    "rest-vs-grpc": ("REST vs gRPC", "REST vs gRPC", "HTTP/JSON ubiquity vs binary HTTP/2 performance and contracts.", "comparison"),
    "graphql-vs-rest": ("GraphQL vs REST", "GraphQL vs REST", "Client-driven queries vs resource-oriented endpoints.", "comparison"),
    "temporal-vs-airflow": ("Temporal vs Airflow", "Temporal vs Airflow", "Durable business workflows vs scheduled data pipelines.", "comparison"),
    "spark-vs-flink": ("Spark vs Flink", "Spark vs Flink", "Batch-first micro-batch vs true streaming latency.", "comparison"),
    "kubernetes-vs-openshift": ("Kubernetes vs OpenShift", "Kubernetes vs OpenShift", "Upstream K8s vs Red Hat enterprise distribution.", "comparison"),
    "eks-vs-aks-vs-gke": ("EKS vs AKS vs GKE", "EKS vs AKS vs GKE", "Managed Kubernetes comparison across the big three clouds.", "comparison"),
    "kong-vs-nginx-vs-aws-api-gateway": (
        "Kong vs NGINX vs AWS API Gateway",
        "Gateway Comparison",
        "Self-hosted extensibility vs performance vs fully managed cloud gateway.",
        "comparison",
    ),
    "elasticsearch-vs-opensearch": ("Elasticsearch vs OpenSearch", "Elasticsearch vs OpenSearch", "Elastic licensing vs open-source fork and AWS alignment.", "comparison"),
    "clickhouse-vs-elasticsearch": ("ClickHouse vs Elasticsearch", "ClickHouse vs ES", "OLAP columnar analytics vs inverted-index search and logs.", "comparison"),
    "oracle-vs-postgresql": ("Oracle vs PostgreSQL", "Oracle vs PostgreSQL", "Enterprise RDBMS TCO vs open-source PostgreSQL capability.", "comparison"),
}


def meta(slug: str) -> tuple:
    if slug in TOPIC_META:
        return TOPIC_META[slug]
    title = slug.replace("-", " ").title()
    return (title, title, f"Technology decision guide for {title}.", "general")


def fm(slug: str, mod_id: int, mod_title: str, topic_idx: int, draft: bool = False) -> str:
    title, short, desc, *rest = meta(slug)
    cat = rest[0] if rest else "general"
    section_ref = f"{mod_id}.{topic_idx + 1}"
    tags = ["technology-playbook", cat, slug.split("-")[0]]
    tags_line = ", ".join(f'"{t}"' for t in tags)
    draft_line = "true" if draft else "false"
    return textwrap.dedent(
        f"""\
        ---
        title: "{title}"
        date: 2026-06-30T10:00:00+00:00
        draft: {draft_line}
        description: "{desc}"
        tags: [{tags_line}]
        categories: ["Technology Playbook"]
        shortTitle: "{short}"
        module: {mod_id}
        moduleTitle: "{mod_title}"
        sectionRef: "{section_ref}"
        weight: {mod_id * 100 + topic_idx}
        ---
        """
    )


def deep_dive_block(slug: str) -> str:
    link = MICROSERVICES_DEEP_DIVES.get(slug)
    if not link:
        return ""
    return f"\n> **Deep dive:** For implementation patterns and code examples, see the [companion post in the Microservices Playbook]({link}).\n"


def architecture_diagram(slug: str, title: str) -> str:
    if "comparison" in slug or slug.startswith("how-to-choose"):
        return textwrap.dedent(
            """\
            ```mermaid
            flowchart TD
              req[Business Requirement] --> criteria{Decision Criteria}
              criteria --> optionA[Option A]
              criteria --> optionB[Option B]
              criteria --> optionC[Option C]
              optionA --> validate[POC / Load Test]
              optionB --> validate
              optionC --> validate
              validate --> decision[Architecture Decision Record]
            ```
            """
        )
    return textwrap.dedent(
        f"""\
        ```mermaid
        flowchart LR
          client[Client / Channel] --> edge[API Gateway / BFF]
          edge --> svc[Application Services]
          svc --> data[Data & Messaging Layer]
          data --> store[({title})]
        ```
        """
    )


def body_pattern(slug: str, title: str, short: str, desc: str) -> str:
    dd = deep_dive_block(slug)
    return textwrap.dedent(
        f"""\
        ## 1. Executive Summary

        {desc} Use this page to decide **when** the pattern earns its complexity — not just what it means on a diagram.{dd}

        ---

        ## 2. What Problem It Solves

        | Business pain | Technical symptom |
        | :--- | :--- |
        | Slow time-to-market from tight coupling | One change ripples across teams and releases |
        | Outages spread across domains | Shared runtime or database becomes a blast-radius multiplier |
        | Hard to scale one hot capability | Monolithic scaling pays for idle components |
        | Integration fragility | Point-to-point calls multiply with every new consumer |

        **{short}** addresses a specific slice of these pains. Match the pattern to the pain — do not adopt it because a reference architecture diagram includes the box.

        ---

        ## 3. Where It Fits in Architecture

        {architecture_diagram(slug, short)}

        ---

        ## 4. When to Choose

        - Team and domain boundaries are clear enough to justify separate deploy units or integration style
        - Non-functional requirements (scale, availability, compliance) explicitly need this pattern
        - You have observability and ops maturity to run the added moving parts
        - A phased migration path exists (especially for strangler and modular monolith approaches)

        ---

        ## 5. When Not to Choose

        - Early product stage with unknown domain boundaries
        - Team lacks distributed systems ops experience and no platform team support
        - Problem is purely CRUD with low traffic — simpler topology wins
        - You are solving an organizational problem with technology alone

        ---

        ## 6. Popular Tools / Products

        | Layer | Examples |
        | :--- | :--- |
        | **Runtime** | Kubernetes, ECS, VM clusters |
        | **Integration** | Kafka, RabbitMQ, REST/gRPC |
        | **Resilience** | Resilience4j, Istio, Envoy, API gateway plugins |
        | **Cloud managed** | AWS/Azure/GCP PaaS equivalents for your chosen building blocks |

        ---

        ## 7. Trade-offs

        {{< comparison-table >}}
        | Dimension | Benefit | Cost |
        | :--- | :--- | :--- |
        | **Complexity** | Solves a real architectural constraint | More components to deploy, monitor, and debug |
        | **Delivery speed** | Parallel team ownership after boundaries settle | Slower initially due to contracts and platform work |
        | **Operational load** | Better fault isolation when done well | Requires SRE/platform investment |
        | **Consistency** | Fits enterprise integration standards | Harder end-to-end testing without good observability |
        {{< /comparison-table >}}

        ---

        ## 8. Real-World Example

        **Global retail ERP modernization:** Order capture stays on legacy SAP while a **strangler** routes new mobile checkout to cloud microservices. **Event-driven** updates sync inventory to the warehouse system overnight. **Circuit breakers** on payment calls prevent cart meltdown when the PSP degrades.

        **BFSI payments:** **Saga** orchestrates authorize → capture → settlement with compensating voids. **Outbox** publishes ledger events without dual-write bugs. **Bulkheads** isolate fraud scoring thread pools from authorization latency.

        ---

        ## 9. Failure Scenarios

        | Failure mode | What breaks | Mitigation |
        | :--- | :--- | :--- |
        | Pattern adopted without boundaries | Distributed monolith — worst of both worlds | Domain discovery workshops first |
        | Missing idempotency / ordering rules | Duplicate charges, inconsistent reads | Explicit contract tests and replay strategy |
        | Observability gap | Mean time to innocence measured in hours | Trace IDs, golden signals, SLOs per dependency |
        | Premature extraction | High coordination overhead, no deploy independence | Modular monolith or strangler first |

        ---

        ## 10. Best Practices

        1. Write an **Architecture Decision Record (ADR)** with triggers and rollback criteria.
        2. Prove the pattern on **one bounded context** before enterprise-wide mandate.
        3. Invest in **contract testing** and **consumer-driven contracts** at integration edges.
        4. Pair every async pattern with a **dead-letter, replay, and reconciliation** story.
        5. Link operational runbooks to **SLOs** — not just architecture slides.

        ---

        ## 11. Interview Answer

        {{< interview-answer >}}
        **"{title} — when would you use it?"**

        "I reach for {short} when the business needs {desc.split('—')[0].strip().lower() if '—' in desc else 'clear separation of concerns'} and the organization can operate the extra moving parts. I would not start there for a small team proving product-market fit — I'd prefer a modular monolith or well-structured monolith until deploy boundaries and traffic patterns are understood. In interviews I always pair the pattern with a failure mode — for example how we'd handle partial outages and idempotent retries."
        {{< /interview-answer >}}

        ---

        ## 12. Related Topics

        - Browse [Module 1: Architecture Patterns](/technology-playbook/) for adjacent patterns
        - [Technology Decision Matrix](/technology-playbook/how-to-choose-database/) for tooling choices
        - [Microservices Playbook](/microservices/) for implementation-depth companion posts
        """
    )


def body_database(slug: str, title: str, short: str, desc: str, db_type: str) -> str:
    type_guidance = {
        "relational": "ACID transactions, JOINs, reporting, and strong schema governance",
        "document": "Flexible schema, nested JSON documents, horizontal scale for product catalogs",
        "wide-column": "Write-heavy, partition-tolerant, time-series and IoT at massive scale",
        "key-value": "Sub-millisecond lookups, caching, session store, and simple access patterns",
        "graph": "Relationship traversal — fraud, social, knowledge graphs, dependency maps",
        "time-series": "Metrics, IoT telemetry, downsampling, and retention policies",
        "search": "Full-text search, faceting, log indexing, and relevance tuning",
        "analytics": "Columnar scans, aggregations, BI dashboards, and petabyte warehouses",
        "vector": "Embedding similarity, semantic search, RAG retrieval, and recommendation vectors",
    }.get(db_type, "Specialized data workloads")

    return textwrap.dedent(
        f"""\
        ## 1. Executive Summary

        **{title}** is a **{db_type.replace('-', ' ')}** store. {desc}

        ---

        ## 2. What Problem It Solves

        | Scenario | Why {short} |
        | :--- | :--- |
        | Primary application datastore | {type_guidance} |
        | Performance-sensitive read path | Tunable indexes and caching layers |
        | Regulated enterprise workloads | Mature backup, audit, and HA options (verify per edition/cloud) |

        ---

        ## 3. Where It Fits in Architecture

        ```mermaid
        flowchart LR
          app[Application Services] --> ORM[Repository / DAO Layer]
          ORM --> db[({short})]
          app --> cache[Cache Layer]
          cache -.-> db
          db --> replica[Read Replicas / Analytics Export]
        ```

        ---

        ## 4. When to Choose

        - Access patterns align with **{db_type}** strengths ({type_guidance.lower()})
        - Team has operational experience or a managed cloud service reduces toil
        - Licensing and support model fit enterprise procurement (especially for Oracle/SQL Server)
        - Ecosystem drivers exist — ORM support, CDC tools, cloud marketplace

        ---

        ## 5. When Not to Choose

        - You need heavy cross-entity JOINs but picked a key-value or wide-column store
        - Operational team cannot run clustered/sharded infrastructure without managed service
        - Workload is pure batch analytics but you chose an OLTP primary store
        - Vendor lock-in risk unacceptable and migration path is unclear

        ---

        ## 6. Popular Tools / Products

        | Category | Related options |
        | :--- | :--- |
        | **Same class** | See [Databases module](/technology-playbook/) for peers in {db_type} |
        | **Cloud managed** | RDS/Aurora, Azure SQL/Cosmos, Cloud SQL/BigQuery equivalents |
        | **Migration** | AWS DMS, Debezium CDC, logical replication (PostgreSQL) |

        ---

        ## 7. Trade-offs

        {{< comparison-table >}}
        | Dimension | {short} strength | Watch out for |
        | :--- | :--- | :--- |
        | **Data model** | Optimized for {db_type} access paths | Misfit patterns cause performance cliffs |
        | **Consistency** | Tunable per product (strong vs eventual) | Misconfigured replicas cause stale reads |
        | **Ops** | Mature tooling in enterprise | HA/sharding complexity without managed service |
        | **Cost** | Predictable at moderate scale | License + IO + egress at cloud scale |
        {{< /comparison-table >}}

        ---

        ## 8. Real-World Example

        **Fintech ledger:** PostgreSQL or Oracle for double-entry accounts with strict ACID. **Inventory notifications:** Redis cache for hot SKU counts with DB as source of truth. **Customer 360 search:** Elasticsearch/OpenSearch for fuzzy name lookup across CRM + support tickets.

        **Reporting:** Nightly ETL from OLTP into Snowflake/BigQuery/ClickHouse — never run heavy BI on primary OLTP without guardrails.

        ---

        ## 9. Failure Scenarios

        | Risk | Symptom | Prevention |
        | :--- | :--- | :--- |
        | Connection pool exhaustion | Random timeouts under load | Pool sizing, RDS proxy, circuit breakers |
        | Missing indexes | Full table scans, p95 latency spikes | Query review, EXPLAIN in CI |
        | Replication lag | Users see stale balances | Monitor lag, read-your-writes routing |
        | Backup without restore test | Data loss discovered too late | Quarterly restore drills |

        ---

        ## 10. Best Practices

        1. Match **access patterns** to storage model before brand selection.
        2. Use **managed services** until team proves self-hosted cost advantage.
        3. Define **RPO/RTO** and test backups — especially for finance workloads.
        4. Separate **OLTP vs analytics** paths early (CDC to warehouse).
        5. Document **data classification** — PII encryption and key rotation.

        ---

        ## 11. Interview Answer

        {{< interview-answer >}}
        "For **{title}**, I'd choose it when workloads need {type_guidance.lower()} and the team can operate it responsibly. I'd compare it against other **{db_type}** options on ops burden, licensing, and cloud managed offerings. I'd also state what I would **not** store there — for example heavy analytics on OLTP or graph traversals on plain relational without extension."
        {{< /interview-answer >}}

        ---

        ## 12. Related Topics

        - [How to Choose a Database](/technology-playbook/how-to-choose-database/)
        - [Databases module index](/technology-playbook/)
        - Compare: search [Interview Preparation](/technology-playbook/) comparisons involving this technology
        """
    )


def body_messaging(slug: str, title: str, short: str, desc: str) -> str:
    return textwrap.dedent(
        f"""\
        ## 1. Executive Summary

        **{title}** — {desc}

        ---

        ## 2. What Problem It Solves

        | Need | How messaging helps |
        | :--- | :--- |
        | Decouple producers and consumers | Scale and deploy independently |
        | Buffer traffic spikes | Queue absorbs burst without dropping users |
        | Event notification | Many subscribers react to one business fact |
        | Integration across legacy and cloud | Stable wire protocol between eras |

        ---

        ## 3. Where It Fits in Architecture

        ```mermaid
        flowchart LR
          producer[Order Service] --> broker[({short})]
          broker --> consumerA[Inventory Worker]
          broker --> consumerB[Analytics Pipeline]
          broker --> consumerC[Notification Service]
        ```

        ---

        ## 4. When to Choose

        - You need **async** processing with clear back-pressure semantics
        - Multiple consumers must react to the same event stream
        - Peak traffic exceeds synchronous processing capacity
        - Cloud-managed ops preferred (SQS, Pub/Sub, Service Bus) vs self-hosted (Kafka, RabbitMQ)

        ---

        ## 5. When Not to Choose

        - Simple request/response suffices and latency budget is tight
        - Strong synchronous consistency required across services without saga/compensation
        - Team cannot operate broker HA, patching, and partition rebalancing
        - Message ordering requirements exceed what the broker guarantees for your config

        ---

        ## 6. Popular Tools / Products

        | Style | Examples |
        | :--- | :--- |
        | **Log / stream** | Kafka, Pulsar, Redpanda, Kinesis |
        | **Queue / AMQP** | RabbitMQ, ActiveMQ, SQS, Service Bus |
        | **Cloud pub/sub** | SNS, Google Pub/Sub, Event Grid |

        ---

        ## 7. Trade-offs

        {{< comparison-table >}}
        | Dimension | Upside | Downside |
        | :--- | :--- | :--- |
        | **Delivery** | At-least-once with retries | Idempotent consumers required |
        | **Ordering** | Partition keys enable order | Global order is expensive |
        | **Ops** | Managed services reduce toil | Self-hosted offers control at cost |
        | **Debugging** | Temporal decoupling | Harder than tracing sync calls |
        {{< /comparison-table >}}

        ---

        ## 8. Real-World Example

        **Order placed event** → inventory reservation, payment capture, email receipt, and fraud scoring run in parallel. **Payment reconciliation batch** reads from the same topic with a consumer group isolated from real-time paths.

        ---

        ## 9. Failure Scenarios

        - **Poison messages** clog queues — use DLQ and alerting
        - **Consumer lag** during campaigns — auto-scale consumers, partition count planning
        - **Schema drift** breaks deserializers — schema registry or contract tests

        ---

        ## 10. Best Practices

        1. Design **idempotent** consumers with business keys.
        2. Use **dead-letter queues** and replay tooling from day one.
        3. Propagate **trace context** in message headers.
        4. Size **partitions/queues** for peak, not average traffic.

        ---

        ## 11. Interview Answer

        {{< interview-answer >}}
        "I'd pick **{short}** when the domain needs {desc.split('—')[0].strip().lower() if '—' in desc else 'reliable async integration'}. I clarify delivery guarantees, ordering needs, and ops model — managed cloud queue vs self-hosted Kafka. I always mention idempotent consumers and dead-letter handling."
        {{< /interview-answer >}}

        ---

        ## 12. Related Topics

        - [How to Choose a Message Broker](/technology-playbook/how-to-choose-message-broker/)
        - [Kafka vs RabbitMQ](/technology-playbook/kafka-vs-rabbitmq/)
        - [Event-Driven Architecture](/technology-playbook/event-driven-architecture/)
        """
    )


def body_comparison(slug: str, title: str, short: str, desc: str) -> str:
    parts = slug.replace("-vs-", "|").split("|")
    left = parts[0].replace("-", " ").title() if parts else "Option A"
    right = parts[1].replace("-", " ").title() if len(parts) > 1 else "Option B"
    third = parts[2].replace("-", " ").title() if len(parts) > 2 else None

    table_header = f"| Capability | {left} | {right} |"
    table_sep = "| :--- | :--- | :--- |"
    if third:
        table_header = f"| Capability | {left} | {right} | {third} |"
        table_sep = "| :--- | :--- | :--- | :--- |"

    sample_rows = """\
| Primary model | See product docs | See product docs |
| Ops burden | Team-dependent | Team-dependent |
| Best fit | Match to access pattern | Match to access pattern |"""
    if third:
        sample_rows = """\
| Primary model | See product docs | See product docs | See product docs |
| Ops burden | Team-dependent | Team-dependent | Team-dependent |
| Best fit | Match to access pattern | Match to access pattern | Match to access pattern |"""

    return textwrap.dedent(
        f"""\
        ## 1. Executive Summary

        **{title}** — {desc} Use this comparison in architecture reviews and interviews to justify a choice with trade-offs, not slogans.

        ---

        ## 2. What Problem It Solves

        Architects face **option overload** — vendors, cloud defaults, and team familiarity pull in different directions. A structured comparison prevents **resume-driven architecture**.

        ---

        ## 3. Where It Fits in Architecture

        ```mermaid
        flowchart TD
          need[Integration / Data Need] --> eval{{"{short}"}}
          eval --> pickA[{left}]
          eval --> pickB[{right}]
        ```

        ---

        ## 4. When to Choose {left}

        - Workload characteristics align with its sweet spot (see table below)
        - Team operational maturity matches the product
        - Enterprise support, licensing, or cloud bundle favors it

        ---

        ## 5. When Not to Choose / Choose Alternative

        - Non-functional requirements (latency, ordering, cost) clearly favor the other side
        - Existing platform standard or skill pool points elsewhere
        - Managed service removes ops burden you cannot staff

        ---

        ## 6. Popular Tools / Products

        See detailed topic pages for each option in the [Technology Playbook index](/technology-playbook/).

        ---

        ## 7. Trade-offs

        {{< comparison-table caption="{title}" >}}
        {table_header}
        {table_sep}
        {sample_rows}
        {{< /comparison-table >}}

        {{< pros-cons pros="<ul><li>Left option: strengths for its primary use case</li><li>Right option: strengths for its primary use case</li></ul>" cons="<ul><li>Left option: operational or model limitations</li><li>Right option: operational or model limitations</li></ul>" >}}

        ---

        ## 8. Real-World Example

        **Notification platform:** High fan-out and replay → log-oriented broker. **Task queue with routing keys and priority** → classic AMQP. **Serverless glue** → cloud-native queue with pay-per-use.

        ---

        ## 9. Failure Scenarios

        - Choosing based on **brand** without load testing representative traffic
        - Ignoring **egress/ licensing** cost at scale
        - **Hybrid** deployment without clear ownership of upgrades and security patches

        ---

        ## 10. Best Practices

        1. Run a **two-week POC** with production-like volume skew (not happy-path only).
        2. Document decision in an **ADR** with rejected alternatives.
        3. Revisit when **scale doubles** or team skills shift.

        ---

        ## 11. Interview Answer

        {{< interview-answer >}}
        "There is no universal winner in **{short}**. I compare delivery semantics, ops model, ordering, replay, and team skills. I give a concrete scenario — for example peak checkout events vs nightly batch — and map each option to that scenario before recommending one."
        {{< /interview-answer >}}

        ---

        ## 12. Related Topics

        - [Technology Decision Matrix](/technology-playbook/how-to-choose-database/)
        - [Interview Preparation module](/technology-playbook/)
        """
    )


def body_cloud_comparison() -> str:
    return textwrap.dedent(
        """\
        ## 1. Executive Summary

        This page maps **equivalent services** across AWS, Azure, GCP, and OpenShift/on-prem Kubernetes so architects can compare apples-to-apples during migration or multi-cloud planning.

        ---

        ## 2. What Problem It Solves

        Teams evaluating cloud or hybrid strategy need a **capability matrix** — not marketing feature lists. Procurement, security, and engineering must align on the same service names and gaps.

        ---

        ## 3. Where It Fits in Architecture

        ```mermaid
        flowchart TB
          subgraph clouds [Cloud & Platform Choices]
            aws[AWS]
            azure[Azure]
            gcp[GCP]
            ocp[OpenShift / On-Prem]
          end
          apps[Enterprise Applications] --> clouds
          clouds --> data[Data & Messaging]
          clouds --> ops[Observability & IAM]
        ```

        ---

        ## 4. When to Choose Each Provider

        | Provider | Strong when |
        | :--- | :--- |
        | **AWS** | Broadest service catalog, startup/SaaS ecosystem, mature IAM patterns |
        | **Azure** | Microsoft stack, hybrid Active Directory, enterprise EA agreements |
        | **GCP** | Data analytics, ML/BigQuery, GKE-centric cloud-native |
        | **OpenShift / On-Prem** | Data residency, regulated industries, existing DC investment |

        ---

        ## 5. When Not to Choose

        - Multi-cloud **by default** without operational justification
        - Lift-and-shift without mapping **managed service equivalents**
        - Ignoring **egress and support** cost in TCO models

        ---

        ## 6. Service Equivalence Table

        {{< comparison-table caption="Capability mapping across platforms" >}}
        | Capability | AWS | Azure | GCP | OpenShift / On-Prem |
        | :--- | :--- | :--- | :--- | :--- |
        | **Compute** | EC2 | Virtual Machines | Compute Engine | Worker Nodes |
        | **Kubernetes** | EKS | AKS | GKE | OpenShift |
        | **Serverless** | Lambda | Azure Functions | Cloud Functions | Knative / OpenShift Serverless |
        | **Queue** | SQS | Service Bus | Pub/Sub | Kafka / RabbitMQ |
        | **Streaming** | Kinesis / MSK | Event Hubs | Pub/Sub / Dataflow | Kafka / Pulsar |
        | **Object Storage** | S3 | Blob Storage | Cloud Storage | MinIO / Ceph |
        | **Relational DB** | RDS / Aurora | Azure SQL | Cloud SQL | PostgreSQL Operator |
        | **NoSQL DB** | DynamoDB | Cosmos DB | Firestore / Bigtable | Cassandra / Mongo Operator |
        | **Cache** | ElastiCache | Azure Cache for Redis | Memorystore | Redis Operator |
        | **API Gateway** | API Gateway | API Management | Apigee / Gateway | Kong / NGINX |
        | **Monitoring** | CloudWatch | Azure Monitor | Cloud Monitoring | Prometheus / Grafana |
        | **Logging** | CloudWatch Logs | Log Analytics | Cloud Logging | ELK / Loki |
        | **IAM** | IAM | Entra ID + RBAC | Cloud IAM | OAuth / LDAP + RBAC |
        | **Secrets** | Secrets Manager | Key Vault | Secret Manager | Vault |
        | **DevOps / CI-CD** | CodePipeline | Azure DevOps | Cloud Build | Tekton / Jenkins / GitLab |
        {{< /comparison-table >}}

        ---

        ## 7. Trade-offs

        | Dimension | Multi-cloud hope | Reality |
        | :--- | :--- | :--- |
        | **Portability** | Write once, run anywhere | Lowest-common-denominator features |
        | **Skills** | Hire generic cloud engineers | Deep provider knowledge still required |
        | **Cost** | Arbitrage pricing | Egress and dual tooling eat savings |

        ---

        ## 8. Real-World Example

        **BFSI hybrid:** Core ledger on-prem OpenShift for residency; customer-facing mobile API on AWS with RDS and SQS; analytics landing in Snowflake fed from both via CDC.

        ---

        ## 9. Failure Scenarios

        - **Shadow IT** accounts without central IAM
        - **Unpatched** self-managed data plane on-prem
        - **Network** hairpinning — on-prem apps calling cloud APIs without ExpressRoute/Direct Connect planning

        ---

        ## 10. Best Practices

        1. Start from **capabilities**, not provider logos.
        2. Maintain a **living equivalence sheet** updated quarterly.
        3. Standardize **observability and IAM** patterns early.

        ---

        ## 11. Interview Answer

        {{< interview-answer >}}
        "I map each business capability to managed services on the target cloud — compute, data, messaging, identity, and observability. I explain why AWS/Azure/GCP/OpenShift fits the regulatory, skill, and commercial constraints. I avoid 'multi-cloud by default' unless exit strategy or residency truly requires it."
        {{< /interview-answer >}}

        ---

        ## 12. Related Topics

        - [AWS](/technology-playbook/aws-cloud/) · [Azure](/technology-playbook/azure-cloud/) · [GCP](/technology-playbook/gcp-cloud/) · [OpenShift / On-Prem](/technology-playbook/openshift-on-prem-kubernetes/)
        - [EKS vs AKS vs GKE](/technology-playbook/eks-vs-aks-vs-gke/)
        """
    )


def body_decision(slug: str, title: str, short: str, desc: str) -> str:
    return textwrap.dedent(
        f"""\
        ## 1. Executive Summary

        {desc} This decision guide turns vague "which tool?" meetings into **repeatable criteria** architects can defend in ADRs and interviews.

        ---

        ## 2. What Problem It Solves

        | Without a framework | With a framework |
        | :--- | :--- |
        | Brand-driven choices | Requirement-driven shortlist |
        | Late performance surprises | POC criteria defined upfront |
        | Ops mismatch | Team skill and SRE capacity factored in |

        ---

        ## 3. Where It Fits in Architecture

        {architecture_diagram(slug, short)}

        ---

        ## 4. When to Choose — Decision Checklist

        {{< decision-card title="Core questions" >}}
        1. What are the **access patterns** (read/write ratio, latency, consistency)?
        2. What is the **scale trajectory** in 12–24 months?
        3. **Managed vs self-hosted** — can we operate HA ourselves?
        4. What **compliance** constraints apply (region, encryption, audit)?
        5. What does the team **already know** — learning curve budget?
        {{< /decision-card >}}

        ---

        ## 5. When Not to Choose — Anti-patterns

        - Picking the tool the team used last job without workload fit
        - Skipping **load test** because POC "felt fast"
        - Ignoring **exit strategy** and vendor lock-in
        - Choosing distributed tech when a single-node solution meets SLOs for years

        ---

        ## 6. Popular Tools / Products

        Browse the relevant playbook module for product-specific pages and cloud equivalents.

        ---

        ## 7. Trade-offs

        {{< comparison-table >}}
        | Criterion | Favor managed cloud | Favor self-hosted / OSS |
        | :--- | :--- | :--- |
        | **Time to prod** | Faster | Slower — need platform team |
        | **Control** | Limited knobs | Full tuning |
        | **Cost at scale** | OpEx predictable early | CapEx/engineering may win later |
        | **Compliance** | Shared responsibility | You own patching and audit |
        {{< /comparison-table >}}

        ---

        ## 8. Real-World Example

        **ERP inventory service:** PostgreSQL for transactional stock; Redis for hot SKU cache; Kafka for stock-change events to warehouse and ecommerce; Elasticsearch for store-facing search.

        ---

        ## 9. Failure Scenarios

        - **Wrong store for access pattern** — e.g. graph traversal in relational without modeling
        - **Operational underestimation** — Kafka without monitoring consumer lag
        - **Cost shock** — serverless + egress at high volume

        ---

        ## 10. Best Practices

        1. Shortlist **two options** and run the same POC scenario on both.
        2. Write an **ADR** with rejected alternatives.
        3. Include **run cost** estimate at 3× expected scale.

        ---

        ## 11. Interview Answer

        {{< interview-answer >}}
        "I don't pick technologies by popularity. For **{short}**, I walk through access patterns, consistency, ops model, compliance, and team skills — then map to a shortlist. I always mention what I'd choose for a startup MVP vs a regulated bank production path."
        {{< /interview-answer >}}

        ---

        ## 12. Related Topics

        - [Technology Playbook index](/technology-playbook/)
        - Product-specific pages in modules 3–6
        """
    )


def body_generic(slug: str, title: str, short: str, desc: str, kind: str) -> str:
    if slug == "cloud-providers-comparison":
        return body_cloud_comparison()
    if kind == "comparison":
        return body_comparison(slug, title, short, desc)
    if kind == "decision":
        return body_decision(slug, title, short, desc)
    m = meta(slug)
    if len(m) > 4 and m[4]:
        return body_database(slug, title, short, desc, m[4])
    cat = m[3] if len(m) > 3 else "general"
    if cat == "architecture":
        return body_pattern(slug, title, short, desc)
    if cat == "messaging":
        return body_messaging(slug, title, short, desc)
    if cat in ("workflow", "batch", "rules", "scheduler", "cloud-native", "cloud"):
        return body_messaging(slug, title, short, desc)  # reuse async/tool template
    return body_pattern(slug, title, short, desc)


def normalize_markdown(body: str) -> str:
    """Dedent body and restore Hugo shortcode delimiters stripped by f-strings."""
    import re

    body = textwrap.dedent(body)
    body = re.sub(r"\n {8}", "\n", body)
    body = re.sub(r"(?<!\{)\{<", "{{<", body)
    body = re.sub(r">\}(?!\})", ">}}", body)
    return body.strip() + "\n"


def module_landing(mod: dict) -> str:
    lines = [
        "---",
        f'title: "{mod["landingTitle"]}"',
        "date: 2026-06-30T10:00:00+00:00",
        "draft: false",
        f'description: "{mod["landingDescription"]}"',
        'tags: ["technology-playbook", "module-index"]',
        'categories: ["Technology Playbook"]',
        f'module: {mod["id"]}',
        f'moduleTitle: "{mod["focus"]}"',
        f'url: "/technology-playbook/module-{mod["slug"]}/"',
        "layout: single",
        "---",
        "",
        f"# Module {mod['id']}: {mod['focus']}",
        "",
        mod["landingDescription"],
        "",
        "---",
        "",
        "## Topics in this module",
        "",
        "| # | Topic |",
        "| :---: | :--- |",
    ]
    for i, slug in enumerate(mod["topics"]):
        title, short, _, *_ = meta(slug)
        lines.append(f'| {mod["id"]}.{i + 1} | [{short}](/technology-playbook/{slug}/) |')
    lines.extend(
        [
            "",
            "---",
            "",
            "[← Back to Technology Playbook index](/technology-playbook/)",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    with open(DATA / "technology_playbook_modules.yaml", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    CONTENT.mkdir(parents=True, exist_ok=True)
    order_topics: list[str] = []

    for mod in data["modules"]:
        mod_id = mod["id"]
        mod_title = mod["focus"]
        landing_path = CONTENT / f"module-{mod['slug']}.md"
        landing_path.write_text(module_landing(mod), encoding="utf-8")

        for topic_idx, slug in enumerate(mod["topics"]):
            order_topics.append(slug)
            if slug in SKIP_SLUGS:
                print(f"Skip (reference): {slug}")
                continue
            title, short, desc, *rest = meta(slug)
            cat = rest[0] if rest else "general"
            content = normalize_markdown(body_generic(slug, title, short, desc, cat))
            path = CONTENT / f"{slug}.md"
            path.write_text(fm(slug, mod_id, mod_title, topic_idx) + content, encoding="utf-8")
            print(f"Wrote {path.relative_to(ROOT)}")

    order_yaml = {"topics": order_topics}
    with open(DATA / "technology_playbook_order.yaml", "w", encoding="utf-8") as f:
        yaml.dump(order_yaml, f, default_flow_style=False, sort_keys=False)

    print(f"Generated {len(order_topics)} topics, {len(data['modules'])} module landing pages.")


if __name__ == "__main__":
    main()
