# Python 3.12.0 alpha 3 / core and builtins / type

[gh-99298](https://github.com/python/cpython/issues/99298): Eliminate the leftover error paths for attribute specializations, and decline to specialize attribute accesses on types where [`PyType_Ready()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_Ready) hasn't been invoked yet.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
