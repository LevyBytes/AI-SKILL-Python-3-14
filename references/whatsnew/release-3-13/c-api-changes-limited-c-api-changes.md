# What's New In Python 3.13 / C API Changes / Limited C API Changes

### Limited C API Changes

- These functions now belong to the Limited C API:

  - [`PyMem_RawMalloc()`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_RawMalloc)

  - [`PyMem_RawCalloc()`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_RawCalloc)

  - [`PyMem_RawRealloc()`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_RawRealloc)

  - [`PyMem_RawFree()`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_RawFree)

  - [`PySys_Audit()`](https://docs.python.org/3.14/c-api/sys.html#c.PySys_Audit)

  - [`PySys_AuditTuple()`](https://docs.python.org/3.14/c-api/sys.html#c.PySys_AuditTuple)

  - [`PyType_GetModuleByDef()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_GetModuleByDef)

(Contributed by Victor Stinner in [gh-85283](https://github.com/python/cpython/issues/85283) and [gh-116936](https://github.com/python/cpython/issues/116936).)

- A Python build that uses [`--with-trace-refs`](https://docs.python.org/3.14/using/configure.html#cmdoption-with-trace-refs) (tracing references) can now work with the [Limited API](https://docs.python.org/3.14/c-api/stable.html#limited-c-api). (Contributed by Victor Stinner in [gh-108634](https://github.com/python/cpython/issues/108634).)

[Subject index](INDEX.md) · [Previous source section](c-api-changes-changed-c-apis.md) · [Next source section](c-api-changes-removed-c-apis.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](c-api-changes-new-features.md)
