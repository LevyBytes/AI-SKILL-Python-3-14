# Python 3.12.0 alpha 1 / core and builtins / yield value instruction s operand stack depth

[gh-89914](https://github.com/python/cpython/issues/89914): The `YIELD_VALUE` instruction's operand is now the stack depth. This aids frame handling on `yield` and may help debuggers.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
