# exceptions C API: `PyUnicodeDecodeError_GetReason()`, `PyUnicodeEncodeError_GetReason()`, `PyUnicodeTranslateError_GetReason()`, `PyUnicodeDecodeError_SetReason()`, `PyUnicodeEncodeError_SetReason()`, `PyUnicodeTranslateError_SetReason()`

[PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicodeDecodeError_GetReason([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *exc)

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicodeEncodeError_GetReason([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *exc)

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicodeTranslateError_GetReason([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *exc)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Return the *reason* attribute of the given exception object.

 int PyUnicodeDecodeError_SetReason([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *exc, const char *reason)

 int PyUnicodeEncodeError_SetReason([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *exc, const char *reason)

 int PyUnicodeTranslateError_SetReason([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *exc, const char *reason)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Assign *reason* as the *reason* attribute on the supplied exception object. The call yields `0` when it succeeds and `-1` when it fails.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](unicode-exception-objects.md) · [Previous source contract](pyunicodedecodeerror-create-to-unicodeerror-end.md) · [Following source contract](py-enterrecursivecall-to-sys-setrecursionlimit.md)
