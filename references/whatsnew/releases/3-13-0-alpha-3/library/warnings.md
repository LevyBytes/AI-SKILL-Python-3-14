# Python 3.13.0 alpha 3 / library / warnings

[bpo-39912](https://bugs.python.org/issue?@action=redirect&bpo=39912): In place of `AssertionError`, [`warnings.filterwarnings()`](https://docs.python.org/3.14/library/warnings.html#warnings.filterwarnings) and [`warnings.simplefilter()`](https://docs.python.org/3.14/library/warnings.html#warnings.simplefilter) now raise the appropriate exceptions. Rémi Lapeyre contributed the patch.

[gh-113781](https://github.com/python/cpython/issues/113781): Quiet the unraisable AttributeError raised when warnings fire during Python finalization.

[gh-104003](https://github.com/python/cpython/issues/104003): Introduce [`warnings.deprecated()`](https://docs.python.org/3.14/library/warnings.html#warnings.deprecated), a decorator that flags deprecated functions for static type checkers and emits a warning when deprecated classes and functions are used. Refer to [**PEP 702**](https://peps.python.org/pep-0702/). Jelle Zijlstra wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
