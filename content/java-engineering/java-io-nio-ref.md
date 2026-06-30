---
title: "Java IO & NIO Reference"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Streams vs channels, Path/Files, buffers, selectors, and migration path."
tags: ["java", "java-engineering", "handbook"]
categories: ["Java Engineering Handbook"]
shortTitle: "IO & NIO"
module: 10
moduleTitle: "Platform APIs"
sectionRef: "10.1"
ShowToc: true
cheatSheet: true
---

## At a Glance

- Classic IO: stream-oriented, blocking — `InputStream`/`Reader`.
- NIO: buffers, channels, selectors — scalable non-blocking servers.
- NIO.2 (7+): `Path`, `Files` — preferred file API.
- `transferTo`/`mmap` for bulk zero-copy where supported.

---

## Reference Tables

| API | Model | Blocking |
| :--- | :--- | :---: |
| `InputStream` | Byte stream | Yes |
| `Reader` | Char stream | Yes |
| `FileChannel` | Byte channel | Configurable |
| `SocketChannel` + `Selector` | Multiplex | Non-blocking |
| `Files.readAllLines` | Convenience | Yes |

| Operation | API |
| :--- | :--- |
| Walk tree | `Files.walk`, `walkFileTree` |
| Copy/move | `Files.copy`, `Files.move` |
| Attributes | `Files.readAttributes` |
| Watch dir | `WatchService` |

| Buffer key methods | |
| :--- | :--- |
| `flip` | Prepare for read after write |
| `clear` | Reset for write |
| `compact` | Partial consume |

---

## Snippets

```java
Path dir = Path.of("/data/inbox");
try (var lines = Files.lines(dir.resolve("events.jsonl"))) {
    lines.map(this::parse).forEach(this::handle);
}

long copied = inChannel.transferTo(0, inChannel.size(), outChannel);
```

---

## Internals & Gotchas

- `Files.lines` uses stream — must close (try-with-resources).
- `DirectByteBuffer` off-heap — GC via `Cleaner`, not young GC.
- `Selector` wake-up/spurious wakeup patterns on shutdown.

---

## Production Notes

- Set charset explicitly — `StandardCharsets.UTF_8`.
- Large files: stream, don't `readAllBytes`.
- For high-performance IO: Netty or mapped files with measurement.

---

## Interview Probes


{< interview-answer >}
**Q:** NIO vs NIO.2?

**A:** NIO (1.4): channels/buffers/selectors. NIO.2 (7): Path/Files/AsynchronousFileChannel — file system focus. Colloquially 'NIO' often means whole package tree.
{< /interview-answer >}

{< interview-answer >}
**Q:** When mmap?

**A:** Large read-mostly files, random access — OS page cache leverage. Writes and portability complexity.
{< /interview-answer >}

---

## See Also

- [Previous: Recent Features](/java-engineering/java-recent-features/)
- [Next: Reflection](/java-engineering/reflection-annotations-ref/)
- [Java Engineering Handbook Index](/java-engineering/)
