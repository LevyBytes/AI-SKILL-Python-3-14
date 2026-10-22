# The Basics — PyObject, PyType_FromSpec, PyObject_HEAD, PyTypeObject, PyVarObject_HEAD_INIT, tp_name, tp_doc, PyDoc_STR, tp_basicsize, tp_itemsize, tp_flags, Py_TPFLAGS_DEFAULT, tp_new, PyType_GenericNew, PyType_Ready, PyModule_AddObjectRef, PyModuleDef_Slot, Py_mod_exec, Py_mod_multiple_interpreters, Py_MOD_MULTIPLE_INTERPRETERS_NOT_SUPPORTED, PyModuleDef, PyModuleDef_HEAD_INIT, PyMODINIT_FUNC, PyInit_custom, PyModuleDef_Init

### 2.1. The Basics

Internally, the [CPython](https://docs.python.org/3.14/glossary.html#term-CPython) runtime treats each Python object as a variable of type [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*, which acts as the shared “base type” underneath every Python object. By itself the [`PyObject`](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) structure holds nothing more than the object’s [reference count](https://docs.python.org/3.14/glossary.html#term-reference-count) plus a pointer aimed at the object’s “type object”. That type object is where everything happens: it dictates which (C) routines the interpreter invokes whenever, say, an attribute is fetched from an object, a method is run, or the object is multiplied against something else. Those C routines carry the label “type methods”.

Consequently, defining a fresh extension type boils down to producing a new type object.

A subject like this really only lands through demonstration, so what follows is a tiny yet fully working module that introduces a type called `Custom` within a C extension module named `custom`:

Note

The approach demonstrated here is the classic recipe for declaring *static* extension types. For the majority of needs it will serve you fine. Beyond that, the C API supports heap-allocated extension types built with the [`PyType_FromSpec()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_FromSpec) function, a route this tutorial leaves aside.

```c
#define PY_SSIZE_T_CLEAN
#include <Python.h>

typedef struct {
    PyObject_HEAD
    /* Type-specific fields go here. */
} CustomObject;

static PyTypeObject CustomType = {
    .ob_base = PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "custom.Custom",
    .tp_doc = PyDoc_STR("Custom objects"),
    .tp_basicsize = sizeof(CustomObject),
    .tp_itemsize = 0,
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_new = PyType_GenericNew,
};

static int
custom_module_exec(PyObject *m)
{
    if (PyType_Ready(&CustomType) < 0) {
        return -1;
    }

    if (PyModule_AddObjectRef(m, "Custom", (PyObject *) &CustomType) < 0) {
        return -1;
    }

    return 0;
}

static PyModuleDef_Slot custom_module_slots[] = {
    {Py_mod_exec, custom_module_exec},
    // Just use this while using static types
    {Py_mod_multiple_interpreters, Py_MOD_MULTIPLE_INTERPRETERS_NOT_SUPPORTED},
    {0, NULL}
};

static PyModuleDef custom_module = {
    .m_base = PyModuleDef_HEAD_INIT,
    .m_name = "custom",
    .m_doc = "Example module that creates an extension type.",
    .m_size = 0,
    .m_slots = custom_module_slots,
};

PyMODINIT_FUNC
PyInit_custom(void)
{
    return PyModuleDef_Init(&custom_module);
}

```

Admittedly that’s a lot to absorb in one go, though several pieces should ring a bell from the preceding chapter. Three separate things are declared in this file:

1.

The contents of a `Custom` **object**: that’s the `CustomObject` struct, allocated freshly for every `Custom` instance.

2.

The behavior of the `Custom` **type**: that’s the `CustomType` struct, holding the collection of flags and function pointers the interpreter consults when particular operations come up.

3.

The way the `custom` module is defined and run: that’s the `PyInit_custom` function together with its companion `custom_module` struct that describes the module, plus the `custom_module_exec` function that wires up a brand-new module object.

Here is the first piece:

[Subject index](INDEX.md) · [Previous source section](defining-extension-types-tutorial.md) · [Next source section](the-basics-and-pytype-genericnew.md)
