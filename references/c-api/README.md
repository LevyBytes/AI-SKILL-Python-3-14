# Python/C API: objects, reference counting and the runtime

![Python 3.14 agent skill: Language + Library, Extensions + C API, Setup + Migration](../../.github/readme-banner.png)

Part of the [Python 3.14 agent skill](../../README.md), this subskill gives Claude Code, Codex and other coding agents 683 reference pages. It covers the abstract and concrete object layers, reference counting and memory management, type objects and slots, initialization and thread state, subinterpreters, monitoring and the stable ABI. Its context router is [SKILL.md](SKILL.md) and its catalog is [INDEX.md](INDEX.md); it installs with the parent skill, as described in [Install](../../README.md#install).

**Status: early draft.** The reference pages and per-subskill reference checks are in place; scripts, assets and evaluations will be added over time.

## What's inside

| Starting point | Covers |
| --- | --- |
| [Check object protocols](abstract-objects-layer/INDEX.md) | Find the generic object interfaces used by native extension code. 2 pages. |
| [Define extension modules](defining-extension-modules/INDEX.md) | Locate module definitions and their interpreter-facing contracts. 6 pages. |
| [Choose an ABI boundary](api-and-abi-versioning/INDEX.md) | Distinguish versioned API and ABI guarantees. 4 pages. |

## When agents load this subskill

Use when writing C/C++ extension modules or embedding CPython 3.14: Python objects, reference ownership, type layouts, object and container protocols, calls, buffers, Unicode, exceptions, memory, modules, interpreter initialization, GIL/thread state, subinterpreters, monitoring, or Stable/Limited/Unstable C API contracts. Not for ordinary Python-only application code or another Python version's undocumented behavior.

## The work behind the references

Native interfaces are grouped by object family and runtime responsibility, retaining signatures, ownership conditions and version constraints with the reference prose. Examples target the documented CPython version and ABI, and their reference ownership, thread state and interpreter-lifecycle requirements apply when adapting them.

## Contributing

Contributions follow the parent skill's process: pull requests are accepted from approved contributors only, after the maintainer reviews and approves an issue. See [CONTRIBUTING](../../.github/CONTRIBUTING.md).

## Sources and license

Skill reference documentation is interpreted content for use in open source projects. Check against [official documentation sources](https://docs.python.org/3.14/) when dealing with defects or issues that may come up from interpreting this skill's references.

Licensed under **Apache-2.0**; see [LICENSE](../../LICENSE). Part of the [Agent Kaizen](https://github.com/LevyBytes/agent-kaizen) skill library.
