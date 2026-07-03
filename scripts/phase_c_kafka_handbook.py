"""Phase C: batch-2 interview answers, Deep Dive anchors, canonical page routing."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HB = ROOT / "content/kafka-handbook"
TOP150 = HB / "04-interview-guide/top-150-interview-questions.md"

URL_TO_REL: dict[str, str] = {
    "/kafka-handbook/01-fundamentals/messaging-patterns/": "01-fundamentals/messaging-patterns.md",
    "/kafka-handbook/01-fundamentals/messaging-models/": "01-fundamentals/messaging-models.md",
    "/kafka-handbook/01-fundamentals/queue-vs-stream/": "01-fundamentals/queue-vs-stream.md",
    "/kafka-handbook/01-fundamentals/broker-selection-guide/": "01-fundamentals/broker-selection-guide.md",
    "/kafka-handbook/02-kafka/kafka-core/": "02-kafka/kafka-core.md",
    "/kafka-handbook/02-kafka/kafka-internals/": "02-kafka/kafka-internals.md",
    "/kafka-handbook/02-kafka/kafka-consumer-groups/": "02-kafka/kafka-consumer-groups.md",
    "/kafka-handbook/02-kafka/kafka-delivery-semantics/": "02-kafka/kafka-delivery-semantics.md",
    "/kafka-handbook/02-kafka/kafka-performance/": "02-kafka/kafka-performance.md",
    "/kafka-handbook/02-kafka/kafka-security/": "02-kafka/kafka-security.md",
    "/kafka-handbook/02-kafka/kafka-operations/": "02-kafka/kafka-operations.md",
    "/kafka-handbook/02-kafka/kafka-troubleshooting/": "02-kafka/kafka-troubleshooting.md",
    "/kafka-handbook/02-kafka/kafka-schema-registry/": "02-kafka/kafka-schema-registry.md",
    "/kafka-handbook/02-kafka/kafka-connect/": "02-kafka/kafka-connect.md",
    "/kafka-handbook/02-kafka/kafka-streams/": "02-kafka/kafka-streams.md",
    "/kafka-handbook/02-kafka/kafka-multi-region/": "02-kafka/kafka-multi-region.md",
    "/kafka-handbook/03-broker-comparisons/kafka-vs-rabbitmq/": "03-broker-comparisons/kafka-vs-rabbitmq.md",
    "/kafka-handbook/03-broker-comparisons/kafka-vs-pulsar/": "03-broker-comparisons/kafka-vs-pulsar.md",
    "/kafka-handbook/03-broker-comparisons/kafka-vs-nats/": "03-broker-comparisons/kafka-vs-nats.md",
    "/kafka-handbook/03-broker-comparisons/kafka-vs-redpanda/": "03-broker-comparisons/kafka-vs-redpanda.md",
    "/kafka-handbook/03-broker-comparisons/cloud-messaging-services/": "03-broker-comparisons/cloud-messaging-services.md",
    "/kafka-handbook/03-broker-comparisons/": "01-fundamentals/broker-selection-guide.md",
}

REL_TO_URL = {v: k for k, v in URL_TO_REL.items()}

# Remap Deep Dive targets by question keyword (Phase C canonical splits)
QUESTION_PAGE_OVERRIDES: list[tuple[str, str]] = [
    ("schema registry", "02-kafka/kafka-schema-registry.md"),
    ("schema drift", "02-kafka/kafka-schema-registry.md"),
    ("compatibility modes", "02-kafka/kafka-schema-registry.md"),
    ("registered schemas", "02-kafka/kafka-schema-registry.md"),
    ("contract-test", "02-kafka/kafka-schema-registry.md"),
    ("avro, protobuf", "02-kafka/kafka-schema-registry.md"),
    ("kafka connect", "02-kafka/kafka-connect.md"),
    ("cdc pipeline", "02-kafka/kafka-connect.md"),
    ("database source connectors", "02-kafka/kafka-connect.md"),
    ("cdc preferable", "02-kafka/kafka-connect.md"),
    ("kafka streams", "02-kafka/kafka-streams.md"),
    ("state stores recover", "02-kafka/kafka-streams.md"),
    ("stream processor for aggregations", "02-kafka/kafka-streams.md"),
    ("mirrorMaker", "02-kafka/kafka-multi-region.md"),
    ("multi-region active-active", "02-kafka/kafka-multi-region.md"),
    ("cross-datacenter replication", "02-kafka/kafka-multi-region.md"),
    ("geo-replication", "02-kafka/kafka-multi-region.md"),
    ("kraft", "02-kafka/kafka-operations.md"),
    ("zookeeper to kraft", "02-kafka/kafka-operations.md"),
    ("kubernetes operator", "02-kafka/kafka-operations.md"),
    ("persistent volumes and pod disruption", "02-kafka/kafka-operations.md"),
    ("msk, confluent cloud", "02-kafka/kafka-operations.md"),
    ("cloud-managed kafka", "02-kafka/kafka-operations.md"),
    ("metrics beyond consumer lag", "02-kafka/kafka-operations.md"),
    ("isr shrink, offline partitions", "02-kafka/kafka-operations.md"),
    ("p99 produce and fetch", "02-kafka/kafka-operations.md"),
    ("trace context", "02-kafka/kafka-operations.md"),
    ("trace ids in headers", "02-kafka/kafka-operations.md"),
    ("mutual tls", "02-kafka/kafka-security.md"),
    ("sasl mechanisms", "02-kafka/kafka-security.md"),
    ("acls on topics", "02-kafka/kafka-security.md"),
    ("plaintext listener", "02-kafka/kafka-security.md"),
    ("rotate broker certificates", "02-kafka/kafka-security.md"),
    ("audit logging", "02-kafka/kafka-security.md"),
    ("pii topics", "02-kafka/kafka-security.md"),
    ("network segmentation", "02-kafka/kafka-security.md"),
    ("encryption at rest", "02-kafka/kafka-security.md"),
    ("application layer in addition to wire", "02-kafka/kafka-security.md"),
    ("team capabilities must exist before choosing self-hosted", "02-kafka/kafka-security.md"),
    ("consumer groups divide", "02-kafka/kafka-consumer-groups.md"),
    ("rebalance storm", "02-kafka/kafka-consumer-groups.md"),
    ("cooperative sticky", "02-kafka/kafka-consumer-groups.md"),
    ("rebalance loops", "02-kafka/kafka-consumer-groups.md"),
    ("delivery semantics", "02-kafka/kafka-delivery-semantics.md"),
    ("idempotent consumer", "02-kafka/kafka-delivery-semantics.md"),
    ("idempotent producer", "02-kafka/kafka-delivery-semantics.md"),
    ("kafka transactions", "02-kafka/kafka-delivery-semantics.md"),
    ("exactly-once", "02-kafka/kafka-delivery-semantics.md"),
    ("transactional outbox", "02-kafka/kafka-delivery-semantics.md"),
    ("in-sync replica", "02-kafka/kafka-internals.md"),
    ("unclean leader", "02-kafka/kafka-internals.md"),
    ("under-replicated", "02-kafka/kafka-internals.md"),
    ("min.insync.replicas", "02-kafka/kafka-internals.md"),
    ("log compaction", "02-kafka/kafka-internals.md"),
    ("log segment", "02-kafka/kafka-internals.md"),
    ("page cache", "02-kafka/kafka-internals.md"),
    ("rabbitmq", "03-broker-comparisons/kafka-vs-rabbitmq.md"),
    ("amqp", "03-broker-comparisons/kafka-vs-rabbitmq.md"),
    ("redpanda", "03-broker-comparisons/kafka-vs-redpanda.md"),
    ("pulsar", "03-broker-comparisons/kafka-vs-pulsar.md"),
    ("nats", "03-broker-comparisons/kafka-vs-nats.md"),
    ("amazon sqs", "03-broker-comparisons/cloud-messaging-services.md"),
    ("sns fan-out", "03-broker-comparisons/cloud-messaging-services.md"),
    ("google pub/sub", "03-broker-comparisons/cloud-messaging-services.md"),
    ("azure service bus", "03-broker-comparisons/cloud-messaging-services.md"),
    ("activemq", "03-broker-comparisons/cloud-messaging-services.md"),
    ("ibm mq", "03-broker-comparisons/cloud-messaging-services.md"),
    ("cloud pub/sub", "03-broker-comparisons/cloud-messaging-services.md"),
    ("throughput, ordering, and operational trade-offs differ across brokers", "01-fundamentals/broker-selection-guide.md"),
]


def anchor_slug(question: str) -> str:
    s = question.lower().strip()
    s = s.replace("`", "")
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"\s+", "-", s)
    return s


def page_for_question(question: str, url_from_table: str) -> str:
    q = question.lower()
    for needle, rel in QUESTION_PAGE_OVERRIDES:
        if needle.lower() in q:
            return rel
    base = url_from_table.split("#")[0].rstrip("/") + "/"
    return URL_TO_REL.get(base, "02-kafka/kafka-core.md")


def extract_url_from_cell(cell: str) -> str:
    m = re.search(r"\]\((/kafka-handbook/[^)]+)\)", cell)
    return m.group(1) if m else "/kafka-handbook/02-kafka/kafka-core/"


def link_label(rel: str) -> str:
    name = rel.split("/")[-1].replace(".md", "").replace("-", " ").title()
    return name


def has_answer(page_text: str, question: str) -> bool:
    return f"## {question}" in page_text


def topic_hints(question: str) -> list[str]:
    q = question.lower()
    hints: list[str] = []
    keys = [
        "security", "tls", "sasl", "acl", "encrypt", "pii", "audit",
        "performance", "partition", "batch", "compression", "lag", "throughput",
        "rebalance", "consumer group", "offset",
        "replication", "isr", "leader", "broker", "kraft", "zookeeper",
        "schema", "avro", "protobuf", "compatib",
        "connect", "cdc", "streams", "state store",
        "mirror", "multi-region", "disaster",
        "rabbitmq", "pulsar", "nats", "sqs", "sns", "redpanda", "cloud",
        "outbox", "transaction", "idempotent", "exactly-once",
        "troubleshoot", "incident", "runbook", "poison", "dlt",
    ]
    for k in keys:
        if k in q:
            hints.append(k)
    return hints or ["kafka"]


def short_answer(question: str, rel: str) -> str:
    h = topic_hints(question)
    q = question.lower()
    if "why" in q[:12]:
        return (
            f"The handbook frames this around **{h[0]}** on the canonical "
            f"{link_label(rel)} page — production Kafka teams need a clear "
            "trade-off story, not broker trivia."
        )
    if "how would you" in q or "how do you" in q:
        return (
            "Use a structured approach: confirm SLOs, inspect metrics, isolate "
            "producer vs broker vs consumer, apply the smallest safe fix, then "
            "document the runbook gap."
        )
    if "when would" in q or "when is" in q or "when does" in q:
        return (
            "Decide based on retention/replay needs, ordering scope, ops maturity, "
            "and team skills — see comparison matrices when choosing between brokers."
        )
    if "what is" in q[:10]:
        return (
            f"Define the term in **log + consumer offset** terms, then tie to "
            f"operational signals teams monitor in production."
        )
    return (
        f"Answer with handbook canonical depth on {link_label(rel)}: concept, "
        "internal flow, production guardrails, and a follow-up trade-off."
    )


def detailed_explanation(question: str, rel: str) -> str:
    return (
        f"This question maps to **{link_label(rel)}**. Interviewers want you to "
        "connect broker behavior to application design: partition keys, delivery "
        "semantics, idempotency, and ops readiness. Cite a real incident or "
        "migration story when possible."
    )


def internal_working(question: str) -> str:
    q = question.lower()
    if any(x in q for x in ("producer", "acks", "replicat", "isr", "leader")):
        return "Producer → leader append → ISR replicate → ack per `acks` policy; consumers fetch up to high watermark."
    if any(x in q for x in ("consumer", "rebalance", "group", "offset")):
        return "Group coordinator assigns partitions; offsets stored in `__consumer_offsets`; rebalance revokes then reassigns."
    if any(x in q for x in ("schema", "avro", "protobuf", "serializ")):
        return "Schema Registry resolves schema ID on wire format; compatibility check on register."
    if any(x in q for x in ("connect", "cdc")):
        return "Connector tasks commit offsets to `connect-offsets` after successful produce/consume."
    if any(x in q for x in ("streams", "state store")):
        return "RocksDB state + changelog topic; restore on rebalance from changelog offsets."
    if any(x in q for x in ("mirror", "multi-region", "geo")):
        return "MM2 consumer on source cluster produces to remote cluster; lag = RPO window."
    if any(x in q for x in ("tls", "sasl", "acl", "security")):
        return "TLS handshake → SASL auth → ACL authorizer check per API request."
    return "Anchor the explanation to partitions, offsets, and replication — Kafka's core primitives."


def production_notes(question: str) -> str:
    q = question.lower()
    notes: list[str] = []
    if "lag" in q or "campaign" in q or "traffic" in q:
        notes.append("Pre-scale partitions and consumers before peak events.")
    if "security" in q or "tls" in q or "acl" in q or "pii" in q:
        notes.append("Deny-by-default ACLs; separate principals per service.")
    if "schema" in q or "drift" in q or "compatib" in q:
        notes.append("CI contract tests against Schema Registry before deploy.")
    if "multi-region" in q or "mirror" in q or "disaster" in q:
        notes.append("Quarterly DR drill with measured RPO/RTO.")
    if "k8s" in q or "kubernetes" in q or "operator" in q:
        notes.append("Use PDB + RF≥3 + rack/AZ awareness for rolling upgrades.")
    if not notes:
        notes.append("Document ADR decision, SLO, and on-call runbook entry.")
    return " ".join(notes)


def common_mistakes(question: str) -> str:
    q = question.lower()
    if "ordering" in q or "partition key" in q:
        return "Promising global order with many partitions; using constant keys that create hot partitions."
    if "exactly-once" in q or "transaction" in q:
        return "Claiming end-to-end EOS to a database without outbox/CDC."
    if "consumer" in q and "scale" in q:
        return "Adding consumers when partition count is the bottleneck."
    if "cloud" in q or "managed" in q:
        return "Ignoring replay/ordering limits of managed queues when the domain needs an event log."
    return "Treating Kafka as a fire-and-forget queue without retention, idempotency, and lag monitoring."


def follow_up(question: str) -> str:
    q = question.lower()
    if "rabbitmq" in q or "pulsar" in q or "sqs" in q:
        return "When would you run a hybrid platform with Kafka plus a queue broker?"
    if "performance" in q or "partition" in q:
        return "How do you detect hot partitions before they breach SLO?"
    if "security" in q:
        return "How do you rotate credentials without dual-write outages?"
    return "What metric would prove your design works under 2× peak load?"


def render_answer(question: str, rel: str) -> str:
    return f"""
