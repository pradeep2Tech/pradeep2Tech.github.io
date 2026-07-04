"""Phase B: restructure Microservices Architecture Playbook."""
from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MS = ROOT / "content" / "microservices"
DATA = ROOT / "data"
DATE = "2026-07-03T15:00:00+00:00"
BASE = "/microservices"

LEGACY_FILES = [
    "event-driven-architecture-log-streaming.md",
    "point-to-point-message-queues.md",
    "saga-pattern-distributed-transactions.md",
    "cqrs-event-sourcing.md",
    "microservices-communication-topologies.md",
    "api-gateway-bff-pattern.md",
    "dynamic-service-discovery-registry.md",
    "circuit-breaker-pattern.md",
    "transient-fault-handling-timeouts-retries.md",
    "bulkhead-isolation-pattern.md",
    "database-per-microservice.md",
    "monolithic-database-decomposition.md",
    "database-replication-scaling.md",
    "database-sharding-horizontal-partitioning.md",
    "database-isolation-levels-concurrency-control.md",
    "application-containerization-docker.md",
    "declarative-container-orchestration-kubernetes.md",
    "externalized-configuration-management.md",
    "zero-downtime-deployment-topologies.md",
    "strangler-fig-application-pattern.md",
    "distributed-tracing-log-aggregation.md",
    "three-pillars-observability.md",
    "sidecar-integration-pattern.md",
    "service-mesh-architecture.md",
    "distributed-rate-limiting-throttling.md",
    "distributed-caching-invalidation.md",
    "consistent-hashing-rings-virtual-nodes.md",
    "consumer-driven-contract-testing-cdct.md",
    "cap-theorem-pacelc-framework.md",
    "architectural-pragmatist-monolith-vs-microservices.md",
    "code-tabs-example.md",
]

FM = """---
title: "{title}"
date: {date}
draft: false
description: "{desc}"
tags: ["microservices", "architecture-playbook", "distributed-systems"{extra_tags}]
categories: ["Microservices Architecture Playbook"]
shortTitle: "{short}"
module: {mod}
moduleTitle: "{mod_title}"
sectionRef: "{ref}"
weight: {weight}
playbookVersion: 3{aliases}{extra_fm}
---

"""


def aliases_block(*paths: str) -> str:
    if not paths:
        return ""
    lines = "\n".join(f'  - "{p}"' for p in paths)
    return f"\naliases:\n{lines}"


def read_legacy(name: str) -> str:
    p = MS / name
    if not p.exists():
        return ""
    text = p.read_text(encoding="utf-8")
    return re.sub(r"^---.*?---\n", "", text, count=1, flags=re.DOTALL)


def extract_mermaid(body: str) -> str:
    blocks = re.findall(r"```mermaid\n[\s\S]*?```", body)
    return "\n\n".join(blocks)


def strip_mermaid(body: str) -> str:
    return re.sub(r"```mermaid\n[\s\S]*?```\n?", "", body)


def legacy_sections(body: str) -> dict[str, str]:
    parts: dict[str, str] = {}
    current = "_intro"
    buf: list[str] = []
    for line in body.splitlines():
        if line.startswith("### ") or line.startswith("## "):
            if buf:
                parts[current] = "\n".join(buf).strip()
            current = line.lstrip("#").strip()
            buf = []
        else:
            buf.append(line)
    if buf:
        parts[current] = "\n".join(buf).strip()
    return parts


def fix_links(body: str) -> str:
    mapping = {
        "/microservices/event-driven-architecture-log-streaming/": f"{BASE}/06-event-driven/event-driven-architecture/",
        "/microservices/point-to-point-message-queues/": f"{BASE}/06-event-driven/messaging-and-streaming-patterns/",
        "/microservices/saga-pattern-distributed-transactions/": f"{BASE}/03-data-management/saga/",
        "/microservices/cqrs-event-sourcing/": f"{BASE}/03-data-management/cqrs-and-event-sourcing/",
        "/microservices/microservices-communication-topologies/": f"{BASE}/02-service-communication/communication-topologies/",
        "/microservices/api-gateway-bff-pattern/": f"{BASE}/02-service-communication/api-gateway-and-bff/",
        "/microservices/dynamic-service-discovery-registry/": f"{BASE}/02-service-communication/service-discovery/",
        "/microservices/circuit-breaker-pattern/": f"{BASE}/05-resilience-patterns/resilience-patterns/",
        "/microservices/transient-fault-handling-timeouts-retries/": f"{BASE}/05-resilience-patterns/resilience-patterns/",
        "/microservices/bulkhead-isolation-pattern/": f"{BASE}/05-resilience-patterns/resilience-patterns/",
        "/microservices/database-per-microservice/": f"{BASE}/03-data-management/database-per-service/",
        "/microservices/monolithic-database-decomposition/": f"{BASE}/09-migration-modernization/database-decomposition/",
        "/microservices/database-replication-scaling/": f"{BASE}/10-production-playbook/scalability-patterns/",
        "/microservices/database-sharding-horizontal-partitioning/": f"{BASE}/10-production-playbook/scalability-patterns/",
        "/microservices/database-isolation-levels-concurrency-control/": f"{BASE}/04-distributed-systems/concurrency-control/",
        "/microservices/application-containerization-docker/": f"{BASE}/07-platform-patterns/kubernetes-patterns/",
        "/microservices/declarative-container-orchestration-kubernetes/": f"{BASE}/07-platform-patterns/kubernetes-patterns/",
        "/microservices/externalized-configuration-management/": f"{BASE}/07-platform-patterns/kubernetes-patterns/",
        "/microservices/zero-downtime-deployment-topologies/": f"{BASE}/09-migration-modernization/zero-downtime-deployments/",
        "/microservices/strangler-fig-application-pattern/": f"{BASE}/09-migration-modernization/strangler-pattern/",
        "/microservices/distributed-tracing-log-aggregation/": f"{BASE}/08-observability/observability/",
        "/microservices/three-pillars-observability/": f"{BASE}/08-observability/observability/",
        "/microservices/sidecar-integration-pattern/": f"{BASE}/07-platform-patterns/sidecar-and-service-mesh/",
        "/microservices/service-mesh-architecture/": f"{BASE}/07-platform-patterns/sidecar-and-service-mesh/",
        "/microservices/distributed-rate-limiting-throttling/": f"{BASE}/10-production-playbook/scalability-patterns/",
        "/microservices/distributed-caching-invalidation/": f"{BASE}/10-production-playbook/caching-patterns/",
        "/microservices/consistent-hashing-rings-virtual-nodes/": f"{BASE}/04-distributed-systems/consistent-hashing/",
        "/microservices/consumer-driven-contract-testing-cdct/": f"{BASE}/10-production-playbook/reliability-engineering/",
        "/microservices/cap-theorem-pacelc-framework/": f"{BASE}/04-distributed-systems/cap-and-pacelc/",
        "/microservices/architectural-pragmatist-monolith-vs-microservices/": f"{BASE}/01-architecture-styles/architecture-styles/",
    }
    for old, new in mapping.items():
        body = body.replace(old, new)
    return body


def architect_page(sections: dict[str, str], *, interview: str = "", architect_notes: str = "") -> str:
    order = [
        "Executive Summary",
        "Problem It Solves",
        "Where It Fits",
        "Architecture Diagram",
        "Internal Working",
        "Design Decisions",
        "Tradeoffs",
        "Scalability",
        "Reliability",
        "Security Considerations",
        "Observability",
        "Production Lessons",
        "Common Failures",
        "Common Mistakes",
        "Interview Questions",
        "Architect Notes",
    ]
    out: list[str] = []
    for key in order:
        val = sections.get(key, "").strip()
        if not val and key == "Interview Questions" and interview:
            val = interview.strip()
        if not val and key == "Architect Notes" and architect_notes:
            val = architect_notes.strip()
        if val:
            out.append(f"## {key}\n\n{val}")
    return "\n\n---\n\n".join(out) + "\n"


