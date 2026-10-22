# Python 3.14.0 alpha 2 / library / os

[gh-125413](https://github.com/python/cpython/issues/125413): Introduce a `pathlib.Path.scandir()` method that efficiently retrieves a directory's children alongside their file attributes. It amounts to a thin wrapper over [`os.scandir()`](https://docs.python.org/3.14/library/os.html#os.scandir).

[gh-126303](https://github.com/python/cpython/issues/126303): Repair pickling along with copying for [`os.sched_param`](https://docs.python.org/3.14/library/os.html#os.sched_param) objects.

[gh-120057](https://github.com/python/cpython/issues/120057): Swap out the `os.environ.refresh()` method for a fresh [`os.reload_environ()`](https://docs.python.org/3.14/library/os.html#os.reload_environ) function. Victor Stinner provided the patch.

[gh-126705](https://github.com/python/cpython/issues/126705): Permit [`os.PathLike`](https://docs.python.org/3.14/library/os.html#os.PathLike) to serve as a base for Protocols.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
