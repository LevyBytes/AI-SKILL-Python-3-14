# Python 3.14.2 final / library / multiprocessing

[gh-142206](https://github.com/python/cpython/issues/142206): By default, the resource tracker inside the [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing) module reverts to the original communication protocol, the one used in Python 3.14.0 and earlier. This avoids problems when Python is upgraded while it remains running. (Bear in mind that such "in-place" upgrades are not tested.) Compatibility with subprocesses that adopt the new protocol is retained (meaning subprocesses on Python 3.13.10, 3.14.1 and 3.15).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