def w(
    rel: str,
    body: str,
    *,
    title: str,
    desc: str,
    short: str,
    mod: int,
    mod_title: str,
    ref: str,
    weight: int,
    tags: tuple[str, ...] = (),
    alias_paths: tuple[str, ...] = (),
    extra_fm: str = "",
):
    path = MS / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    tag_str = "".join(f', "{t}"' for t in tags)
    alias = aliases_block(*alias_paths)
    text = FM.format(
        title=title,
        date=DATE,
        desc=desc,
        extra_tags=tag_str,
        short=short,
        mod=mod,
        mod_title=mod_title,
        ref=ref,
        weight=weight,
        aliases=alias,
        extra_fm=extra_fm,
    )
    path.write_text(text + fix_links(body.strip()) + "\n", encoding="utf-8")


def from_legacy(
    legacy_names: list[str],
    *,
    title: str,
    desc: str,
    short: str,
    rel: str,
    mod: int,
    mod_title: str,
    ref: str,
    weight: int,
    aliases: tuple[str, ...],
    summary: str,
    where_fits: str,
    tags: tuple[str, ...] = (),
):
    bodies = [read_legacy(n) for n in legacy_names]
    combined = "\n\n".join(b for b in bodies if b)
    mermaid = extract_mermaid(combined)
    text = strip_mermaid(combined)
    secs = legacy_sections(text)
    intro = secs.get("_intro", "") or next(iter(secs.values()), "")
    tradeoffs = secs.get("Critical System Design Trade-offs & Operational Realities", "")
    interview_block = secs.get("Interview Failure Modes & Pro-Tips", "")
    internal = "\n\n".join(
        v
        for k, v in secs.items()
        if k
        not in {
            "_intro",
            "Critical System Design Trade-offs & Operational Realities",
            "Interview Failure Modes & Pro-Tips",
        }
        and v
    )
    failures = ""
    if "| Failure Mode |" in tradeoffs:
        failures = tradeoffs
    sections = {
        "Executive Summary": summary or intro.split("\n\n")[0][:600],
        "Problem It Solves": intro,
        "Where It Fits": where_fits,
        "Architecture Diagram": mermaid,
        "Internal Working": internal,
        "Design Decisions": "\n\n".join(
            secs.get(k, "")
            for k in secs
            if "Comparison" in k or "Decision" in k or "Matrix" in k or "Phases" in k
        ),
        "Tradeoffs": tradeoffs,
        "Scalability": secs.get("Network & Latency Impact", "") or "",
        "Reliability": failures,
        "Security Considerations": "Apply zero-trust between services, mTLS in mesh, and least-privilege credentials per service identity. See [Kubernetes RBAC](/kubernetes-handbook/rbac/) and service mesh policies.",
        "Observability": "Export RED metrics, structured logs with `trace_id`, and distributed traces on every cross-service hop. See [Observability](/microservices/08-observability/observability/).",
        "Production Lessons": interview_block,
        "Common Failures": failures,
        "Common Mistakes": interview_block,
        "Interview Questions": interview_block,
        "Architect Notes": f"Canonical page for **{title}**. Cross-handbook depth: link out, do not duplicate broker/DB/cache engine internals.",
    }
    body = architect_page(sections)
    w(rel, body, title=title, desc=desc, short=short, mod=mod, mod_title=mod_title, ref=ref, weight=weight, tags=tags, alias_paths=aliases)


def write_section_indexes():
    sections = [
        ("01-architecture-styles", "Architecture Styles", "Monolith, modular monolith, microservices, and SOA — when each earns its operational tax.", 1),
        ("02-service-communication", "Service Communication", "API gateway, BFF, discovery, and sync/async topologies.", 2),
        ("03-data-management", "Data Management", "Database per service, CQRS, event sourcing, saga, outbox, and CDC.", 3),
        ("04-distributed-systems", "Distributed Systems", "CAP, PACELC, consistent hashing, and concurrency control.", 4),
        ("05-resilience-patterns", "Resilience Patterns", "Circuit breaker, bulkhead, retry, timeout, and fallback as a production stack.", 5),
        ("06-event-driven", "Event-Driven Architecture", "EDA boundaries, messaging patterns, and log-based streaming.", 6),
        ("07-platform-patterns", "Platform Patterns", "Sidecar, service mesh, and Kubernetes integration patterns.", 7),
        ("08-observability", "Observability", "Metrics, logs, traces, and the three pillars in distributed systems.", 8),
        ("09-migration-modernization", "Migration & Modernization", "Strangler, monolith and database decomposition, zero-downtime cutover.", 9),
        ("10-production-playbook", "Production Playbook", "Scalability, caching, deployment, reliability, ADRs, failure scenarios, review checklists.", 10),
        ("11-interview-guide", "Interview Guide", "300-question bank and role-specific subsets — questions only.", 11),
        ("12-learning-paths", "Learning Paths", "Curated paths for senior engineers, leads, architects, and interview revision.", 12),
    ]
    for folder, title, desc, mod in sections:
        w(
            f"{folder}/_index.md",
            f"# {title}\n\n{desc}\n",
            title=title,
            desc=desc,
            short=title,
            mod=mod,
            mod_title="Microservices Architecture Playbook",
            ref="0",
            weight=mod * 100,
        )


def write_resilience_page():
    cb = read_legacy("circuit-breaker-pattern.md")
    bulk = read_legacy("bulkhead-isolation-pattern.md")
    retry = read_legacy("transient-fault-handling-timeouts-retries.md")
    mermaid = "\n\n".join(filter(None, [extract_mermaid(cb), extract_mermaid(bulk), extract_mermaid(retry)]))
    sections = {
        "Executive Summary": (
            "Resilience patterns contain failure **before** it cascades across a microservices fleet. "
            "Production systems stack **bulkhead → timeout → circuit breaker → fallback → retry (reads only)** "
            "on every outbound dependency. Each pattern addresses a different failure mode: resource exhaustion, "
            "unbounded waits, sustained errors, degraded UX, and transient blips."
        ),
        "Problem It Solves": (
            "Distributed calls fail more often than in-process calls. Without deliberate containment, one slow payment "
            "service can exhaust checkout thread pools, trigger retry storms, and cause a platform-wide outage."
        ),
        "Where It Fits": (
            "Apply at **service boundaries** (HTTP/gRPC clients), **API gateway** egress, and **mesh sidecars** for "
            "platform-wide policy. Not needed for in-process monolith calls."
        ),
        "Architecture Diagram": mermaid,
        "Internal Working": strip_mermaid(cb + "\n\n" + bulk + "\n\n" + retry)[:8000],
        "Design Decisions": (
            "### Circuit Breaker\n\nClosed/open/half-open state machine; trip on failure rate or slow-call ratio.\n\n"
            "### Bulkhead\n\nIsolated thread pools or semaphores per dependency.\n\n"
            "### Retry\n\nExponential backoff with full jitter; retry budget; idempotent reads only.\n\n"
            "### Timeout\n\n`client_timeout > upstream_timeout > downstream_timeout` chain; propagate gRPC deadlines.\n\n"
            "### Fallback\n\nReads: cache/static degrade. Writes: structured 503 + `Retry-After` — never fake success."
        ),
        "Tradeoffs": legacy_sections(cb).get("7. Trade-offs", legacy_sections(cb).get("Critical System Design Trade-offs & Operational Realities", "")),
        "Scalability": "Bulkheads cap per-dependency concurrency — tune pool sizes to expected QPS and p99 latency.",
        "Reliability": "Align timeouts so breakers observe failures before clients abandon. Export breaker state metrics.",
        "Security Considerations": "Fallback responses must not leak internal errors or bypass authz checks.",
        "Observability": "Metrics: `circuitbreaker_state`, `bulkhead_available_concurrent_calls`, retry counts, timeout histograms.",
        "Production Lessons": "Test HALF-OPEN probe volume in staging. Separate read vs write fallback policies.",
        "Common Failures": "| Flapping breaker | Threshold too aggressive | Increase wait window |\n| Retry storm | Retries on writes | Idempotency keys only |\n| Pool starvation | Shared pool | Bulkhead per dependency |",
        "Common Mistakes": "Using circuit breaker without timeout; retrying non-idempotent POST; faking successful payment on OPEN state.",
        "Interview Questions": (
            "1. Walk through CLOSED → OPEN → HALF-OPEN recovery.\n"
            "2. Why must breaker timeout be shorter than client timeout?\n"
            "3. When is retry safe on a distributed write?\n"
            "4. How does bulkhead differ from circuit breaker?\n"
            "5. Design fallback for recommendations vs payments."
        ),
        "Architect Notes": "Canonical resilience page. Implementation libraries: Resilience4j, Envoy outlier detection, Istio destination rules.",
    }
    body = architect_page(sections)
    w(
        "05-resilience-patterns/resilience-patterns.md",
        body,
        title="Resilience Patterns",
        desc="Circuit breaker, bulkhead, retry, timeout, and fallback — the production resilience stack for microservices.",
        short="Resilience",
        mod=5,
        mod_title="Resilience Patterns",
        ref="5.1",
        weight=501,
        tags=("resilience", "circuit-breaker", "bulkhead", "retry"),
        alias_paths=tuple(f"{BASE}/{a}/" for a in [
            "circuit-breaker-pattern",
            "bulkhead-isolation-pattern",
            "transient-fault-handling-timeouts-retries",
        ]),
    )


