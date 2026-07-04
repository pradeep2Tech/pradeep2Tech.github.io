---
title: "Library Management System LLD"
date: 2026-07-03T14:00:00+00:00
draft: false
description: "Books, copies, loans, reservations, and fines — inventory and lifecycle design."
tags: ["design-patterns", "lld"]
categories: ["Design Patterns"]
shortTitle: "Library LLD"
module: 8
moduleTitle: "LLD Case Studies"
sectionRef: "8.6"
weight: 806
---

### Problem & Intent

**Library management:** members borrow and return books, reservations queue for unavailable copies, fines accrue on late return. Forces: **inventory per copy**, **loan lifecycle**, **fine policy**.

---

### When to Use / When NOT to Use

| Situation | Include? | Why |
| :--- | :---: | :--- |
| Multiple copies per title | Yes | Copy vs Book separation |
| Reservation queue | Yes | Fairness rules |
| Inter-library loan network | Scope out | Federation complexity |

---

### Structure (Class Diagram)

```mermaid
classDiagram
    class LibraryService {
        +borrow(member, bookId) Loan
        +returnBook(loanId)
        +reserve(member, bookId)
    }
    class Book {
        +isbn
        +title
    }
    class BookCopy {
        +copyId
        +available
    }
    class Loan {
        +dueDate
        +return()
    }
    class Member
    Book "1" --> "*" BookCopy
    LibraryService --> Loan
```

---

### Interaction Flow

```mermaid
sequenceDiagram
    participant M as Member
    participant L as LibraryService
    participant C as BookCopy
    M->>L: borrow(bookId)
    L->>C: mark unavailable
    L-->>M: Loan + dueDate
```

---

### Implementation

{{< impl-tabs default="java" java="Java" golang="Go" python="Python" >}}
{{< impl-tab lang="java" >}}

```java
public record Loan(String id, String memberId, String copyId, LocalDate dueDate) {
    public Money fineOn(LocalDate returnDate, FinePolicy policy) {
        return policy.calculate(dueDate, returnDate);
    }
}
```

{{< /impl-tab >}}
{{< impl-tab lang="golang" >}}

```go
type Loan struct {
    ID, MemberID, CopyID string
    DueDate            time.Time
}
```

{{< /impl-tab >}}
{{< impl-tab lang="python" >}}

```python
from dataclasses import dataclass
from datetime import date
from typing import Protocol

class FinePolicy(Protocol):
    def calculate(self, due: date, returned: date) -> float: ...

@dataclass
class Loan:
    id: str
    member_id: str
    copy_id: str
    due_date: date

    def fine_on(self, returned: date, policy: FinePolicy) -> float:
        return policy.calculate(self.due_date, returned)
```

{{< /impl-tab >}}
{{< /impl-tabs >}}

---

### Trade-offs & Operational Realities

| Decision | Tradeoff |
| :--- | :--- |
| Fine as Strategy | Flexible policies |
| Reservation FIFO | Simple; priority needs heap |

---

### Junior Mistakes

- Single `Book` entity with `available: boolean` for 50 copies.
- Fines calculated in controller.

---

### Senior Questions

1. How do two members reserve the last copy?
2. State vs Strategy for loan status?

---

### Revision Cheat Sheet

- **Book** (title) vs **BookCopy** (inventory unit).
- **Loan** owns return + fine calculation hook.

---

### See Also

- [State Pattern](/design-patterns/04-behavioral-patterns/state-pattern/)
- [Library fine anti-patterns](/design-patterns/07-anti-patterns/anemic-domain-model/)
