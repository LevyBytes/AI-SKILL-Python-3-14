# Descriptor Objects

## Descriptor Objects

### Descriptor Objects

“Descriptors” are the objects that characterize a particular attribute belonging to some object. You'll come across them inside the dictionary that type objects keep.

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyProperty_Type

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

The type object for the built-in descriptor types.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyDescr_NewGetSet([PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) *type, struct [PyGetSetDef](https://docs.python.org/3.14/c-api/structures.html#c.PyGetSetDef) *getset)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyDescr_NewMember([PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) *type, struct [PyMemberDef](https://docs.python.org/3.14/c-api/structures.html#c.PyMemberDef) *meth)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyMemberDescr_Type

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

The type object backing member descriptor objects that come from [`PyMemberDef`](https://docs.python.org/3.14/c-api/structures.html#c.PyMemberDef) structures. Such descriptors surface a C struct's fields as attributes on a type, and they map onto [`types.MemberDescriptorType`](https://docs.python.org/3.14/library/types.html#types.MemberDescriptorType) objects on the Python side.

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyGetSetDescr_Type

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

The type object behind get/set descriptor objects that come from [`PyGetSetDef`](https://docs.python.org/3.14/c-api/structures.html#c.PyGetSetDef) structures. Descriptors of this kind realize attributes whose values are produced by C getter and setter functions, and they underlie a great many attributes of built-in types.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyDescr_NewMethod([PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) *type, struct [PyMethodDef](https://docs.python.org/3.14/c-api/structures.html#c.PyMethodDef) *meth)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyMethodDescr_Type

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

The type object behind method descriptor objects that come from [`PyMethodDef`](https://docs.python.org/3.14/c-api/structures.html#c.PyMethodDef) structures. Such descriptors present C functions as methods on a type, and they map onto [`types.MemberDescriptorType`](https://docs.python.org/3.14/library/types.html#types.MemberDescriptorType) objects in Python.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyDescr_NewWrapper([PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) *type, struct wrapperbase *wrapper, void *wrapped)

*Return value: New reference.*

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyWrapperDescr_Type

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

The type object behind wrapper descriptor objects that `PyDescr_NewWrapper()` and `PyWrapper_New()` produce. Internally, wrapper descriptors serve to present special methods that are implemented through wrapper structures, and on the Python side they show up as [`types.WrapperDescriptorType`](https://docs.python.org/3.14/library/types.html#types.WrapperDescriptorType) objects.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyDescr_NewClassMethod([PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) *type, [PyMethodDef](https://docs.python.org/3.14/c-api/structures.html#c.PyMethodDef) *method)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

 int PyDescr_IsData([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *descr)

Hands back a nonzero value when the descriptor object *descr* characterizes a data attribute, or `0` when it characterizes a method. The *descr* argument has to be a descriptor object, and no error checking is done.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyWrapper_New([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

[Subject index](INDEX.md) · [Previous source contract](../datetime-objects/pydatetime-capsule-name.md) · [Following source contract](pysuper-type-to-pystaticmethod-new.md)
