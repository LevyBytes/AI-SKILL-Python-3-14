# Python 3.13.0 alpha 1 / library / logging

[gh-76913](https://github.com/python/cpython/issues/76913): Introduce a *merge_extra* parameter/feature for [`logging.LoggerAdapter`](https://docs.python.org/3.14/library/logging.html#logging.LoggerAdapter)

[gh-105376](https://github.com/python/cpython/issues/105376): [`logging`](https://docs.python.org/3.14/library/logging.html#module-logging): Took out the undocumented and untested `Logger.warn()` plus `LoggerAdapter.warn()` methods alongside the `logging.warn()` function. Deprecated as far back as Python 3.3, each acted as an alias for the [`logging.Logger.warning()`](https://docs.python.org/3.14/library/logging.html#logging.Logger.warning) method, the `logging.LoggerAdapter.warning()` method, and the [`logging.warning()`](https://docs.python.org/3.14/library/logging.html#logging.warning) function respectively. Victor Stinner authored the change.

[gh-109461](https://github.com/python/cpython/issues/109461): Within [`logging`](https://docs.python.org/3.14/library/logging.html#module-logging): adopt a context manager for acquiring the lock.

[gh-107710](https://github.com/python/cpython/issues/107710): Make [`logging.getHandlerNames()`](https://docs.python.org/3.14/library/logging.html#logging.getHandlerNames) run faster.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
