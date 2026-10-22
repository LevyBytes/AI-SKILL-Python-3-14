# Python 3.14 changes: Type freezing, base tokens and Unicode writers

Introduce the [`PyType_Freeze()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_Freeze) function, which renders a type immutable. (Contributed by Victor Stinner in [gh-121654](https://github.com/python/cpython/issues/121654).)

- Introduce [`PyType_GetBaseByToken()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_GetBaseByToken) plus the [`Py_tp_token`](https://docs.python.org/3.14/c-api/type.html#c.Py_tp_token) slot, simplifying superclass identification and aiming to address the type-checking concern raised in [**PEP 630**](https://peps.python.org/pep-0630/#type-checking). (Contributed in [gh-124153](https://github.com/python/cpython/issues/124153).)

- Introduce a fresh [`PyUnicode_Equal()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_Equal) function for checking whether two strings match. It is included in the Limited C API as well. (Contributed by Victor Stinner in [gh-124502](https://github.com/python/cpython/issues/124502).)

- Introduce a fresh [`PyUnicodeWriter`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter) API for building a Python [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) object, providing these functions:

  - [`PyUnicodeWriter_Create()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_Create)

  - [`PyUnicodeWriter_DecodeUTF8Stateful()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_DecodeUTF8Stateful)

  - [`PyUnicodeWriter_Discard()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_Discard)

  - [`PyUnicodeWriter_Finish()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_Finish)

  - [`PyUnicodeWriter_Format()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_Format)

  - [`PyUnicodeWriter_WriteASCII()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_WriteASCII)

  - [`PyUnicodeWriter_WriteChar()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_WriteChar)

  - [`PyUnicodeWriter_WriteRepr()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_WriteRepr)

  - [`PyUnicodeWriter_WriteStr()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_WriteStr)

  - [`PyUnicodeWriter_WriteSubstring()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_WriteSubstring)

  - [`PyUnicodeWriter_WriteUCS4()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_WriteUCS4)

  - [`PyUnicodeWriter_WriteUTF8()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_WriteUTF8)

  - [`PyUnicodeWriter_WriteWideChar()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_WriteWideChar)

(Contributed by Victor Stinner in [gh-119182](https://github.com/python/cpython/issues/119182).)

- Within [`PyArg_ParseTuple()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_ParseTuple) and comparable functions, the `k` and `K` formats now consult [`__index__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__) when present, matching every other integer format. (Contributed by Serhiy Storchaka in [gh-112068](https://github.com/python/cpython/issues/112068).)

- Provide a fresh `p` format unit inside [`Py_BuildValue()`](https://docs.python.org/3.14/c-api/arg.html#c.Py_BuildValue) that turns a C integer into a Python [`bool`](https://docs.python.org/3.14/library/functions.html#bool) object. (Contributed by Pablo Galindo in [bpo-45325](https://bugs.python.org/issue?@action=redirect&bpo=45325).)

- Introduce [`PyUnstable_IsImmortal()`](https://docs.python.org/3.14/c-api/object.html#c.PyUnstable_IsImmortal), which checks whether an object is [immortal](https://docs.python.org/3.14/glossary.html#term-immortal), intended for debugging. (Contributed by Peter Bierma in [gh-128509](https://github.com/python/cpython/issues/128509).)

- Introduce [`PyUnstable_Object_EnableDeferredRefcount()`](https://docs.python.org/3.14/c-api/object.html#c.PyUnstable_Object_EnableDeferredRefcount), which turns on deferred reference counting, per [**PEP 703**](https://peps.python.org/pep-0703/).

[Subject index](INDEX.md) · [Previous source section](iterator-results-and-monitoring-apis.md) · [Next source section](unique-reference-and-free-threading-apis.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](c-api-changes-python-configuration-c-api.md) · [Release/subject declaration](c-api-additions.md) · [Preceding release/subject continuation](c-api-additions.md)
