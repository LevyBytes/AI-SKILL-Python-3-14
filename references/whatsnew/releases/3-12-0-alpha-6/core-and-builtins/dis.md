# Python 3.12.0 alpha 6 / core and builtins / dis

[gh-100982](https://github.com/python/cpython/issues/100982): To permit instrumentation, confine the `FOR_ITER_RANGE` instruction's scope to that of the original [`FOR_ITER`](https://docs.python.org/3.14/library/dis.html#opcode-FOR_ITER) instruction.

[gh-101799](https://github.com/python/cpython/issues/101799): Introduce [`CALL_INTRINSIC_2`](https://docs.python.org/3.14/library/dis.html#opcode-CALL_INTRINSIC_2) and rely on it in place of `PREP_RERAISE_STAR`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
