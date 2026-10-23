# Python HOWTOs

```mermaid
---
config:
  flowchart:
    wrappingWidth: 400
---
flowchart LR
    brand["KAIZEN<br/>SKILL LIBRARY"]:::brand
    skill("Python HOWTOs"):::skill
    first(["Language Techniques"]):::topic
    second(["Concurrency Patterns"]):::topic
    third(["Debugging and Tooling"]):::accent
    brand --- skill
    skill --- first
    skill --- second
    skill --- third
    classDef brand fill:#0f172a,color:#67e8f9,stroke:#22d3ee,stroke-width:2px,font-family:monospace
    classDef skill fill:#172554,color:#eff6ff,stroke:#60a5fa,stroke-width:2px,font-size:20px
    classDef topic fill:#0c4a6e,color:#bae6fd,stroke:#38bdf8,stroke-width:1px
    classDef accent fill:#1e293b,color:#fcd34d,stroke:#f59e0b,stroke-width:1px
    linkStyle default stroke:#38bdf8,stroke-width:1px
```

Task-oriented Python guidance for techniques that need more context than an API entry. The HOWTO collection connects language features, concurrency and development tools through focused explanations and examples.

Use when applying Python HOWTO guidance: asyncio, argparse, curses, descriptors, enums, functional programming, sorting, regular expressions, Unicode, networking, logging, free threading, extension isolation, annotations, migration, GDB, tracing, profiling or remote debugging.

## What this skill helps with

| Task | Useful reference material |
| --- | --- |
| [Understand asynchronous execution](a-conceptual-overview-of-asyncio/INDEX.md) | Read the conceptual guide before selecting lower-level asyncio APIs. |
| [Design application logging](logging-cookbook/INDEX.md) | Find logging patterns and their associated setup. |
| [Work with free-threaded Python](free-threading-python/INDEX.md) | Check the documented conditions and limitations of free-threaded execution. |
| [Understand descriptors](descriptor/INDEX.md) | Follow the language technique and its documented protocol behavior. |

## The work behind the references

The guides preserve their individual subject and historical context, with linked examples and focused indexes for techniques such as descriptors, argparse, annotations and extension isolation.

## Start here

Start with [SKILL.md](SKILL.md) and follow its context routes.

Select the guide for the task and retain its named Python version and platform. Historical porting guides apply to the versions they describe.

## Sources and license

Skill reference documentation is interpreted content for use in open source projects. Check against [official documentation sources](https://docs.python.org/3.14/) when dealing with defects or issues that may come up from interpreting this skill's references.

Licensed under **Apache-2.0**; see [LICENSE](../../LICENSE). Part of the [Agent Kaizen](https://github.com/LevyBytes/agent-kaizen) skill library.
