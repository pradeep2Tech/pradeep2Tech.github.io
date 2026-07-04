---
title: "Top 100 Java Interview Questions"
date: 2026-06-30T10:00:00+00:00
draft: false
description: "Index of high-signal Java interview questions with difficulty, topic, and deep-dive links."
tags: ["java", "java-engineering", "handbook", "interview"]
categories: ["Java Engineering Handbook"]
shortTitle: "Top 100"
module: 6
moduleTitle: "Interview Cheat Sheets"
sectionRef: "6.1"
interviewHandbook: true
---


Curated questions for **6+ year** Java engineers. Each links to a detailed interview page.

| # | Question | Difficulty | Topic | Deep Dive |
| --: | :--- | :--- | :--- | :--- |
| 1 | Why is String immutable? | Easy | Strings | [Strings And Enums Interview](/java-engineering/strings-and-enums-interview/) |
| 2 | StringBuilder vs concat in loops? | Easy | Strings | [Strings And Enums Interview](/java-engineering/strings-and-enums-interview/) |
| 3 | Enum vs int constants? | Easy | Enums | [Strings And Enums Interview](/java-engineering/strings-and-enums-interview/) |
| 4 | Composition over inheritance? | Medium | OOP | [Oop Interview](/java-engineering/oop-interview/) |
| 5 | Record vs class? | Medium | OOP | [Oop Interview](/java-engineering/oop-interview/) |
| 6 | What is PECS? | Medium | Generics | [Generics Interview](/java-engineering/generics-interview/) |
| 7 | Type erasure? | Medium | Generics | [Generics Interview](/java-engineering/generics-interview/) |
| 8 | Checked vs unchecked exceptions? | Easy | Exceptions | [Exceptions Interview](/java-engineering/exceptions-interview/) |
| 9 | equals/hashCode contract? | Medium | Object Contract | [Object Contract Interview](/java-engineering/object-contract-interview/) |
| 10 | ArrayList vs LinkedList? | Easy | Collections | [Collection Selection Matrix](/java-engineering/collection-selection-matrix/) |
| 11 | When LinkedHashMap? | Medium | Collections | [Collection Selection Matrix](/java-engineering/collection-selection-matrix/) |
| 12 | HashMap internal structure? | Hard | Collections | [Hashmap Internals](/java-engineering/hashmap-internals/) |
| 13 | HashMap vs TreeMap? | Easy | Collections | [Map Implementations](/java-engineering/map-implementations/) |
| 14 | Why ConcurrentHashMap? | Medium | Collections | [Concurrenthashmap Internals](/java-engineering/concurrenthashmap-internals/) |
| 15 | CHM vs synchronized HashMap? | Medium | Collections | [Concurrent Collections](/java-engineering/concurrent-collections/) |
| 16 | CHM null policy? | Easy | Collections | [Concurrenthashmap Internals](/java-engineering/concurrenthashmap-internals/) |
| 17 | CopyOnWrite when? | Medium | Collections | [Concurrent Collections](/java-engineering/concurrent-collections/) |
| 18 | BlockingQueue purpose? | Easy | Collections | [Concurrent Collections](/java-engineering/concurrent-collections/) |
| 19 | Why are streams lazy? | Medium | Streams | [Streams Collectors Interview Guide](/java-engineering/streams-collectors-interview-guide/) |
| 20 | Parallel stream when? | Medium | Streams | [Streams Collectors Interview Guide](/java-engineering/streams-collectors-interview-guide/) |
| 21 | reduce vs collect? | Medium | Streams | [Streams Collectors Interview Guide](/java-engineering/streams-collectors-interview-guide/) |
| 22 | Optional anti-patterns? | Medium | Streams | [Streams Collectors Interview Guide](/java-engineering/streams-collectors-interview-guide/) |
| 23 | BLOCKED vs WAITING? | Medium | Threading | [Java Threading Interview Guide](/java-engineering/java-threading-interview-guide/) |
| 24 | Thread pool sizing? | Medium | Threading | [Java Threading Interview Guide](/java-engineering/java-threading-interview-guide/) |
| 25 | shutdown vs shutdownNow? | Easy | Threading | [Java Threading Interview Guide](/java-engineering/java-threading-interview-guide/) |
| 26 | What is happens-before? | Hard | JMM | [Java Memory Model](/java-engineering/java-memory-model/) |
| 27 | volatile guarantees? | Medium | JMM | [Java Memory Model](/java-engineering/java-memory-model/) |
| 28 | Why volatile not enough for i++? | Medium | Concurrency | [Locks And Atomics](/java-engineering/locks-and-atomics/) |
| 29 | synchronized vs ReentrantLock? | Medium | Concurrency | [Locks And Atomics](/java-engineering/locks-and-atomics/) |
| 30 | What is CAS? | Medium | Concurrency | [Cas And Lock Free Programming](/java-engineering/cas-and-lock-free-programming/) |
| 31 | ABA problem? | Hard | Concurrency | [Cas And Lock Free Programming](/java-engineering/cas-and-lock-free-programming/) |
| 32 | LongAdder vs AtomicLong? | Medium | Concurrency | [Cas And Lock Free Programming](/java-engineering/cas-and-lock-free-programming/) |
| 33 | ThreadLocal internals? | Hard | Concurrency | [Threadlocal Internals](/java-engineering/threadlocal-internals/) |
| 34 | ThreadLocal leak in pools? | Medium | Concurrency | [Threadlocal Internals](/java-engineering/threadlocal-internals/) |
| 35 | ForkJoinPool work-stealing? | Hard | Concurrency | [Forkjoinpool Internals](/java-engineering/forkjoinpool-internals/) |
| 36 | Deadlock four conditions? | Medium | Concurrency | [Deadlock Detection](/java-engineering/deadlock-detection/) |
| 37 | CountDownLatch vs CyclicBarrier? | Medium | Coordination | [Concurrent Coordination](/java-engineering/concurrent-coordination/) |
| 38 | Semaphore use case? | Easy | Coordination | [Concurrent Coordination](/java-engineering/concurrent-coordination/) |
| 39 | thenApply vs thenCompose? | Medium | Async | [Completablefuture Interview Guide](/java-engineering/completablefuture-interview-guide/) |
| 40 | CompletableFuture executor choice? | Medium | Async | [Completablefuture Interview Guide](/java-engineering/completablefuture-interview-guide/) |
| 41 | Platform vs virtual threads? | Medium | Virtual Threads | [Virtual Threads Interview Guide](/java-engineering/virtual-threads-interview-guide/) |
| 42 | What is pinning? | Hard | Virtual Threads | [Virtual Threads Interview Guide](/java-engineering/virtual-threads-interview-guide/) |
| 43 | ScopedValue vs ThreadLocal? | Medium | Virtual Threads | [Virtual Threads Interview Guide](/java-engineering/virtual-threads-interview-guide/) |
| 44 | Stack vs heap? | Easy | JVM | [Jvm Memory Gc Oom Guide](/java-engineering/jvm-memory-gc-oom-guide/) |
| 45 | Minor vs major GC? | Medium | JVM | [Jvm Memory Gc Oom Guide](/java-engineering/jvm-memory-gc-oom-guide/) |
| 46 | Generational hypothesis? | Medium | JVM | [Jvm Memory Gc Oom Guide](/java-engineering/jvm-memory-gc-oom-guide/) |
| 47 | G1 vs ZGC? | Hard | JVM | [Jvm Memory Gc Oom Guide](/java-engineering/jvm-memory-gc-oom-guide/) |
| 48 | Memory leak with GC? | Medium | JVM | [Jvm Memory Gc Oom Guide](/java-engineering/jvm-memory-gc-oom-guide/) |
| 49 | Metaspace OOM cause? | Medium | JVM | [Classloader Memory Leaks](/java-engineering/classloader-memory-leaks/) |
| 50 | Soft vs weak vs phantom? | Medium | JVM | [Reference Types Interview](/java-engineering/reference-types-interview/) |
| 51 | Class loader delegation? | Medium | JVM | [Classloader Internals](/java-engineering/classloader-internals/) |
| 52 | Classloader leak on redeploy? | Hard | JVM | [Classloader Memory Leaks](/java-engineering/classloader-memory-leaks/) |
| 53 | Escape analysis? | Hard | JVM | [Jit Escape Analysis Safepoints](/java-engineering/jit-escape-analysis-safepoints/) |
| 54 | Safepoint purpose? | Medium | JVM | [Jit Escape Analysis Safepoints](/java-engineering/jit-escape-analysis-safepoints/) |
| 55 | JIT C1 vs C2? | Medium | JVM | [Jvm Internals](/java-engineering/jvm-internals/) |
| 56 | TLAB purpose? | Medium | JVM | [Jvm Memory Gc Oom Guide](/java-engineering/jvm-memory-gc-oom-guide/) |
| 57 | -XX:MaxRAMPercentage? | Easy | JVM Flags | [Jvm Flags And Tuning](/java-engineering/jvm-flags-and-tuning/) |
| 58 | Heap dump on OOM? | Easy | JVM Flags | [Jvm Flags And Tuning](/java-engineering/jvm-flags-and-tuning/) |
| 59 | GC logging flag (11+)? | Easy | JVM Flags | [Jvm Flags And Tuning](/java-engineering/jvm-flags-and-tuning/) |
| 60 | Reflection performance? | Medium | Platform | [Reflection Interview](/java-engineering/reflection-interview/) |
| 61 | Annotation RUNTIME vs SOURCE? | Easy | Platform | [Reflection Interview](/java-engineering/reflection-interview/) |
| 62 | Why avoid Java serialization? | Medium | Platform | [Serialization Interview](/java-engineering/serialization-interview/) |
| 63 | serialVersionUID purpose? | Easy | Platform | [Serialization Interview](/java-engineering/serialization-interview/) |
| 64 | Why LTS? | Easy | Versions | [Java Version Migration Guide](/java-engineering/java-version-migration-guide/) |
| 65 | Java 17 headline features? | Medium | Versions | [Java Version Migration Guide](/java-engineering/java-version-migration-guide/) |
| 66 | Java 21 headline features? | Medium | Versions | [Java Version Migration Guide](/java-engineering/java-version-migration-guide/) |
| 67 | Primitives vs wrappers in hot loops? | Easy | Language | [Language Fundamentals](/java-engineering/language-fundamentals/) |
| 68 | final on reference? | Easy | Language | [Language Fundamentals](/java-engineering/language-fundamentals/) |
| 69 | Covariant arrays vs generics? | Medium | Language | [Language Fundamentals](/java-engineering/language-fundamentals/) |
| 70 | Overloading vs overriding? | Easy | OOP | [Oop Interview](/java-engineering/oop-interview/) |
| 71 | Sealed classes purpose? | Medium | OOP | [Oop Interview](/java-engineering/oop-interview/) |
| 72 | Comparable vs Comparator? | Easy | Object Contract | [Object Contract Interview](/java-engineering/object-contract-interview/) |
| 73 | HashMap load factor? | Medium | Collections | [Hashmap Internals](/java-engineering/hashmap-internals/) |
| 74 | HashMap treeify threshold? | Hard | Collections | [Hashmap Internals](/java-engineering/hashmap-internals/) |
| 75 | CHM sizeCtl? | Hard | Collections | [Concurrenthashmap Internals](/java-engineering/concurrenthashmap-internals/) |
| 76 | WeakHashMap use case? | Medium | Collections | [Map Implementations](/java-engineering/map-implementations/) |
| 77 | IdentityHashMap use case? | Medium | Collections | [Map Implementations](/java-engineering/map-implementations/) |
| 78 | PriorityQueue iterator order? | Easy | Collections | [Collection Selection Matrix](/java-engineering/collection-selection-matrix/) |
| 79 | fail-fast vs weakly consistent? | Medium | Collections | [Concurrent Collections](/java-engineering/concurrent-collections/) |
| 80 | Spliterator characteristics? | Hard | Streams | [Streams Collectors Interview Guide](/java-engineering/streams-collectors-interview-guide/) |
| 81 | Collectors.toMap merge function? | Easy | Streams | [Streams Collectors Interview Guide](/java-engineering/streams-collectors-interview-guide/) |
| 82 | Effectively final in lambdas? | Easy | Streams | [Streams Collectors Interview Guide](/java-engineering/streams-collectors-interview-guide/) |
| 83 | Thread.start happens-before run? | Easy | JMM | [Java Memory Model](/java-engineering/java-memory-model/) |
| 84 | Double-checked locking fix? | Hard | JMM | [Java Memory Model](/java-engineering/java-memory-model/) |
| 85 | ReadWriteLock when? | Medium | Concurrency | [Locks And Atomics](/java-engineering/locks-and-atomics/) |
| 86 | StampedLock optimistic read? | Hard | Concurrency | [Locks And Atomics](/java-engineering/locks-and-atomics/) |
| 87 | False sharing? | Hard | Concurrency | [Locks And Atomics](/java-engineering/locks-and-atomics/) |
| 88 | VarHandle purpose? | Hard | Concurrency | [Locks And Atomics](/java-engineering/locks-and-atomics/) |
| 89 | AtomicReference use case? | Medium | Concurrency | [Cas And Lock Free Programming](/java-engineering/cas-and-lock-free-programming/) |
| 90 | Phaser vs CyclicBarrier? | Hard | Coordination | [Concurrent Coordination](/java-engineering/concurrent-coordination/) |
| 91 | CompletableFuture allOf vs anyOf? | Medium | Async | [Completablefuture Interview Guide](/java-engineering/completablefuture-interview-guide/) |
| 92 | Structured concurrency goal? | Medium | Virtual Threads | [Virtual Threads Interview Guide](/java-engineering/virtual-threads-interview-guide/) |
| 93 | Object layout mark word? | Hard | JVM | [Memory Diagram Cheatsheet](/java-engineering/memory-diagram-cheatsheet/) |
| 94 | Compressed oops? | Medium | JVM | [Memory Diagram Cheatsheet](/java-engineering/memory-diagram-cheatsheet/) |
| 95 | Direct buffer OOM? | Medium | JVM | [Jvm Memory Gc Oom Guide](/java-engineering/jvm-memory-gc-oom-guide/) |
| 96 | Card table / remembered set? | Hard | JVM | [Jvm Memory Gc Oom Guide](/java-engineering/jvm-memory-gc-oom-guide/) |
| 97 | Humongous object in G1? | Hard | JVM | [Jvm Memory Gc Oom Guide](/java-engineering/jvm-memory-gc-oom-guide/) |
| 98 | Shenandoah vs ZGC? | Hard | JVM | [Jvm Memory Gc Oom Guide](/java-engineering/jvm-memory-gc-oom-guide/) |
| 99 | Deoptimization in JIT? | Hard | JVM | [Jvm Internals](/java-engineering/jvm-internals/) |
| 100 | javac --release vs target? | Medium | Versions | [Java Version Migration Guide](/java-engineering/java-version-migration-guide/) |
| 101 | Module opens vs exports? | Medium | Platform | [Reflection Interview](/java-engineering/reflection-interview/) |
| 102 | Cleaner vs finalization? | Medium | JVM | [Reference Types Interview](/java-engineering/reference-types-interview/) |
| 103 | String intern() cost? | Medium | Strings | [Strings And Enums Interview](/java-engineering/strings-and-enums-interview/) |
| 104 | Text blocks (15+)? | Easy | Strings | [Strings And Enums Interview](/java-engineering/strings-and-enums-interview/) |
| 105 | try-with-resources suppression? | Medium | Exceptions | [Exceptions Interview](/java-engineering/exceptions-interview/) |
| 106 | Arrays.asList vs List.of? | Easy | Collections | [Collection Selection Matrix](/java-engineering/collection-selection-matrix/) |
| 107 | NavigableMap floorKey? | Medium | Collections | [Map Implementations](/java-engineering/map-implementations/) |
| 108 | Record serialization concerns? | Medium | OOP | [Oop Interview](/java-engineering/oop-interview/) |
