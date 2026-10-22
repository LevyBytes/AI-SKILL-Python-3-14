# Python 3.14.0 beta 4 / core and builtins / exceptions and tracebacks

[gh-78465](https://github.com/python/cpython/issues/78465): The error message for `cls.__new__(cls, ...)` was fixed for when `cls` is a builtin or extension type that cannot be instantiated (its `tp_new` being set to `NULL`).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
