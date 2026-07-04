---
title: "pytest"
date: 2026-07-03T12:00:00+00:00
draft: false
description: "Fixtures, `conftest.py`, parametrization `@pytest.mark.parametrize`, markers for slow tests."
tags: ["python", "python-cheatsheet", "handbook", "interview"]
categories: ["Python Handbook"]
shortTitle: "pytest"
module: 8
moduleTitle: "Testing"
sectionRef: "8.2"
weight: 802
interviewHandbook: true
---

## Quick Revision

- Fixtures in `conftest.py` — scoped `function`, `module`, `session`.
- `@pytest.mark.parametrize` for table-driven cases.
- `pytest.raises` for exception contracts.

## Core Concepts

| Feature | Use |
| :--- | :--- |
| `fixture` | Setup/teardown reuse |
| `parametrize` | Many inputs, one test function |
| `mark` | slow, integration, skip |
| `monkeypatch` | Env/path stubs |

## Production Usage

```python
import pytest

@pytest.fixture
def client():
    app = create_app(testing=True)
    with app.test_client() as c:
        yield c

@pytest.mark.parametrize("status", [200, 404])
def test_health(client, status):
    ...
```

## Common Mistakes

- Shared mutable fixture state between tests.
- Over-broad `autouse=True` fixtures slowing all tests.



## Interview Questions

See [Top 150](/python-cheatsheet/09-interview-guide/top-150-interview-questions/).

---

## See Also

- [Previous: Testing](/python-cheatsheet/08-testing/testing/)
- [Next: Mocking](/python-cheatsheet/08-testing/mocking/)
- [Python Handbook Index](/python-cheatsheet/)
- [Top 150 Interview Questions](/python-cheatsheet/09-interview-guide/top-150-interview-questions/)
