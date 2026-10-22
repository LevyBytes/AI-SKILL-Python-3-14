# Python 3.14.0 alpha 1 / library / logging

[gh-124653](https://github.com/python/cpython/issues/124653): Corrects how the minimal Queue API required by the [`logging`](https://docs.python.org/3.14/library/logging.html#module-logging) module gets detected. Bénédikt Tran authored the patch.

[gh-105376](https://github.com/python/cpython/issues/105376): Bring back the deprecated [`logging`](https://docs.python.org/3.14/library/logging.html#module-logging) `warn()` method, which had gone away in Python 3.13 alpha 1. Retain the deprecated `warn()` method in Python 3.13. Patch by Victor Stinner.

[gh-118868](https://github.com/python/cpython/issues/118868): Resolve the bug where kwargs had stopped being forwarded to the QueueHandler logging handler

[gh-120683](https://github.com/python/cpython/issues/120683): Repair a defect in [`logging.LogRecord`](https://docs.python.org/3.14/library/logging.html#logging.LogRecord): the timestamp's integer portion was being rounded upward while the millisecond figure was truncated, which threw the recorded time off by as much as 999 ms (about 1 timestamp in every 8 million was hit).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
