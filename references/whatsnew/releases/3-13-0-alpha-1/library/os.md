# Python 3.13.0 alpha 1 / library / os

[gh-104898](https://github.com/python/cpython/issues/104898): Supplied the missing [`__slots__`](https://docs.python.org/3.14/reference/datamodel.html#object.__slots__) on [`os.PathLike`](https://docs.python.org/3.14/library/os.html#os.PathLike).

[gh-106046](https://github.com/python/cpython/issues/106046): Sharpen the error message coming from [`os.fspath()`](https://docs.python.org/3.14/library/os.html#os.fspath) when it is handed an object whose `__fspath__` equals `None`. Alex Waygood provided the patch.

[gh-109649](https://github.com/python/cpython/issues/109649): Provide an [`os.process_cpu_count()`](https://docs.python.org/3.14/library/os.html#os.process_cpu_count) function returning the number of logical CPUs that the calling thread of the current process is permitted to use. Victor Stinner contributed the patch.

[gh-109613](https://github.com/python/cpython/issues/109613): Repaired [`os.stat()`](https://docs.python.org/3.14/library/os.html#os.stat) along with [`os.DirEntry.stat()`](https://docs.python.org/3.14/library/os.html#os.DirEntry.stat) to check for exceptions. Formerly, on a Python built in debug mode, these routines could provoke a fatal Python error (aborting the process) whenever a function returned success while leaving an exception set. Victor Stinner authored the patch.

[gh-108277](https://github.com/python/cpython/issues/108277): Provide [`os.timerfd_create()`](https://docs.python.org/3.14/library/os.html#os.timerfd_create), [`os.timerfd_settime()`](https://docs.python.org/3.14/library/os.html#os.timerfd_settime), [`os.timerfd_gettime()`](https://docs.python.org/3.14/library/os.html#os.timerfd_gettime), [`os.timerfd_settime_ns()`](https://docs.python.org/3.14/library/os.html#os.timerfd_settime_ns), and [`os.timerfd_gettime_ns()`](https://docs.python.org/3.14/library/os.html#os.timerfd_gettime_ns) as a low level interface onto Linux’s timer notification file descriptor.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
