# Python 3.13.0 alpha 6 / c api / unicode

[gh-111696](https://github.com/python/cpython/issues/111696): Extend [`PyUnicode_FromFormat()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_FromFormat) with support for the `%T`, `%T#`, `%N` and `%N#` formats: they render the fully qualified name of an object's type and of a type by calling [`PyType_GetModuleName()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_GetModuleName). Consult [**PEP 737**](https://peps.python.org/pep-0737/) for further detail. Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
