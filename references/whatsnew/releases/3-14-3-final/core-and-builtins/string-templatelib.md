# Python 3.14.3 final / core and builtins / string templatelib

[gh-142402](https://github.com/python/cpython/issues/142402): Correct reference counting when neighboring literal parts get merged during construction of [`string.templatelib.Template`](https://docs.python.org/3.14/library/string.templatelib.html#string.templatelib.Template), which keeps the displaced string object from leaking.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
