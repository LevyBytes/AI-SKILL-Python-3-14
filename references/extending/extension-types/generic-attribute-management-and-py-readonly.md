# Generic Attribute Management — PyType_Ready, tp_getattro, PyTypeObject, tp_setattro, PyMethodDef, tp_methods, PyMemberDef, tp_members, PyGetSetDef, tp_getset, PyCFunction, Py_T_INT, Py_T_DOUBLE, Py_READONLY

### 3.3.1. Generic Attribute Management

The bulk of extension types rely solely on *simple* attributes. So what qualifies an attribute as simple? Just a small handful of requirements have to hold:

1.

By the time [`PyType_Ready()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_Ready) runs, the names of the attributes have to be known.

2.

No special handling is required to note that an attribute got read or assigned, and no behavior has to depend on the value either.

Bear in mind that nothing in this list constrains what the attribute values may be, the moment those values are computed, or the manner in which relevant data is kept.

The moment [`PyType_Ready()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_Ready) executes, it draws on three tables that the type object references in order to build [descriptor](https://docs.python.org/3.14/glossary.html#term-descriptor)s, which then land in the type object's dictionary. Every descriptor governs access to a single attribute of the instance object. None of the tables is mandatory; should all three be `NULL`, the type's instances will carry only the attributes handed down from their base type, and you ought to keep the [`tp_getattro`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_getattro) and [`tp_setattro`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_setattro) fields set to `NULL` too, so the base type takes charge of attributes.

These tables show up as a trio of fields on the type object:

```c
struct PyMethodDef *tp_methods;
struct PyMemberDef *tp_members;
struct PyGetSetDef *tp_getset;

```

Whenever [`tp_methods`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_methods) is non-`NULL`, it has to point at an array of [`PyMethodDef`](https://docs.python.org/3.14/c-api/structures.html#c.PyMethodDef) structures. Every row in the table is one instance of the following structure:

```c
typedef struct PyMethodDef {
    const char  *ml_name;       /* method name */
    PyCFunction  ml_meth;       /* implementation function */
    int          ml_flags;      /* flags */
    const char  *ml_doc;        /* docstring */
} PyMethodDef;

```

You should supply one row per method the type offers; methods handed down from a base type call for no rows. A single extra row belongs at the very end, serving as a sentinel that signals where the array stops. That sentinel's [`ml_name`](https://docs.python.org/3.14/c-api/structures.html#c.PyMethodDef.ml_name) field has to be `NULL`.

The job of the second table is to declare attributes that correspond straight to data held in the instance. A range of primitive C types is supported, and access can be either read-only or read-write. Here is how the table's structures are defined:

```c
typedef struct PyMemberDef {
    const char *name;
    int         type;
    int         offset;
    int         flags;
    const char *doc;
} PyMemberDef;

```

Per row in the table, a [descriptor](https://docs.python.org/3.14/glossary.html#term-descriptor) gets built and attached to the type, capable of pulling a value out of the instance structure. The [`type`](https://docs.python.org/3.14/c-api/structures.html#c.PyMemberDef.type) field ought to hold a type code such as [`Py_T_INT`](https://docs.python.org/3.14/c-api/structures.html#c.Py_T_INT) or [`Py_T_DOUBLE`](https://docs.python.org/3.14/c-api/structures.html#c.Py_T_DOUBLE); that value drives how Python values are converted to and from C values. As for the [`flags`](https://docs.python.org/3.14/c-api/structures.html#c.PyMemberDef.flags) field, it holds flags governing how the attribute may be reached: setting it to [`Py_READONLY`](https://docs.python.org/3.14/c-api/structures.html#c.Py_READONLY) stops Python code from assigning to it.

A neat benefit of relying on the [`tp_members`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_members) table to construct descriptors used at runtime is that every attribute declared in this fashion can carry an associated doc string just by supplying the text within the table. Through the introspection API, an application can pull the descriptor off the class object and obtain the doc string via its [`__doc__`](https://docs.python.org/3.14/reference/datamodel.html#type.__doc__) attribute.

Just like the [`tp_methods`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_methods) table, a sentinel row whose [`ml_name`](https://docs.python.org/3.14/c-api/structures.html#c.PyMethodDef.ml_name) value is `NULL` must be present.

[Subject index](INDEX.md) · [Previous source section](attribute-access-slots.md) · [Next source section](type-specific-attribute-management-and-pyexc-runtimeerror.md)
