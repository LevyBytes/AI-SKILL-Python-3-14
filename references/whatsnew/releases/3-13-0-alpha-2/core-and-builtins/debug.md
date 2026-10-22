# Python 3.13.0 alpha 2 / core and builtins / debug

[gh-112243](https://github.com/python/cpython/issues/112243): Keep comments out of f-string debug expressions. Pablo Galindo wrote the patch

[gh-111807](https://github.com/python/cpython/issues/111807): Cut the parser stack's maximum depth to 1000 for WASI debug builds.

[gh-111798](https://github.com/python/cpython/issues/111798): With a debug-mode Python build, fix the C recursion limit at 500 rather than 1500. Debug builds usually carry a low optimization level, which means greater stack memory use than a release build. Victor Stinner authored the patch.

[gh-110722](https://github.com/python/cpython/issues/110722): Provide `PYTHON_PRESITE=package.module` for importing a module early during the interpreter lifecycle, ahead of `site.py` running. This option only exists when Python is [built in debug mode](https://docs.python.org/3.14/using/configure.html#debug-build).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
