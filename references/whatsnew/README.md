# Python Release Changes: What's New from Python 2.0 to 3.14

![Python 3.14 agent skill: Language + Library, Extensions + C API, Setup + Migration](../../.github/readme-banner.png)

Part of the [Python 3.14 agent skill](../../README.md), this subskill gives Claude Code, Codex and other coding agents 13,043 reference pages. It covers the What's New guide for every release from 2.0 to 3.14, with porting notes, and the changelogs of individual releases and pre-releases. Its context router is [SKILL.md](SKILL.md) and its catalog is [INDEX.md](INDEX.md); it installs with the parent skill, as described in [Install](../../README.md#install).

**Status: early draft.** The reference pages and per-subskill reference checks are in place; scripts, assets and evaluations will be added over time.

## What's inside

| Starting point | Covers |
| --- | --- |
| [Review Python 3.14 changes](release-3-14/INDEX.md) | Find the bundled 3.14 feature and porting material. 154 pages. |
| [Compare Python 3.13 behavior](release-3-13/INDEX.md) | Inspect the preceding version's documented changes. 120 pages. |
| [Explore release history](INDEX.md) | Select other bundled Python 2.x and 3.x release guides. |

## When agents load this subskill

Use when researching historical Python release changes, new language or standard-library features, PEP introductions, compatibility changes, deprecations, removal schedules, porting guidance or dated CPython maintenance/prerelease fixes. Covers Python 2.0 to 2.7 and 3.0 to 3.14 feature guides and changelogs.

## The work behind the references

Release material is organized chronologically by named version, preserving dated maintenance and prerelease context rather than merging it into current API claims. Historical notes apply only to their named versions; the language and library references hold current API contracts.

## Contributing

Contributions follow the parent skill's process: pull requests are accepted from approved contributors only, after the maintainer reviews and approves an issue. See [CONTRIBUTING](../../.github/CONTRIBUTING.md).

## Sources and license

Skill reference documentation is interpreted content for use in open source projects. Check against [official documentation sources](https://docs.python.org/3.14/) when dealing with defects or issues that may come up from interpreting this skill's references.

Licensed under **Apache-2.0**; see [LICENSE](../../LICENSE). Part of the [Agent Kaizen](https://github.com/LevyBytes/agent-kaizen) skill library.
