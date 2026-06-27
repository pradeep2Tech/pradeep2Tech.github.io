import re
from html.parser import HTMLParser

class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.h2_info = []

    def handle_starttag(self, tag, attrs):
        self.stack.append(tag)
        if tag == "h2":
            parent = self.stack[-2] if len(self.stack) > 1 else "ROOT"
            self.h2_info.append((parent, dict(attrs).get("id", "")))

    def handle_endtag(self, tag):
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()

html = open("public/system-design/distributed-rate-limiter/index.html", encoding="utf-8").read()
idx = html.find("sd-collapsible-content")
if idx < 0:
    print("no sd-collapsible-content")
    raise SystemExit(1)
chunk = html[idx : idx + 80000]
# truncate at post-footer
footer = chunk.find('<footer class="post-footer">')
if footer > 0:
    chunk = chunk[:footer]

p = Parser()
p.feed(chunk)
for i, (parent, hid) in enumerate(p.h2_info):
    print(f"{i+1:2} parent=<{parent}> id={hid}")
print("total", len(p.h2_info))
