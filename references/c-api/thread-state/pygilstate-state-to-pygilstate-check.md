# thread state C API: `PyGILState_STATE`, `PyGILState_Ensure()`, `PyGILState_Release()`, `PyGILState_GetThisThreadState()`, `PyThreadState_Get()`, `PyGILState_Check()`

type PyGILState_STATE

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

The type of the value that `PyGILState_Ensure()` returns and that gets passed into `PyGILState_Release()`.

 enumerator PyGILState_LOCKED

The GIL was being held already at the time `PyGILState_Ensure()` was called.

 enumerator PyGILState_UNLOCKED

The GIL was not being held at the time `PyGILState_Ensure()` was called.

 PyGILState_STATE PyGILState_Ensure()

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Guarantee that the current thread is prepared to call the Python C API no matter the present state of Python or of the [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state). A thread may call this as often as it likes, provided each call is paired with a `PyGILState_Release()` call. As a rule, other thread-related APIs may be used in between `PyGILState_Ensure()` and `PyGILState_Release()` calls, so long as the thread state is brought back to its earlier state ahead of the Release(). For instance, ordinary use of the `Py_BEGIN_ALLOW_THREADS` and `Py_END_ALLOW_THREADS` macros is fine.

What gets returned is an opaque "handle" to the [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state) at the moment `PyGILState_Ensure()` was called, and you must pass it to `PyGILState_Release()` so that Python is left in an identical state. While recursive calls are permitted, these handles *cannot* be shared — every distinct `PyGILState_Ensure()` call must retain its own handle for its matching `PyGILState_Release()`.

After the function returns, an [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state) will exist and the thread will be free to run arbitrary Python code. A failure is a fatal error.

Warning

It's unsafe to call this function while the runtime finalizes. Doing that will either block the thread until the program ends, or, in uncommon cases, crash the interpreter outright. See [Cautions regarding runtime finalization](https://docs.python.org/3.14/c-api/interp-lifecycle.html#cautions-regarding-runtime-finalization) for additional detail.

Changed in version 3.14: Now hangs the current thread instead of terminating it when called as the interpreter finalizes.

 void PyGILState_Release(PyGILState_STATE)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Free whatever resources were acquired earlier. Following this call, Python's state matches what it was before the corresponding `PyGILState_Ensure()` call (though typically the caller won't know that state, which is exactly why the GILState API exists).

On the same thread, each `PyGILState_Ensure()` call has to be paired with a `PyGILState_Release()` call.

 PyThreadState *PyGILState_GetThisThreadState()

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Fetch the [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state) for this thread. It may give back `NULL` when no GILState API has been used on the current thread. Bear in mind that the main thread always carries such a thread-state, even when no auto-thread-state call has occurred on the main thread. This is largely a helper/diagnostic function.

Note

It's possible for this function to give back a non-`NULL` value even while the [thread state](https://docs.python.org/3.14/glossary.html#term-thread-state) is detached. For most situations, favor `PyThreadState_Get()` or `PyThreadState_GetUnchecked()`.

See also

`PyThreadState_Get()`

 int PyGILState_Check()

Return `1` when the current thread is holding the [GIL](https://docs.python.org/3.14/glossary.html#term-GIL), otherwise `0`. Any thread may call this function at any moment. It will return `1` only when that thread has had its [thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state) set up via `PyGILState_Ensure()`. This is largely a helper/diagnostic function. It can prove handy, for example, inside callback contexts or memory allocation functions, where knowing the GIL is locked lets the caller carry out sensitive actions or otherwise act differently.

Note

If at any point the current Python process has created a subinterpreter, this function will *always* return `1`. For most situations, favor `PyThreadState_GetUnchecked()`.

Added in version 3.4.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](gil-state-apis.md) · [Following source contract](pythreadstate-new-to-pythreadstate-entertracing.md)
