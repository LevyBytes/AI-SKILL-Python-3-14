# Python 3.12.0 alpha 3 / build / compileall

[gh-99289](https://github.com/python/cpython/issues/99289): Add a `COMPILEALL_OPTS` variable to the Makefile so [`compileall`](https://docs.python.org/3.14/library/compileall.html#module-compileall) options (default: `-j0`) can be overridden during `make install`. The `compileall` invocations were also folded into one command that builds .pyc files for every optimization level (0, 1, 2) in a single pass. Victor Stinner contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
