"""Build Spring Boot Handbook pages from data/spring_boot_modules.yaml."""
from __future__ import annotations

from pathlib import Path

import yaml

from generate_spring_boot_handbook_refactor import (
    EXTRA_RELATED,
    PAGES,
    SECTION,
    SECTION_TITLE,
    TOPIC_META,
)

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
CONTENT = ROOT / "content" / "spring-boot"


def flatten_topics(modules: list) -> list[str]:
    topics: list[str] = []
    for mod in modules:
        if mod.get("groups"):
            for group in mod["groups"]:
                topics.extend(group["topics"])
        else:
            topics.extend(mod["topics"])
    return topics


def iter_module_topics(modules: list) -> list[tuple[int, str, str, int]]:
    result: list[tuple[int, str, str, int]] = []
    for mod in modules:
        mod_id = mod["id"]
        mod_title = mod["focus"]
        slugs = flatten_topics([mod])
        for idx, slug in enumerate(slugs, start=1):
            result.append((mod_id, mod_title, slug, idx))
    return result


def write_order_yaml(topics: list[str], path: Path) -> None:
    header = (
        "# Flat topic order — derived from spring_boot_modules.yaml.\n"
        "# Prefer editing data/spring_boot_modules.yaml for module structure.\n"
        "topics:\n"
    )
    path.write_text(header + "".join(f"  - {s}\n" for s in topics), encoding="utf-8")


def see_also_links(slug: str, ordered: list[str]) -> str:
    if slug == "interview-questions":
        return ""
    links: list[str] = []
    seen: set[str] = set()
    idx = ordered.index(slug)

    def add(link: str) -> None:
        if link not in seen:
            seen.add(link)
            links.append(link)

    if idx > 0:
        prev = ordered[idx - 1]
        add(f"- [Previous: {TOPIC_META[prev][1]}](/{SECTION}/{prev}/)")
    if idx < len(ordered) - 1:
        nxt = ordered[idx + 1]
        add(f"- [Next: {TOPIC_META[nxt][1]}](/{SECTION}/{nxt}/)")
    for rel in EXTRA_RELATED.get(slug, []):
        if rel in TOPIC_META:
            add(f"- [{TOPIC_META[rel][1]}](/{SECTION}/{rel}/)")
    add(f"- [100+ Interview Questions](/{SECTION}/interview-questions/)")
    add(f"- [{SECTION_TITLE} Index](/{SECTION}/)")
    add("- [Java Engineering](/java-engineering/)")
    add("- [Microservices Playbook](/microservices/) — Saga, Outbox, CQRS, API Gateway")
    add("- [Kafka Handbook](/kafka-handbook/)")
    add("- [Security Architecture](/security-architecture/)")
    return "\n".join(links)


def append_see_also(body: str, slug: str, ordered: list[str]) -> str:
    if slug == "interview-questions":
        return body
    body = body.rstrip()
    if body.endswith("---"):
        body = body[:-3].rstrip()
    see_also = see_also_links(slug, ordered)
    return body + "\n\n---\n\n## See Also\n\n" + see_also + "\n"


def main() -> None:
    modules_path = DATA / "spring_boot_modules.yaml"
    with open(modules_path, encoding="utf-8") as f:
        modules = yaml.safe_load(f)["modules"]

    ordered = flatten_topics(modules)
    write_order_yaml(ordered, DATA / "spring_boot_order.yaml")

    missing = [s for s in ordered if s not in TOPIC_META or s not in PAGES]
    if missing:
        raise SystemExit(f"Missing meta or body for: {missing}")

    CONTENT.mkdir(parents=True, exist_ok=True)
    written = 0
    for mod_id, mod_title, slug, topic_idx in iter_module_topics(modules):
        body = append_see_also(PAGES[slug], slug, ordered)
        path = CONTENT / f"{slug}.md"
        path.write_text(body, encoding="utf-8")
        written += 1
        print(f"Wrote {path.relative_to(ROOT)}")

    keep = {"_index.md"} | {f"{s}.md" for s in ordered}
    deleted = 0
    for path in CONTENT.glob("*.md"):
        if path.name not in keep:
            path.unlink()
            deleted += 1
            print(f"Deleted {path.relative_to(ROOT)}")

    print(f"\nSummary: {written} pages written, {deleted} deleted, {len(ordered)} topics.")


if __name__ == "__main__":
    main()
