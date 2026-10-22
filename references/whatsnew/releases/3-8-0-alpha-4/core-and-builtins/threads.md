# Python 3.8.0 alpha 4 / core and builtins / threads

[bpo-36475](https://bugs.python.org/issue?@action=redirect&bpo=36475): When the interpreter is shutting down, `PyEval_AcquireLock()` and `PyEval_AcquireThread()` will now end the calling thread, bringing their behavior in line with [`PyEval_RestoreThread()`](https://docs.python.org/3.14/c-api/threads.html#c.PyEval_RestoreThread), [`Py_END_ALLOW_THREADS()`](https://docs.python.org/3.14/c-api/threads.html#c.Py_END_ALLOW_THREADS), and [`PyGILState_Ensure()`](https://docs.python.org/3.14/c-api/threads.html#c.PyGILState_Ensure).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