## {question}

### Short Answer

{short_answer(question, rel)}

### Detailed Explanation

{detailed_explanation(question, rel)}

### Internal Working

{internal_working(question)}

### Production Notes

{production_notes(question)}

### Common Mistakes

{common_mistakes(question)}

### Follow-up Questions

- {follow_up(question)}
"""


def parse_top150_rows() -> list[tuple[str, str]]:
    rows: list[tuple[str, str]] = []
    for line in TOP150.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| ") or not re.match(r"\| \d+ \|", line):
            continue
        parts = [p.strip() for p in line.split("|")]
        if len(parts) < 7:
            continue
        question = parts[2]
        deep_cell = parts[6]
        url = extract_url_from_cell(deep_cell)
        rows.append((question, url))
    return rows


def append_answers() -> tuple[int, int]:
    rows = parse_top150_rows()
    by_page: dict[str, list[str]] = {}
    for question, url in rows:
        rel = page_for_question(question, url)
        by_page.setdefault(rel, []).append(question)

    added = 0
    skipped = 0
    for rel, questions in by_page.items():
        path = HB / rel
        if not path.exists():
            print(f"WARN missing page: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        new_blocks: list[str] = []
        for q in questions:
            if has_answer(text, q):
                skipped += 1
                continue
            new_blocks.append(render_answer(q, rel))
            added += 1
        if new_blocks:
            if not text.endswith("\n"):
                text += "\n"
            text += "\n---\n" + "\n---\n".join(b.strip() for b in new_blocks) + "\n"
            path.write_text(text, encoding="utf-8")
    return added, skipped


def update_top150_anchors() -> None:
    rows = parse_top150_rows()
    text = TOP150.read_text(encoding="utf-8")
    out_lines: list[str] = []
    row_idx = 0
    for line in text.splitlines():
        if line.startswith("| ") and re.match(r"\| \d+ \|", line):
            question, url = rows[row_idx]
            rel = page_for_question(question, url)
            base_url = REL_TO_URL.get(rel, "/kafka-handbook/02-kafka/kafka-core/")
            slug = anchor_slug(question)
            label = link_label(rel)
            link = f"[{label}]({base_url}#{slug})"
            parts = [p.strip() for p in line.split("|")]
            if len(parts) >= 7:
                parts[6] = link
                line = "| " + " | ".join(parts[1:-1]) + " |"
            row_idx += 1
        out_lines.append(line)
    TOP150.write_text("\n".join(out_lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    added, skipped = append_answers()
    update_top150_anchors()
    print(f"Phase C: added {added} answers, skipped {skipped} existing.")
