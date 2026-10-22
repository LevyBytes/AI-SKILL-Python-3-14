# Python 3.12.0 beta 1 / library / functions and types

[gh-94518](https://github.com/python/cpython/issues/94518): Switch the private `_posixsubprocess.fork_exec()` over to Argument Clinic.

[gh-103699](https://github.com/python/cpython/issues/103699): Attach `__orig_bases__` to non-generic TypedDicts, call-based TypedDicts, and call-based NamedTuples. The remaining TypedDicts and NamedTuples carried the attribute already.

[gh-92248](https://github.com/python/cpython/issues/92248): The `type`, `choices`, and `metavar` parameters belonging to `argparse.BooleanOptionalAction` are now deprecated.

[gh-104265](https://github.com/python/cpython/issues/104265): Guard against a potential crash by forbidding instantiation of the `_csv.Reader` and `_csv.Writer` types. The regression came in with 3.10.0a4 via PR 23224 ([bpo-14935](https://bugs.python.org/issue?@action=redirect&bpo=14935)). Radislav Chugunov wrote the patch.

[gh-74690](https://github.com/python/cpython/issues/74690): A runtime-checkable protocol's members are now treated as "frozen" at runtime the moment the class finishes being created. Consult ["What's new in Python 3.12"](https://docs.python.org/3.14/whatsnew/3.12.html#whatsnew-typing-py312) for further specifics.

[gh-103822](https://github.com/python/cpython/issues/103822): Change the return type of `weekday` to use the newly introduced Day attribute

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
