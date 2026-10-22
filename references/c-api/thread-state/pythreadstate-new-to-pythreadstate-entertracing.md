# thread state C API: `PyThreadState_New()`, `PyThreadState_Clear()`, `PyThreadState_Delete()`, `PyThreadState_DeleteCurrent()`, `PyThreadState_GetFrame()`, `PyThreadState_GetInterpreter()`, `PyThreadState_EnterTracing()`

### Low-level APIs

 PyThreadState *PyThreadState_New([PyInterpreterState](https://docs.python.org/3.14/c-api/subinterpreters.html#c.PyInterpreterState) *interp)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Build a new thread state object that belongs to the given interpreter object. No [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state) is required.

 void PyThreadState_Clear(PyThreadState *tstate)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Clear out every piece of information in a [thread state](https://docs.python.org/3.14/glossary.html#term-thread-state) object. *tstate* must be [attached](https://docs.python.org/3.14/glossary.html#term-attached-thread-state)

Changed in version 3.9: This function now triggers the `PyThreadState.on_delete` callback. Formerly, that took place in `PyThreadState_Delete()`.

Changed in version 3.13: The `PyThreadState.on_delete` callback was removed.

 void PyThreadState_Delete(PyThreadState *tstate)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Destroy a [thread state](https://docs.python.org/3.14/glossary.html#term-thread-state) object. *tstate* should not be [attached](https://docs.python.org/3.14/glossary.html#term-attached-thread-state) to any thread. *tstate* must already have been reset by an earlier `PyThreadState_Clear()` call.

 void PyThreadState_DeleteCurrent(void)

Detach the [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state) (which must already have been reset by an earlier `PyThreadState_Clear()` call) and then destroy it.

On return, no [thread state](https://docs.python.org/3.14/glossary.html#term-thread-state) will be [attached](https://docs.python.org/3.14/glossary.html#term-attached-thread-state).

 [PyFrameObject](https://docs.python.org/3.14/c-api/frame.html#c.PyFrameObject) *PyThreadState_GetFrame(PyThreadState *tstate)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.10.*

Fetch the current frame belonging to the Python thread state *tstate*.

Return a [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference). Return `NULL` when no frame is executing at the moment.

See also [`PyEval_GetFrame()`](https://docs.python.org/3.14/c-api/reflection.html#c.PyEval_GetFrame).

*tstate* must not be `NULL`, and must be [attached](https://docs.python.org/3.14/glossary.html#term-attached-thread-state).

Added in version 3.9.

 uint64_t PyThreadState_GetID(PyThreadState *tstate)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.10.*

Fetch the unique [thread state](https://docs.python.org/3.14/glossary.html#term-thread-state) identifier belonging to the Python thread state *tstate*.

*tstate* must not be `NULL`, and must be [attached](https://docs.python.org/3.14/glossary.html#term-attached-thread-state).

Added in version 3.9.

 [PyInterpreterState](https://docs.python.org/3.14/c-api/subinterpreters.html#c.PyInterpreterState) *PyThreadState_GetInterpreter(PyThreadState *tstate)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.10.*

Fetch the interpreter belonging to the Python thread state *tstate*.

*tstate* must not be `NULL`, and must be [attached](https://docs.python.org/3.14/glossary.html#term-attached-thread-state).

Added in version 3.9.

 void PyThreadState_EnterTracing(PyThreadState *tstate)

Pause tracing and profiling within the Python thread state *tstate*.

Bring them back using the `PyThreadState_LeaveTracing()` function.

Added in version 3.11.

[Subject index](INDEX.md) · [Previous source contract](pygilstate-state-to-pygilstate-check.md) · [Following source contract](pythreadstate-leavetracing.md)
