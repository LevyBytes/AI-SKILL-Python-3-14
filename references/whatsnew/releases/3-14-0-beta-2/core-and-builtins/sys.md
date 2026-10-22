# Python 3.14.0 beta 2 / core and builtins / sys

[gh-134100](https://github.com/python/cpython/issues/134100): Repair a use-after-free defect that surfaces when an imported module is missing from [`sys.modules`](https://docs.python.org/3.14/library/sys.html#sys.modules) once its first import completes. Patch by Nico-Posada.

[gh-133886](https://github.com/python/cpython/issues/133886): Repair [`sys.remote_exec()`](https://docs.python.org/3.14/library/sys.html#sys.remote_exec) for non-ASCII paths under non-UTF-8 locales and for non-UTF-8 paths under UTF-8 locales.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
