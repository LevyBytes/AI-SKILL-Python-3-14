# Python 3.11 changes: Frame member accessor migration

`f_globals`: use [`PyFrame_GetGlobals()`](https://docs.python.org/3.14/c-api/frame.html#c.PyFrame_GetGlobals).

  - `f_iblock`: removed.

  - `f_lasti`: use [`PyFrame_GetLasti()`](https://docs.python.org/3.14/c-api/frame.html#c.PyFrame_GetLasti). Where code paired `f_lasti` with `PyCode_Addr2Line()`, switch to [`PyFrame_GetLineNumber()`](https://docs.python.org/3.14/c-api/frame.html#c.PyFrame_GetLineNumber), which can be quicker.

  - `f_lineno`: use [`PyFrame_GetLineNumber()`](https://docs.python.org/3.14/c-api/frame.html#c.PyFrame_GetLineNumber)

  - `f_locals`: use [`PyFrame_GetLocals()`](https://docs.python.org/3.14/c-api/frame.html#c.PyFrame_GetLocals).

  - `f_stackdepth`: removed.

  - `f_state`: no public API (renamed to `f_frame.f_state`).

  - `f_trace`: no public API.

  - `f_trace_lines`: use `PyObject_GetAttrString((PyObject*)frame, "f_trace_lines")`.

  - `f_trace_opcodes`: use `PyObject_GetAttrString((PyObject*)frame, "f_trace_opcodes")`.

  - `f_localsplus`: no public API (renamed to `f_frame.localsplus`).

  - `f_valuestack`: removed.

Construction of the Python frame object now happens lazily. One consequence is that you must not read the [`f_back`](https://docs.python.org/3.14/reference/datamodel.html#frame.f_back) member directly any longer, given that its value too is worked out lazily now. Call the [`PyFrame_GetBack()`](https://docs.python.org/3.14/c-api/frame.html#c.PyFrame_GetBack) function in its place.

Any debugger that used to read [`f_locals`](https://docs.python.org/3.14/reference/datamodel.html#frame.f_locals) directly *must* now call [`PyFrame_GetLocals()`](https://docs.python.org/3.14/c-api/frame.html#c.PyFrame_GetLocals) instead. There's no longer any call for `PyFrame_FastToLocalsWithError()` or `PyFrame_LocalsToFast()` — indeed those functions should be left alone. Keeping the frame up to date is now the virtual machine's responsibility.

A definition of `PyFrame_GetCode()` for use on Python 3.8 and earlier:

```python
#if PY_VERSION_HEX < 0x030900B1
static inline PyCodeObject* PyFrame_GetCode(PyFrameObject *frame)
{
    Py_INCREF(frame->f_code);
    return frame->f_code;
}
#endif

```

A definition of `PyFrame_GetBack()` suitable for Python 3.8 and earlier:

```python
#if PY_VERSION_HEX < 0x030900B1
static inline PyFrameObject* PyFrame_GetBack(PyFrameObject *frame)
{
    Py_XINCREF(frame->f_back);
    return frame->f_back;
}
#endif

```

Alternatively, lean on the [pythoncapi_compat project](https://github.com/python/pythoncapi-compat) to obtain these two functions across older Python versions.

- Changes of the [`PyThreadState`](https://docs.python.org/3.14/c-api/threads.html#c.PyThreadState) structure members:

  -

[Subject index](INDEX.md) · [Previous source section](limited-api-header-dependencies.md) · [Next source section](thread-state-frame-access-migration.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](c-api-changes-new-features.md) · [Release/subject declaration](c-api-trashcan-lifecycle-migration.md) · [Preceding release/subject continuation](immutable-heap-types-and-vectorcall.md)
