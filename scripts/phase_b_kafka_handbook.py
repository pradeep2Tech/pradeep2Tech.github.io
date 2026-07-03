"""Phase B: update Top 150 Deep Dive links and extract performance questions."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOP150 = ROOT / "content/kafka-handbook/04-interview-guide/top-150-interview-questions.md"
PERF_OUT = ROOT / "content/kafka-handbook/04-interview-guide/performance-questions.md"

# file path prefix -> hugo path
PATH_TO_URL = {
    "content/kafka-handbook/01-fundamentals/messaging-patterns.md": "/kafka-handbook/01-fundamentals/messaging-patterns/",
    "content/kafka-handbook/01-fundamentals/messaging-models.md": "/kafka-handbook/01-fundamentals/messaging-models/",
    "content/kafka-handbook/01-fundamentals/queue-vs-stream.md": "/kafka-handbook/01-fundamentals/queue-vs-stream/",
    "content/kafka-handbook/01-fundamentals/broker-selection-guide.md": "/kafka-handbook/01-fundamentals/broker-selection-guide/",
    "content/kafka-handbook/02-kafka/kafka-core.md": "/kafka-handbook/02-kafka/kafka-core/",
    "content/kafka-handbook/02-kafka/kafka-internals.md": "/kafka-handbook/02-kafka/kafka-internals/",
    "content/kafka-handbook/02-kafka/kafka-consumer-groups.md": "/kafka-handbook/02-kafka/kafka-consumer-groups/",
    "content/kafka-handbook/02-kafka/kafka-delivery-semantics.md": "/kafka-handbook/02-kafka/kafka-delivery-semantics/",
    "content/kafka-handbook/02-kafka/kafka-performance.md": "/kafka-handbook/02-kafka/kafka-performance/",
    "content/kafka-handbook/02-kafka/kafka-security.md": "/kafka-handbook/02-kafka/kafka-security/",
    "content/kafka-handbook/02-kafka/kafka-operations.md": "/kafka-handbook/02-kafka/kafka-operations/",
    "content/kafka-handbook/02-kafka/kafka-troubleshooting.md": "/kafka-handbook/02-kafka/kafka-troubleshooting/",
    "content/kafka-handbook/03-broker-comparisons/kafka-vs-rabbitmq.md": "/kafka-handbook/03-broker-comparisons/kafka-vs-rabbitmq/",
    "content/kafka-handbook/03-broker-comparisons/kafka-vs-pulsar.md": "/kafka-handbook/03-broker-comparisons/kafka-vs-pulsar/",
    "content/kafka-handbook/03-broker-comparisons/kafka-vs-nats.md": "/kafka-handbook/03-broker-comparisons/kafka-vs-nats/",
    "content/kafka-handbook/03-broker-comparisons/kafka-vs-redpanda.md": "/kafka-handbook/03-broker-comparisons/kafka-vs-redpanda/",
    "content/kafka-handbook/03-broker-comparisons/cloud-messaging-services.md": "/kafka-handbook/03-broker-comparisons/cloud-messaging-services/",
    "content/kafka-handbook/module-messaging-streaming.md": "/kafka-handbook/01-fundamentals/broker-selection-guide/",
}

# Remap topics on kafka-core/internals to new canonical pages (by question keyword)
QUESTION_URL_OVERRIDES: list[tuple[str, str]] = [
    ("consumer groups divide partition", "/kafka-handbook/02-kafka/kafka-consumer-groups/"),
    ("rebalance storm", "/kafka-handbook/02-kafka/kafka-consumer-groups/"),
    ("cooperative sticky rebalancing", "/kafka-handbook/02-kafka/kafka-consumer-groups/"),
    ("rebalance loops", "/kafka-handbook/02-kafka/kafka-consumer-groups/"),
    ("session.timeout.ms", "/kafka-handbook/02-kafka/kafka-consumer-groups/"),
    ("duplicate processing during consumer group rebalancing", "/kafka-handbook/02-kafka/kafka-consumer-groups/"),
    ("delivery semantics", "/kafka-handbook/02-kafka/kafka-delivery-semantics/"),
    ("idempotent consumers mandatory", "/kafka-handbook/02-kafka/kafka-delivery-semantics/"),
    ("idempotent producers", "/kafka-handbook/02-kafka/kafka-delivery-semantics/"),
    ("Kafka transactions required", "/kafka-handbook/02-kafka/kafka-delivery-semantics/"),
    ("exactly-once stream processing", "/kafka-handbook/02-kafka/kafka-delivery-semantics/"),
    ("transactional outbox", "/kafka-handbook/02-kafka/kafka-delivery-semantics/"),
    ("schema drift", "/kafka-handbook/02-kafka/kafka-internals/"),
    ("Schema Registry enforce", "/kafka-handbook/02-kafka/kafka-internals/"),
    ("In-Sync Replica", "/kafka-handbook/02-kafka/kafka-internals/"),
    ("unclean leader election", "/kafka-handbook/02-kafka/kafka-internals/"),
    ("under-replicated partitions", "/kafka-handbook/02-kafka/kafka-internals/"),
    ("min.insync.replicas", "/kafka-handbook/02-kafka/kafka-internals/"),
    ("log compaction", "/kafka-handbook/02-kafka/kafka-internals/"),
    ("log segment", "/kafka-handbook/02-kafka/kafka-internals/"),
    ("business keys would you use to make consumer processing idempotent", "/kafka-handbook/02-kafka/kafka-delivery-semantics/"),
    ("minimal consumer design handles at-least-once", "/kafka-handbook/02-kafka/kafka-delivery-semantics/"),
    ("throughput, ordering, and operational trade-offs differ across brokers", "/kafka-handbook/03-broker-comparisons/"),
]


def deep_dive_for_line(line: str) -> str:
    for needle, url in QUESTION_URL_OVERRIDES:
        if needle.lower() in line.lower():
            label = url.rstrip("/").split("/")[-1].replace("-", " ").title()
            return f"[{label}]({url})"
    m = re.search(r"`(content/kafka-handbook/[^`]+)`", line)
    if m:
        path = m.group(1)
        url = PATH_TO_URL.get(path, "/kafka-handbook/")
        label = path.split("/")[-1].replace(".md", "").replace("-", " ").title()
        return f"[{label}]({url})"
    return ""


def update_top150() -> None:
    text = TOP150.read_text(encoding="utf-8")
    text = text.replace("| Related Document |", "| Deep Dive |")
    text = text.replace(
        "Each row maps to a handbook document.",
        "Each row links to the canonical deep-dive page.",
    )
    out_lines = []
    for line in text.splitlines():
        if line.startswith("| ") and re.match(r"\| \d+ \|", line):
            parts = [p.strip() for p in line.split("|")]
            if len(parts) >= 7:
                link = deep_dive_for_line(line)
                if link:
                    parts[6] = link
                    line = "| " + " | ".join(parts[1:-1]) + " |"
        out_lines.append(line)
    TOP150.write_text("\n".join(out_lines) + "\n", encoding="utf-8")


def extract_performance_questions() -> None:
    text = TOP150.read_text(encoding="utf-8")
    section = "# Top 25 Performance & Scalability Questions"
    if section not in text:
        return
    block = text.split(section, 1)[1].split("\n# ", 1)[0]
    questions = []
    for line in block.splitlines():
        line = line.strip()
        if line and line[0].isdigit() and ". " in line[:4]:
            questions.append(line.split(". ", 1)[1])
    fm = """---
title: "Performance & Scalability Questions"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "Top 25 performance and scalability questions from the Kafka handbook question bank."
tags: ["kafka-handbook", "kafka", "messaging", "streaming", "interview"]
categories: ["Kafka Handbook"]
shortTitle: "Performance"
module: 4
moduleTitle: "Interview Guide"
sectionRef: "4.4"
weight: 404
ShowToc: true
interviewHandbook: true
---

Questions only — no answers. Sourced from [Top 150](/kafka-handbook/04-interview-guide/top-150-interview-questions/).

# Top 25 Performance & Scalability Questions

"""
    body = "\n".join(f"{i}. {q}" for i, q in enumerate(questions, 1))
    PERF_OUT.write_text(fm + body + "\n", encoding="utf-8")


if __name__ == "__main__":
    update_top150()
    extract_performance_questions()
    print("Top 150 Deep Dive links updated; performance-questions.md created.")
