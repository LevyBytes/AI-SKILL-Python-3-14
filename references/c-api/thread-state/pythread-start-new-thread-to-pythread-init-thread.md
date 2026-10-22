# thread state C API: `PyThread_start_new_thread()`, `PyThread_get_thread_ident()`, `threading.get_ident()`, `PyThread_GetInfo()`, `PyThread_get_thread_native_id()`, `threading.get_native_id()`, `PyThread_exit_thread()`, `PyThread_init_thread()`

### Operating system thread APIs

 PYTHREAD_INVALID_THREAD_ID

A marker standing in for a thread ID that is not valid.

At present its value matches `(unsigned long)-1`.

 unsigned long PyThread_start_new_thread(void (*func)(void*), void *arg)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Launch *func* on a freshly created thread, passing it *arg*. The thread that results is not meant to be joined later.

Whereas *func* is forbidden from being `NULL`, *arg* is permitted to be `NULL`.

Upon succeeding, the call hands back the new thread's identifier; upon failing, it hands back `PYTHREAD_INVALID_THREAD_ID`.

Holding an [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state) is not a prerequisite for the caller.

 unsigned long PyThread_get_thread_ident(void)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Give back the identifier belonging to the running thread; this value is guaranteed to be nonzero.

Failure is impossible for this routine, and the caller is under no obligation to hold an [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state).

See also

[`threading.get_ident()`](https://docs.python.org/3.14/library/threading.html#threading.get_ident)

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyThread_GetInfo(void)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.3.*

Obtain a broad set of facts about the running thread, packaged as a [struct sequence](https://docs.python.org/3.14/c-api/tuple.html#struct-sequence-objects) object. From Python, the same data shows up under [`sys.thread_info`](https://docs.python.org/3.14/library/sys.html#sys.thread_info).

When it succeeds, a fresh [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) to that thread information comes back; when it fails, the result is `NULL` and an exception is set.

An [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state) is mandatory for whoever calls this.

 PY_HAVE_THREAD_NATIVE_ID

Whenever native thread IDs are supported by the platform, this macro gets defined.

 unsigned long PyThread_get_thread_native_id(void)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) on platforms with native thread IDs.*

Fetch the running thread's native identifier, the one handed out by the operating system's kernel; its value is never below zero.

Only when `PY_HAVE_THREAD_NATIVE_ID` has been defined does this routine exist.

This routine cannot fail, and there is no requirement that the caller hold an [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state).

See also

[`threading.get_native_id()`](https://docs.python.org/3.14/library/threading.html#threading.get_native_id)

 void PyThread_exit_thread(void)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

End the running thread. Most developers regard this routine as unsafe and best left alone; it survives purely for backwards compatibility.

Calling it is safe only when every function across the entire call stack has been written to permit it.

Warning

On a platform built around POSIX threads (the “pthreads” model), the routine dispatches to *[pthread_exit(3)](https://manpages.debian.org/pthread_exit(3))*, which on certain libc implementations tries to unwind the stack and fire C++ destructors. That said, reaching a `noexcept` function may instead bring the whole process down. Platforms like macOS perform the unwinding as well.

Under Windows, the routine invokes `_endthreadex()`, terminating the thread while skipping any C++ destructors.

Regardless of the path taken, the thread's stack is exposed to a corruption hazard.

Deprecated since version 3.14.

 void PyThread_init_thread(void)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Set up the `PyThread*` APIs. Since Python runs this routine on its own, an extension module rarely has any reason to call it.

[Subject index](INDEX.md) · [Previous source contract](py-addpendingcall-to-pythreadstate-setasyncexc.md) · [Following source contract](pythread-set-stacksize-to-pythread-get-stacksize.md)
