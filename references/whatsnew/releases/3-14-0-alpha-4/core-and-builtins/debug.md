# Python 3.14.0 alpha 4 / core and builtins / debug

[gh-127705](https://github.com/python/cpython/issues/127705): Introduce stackref diagnostics that activate once `Py_STACKREF_DEBUG` is enabled. They catch every double-close and leak, recording where the value came from along with its most recent borrow.

Inspired by HPy's debug mode. [https://docs.hpyproject.org/en/latest/debug-mode.html](https://docs.hpyproject.org/en/latest/debug-mode.html)

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
