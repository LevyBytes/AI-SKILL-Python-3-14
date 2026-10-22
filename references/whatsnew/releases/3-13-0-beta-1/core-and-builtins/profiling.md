# Python 3.13.0 beta 1 / core and builtins / profiling

[gh-93502](https://github.com/python/cpython/issues/93502): Two fresh C-API functions appear, [`PyRefTracer_SetTracer()`](https://docs.python.org/3.14/c-api/profiling.html#c.PyRefTracer_SetTracer) and [`PyRefTracer_GetTracer()`](https://docs.python.org/3.14/c-api/profiling.html#c.PyRefTracer_GetTracer), which let you follow object creation and destruction in the same fashion as the [`tracemalloc`](https://docs.python.org/3.14/library/tracemalloc.html#module-tracemalloc) module. Pablo Galindo wrote the patch

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
