# type slots C API: `PyTypeObject.tp_methods`, `PyTypeObject.tp_members`, `PyTypeObject.tp_getset`, `PyTypeObject.tp_base`, `PyTypeObject.tp_dict`

struct [PyMethodDef](https://docs.python.org/3.14/c-api/structures.html#c.PyMethodDef) *[PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject).tp_methods

* The corresponding [slot ID](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) `Py_tp_methods` is part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

A nullable pointer to a static `NULL`-terminated array of [`PyMethodDef`](https://docs.python.org/3.14/c-api/structures.html#c.PyMethodDef) structures, which declare the ordinary methods belonging to this type.

Every array entry causes a method descriptor to be placed into the type’s dictionary (refer to `tp_dict` further down).

**Inheritance:**

Subtypes do not inherit this field (a separate mechanism handles method inheritance).

 struct [PyMemberDef](https://docs.python.org/3.14/c-api/structures.html#c.PyMemberDef) *[PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject).tp_members

* The corresponding [slot ID](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) `Py_tp_members` is part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

A nullable pointer to a static `NULL`-terminated array of [`PyMemberDef`](https://docs.python.org/3.14/c-api/structures.html#c.PyMemberDef) structures, which declare the ordinary data members (fields or slots) carried by instances of this type.

Every array entry causes a member descriptor to be placed into the type’s dictionary (refer to `tp_dict` further down).

**Inheritance:**

Subtypes do not inherit this field (a separate mechanism handles member inheritance).

 struct [PyGetSetDef](https://docs.python.org/3.14/c-api/structures.html#c.PyGetSetDef) *[PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject).tp_getset

* The corresponding [slot ID](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) `Py_tp_getset` is part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

A nullable pointer to a static `NULL`-terminated array of [`PyGetSetDef`](https://docs.python.org/3.14/c-api/structures.html#c.PyGetSetDef) structures, which declare the computed attributes carried by instances of this type.

Every array entry causes a getset descriptor to be placed into the type’s dictionary (refer to `tp_dict` further down).

**Inheritance:**

Subtypes do not inherit this field (a separate mechanism handles inheritance of computed attributes).

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) *[PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject).tp_base

* The corresponding [slot ID](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) `Py_tp_base` is part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

A nullable pointer to the base type whose type properties are inherited. Only single inheritance applies here; to obtain multiple inheritance you must build a type object dynamically by invoking the metatype.

Note

How a slot is initialized follows the rules that govern initializing globals. Under C99 the initializers have to be “address constants”. Function designators such as [`PyType_GenericNew()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_GenericNew), which implicitly convert to a pointer, qualify as valid C99 address constants.

By contrast, applying the unary ‘&’ operator to a variable that isn’t static, for example [`PyBaseObject_Type`](https://docs.python.org/3.14/c-api/structures.html#c.PyBaseObject_Type), need not yield an address constant. Some compilers permit it (gcc does), whereas MSVC refuses. In this specific respect both compilers conform strictly to the standard.

Because of that, set `tp_base` within the extension module’s init function.

**Inheritance:**

Subtypes do not inherit this field (obviously).

**Default:**

The default value of this field is `&PyBaseObject_Type` (which Python programmers recognize as the type [`object`](https://docs.python.org/3.14/library/functions.html#object)).

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *[PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject).tp_dict

Here is where [`PyType_Ready()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_Ready) keeps the type’s dictionary.

Ordinarily you should set this field to `NULL` prior to calling PyType_Ready; alternatively, you may supply a dictionary holding starting attributes for the type. After [`PyType_Ready()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_Ready) has initialized the type, you may still add further attributes to this dictionary, provided they don’t map to overloaded operations (such as [`__add__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__add__)). After the type’s initialization is complete, regard this field as read-only.

Certain types keep their dictionary elsewhere than this slot. Call [`PyType_GetDict()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_GetDict) to fetch the dictionary belonging to any given type.

Changed in version 3.12: Internals detail: Static builtin types always leave this as `NULL`. The dict for those types instead lives on `PyInterpreterState`. Call [`PyType_GetDict()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_GetDict) to obtain the dict for any given type.

**Inheritance:**

Subtypes do not inherit this field (although the attributes declared inside it are inherited through a separate mechanism).

**Default:**

When this field is `NULL`, [`PyType_Ready()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_Ready) will attach a fresh dictionary to it.

Warning

Using [`PyDict_SetItem()`](https://docs.python.org/3.14/c-api/dict.html#c.PyDict_SetItem) on `tp_dict`, or otherwise altering it through the dictionary C-API, is unsafe.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pytypeobject-tp-name-to-pytypeobject-tp-itemsize.md) · [Following source contract](pytypeobject-tp-descr-get-to-pytypeobject-tp-dictoffset.md)
