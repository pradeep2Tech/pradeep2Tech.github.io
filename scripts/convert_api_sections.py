#!/usr/bin/env python3
"""Convert ## 3. API Design sections to collapsible api-* shortcodes."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content" / "system-design"

METHOD_PATH_RE = re.compile(
    r"^\*\*`(GET|POST|PUT|PATCH|DELETE|HEAD|OPTIONS)\s+([^`]+)`\*\*\s*$",
    re.MULTILINE,
)
RESPONSE_RE = re.compile(
    r"^Response\s*\(`(\d{3})\s+([^`]+)`\):\s*$",
    re.MULTILINE,
)
SECTION_START = re.compile(r"^## 3\. API Design\s*$", re.MULTILINE)
SECTION_END = re.compile(r"^(?:---\s*\n\s*)?## 4\. ", re.MULTILINE)

SKIP_FILES = {"_index.md", "urlshortner.md"}
SKIP_SUFFIXES = ("-interview-questions.md", "-debate-questions.md")


def extract_api_section(text: str) -> tuple[str, int, int] | None:
    heading = SECTION_START.search(text)
    if not heading:
        return None
    body_start = heading.end()
    rest = text[body_start:]
    end = SECTION_END.search(rest)
    if not end:
        return None
    section = rest[: end.start()]
    abs_start = heading.start()
    abs_end = body_start + end.start()
    return section, abs_start, abs_end


def split_blocks(section: str) -> list[tuple[str, str]]:
    """Split by ### headings. Returns list of (title, body)."""
    parts = re.split(r"^### (.+)$", section, flags=re.MULTILINE)
    if not parts:
        return []
    intro = parts[0].strip()
    blocks: list[tuple[str, str]] = []
    if intro:
        blocks.append(("", intro))
    for i in range(1, len(parts), 2):
        title = parts[i].strip()
        body = parts[i + 1] if i + 1 < len(parts) else ""
        blocks.append((title, body.strip()))
    return blocks


def parse_response(body: str) -> tuple[str | None, str | None, str]:
    m = RESPONSE_RE.search(body)
    if not m:
        return None, None, body
    code, label = m.group(1), m.group(2).strip()
    before = body[: m.start()].strip()
    after = body[m.end() :].strip()
    return code, label, before, after  # type: ignore[return-value]


def parse_response_fixed(body: str) -> tuple[str, str, str, str]:
    m = RESPONSE_RE.search(body)
    if not m:
        return "", "", body.strip(), ""
    code, label = m.group(1), m.group(2).strip()
    before = body[: m.start()].strip()
    after = body[m.end() :].strip()
    return code, label, before, after


def is_error_block(title: str) -> bool:
    t = title.lower()
    return "error" in t and ("http" in t or "code" in t or "status" in t)


def is_non_endpoint_block(title: str, body: str) -> bool:
    if is_error_block(title):
        return True
    if not METHOD_PATH_RE.search(body) and not title:
        return bool(body)
    return False


def extract_method_path(body: str) -> tuple[str, str, str] | None:
    m = METHOD_PATH_RE.search(body)
    if not m:
        return None
    method, path = m.group(1), m.group(2).strip()
    rest = body[m.end() :].strip()
    return method, path, rest


def split_request_response(rest: str) -> tuple[str, str, str, str, str]:
    """Returns pre_request, request, resp_code, resp_label, response_tail."""
    resp_m = RESPONSE_RE.search(rest)
    if resp_m:
        pre_and_req = rest[: resp_m.start()].strip()
        code, label = resp_m.group(1), resp_m.group(2).strip()
        response_tail = rest[resp_m.end() :].strip()
    else:
        pre_and_req = rest.strip()
        code, label, response_tail = "", "", ""

    request = ""
    pre_request = pre_and_req
    req_m = re.search(r"^Request:\s*$", pre_and_req, re.MULTILINE)
    if req_m:
        pre_request = pre_and_req[: req_m.start()].strip()
        request = pre_and_req[req_m.end() :].strip()
    return pre_request, request, code, label, response_tail


def build_overview_table(endpoints: list[tuple[str, str, str, str]]) -> str:
    lines = [
        "| # | Method | Path | Purpose |",
        "| :---: | :--- | :--- | :--- |",
    ]
    for i, (method, path, desc, _) in enumerate(endpoints, 1):
        lines.append(f"| {i} | {method} | `{path}` | {desc} |")
    return "\n".join(lines)


def wrap_shortcode(name: str, inner: str, **params: str) -> str:
    param_str = " ".join(f'{k}="{v}"' for k, v in params.items())
    open_tag = f"{{{{< {name} {param_str} >}}}}" if param_str else f"{{{{< {name} >}}}}"
    inner = inner.strip()
    if not inner:
        return ""
    return f"{open_tag}\n{inner}\n{{{{< /{name} >}}}}"


