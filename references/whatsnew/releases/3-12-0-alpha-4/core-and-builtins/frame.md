# Python 3.12.0 alpha 4 / core and builtins / frame

[gh-99110](https://github.com/python/cpython/issues/99110): A segfault when reaching frames produced by [`PyFrame_New()`](https://docs.python.org/3.14/c-api/frame.html#c.PyFrame_New) is fixed by setting frame->previous to an initial value inside frameobject.c.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
