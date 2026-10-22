# Python 3.13.0 alpha 1 / library / compiler and parser

[gh-105481](https://github.com/python/cpython/issues/105481): Surface opcode metadata by way of `_opcode`.

[gh-105481](https://github.com/python/cpython/issues/105481): Drop `opcode.is_pseudo`, `opcode.MIN_PSEUDO_OPCODE` and `opcode.MAX_PSEUDO_OPCODE`; these arrived in 3.12, lacked documentation, and were not meant for outside callers.

[gh-105481](https://github.com/python/cpython/issues/105481): The `opcode.ENABLE_SPECIALIZATION` symbol (introduced in 3.12 yet undocumented and not meant for outside use) now lives at `_opcode.ENABLE_SPECIALIZATION`, a spot the tests can reach.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
