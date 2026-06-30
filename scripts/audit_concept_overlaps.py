#!/usr/bin/env python3
"""Find conceptual overlaps across curriculum sections."""
import os
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")


def load(name):
    path = os.path.join(DATA, name)
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def flatten_modules(mod_key):
    topics = []
    for m in load(f"{mod_key}.yaml").get("modules") or []:
        topics.extend(m.get("topics") or [])
        for g in m.get("groups") or []:
            topics.extend(g.get("topics") or [])
    return topics


def main():
    sidebar = load("curriculum_sidebar.yaml").get("sections") or {}

    print("=== Order vs modules (including nested groups) ===\n")
    for sec, cfg in sorted(sidebar.items()):
        ord_key = cfg.get("order")
        mod_key = cfg.get("modules")
        if not ord_key:
            continue
        ord_topics = load(f"{ord_key}.yaml").get("topics") or []
        mod_topics = flatten_modules(mod_key) if mod_key else []
        only_ord = sorted(set(ord_topics) - set(mod_topics))
        only_mod = sorted(set(mod_topics) - set(ord_topics))
        if only_ord or only_mod:
            print(f"{sec}:")
            if only_mod:
                print(f"  in modules, missing from order ({len(only_mod)}): {', '.join(only_mod[:8])}")
                if len(only_mod) > 8:
                    print(f"    ... +{len(only_mod) - 8} more")
            if only_ord:
                print(f"  in order, missing from modules ({len(only_ord)}): {', '.join(only_ord[:8])}")
                if len(only_ord) > 8:
                    print(f"    ... +{len(only_ord) - 8} more")
            print()

    tp = set(load("technology_playbook_order.yaml").get("topics") or [])
    ms = set(load("microservices_order.yaml").get("topics") or [])
    db = set(load("database_handbook_order.yaml").get("topics") or [])
    k8s = set(load("kubernetes_handbook_order.yaml").get("topics") or [])

    pairs = [
        ("Saga", "saga-pattern", "saga-pattern-distributed-transactions"),
        ("Outbox", "outbox-pattern", "transactional-outbox-pattern"),
        ("CQRS", "cqrs-pattern", "cqrs-event-sourcing"),
        ("Circuit breaker", "circuit-breaker-pattern", "circuit-breaker-pattern"),
        ("Event-driven", "event-driven-architecture", "event-driven-architecture-log-streaming"),
        ("Bulkhead", "bulkhead-pattern", "bulkhead-isolation-pattern"),
        ("Sidecar", "sidecar-pattern", "sidecar-integration-pattern"),
        ("Service mesh", "service-mesh", "service-mesh-architecture"),
        ("Strangler", "strangler-pattern", "strangler-fig-application-pattern"),
        ("BFF / API gateway", "bff-pattern", "api-gateway-bff-pattern"),
        ("API gateway", "api-gateway", "api-gateway-bff-pattern"),
    ]

    print("=== Conceptual overlaps (by design: ADR summary vs deep dive) ===\n")
    for label, tp_slug, deep_slug in pairs:
        locs = []
        if tp_slug in tp:
            locs.append(f"technology-playbook/{tp_slug}")
        if deep_slug in ms:
            locs.append(f"microservices/{deep_slug}")
        if deep_slug in db:
            locs.append(f"database-handbook/{deep_slug}")
        if tp_slug in ms and f"microservices/{tp_slug}" not in locs:
            locs.append(f"microservices/{tp_slug} (same slug)")
        if len(locs) > 1:
            print(f"  {label}:")
            for loc in locs:
                print(f"    - {loc}")
            print()

    print("=== Handbook vs interview-prep comparison pages ===\n")
    ip = set(load("interview_prep_order.yaml").get("topics") or [])
    for book, topics in [
        ("kafka-handbook", k8s),
        ("kubernetes-handbook", k8s),
        ("database-handbook", db),
    ]:
        overlap = sorted(ip & topics)
        if overlap:
            print(f"  {book} ∩ interview-prep: {overlap}")

    print("\n=== Modules with nested groups (sidebar must support) ===\n")
    for path in sorted(os.listdir(DATA)):
        if not path.endswith("_modules.yaml"):
            continue
        key = path.replace(".yaml", "")
        for m in load(path).get("modules") or []:
            if m.get("groups"):
                n = sum(len(g.get("topics") or []) for g in m["groups"])
                print(f"  {key} module {m.get('id')}: {n} topics in {len(m['groups'])} groups")


if __name__ == "__main__":
    main()