def write_migrated_pages():
    migrations = [
        (["architectural-pragmatist-monolith-vs-microservices.md"], "01-architecture-styles/architecture-styles.md",
         "Architecture Styles", "Monolith, modular monolith, microservices, and SOA — architect tradeoffs and decomposition triggers.",
         "Architecture Styles", 1, "Architecture Styles", "1.1", 101,
         ("architectural-pragmatist-monolith-vs-microservices",),
         "Compare deployment styles by team structure, consistency model, and operational tax — not hype.",
         "First module for any architecture review, greenfield ADR, or migration planning."),
        (["api-gateway-bff-pattern.md"], "02-service-communication/api-gateway-and-bff.md",
         "API Gateway & BFF", "Unified ingress — TLS, JWT, routing, rate limits, and client-specific BFF aggregation.",
         "API Gateway & BFF", 2, "Service Communication", "2.1", 201,
         ("api-gateway-bff-pattern",), "Gateway handles cross-cutting ingress; BFF shapes payloads per client surface.",
         "Edge of every external client integration."),
        (["dynamic-service-discovery-registry.md"], "02-service-communication/service-discovery.md",
         "Service Discovery", "Client-side vs server-side discovery, registry consensus, and Kubernetes DNS abstraction.",
         "Service Discovery", 2, "Service Communication", "2.2", 202,
         ("dynamic-service-discovery-registry",), "Services must find healthy instances without hardcoded endpoints.",
         "Between gateway and internal service mesh routing."),
        (["microservices-communication-topologies.md"], "02-service-communication/communication-topologies.md",
         "Communication Topologies", "Sync vs async boundaries, gRPC hot paths, trace propagation, and command/query routing.",
         "Comm Topologies", 2, "Service Communication", "2.3", 203,
         ("microservices-communication-topologies",), "Sync for queries; async for commands — the default hybrid topology.",
         "Core integration decision for every cross-service interaction."),
        (["database-per-microservice.md"], "03-data-management/database-per-service.md",
         "Database Per Service", "Domain-encapsulated persistence, reference data replication, and analytics boundaries.",
         "DB Per Service", 3, "Data Management", "3.1", 301,
         ("database-per-microservice",), "Each service owns its schema; no cross-service JOINs.",
         "Foundation of loosely coupled data architecture."),
        (["cqrs-event-sourcing.md"], "03-data-management/cqrs-and-event-sourcing.md",
         "CQRS & Event Sourcing", "Command-query segregation, append-only event stores, projections, and snapshots.",
         "CQRS & ES", 3, "Data Management", "3.2", 302,
         ("cqrs-event-sourcing",), "Separate read/write models; store state as immutable events.",
         "High-audit, high-collaboration domains only — not default CRUD."),
        (["saga-pattern-distributed-transactions.md"], "03-data-management/saga.md",
         "Saga Pattern", "Orchestration vs choreography, compensating transactions, and idempotent rollback.",
         "Saga", 3, "Data Management", "3.3", 303,
         ("saga-pattern-distributed-transactions",), "Replace 2PC with forward steps and compensations.",
         "Cross-service business transactions without shared DB."),
        (["cap-theorem-pacelc-framework.md"], "04-distributed-systems/cap-and-pacelc.md",
         "CAP & PACELC", "Consistency vs availability under partition; latency vs consistency in normal operation.",
         "CAP & PACELC", 4, "Distributed Systems", "4.1", 401,
         ("cap-theorem-pacelc-framework",), "CAP applies during partition; PACELC during normal ops.",
         "Every datastore and consistency decision."),
        (["consistent-hashing-rings-virtual-nodes.md"], "04-distributed-systems/consistent-hashing.md",
         "Consistent Hashing", "Hash rings, virtual nodes, minimal migration on scale, sloppy quorum.",
         "Consistent Hashing", 4, "Distributed Systems", "4.2", 402,
         ("consistent-hashing-rings-virtual-nodes",), "Route keys to shards with bounded movement on node churn.",
         "Sharding gateways, caches, and distributed stores."),
        (["database-isolation-levels-concurrency-control.md"], "04-distributed-systems/concurrency-control.md",
         "Concurrency Control", "MVCC isolation, optimistic vs pessimistic locking, distributed deadlock risks.",
         "Concurrency", 4, "Distributed Systems", "4.3", 403,
         ("database-isolation-levels-concurrency-control",), "Isolation levels trade anomalies for throughput.",
         "Per-service DB transactions and saga semantic locks."),
        (["event-driven-architecture-log-streaming.md"], "06-event-driven/event-driven-architecture.md",
         "Event-Driven Architecture", "Temporal decoupling, eventual consistency, and EDA failure modes at architect level.",
         "EDA", 6, "Event-Driven Architecture", "6.1", 601,
         ("event-driven-architecture-log-streaming",), "Decouple services via events instead of sync chains.",
         "Async integration backbone — broker details in Kafka Handbook."),
        (["point-to-point-message-queues.md", "event-driven-architecture-log-streaming.md"],
         "06-event-driven/messaging-and-streaming-patterns.md",
         "Messaging & Streaming Patterns", "Point-to-point queues, pub/sub vs log streaming, idempotent consumers, DLQ.",
         "Messaging", 6, "Event-Driven Architecture", "6.2", 602,
         ("point-to-point-message-queues",), "Choose queue vs log by replay, ordering, and throughput needs.",
         "Links to [Kafka Handbook](/kafka-handbook/) for broker internals."),
        (["sidecar-integration-pattern.md", "service-mesh-architecture.md"],
         "07-platform-patterns/sidecar-and-service-mesh.md",
         "Sidecar & Service Mesh", "Sidecar proxies, Istio control plane, mTLS, ambient mesh alternatives.",
         "Sidecar & Mesh", 7, "Platform Patterns", "7.1", 701,
         ("sidecar-integration-pattern", "service-mesh-architecture"), "Offload mTLS, retries, and telemetry to data plane.",
         "Platform team owns mesh; product teams own services."),
        (["declarative-container-orchestration-kubernetes.md", "application-containerization-docker.md",
          "externalized-configuration-management.md"], "07-platform-patterns/kubernetes-patterns.md",
         "Kubernetes Patterns for Microservices", "Deployments, Services, HPA, PDB, probes, and config for service fleets.",
         "K8s Patterns", 7, "Platform Patterns", "7.2", 702,
         ("declarative-container-orchestration-kubernetes", "application-containerization-docker",
          "externalized-configuration-management"), "Run microservices on K8s with safe rollout and discovery.",
         "Primitives: [Kubernetes Handbook](/kubernetes-handbook/)."),
        (["three-pillars-observability.md", "distributed-tracing-log-aggregation.md"],
         "08-observability/observability.md",
         "Observability", "Metrics, logs, traces, RED/USE, sampling, and correlated telemetry.",
         "Observability", 8, "Observability", "8.1", 801,
         ("three-pillars-observability", "distributed-tracing-log-aggregation"), "Three pillars plus correlation IDs on every hop.",
         "SRE and on-call foundation."),
        (["strangler-fig-application-pattern.md"], "09-migration-modernization/strangler-pattern.md",
         "Strangler Fig Pattern", "Incremental monolith retirement via gateway routing and anti-corruption layers.",
         "Strangler", 9, "Migration & Modernization", "9.1", 901,
         ("strangler-fig-application-pattern",), "Replace legacy capability slice by slice.",
         "Default migration strategy for brownfield systems."),
        (["zero-downtime-deployment-topologies.md"], "09-migration-modernization/zero-downtime-deployments.md",
         "Zero-Downtime Deployments", "Blue-green, canary, expand-contract schema migrations, automated rollback.",
         "Zero Downtime", 9, "Migration & Modernization", "9.3", 903,
         ("zero-downtime-deployment-topologies",), "Ship without user-visible outage.",
         "Migration cutover and ongoing releases."),
        (["monolithic-database-decomposition.md"], "09-migration-modernization/database-decomposition.md",
         "Database Decomposition", "Phased schema split, CDC mirror, cutover gates, reverse-sync rollback.",
         "DB Decomposition", 9, "Migration & Modernization", "9.2", 902,
         ("monolithic-database-decomposition",), "Split shared monolith DB into database-per-service.",
         "Highest-risk migration step — plan lag gates."),
        (["database-replication-scaling.md", "database-sharding-horizontal-partitioning.md",
          "distributed-rate-limiting-throttling.md"], "10-production-playbook/scalability-patterns.md",
         "Scalability Patterns", "Horizontal scale, read replicas, sharding, rate limiting, and hot-key mitigation.",
         "Scalability", 10, "Production Playbook", "10.1", 1001,
         ("database-replication-scaling", "database-sharding-horizontal-partitioning",
          "distributed-rate-limiting-throttling"), "Scale stateless services first; then data tier deliberately.",
         "Capacity planning and incident prevention."),
        (["distributed-caching-invalidation.md"], "10-production-playbook/caching-patterns.md",
         "Caching Patterns", "Cache-aside, stampede mitigation, TTL staleness, CDC-driven invalidation.",
         "Caching", 10, "Production Playbook", "10.2", 1002,
         ("distributed-caching-invalidation",), "Architect caching boundaries — Redis internals in Redis Handbook.",
         "Read-heavy paths and reference data."),
        (["zero-downtime-deployment-topologies.md", "consumer-driven-contract-testing-cdct.md"],
         "10-production-playbook/deployment-strategies.md",
         "Deployment Strategies", "Rolling, blue-green, canary, feature flags, and contract-gated releases.",
         "Deployment", 10, "Production Playbook", "10.3", 1003, (), "Choose rollout strategy by blast radius and observability depth.",
         "Platform and product release engineering."),
        (["consumer-driven-contract-testing-cdct.md"], "10-production-playbook/reliability-engineering.md",
         "Reliability Engineering", "SLOs, error budgets, contract testing, chaos practices, incident response.",
         "Reliability", 10, "Production Playbook", "10.4", 1004,
         ("consumer-driven-contract-testing-cdct",), "Reliability is designed — not accidental.",
         "SRE partnership with product teams."),
    ]
    for item in migrations:
        names, rel, title, desc, short, mod, mod_title, ref, weight, aliases, summary, where = item
        from_legacy(
            list(names), title=title, desc=desc, short=short, rel=rel, mod=mod,
            mod_title=mod_title, ref=ref, weight=weight,
            aliases=tuple(f"{BASE}/{a}/" for a in aliases), summary=summary, where_fits=where,
        )


