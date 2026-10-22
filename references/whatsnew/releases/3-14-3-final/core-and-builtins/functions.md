# Python 3.14.3 final / core and builtins / functions

[gh-142554](https://github.com/python/cpython/issues/142554): Address a crash in [`divmod()`](https://docs.python.org/3.14/library/functions.html#divmod) for when `_pylong.int_divmod()` fails to hand back a two-element tuple exactly. Bénédikt Tran authored the patch.

[gh-138568](https://github.com/python/cpython/issues/138568): The built-in [`help()`](https://docs.python.org/3.14/library/functions.html#help) function was tuned so that an empty input is disregarded while in interactive mode.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
