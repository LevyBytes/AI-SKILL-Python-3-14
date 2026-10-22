# Python 3.13.0 alpha 3 / core and builtins / functions and types

[gh-112217](https://github.com/python/cpython/issues/112217): Add a check on the type of `__cause__` that comes back from calling the type `T` within `raise from T`.

[bpo-21861](https://bugs.python.org/issue?@action=redirect&bpo=21861): Use the actual class name of the object inside `_io.FileIO.__repr__()`, `_io._WindowsConsoleIO()` and `_io.TextIOWrapper.__repr__()`, rendering these methods friendlier toward subclasses.

[gh-113486](https://github.com/python/cpython/issues/113486): Stop emitting bogus `PY_UNWIND` events for optimized class calls.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
