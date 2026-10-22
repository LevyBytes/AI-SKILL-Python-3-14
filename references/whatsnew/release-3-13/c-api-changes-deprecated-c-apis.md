# What's New In Python 3.13 / C API Changes / Deprecated C APIs — sys

### Deprecated C APIs

- Deprecate old Python initialization functions:

  - [`PySys_ResetWarnOptions()`](https://docs.python.org/3.14/c-api/sys.html#c.PySys_ResetWarnOptions): clears [`sys.warnoptions`](https://docs.python.org/3.14/library/sys.html#sys.warnoptions) along with `warnings.filters` as the replacement.

  - [`Py_GetExecPrefix()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_GetExecPrefix): Get [`sys.exec_prefix`](https://docs.python.org/3.14/library/sys.html#sys.exec_prefix) instead.

  - [`Py_GetPath()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_GetPath): Get [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) instead.

  - [`Py_GetPrefix()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_GetPrefix): Get [`sys.prefix`](https://docs.python.org/3.14/library/sys.html#sys.prefix) instead.

  - [`Py_GetProgramFullPath()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_GetProgramFullPath): Get [`sys.executable`](https://docs.python.org/3.14/library/sys.html#sys.executable) instead.

  - [`Py_GetProgramName()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_GetProgramName): Get [`sys.executable`](https://docs.python.org/3.14/library/sys.html#sys.executable) instead.

  - [`Py_GetPythonHome()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_GetPythonHome): read [`PyConfig.home`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.home) or fall back to the [`PYTHONHOME`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONHOME) environment variable.

(Contributed by Victor Stinner in [gh-105145](https://github.com/python/cpython/issues/105145).)

- [Soft deprecate](https://docs.python.org/3.14/glossary.html#term-soft-deprecated) the [`PyEval_GetBuiltins()`](https://docs.python.org/3.14/c-api/reflection.html#c.PyEval_GetBuiltins), [`PyEval_GetGlobals()`](https://docs.python.org/3.14/c-api/reflection.html#c.PyEval_GetGlobals), and [`PyEval_GetLocals()`](https://docs.python.org/3.14/c-api/reflection.html#c.PyEval_GetLocals) functions, each handing back a [borrowed reference](https://docs.python.org/3.14/glossary.html#term-borrowed-reference). (Soft deprecated as part of [**PEP 667**](https://peps.python.org/pep-0667/).)

- Deprecate [`PyImport_ImportModuleNoBlock()`](https://docs.python.org/3.14/c-api/import.html#c.PyImport_ImportModuleNoBlock), which has been nothing but an alias for [`PyImport_ImportModule()`](https://docs.python.org/3.14/c-api/import.html#c.PyImport_ImportModule) ever since Python 3.3. (Contributed by Victor Stinner in [gh-105396](https://github.com/python/cpython/issues/105396).)

- [Soft deprecate](https://docs.python.org/3.14/glossary.html#term-soft-deprecated) the [`PyModule_AddObject()`](https://docs.python.org/3.14/c-api/module.html#c.PyModule_AddObject) function. Prefer [`PyModule_Add()`](https://docs.python.org/3.14/c-api/module.html#c.PyModule_Add) or [`PyModule_AddObjectRef()`](https://docs.python.org/3.14/c-api/module.html#c.PyModule_AddObjectRef) in its place. (Contributed by Serhiy Storchaka in [gh-86493](https://github.com/python/cpython/issues/86493).)

- Deprecate the legacy `Py_UNICODE` and `PY_UNICODE_TYPE` types together with the `Py_UNICODE_WIDE` define. Work with the `wchar_t` type directly going forward. From Python 3.3 on, `Py_UNICODE` and `PY_UNICODE_TYPE` have merely been aliases for `wchar_t`. (Contributed by Victor Stinner in [gh-105156](https://github.com/python/cpython/issues/105156).)

- Deprecate the [`PyWeakref_GetObject()`](https://docs.python.org/3.14/c-api/weakref.html#c.PyWeakref_GetObject) and [`PyWeakref_GET_OBJECT()`](https://docs.python.org/3.14/c-api/weakref.html#c.PyWeakref_GET_OBJECT) functions, each yielding a [borrowed reference](https://docs.python.org/3.14/glossary.html#term-borrowed-reference). Swap them for the fresh [`PyWeakref_GetRef()`](https://docs.python.org/3.14/c-api/weakref.html#c.PyWeakref_GetRef) function, which hands back a [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference). To obtain `PyWeakref_GetRef()` on Python 3.12 and earlier, rely on the [pythoncapi-compat project](https://github.com/python/pythoncapi-compat/). (Contributed by Victor Stinner in [gh-105927](https://github.com/python/cpython/issues/105927).)

[Subject index](INDEX.md) · [Previous source section](removed-thread-and-internal-apis.md) · [Next source section](c-api-removals-scheduled-for-3-14.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](c-api-changes-new-features.md)
