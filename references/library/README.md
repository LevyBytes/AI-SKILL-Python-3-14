# Python Standard Library: built-in functions, types and modules

![Python 3.14 agent skill: Language + Library, Extensions + C API, Setup + Migration](../../.github/readme-banner.png)

Part of the [Python 3.14 agent skill](../../README.md), this subskill gives Claude Code, Codex and other coding agents 4,327 reference pages. It covers built-in functions, types, constants and exceptions and the standard-library modules, from `asyncio`, `pathlib` and `typing` to the 3.14 additions `annotationlib`, `string.templatelib`, `compression.zstd` and `concurrent.interpreters`. Its context router is [SKILL.md](SKILL.md) and its catalog is [INDEX.md](INDEX.md); it installs with the parent skill, as described in [Install](../../README.md#install).

**Status: early draft.** The reference pages and per-subskill reference checks are in place; scripts, assets and evaluations will be added over time.

## What's inside

| Starting point | Covers |
| --- | --- |
| [Check built-in functions](functions/INDEX.md) | Look up function contracts and their version conditions. 74 pages. |
| [Work with filesystem paths](pathlib/INDEX.md) | Find path operations and platform-dependent behavior. 40 pages. |
| [Use asynchronous APIs](asyncio-api-index/INDEX.md) | Navigate the asyncio interfaces and their runtime requirements. 8 pages. |

## When agents load this subskill

Use for the Python 3.14 standard library: built-in functions, types and exceptions; typing and collections; text, binary data and mathematics; files, databases and archives; operating systems, concurrency and asyncio; networking, email, web protocols and markup; GUI tools, testing, debugging, importing and interpreter services.

## The work behind the references

The large library reference is divided into subject-owned files and catalogs, retaining examples, signatures and version restrictions with the APIs they explain. Entries keep their Python version and platform conditions. Core syntax, execution semantics and object protocols are in the language reference subskill.

## Contributing

Contributions follow the parent skill's process: pull requests are accepted from approved contributors only, after the maintainer reviews and approves an issue. See [CONTRIBUTING](../../.github/CONTRIBUTING.md).

## Sources and license

Skill reference documentation is interpreted content for use in open source projects. Check against [official documentation sources](https://docs.python.org/3.14/) when dealing with defects or issues that may come up from interpreting this skill's references.

Licensed under **Apache-2.0**; see [LICENSE](../../LICENSE). Part of the [Agent Kaizen](https://github.com/LevyBytes/agent-kaizen) skill library.
