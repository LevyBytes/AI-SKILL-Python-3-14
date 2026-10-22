# Python 3.14.0 beta 1 / library / sys monitoring

[gh-132536](https://github.com/python/cpython/issues/132536): Refrain from turning off the [`PY_THROW`](https://docs.python.org/3.14/library/sys.monitoring.html#monitoring-event-PY_THROW) event inside [`bdb`](https://docs.python.org/3.14/library/bdb.html#module-bdb), since disabling it is not possible.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
