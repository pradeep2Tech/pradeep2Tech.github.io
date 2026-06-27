from bs4 import BeautifulSoup, NavigableString, Tag

HLD_RE = __import__("re").compile(r"high[- ]level architecture", __import__("re").I)


def is_hld(h2):
    return bool(HLD_RE.search(h2.get_text()))


def direct_h2s(container):
    return [c for c in container.children if isinstance(c, Tag) and c.name == "h2"]


def move_section_content(body, start, root, end_h2):
    node = start
    while node and node is not end_h2:
        if isinstance(node, Tag) and node.name == "h2" and node.parent is root:
            break
        nxt = node.next_sibling
        body.append(node)
        node = nxt


def wrap_subsections(body, soup):
    idx = 0
    while True:
        h3s = [c for c in body.children if isinstance(c, Tag) and c.name == "h3"]
        if not h3s:
            break
        h3 = h3s[0]
        nxt = h3s[1] if len(h3s) > 1 else None
        sub = soup.new_tag("details")
        sub["class"] = ["sd-subsection"]
        summary = soup.new_tag("summary")
        summary["class"] = ["sd-subsection-summary"]
        summary.append(h3.extract())
        sub_body = soup.new_tag("div")
        sub_body["class"] = ["sd-subsection-body"]
        sub.append(summary)
        sub.append(sub_body)
        body.insert(idx, sub)
        move_section_content(sub_body, sub.next_sibling, body, nxt)
        idx += 1


def wrap_hld(container, h2, next_h2, soup):
    block = soup.new_tag("div")
    block["class"] = ["sd-hld-block"]
    container.insert(list(container.children).index(h2), block)
    block.append(h2.extract())
    move_section_content(block, block.next_sibling, container, next_h2)


def unwrap_shortcode_headings(container):
    for h2 in container.find_all("h2", id=lambda x: x and x.startswith("hahahugoshortcode")):
        parent = h2.parent
        for child in list(h2.children):
            h2.insert_before(child.extract() if hasattr(child, "extract") else child)
        h2.decompose()


def wrap_sections(container, soup):
    unwrap_shortcode_headings(container)
    section_index = 0
    while True:
        h2s = direct_h2s(container)
        if not h2s:
            break
        h2 = h2s[0]
        next_h2 = h2s[1] if len(h2s) > 1 else None

        if is_hld(h2):
            wrap_hld(container, h2, next_h2, soup)
            section_index += 1
            continue

        section = soup.new_tag("details")
        section["class"] = ["sd-section"]
        if section_index == 0:
            section["open"] = "open"
        section_index += 1

        summary = soup.new_tag("summary")
        summary["class"] = ["sd-section-summary"]
        body = soup.new_tag("div")
        body["class"] = ["sd-section-body"]

        container.insert(list(container.children).index(h2), section)
        summary.append(h2.extract())
        section.append(summary)
        section.append(body)
        move_section_content(body, section.next_sibling, container, next_h2)
        wrap_subsections(body, soup)


html = open("public/system-design/distributed-rate-limiter/index.html", encoding="utf-8").read()
soup = BeautifulSoup(html, "html.parser")
content = soup.select_one(".sd-collapsible-content")
wrap_sections(content, soup)

sections = content.find_all("details", class_="sd-section", recursive=False)
print("top-level sd-section count:", len(sections))
for i, s in enumerate(sections[:5]):
    h2 = s.find("h2")
    print(i + 1, h2.get_text()[:50] if h2 else "?", "open" if s.has_attr("open") else "closed")

# check if section 2 h2 nested
h2_2 = content.find("h2", id="2-back-of-the-envelope-calculations")
print("h2_2 parent:", h2_2.parent.name, h2_2.parent.get("class") if h2_2.parent else None)
sec2 = h2_2.find_parent("details", class_="sd-section")
print("section2 parent of details:", sec2.parent.name if sec2 else None, sec2.parent.get("class") if sec2 and sec2.parent else None)
