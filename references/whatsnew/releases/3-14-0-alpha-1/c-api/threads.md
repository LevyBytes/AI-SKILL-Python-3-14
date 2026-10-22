# Python 3.14.0 alpha 1 / c api / threads

[gh-119585](https://github.com/python/cpython/issues/119585): Stop the crash that struck when a thread state spawned by [`PyGILState_Ensure()`](https://docs.python.org/3.14/c-api/threads.html#c.PyGILState_Ensure) ran a destructor during [`PyThreadState_Clear()`](https://docs.python.org/3.14/c-api/threads.html#c.PyThreadState_Clear) that looped back into `PyGILState_Ensure()` and [`PyGILState_Release()`](https://docs.python.org/3.14/c-api/threads.html#c.PyGILState_Release). Such a scenario can arise within the free-threaded build, or whenever thread-local variables have destructors that call `PyGILState_Ensure()`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
