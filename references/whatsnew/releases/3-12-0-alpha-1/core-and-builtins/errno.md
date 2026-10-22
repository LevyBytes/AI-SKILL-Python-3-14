# Python 3.12.0 alpha 1 / core and builtins / errno

[gh-96005](https://github.com/python/cpython/issues/96005): Under WASI, [`ENOTCAPABLE`](https://docs.python.org/3.14/library/errno.html#errno.ENOTCAPABLE) now maps onto [`PermissionError`](https://docs.python.org/3.14/library/exceptions.html#PermissionError). The fresh error number is surfaced by the [`errno`](https://docs.python.org/3.14/library/errno.html#module-errno) modules. `getpath.py` now passes over `PermissionError` whenever it fails to open the landmark files `pybuilddir.txt` and `pyenv.cfg`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
