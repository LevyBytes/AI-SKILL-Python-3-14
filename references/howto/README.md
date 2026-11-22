# Python HOWTOs: asyncio, logging, regular expressions, free threading and more

![Python 3.14 agent skill: Language + Library, Extensions + C API, Setup + Migration](../../.github/readme-banner.png)

Part of the [Python 3.14 agent skill](../../README.md), this subskill gives Claude Code, Codex and other coding agents 536 reference pages. It covers a conceptual overview of asyncio, logging and its cookbook, regular expressions, sorting, descriptors, the method resolution order, enums, annotations, argparse, sockets, Unicode, free-threaded Python and extensions, remote debugging, profiling with perf and DTrace, and porting to Python 3. Its context router is [SKILL.md](SKILL.md) and its catalog is [INDEX.md](INDEX.md); it installs with the parent skill, as described in [Install](../../README.md#install).

**Status: early draft.** The reference pages and per-subskill reference checks are in place; scripts, assets and evaluations will be added over time.

## What's inside

| Starting point | Covers |
| --- | --- |
| [Understand asynchronous execution](a-conceptual-overview-of-asyncio/INDEX.md) | Read the conceptual guide before selecting lower-level asyncio APIs. 11 pages. |
| [Design application logging](logging-cookbook/INDEX.md) | Find logging patterns and their associated setup. 86 pages. |
| [Work with free-threaded Python](free-threading-python/INDEX.md) | Check the documented conditions and limitations of free-threaded execution. 21 pages. |
| [Understand descriptors](descriptor/INDEX.md) | Follow the language technique and its documented protocol behavior. 35 pages. |

## When agents load this subskill

Use when applying Python HOWTO guidance: asyncio, argparse, curses, descriptors, enums, functional programming, sorting, regular expressions, Unicode, networking, logging, free threading, extension isolation, annotations, migration, GDB, tracing, profiling or remote debugging.

## The work behind the references

The guides preserve their individual subject and historical context, with linked examples and focused indexes for techniques such as descriptors, argparse, annotations and extension isolation. Each guide keeps its named Python version and platform, and historical porting guides apply to the versions they describe.

## Contributing

Contributions follow the parent skill's process: pull requests are accepted from approved contributors only, after the maintainer reviews and approves an issue. See [CONTRIBUTING](../../.github/CONTRIBUTING.md).

## Sources and license

Skill reference documentation is interpreted content for use in open source projects. Check against [official documentation sources](https://docs.python.org/3.14/) when dealing with defects or issues that may come up from interpreting this skill's references.

Licensed under **Apache-2.0**; see [LICENSE](../../LICENSE). Part of the [Agent Kaizen](https://github.com/LevyBytes/agent-kaizen) skill library.