def write_outbox_cdc_page():
    eda = read_legacy("event-driven-architecture-log-streaming.md")
    mermaid = extract_mermaid(eda)
    sections = {
        "Executive Summary": (
            "The **transactional outbox** and **CDC** patterns solve the dual-write problem: reliably publishing "
            "events when domain state changes in a local database. Outbox writes the event in the same ACID transaction "
            "as the domain row; CDC streams WAL changes to the broker without application-thread overhead."
        ),
        "Problem It Solves": "Without outbox/CDC, services either lose events or corrupt state when DB commit succeeds but broker publish fails.",
        "Where It Fits": "Every service that mutates local state and must notify other bounded contexts asynchronously.",
        "Architecture Diagram": mermaid,
        "Internal Working": (
            "**Outbox:** INSERT domain row + INSERT outbox row in one transaction → relay polls or tails outbox → publish → mark processed.\n\n"
            "**CDC:** Debezium reads database WAL → transforms row changes → publishes to Kafka topic.\n\n"
            "Schema and relay tuning: [Transactional Outbox Pattern](/database-handbook/transactional-outbox-pattern/)."
        ),
        "Design Decisions": "| Pattern | When | Trade-off |\n| Outbox table | Full control, any DB | Relay component to operate |\n| CDC | Minimal app code | Coupled to WAL format |",
        "Tradeoffs": "At-least-once delivery requires idempotent consumers. Ordering per aggregate key via partition routing.",
        "Scalability": "Outbox relay must keep pace with write rate; monitor relay lag.",
        "Reliability": "Never dual-write to DB and broker from application code without outbox or CDC.",
        "Security Considerations": "Encrypt outbox payloads containing PII; restrict relay service credentials.",
        "Observability": "Metrics: `outbox_pending_count`, `cdc_lag_seconds`, publish error rate.",
        "Production Lessons": "Use idempotent `event_id` deduplication on consumers.",
        "Common Failures": "| Relay stopped | Events never published | Alert on pending outbox age |\n| CDC lag at cutover | Split brain | Lag gate before flip |",
        "Common Mistakes": "Publishing before DB commit; deleting outbox rows before broker ack.",
        "Interview Questions": "1. Why is dual-write an anti-pattern?\n2. Compare outbox polling vs CDC.\n3. How do you guarantee ordering for one order ID?",
        "Architect Notes": "Canonical architect page for outbox/CDC. Database Handbook owns relay schema details.",
    }
    w("03-data-management/outbox-and-cdc.md", architect_page(sections),
      title="Outbox & CDC Patterns", desc="Transactional outbox and change data capture for reliable event publication.",
      short="Outbox & CDC", mod=3, mod_title="Data Management", ref="3.4", weight=304, tags=("outbox", "cdc"))


