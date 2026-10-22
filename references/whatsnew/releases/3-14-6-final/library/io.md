# Python 3.14.6 final / library / io

[gh-143008](https://github.com/python/cpython/issues/143008): Repair race conditions occurring while a [`io.TextIOWrapper`](https://docs.python.org/3.14/library/io.html#io.TextIOWrapper) object is being re-initialized.

[gh-149046](https://github.com/python/cpython/issues/149046): [`io`](https://docs.python.org/3.14/library/io.html#module-io): Repair [`io.StringIO`](https://docs.python.org/3.14/library/io.html#io.StringIO) serialization: `str(obj)` is no longer invoked on [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) subclasses. Thomas Kowalski authored the change.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
