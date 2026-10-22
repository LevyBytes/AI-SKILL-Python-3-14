# Python 3.13.0 alpha 1 / core and builtins / multiprocessing

[gh-77377](https://github.com/python/cpython/issues/77377): Guarantee that multiprocessing synchronization objects built within a fork context never travel to a separate process spawned under a spawn context. The result converts a segfault into a workable RuntimeError raised inside the parent process.

[gh-106723](https://github.com/python/cpython/issues/106723): Carry `frozen_modules` across to multiprocessing's spawned-process interpreters.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
