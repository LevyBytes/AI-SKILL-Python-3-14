# thread state C API: `PyUnstable_ThreadState_ResetStackProtection()`, `PyThreadState_GetDict()`, `PyEval_AcquireThread()`, `PyEval_ReleaseThread()`

void PyUnstable_ThreadState_ResetStackProtection(PyThreadState *tstate)

 *This is [Unstable API](https://docs.python.org/3.14/c-api/stable.html#unstable-c-api). It may change without warning in minor releases.*

Restore the stack-protection start address and size for a Python thread state back to whatever the operating system uses by default.

For the rationale, look at `PyUnstable_ThreadState_SetStackProtection()`.

Added in version 3.15.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyThreadState_GetDict()

*Return value: Borrowed reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Hand back a dictionary where extensions are free to keep per-thread state data. Every extension ought to pick a distinct key under which to file its state in that dictionary. Invoking this routine is fine even while no [thread state](https://docs.python.org/3.14/glossary.html#term-thread-state) is [attached](https://docs.python.org/3.14/glossary.html#term-attached-thread-state). A `NULL` result signals that no exception was set, and the caller ought to treat that as meaning no thread state is currently attached.

 void PyEval_AcquireThread(PyThreadState *tstate)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

[Attach](https://docs.python.org/3.14/glossary.html#term-attached-thread-state) *tstate* onto the thread now running; that argument may neither be `NULL` nor already in an attached state.

No [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state) may be held by the thread doing the calling.

Note

Should a thread call this routine while the runtime is in the middle of finalizing, that thread will stall until the program quits — and this holds true even for threads Python itself never spawned. The page [Cautions regarding runtime finalization](https://docs.python.org/3.14/c-api/interp-lifecycle.html#cautions-regarding-runtime-finalization) covers the specifics.

Changed in version 3.8: Brought into line with `PyEval_RestoreThread()`, `Py_END_ALLOW_THREADS()`, and `PyGILState_Ensure()`; it now ends the active thread whenever it is invoked during interpreter finalization.

Changed in version 3.14: When invoked during interpreter finalization, it now stalls the active thread instead of ending it.

A more abstract counterpart, `PyEval_RestoreThread()`, can be used at any time — including before threads have been set up.

 void PyEval_ReleaseThread(PyThreadState *tstate)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Release the [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state). Passing *tstate* (it may not be `NULL`) serves purely as a verification that the value matches the attached thread state; a mismatch triggers a fatal error.

Its higher-level analogue `PyEval_SaveThread()` remains usable in every situation, even prior to thread initialization.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pythreadstate-new-to-pythreadstate-entertracing.md) · [Previous source contract](pyunstable-threadstate-setstackprotection.md) · [Following source contract](py-addpendingcall-to-pythreadstate-setasyncexc.md)
