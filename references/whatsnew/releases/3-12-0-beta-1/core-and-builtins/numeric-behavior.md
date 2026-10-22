# Python 3.12.0 beta 1 / core and builtins / numeric behavior

[gh-104263](https://github.com/python/cpython/issues/104263): Make `float("nan")` yield a quiet NaN on platforms such as MIPS, where the signalling-versus-quiet bit carries the reverse of its customary meaning. Additionally, add a fresh macro `Py_INFINITY` that mirrors C99's `INFINITY`, and rework the internals so they lean on C99's `NAN` and `INFINITY` macros rather than hard-coded bit patterns for infinities and NaNs. With thanks to Sebastian Berg.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
