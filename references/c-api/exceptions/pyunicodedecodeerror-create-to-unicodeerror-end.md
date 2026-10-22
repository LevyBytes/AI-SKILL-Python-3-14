# exceptions C API: Unicode exception creation, encoding and range fields

[PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicodeDecodeError_Create(const char *encoding, const char *object, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) length, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) start, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) end, const char *reason)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Build a [`UnicodeDecodeError`](https://docs.python.org/3.14/library/exceptions.html#UnicodeDecodeError) instance whose attributes are populated from *encoding*, *object*, *length*, *start*, *end* and *reason*. Supply both *encoding* and *reason* as UTF-8 encoded strings.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicodeDecodeError_GetEncoding([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *exc)

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicodeEncodeError_GetEncoding([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *exc)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Return the *encoding* attribute of the given exception object.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicodeDecodeError_GetObject([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *exc)

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicodeEncodeError_GetObject([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *exc)

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicodeTranslateError_GetObject([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *exc)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Return the *object* attribute of the given exception object.

 int PyUnicodeDecodeError_GetStart([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *exc, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) *start)

 int PyUnicodeEncodeError_GetStart([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *exc, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) *start)

 int PyUnicodeTranslateError_GetStart([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *exc, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) *start)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Read the *start* attribute from the supplied exception object and store it through **start*. Note that *start* must not be `NULL`. The call yields `0` when it succeeds and `-1` when it fails.

When the [`UnicodeError.object`](https://docs.python.org/3.14/library/exceptions.html#UnicodeError.object) holds an empty sequence, the *start* value comes out as `0`; in every other case it is clamped to the range `[0, len(object) - 1]`.

See also

[`UnicodeError.start`](https://docs.python.org/3.14/library/exceptions.html#UnicodeError.start)

 int PyUnicodeDecodeError_SetStart([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *exc, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) start)

 int PyUnicodeEncodeError_SetStart([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *exc, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) start)

 int PyUnicodeTranslateError_SetStart([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *exc, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) start)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Assign *start* as the *start* attribute on the supplied exception object. The call yields `0` when it succeeds and `-1` when it fails.

Note

A negative *start* is accepted silently and raises nothing, yet the matching getters won't treat such a value as an offset measured from the end.

 int PyUnicodeDecodeError_GetEnd([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *exc, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) *end)

 int PyUnicodeEncodeError_GetEnd([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *exc, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) *end)

 int PyUnicodeTranslateError_GetEnd([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *exc, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) *end)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Read the *end* attribute from the supplied exception object and store it through **end*. Note that *end* must not be `NULL`. The call yields `0` when it succeeds and `-1` when it fails.

When the [`UnicodeError.object`](https://docs.python.org/3.14/library/exceptions.html#UnicodeError.object) holds an empty sequence, the *end* value comes out as `0`; in every other case it is clamped to the range `[1, len(object)]`.

 int PyUnicodeDecodeError_SetEnd([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *exc, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) end)

 int PyUnicodeEncodeError_SetEnd([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *exc, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) end)

 int PyUnicodeTranslateError_SetEnd([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *exc, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) end)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Assign *end* as the *end* attribute on the supplied exception object. The call yields `0` when it succeeds and `-1` when it fails.

See also

[`UnicodeError.end`](https://docs.python.org/3.14/library/exceptions.html#UnicodeError.end)

[Subject index](INDEX.md) · [Owning C API section and shared conditions](unicode-exception-objects.md) · [Following source contract](unicode-exception-reason-accessors.md)
