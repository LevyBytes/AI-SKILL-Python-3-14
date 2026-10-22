# Module State Access from Classes

### Module State Access from Classes

When you hold a type object created with [`PyType_FromModuleAndSpec()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_FromModuleAndSpec), you can invoke [`PyType_GetModule()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_GetModule) to fetch the linked module, then [`PyModule_GetState()`](https://docs.python.org/3.14/c-api/module.html#c.PyModule_GetState) to fetch that module's state.

To spare yourself some tiresome error-handling boilerplate code, fold those two steps together via [`PyType_GetModuleState()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_GetModuleState), yielding:

```c
my_struct *state = (my_struct*)PyType_GetModuleState(type);
if (state == NULL) {
    return NULL;
}

```

[Subject index](INDEX.md) · [Previous source context](avoiding-pyobject-new.md) · [Following source context](module-state-access-from-regular-methods.md)