def convert_endpoint(
    method: str,
    path: str,
    desc: str,
    body: str,
    open_first: bool,
) -> str:
    pre, request, code, label, response_tail = split_request_response(body)

    params: dict[str, str] = {
        "method": method,
        "path": path,
        "desc": desc,
    }
    if open_first:
        params["open"] = "true"

    parts: list[str] = []
    inner_parts: list[str] = []

    if pre:
        inner_parts.append(pre)

    if request:
        inner_parts.append(wrap_shortcode("api-request", request))

    if code:
        inner_parts.append(
            wrap_shortcode("api-response", response_tail, code=code, label=label)
        )
    elif response_tail and not request:
        # GET with query params only, no explicit Response line
        inner_parts.append(wrap_shortcode("api-response", response_tail, code="200", label="OK"))

    # Remaining tables/notes after response json - fold into response or notes
    endpoint_inner = "\n\n".join(p for p in inner_parts if p)
    parts.append(wrap_shortcode("api-endpoint", endpoint_inner, **params))
    return "\n\n".join(parts)


def convert_block(title: str, body: str, open_first: bool) -> tuple[str | None, bool, str | None]:
    """Returns (endpoint_md, consumed_open_flag, standalone_errors_md)."""
    extracted = extract_method_path(body)
    if extracted:
        method, path, rest = extracted
        desc = title if title else f"{method} {path}"
        md = convert_endpoint(method, path, desc, rest, open_first)
        return md, True, None

    if is_error_block(title):
        return None, False, wrap_shortcode("api-errors", body)

    if title and not METHOD_PATH_RE.search(body):
        # e.g. Client Rejection Response (429) with http+json but no method line
        if "429" in title or "```http" in body.lower():
            md = wrap_shortcode(
                "api-endpoint",
                "\n\n".join(
                    filter(
                        None,
                        [
                            body.split("Response")[0].strip() if "Response" in body else "",
                            wrap_shortcode("api-response", body, code="429", label="Too Many Requests")
                            if "```" in body
                            else wrap_shortcode("api-response", body, code="429", label="Too Many Requests"),
                        ],
                    )
                ),
                method="—",
                path="(throttled clients)",
                desc=title,
            )
            return md, True, None

    return None, False, None


def convert_section(section: str) -> str:
    blocks = split_blocks(section)
    endpoints_meta: list[tuple[str, str, str, str]] = []
    for title, body in blocks:
        ex = extract_method_path(body)
        if ex:
            method, path, _ = ex
            endpoints_meta.append((method, path, title or path, body))

    out: list[str] = ["## 3. API Design", ""]
    if endpoints_meta:
        out.append(build_overview_table(endpoints_meta))
        out.append("")

    first_open = True
    pending_errors: list[str] = []

    for title, body in blocks:
        if not title and not body:
            continue
        if not title and body:
            out.append(body)
            out.append("")
            continue

        if is_error_block(title):
            pending_errors.append(wrap_shortcode("api-errors", body))
            continue

        extracted = extract_method_path(body)
        if not extracted:
            # Special blocks without method line
            if "429" in title or "```http" in body:
                pre = body
                if "When a consumer" in body:
                    lines = body.split("\n\n", 1)
                    note = lines[0]
                    payload = lines[1] if len(lines) > 1 else body
                    ep = wrap_shortcode(
                        "api-endpoint",
                        "\n\n".join(
                            [
                                wrap_shortcode("api-notes", note) if note else "",
                                wrap_shortcode("api-response", payload, code="429", label="Too Many Requests"),
                            ]
                        ),
                        method="—",
                        path="Rate limit exceeded",
                        desc=title,
                    )
                    out.append(ep)
                    out.append("")
                    continue
            out.append(f"### {title}")
            out.append("")
            out.append(body)
            out.append("")
            continue

        method, path, rest = extracted
        desc = title
        pre, request, code, label, response_tail = split_request_response(rest)

        params: dict[str, str] = {"method": method, "path": path, "desc": desc}
        if first_open:
            params["open"] = "true"
            first_open = False

        inner: list[str] = []
        if pre:
            inner.append(pre)
        if request:
            inner.append(wrap_shortcode("api-request", request))
        if code:
            inner.append(wrap_shortcode("api-response", response_tail, code=code, label=label))
        elif response_tail:
            # response content without explicit Response (`...`) line
            inner.append(wrap_shortcode("api-response", response_tail, code="200", label="OK"))

        out.append(wrap_shortcode("api-endpoint", "\n\n".join(inner), **params))
        out.append("")

    if pending_errors:
        out.append("**Common HTTP error codes**")
        out.append("")
        out.extend(pending_errors)
        out.append("")

    return "\n".join(out).rstrip() + "\n"


def convert_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if "api-endpoint" in text and "## 3. API Design" in text:
        # Already converted (urlshortner)
        extracted = extract_api_section(text)
        if extracted and "api-endpoint" in extracted[0]:
            return False

    result = extract_api_section(text)
    if not result:
        print(f"  skip (no API section): {path.name}")
        return False

    section, start, end = result
    if "api-endpoint" in section:
        print(f"  skip (already converted): {path.name}")
        return False

    new_section = convert_section(section)
    new_text = text[:start] + new_section + text[end:]
    path.write_text(new_text, encoding="utf-8")
    print(f"  converted: {path.name}")
    return True


def main() -> int:
    files = sorted(CONTENT.glob("*.md"))
    count = 0
    for f in files:
        if f.name in SKIP_FILES or f.name.endswith(SKIP_SUFFIXES):
            continue
        if convert_file(f):
            count += 1
    print(f"\nDone: {count} file(s) converted.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
