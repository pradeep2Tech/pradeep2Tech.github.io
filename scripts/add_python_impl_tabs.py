"""Add Python impl-tab panels to design-patterns posts that only have Java/Go."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DP = ROOT / "content" / "design-patterns"

IMPL_TABS_OPEN = re.compile(
    r'(\{\{<\s*impl-tabs\s+default="[^"]*"\s+java="Java"\s+golang="Go")(\s*)(>\}\}|\}\})'
)
IMPL_TABS_OPEN_WITH_PY = re.compile(r'python="Python"')
IMPL_CLOSE = re.compile(r'\{\{<\s*/impl-tabs\s*>\}\}')

# slug stem -> Python panel inner (without impl-tab wrapper)
SNIPPETS: dict[str, str] = {
    "strategy-pattern": '''**Strategy via Protocol + registry:**

```python
from dataclasses import dataclass
from typing import Protocol

@dataclass
class Cart:
    subtotal: float

class PricingStrategy(Protocol):
    def calculate(self, cart: Cart) -> float: ...

class StandardPricing:
    def calculate(self, cart: Cart) -> float:
        return cart.subtotal

class PremiumPricing:
    def calculate(self, cart: Cart) -> float:
        return cart.subtotal * 0.90

class CheckoutService:
    def __init__(self, strategy: PricingStrategy) -> None:
        self._strategy = strategy

    def total(self, cart: Cart) -> float:
        return self._strategy.calculate(cart)

def pricing_for_tier(tier: str) -> PricingStrategy:
    return {"STANDARD": StandardPricing(), "PREMIUM": PremiumPricing()}[tier]
```

Python favors **Protocols** (structural typing) and **callables** when strategies are stateless.
''',
    "single-responsibility-principle": '''**Violation — god object:**

```python
class OrderManager:
    def place(self, req: dict) -> None:
        self._validate(req)
        self._save(req)
        self._send_email(req)
        self._generate_pdf(req)
```

**Fixed — SRP splits:**

```python
class OrderService:
    def __init__(self, validator, repo, notifier) -> None:
        self._validator = validator
        self._repo = repo
        self._notifier = notifier

    def place(self, req: dict) -> str:
        self._validator.check(req)
        order_id = self._repo.save(req)
        self._notifier.confirm(order_id)
        return order_id
```
''',
    "god-object": '''**Violation:**

```python
class OrderManager:
    def place(self, req: dict) -> None:
        # validate + persist + email + pdf in one class
        ...
```

**Fixed:**

```python
class OrderService:
    def __init__(self, validator, repo, notifier) -> None:
        self._validator = validator
        self._repo = repo
        self._notifier = notifier

    def place(self, req: dict) -> str:
        self._validator.check(req)
        oid = self._repo.save(req)
        self._notifier.confirm(oid)
        return oid
```
''',
    "factory-method-pattern": '''```python
from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def render(self) -> str: ...

class PdfDocument(Document):
    def render(self) -> str:
        return "<pdf>"

class DocumentCreator(ABC):
    @abstractmethod
    def create(self) -> Document: ...

    def deliver(self) -> str:
        return self.create().render()

class PdfCreator(DocumentCreator):
    def create(self) -> Document:
        return PdfDocument()
```
''',
    "singleton-pattern": '''```python
# Prefer module-level singleton or explicit DI — not metaclass tricks.

_config: dict | None = None

def get_config() -> dict:
    global _config
    if _config is None:
        _config = {"loaded": True}
    return _config

# Thread-safe variant:
import threading
_lock = threading.Lock()
def get_config_safe() -> dict:
    global _config
    if _config is None:
        with _lock:
            if _config is None:
                _config = {"loaded": True}
    return _config
```
''',
    "observer-pattern": '''```python
from typing import Callable, List

class EventBus:
    def __init__(self) -> None:
        self._subs: List[Callable[[str], None]] = []

    def subscribe(self, handler: Callable[[str], None]) -> None:
        self._subs.append(handler)

    def publish(self, event: str) -> None:
        for h in list(self._subs):
            h(event)
```
''',
    "decorator-pattern": '''```python
from typing import Protocol

class Notifier(Protocol):
    def send(self, msg: str) -> None: ...

class EmailNotifier:
    def send(self, msg: str) -> None:
        print(f"email: {msg}")

class LoggingDecorator:
    def __init__(self, inner: Notifier) -> None:
        self._inner = inner

    def send(self, msg: str) -> None:
        print("log: sending")
        self._inner.send(msg)
```
''',
    "adapter-pattern": '''```python
class LegacyXmlClient:
    def fetch_xml(self) -> str:
        return "<user id='1'/>"

class UserPort:
    def get_user(self) -> dict:
        raise NotImplementedError

class XmlUserAdapter(UserPort):
    def __init__(self, legacy: LegacyXmlClient) -> None:
        self._legacy = legacy

    def get_user(self) -> dict:
        xml = self._legacy.fetch_xml()
        return {"id": "1", "raw": xml}
```
''',
    "command-pattern": '''```python
from typing import Protocol

class Command(Protocol):
    def execute(self) -> None: ...

class LightOn:
    def execute(self) -> None:
        print("on")

class Remote:
    def __init__(self) -> None:
        self._history: list[Command] = []

    def press(self, cmd: Command) -> None:
        cmd.execute()
        self._history.append(cmd)
```
''',
    "state-pattern": '''```python
from typing import Protocol

class OrderState(Protocol):
    def ship(self, ctx: "Order") -> None: ...
    def cancel(self, ctx: "Order") -> None: ...

class Paid:
    def ship(self, ctx: "Order") -> None:
        ctx.state = Shipped()
    def cancel(self, ctx: "Order") -> None:
        ctx.state = Cancelled()

class Order:
    def __init__(self) -> None:
        self.state: OrderState = Paid()
```
''',
    "builder-pattern": '''```python
from dataclasses import dataclass, field

@dataclass
class HttpRequest:
    method: str = "GET"
    path: str = "/"
    headers: dict = field(default_factory=dict)

class HttpRequestBuilder:
    def __init__(self) -> None:
        self._req = HttpRequest()

    def get(self, path: str) -> "HttpRequestBuilder":
        self._req.method, self._req.path = "GET", path
        return self

    def header(self, k: str, v: str) -> "HttpRequestBuilder":
        self._req.headers[k] = v
        return self

    def build(self) -> HttpRequest:
        return self._req
```
''',
    "rate-limiter": '''```python
import time
from collections import deque

class SlidingWindowLimiter:
    def __init__(self, limit: int, window_sec: float) -> None:
        self._limit = limit
        self._window = window_sec
        self._ts: deque[float] = deque()

    def allow(self) -> bool:
        now = time.monotonic()
        while self._ts and now - self._ts[0] > self._window:
            self._ts.popleft()
        if len(self._ts) >= self._limit:
            return False
        self._ts.append(now)
        return True
```
''',
}

# Shared templates for slug suffix / keyword
ANTI_PATTERN = '''**Violation:**

```python
class OrderManager:
    def place(self, req: dict) -> None:
        # many unrelated responsibilities in one type
        ...
```

**Fixed:**

```python
class OrderService:
    def __init__(self, validator, repo, notifier) -> None:
        self._validator = validator
        self._repo = repo
        self._notifier = notifier

    def place(self, req: dict) -> str:
        self._validator.check(req)
        return self._repo.save(req)
```
'''

SOLID_DIP = '''```python
from typing import Protocol

class Notifier(Protocol):
    def send(self, msg: str) -> None: ...

class OrderService:
    def __init__(self, notifier: Notifier) -> None:
        self._notifier = notifier

    def confirm(self, order_id: str) -> None:
        self._notifier.send(f"Order {order_id} confirmed")
```
'''

ARCH_REPO = '''```python
from typing import Protocol, Optional

class OrderRepository(Protocol):
    def find(self, order_id: str) -> Optional[dict]: ...
    def save(self, order: dict) -> None: ...

class UnitOfWork(Protocol):
    def orders(self) -> OrderRepository: ...
    def commit(self) -> None: ...
    def rollback(self) -> None: ...
```
'''

GENERIC_PROTOCOL = '''```python
from typing import Protocol

class ExamplePort(Protocol):
    def execute(self) -> None: ...

class ExampleService:
    def __init__(self, port: ExamplePort) -> None:
        self._port = port

    def run(self) -> None:
        self._port.execute()
```
'''


def snippet_for(stem: str) -> str:
    if stem in SNIPPETS:
        return SNIPPETS[stem]
    if stem in {"anemic-domain-model", "spaghetti-code", "golden-hammer", "shotgun-surgery"}:
        return ANTI_PATTERN
    if "principle" in stem or stem.startswith("solid"):
        return SOLID_DIP
    if stem in {"repository-and-unit-of-work", "specification-pattern", "dto-entity-mapper-separation"}:
        return ARCH_REPO
    if "lld" in stem or stem.endswith("-system") or stem in {
        "parking-lot", "elevator-control-system", "notification-system",
        "library-management-system", "ride-sharing-system", "task-scheduler-lld",
    }:
        return GENERIC_PROTOCOL.replace("ExamplePort", "DomainPort").replace("ExampleService", "ApplicationService")
    if "comparison" in stem or "vs-" in stem:
        return "**Python note:** compare trade-offs using the Java/Go tabs — Python uses Protocols, dataclasses, and composition similarly.\n\n" + GENERIC_PROTOCOL
    return GENERIC_PROTOCOL


def wrap_python(inner: str) -> str:
    return (
        '{{< impl-tab lang="python" >}}\n\n'
        + inner.strip()
        + "\n\n{{< /impl-tab >}}\n"
    )


def patch_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if "impl-tabs" not in text:
        return False
    if 'lang="python"' in text and 'python="Python"' in text:
        return False

    changed = False

    if 'python="Python"' not in text:
        def add_py_label(m: re.Match[str]) -> str:
            return m.group(1) + ' python="Python"' + m.group(2) + m.group(3)
        new_text, n = IMPL_TABS_OPEN.subn(add_py_label, text)
        if n:
            text = new_text
            changed = True

    if 'lang="python"' not in text:
        stem = path.stem
        panel = wrap_python(snippet_for(stem))
        # Insert before first closing impl-tabs after golang tab
        idx = text.rfind("{{< /impl-tab >}}")
        close_idx = text.find("{{< /impl-tabs >}}", idx)
        if idx == -1 or close_idx == -1:
            return changed
        text = text[:close_idx] + panel + text[close_idx:]
        changed = True

    if changed:
        path.write_text(text, encoding="utf-8")
    return changed


def main() -> None:
    count = 0
    for path in sorted(DP.rglob("*.md")):
        if patch_file(path):
            print(f"Updated {path.relative_to(ROOT)}")
            count += 1
    print(f"\nPatched {count} files.")


if __name__ == "__main__":
    main()
