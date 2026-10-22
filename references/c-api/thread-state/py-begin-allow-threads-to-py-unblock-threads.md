# APIs

### APIs

It's customary to write the macros below without a trailing semicolon; consult the Python source distribution for examples of their use.

Note

Even on the [free-threaded build](https://docs.python.org/3.14/glossary.html#term-free-threaded-build), these macros remain necessary in order to avoid deadlocks.

 Py_BEGIN_ALLOW_THREADS

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

This macro expands into `{ PyThreadState *_save; _save = PyEval_SaveThread();`. Observe that it includes an opening brace; a subsequent `Py_END_ALLOW_THREADS` macro has to pair with it. Refer above for more on this macro.

 Py_END_ALLOW_THREADS

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

This macro expands into `PyEval_RestoreThread(_save); }`. Observe that it includes a closing brace; a preceding `Py_BEGIN_ALLOW_THREADS` macro has to pair with it. Refer above for more on this macro.

 Py_BLOCK_THREADS

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

This macro expands into `PyEval_RestoreThread(_save);`: it amounts to `Py_END_ALLOW_THREADS` minus the closing brace.

 Py_UNBLOCK_THREADS

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

This macro expands into `_save = PyEval_SaveThread();`: it amounts to `Py_BEGIN_ALLOW_THREADS` minus the opening brace and the variable declaration.

[Subject index](INDEX.md) · [Previous source contract](detaching-the-thread-state-from-extension-code.md) · [Following source contract](non-python-created-threads.md)