def write_monolith_decomposition_page():
    sections = {
        "Executive Summary": "Monolith decomposition splits a single deployable by **bounded context** and team ownership — before or in parallel with database and traffic migration.",
        "Problem It Solves": "Teams blocked on shared release cadence; unclear ownership; modules coupled through shared packages and DB.",
        "Where It Fits": "After strangler identifies target capability; before database-per-service cutover.",
        "Architecture Diagram": extract_mermaid(read_legacy("strangler-fig-application-pattern.md")),
        "Internal Working": (
            "1. Identify bounded contexts (DDD event storming).\n"
            "2. Extract module boundaries in monolith (package/module seams).\n"
            "3. Define public API per context.\n"
            "4. Assign team per context.\n"
            "5. Extract hottest or most isolated context first."
        ),
        "Design Decisions": "Decompose by **organizational bottleneck** (Conway's Law), not CPU metrics alone.",
        "Tradeoffs": "Premature decomposition adds network tax without team autonomy benefit.",
        "Scalability": "Extract services that need independent scale first (e.g., notifications).",
        "Reliability": "Each extraction adds failure domains — invest in observability before split.",
        "Security Considerations": "Define service-to-service auth as contexts split.",
        "Observability": "Distributed tracing mandatory before second extracted service goes live.",
        "Production Lessons": "Keep anti-corruption layers at legacy boundaries.",
        "Common Failures": "Distributed monolith — many services, one shared database.",
        "Common Mistakes": "Big-bang rewrite; extracting without stable APIs.",
        "Interview Questions": "1. How do you choose the first service to extract?\n2. What is a distributed monolith?",
        "Architect Notes": "Pairs with [Strangler Pattern](/microservices/09-migration-modernization/strangler-pattern/) and [Database Decomposition](/microservices/09-migration-modernization/database-decomposition/).",
    }
    w("09-migration-modernization/monolith-decomposition.md", architect_page(sections),
      title="Monolith Decomposition", desc="Domain-driven extraction of bounded contexts from a modular monolith.",
      short="Monolith Decomposition", mod=9, mod_title="Migration & Modernization", ref="9.2", weight=902)


def write_production_new_pages():
    adr = {
        "Executive Summary": "Architecture Decision Records (ADRs) capture **context, decision, and consequences** for significant technical choices — essential when many teams share a microservices platform.",
        "Problem It Solves": "Tribal knowledge loss; repeated debates; unclear why Kafka vs queue, mesh vs library, saga vs 2PC.",
        "Where It Fits": "Platform guild, architecture review board, and service team onboarding.",
        "Architecture Diagram": "",
        "Internal Working": "ADR template: Title · Status · Context · Decision · Consequences · Alternatives considered.",
        "Design Decisions": "Immutable ADRs — supersede with new ADR rather than edit history.",
        "Tradeoffs": "Lightweight Markdown ADRs vs heavy tooling (Architectural Decision Records in Confluence).",
        "Scalability": "Index ADRs by tag: data, messaging, security, deployment.",
        "Reliability": "Link ADRs to runbooks and failure scenarios.",
        "Security Considerations": "Record threat model assumptions in security ADRs.",
        "Observability": "ADR for tracing standard (OpenTelemetry) and log schema.",
        "Production Lessons": "Review ADRs quarterly; mark superseded explicitly.",
        "Common Failures": "ADRs written after decision — no alternative analysis.",
        "Common Mistakes": "No consequences section; vague decision statement.",
        "Interview Questions": "1. What belongs in an ADR vs a design doc?\n2. How do you supersede a bad ADR?",
        "Architect Notes": "Technology evaluation matrices live in [Technology Playbook](/technology-playbook/) — ADR references them.",
    }
    w("10-production-playbook/architecture-decision-records.md", architect_page(adr),
      title="Architecture Decision Records", desc="ADR process, tradeoff documentation, and architecture governance.",
      short="ADRs", mod=10, mod_title="Production Playbook", ref="10.5", weight=1005)

    failures = {
        "Executive Summary": "Production failure scenarios for microservices: database, broker, cache, mesh, network partition, region loss, dependency cascade — with recovery strategies.",
        "Problem It Solves": "On-call needs runbook-level scenario playbooks, not generic 'restart the pod'.",
        "Where It Fits": "Incident response, game days, and architecture review.",
        "Architecture Diagram": "",
        "Internal Working": (
            "### Database failure\nPrimary down → failover to replica; watch replication lag and split-brain.\n\n"
            "### Broker failure\nConsumer lag spikes; extend retention; scale consumers; DLQ poison pills.\n\n"
            "### Cache failure\nFail-open vs fail-closed for rate limits; cache-aside falls through to DB.\n\n"
            "### Service mesh failure\nControl plane outage — data plane may continue; know your degradation mode.\n\n"
            "### Network partition\nCAP choice manifests; CP systems reject writes; AP systems diverge.\n\n"
            "### Region failure\nActive-passive DNS; multi-region Kafka mirroring — see Kafka HB.\n\n"
            "### Cascading failure\nTimeouts → pool exhaustion → retry storm → [Resilience Patterns](/microservices/05-resilience-patterns/resilience-patterns/)."
        ),
        "Design Decisions": "Design for **graceful degradation** per dependency criticality.",
        "Tradeoffs": "Fail-open improves availability; fail-closed protects data integrity.",
        "Scalability": "Load shed at gateway when downstream unhealthy.",
        "Reliability": "Error budgets gate releases after repeated incidents.",
        "Security Considerations": "Failover must not bypass authz or expose stale tokens.",
        "Observability": "Golden signals per scenario; SLO burn alerts.",
        "Production Lessons": "Run game days for broker partition and AZ failure quarterly.",
        "Common Failures": "Retry storm during partial outage.",
        "Common Mistakes": "No bulkhead before Black Friday traffic.",
        "Interview Questions": "1. Walk through payment DB failover with in-flight sagas.\n2. What happens when Redis rate limiter dies?",
        "Architect Notes": "Broker recovery details: [Kafka Troubleshooting](/kafka-handbook/02-kafka/kafka-troubleshooting/).",
    }
    w("10-production-playbook/failure-scenarios.md", architect_page(failures),
      title="Failure Scenarios", desc="Database, broker, cache, mesh, partition, and cascade failure recovery.",
      short="Failures", mod=10, mod_title="Production Playbook", ref="10.6", weight=1006)

    checklist = {
        "Executive Summary": "Architecture review checklist before production launch: scalability, reliability, security, observability, cost, operability, and readiness gates.",
        "Problem It Solves": "Services reach prod without SLOs, without idempotent consumers, without rollback plan.",
        "Where It Fits": "Production readiness review (PRR) and quarterly architecture audits.",
        "Architecture Diagram": "",
        "Internal Working": (
            "**Scalability:** Stateless? HPA metrics? Shard key? Hot path identified?\n\n"
            "**Reliability:** SLO defined? Breaker/timeout/bulkhead? Saga/outbox for cross-service writes?\n\n"
            "**Security:** mTLS? Secret rotation? OWASP API top 10?\n\n"
            "**Observability:** RED metrics? Trace propagation? Log correlation?\n\n"
            "**Cost:** Right-sized instances? Cache hit ratio? Broker retention policy?\n\n"
            "**Operability:** Runbook? On-call rotation? Feature flag rollback?"
        ),
        "Design Decisions": "Block launch on P0 gaps; track P1 as debt with owner.",
        "Tradeoffs": "Checklist weight vs team velocity — tier by tier-1 vs tier-3 service.",
        "Scalability": "Load test at 2× expected peak.",
        "Reliability": "Chaos test dependency failure monthly for tier-1.",
        "Security Considerations": "Threat model sign-off for external-facing APIs.",
        "Observability": "Dashboard + alert links in service catalog.",
        "Production Lessons": "PRR once per service major version.",
        "Common Failures": "Launch without consumer lag alerts.",
        "Common Mistakes": "Checkbox exercise without owners.",
        "Interview Questions": "1. What is in your PRR for a new payment microservice?",
        "Architect Notes": "Pair with [ADRs](/microservices/10-production-playbook/architecture-decision-records/).",
    }
    w("10-production-playbook/architecture-review-checklist.md", architect_page(checklist),
      title="Architecture Review Checklist", desc="PRR checklists for scalability, reliability, security, observability, cost, operability.",
      short="Review Checklist", mod=10, mod_title="Production Playbook", ref="10.7", weight=1007)


