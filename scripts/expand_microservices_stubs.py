#!/usr/bin/env python3
"""Expand thin microservices stub pages from recovered legacy _legacy_flat content."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECOVER = ROOT / "_recover"
CONTENT = ROOT / "content" / "microservices"

# legacy filename -> new relative path under content/microservices
MAPPING = {
    "architectural-pragmatist-monolith-vs-microservices.md": "01-architecture-styles/architecture-styles.md",
    "microservices-communication-topologies.md": "02-service-communication/communication-topologies.md",
    "dynamic-service-discovery-registry.md": "02-service-communication/service-discovery.md",
    "database-per-microservice.md": "03-data-management/database-per-service.md",
    "cqrs-event-sourcing.md": "03-data-management/cqrs-and-event-sourcing.md",
    "monolithic-database-decomposition.md": "09-migration-modernization/database-decomposition.md",
    "cap-theorem-pacelc-framework.md": "04-distributed-systems/cap-and-pacelc.md",
    "consistent-hashing-rings-virtual-nodes.md": "04-distributed-systems/consistent-hashing.md",
    "database-isolation-levels-concurrency-control.md": "04-distributed-systems/concurrency-control.md",
    "event-driven-architecture-log-streaming.md": "06-event-driven/event-driven-architecture.md",
    "point-to-point-message-queues.md": "06-event-driven/messaging-and-streaming-patterns.md",
    "sidecar-integration-pattern.md": "07-platform-patterns/sidecar-and-service-mesh.md",
    "service-mesh-architecture.md": "07-platform-patterns/sidecar-and-service-mesh.md",
    "declarative-container-orchestration-kubernetes.md": "07-platform-patterns/kubernetes-patterns.md",
    "application-containerization-docker.md": "07-platform-patterns/kubernetes-patterns.md",
    "three-pillars-observability.md": "08-observability/observability.md",
    "distributed-tracing-log-aggregation.md": "08-observability/observability.md",
    "strangler-fig-application-pattern.md": "09-migration-modernization/strangler-pattern.md",
    "zero-downtime-deployment-topologies.md": "09-migration-modernization/zero-downtime-deployments.md",
    "database-sharding-horizontal-partitioning.md": "10-production-playbook/scalability-patterns.md",
    "database-replication-scaling.md": "10-production-playbook/scalability-patterns.md",
    "distributed-rate-limiting-throttling.md": "10-production-playbook/scalability-patterns.md",
    "distributed-caching-invalidation.md": "10-production-playbook/caching-patterns.md",
    "consumer-driven-contract-testing-cdct.md": "10-production-playbook/reliability-engineering.md",
}

SECTION_MAP = [
    (r"Core Microservices Pattern.*", "## Executive Summary"),
    (r"Production-Grade Implementation.*", "## Architecture Diagram"),
    (r"Runtime Execution Path.*", "## Internal Working"),
    (r"Choreography vs.*|API Gateway vs.*|Architecture Decision Matrix|Five-Phase Migration|When to Decompose.*", "## Design Options"),
    (r"Critical System Design Trade-offs.*", "## Tradeoffs"),
    (r"Network & Latency Impact", "### Network & Latency"),
    (r"Data Consistency & Isolation", "### Data Consistency"),
    (r"Failure Modes & Cascading Risk", "## Common Failures"),
    (r"Interview Failure Modes.*", "## Interview Questions"),
    (r'The "Junior" Mistake', "### Junior Mistake"),
    (r'The "Senior" Counter-Measure', "### Senior Counter-Measure"),
    (r"Conway's Law Alignment", "## Design Decisions"),
    (r"Cutover Gate.*", "## Production Lessons"),
]


def parse_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---"):
        return "", text
    end = text.find("\n---", 3)
    if end == -1:
        return "", text
    return text[: end + 4], text[end + 4 :].lstrip("\n")


def clean_body(body: str) -> str:
    body = body.replace("\r\n", "\n")
    # Fix common mojibake from recovery
    replacements = {
        "ΓÇö": "—",
        "ΓÇÖ": "'",
        "ΓåÆ": "→",
        "Γöé": "│",
        "Γû╝": "▼",
        "Γöö": "└",
        "Γö¼": "┬",
        "ΓöÇ": "─",
        "ΓöÉ": "┐",
        "Γöÿ": "┘",
        "Γ£ô": "✓",
        "├ù": "×",
        "┬╖": "·",
    }
    for old, new in replacements.items():
        body = body.replace(old, new)
    return body


def transform_headings(body: str) -> str:
  lines = []
  for line in body.split("\n"):
    matched = False
    for pattern, replacement in SECTION_MAP:
      if re.match(pattern, line.strip().lstrip("#").strip(), re.I) or (
        line.startswith("###") and re.search(pattern, line, re.I)
      ):
        if not line.startswith("##"):
          lines.append(replacement)
          matched = True
          break
    if matched:
      continue
    if line.startswith("### "):
      title = line[4:].strip()
      if title.startswith("Runtime") or title.startswith("Coordination"):
        lines.append("## Internal Working")
      else:
        lines.append(f"### {title}")
    elif line.startswith("#### "):
      lines.append(f"### {line[5:].strip()}")
    else:
      lines.append(line)
  return "\n".join(lines)


def append_standard_sections(body: str) -> str:
    extras = """

