# Python 3.14.1 final / library / os

[gh-138779](https://github.com/python/cpython/issues/138779): Allows device numbers above `2**63-1` for the [`st_rdev`](https://docs.python.org/3.14/library/os.html#os.stat_result.st_rdev) field within the [`os.stat_result`](https://docs.python.org/3.14/library/os.html#os.stat_result) structure.

[gh-138432](https://github.com/python/cpython/issues/138432): Any [`os.PathLike`](https://docs.python.org/3.14/library/os.html#os.PathLike) objects passed to [`zoneinfo.reset_tzpath()`](https://docs.python.org/3.14/library/zoneinfo.html#zoneinfo.reset_tzpath) are now turned into strings ahead of being added to `TZPATH`. Should anything other than a string remain after that conversion, `TypeError` is raised. When the supplied `os.PathLike` object stands for a relative path, the call now raises `ValueError` rather than `TypeError`, accompanied by a clearer error message.

[bpo-41839](https://bugs.python.org/issue?@action=redirect&bpo=41839): Permit negative priority values returned from the [`os.sched_get_priority_min()`](https://docs.python.org/3.14/library/os.html#os.sched_get_priority_min) plus [`os.sched_get_priority_max()`](https://docs.python.org/3.14/library/os.html#os.sched_get_priority_max) functions.

[gh-120057](https://github.com/python/cpython/issues/120057): [`os.reload_environ()`](https://docs.python.org/3.14/library/os.html#os.reload_environ) is now listed in `os.__all__`.

[gh-137109](https://github.com/python/cpython/issues/137109): The [`os.fork`](https://docs.python.org/3.14/library/os.html#os.fork) API plus the other forking entry points will stop emitting a warning in the usual situation where the Linux or macOS platform APIs report a process thread count of 1, even after a [`os.register_at_fork()`](https://docs.python.org/3.14/library/os.html#os.register_at_fork) `after_in_parent=` callback (re)starts a thread.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
