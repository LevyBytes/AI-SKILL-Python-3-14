# What’s New In Python 3.5 / Porting to Python 3.5 / Changes in the C API

### Changes in the C API

- The `format` member, which was undocumented, has been dropped from the (non-public) `PyMemoryViewObject` structure. Every extension that depends on the affected portions of `memoryobject.h` has to be rebuilt.

- The `PyMemAllocator` structure took on the new name [`PyMemAllocatorEx`](https://docs.python.org/3.14/c-api/memory.html#c.PyMemAllocatorEx), and a fresh `calloc` field joined it.

- The undocumented `PyObject_REPR()` macro, a source of reference leaks, was removed. To render the [`repr()`](https://docs.python.org/3.14/library/functions.html#repr) of an object, reach instead for the `%R` format character within [`PyUnicode_FromFormat()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_FromFormat)-style functions. (Contributed by Serhiy Storchaka in [bpo-22453](https://bugs.python.org/issue?@action=redirect&bpo=22453).)

- Since a missing [`__module__`](https://docs.python.org/3.14/reference/datamodel.html#type.__module__) attribute disrupts both pickling and introspection, builtin types that lack the `__module__` attribute now provoke a deprecation warning. Down the road this will turn into an [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError). (Contributed by Serhiy Storchaka in [bpo-20204](https://bugs.python.org/issue?@action=redirect&bpo=20204).)

- While implementing [**PEP 492**](https://peps.python.org/pep-0492/), the `tp_reserved` slot belonging to [`PyTypeObject`](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) gave way to a [`tp_as_async`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_as_async) slot. See [Coroutine Objects](https://docs.python.org/3.14/c-api/coro.html#coro-objects) for the newly added types, structures, and functions.

[Subject index](INDEX.md) · [Previous source section](changes-in-the-python-api.md) · [Next source section](new-make-regen-all-build-target.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](porting-to-python-3-5.md)
