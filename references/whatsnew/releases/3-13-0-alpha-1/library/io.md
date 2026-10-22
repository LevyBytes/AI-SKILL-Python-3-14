# Python 3.13.0 alpha 1 / library / io

[gh-62948](https://github.com/python/cpython/issues/62948): The [`io.IOBase`](https://docs.python.org/3.14/library/io.html#io.IOBase) finalizer now reports any `close()` method failures through [`sys.unraisablehook`](https://docs.python.org/3.14/library/sys.html#sys.unraisablehook). Formerly such errors went silently unnoticed by default, surfacing only within [Python Development Mode](https://docs.python.org/3.14/library/devmode.html#devmode) or on a [Python built on debug mode](https://docs.python.org/3.14/using/configure.html#debug-build). Victor Stinner authored the change.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