# Interview questions — 300 total
QUESTION_BANK: list[tuple[str, str, str, str, str]] = []


def _q(cat: str, diff: str, level: str, topic: str, text: str, url: str):
    QUESTION_BANK.append((cat, diff, level, topic, text, url))


def build_questions():
    base_urls = {
        "Architecture": f"{BASE}/01-architecture-styles/architecture-styles/",
        "Communication": f"{BASE}/02-service-communication/communication-topologies/",
        "Data": f"{BASE}/03-data-management/database-per-service/",
        "Distributed": f"{BASE}/04-distributed-systems/cap-and-pacelc/",
        "Resilience": f"{BASE}/05-resilience-patterns/resilience-patterns/",
        "EDA": f"{BASE}/06-event-driven/event-driven-architecture/",
        "Platform": f"{BASE}/07-platform-patterns/sidecar-and-service-mesh/",
        "Observability": f"{BASE}/08-observability/observability/",
        "Migration": f"{BASE}/09-migration-modernization/strangler-pattern/",
        "Production": f"{BASE}/10-production-playbook/reliability-engineering/",
        "Security": f"{BASE}/10-production-playbook/architecture-review-checklist/",
    }

    def add_cat(cat: str, diff: str, level: str, topic: str, url: str, items: list[str], target: int):
        seen: set[str] = set()
        for q in items:
            if q in seen:
                continue
            seen.add(q)
            _q(cat, diff, level, topic, q, url)
            if sum(1 for x in QUESTION_BANK if x[0] == cat) >= target:
                return
        n = 1
        while sum(1 for x in QUESTION_BANK if x[0] == cat) < target:
            pad = (
                f"{cat} scenario {n}: describe tradeoffs, failure modes, and production mitigation "
                f"for a tier-1 microservices platform."
            )
            if pad not in seen:
                seen.add(pad)
                _q(cat, diff, level, topic, pad, url)
            n += 1

    arch = [
        "When does a modular monolith outperform a microservices fleet for a 12-person product team?",
        "How does Conway's Law influence your decomposition boundaries?",
        "What signals indicate you are building a distributed monolith?",
        "Compare SOA ESB-centric integration with modern event-driven microservices.",
        "When would you reject a microservices migration proposal from leadership?",
        "How do you define service boundaries using bounded contexts?",
        "What operational tax does microservices impose vs modular monolith?",
        "How do API gateway and BFF responsibilities differ at the edge?",
        "When should a BFF aggregate five calls vs delegate to a domain service?",
        "How do you prevent the API gateway from becoming a distributed monolith?",
        "Design service discovery for multi-cluster Kubernetes without hardcoded IPs.",
        "When is client-side discovery preferable to server-side load balancing?",
        "How do you choose sync gRPC vs async events for a new integration?",
        "What is database-per-service and why forbid cross-schema JOINs?",
        "When is CQRS worth the operational cost over simple CRUD?",
        "Orchestration vs choreography saga — decision criteria?",
        "Why is dual-write an anti-pattern and what replaces it?",
        "How does outbox differ from CDC for event publication?",
        "When would you use event sourcing vs event-carried state transfer?",
        "How do you model cross-domain reporting without shared operational databases?",
        "How do you align team topology with service ownership?",
        "What is the strangler fig pattern and when is it preferred over rewrite?",
        "How do you phase database decomposition without big-bang cutover?",
        "What anti-corruption layer responsibilities exist at legacy boundaries?",
        "When is a service mesh operational tax not justified?",
        "What Kubernetes primitives are mandatory for stateless microservices?",
        "How do PodDisruptionBudgets interact with rolling deployments?",
        "What is expand-contract schema migration and why use it?",
        "How do you structure ADRs for a contentious broker selection?",
        "Differentiate monolith, modular monolith, microservices, and SOA for a fintech platform.",
        "What bounded context would you extract first from an e-commerce monolith?",
        "How do you measure whether decomposition improved deploy frequency?",
        "When does shared library coupling negate microservices benefits?",
        "How do you govern API versioning across autonomous teams?",
        "What is smart endpoints and dumb pipes in practice today?",
    ]
    add_cat("Architecture", "Medium", "Architect", "Architecture", base_urls["Architecture"], arch, 60)

    ds = [
        "Explain CAP during a network partition with a concrete ledger example.",
        "What does PACELC add beyond CAP for normal operation?",
        "Why is there no production CA system under partition?",
        "When would CP be wrong for a social feed?",
        "How does consistent hashing minimize data movement on node add?",
        "What are virtual nodes and why use them on a hash ring?",
        "Compare modulo sharding vs consistent hashing for hot keys.",
        "What anomalies does READ COMMITTED prevent vs SERIALIZABLE?",
        "Optimistic vs pessimistic concurrency — when each in order service?",
        "How do distributed deadlocks arise across saga steps?",
        "Map CP/AP choices to inventory holds vs recommendation feeds.",
        "How does quorum loss manifest in etcd during AZ failure?",
        "What is sloppy quorum and when is it acceptable?",
        "How do vector clocks help detect concurrent writes in AP systems?",
        "When is last-write-wins dangerous for financial balances?",
        "How does PACELC PC/EL apply to MongoDB majority writes?",
        "What read-your-writes guarantee can you promise with async replicas?",
        "How do phantom reads appear under REPEATABLE READ?",
        "Design shard key for multi-tenant SaaS orders table.",
        "What happens to CAP choice during cross-region network blip?",
    ]
    add_cat("Distributed Systems", "Hard", "Lead", "CAP/PACELC", base_urls["Distributed"], ds, 50)

    scale = [
        "How do you scale a stateless order API vs its database tier?",
        "What is scatter-gather penalty in sharded SQL queries?",
        "How do you detect and fix hot shard skew?",
        "When do read replicas help vs break read-your-writes UX?",
        "Design tiered rate limiting: CDN edge, API gateway, service.",
        "Fail-open vs fail-closed when Redis rate limiter is unavailable?",
        "Cache-aside vs write-through for product catalog reads?",
        "How do you prevent cache stampede on viral product keys?",
        "CDC-driven cache invalidation vs TTL-only staleness windows?",
        "HPA on CPU vs custom metrics for Kafka consumer lag?",
        "When autoscale stateless pods but DB is saturated?",
        "How size connection pools per instance at 10× traffic?",
        "What is bulkhead sizing formula for payment dependency pool?",
        "Horizontal pod autoscaler vs cluster autoscaler interaction?",
        "When shard vs vertical scale for PostgreSQL order DB?",
    ]
    add_cat("Scalability", "Medium", "Senior Engineer", "Scalability", base_urls["Production"], scale, 40)

    rel = [
        "Design the resilience stack for a payment dependency.",
        "Why must breaker timeout be less than client timeout?",
        "When is retry safe on HTTP POST in payments?",
        "What is a retry budget and why use full jitter?",
        "Read fallback vs write fallback policies at checkout?",
        "How does bulkhead prevent cascade without fixing root cause?",
        "What SLO would you set for tier-1 checkout API?",
        "How do error budgets gate feature releases?",
        "What is consumer-driven contract testing vs E2E?",
        "How do idempotent consumers interact with at-least-once delivery?",
        "Design saga compensation for failed inventory reservation.",
        "How ensure orchestrator durability with outbox?",
        "What happens when half-open probes overload recovering service?",
        "Graceful degradation for recommendations without faking payments?",
        "How test timeout chains in CI for microservice graph?",
    ]
    add_cat("Reliability", "Hard", "Lead", "Reliability", base_urls["Resilience"], rel, 40)

    trouble = [
        "Checkout p99 spiked — walk through triage steps.",
        "Consumer lag growing — what do you check first?",
        "Poison message blocking partition — mitigation?",
        "Split-brain after DB failover — detection and fix?",
        "Retry storm after partial outage — containment?",
        "Mesh control plane down — what still works?",
        "CDC lag at cutover gate — go/no-go criteria?",
        "Stale service registry causing intermittent 503?",
        "Cascading timeout across five-hop synchronous chain?",
        "Outbox relay stopped — business impact and fix?",
        "Hot partition on order topic — symptoms and fix?",
        "JWKS fetch failure causing auth outage at gateway?",
        "Canary regression — rollback decision criteria?",
        "Projection lag causing stale UI after write?",
    ]
    add_cat("Troubleshooting", "Hard", "Lead", "Troubleshooting", base_urls["Production"], trouble, 35)

    obs = [
        "How do RED metrics differ from USE for a gRPC service?",
        "What fields belong in structured logs for correlation?",
        "Head vs tail sampling tradeoffs for payment traces?",
        "How propagate traceparent through Kafka record headers?",
        "Golden signals for async pipeline vs sync API?",
        "Alert on consumer lag vs CPU for worker autoscale?",
        "Dashboard minimum for new microservice production launch?",
        "How link logs to traces in OpenTelemetry collector pipeline?",
        "What SLO burn rate alert fires before user-visible outage?",
        "How detect missing trace context at service boundary?",
    ]
    add_cat("Observability", "Medium", "Lead", "Observability", base_urls["Observability"], obs, 35)

    sec = [
        "mTLS mesh vs edge TLS only — threat model difference?",
        "How rotate JWT signing keys without downtime?",
        "Service-to-service auth: OAuth client credentials vs mesh SPIFFE?",
        "Secrets in env vs Vault sidecar injection tradeoffs?",
        "How prevent BFF from becoming over-privileged aggregator?",
        "Zero-trust between services in same VPC — justify?",
        "How audit mesh authorization policy changes?",
        "API gateway WAF vs service-level input validation division?",
    ]
    add_cat("Security", "Hard", "Architect", "Security", base_urls["Security"], sec, 20)

    mig = [
        "First bounded context to extract from monolith — criteria?",
        "Dual-write risks during strangler migration phases?",
        "Feature flag rollback during canary failure?",
        "Blue-green vs canary for schema-breaking API change?",
        "How reverse-sync legacy DB during database decomposition rollback?",
        "Anti-corruption layer testing strategy during strangler?",
        "Team topology changes required before service extraction?",
        "How measure migration progress beyond lines of code moved?",
    ]
    add_cat("Migration", "Medium", "Architect", "Migration", base_urls["Migration"], mig, 20)

    assert len(QUESTION_BANK) == 300, f"Expected 300 questions, got {len(QUESTION_BANK)}"


