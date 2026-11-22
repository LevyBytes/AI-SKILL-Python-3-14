# Python Setup and Usage: installing, building and running Python

![Python 3.14 agent skill: Language + Library, Extensions + C API, Setup + Migration](../../.github/readme-banner.png)

Part of the [Python 3.14 agent skill](../../README.md), this subskill gives Claude Code, Codex and other coding agents 375 reference pages. It covers command-line options and environment variables, build configuration, and setup on Unix, Windows, macOS, Android and iOS, plus editors and IDEs. Its context router is [SKILL.md](SKILL.md) and its catalog is [INDEX.md](INDEX.md); it installs with the parent skill, as described in [Install](../../README.md#install).

**Status: early draft.** The reference pages and per-subskill reference checks are in place; scripts, assets and evaluations will be added over time.

## What's inside

| Starting point | Covers |
| --- | --- |
| [Configure interpreter invocation](command-line/INDEX.md) | Look up command-line options and environment behavior. 109 pages. |
| [Use Python on Windows](windows/INDEX.md) | Find the bundled Windows installation and execution guidance. 53 pages. |
| [Build the interpreter](build-configuration/INDEX.md) | Check configuration options and build requirements. 167 pages. |

## When agents load this subskill

Use when configuring or invoking Python 3.14, choosing command-line options and environment variables, building CPython, or installing and embedding Python on Unix, Windows, macOS, Android or iOS.

## The work behind the references

Invocation, build and platform material have separate indexes, retaining operating-system and interpreter-version conditions with their procedures. Separate routes cover Unix, Windows, macOS, Android and iOS. These references describe Python setup; they do not change the runtime used by an agent session.

## Contributing

Contributions follow the parent skill's process: pull requests are accepted from approved contributors only, after the maintainer reviews and approves an issue. See [CONTRIBUTING](../../.github/CONTRIBUTING.md).

## Sources and license

Skill reference documentation is interpreted content for use in open source projects. Check against [official documentation sources](https://docs.python.org/3.14/) when dealing with defects or issues that may come up from interpreting this skill's references.

Licensed under **Apache-2.0**; see [LICENSE](../../LICENSE). Part of the [Agent Kaizen](https://github.com/LevyBytes/agent-kaizen) skill library.
