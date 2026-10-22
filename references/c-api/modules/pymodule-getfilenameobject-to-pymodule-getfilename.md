# modules C API: `PyModule_GetFilenameObject()`, `PyModule_GetFilename()`

[PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyModule_GetFilenameObject([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *module)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Hand back the filename that *module* was loaded from, drawn from *module*'s [`__file__`](https://docs.python.org/3.14/reference/datamodel.html#module.__file__) attribute. Where that is undefined, or where it isn't a string, raise [`SystemError`](https://docs.python.org/3.14/library/exceptions.html#SystemError) and return `NULL`; failing those cases, give back a reference to a Unicode object.

Added in version 3.2.

 const char *PyModule_GetFilename([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *module)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Behaves like `PyModule_GetFilenameObject()` but hands back the filename encoded as 'utf-8'.

That buffer holds good only until the module's [`__file__`](https://docs.python.org/3.14/reference/datamodel.html#module.__file__) attribute is reassigned or the module is destroyed.

Deprecated since version 3.2: `PyModule_GetFilename()` raises [`UnicodeEncodeError`](https://docs.python.org/3.14/library/exceptions.html#UnicodeEncodeError) on unencodable filenames, use `PyModule_GetFilenameObject()` instead.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pymodule-type-to-pymodule-getdef.md) · [Following source contract](module-definitions.md)
