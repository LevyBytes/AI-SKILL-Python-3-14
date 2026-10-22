# Thread State and GIL APIs

### Thread State and GIL APIs

A collection of functions and macros ships with Python for handling thread state together with the GIL, including:

- [`PyGILState_Ensure()`](https://docs.python.org/3.14/c-api/threads.html#c.PyGILState_Ensure) and [`PyGILState_Release()`](https://docs.python.org/3.14/c-api/threads.html#c.PyGILState_Release)

- [`PyEval_SaveThread()`](https://docs.python.org/3.14/c-api/threads.html#c.PyEval_SaveThread) and [`PyEval_RestoreThread()`](https://docs.python.org/3.14/c-api/threads.html#c.PyEval_RestoreThread)

- [`Py_BEGIN_ALLOW_THREADS`](https://docs.python.org/3.14/c-api/threads.html#c.Py_BEGIN_ALLOW_THREADS) and [`Py_END_ALLOW_THREADS`](https://docs.python.org/3.14/c-api/threads.html#c.Py_END_ALLOW_THREADS)

Even with the [GIL](https://docs.python.org/3.14/glossary.html#term-GIL) switched off, you ought to keep calling these in the free-threaded build to look after thread state. Say you spin up a thread somewhere outside of Python: you then have to invoke [`PyGILState_Ensure()`](https://docs.python.org/3.14/c-api/threads.html#c.PyGILState_Ensure) before that thread touches the Python API, guaranteeing it carries a valid Python thread state.

Keep wrapping any blocking work — I/O or grabbing a lock, for instance — inside [`PyEval_SaveThread()`](https://docs.python.org/3.14/c-api/threads.html#c.PyEval_SaveThread) or [`Py_BEGIN_ALLOW_THREADS`](https://docs.python.org/3.14/c-api/threads.html#c.Py_BEGIN_ALLOW_THREADS), which frees up other threads to drive the [cyclic garbage collector](https://docs.python.org/3.14/glossary.html#term-garbage-collection).

[Subject index](INDEX.md) · [Previous source context](memory-allocation-apis.md) · [Following source context](protecting-internal-extension-state.md)
