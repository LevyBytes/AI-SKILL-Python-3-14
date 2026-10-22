# Python 3.14.6 final / core and builtins / os

[gh-149156](https://github.com/python/cpython/issues/149156): Repair an occasional segfault following [`os.fork()`](https://docs.python.org/3.14/library/os.html#os.fork) while perf trampoline profiling is on and the child unwinds via trampoline frames it inherited from its parent process.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
