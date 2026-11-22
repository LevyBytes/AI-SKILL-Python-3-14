# Python 3.14 Agent Skill

![Python 3.14 agent skill: Language + Library, Extensions + C API, Setup + Migration](.github/readme-banner.png)

Gives Claude Code, Codex and other coding agents the Python 3.14 (CPython) documentation as 19,903 reference pages in 13 subskills: the standard library, the language reference, the tutorial and HOWTOs, interpreter setup, packaging, C and C++ extensions and the Python/C API, FAQs, the glossary, release changes from Python 2.0 to 3.14 and deprecation schedules. Each subskill loads on its own, so an agent reads the tutorial, the API contract or the release note that a task needs.

**Status: early draft.** The reference pages and per-subskill reference checks are in place; scripts, assets and evaluations will be added over time.

## Install

```sh
npx skills add LevyBytes/AI-SKILL-Python-3-14 -g
```

This installs the skill as `python-3-14` for each coding agent it finds on your computer; without `-g` it goes into the current project only. The command needs Node.js 22.20 or later.

<details>
<summary>Install without Node.js</summary>

Clone the repository into your agent's skills folder:

| Agent | Command |
| --- | --- |
| Claude Code | `git clone https://github.com/LevyBytes/AI-SKILL-Python-3-14 ~/.claude/skills/python-3-14` |
| Codex | `git clone https://github.com/LevyBytes/AI-SKILL-Python-3-14 ~/.agents/skills/python-3-14` |

</details>

## Use

Ask your agent about Python as usual; it loads the skill when a task matches. You can also call it by name with `/python-3-14` in Claude Code or `$python-3-14` in Codex.

- "What do template strings (t-strings) return in Python 3.14, and how do I read their interpolations?"
- "How do I read annotations that refer to names that are not defined yet?"
- "How do I tell whether my interpreter is a free-threaded build with the GIL disabled?"
- "Which standard-library APIs are scheduled for removal in Python 3.15, and what replaces them?"
- "How do I write a C extension type that supports cyclic garbage collection?"

## Subskills

The 13 subskills and 16 shared example pages hold 19,919 pages. Pages keep the documentation's `Added in version`, `Changed in version` and `Deprecated since version` notes, so an answer can be checked against the interpreter in use.

### Standard library: built-in functions, types and modules

[Standard library](references/library/INDEX.md) covers built-in functions, types, constants and exceptions and the standard-library modules, from `asyncio`, `pathlib` and `typing` to the 3.14 additions `annotationlib`, `string.templatelib`, `compression.zstd` and `concurrent.interpreters`. 4,327 pages.

### Language reference: syntax, data model, execution and imports

[Language reference](references/reference/INDEX.md) covers lexical analysis, the data model, the execution model, the import system, expressions, simple and compound statements and the full grammar. 388 pages.

### Tutorial: learning Python with examples

[Tutorial](references/tutorial/INDEX.md) covers the interpreter, control flow, data structures, modules, input and output, errors and exceptions, classes, a tour of the standard library, floating-point arithmetic and virtual environments, for readers who already program. 184 pages.

### HOWTOs: asyncio, logging, regular expressions, free threading and more

[HOWTOs](references/howto/INDEX.md) covers a conceptual overview of asyncio, logging and its cookbook, regular expressions, sorting, descriptors, the method resolution order, enums, annotations, argparse, sockets, Unicode, free-threaded Python and extensions, remote debugging, profiling with perf and DTrace, and porting to Python 3. 536 pages.

### Release changes: What's New from Python 2.0 to 3.14

[Release changes](references/whatsnew/INDEX.md) covers the What's New guide for every release from 2.0 to 3.14, with porting notes, and the changelogs of individual releases and pre-releases. 13,043 pages.

### Deprecations: pending removals and replacements

[Deprecations](references/deprecations/INDEX.md) covers language, library and C API features scheduled for removal in Python 3.13 through 3.19 or without a set date, with the replacement for each. 46 pages.

### Interpreter usage: installing, building and running Python

[Interpreter usage](references/using/INDEX.md) covers command-line options and environment variables, build configuration, and setup on Unix, Windows, macOS, Android and iOS, plus editors and IDEs. 375 pages.

### Python/C API: objects, reference counting and the runtime

[Python/C API](references/c-api/INDEX.md) covers the abstract and concrete object layers, reference counting and memory management, type objects and slots, initialization and thread state, subinterpreters, monitoring and the stable ABI. 683 pages.

### Extending and embedding: C and C++ extensions

[Extending and embedding](references/extending/INDEX.md) covers writing extension modules and custom extension types, building C and C++ extensions, Windows builds and embedding Python in another application. 94 pages.

### FAQs: design, programming, library, extending and Windows

[FAQs](references/faq/INDEX.md) covers the general, design and history, programming, library, extending and embedding, Windows, GUI and installed-Python FAQs. 188 pages.

### Installing modules: pip and package installation

[Installing modules](references/installing/INDEX.md) gives the package installation overview and points to the Python Packaging User Guide for detailed workflows. 7 pages.

### Distributing modules: packaging overview

[Distributing modules](references/distributing/INDEX.md) gives the official distribution overview and points to the Python Packaging User Guide. 4 pages.

### General reference: glossary and documentation

[General reference](references/general/INDEX.md) covers the glossary, documentation conventions and contributors. 28 pages.

## When agents load this skill

Use when writing, debugging or reviewing Python 3.14 (CPython): standard-library APIs, language syntax and object protocols, tutorials and HOWTOs, interpreter setup, package installation and distribution, C/C++ extensions, embedding and the Python/C API. Also use for bundled Python FAQs, terminology, version-specific release changes and deprecation schedules.

## The work behind the references

The documentation is organized into focused subject files with linked prerequisites, examples and continuations. The repair work reviewed code formatting and protected technical content alongside naming and navigation, and kept the version conditions around historical material.

## Contributing

Pull requests are accepted from approved contributors only. To propose a fix or a feature, first open an issue that describes the change your pull request would make, such as a page that differs from the Python 3.14 documentation or an example that fails on CPython 3.14, and the documentation section it should match. The maintainer reviews the issue and your GitHub account, then approves or declines. New maintainers are approved the same way. See [CONTRIBUTING](.github/CONTRIBUTING.md).

## Sources and license

Skill reference documentation is interpreted content for use in open source projects. Check against [official documentation sources](https://docs.python.org/3.14/) when dealing with defects or issues that may come up from interpreting this skill's references.

Licensed under **Apache-2.0**; see [LICENSE](LICENSE). Part of the [Agent Kaizen](https://github.com/LevyBytes/agent-kaizen) skill library.
