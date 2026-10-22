# Python 3.13.0 alpha 2 / library / code

[gh-102895](https://github.com/python/cpython/issues/102895): A `local_exit` parameter was added to [`code.interact()`](https://docs.python.org/3.14/library/code.html#code.interact) so that `exit()` and `quit` no longer close `sys.stdin` and raise `SystemExit`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
