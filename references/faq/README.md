# Python FAQs: design, programming, library, extending and Windows

![Python 3.14 agent skill: Language + Library, Extensions + C API, Setup + Migration](../../.github/readme-banner.png)

Part of the [Python 3.14 agent skill](../../README.md), this subskill gives Claude Code, Codex and other coding agents 188 reference pages. It covers the general, design and history, programming, library, extending and embedding, Windows, GUI and installed-Python FAQs. Its context router is [SKILL.md](SKILL.md) and its catalog is [INDEX.md](INDEX.md); it installs with the parent skill, as described in [Install](../../README.md#install).

**Status: early draft.** The reference pages and per-subskill reference checks are in place; scripts, assets and evaluations will be added over time.

## What's inside

| Starting point | Covers |
| --- | --- |
| [Explain language design](design/INDEX.md) | Find documented reasons behind Python language choices. 29 pages. |
| [Investigate programming behavior](programming/INDEX.md) | Look up common coding questions and their explanations. 68 pages. |
| [Answer Windows questions](windows/INDEX.md) | Locate platform-specific execution and installation guidance. 10 pages. |

## When agents load this subskill

Use when answering Python FAQ questions about design, history, programming behavior, library tasks, extension or embedding interfaces, Windows execution, GUI toolkits, or why Python is installed.

## The work behind the references

FAQ subjects remain grouped by the question being answered, with separate routes for general, library, extension and graphical-interface topics. Answers hold for their documented version and platform. Formal API and syntax contracts are in the standard library and language reference subskills.

## Contributing

Contributions follow the parent skill's process: pull requests are accepted from approved contributors only, after the maintainer reviews and approves an issue. See [CONTRIBUTING](../../.github/CONTRIBUTING.md).

## Sources and license

Skill reference documentation is interpreted content for use in open source projects. Check against [official documentation sources](https://docs.python.org/3.14/) when dealing with defects or issues that may come up from interpreting this skill's references.

Licensed under **Apache-2.0**; see [LICENSE](../../LICENSE). Part of the [Agent Kaizen](https://github.com/LevyBytes/agent-kaizen) skill library.
