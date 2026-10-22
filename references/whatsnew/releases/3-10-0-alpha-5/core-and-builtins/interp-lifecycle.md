# Python 3.10.0 alpha 5 / core and builtins / interp lifecycle

[bpo-42882](https://bugs.python.org/issue?@action=redirect&bpo=42882): Correct the `_PyUnicode_FromId()` function (the _Py_IDENTIFIER(var) API) for the case where [`Py_Initialize()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_Initialize) / [`Py_Finalize()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_Finalize) runs more than once: hang onto the `_PyRuntime.unicode_ids.next_index` value.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
