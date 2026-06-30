#!/usr/bin/env python3
"""Audit curriculum YAML and content for duplicate/misaligned topics."""
import glob
import os
from collections import Counter, defaultdict

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
CONTENT = os.path.join(ROOT, "content")


def load(path):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def main():
    issues = []

    # Duplicate slugs within order files
    for path in glob.glob(os.path.join(DATA, "*_order.yaml")):
        name = os.path.basename(path)
        topics = load(path).get("topics") or []
        seen = {}
        for i, t in enumerate(topics):
            if t in seen:
                issues.append((name, "duplicate in order", t, f"at {seen[t]} and {i}"))
            else:
                seen[t] = i

    # Duplicate topics across modules
    for path in glob.glob(os.path.join(DATA, "*_modules.yaml")):
        name = os.path.basename(path)
        by_topic = defaultdict(list)
        for m in load(path).get("modules") or []:
            mid = m.get("id")
            all_slugs = list(m.get("topics") or [])
            for g in m.get("groups") or []:
                all_slugs.extend(g.get("topics") or [])
            for t in all_slugs:
                by_topic[t].append(mid)
        for t, mids in by_topic.items():
            if len(mids) > 1:
                issues.append((name, "topic in multiple modules", t, str(mids)))

    # Order vs modules alignment
    sidebar = load(os.path.join(DATA, "curriculum_sidebar.yaml")).get("sections") or {}
    for section, cfg in sidebar.items():
        mod_key = cfg.get("modules")
        ord_key = cfg.get("order")
        if not (mod_key and ord_key):
            continue
        mod_path = os.path.join(DATA, f"{mod_key}.yaml")
        ord_path = os.path.join(DATA, f"{ord_key}.yaml")
        if not (os.path.exists(mod_path) and os.path.exists(ord_path)):
            continue
        mod_topics = []
        for m in load(mod_path).get("modules") or []:
            mod_topics.extend(m.get("topics") or [])
            for g in m.get("groups") or []:
                mod_topics.extend(g.get("topics") or [])
        ord_topics = load(ord_path).get("topics") or []
        only_mod = set(mod_topics) - set(ord_topics)
        only_ord = set(ord_topics) - set(mod_topics)
        if only_mod:
            issues.append((section, "in modules not order", ", ".join(sorted(only_mod)[:12]), ""))
        if only_ord:
            issues.append((section, "in order not modules", ", ".join(sorted(only_ord)[:12]), ""))

    # Stale data files
    stale = [
        "lld_order.yaml",
        "lld_modules.yaml",
        "java_cheatsheet_order.yaml",
        "java_cheatsheet_modules.yaml",
        "database_internals_order.yaml",
        "database_internals_modules.yaml",
        "database_handbook_internals_order.yaml",
        "database_handbook_internals_modules.yaml",
        "system_fundamentals_order.yaml",
        "system_fundamentals_modules.yaml",
    ]
    for s in stale:
        if os.path.exists(os.path.join(DATA, s)):
            issues.append((s, "stale file (unused by sidebar)", "", ""))

    # Order entries without content files
    for section, cfg in sidebar.items():
        ord_key = cfg.get("order")
        if not ord_key:
            continue
        ord_topics = load(os.path.join(DATA, f"{ord_key}.yaml")).get("topics") or []
        sec_dir = os.path.join(CONTENT, section)
        if not os.path.isdir(sec_dir):
            continue
        files = {
            f.replace(".md", "")
            for f in os.listdir(sec_dir)
            if f.endswith(".md") and f != "_index.md"
        }
        for t in ord_topics:
            if t not in files:
                issues.append((section, "order missing file", t, ""))

    # Module topics without content files
    for section, cfg in sidebar.items():
        mod_key = cfg.get("modules")
        if not mod_key:
            continue
        sec_dir = os.path.join(CONTENT, section)
        if not os.path.isdir(sec_dir):
            continue
        files = {
            f.replace(".md", "")
            for f in os.listdir(sec_dir)
            if f.endswith(".md") and f != "_index.md"
        }
        for m in load(os.path.join(DATA, f"{mod_key}.yaml")).get("modules") or []:
            all_slugs = list(m.get("topics") or [])
            for g in m.get("groups") or []:
                all_slugs.extend(g.get("topics") or [])
            for t in all_slugs:
                if t not in files:
                    issues.append((section, "module missing file", t, f"module {m.get('id')}"))

    # Cross-section same slug (conceptual duplication across books)
    slug_locs = defaultdict(list)
    for sec in os.listdir(CONTENT):
        sec_path = os.path.join(CONTENT, sec)
        if not os.path.isdir(sec_path):
            continue
        for f in os.listdir(sec_path):
            if not f.endswith(".md") or f == "_index.md":
                continue
            if f.endswith("-interview-questions.md") or f.endswith("-debate-questions.md"):
                continue
            slug_locs[f.replace(".md", "")].append(sec)

    for slug, secs in sorted(slug_locs.items()):
        if len(secs) > 1:
            issues.append(("cross-section", slug, " | ".join(secs), ""))

    # Technology playbook order vs slim content
    tp_order = load(os.path.join(DATA, "technology_playbook_order.yaml")).get("topics") or []
    tp_dir = os.path.join(CONTENT, "technology-playbook")
    tp_files = {
        f.replace(".md", "")
        for f in os.listdir(tp_dir)
        if f.endswith(".md") and f != "_index.md"
    }
    for t in tp_order:
        if t not in tp_files:
            issues.append(("technology-playbook", "stale order entry", t, "file moved to handbook"))

    print(f"Total issues: {len(issues)}\n")
    for row in sorted(issues, key=lambda x: (x[0], x[1], x[2])):
        print("\t".join(str(c) for c in row if c))


if __name__ == "__main__":
    main()
