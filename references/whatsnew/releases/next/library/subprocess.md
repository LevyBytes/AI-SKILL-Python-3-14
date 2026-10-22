# Python next / library / subprocess

[gh-151403](https://github.com/python/cpython/issues/151403): Resolved a segfault in [`subprocess.Popen`](https://docs.python.org/3.14/library/subprocess.html#subprocess.Popen) (and `_posixsubprocess.fork_exec`) triggered when an `argv` entry’s [`__fspath__()`](https://docs.python.org/3.14/library/os.html#os.PathLike.__fspath__) mutates, in parallel, the `args` sequence that is being converted.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
