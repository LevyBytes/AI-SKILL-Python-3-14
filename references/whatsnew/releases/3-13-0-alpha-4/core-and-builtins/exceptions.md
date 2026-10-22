# Python 3.13.0 alpha 4 / core and builtins / exceptions

[gh-114570](https://github.com/python/cpython/issues/114570): Introduce the [`PythonFinalizationError`](https://docs.python.org/3.14/library/exceptions.html#PythonFinalizationError) exception. Derived from [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError), it is raised whenever an operation is blocked during [Python finalization](https://docs.python.org/3.14/glossary.html#term-interpreter-shutdown). Victor Stinner contributed the patch.

[gh-114388](https://github.com/python/cpython/issues/114388): Repair a [`RuntimeWarning`](https://docs.python.org/3.14/library/exceptions.html#RuntimeWarning) that fired when an integer-like value that is not itself an [`int`](https://docs.python.org/3.14/library/functions.html#int) instance was assigned to an attribute mapping to a C struct member of [type](https://docs.python.org/3.14/c-api/structures.html#pymemberdef-types) T_UINT and T_ULONG. Also repair the duplicate `RuntimeWarning` that fired when a negative integer was assigned to an attribute mapping to a C struct member of type T_UINT.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
