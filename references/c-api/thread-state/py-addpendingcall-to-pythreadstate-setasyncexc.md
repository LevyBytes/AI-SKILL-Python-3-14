# Asynchronous notifications

### Asynchronous notifications

There exists a facility for delivering asynchronous notifications to the principal interpreter thread. Each such notification is expressed as a function pointer paired with a void pointer that serves as its argument.

 int Py_AddPendingCall(int (*func)(void*), void *arg)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Arrange for a function to run on the main interpreter thread. When this succeeds, the return value is `0` and *func* has been placed in line to execute on the main thread. When it fails, `-1` comes back and no exception is set.

Once queuing succeeds, *func* is destined to run *eventually* on the main interpreter thread, receiving *arg* as its argument. That call happens asynchronously alongside Python code that is executing as usual, yet it always respects the following two guarantees:

- on a [bytecode](https://docs.python.org/3.14/glossary.html#term-bytecode) boundary;

- while the main thread possesses an [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state) (which is why *func* may freely exercise the entire C API).

On success *func* is required to give back `0`, and on failure `-1` together with an exception set. No recursive asynchronous notification will break into *func* while it runs, though a thread switch can still interrupt it whenever the [thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state) becomes detached.

No [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state) is required by this routine. That said, using it inside a subinterpreter does demand that the caller already hold an attached thread state; absent that, *func* risks being queued against the wrong interpreter.

Warning

Being a low-level primitive, this is relevant only in highly unusual scenarios. Nothing promises that *func* runs as soon as possible: while the main thread sits inside a system call, *func* stays pending until that call comes back. For invoking Python code from arbitrary C threads, this routine is generally **not** the right tool — reach for the PyGILState API there instead.

Added in version 3.1.

Changed in version 3.9: Calling this from within a subinterpreter now queues *func* to run on that subinterpreter, no longer on the main interpreter. Every subinterpreter henceforth keeps a separate queue of scheduled calls.

Changed in version 3.12: From now on this routine invariably queues *func* for execution on the main interpreter.

 int Py_MakePendingCalls(void)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Run every call that is still outstanding. Ordinarily the interpreter does this on its own.

A successful run yields `0` from this routine, whereas a failure yields `-1` accompanied by a set exception.

Should the invocation happen anywhere other than the main thread of the main interpreter, the routine simply does nothing and gives back `0`. An [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state) must be held by whoever calls it.

Added in version 3.1.

Changed in version 3.12: Pending calls are now processed by this routine solely within the main interpreter.

 int PyThreadState_SetAsyncExc(unsigned long id, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *exc)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Throw an exception into a thread asynchronously. Here *id* identifies the destination thread by its thread id, while *exc* is the exception object you want raised. The routine takes no reference to *exc*. As a safeguard against careless use, calling it requires you to author your own C extension. It has to run with an [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state). The count of thread states it altered is returned — typically that is one, but it drops to zero when the given thread id cannot be located. Supplying `NULL` for *exc* wipes out the thread's pending exception, if one exists. No exception is ever raised by this call.

Changed in version 3.7: The *id* parameter's type was switched from long over to unsigned long.

[Subject index](INDEX.md) · [Previous source contract](stack-protection-and-thread-lock-apis.md) · [Following source contract](pythread-start-new-thread-to-pythread-init-thread.md)
