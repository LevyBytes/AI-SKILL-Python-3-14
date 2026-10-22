# Module State Access from Slot Methods, Getters and Setters

### Module State Access from Slot Methods, Getters and Setters

Note

This is new in Python 3.11.

Slot methods — the speedy C counterparts to special methods, like [`nb_add`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyNumberMethods.nb_add) for [`__add__`](https://docs.python.org/3.14/reference/datamodel.html#object.__add__) or [`tp_new`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_new) for initialization — expose a very plain API that offers no way to pass in the defining class, in contrast with [`PyCMethod`](https://docs.python.org/3.14/c-api/structures.html#c.PyCMethod). The same holds for getters and setters declared via [`PyGetSetDef`](https://docs.python.org/3.14/c-api/structures.html#c.PyGetSetDef).

To get at the module state in those situations, apply the [`PyType_GetModuleByDef()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_GetModuleByDef) function and hand it the module definition. After you hold the module, invoke [`PyModule_GetState()`](https://docs.python.org/3.14/c-api/module.html#c.PyModule_GetState) to obtain the state:

```c
PyObject *module = PyType_GetModuleByDef(Py_TYPE(self), &module_def);
my_struct *state = (my_struct*)PyModule_GetState(module);
if (state == NULL) {
    return NULL;
}

```

`PyType_GetModuleByDef()` operates by scanning the [method resolution order](https://docs.python.org/3.14/glossary.html#term-method-resolution-order) (that is, every superclass) for the earliest superclass that owns a matching module.

Note

In truly unusual cases (inheritance chains that span several modules built from one definition), `PyType_GetModuleByDef()` may not hand back the module of the genuine defining class. Even so, it will always hand back a module carrying the same definition, which guarantees a compatible C memory layout.

[Subject index](INDEX.md) · [Previous source context](module-state-access-from-regular-methods.md) · [Following source context](lifetime-of-the-module-state.md)
