# Python 3.13.0 alpha 4 / library / trace

[gh-38807](https://github.com/python/cpython/issues/38807): Resolve a race condition inside [`trace`](https://docs.python.org/3.14/library/trace.html#module-trace). Rather than testing whether a directory is present and then creating it, call [`os.makedirs()`](https://docs.python.org/3.14/library/os.html#os.makedirs) outright with the kwarg `exist_ok=True`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
