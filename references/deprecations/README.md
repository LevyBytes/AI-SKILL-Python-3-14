# Python Deprecations: pending removals and replacements

![Python 3.14 agent skill: Language + Library, Extensions + C API, Setup + Migration](../../.github/readme-banner.png)

Part of the [Python 3.14 agent skill](../../README.md), this subskill gives Claude Code, Codex and other coding agents 46 reference pages. It covers language, library and C API features scheduled for removal in Python 3.13 through 3.19 or without a set date, with the replacement for each. Its context router is [SKILL.md](SKILL.md) and its catalog is [INDEX.md](INDEX.md); it installs with the parent skill, as described in [Install](../../README.md#install).

**Status: early draft.** The reference pages and per-subskill reference checks are in place; scripts, assets and evaluations will be added over time.

## What's inside

| Starting point | Covers |
| --- | --- |
| [Review language and library changes](language-library-removals/INDEX.md) | Locate deprecated features, replacements and documented removal versions. 30 pages. |
| [Review native API changes](c-api-removals/INDEX.md) | Find C API deprecations and migration requirements. 13 pages. |
| [Interpret version conditions](version-and-contract-conditions.md) | Keep scheduled removals distinct from deprecations without a fixed removal date. |

## When agents load this subskill

Use when checking Python deprecated features, scheduled removal versions, migration replacements, compatibility shims, standard-library deprecations or C API removals in the bundled Python 3.14 documentation.

## The work behind the references

The material preserves the version attached to each change, with focused indexes for Python-level behavior and native extension contracts. This is the bundled Python 3.14 deprecation reference. A historical schedule is evidence for its named release, not proof of the behavior of every installed interpreter.

## Contributing

Contributions follow the parent skill's process: pull requests are accepted from approved contributors only, after the maintainer reviews and approves an issue. See [CONTRIBUTING](../../.github/CONTRIBUTING.md).

## Sources and license

Skill reference documentation is interpreted content for use in open source projects. Check against [official documentation sources](https://docs.python.org/3.14/) when dealing with defects or issues that may come up from interpreting this skill's references.

Licensed under **Apache-2.0**; see [LICENSE](../../LICENSE). Part of the [Agent Kaizen](https://github.com/LevyBytes/agent-kaizen) skill library.
