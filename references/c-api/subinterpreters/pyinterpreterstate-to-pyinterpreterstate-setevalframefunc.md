# High-level APIs

### High-level APIs

 type PyInterpreterState

* Part of the [Limited API](https://docs.python.org/3.14/c-api/stable.html#stable) (as an opaque struct).*

What this data structure captures is the state held in common by several threads working in concert. Threads that fall under one interpreter pool their module bookkeeping plus a handful of additional internal items. This structure exposes no public members.

At the outset, threads under separate interpreters hold nothing in common save process-level state — memory on hand, open file descriptors, and the like. The global interpreter lock too is held in common by all threads no matter which interpreter claims them.

Changed in version 3.12: A per-interpreter GIL became feasible with [**PEP 684**](https://peps.python.org/pep-0684/). Consult `Py_NewInterpreterFromConfig()`.

 PyInterpreterState *PyInterpreterState_Get(void)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.9.*

Get the current interpreter.

Raise a fatal error should no [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state) be present. Returning NULL is not possible.

Added in version 3.9.

 int64_t PyInterpreterState_GetID(PyInterpreterState *interp)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.7.*

Hand back the interpreter's distinct ID. Where anything goes wrong while doing so, `-1` comes back and an error gets set.

An [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state) is required on the caller's part.

Added in version 3.7.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyInterpreterState_GetDict(PyInterpreterState *interp)

*Return value: Borrowed reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.8.*

Give back a dictionary suited to holding interpreter-specific data. Should this function give back `NULL`, no exception was raised and the caller ought to treat it as no interpreter-specific dict being on offer.

It does not stand in for [`PyModule_GetState()`](https://docs.python.org/3.14/c-api/module.html#c.PyModule_GetState), the route extensions should take when storing interpreter-specific state information.

This dictionary you get back is borrowed off the interpreter and stays valid right up until the interpreter shuts down.

Added in version 3.8.

 typedef [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *(*_PyFrameEvalFunction)([PyThreadState](https://docs.python.org/3.14/c-api/threads.html#c.PyThreadState) *tstate, [_PyInterpreterFrame](https://docs.python.org/3.14/c-api/frame.html#c._PyInterpreterFrame) *frame, int throwflag)

Type of a frame evaluation function.

Generators' `throw()` method draws on the *throwflag* parameter: when it is non-zero, deal with the current exception.

Changed in version 3.9: A *tstate* parameter is now accepted by the function.

Changed in version 3.11: From `PyFrameObject*` the *frame* parameter switched to `_PyInterpreterFrame*`.

 _PyFrameEvalFunction _PyInterpreterState_GetEvalFrameFunc(PyInterpreterState *interp)

Retrieve the frame evaluation function.

Refer to [**PEP 523**](https://peps.python.org/pep-0523/), “Adding a frame evaluation API to CPython”.

Added in version 3.9.

 void _PyInterpreterState_SetEvalFrameFunc(PyInterpreterState *interp, _PyFrameEvalFunction eval_frame)

Install the frame evaluation function.

Refer to [**PEP 523**](https://peps.python.org/pep-0523/), “Adding a frame evaluation API to CPython”.

Added in version 3.9.

[Subject index](INDEX.md) · [Previous source contract](bugs-and-caveats.md) · [Following source contract](pyinterpreterstate-new-to-pyinterpreterstate-delete.md)
