# Python 3.14.0 alpha 5 / core and builtins / exceptions

[gh-115911](https://github.com/python/cpython/issues/115911): When the working directory cannot be resolved owing to permissions, the import machinery will from now on avoid raising [`PermissionError`](https://docs.python.org/3.14/library/exceptions.html#PermissionError). Alex Willmer wrote the patch.

[gh-129668](https://github.com/python/cpython/issues/129668): Eliminate a race condition that arose when raising [`MemoryError`](https://docs.python.org/3.14/library/exceptions.html#MemoryError) in the free threaded build.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
