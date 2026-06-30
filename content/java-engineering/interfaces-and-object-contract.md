---
title: "Interfaces & Object Contract"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "equals/hashCode/toString, Comparable, default methods, composition over inheritance."
tags: ["java", "java-engineering", "handbook"]
categories: ["Java Engineering Handbook"]
shortTitle: "Object Contract"
module: 2
moduleTitle: "OOP"
sectionRef: "2.2"
ShowToc: true
cheatSheet: true
---

## At a Glance

- `equals`/`hashCode` contract: equal objects → same hash; implement together.
- `toString` for logs — never parse; use structured logging.
- `Comparable` = natural order; `Comparator` = external/multiple orders.
- Default methods: evolve interfaces without breaking implementors.

---

## Reference Tables

| Method | Contract highlight |
| :--- | :--- |
| `equals(Object)` | Reflexive, symmetric, transitive, consistent; `null` → false |
| `hashCode()` | Must change when fields used in equals change |
| `compareTo` | Consistent with equals if natural ordering is total |
| `clone()` | Shallow by default — prefer copy ctor/factory |

| `equals` implementation checklist | |
| :--- | :--- |
| 1 | `if (this == o) return true` |
| 2 | `if (!(o instanceof Target t)) return false` — pattern match in modern Java |
| 3 | Compare significant fields with `Objects.equals` |
| 4 | Override `hashCode` with same fields |

| Interface evolution | JDK approach |
| :--- | :--- |
| `default` method | Body on interface |
| `static` method | Utility on interface |
| Private method | Shared default helper |

---

## Snippets

```java
@Override
public boolean equals(Object o) {
    return o instanceof User u
&& id == u.id
&& Objects.equals(email, u.email);
}

@Override
public int hashCode() {
    return Objects.hash(id, email);
}

Comparator<User> byName = Comparator.comparing(User::name)
    .thenComparingInt(User::id);
```

---

## Internals & Gotchas

- `instanceof` pattern binding avoids double cast.
- `Comparator` contract: anti-symmetric, transitive; inconsistent with equals OK (e.g. `TreeSet` with comparator not aligned to equals).
- `identityHashCode` ≠ `hashCode` after override.

---

## Production Notes

- Use `Objects.equals` / `hash` — handles nulls.
- For JPA entities: business-key equals or avoid collection membership by entity.
- Document if class is value vs identity type.

---

## Interview Probes


{< interview-answer >}
**Q:** Broken equals/hashCode symptom in HashMap?

**A:** Equal keys land in different buckets → duplicates, 'lost' updates. Or mutations after insert break bucket invariant.
{< /interview-answer >}

{< interview-answer >}
**Q:** Comparable vs Comparator in TreeSet?

**A:** `TreeSet` uses Comparator if provided; else natural order via Comparable. Comparator inconsistent with equals → set may contain 'duplicate' values per equals.
{< /interview-answer >}

---

## See Also

- [Previous: OOP](/java-engineering/oop-quick-ref/)
- [Next: Collection Choice](/java-engineering/collections-decision-matrix/)
- [Java Engineering Handbook Index](/java-engineering/)
