# Python 3.14.0 alpha 1 / library / multiprocessing

[gh-84559](https://github.com/python/cpython/issues/84559): On Linux and the other POSIX systems, the default [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing) start method has shifted off the frequently unsafe `"fork"` toward `"forkserver"` (where the platform can pass file handles across pipes, as most do) or otherwise `"spawn"`. Nothing changes on Mac and Windows, which already default to `"spawn"`.

[gh-103134](https://github.com/python/cpython/issues/103134): Several extra methods are added to [proxy objects](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing-proxy-objects) within the `multiprocessing` module:

  - `clear()` and `copy()` for proxies of [`list`](https://docs.python.org/3.14/library/stdtypes.html#list)

  - [`fromkeys()`](https://docs.python.org/3.14/library/stdtypes.html#dict.fromkeys), `reversed(d)`, `d | {}`, `{} | d`, `d |= {'b': 2}` for proxies of [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict)

[gh-121313](https://github.com/python/cpython/issues/121313): Cap each read inside the [`multiprocessing.connection.Connection`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.connection.Connection) class at 64 KiB, heading off memory overallocation along with needless memory-management system calls.

[gh-119819](https://github.com/python/cpython/issues/119819): Undo a regression so that logging configuration once again works with multiprocessing queue types.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