---

## Where It Fits

Apply at service boundaries within the microservices fleet. Cross-link to domain handbooks for broker, database, and cache engine internals.

---

## Security Considerations

Apply zero-trust between services, mTLS in mesh, and least-privilege credentials per service identity.

---

## Observability

Export RED metrics, structured logs with `trace_id`, and distributed traces on every cross-service hop. See [Observability](/microservices/08-observability/observability/).

---

## Architect Notes

Expanded from legacy playbook content. See related modules in the curriculum sidebar for adjacent patterns.
"""
    if "## Where It Fits" not in body:
        body += extras
    return body


def merge_legacy_into_target(legacy_path: Path, target_path: Path) -> None:
    if not legacy_path.exists() or not target_path.exists():
        return
    _, target_fm = parse_frontmatter(target_path.read_text(encoding="utf-8"))
    _, legacy_body = parse_frontmatter(legacy_path.read_text(encoding="utf-8"))
    legacy_body = clean_body(legacy_body)
    legacy_body = transform_headings(legacy_body)
    legacy_body = append_standard_sections(legacy_body)

    # Keep target frontmatter; replace body with expanded legacy
    # Preserve aliases from target
    fm = target_path.read_text(encoding="utf-8").split("---", 2)
    if len(fm) >= 3:
        front = f"---{fm[1]}---"
    else:
        front = ""

    # If target already has substantial content (>120 lines), append legacy core only once
    target_lines = len(target_fm.splitlines())
    if target_lines > 120:
        return

    out = front.rstrip() + "\n\n" + legacy_body.strip() + "\n"
    target_path.write_text(out, encoding="utf-8")
    print(f"expanded {target_path.relative_to(ROOT)}")


def main() -> None:
    merged: dict[str, list[str]] = {}
    for legacy_name, rel in MAPPING.items():
        merged.setdefault(rel, []).append(legacy_name)

    for rel, legacy_names in merged.items():
        target = CONTENT / rel
        for i, legacy_name in enumerate(legacy_names):
            legacy = RECOVER / legacy_name
            if i == 0:
                merge_legacy_into_target(legacy, target)
            else:
                # Append additional legacy sources (mesh + sidecar, etc.)
                if legacy.exists() and target.exists():
                    _, extra = parse_frontmatter(legacy.read_text(encoding="utf-8"))
                    extra = clean_body(transform_headings(extra))
                    text = target.read_text(encoding="utf-8")
                    if legacy_name.replace(".md", "") not in text:
                        target.write_text(
                            text.rstrip() + f"\n\n---\n\n## Related: {legacy_name}\n\n" + extra.strip() + "\n",
                            encoding="utf-8",
                        )
                        print(f"appended {legacy_name} -> {rel}")


if __name__ == "__main__":
    main()
