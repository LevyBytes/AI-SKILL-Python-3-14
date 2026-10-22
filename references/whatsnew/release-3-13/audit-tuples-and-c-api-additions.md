# Python 3.13 changes: Audit tuples, thread state and attribute-query additions

- Introduce the [`PySys_AuditTuple()`](https://docs.python.org/3.14/c-api/sys.html#c.PySys_AuditTuple) function to stand alongside [`PySys_Audit()`](https://docs.python.org/3.14/c-api/sys.html#c.PySys_Audit), receiving its event arguments through a Python [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple) object. (Contributed by Victor Stinner in [gh-85283](https://github.com/python/cpython/issues/85283).)

- Introduce the [`PyThreadState_GetUnchecked()`](https://docs.python.org/3.14/c-api/threads.html#c.PyThreadState_GetUnchecked) function as a counterpart to [`PyThreadState_Get()`](https://docs.python.org/3.14/c-api/threads.html#c.PyThreadState_Get) that, when the value is `NULL`, refrains from terminating the process via a fatal error. Verifying whether the outcome is `NULL` then falls to the caller. (Contributed by Victor Stinner in [gh-108867](https://github.com/python/cpython/issues/108867).)

- Introduce the [`PyType_GetFullyQualifiedName()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_GetFullyQualifiedName) function that retrieves the fully qualified name of a type. Whenever [`type.__module__`](https://docs.python.org/3.14/reference/datamodel.html#type.__module__) holds a string differing from both `'builtins'` and `'__main__'`, that module name gets placed in front. (Contributed by Victor Stinner in [gh-111696](https://github.com/python/cpython/issues/111696).)

- Introduce the [`PyType_GetModuleName()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_GetModuleName) function that retrieves the module name of a type. The result matches what reading the [`type.__module__`](https://docs.python.org/3.14/reference/datamodel.html#type.__module__) attribute returns. (Contributed by Eric Snow and Victor Stinner in [gh-111696](https://github.com/python/cpython/issues/111696).)

- Introduce the [`PyUnicode_EqualToUTF8AndSize()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_EqualToUTF8AndSize) and [`PyUnicode_EqualToUTF8()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_EqualToUTF8) functions that match a Unicode object against a const char* UTF-8 encoded string, giving `1` on equality and `0` when they differ. Exceptions are never raised by these functions. (Contributed by Serhiy Storchaka in [gh-110289](https://github.com/python/cpython/issues/110289).)

- Introduce the [`PyWeakref_GetRef()`](https://docs.python.org/3.14/c-api/weakref.html#c.PyWeakref_GetRef) function to stand alongside [`PyWeakref_GetObject()`](https://docs.python.org/3.14/c-api/weakref.html#c.PyWeakref_GetObject), yielding a [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference), or `NULL` once the referent has stopped being live. (Contributed by Victor Stinner in [gh-105927](https://github.com/python/cpython/issues/105927).)

- Introduce corrected variants of functions that quietly discard errors:

  - [`PyObject_HasAttrWithError()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_HasAttrWithError) replaces [`PyObject_HasAttr()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_HasAttr).

  - [`PyObject_HasAttrStringWithError()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_HasAttrStringWithError) replaces [`PyObject_HasAttrString()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_HasAttrString).

  - [`PyMapping_HasKeyWithError()`](https://docs.python.org/3.14/c-api/mapping.html#c.PyMapping_HasKeyWithError) replaces [`PyMapping_HasKey()`](https://docs.python.org/3.14/c-api/mapping.html#c.PyMapping_HasKey).

  - [`PyMapping_HasKeyStringWithError()`](https://docs.python.org/3.14/c-api/mapping.html#c.PyMapping_HasKeyStringWithError) replaces [`PyMapping_HasKeyString()`](https://docs.python.org/3.14/c-api/mapping.html#c.PyMapping_HasKeyString).

The fresh functions yield `-1` whenever an error arises, the usual `1` for true, and `0` for false.

(Contributed by Serhiy Storchaka in [gh-108511](https://github.com/python/cpython/issues/108511).)

[Subject index](INDEX.md) · [Previous source section](dictionary-removal-and-c-api-additions.md) · [Next source section](c-api-changes-changed-c-apis.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](c-api-changes-new-features.md) · [Preceding release/subject continuation](c-api-changes-new-features.md)
