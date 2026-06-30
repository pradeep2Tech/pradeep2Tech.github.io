---
title: "Functional Java Reference"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Functional interfaces, lambdas, method references, Optional patterns."
tags: ["java", "java-engineering", "handbook"]
categories: ["Java Engineering Handbook"]
shortTitle: "Functional Java"
module: 5
moduleTitle: "Functional & Streams"
sectionRef: "5.1"
ShowToc: true
cheatSheet: true
---

## At a Glance

- `@FunctionalInterface` — one abstract method (SAM); Object methods don't count.
- Lambdas: syntactic sugar for anonymous SAM instances — capture must be effectively final.
- Method references: `Type::static`, `instance::method`, `Type::new`.
- `Optional` — return type for absent values; never fields/parameters/collections.

---

## Reference Tables

| Interface | Method | Typical use |
| :--- | :--- | :--- |
| `Supplier<T>` | `get` | Lazy factory |
| `Consumer<T>` | `accept` | Side effect |
| `Predicate<T>` | `test` | Filter |
| `Function<T,R>` | `apply` | Map |
| `UnaryOperator<T>` | `apply` | Same-type map |
| `BiFunction<T,U,R>` | `apply` | Combine |

| Lambda form | Example |
| :--- | :--- |
| No params | `() -> System.nanoTime()` |
| One param | `x -> x * 2` |
| Block body | `(a, b) -> { validate(a); return a + b; }` |

| Method ref | Equivalent lambda |
| :--- | :--- |
| `String::valueOf` | `x -> String.valueOf(x)` |
| `list::add` | `x -> list.add(x)` |
| `ArrayList::new` | `() -> new ArrayList<>()` |

| Optional anti-use | Prefer |
| :--- | :--- |
| `Optional` field | Nullable or empty object |
| `Optional` parameter | Overloads |
| `get()` without check | `orElseThrow`, `orElse` |

---

## Snippets

```java
Function<String, Integer> len = String::length;
Predicate<User> active = u -> u.status() == Status.ACTIVE;

Optional<User> user = repo.findById(id);
return user.map(User::email).orElseThrow(() -> new NotFoundException(id));
```

---

## Internals & Gotchas

- Lambdas may be invokedynamic + LambdaMetafactory — not always inner classes.
- Serialization of lambdas uses `SerializedLambda` — fragile across versions.
- `Optional` is `final` with private ctor — not for JSON null mapping by default.

---

## Production Notes

- Keep lambdas short; extract named methods when >3 lines.
- Don't parallelize streams solely because lambdas exist.
- Use `Objects.requireNonNull` in factories, not Optional for required params.

---

## Interview Probes


{< interview-answer >}
**Q:** Effectively final — why?

**A:** Captured locals must not change — JVM needs stable closure snapshot without synchronized mutable cell.
{< /interview-answer >}

{< interview-answer >}
**Q:** Optional in API design?

**A:** Good for return types signaling absence. Bad as field (serializable pain) or param (overload clearer).
{< /interview-answer >}

---

## See Also

- [Previous: Generics](/java-engineering/generics-quick-ref/)
- [Next: Streams](/java-engineering/streams-quick-ref/)
- [Java Engineering Handbook Index](/java-engineering/)
