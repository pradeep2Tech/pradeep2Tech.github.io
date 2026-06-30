---
title: "Serialization Quick Reference"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Serializable contract, serialVersionUID, Externalizable, and safer alternatives."
tags: ["java", "java-engineering", "handbook"]
categories: ["Java Engineering Handbook"]
shortTitle: "Serialization"
module: 10
moduleTitle: "Platform APIs"
sectionRef: "10.3"
ShowToc: true
cheatSheet: true
---

## At a Glance

- Java serialization: brittle, slow, security risk — avoid for new cross-service contracts.
- Prefer JSON/Protobuf/Avro with schema evolution.
- If required: `serialVersionUID`, explicit `readObject` validation.
- `Externalizable` manual control vs default reflection walk.

---

## Reference Tables

| Mechanism | Pros | Cons |
| :--- | :--- | :--- |
| `Serializable` | Built-in | Fragile, opaque |
| `Externalizable` | Control | Boilerplate |
| JSON + Jackson | Human, interoperable | Schema discipline |
| Protobuf | Compact, versioned | Codegen |

| Security | Mitigation |
| :--- | :--- |
| Gadget chains | Don't deserialize untrusted |
| | `ObjectInputFilter` (9+) |
| | Allowlist classes |

| UID rule | |
| :--- | :--- |
| Change incompatible fields | Bump `serialVersionUID` |
| Compatible add optional field | Often OK with defaults |

| Alternative | When |
| :--- | :--- |
| `Record` + JSON | APIs |
| `ByteBuffer` + schema | High perf internal |

---

## Snippets

```java
private static final ObjectInputFilter filter =
    ObjectInputFilter.Config.createFilter(
"com.myapp.**;java.base/java.lang.String;!*");

ObjectInputStream ois = new ObjectInputStream(in);
ois.setObjectInputFilter(filter);
```

---

## Internals & Gotchas

- `writeObject`/`readObject` hooks for custom serialization.
- `transient` skips fields.
- Enum serialization special-cased by name.

---

## Production Notes

{{% warning %}}
Never accept Java serialized blobs from untrusted clients — RCE history.
{{% /warning %}}
- Migrate session replication to JSON or sticky sessions.
- RMI/JMX exposure audit in legacy apps.

---

## Interview Probes


{< interview-answer >}
**Q:** serialVersionUID purpose?

**A:** Version handshake — mismatch throws `InvalidClassException`. Without explicit UID, compiler generates from structure — fragile across compilers.
{< /interview-answer >}

{< interview-answer >}
**Q:** ObjectInputFilter?

**A:** JDK allowlist/denylist during deserialization — defense in depth if legacy serialization unavoidable.
{< /interview-answer >}

---

## See Also

- [Previous: Reflection](/java-engineering/reflection-annotations-ref/)
- [Next: Collections Big-O](/java-engineering/collections-complexity/)
- [Java Engineering Handbook Index](/java-engineering/)
