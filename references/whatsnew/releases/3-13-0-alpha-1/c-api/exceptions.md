# Python 3.13.0 alpha 1 / c api / exceptions

[gh-105375](https://github.com/python/cpython/issues/105375): Resolve a defect in [`PyErr_WarnExplicit()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_WarnExplicit) by which an exception could wind up overwritten when the API hit an internal failure.

[gh-107810](https://github.com/python/cpython/issues/107810): Better [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) is emitted where [`PyType_Spec`](https://docs.python.org/3.14/c-api/type.html#c.PyType_Spec) is used together with metaclasses carrying a custom `tp_new`.

[gh-110235](https://github.com/python/cpython/issues/110235): The `PyStructSequence` constructor now raises [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) when fields are duplicated or unknown. Xuehai Pan supplied this patch.

[gh-107916](https://github.com/python/cpython/issues/107916): The C API functions [`PyErr_SetFromErrnoWithFilename()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_SetFromErrnoWithFilename), [`PyErr_SetExcFromWindowsErrWithFilename()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_SetExcFromWindowsErrWithFilename) and [`PyErr_SetFromWindowsErrWithFilename()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_SetFromWindowsErrWithFilename) now stash the error code before they call [`PyUnicode_DecodeFSDefault()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_DecodeFSDefault).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