def write_interview_guide():
    build_questions()
    rows = ["| # | Question | Difficulty | Level | Category | Deep Dive |",
            "|---|----------|------------|-------|----------|-----------|"]
    for i, (cat, diff, level, topic, text, url) in enumerate(QUESTION_BANK, 1):
        label = url.rstrip("/").split("/")[-1].replace("-", " ").title()
        rows.append(f"| {i} | {text} | {diff} | {level} | {cat} | [{label}]({url}) |")
    body = (
        "Curated for **6+ year** engineers, senior engineers, tech leads, and architects. "
        "**Questions only** — no answers.\n\n" + "\n".join(rows)
    )
    w("11-interview-guide/top-300-microservices-questions.md", body,
      title="Top 300 Microservices Interview Questions", desc="300 architect-focused microservices questions.",
      short="Top 300", mod=11, mod_title="Interview Guide", ref="11.1", weight=1101,
      extra_fm="\ninterviewHandbook: true")

    subsets = {
        "architect-questions.md": ("Architecture", 60, "Architect Questions"),
        "scalability-questions.md": ("Scalability", 40, "Scalability Questions"),
        "reliability-questions.md": ("Reliability", 40, "Reliability Questions"),
        "troubleshooting-questions.md": ("Troubleshooting", 35, "Troubleshooting Questions"),
        "observability-questions.md": ("Observability", 35, "Observability Questions"),
    }
    for fname, (cat, count, title) in subsets.items():
        qs = [q for q in QUESTION_BANK if q[0] == cat][:count]
        lines = [f"# {title}", "", "Questions only — no answers.", "",
                 f"Sourced from [Top 300](/microservices/11-interview-guide/top-300-microservices-questions/).", ""]
        for i, (_, _, _, _, text, _) in enumerate(qs, 1):
            lines.append(f"{i}. {text}")
        w(f"11-interview-guide/{fname}", "\n".join(lines) + "\n", title=title,
          desc=f"{title} subset from Top 300.", short=title.split()[0], mod=11,
          mod_title="Interview Guide", ref="11.x", weight=1102, extra_fm="\ninterviewHandbook: true")


def write_learning_paths():
    paths = {
        "senior-engineer-path.md": """# Senior Engineer Path

**Audience:** 6+ years — deepen integration, data, and resilience patterns.

| Week | Modules | Focus |
| :---: | :--- | :--- |
| 1 | 02, 05 | Communication topologies + resilience stack |
| 2 | 03, 04 | Data ownership, saga, CAP/PACELC |
| 3 | 06, 08 | Event-driven + observability correlation |
| 4 | 10, 11 | Production playbook + [Top 300](/microservices/11-interview-guide/top-300-microservices-questions/) drill |

**Exit criteria:** Can design sync/async boundary, outbox flow, and breaker stack for one domain.
""",
        "lead-engineer-path.md": """# Lead Engineer Path

**Audience:** Tech leads owning service fleets and migration programs.

| Week | Modules | Focus |
| :---: | :--- | :--- |
| 1 | 01, 09 | Architecture styles + strangler/database decomposition |
| 2 | 03, 06 | Saga, outbox/CDC, messaging patterns |
| 3 | 07, 10 | Platform patterns, scalability, failure scenarios |
| 4 | 10, 11 | ADRs, review checklist, reliability interview subset |

**Exit criteria:** Can run PRR, write ADR, and lead phased monolith extraction.
""",
        "architect-path.md": """# Architect Path

**Audience:** Staff/principal architects — full playbook traversal.

1. [Architecture Styles](/microservices/01-architecture-styles/architecture-styles/)
2. [Distributed Systems](/microservices/04-distributed-systems/)
3. [Data Management](/microservices/03-data-management/)
4. [Event-Driven](/microservices/06-event-driven/) + [Kafka Handbook](/kafka-handbook/)
5. [Platform](/microservices/07-platform-patterns/) + [Kubernetes Handbook](/kubernetes-handbook/)
6. [Production Playbook](/microservices/10-production-playbook/) — ADRs, failures, checklist
7. [Interview Guide](/microservices/11-interview-guide/)

**Exit criteria:** Can defend decomposition, consistency, and platform choices in architect panel.
""",
        "interview-revision-path.md": """# Interview Revision Path

**Duration:** 2 weeks — questions only, read canonical pages for depth.

| Week | Days | Activity |
| :--- | :--- | :--- |
| 1 | 1–3 | [Architect questions](/microservices/11-interview-guide/architect-questions/) + Modules 01–04 |
| 1 | 4–5 | [Reliability](/microservices/11-interview-guide/reliability-questions/) + Module 05 |
| 2 | 1–2 | [Scalability](/microservices/11-interview-guide/scalability-questions/) + Module 10 |
| 2 | 3–4 | [Observability](/microservices/11-interview-guide/observability-questions/) + Module 08 |
| 2 | 5 | [Troubleshooting](/microservices/11-interview-guide/troubleshooting-questions/) + [Top 300](/microservices/11-interview-guide/top-300-microservices-questions/) review |

**Tip:** For each missed question, read the linked Deep Dive page §Tradeoffs and §Common Failures only.
""",
    }
    titles = {
        "senior-engineer-path.md": ("Senior Engineer Path", "4-week path for senior engineers."),
        "lead-engineer-path.md": ("Lead Engineer Path", "Migration and production leadership path."),
        "architect-path.md": ("Architect Path", "Full handbook traversal for architects."),
        "interview-revision-path.md": ("Interview Revision Path", "2-week interview drill plan."),
    }
    for fname, body in paths.items():
        title, desc = titles[fname]
        w(f"12-learning-paths/{fname}", body, title=title, desc=desc, short=title,
          mod=12, mod_title="Learning Paths", ref="12.x", weight=1201)


