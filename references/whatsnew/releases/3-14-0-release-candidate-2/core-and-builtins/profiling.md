# Python 3.14.0 release candidate 2 / core and builtins / profiling

[gh-137400](https://github.com/python/cpython/issues/137400): Repair a crash within the [free threading](https://docs.python.org/3.14/glossary.html#term-free-threading) build that struck when turning off profiling or tracing on every thread via [`PyEval_SetProfileAllThreads()`](https://docs.python.org/3.14/c-api/profiling.html#c.PyEval_SetProfileAllThreads) or [`PyEval_SetTraceAllThreads()`](https://docs.python.org/3.14/c-api/profiling.html#c.PyEval_SetTraceAllThreads), or via their Python counterparts [`threading.settrace_all_threads()`](https://docs.python.org/3.14/library/threading.html#threading.settrace_all_threads) and [`threading.setprofile_all_threads()`](https://docs.python.org/3.14/library/threading.html#threading.setprofile_all_threads).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
