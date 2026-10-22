# Python 3.12.0 alpha 4 / core and builtins / dis

[gh-99005](https://github.com/python/cpython/issues/99005): Add a new [`CALL_INTRINSIC_1`](https://docs.python.org/3.14/library/dis.html#opcode-CALL_INTRINSIC_1) instruction. Drop `IMPORT_STAR`, `PRINT_EXPR` and `STOPITERATION_ERROR`, swapping them for the `CALL_INTRINSIC_1` instruction.

[gh-90043](https://github.com/python/cpython/issues/90043): Deal with NaNs while specializing [`COMPARE_OP`](https://docs.python.org/3.14/library/dis.html#opcode-COMPARE_OP) for [`float`](https://docs.python.org/3.14/library/functions.html#float) values.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