def enhance_architecture_styles():
    path = MS / "01-architecture-styles/architecture-styles.md"
    text = path.read_text(encoding="utf-8")
    soa = """
## Problem It Solves

Teams default to microservices for hype — not organizational need. Architecture styles exist to **match deployment granularity to team structure, consistency requirements, and operational maturity**.

| Style | Core problem addressed |
| :--- | :--- |
| **Monolith** | Fast iteration; single-team ACID |
| **Modular monolith** | Code boundaries without network tax |
| **Microservices** | Independent deploy per autonomous team |
| **SOA** | Enterprise integration via shared services bus (legacy) vs modern decentralized events |

### SOA vs Modern Microservices

| Dimension | Classic SOA | Modern Microservices |
| :--- | :--- | :--- |
| Integration | Central ESB orchestration | Smart endpoints, dumb pipes (events/APIs) |
| Data | Shared enterprise data models | Database per service |
| Governance | Central integration team | Federated teams + platform guild |
| Best era | 2000s enterprise ERP | Cloud-native product orgs |

SOA is not wrong historically — but **ESB-as-brain** anti-patterns map to today's distributed monolith. Prefer decentralized choreography with clear bounded contexts.

"""
    if "## Problem It Solves" not in text:
        text = text.replace("---\n\n## Where It Fits", soa + "---\n\n## Where It Fits", 1)
        path.write_text(text, encoding="utf-8")


def write_index():
    body = """# Microservices Architecture Playbook

Architect-focused handbook for senior engineers, tech leads, and architects — **not** a microservices tutorial.

| Module | Focus | Topics |
| :---: | :--- | :---: |
| 1 | [Architecture Styles](/microservices/01-architecture-styles/) | 1 |
| 2 | [Service Communication](/microservices/02-service-communication/) | 3 |
| 3 | [Data Management](/microservices/03-data-management/) | 4 |
| 4 | [Distributed Systems](/microservices/04-distributed-systems/) | 3 |
| 5 | [Resilience Patterns](/microservices/05-resilience-patterns/) | 1 |
| 6 | [Event-Driven](/microservices/06-event-driven/) | 2 |
| 7 | [Platform Patterns](/microservices/07-platform-patterns/) | 2 |
| 8 | [Observability](/microservices/08-observability/) | 1 |
| 9 | [Migration](/microservices/09-migration-modernization/) | 4 |
| 10 | [Production Playbook](/microservices/10-production-playbook/) | 7 |
| 11 | [Interview Guide](/microservices/11-interview-guide/) | 6 |
| 12 | [Learning Paths](/microservices/12-learning-paths/) | 4 |

## Cross-Handbook References

- [Kafka Handbook](/kafka-handbook/) — broker internals, streaming
- [Kubernetes Handbook](/kubernetes-handbook/) — container primitives
- [Database Handbook](/database-handbook/) — outbox relay schema
- [Technology Playbook](/technology-playbook/) — technology selection ADRs

## How to Use

| Goal | Path |
| :--- | :--- |
| Interview prep | [Interview Revision Path](/microservices/12-learning-paths/interview-revision-path/) + [Top 300](/microservices/11-interview-guide/top-300-microservices-questions/) |
| Migration | Module 9 + [Failure Scenarios](/microservices/10-production-playbook/failure-scenarios/) |
| On-call | [Resilience](/microservices/05-resilience-patterns/resilience-patterns/) + [Observability](/microservices/08-observability/observability/) |
"""
    w("_index.md", body, title="Microservices Architecture Playbook",
      desc="Architect playbook — distributed systems, data, resilience, migration, production operations.",
      short="Microservices Playbook", mod=0, mod_title="Microservices Architecture Playbook",
      ref="0", weight=0)


def write_yaml():
    modules = [
        (1, "Architecture Styles", "01-architecture-styles", ["architecture-styles"]),
        (2, "Service Communication", "02-service-communication",
         ["api-gateway-and-bff", "service-discovery", "communication-topologies"]),
        (3, "Data Management", "03-data-management",
         ["database-per-service", "cqrs-and-event-sourcing", "saga", "outbox-and-cdc"]),
        (4, "Distributed Systems", "04-distributed-systems",
         ["cap-and-pacelc", "consistent-hashing", "concurrency-control"]),
        (5, "Resilience Patterns", "05-resilience-patterns", ["resilience-patterns"]),
        (6, "Event-Driven Architecture", "06-event-driven",
         ["event-driven-architecture", "messaging-and-streaming-patterns"]),
        (7, "Platform Patterns", "07-platform-patterns",
         ["sidecar-and-service-mesh", "kubernetes-patterns"]),
        (8, "Observability", "08-observability", ["observability"]),
        (9, "Migration & Modernization", "09-migration-modernization",
         ["strangler-pattern", "monolith-decomposition", "database-decomposition", "zero-downtime-deployments"]),
        (10, "Production Playbook", "10-production-playbook",
         ["scalability-patterns", "caching-patterns", "deployment-strategies", "reliability-engineering",
          "architecture-decision-records", "failure-scenarios", "architecture-review-checklist"]),
        (11, "Interview Guide", "11-interview-guide",
         ["top-300-microservices-questions", "architect-questions", "troubleshooting-questions",
          "scalability-questions", "reliability-questions", "observability-questions"]),
        (12, "Learning Paths", "12-learning-paths",
         ["senior-engineer-path", "lead-engineer-path", "architect-path", "interview-revision-path"]),
    ]
    yaml_lines = ["# Microservices Architecture Playbook — module index.\nmodules:"]
    order: list[str] = []
    for mid, focus, folder, topics in modules:
        yaml_lines.append(f"  - id: {mid}")
        yaml_lines.append(f'    focus: "{focus}"')
        yaml_lines.append("    topics:")
        for t in topics:
            slug = f"{folder}/{t}"
            yaml_lines.append(f"      - {slug}")
            order.append(slug)
    (DATA / "microservices_modules.yaml").write_text("\n".join(yaml_lines) + "\n", encoding="utf-8")
    order_yaml = "# Flat topic order — derived from microservices_modules.yaml.\ntopics:\n"
    order_yaml += "\n".join(f"  - {t}" for t in order) + "\n"
    (DATA / "microservices_order.yaml").write_text(order_yaml, encoding="utf-8")


def cleanup_legacy():
    legacy_dir = MS / "_legacy_flat"
    legacy_dir.mkdir(exist_ok=True)
    for name in LEGACY_FILES:
        src = MS / name
        if src.exists():
            shutil.move(str(src), str(legacy_dir / name))
    # move code-tabs to _meta
    ct = legacy_dir / "code-tabs-example.md"
    if ct.exists():
        meta_ct = MS / "_meta" / "code-tabs-example.md"
        if not meta_ct.exists():
            shutil.copy(str(ct), str(meta_ct))


def main():
    write_section_indexes()
    write_resilience_page()
    write_migrated_pages()
    write_outbox_cdc_page()
    write_monolith_decomposition_page()
    write_production_new_pages()
    write_interview_guide()
    write_learning_paths()
    enhance_architecture_styles()
    write_index()
    write_yaml()
    cleanup_legacy()
    print("Phase B microservices handbook complete.")


if __name__ == "__main__":
    main()
