# Python 3.13.0 alpha 5 / library / pydoc

[gh-116143](https://github.com/python/cpython/issues/116143): Repair a race within pydoc `_start_server`, closing a window where `_start_server` could hand back a thread that is "serving" yet carries no `docserver`.

[gh-65824](https://github.com/python/cpython/issues/65824): Make the `less` prompt nicer in [`pydoc`](https://docs.python.org/3.14/library/pydoc.html#module-pydoc).

[gh-113942](https://github.com/python/cpython/issues/113942): [`pydoc`](https://docs.python.org/3.14/library/pydoc.html#module-pydoc) will now list module-level functions that are implemented as builtin methods, including `MethodDescriptorType` and `WrapperDescriptorType`, rather than omitting them.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
