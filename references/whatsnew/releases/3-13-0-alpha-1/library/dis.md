# Python 3.13.0 alpha 1 / library / dis

[gh-105481](https://github.com/python/cpython/issues/105481): Within the [`dis`](https://docs.python.org/3.14/library/dis.html#module-dis) module the assorted opcode lists are now derived from bytecodes.c rather than being spelled out by hand in opcode.py.

[gh-102676](https://github.com/python/cpython/issues/102676): Tacked the `start_offset`, `cache_offset`, `end_offset`, `baseopname`, `baseopcode`, `jump_target` and `oparg` fields onto [`dis.Instruction`](https://docs.python.org/3.14/library/dis.html#dis.Instruction).

[gh-105481](https://github.com/python/cpython/issues/105481): [`stack_effect()`](https://docs.python.org/3.14/library/dis.html#dis.stack_effect) stops raising an exception when an `oparg` is supplied for an `opcode` that doesn't use its arg, or when none is supplied for an `opcode` that does need it. For that second case, the stack effect comes back for `oparg=0`.

[gh-110249](https://github.com/python/cpython/issues/110249): Provide an `--inline-caches` flag for the `dis` command line.

[gh-107932](https://github.com/python/cpython/issues/107932): Corrected the `dis` module so it correctly reports and shows bytecode lacking source lines.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
