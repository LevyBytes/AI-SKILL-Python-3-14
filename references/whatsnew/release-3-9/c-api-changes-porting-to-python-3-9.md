# What's New In Python 3.9 / C API Changes / Porting to Python 3.9 - sys

### Porting to Python 3.9

- `PyInterpreterState.eval_frame` ([**PEP 523**](https://peps.python.org/pep-0523/)) has gained a fresh, compulsory *tstate* parameter of type `PyThreadState*`. (Contributed by Victor Stinner in [bpo-38500](https://bugs.python.org/issue?@action=redirect&bpo=38500).)

- Extension modules: the [`m_traverse`](https://docs.python.org/3.14/c-api/module.html#c.PyModuleDef.m_traverse), [`m_clear`](https://docs.python.org/3.14/c-api/module.html#c.PyModuleDef.m_clear) and [`m_free`](https://docs.python.org/3.14/c-api/module.html#c.PyModuleDef.m_free) functions on [`PyModuleDef`](https://docs.python.org/3.14/c-api/module.html#c.PyModuleDef) stop being invoked once the module state has been asked for but not yet allocated. That situation arises right after a module gets created and ahead of it running (the [`Py_mod_exec`](https://docs.python.org/3.14/c-api/module.html#c.Py_mod_exec) function). To be exact, those functions go uncalled when [`m_size`](https://docs.python.org/3.14/c-api/module.html#c.PyModuleDef.m_size) exceeds 0 while the module state — what [`PyModule_GetState()`](https://docs.python.org/3.14/c-api/module.html#c.PyModule_GetState) returns — is `NULL`.

Modules carrying no module state (`m_size <= 0`) feel none of this.

- Should [`Py_AddPendingCall()`](https://docs.python.org/3.14/c-api/threads.html#c.Py_AddPendingCall) be invoked within a subinterpreter, it now gets queued to run from that subinterpreter rather than from the main one. Every subinterpreter keeps a scheduled-call list all its own these days. (Contributed by Victor Stinner in [bpo-39984](https://bugs.python.org/issue?@action=redirect&bpo=39984).)

- With the `-E` option active — that is, when [`PyConfig.use_environment`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.use_environment) equals `0` — the Windows registry no longer feeds the initialization of [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path). That matters whenever you embed Python on Windows. (Contributed by Zackery Spytz in [bpo-8901](https://bugs.python.org/issue?@action=redirect&bpo=8901).)

- These days the global variable [`PyStructSequence_UnnamedField`](https://docs.python.org/3.14/c-api/tuple.html#c.PyStructSequence_UnnamedField) is a constant pointing at a constant string. (Contributed by Serhiy Storchaka in [bpo-38650](https://bugs.python.org/issue?@action=redirect&bpo=38650).)

- The `PyGC_Head` structure has gone opaque; its definition lives solely in the internal C API (`pycore_gc.h`). (Contributed by Victor Stinner in [bpo-40241](https://bugs.python.org/issue?@action=redirect&bpo=40241).)

- The `Py_UNICODE_COPY`, `Py_UNICODE_FILL`, `PyUnicode_WSTR_LENGTH`, `PyUnicode_FromUnicode()`, `PyUnicode_AsUnicode()`, `_PyUnicode_AsUnicode`, and `PyUnicode_AsUnicodeAndSize()` now carry a deprecation flag in C. Their deprecation traces back to [**PEP 393**](https://peps.python.org/pep-0393/), in effect ever since Python 3.3. (Contributed by Inada Naoki in [bpo-36346](https://bugs.python.org/issue?@action=redirect&bpo=36346).)

- A macro now stands in for the [`Py_FatalError()`](https://docs.python.org/3.14/c-api/sys.html#c.Py_FatalError) function, and it records the current function’s name on its own — except where the `Py_LIMITED_API` macro is defined. (Contributed by Victor Stinner in [bpo-39882](https://bugs.python.org/issue?@action=redirect&bpo=39882).)

- Under the vectorcall protocol, callers must from now on supply nothing but strings for the keyword names. (See [bpo-37540](https://bugs.python.org/issue?@action=redirect&bpo=37540) for more information.)

- For several macros and functions, the implementation details are now tucked away:

  - [`PyObject_IS_GC()`](https://docs.python.org/3.14/c-api/gcsupport.html#c.PyObject_IS_GC) macro was converted to a function.

  - The `PyObject_NEW()` macro turns into an alias for the [`PyObject_New`](https://docs.python.org/3.14/c-api/allocation.html#c.PyObject_New) macro, while `PyObject_NEW_VAR()` turns into an alias for the [`PyObject_NewVar`](https://docs.python.org/3.14/c-api/allocation.html#c.PyObject_NewVar) macro. Neither reaches into the [`PyTypeObject.tp_basicsize`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_basicsize) member directly any longer.

  - `PyObject_GET_WEAKREFS_LISTPTR()` shifted from a macro to a function, the old macro having reached straight into the [`PyTypeObject.tp_weaklistoffset`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_weaklistoffset) member.

  - [`PyObject_CheckBuffer()`](https://docs.python.org/3.14/c-api/buffer.html#c.PyObject_CheckBuffer) shifted from a macro to a function, the old macro having reached straight into the [`PyTypeObject.tp_as_buffer`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_as_buffer) member.

  - [`PyIndex_Check()`](https://docs.python.org/3.14/c-api/number.html#c.PyIndex_Check) is from now on invariably an opaque function that keeps implementation details hidden, the `PyIndex_Check()` macro having been dropped. That macro used to reach straight into the [`PyTypeObject.tp_as_number`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_as_number) member.

(See [bpo-40170](https://bugs.python.org/issue?@action=redirect&bpo=40170) for more details.)

[Subject index](INDEX.md) · [Previous source section](c-api-changes-new-features.md) · [Next source section](c-api-changes-removed.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](c-api-changes-new-features.md)
