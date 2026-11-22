# Python Language Reference: syntax, data model, execution and imports

![Python 3.14 agent skill: Language + Library, Extensions + C API, Setup + Migration](../../.github/readme-banner.png)

Part of the [Python 3.14 agent skill](../../README.md), this subskill gives Claude Code, Codex and other coding agents 388 reference pages. It covers lexical analysis, the data model, the execution model, the import system, expressions, simple and compound statements and the full grammar. Its context router is [SKILL.md](SKILL.md) and its catalog is [INDEX.md](INDEX.md); it installs with the parent skill, as described in [Install](../../README.md#install).

**Status: early draft.** The reference pages and per-subskill reference checks are in place; scripts, assets and evaluations will be added over time.

## What's inside

| Starting point | Covers |
| --- | --- |
| [Check object behavior](data-model/INDEX.md) | Find object protocols and special-method contracts. 157 pages. |
| [Understand execution](execution-model/INDEX.md) | Look up name binding, scopes and execution rules. 11 pages. |
| [Inspect expression semantics](expressions/INDEX.md) | Check the evaluation rules for expressions and operators. 52 pages. |

## When agents load this subskill

Use when checking the Python 3.14 language definition: lexical analysis, literals, object data model and special methods, name binding and execution, imports, expression semantics, simple and compound statements, top-level execution or PEG grammar.

## The work behind the references

Language-definition material is grouped by semantic responsibility, preserving grammar, examples and qualifications with their explanations. This area holds the language contracts; the tutorial and standard library subskills provide learning and module-level guidance.

## Contributing

Contributions follow the parent skill's process: pull requests are accepted from approved contributors only, after the maintainer reviews and approves an issue. See [CONTRIBUTING](../../.github/CONTRIBUTING.md).

## Sources and license

Skill reference documentation is interpreted content for use in open source projects. Check against [official documentation sources](https://docs.python.org/3.14/) when dealing with defects or issues that may come up from interpreting this skill's references.

Licensed under **Apache-2.0**; see [LICENSE](../../LICENSE). Part of the [Agent Kaizen](https://github.com/LevyBytes/agent-kaizen) skill library.
