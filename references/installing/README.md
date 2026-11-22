# Installing Python Modules: pip and package installation

![Python 3.14 agent skill: Language + Library, Extensions + C API, Setup + Migration](../../.github/readme-banner.png)

Part of the [Python 3.14 agent skill](../../README.md), this subskill gives Claude Code, Codex and other coding agents 7 reference pages. It gives the package installation overview and points to the Python Packaging User Guide for detailed workflows. Its context router is [SKILL.md](SKILL.md) and its catalog is [INDEX.md](INDEX.md); it installs with the parent skill, as described in [Install](../../README.md#install).

**Status: early draft.** The reference pages and per-subskill reference checks are in place; scripts, assets and evaluations will be added over time.

## What's inside

| Starting point | Covers |
| --- | --- |
| [Install and update packages](orientation/install-version-pin-upgrade-and-use-virtual-environments.md) | Find the overview of version selection, upgrades and virtual environments. |
| [Choose the installation context](orientation/per-user-scientific-and-multiple-interpreter-installation.md) | Review per-user and multiple-interpreter considerations. |
| [Diagnose setup limitations](orientation/system-python-safety-missing-pip-and-binary-extensions.md) | Check system-interpreter, pip and binary-extension concerns. |

## When agents load this subskill

Use when installing Python packages: the official overview of pip, virtual environments and the detailed packaging guides, not the full packaging workflow.

## The work behind the references

The overview is kept separate from the external packaging guides, preserving the boundary between bundled orientation and detailed installation procedures. Commands depend on the interpreter and environment they target. The full workflow is in the linked official packaging documentation.

## Contributing

Contributions follow the parent skill's process: pull requests are accepted from approved contributors only, after the maintainer reviews and approves an issue. See [CONTRIBUTING](../../.github/CONTRIBUTING.md).

## Sources and license

Skill reference documentation is interpreted content for use in open source projects. Check against [official documentation sources](https://docs.python.org/3.14/) when dealing with defects or issues that may come up from interpreting this skill's references.

Licensed under **Apache-2.0**; see [LICENSE](../../LICENSE). Part of the [Agent Kaizen](https://github.com/LevyBytes/agent-kaizen) skill library.
