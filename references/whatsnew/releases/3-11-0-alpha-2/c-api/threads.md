# Python 3.11.0 alpha 2 / c api / threads

[bpo-43760](https://bugs.python.org/issue?@action=redirect&bpo=43760): Introduce the new [`PyThreadState_EnterTracing()`](https://docs.python.org/3.14/c-api/threads.html#c.PyThreadState_EnterTracing) and [`PyThreadState_LeaveTracing()`](https://docs.python.org/3.14/c-api/threads.html#c.PyThreadState_LeaveTracing) functions within the limited C API to pause and restart tracing and profiling. Victor Stinner contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
