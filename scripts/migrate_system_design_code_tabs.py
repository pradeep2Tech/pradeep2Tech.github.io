"""Wrap ```java blocks in system-design posts with impl-tabs (Java + Go)."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SD_DIR = ROOT / "content" / "system-design"

JAVA_FENCE = re.compile(r"```java\n(.*?)```", re.DOTALL)


def wrap_block(java_code: str) -> str:
    java_code = java_code.strip("\n")
    return (
        '{{< impl-tabs default="java" java="Java" golang="Go" >}}\n'
        '{{< impl-tab lang="java" >}}\n\n'
        f"```java\n{java_code}\n```\n\n"
        "{{< /impl-tab >}}\n"
        '{{< impl-tab lang="golang" >}}\n\n'
        "```go\n"
        "// TODO: idiomatic Go equivalent — mirror the Java snippet above\n"
        "```\n\n"
        "{{< /impl-tab >}}\n"
        "{{< /impl-tabs >}}"
    )


def migrate_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if "impl-tabs" in text and "```java" not in text:
        return False
    if not JAVA_FENCE.search(text):
        return False
    new_text = JAVA_FENCE.sub(lambda m: wrap_block(m.group(1)), text)
    if new_text == text:
        return False
    path.write_text(new_text, encoding="utf-8")
    return True


def main() -> None:
    changed = []
    for path in sorted(SD_DIR.glob("*.md")):
        if path.name.endswith("-interview-questions.md"):
            continue
        if migrate_file(path):
            changed.append(path.name)
            print(f"migrated {path.name}")
    print(f"done — {len(changed)} file(s)")


if __name__ == "__main__":
    main()
