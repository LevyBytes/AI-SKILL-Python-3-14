# void PyThreadState_LeaveTracing(PyThreadState *tstate)

void PyThreadState_LeaveTracing(PyThreadState *tstate)

Bring back tracing and profiling within the Python thread state *tstate* that the `PyThreadState_EnterTracing()` function had paused.
Refer additionally to the [`PyEval_SetTrace()`](https://docs.python.org/3.14/c-api/profiling.html#c.PyEval_SetTrace) and [`PyEval_SetProfile()`](https://docs.python.org/3.14/c-api/profiling.html#c.PyEval_SetProfile) routines.

Added in version 3.11.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pythreadstate-new-to-pythreadstate-entertracing.md) · [Previous source contract](pyunstable-threadstate-setstackprotection.md)
