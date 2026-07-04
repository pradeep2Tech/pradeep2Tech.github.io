"""Build DSA & Coding handbook — sync yaml registry from problem data, prune orphans."""
from __future__ import annotations

from pathlib import Path

from dsa_coding_questions_data import MODULES, SUPPORT_MODULES, all_topics

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
CONTENT = ROOT / "content" / "dsa-coding"

KEEP_ROOT = {"_index.md"}


def write_modules_yaml() -> None:
    lines = ["# DSA & Coding — module index (canonical structure).", "modules:"]
    for mod in MODULES:
        lines.append(f"  - id: {mod.id}")
        lines.append(f'    focus: "{mod.focus}"')
        lines.append("    topics:")
        lines.append(f"      - {mod.folder}/_index")
        for p in mod.problems:
            lines.append(f"      - {mod.folder}/{p.slug}")
    for mod_id, focus, folder, topics in SUPPORT_MODULES:
        lines.append(f"  - id: {mod_id}")
        lines.append(f'    focus: "{focus}"')
        lines.append("    topics:")
        for t in topics:
            lines.append(f"      - {folder}/{t}")
    (DATA / "dsa_coding_modules.yaml").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_order_yaml(topics: list[str]) -> None:
    header = (
        "# Flat topic order — derived from dsa_coding_modules.yaml.\n"
        "# Prefer editing scripts/dsa_coding_questions_data.py for structure changes.\n"
        "topics:\n"
    )
    (DATA / "dsa_coding_order.yaml").write_text(
        header + "".join(f"  - {t}\n" for t in topics),
        encoding="utf-8",
    )


def prune_orphans(expected: set[str]) -> int:
    deleted = 0
    for path in CONTENT.rglob("*.md"):
        if path.parent == CONTENT and path.name in KEEP_ROOT:
            continue
        rel = path.relative_to(CONTENT).with_suffix("").as_posix()
        if rel not in expected:
            path.unlink()
            deleted += 1
            print(f"Deleted orphan {path.relative_to(ROOT)}")
    return deleted


def validate_files(expected: list[str]) -> list[str]:
    missing = []
    for rel in expected:
        path = CONTENT / f"{rel}.md"
        if not path.exists():
            missing.append(rel)
    return missing


def main() -> None:
    write_modules_yaml()
    ordered = all_topics()
    write_order_yaml(ordered)

    expected = set(ordered)
    missing = validate_files(ordered)
    if missing:
        raise SystemExit(f"Missing pages: {missing[:5]}{'...' if len(missing) > 5 else ''}")

    deleted = prune_orphans(expected)
    print(f"Build complete: {len(ordered)} topics, {deleted} orphans removed.")


if __name__ == "__main__":
    main()
