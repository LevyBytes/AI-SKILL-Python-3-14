# PyObject Slots

### PyObject Slots

A type object's structure builds on the [`PyVarObject`](https://docs.python.org/3.14/c-api/structures.html#c.PyVarObject) structure. Dynamic types — those produced by `type_new()`, which a class statement normally triggers — rely on the [`ob_size`](https://docs.python.org/3.14/c-api/structures.html#c.PyVarObject.ob_size) field. Keep in mind that [`PyType_Type`](https://docs.python.org/3.14/c-api/type.html#c.PyType_Type) (the metatype) sets up `tp_itemsize`, so its instances (that is, type objects) *must* carry the `ob_size` field.

[`PyObject.ob_refcnt`](https://docs.python.org/3.14/c-api/structures.html#c.PyObject.ob_refcnt)

>

By way of the `PyObject_HEAD_INIT` macro, a type object's reference count starts at `1`. Be aware that with statically allocated type objects, the instances of that type (objects whose [`ob_type`](https://docs.python.org/3.14/c-api/structures.html#c.PyObject.ob_type) refers back to the type) are *not* counted as references. With dynamically allocated type objects, however, the instances *are* counted as references.

**Inheritance:**

This field is not inherited by subtypes.

[`PyObject.ob_type`](https://docs.python.org/3.14/c-api/structures.html#c.PyObject.ob_type)

>

Here lies the type's own type: that is, its metatype. The argument given to the `PyObject_HEAD_INIT` macro sets it, and ordinarily it ought to be `&PyType_Type`. That said, with dynamically loadable extension modules that have to run on Windows (at minimum), the compiler objects that such a value isn't a valid initializer. The usual workaround, then, is to hand `NULL` to the `PyObject_HEAD_INIT` macro and set this field by hand right when the module's initialization function begins, ahead of any other work. The customary form is:

```c
Foo_Type.ob_type = &PyType_Type;

```

Carry this out before constructing any instances of the type. [`PyType_Ready()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_Ready) tests whether [`ob_type`](https://docs.python.org/3.14/c-api/structures.html#c.PyObject.ob_type) holds `NULL`, and where it does, sets it to the base class's `ob_type` field. Should the field already be non-zero, `PyType_Ready()` leaves it untouched.

**Inheritance:**

This field is inherited by subtypes.

[Subject index](INDEX.md) · [Previous source contract](type-descriptors-construction-and-version-cache.md) · [Following source contract](pyvarobject-ob-size.md)
