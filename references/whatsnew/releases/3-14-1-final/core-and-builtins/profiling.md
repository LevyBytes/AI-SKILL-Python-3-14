# Python 3.14.1 final / core and builtins / profiling

[gh-137400](https://github.com/python/cpython/issues/137400): Resolve a crash within the [free threading](https://docs.python.org/3.14/glossary.html#term-free-threading) build whenever profiling or tracing gets switched off over every thread via [`PyEval_SetProfileAllThreads()`](https://docs.python.org/3.14/c-api/profiling.html#c.PyEval_SetProfileAllThreads) or [`PyEval_SetTraceAllThreads()`](https://docs.python.org/3.14/c-api/profiling.html#c.PyEval_SetTraceAllThreads), or their Python counterparts [`threading.settrace_all_threads()`](https://docs.python.org/3.14/library/threading.html#threading.settrace_all_threads) plus [`threading.setprofile_all_threads()`](https://docs.python.org/3.14/library/threading.html#threading.setprofile_all_threads).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
