# modules C API: `PyModule_Type`, `PyModule_Check()`, `PyModule_CheckExact()`, `PyModule_NewObject()`, `PyModule_New()`, `PyModule_GetDict()`, `PyModule_GetNameObject()`, `PyModule_GetName()`, `PyModule_GetState()`, `PyModule_GetDef()`

### Module Objects

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyModule_Type

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

This [`PyTypeObject`](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) instance stands for the module type in Python. Within Python programs it surfaces under the name [`types.ModuleType`](https://docs.python.org/3.14/library/types.html#types.ModuleType).

 int PyModule_Check([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p)

Yields true when *p* is either a module object or a subtype of one. Success is guaranteed every time this function runs.

 int PyModule_CheckExact([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *p)

Yields true when *p* is a module object proper, though not a subtype of `PyModule_Type`. Success is guaranteed every time this function runs.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyModule_NewObject([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *name)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.7.*

Produce a fresh module object whose [`module.__name__`](https://docs.python.org/3.14/reference/datamodel.html#module.__name__) is assigned *name*. Its `__name__`, [`__doc__`](https://docs.python.org/3.14/reference/datamodel.html#module.__doc__), [`__package__`](https://docs.python.org/3.14/reference/datamodel.html#module.__package__) and [`__loader__`](https://docs.python.org/3.14/reference/datamodel.html#module.__loader__) attributes are populated (every one except `__name__` becomes `None`). Supplying a [`__file__`](https://docs.python.org/3.14/reference/datamodel.html#module.__file__) attribute is left to the caller.

On error, `NULL` is returned together with an exception set.

Added in version 3.3.

Changed in version 3.4: [`__package__`](https://docs.python.org/3.14/reference/datamodel.html#module.__package__) and [`__loader__`](https://docs.python.org/3.14/reference/datamodel.html#module.__loader__) are now set to `None`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyModule_New(const char *name)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Behaves like `PyModule_NewObject()`, except the name arrives as a UTF-8 encoded string rather than as a Unicode object.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyModule_GetDict([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *module)

*Return value: Borrowed reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Hand back the dictionary object backing *module*'s namespace; that object matches the module object's [`__dict__`](https://docs.python.org/3.14/reference/datamodel.html#object.__dict__) attribute. Should *module* not be a module object (nor a subtype of one), [`SystemError`](https://docs.python.org/3.14/library/exceptions.html#SystemError) is raised and `NULL` comes back.

The advice is for extensions to lean on the other `PyModule_*` and `PyObject_*` functions instead of touching a module's [`__dict__`](https://docs.python.org/3.14/reference/datamodel.html#object.__dict__) directly.

What you get back is a borrowed reference held by the module; it stays valid right up until the module is destroyed.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyModule_GetNameObject([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *module)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.7.*

Hand back the [`__name__`](https://docs.python.org/3.14/reference/datamodel.html#module.__name__) value of *module*. When the module supplies none, or when the value isn't a string, [`SystemError`](https://docs.python.org/3.14/library/exceptions.html#SystemError) is raised and `NULL` comes back.

Added in version 3.3.

 const char *PyModule_GetName([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *module)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Behaves like `PyModule_GetNameObject()` but hands back the name encoded as `'utf-8'`.

That buffer stays good only until the module gets renamed or destroyed. Be aware that Python code can rename a module simply by assigning to its [`__name__`](https://docs.python.org/3.14/reference/datamodel.html#module.__name__) attribute.

 void *PyModule_GetState([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *module)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Hand back the module's "state": namely a pointer to the memory block reserved when the module was created, or else `NULL`. Refer to `PyModuleDef.m_size`.

 PyModuleDef *PyModule_GetDef([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *module)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Hand back a pointer to the `PyModuleDef` struct that the module was built from, or `NULL` when the module didn't come from a definition.

When something goes wrong, `NULL` is returned with an exception set. Call [`PyErr_Occurred()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Occurred) to distinguish that situation from an absent `PyModuleDef`.

[Subject index](INDEX.md) · [Following source contract](pymodule-getfilenameobject-to-pymodule-getfilename.md)
