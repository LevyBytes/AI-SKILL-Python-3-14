# thread state C API: `PyThreadState`, `PyEval_InitThreads()`, `PyEval_SaveThread()`, `PyEval_RestoreThread()`, `PyThreadState_Get()`, `PyThreadState_GetUnchecked()`, `PyThreadState_Swap()`, `PyEval_ReleaseThread()`

type PyThreadState

* Part of the [Limited API](https://docs.python.org/3.14/c-api/stable.html#stable) (as an opaque struct).*

A single thread's state is what this data structure stands for. Its one public data member is:

 [PyInterpreterState](https://docs.python.org/3.14/c-api/subinterpreters.html#c.PyInterpreterState) *interp

This thread's interpreter state.

 void PyEval_InitThreads()

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

A deprecated function that has no effect.

Under Python 3.6 and earlier, this function set up the GIL when it didn't already exist.

Changed in version 3.9: The function now does nothing.

Changed in version 3.7: [`Py_Initialize()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_Initialize) now invokes this function, so calling it yourself is no longer needed.

Changed in version 3.2: Calling this function ahead of [`Py_Initialize()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_Initialize) is no longer permitted.

Deprecated since version 3.9.

 PyThreadState *PyEval_SaveThread()

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Detach the [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state) and hand it back. On return, the thread will hold no [thread state](https://docs.python.org/3.14/glossary.html#term-thread-state).

 void PyEval_RestoreThread(PyThreadState *tstate)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Set the [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state) to *tstate*. The [thread state](https://docs.python.org/3.14/glossary.html#term-thread-state) you supply **should not** already be attached, or a deadlock results. On return, *tstate* will be attached.

Note

Invoking this function from a thread while the runtime finalizes will block that thread until the program exits, even when Python did not create the thread. See [Cautions regarding runtime finalization](https://docs.python.org/3.14/c-api/interp-lifecycle.html#cautions-regarding-runtime-finalization) for additional detail.

Changed in version 3.14: Now hangs the current thread instead of terminating it when called as the interpreter finalizes.

 PyThreadState *PyThreadState_Get()

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Return the [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state). When the thread holds no attached thread state (for example, while inside a `Py_BEGIN_ALLOW_THREADS` block), this raises a fatal error (sparing the caller from having to check for `NULL`).

See also `PyThreadState_GetUnchecked()`.

 PyThreadState *PyThreadState_GetUnchecked()

Like `PyThreadState_Get()`, except it won't take down the process with a fatal error when the result is NULL. Checking whether the result is NULL falls to the caller.

Added in version 3.13: Across Python 3.5 through 3.12, this function existed privately under the name `_PyThreadState_UncheckedGet()`.

 PyThreadState *PyThreadState_Swap(PyThreadState *tstate)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Set the [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state) to *tstate*, and give back whichever [thread state](https://docs.python.org/3.14/glossary.html#term-thread-state) had been attached before the call.

You may safely call this function with no [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state); under that condition it merely returns `NULL` to signal there was no prior thread state.

See also

`PyEval_ReleaseThread()`

Note

As with `PyGILState_Ensure()`, this function will hang the thread should the runtime be finalizing.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](high-level-apis.md) · [Following source contract](gil-state-apis.md)
