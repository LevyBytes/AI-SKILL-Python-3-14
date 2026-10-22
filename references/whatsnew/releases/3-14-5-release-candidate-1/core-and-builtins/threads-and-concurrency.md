# Python 3.14.5 release candidate 1 / core and builtins / threads and concurrency

[gh-148820](https://github.com/python/cpython/issues/148820): Close a race within `_PyRawMutex` on the free-threaded build: a `Py_PARK_INTR` result coming back from `_PySemaphore_Wait` allowed the waiter to tear down its semaphore ahead of the unlocking thread's `_PySemaphore_Wakeup` finishing, which triggered a fatal `ReleaseSemaphore` error.

[gh-148037](https://github.com/python/cpython/issues/148037): Drop the critical section around `PyCode_Addr2Line()` under free-threading.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
