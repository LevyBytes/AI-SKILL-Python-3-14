# Python 3.14.1 final / core and builtins / concurrent interpreters

[gh-141528](https://github.com/python/cpython/issues/141528): When the warning about leftover subinterpreters fires, recommend [`concurrent.interpreters.Interpreter.close()`](https://docs.python.org/3.14/library/concurrent.interpreters.html#concurrent.interpreters.Interpreter.close) rather than the private `_interpreters.destroy` function. Sergey Miryanov supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
