"""Fix See Also prev/next links from postgresql_cheatsheet_order.yaml."""
from __future__ import annotations

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
PG = ROOT / "content" / "postgresql-cheatsheet"
DATA = ROOT / "data" / "postgresql_cheatsheet_order.yaml"
SECTION = "postgresql-cheatsheet"


def short_title(path: str) -> str:
    p = PG / f"{path}.md"
    if not p.exists():
        return path.split("/")[-1]
    m = re.search(r'shortTitle: "([^"]+)"', p.read_text(encoding="utf-8"))
    return m.group(1) if m else path.split("/")[-1]


def main() -> None:
    topics = yaml.safe_load(DATA.read_text(encoding="utf-8"))["topics"]
    for i, slug in enumerate(topics):
        p = PG / f"{slug}.md"
        if not p.exists():
            continue
        text = p.read_text(encoding="utf-8")
        links: list[str] = []
        if i > 0:
            prev = topics[i - 1]
            links.append(f"- [Previous: {short_title(prev)}](/{SECTION}/{prev}/)")
        if i < len(topics) - 1:
            nxt = topics[i + 1]
            links.append(f"- [Next: {short_title(nxt)}](/{SECTION}/{nxt}/)")
        links.append(f"- [PostgreSQL Handbook](/{SECTION}/)")
        links.append("- [Database Handbook — PostgreSQL](/database-handbook/postgresql/)")
        new_see = "## See Also\n\n" + "\n".join(links)
        text = re.sub(r"## See Also\n\n.*", new_see, text, flags=re.DOTALL)
        p.write_text(text, encoding="utf-8")
    print(f"Fixed See Also on {len(topics)} pages")


if __name__ == "__main__":
    main()
