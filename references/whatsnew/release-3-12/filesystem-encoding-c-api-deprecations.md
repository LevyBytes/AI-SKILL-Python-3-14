# Python 3.12 changes: Filesystem encoding, member and exception-display deprecations

`Py_HasFileSystemDefaultEncoding`: use [`PyConfig.filesystem_encoding`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.filesystem_encoding)

  - `Py_FileSystemDefaultEncodeErrors`: use [`PyConfig.filesystem_errors`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.filesystem_errors)

  - `Py_UTF8Mode`: use [`PyPreConfig.utf8_mode`](https://docs.python.org/3.14/c-api/init_config.html#c.PyPreConfig.utf8_mode) (see [`Py_PreInitialize()`](https://docs.python.org/3.14/c-api/init_config.html#c.Py_PreInitialize))

Reach for the [`Py_InitializeFromConfig()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_InitializeFromConfig) API together with [`PyConfig`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig) in their place. (Contributed by Victor Stinner in [gh-77782](https://github.com/python/cpython/issues/77782).)

- Building [`immutable types`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_IMMUTABLETYPE) atop mutable bases is now deprecated and Python 3.14 will switch it off. ([gh-95388](https://github.com/python/cpython/issues/95388))

- Although the `structmember.h` header is now deprecated, it stays available and nobody intends to delete it.

Simply including `Python.h` now surfaces everything it held, with a `Py` prefix tacked on wherever one was absent:

  - [`PyMemberDef`](https://docs.python.org/3.14/c-api/structures.html#c.PyMemberDef), [`PyMember_GetOne()`](https://docs.python.org/3.14/c-api/structures.html#c.PyMember_GetOne) and [`PyMember_SetOne()`](https://docs.python.org/3.14/c-api/structures.html#c.PyMember_SetOne)

  - Type macros like [`Py_T_INT`](https://docs.python.org/3.14/c-api/structures.html#c.Py_T_INT), [`Py_T_DOUBLE`](https://docs.python.org/3.14/c-api/structures.html#c.Py_T_DOUBLE), etc. (previously `T_INT`, `T_DOUBLE`, etc.)

  - The flags [`Py_READONLY`](https://docs.python.org/3.14/c-api/structures.html#c.Py_READONLY) (previously `READONLY`) and [`Py_AUDIT_READ`](https://docs.python.org/3.14/c-api/structures.html#c.Py_AUDIT_READ) (previously all uppercase)

A handful of items stay unexposed from `Python.h`:

  - [`T_OBJECT`](https://docs.python.org/3.14/c-api/structures.html#c.T_OBJECT) (use [`Py_T_OBJECT_EX`](https://docs.python.org/3.14/c-api/structures.html#c.Py_T_OBJECT_EX))

  - [`T_NONE`](https://docs.python.org/3.14/c-api/structures.html#c.T_NONE) (previously undocumented, and pretty quirky)

  - The macro `WRITE_RESTRICTED` which does nothing.

  - The macros `RESTRICTED` and `READ_RESTRICTED`, equivalents of [`Py_AUDIT_READ`](https://docs.python.org/3.14/c-api/structures.html#c.Py_AUDIT_READ).

  - Under certain configurations, `Python.h` skips pulling in `<stddef.h>`. Include it by hand whenever you reach for `offsetof()`.

The deprecated header keeps serving its original contents beneath the original names. Existing code may carry on untouched, save for cases where the extra include and the non-namespaced macros genuinely irritate you.

(Contributed in [gh-47146](https://github.com/python/cpython/issues/47146) by Petr Viktorin; this built upon prior groundwork from Alexander Belopolsky together with Matthias Braun.)

- Both [`PyErr_Fetch()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Fetch) and [`PyErr_Restore()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Restore) are deprecated. Reach for [`PyErr_GetRaisedException()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_GetRaisedException) and [`PyErr_SetRaisedException()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_SetRaisedException) in their place. (Contributed by Mark Shannon in [gh-101578](https://github.com/python/cpython/issues/101578).)

- `PyErr_Display()` is deprecated. Reach for [`PyErr_DisplayException()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_DisplayException) in its place. (Contributed by Irit Katriel in [gh-102755](https://github.com/python/cpython/issues/102755)).

- `_PyErr_ChainExceptions` is deprecated. Reach for `_PyErr_ChainExceptions1` in its place. (Contributed by Irit Katriel in [gh-102192](https://github.com/python/cpython/issues/102192).)

- Reaching for [`PyType_FromSpec()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_FromSpec), [`PyType_FromSpecWithBases()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_FromSpecWithBases) or [`PyType_FromModuleAndSpec()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_FromModuleAndSpec) to build a class whose metaclass replaces [`tp_new`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_new) is deprecated. Invoke the metaclass in its place.

[Subject index](INDEX.md) · [Previous source section](c-api-changes-deprecated-deprecated.md) · [Next source section](c-api-changes-deprecated-pending-removal-in-python-3-14.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](c-api-changes-new-features.md) · [Release/subject declaration](c-api-changes-deprecated-deprecated.md)
