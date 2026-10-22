# type slots C API: `PyTypeObject.tp_weaklist`, `PyTypeObject.tp_version_tag`

void *[PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject).tp_subclasses

A collection of subclasses. Internal use only. May be an invalid pointer.

For a list of subclasses, call the Python method [`__subclasses__()`](https://docs.python.org/3.14/reference/datamodel.html#type.__subclasses__).

Changed in version 3.12: For certain types this field does not contain a valid [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*. Its type became void* to signal this.

**Inheritance:**

This field is not inherited.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *[PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject).tp_weaklist

Head of the weak reference list, covering weak references to this type object. Not inherited. Internal use only.

Changed in version 3.12: Internals detail: Across the static builtin types this stays `NULL`, even when weakrefs are added. The weakrefs for each are kept on `PyInterpreterState` instead. Rely on the public C-API or the internal `_PyObject_GET_WEAKREFS_LISTPTR()` macro to sidestep the distinction.

**Inheritance:**

This field is not inherited.

 destructor [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject).tp_del

* The corresponding [slot ID](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) `Py_tp_del` is part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

This field is deprecated. Use `tp_finalize` instead.

 unsigned int [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject).tp_version_tag

Serves as an index into the method cache. Internal use only.

**Inheritance:**

This field is not inherited.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pytypeobject-tp-name-to-pytypeobject-tp-itemsize.md) · [Previous source contract](pytypeobject-tp-free-to-pytypeobject-tp-cache.md) · [Following source contract](pytypeobject-tp-finalize.md)
