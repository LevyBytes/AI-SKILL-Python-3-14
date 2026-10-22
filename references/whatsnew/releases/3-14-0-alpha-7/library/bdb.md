# Python 3.14.0 alpha 7 / library / bdb

[gh-120144](https://github.com/python/cpython/issues/120144): Turned off the `CALL` event in [`bdb`](https://docs.python.org/3.14/library/bdb.html#module-bdb) under the `monitoring` backend whenever no new events on the code object are required, which yields better performance.

[gh-120144](https://github.com/python/cpython/issues/120144): Added the optional `sys.monitoring` backend to [`bdb`](https://docs.python.org/3.14/library/bdb.html#module-bdb) and put it to use for [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
