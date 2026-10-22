# Python 3.12 changes: Managed dictionaries, observation APIs and immortal objects

The [`Py_TPFLAGS_MANAGED_DICT`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_MANAGED_DICT) plus [`Py_TPFLAGS_MANAGED_WEAKREF`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_MANAGED_WEAKREF) flags have been introduced. With them, extension classes can back object [`__dict__`](https://docs.python.org/3.14/reference/datamodel.html#object.__dict__) and weakrefs while doing less bookkeeping, consuming less memory, and granting faster access.

- An API for carrying out calls via [the vectorcall protocol](https://docs.python.org/3.14/c-api/call.html#vectorcall) was contributed to the [Limited API](https://docs.python.org/3.14/c-api/stable.html#stable):

  - [`PyObject_Vectorcall()`](https://docs.python.org/3.14/c-api/call.html#c.PyObject_Vectorcall)

  - [`PyObject_VectorcallMethod()`](https://docs.python.org/3.14/c-api/call.html#c.PyObject_VectorcallMethod)

  - [`PY_VECTORCALL_ARGUMENTS_OFFSET`](https://docs.python.org/3.14/c-api/call.html#c.PY_VECTORCALL_ARGUMENTS_OFFSET)

Consequently, the [Limited API](https://docs.python.org/3.14/c-api/stable.html#stable) now exposes both the inbound and outbound sides of the vector call protocol. (Contributed by Wenzel Jakob in [gh-98586](https://github.com/python/cpython/issues/98586).)

- Introduce two fresh public functions, [`PyEval_SetProfileAllThreads()`](https://docs.python.org/3.14/c-api/profiling.html#c.PyEval_SetProfileAllThreads) plus [`PyEval_SetTraceAllThreads()`](https://docs.python.org/3.14/c-api/profiling.html#c.PyEval_SetTraceAllThreads), which let you install tracing and profiling functions across every running thread, not solely the one doing the call. (Contributed by Pablo Galindo in [gh-93503](https://github.com/python/cpython/issues/93503).)

- Introduce a fresh function [`PyFunction_SetVectorcall()`](https://docs.python.org/3.14/c-api/function.html#c.PyFunction_SetVectorcall) into the C API that assigns the vectorcall field belonging to a supplied [`PyFunctionObject`](https://docs.python.org/3.14/c-api/function.html#c.PyFunctionObject). (Contributed by Andrew Frost in [gh-92257](https://github.com/python/cpython/issues/92257).)

- Through [`PyDict_AddWatcher()`](https://docs.python.org/3.14/c-api/dict.html#c.PyDict_AddWatcher), [`PyDict_Watch()`](https://docs.python.org/3.14/c-api/dict.html#c.PyDict_Watch) and the related APIs, the C API now lets you register callbacks fired any time a dictionary gets modified. The intended consumers are optimizing interpreters, JIT compilers, or debuggers. (Contributed by Carl Meyer in [gh-91052](https://github.com/python/cpython/issues/91052).)

- Introduce the [`PyType_AddWatcher()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_AddWatcher) plus [`PyType_Watch()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_Watch) API for registering callbacks that get notified about changes to a type. (Contributed by Carl Meyer in [gh-91051](https://github.com/python/cpython/issues/91051).)

- Introduce the [`PyCode_AddWatcher()`](https://docs.python.org/3.14/c-api/code.html#c.PyCode_AddWatcher) plus [`PyCode_ClearWatcher()`](https://docs.python.org/3.14/c-api/code.html#c.PyCode_ClearWatcher) APIs for registering callbacks that get notified when code objects are created and destroyed. (Contributed by Itamar Oren in [gh-91054](https://github.com/python/cpython/issues/91054).)

- Introduce the [`PyFrame_GetVar()`](https://docs.python.org/3.14/c-api/frame.html#c.PyFrame_GetVar) plus [`PyFrame_GetVarString()`](https://docs.python.org/3.14/c-api/frame.html#c.PyFrame_GetVarString) functions, which fetch a frame variable by way of its name. (Contributed by Victor Stinner in [gh-91248](https://github.com/python/cpython/issues/91248).)

- Introduce [`PyErr_GetRaisedException()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_GetRaisedException) plus [`PyErr_SetRaisedException()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_SetRaisedException) for stashing and restoring the current exception. Each of these returns or accepts one exception object, rather than the three arguments expected by the now-deprecated [`PyErr_Fetch()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Fetch) plus [`PyErr_Restore()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Restore). That is less error prone and somewhat more efficient. (Contributed by Mark Shannon in [gh-101578](https://github.com/python/cpython/issues/101578).)

- Introduce `_PyErr_ChainExceptions1`, taking an exception instance, as a replacement for the legacy-API `_PyErr_ChainExceptions`, which is deprecated from now on. (Contributed by Mark Shannon in [gh-101578](https://github.com/python/cpython/issues/101578).)

- Introduce [`PyException_GetArgs()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyException_GetArgs) plus [`PyException_SetArgs()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyException_SetArgs) as helper functions that read and adjust the [`args`](https://docs.python.org/3.14/library/exceptions.html#BaseException.args) handed to the exception's constructor. (Contributed by Mark Shannon in [gh-101578](https://github.com/python/cpython/issues/101578).)

- Introduce [`PyErr_DisplayException()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_DisplayException), taking an exception instance, as a replacement for the legacy-api `PyErr_Display()`. (Contributed by Irit Katriel in [gh-102755](https://github.com/python/cpython/issues/102755)).

- [**PEP 683**](https://peps.python.org/pep-0683/): Bring in *Immortal Objects*, letting objects sidestep reference counts, plus the related C-API changes:

  - `_Py_IMMORTAL_REFCNT`: The reference count that marks an object as immortal.

  - `_Py_IsImmortal` Tests whether an object holds the immortal reference count.

  - `PyObject_HEAD_INIT` Used together with `Py_BUILD_CORE`, this will now set the reference count to `_Py_IMMORTAL_REFCNT`.

  - `SSTATE_INTERNED_IMMORTAL` An identifier for interned unicode objects that are immortal.

  - `SSTATE_INTERNED_IMMORTAL_STATIC` An identifier for interned unicode objects that are immortal and static

  - `sys.getunicodeinternedsize` This hands back the running total of unicode objects that have been interned. `refleak.py` now relies on this to keep an accurate count of reference counts and allocated blocks

(Contributed by Eddie Elizondo in [gh-84436](https://github.com/python/cpython/issues/84436).)

[Subject index](INDEX.md) · [Previous source section](c-api-changes-new-features.md) · [Next source section](opaque-reference-counting-calls.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](c-api-changes-new-features.md)
