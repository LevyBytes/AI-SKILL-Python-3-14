# Python 3.12.0 alpha 2 / build / development

[gh-98831](https://github.com/python/cpython/issues/98831): Add fresh tooling under `Tools/cases_generator` that produces the interpreter switch statement out of a list of opcode definitions. Only the addition, change, or removal of instruction definitions is touched by this. Those instruction definitions now reside in `Python/bytecodes.c`, expressed in a [custom DSL (under development)](https://github.com/faster-cpython/ideas/blob/main/3.12/interpreter_definition.md). The tooling consumes that file and emits `Python/generated_cases.c.h`, which `Python/ceval.c` then includes to furnish the bulk of the cases for the main interpreter switch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
