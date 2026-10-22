# type slots C API: `PyTypeObject.tp_name`, `PyTypeObject.tp_basicsize`, `PyTypeObject.tp_itemsize`

### PyTypeObject Slots

A section on inheritance accompanies each slot. Where [`PyType_Ready()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_Ready) is able to supply a value once the field has been left as `NULL`, a “Default” section appears as well. (Bear in mind that a good many fields configured on [`PyBaseObject_Type`](https://docs.python.org/3.14/c-api/structures.html#c.PyBaseObject_Type) and [`PyType_Type`](https://docs.python.org/3.14/c-api/type.html#c.PyType_Type) effectively serve as defaults.)

 const char *[PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject).tp_name

A pointer to a NUL-terminated string holding the type's name. When a type is reachable as a module global, that string ought to be the complete module name, then a dot, then the type's name; for built-in types it is simply the type name on its own. Where the module sits as a submodule within a package, the entire package name forms part of the complete module name. As an illustration, a type called `T` declared in module `M`, inside subpackage `Q`, inside package `P`, should carry the `tp_name` initializer `"P.Q.M.T"`.

With dynamically allocated type objects, restrict this to just the type name, and place the module name into the type dict explicitly under the key `'__module__'`.

With statically allocated type objects, a dot belongs in the *tp_name* field. Whatever precedes the final dot becomes reachable through the [`__module__`](https://docs.python.org/3.14/reference/datamodel.html#type.__module__) attribute, while whatever follows it becomes reachable through the [`__name__`](https://docs.python.org/3.14/reference/datamodel.html#type.__name__) attribute.

Where there is no dot at all, the whole `tp_name` field becomes reachable through the [`__name__`](https://docs.python.org/3.14/reference/datamodel.html#type.__name__) attribute, and the [`__module__`](https://docs.python.org/3.14/reference/datamodel.html#type.__module__) attribute stays undefined (barring an explicit entry in the dictionary, as covered above). The consequence is that pickling your type becomes impossible. On top of that, pydoc-generated module documentation will omit it.

`NULL` is not allowed for this field. Apart from `tp_itemsize` in some cases, it is the sole mandatory field in [`PyTypeObject()`](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject).

**Inheritance:**

This field is not inherited by subtypes.

 [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject).tp_basicsize

 [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject).tp_itemsize

Together these fields make it possible to compute, in bytes, how large the type's instances are.

Types come in two varieties: a type whose instances are fixed-length carries a zero `tp_itemsize` field, whereas a type whose instances are variable-length carries a non-zero `tp_itemsize` field. Where instances are fixed-length, every instance is the same size — the value held in `tp_basicsize`. (You can break this rule by way of [`PyUnstable_Object_GC_NewWithExtraData()`](https://docs.python.org/3.14/c-api/gcsupport.html#c.PyUnstable_Object_GC_NewWithExtraData).)

Where a type's instances are variable-length, each instance has to include an [`ob_size`](https://docs.python.org/3.14/c-api/structures.html#c.PyVarObject.ob_size) field, and its size works out to `tp_basicsize` plus N multiplied by `tp_itemsize`, with N standing for the object's “length”.

Functions such as [`PyObject_NewVar()`](https://docs.python.org/3.14/c-api/allocation.html#c.PyObject_NewVar) accept N as one of their arguments and record it within the instance's [`ob_size`](https://docs.python.org/3.14/c-api/structures.html#c.PyVarObject.ob_size) field. Be aware that the `ob_size` field can subsequently serve other ends. To illustrate, [`int`](https://docs.python.org/3.14/library/functions.html#int) instances repurpose the bits of `ob_size` in an implementation-defined manner; reach the backing storage and its size through [`PyLong_Export()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_Export).

Note

Reach the [`ob_size`](https://docs.python.org/3.14/c-api/structures.html#c.PyVarObject.ob_size) field through the [`Py_SIZE()`](https://docs.python.org/3.14/c-api/structures.html#c.Py_SIZE) and [`Py_SET_SIZE()`](https://docs.python.org/3.14/c-api/structures.html#c.Py_SET_SIZE) macros.

Note too that having an [`ob_size`](https://docs.python.org/3.14/c-api/structures.html#c.PyVarObject.ob_size) field present in the instance layout is no guarantee that the instance structure is variable-length. Take the [`list`](https://docs.python.org/3.14/library/stdtypes.html#list) type: its instances are fixed-length, and yet they do carry a `ob_size` field. (Just as with [`int`](https://docs.python.org/3.14/library/functions.html#int), steer clear of reading a list's `ob_size` directly. Use [`PyList_Size()`](https://docs.python.org/3.14/c-api/list.html#c.PyList_Size) instead.)

What `tp_basicsize` covers is the room required for the data belonging to the type's `tp_base`, together with whatever additional data each instance demands.

To set `tp_basicsize` properly, apply the `sizeof` operator to the struct that declares the instance layout. That struct is required to contain the struct that declares the base type. Phrased differently, `tp_basicsize` has to be at least as large as the base's `tp_basicsize`.

Given that every type derives from [`object`](https://docs.python.org/3.14/library/functions.html#object), this struct has to contain either [`PyObject`](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) or [`PyVarObject`](https://docs.python.org/3.14/c-api/structures.html#c.PyVarObject) (the choice hinges on whether [`ob_size`](https://docs.python.org/3.14/c-api/structures.html#c.PyVarObject.ob_size) belongs there). The macros [`PyObject_HEAD`](https://docs.python.org/3.14/c-api/structures.html#c.PyObject_HEAD) and [`PyObject_VAR_HEAD`](https://docs.python.org/3.14/c-api/structures.html#c.PyObject_VAR_HEAD) typically supply these, respectively.

The GC header size falls outside the basic size, since that header does not belong to [`PyObject_HEAD`](https://docs.python.org/3.14/c-api/structures.html#c.PyObject_HEAD).

Where the struct that declares the base type isn't known, consult [`PyType_Spec.basicsize`](https://docs.python.org/3.14/c-api/type.html#c.PyType_Spec.basicsize) and [`PyType_FromMetaclass()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_FromMetaclass).

Notes about alignment:

- A multiple of `_Alignof(PyObject)` is what `tp_basicsize` must be. Applying `sizeof` to a `struct` containing [`PyObject_HEAD`](https://docs.python.org/3.14/c-api/structures.html#c.PyObject_HEAD), as advised, lets the compiler guarantee this. Where you forgo a C `struct`, or lean on compiler extensions such as `__attribute__((packed))`, the responsibility falls to you.

- Should the variable items call for some particular alignment, each of `tp_basicsize` and `tp_itemsize` has to be a multiple of it. As an example, where a type's variable part holds a `double`, you are accountable for keeping both fields a multiple of `_Alignof(double)`.

**Inheritance:**

Subtypes inherit these fields independently of one another. (Put another way, where the field is left at zero, [`PyType_Ready()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_Ready) will pull the value across from the base type, signaling that the instances call for no extra storage.)

Where the base type carries a non-zero `tp_itemsize`, assigning `tp_itemsize` a different non-zero value in a subtype is, as a rule, unsafe (though that turns on how the base type is implemented).

[Subject index](INDEX.md) · [Previous source contract](pyvarobject-ob-size.md) · [Following source contract](pytypeobject-tp-dealloc.md)
