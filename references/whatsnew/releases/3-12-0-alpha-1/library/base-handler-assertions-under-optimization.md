# Python 3.12.0 alpha 1 / library / swap assert statements basehandler raise assertionerror verified behaviour survives

[gh-92886](https://github.com/python/cpython/issues/92886): Swap the `assert` statements in `BaseHandler` for `raise AssertionError()` so the verified behaviour survives even when running under optimizations `(-O)`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
