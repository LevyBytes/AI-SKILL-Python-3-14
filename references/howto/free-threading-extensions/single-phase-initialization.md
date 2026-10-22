# Single-Phase Initialization

### Single-Phase Initialization

For an extension built on single-phase initialization (namely [`PyModule_Create()`](https://docs.python.org/3.14/c-api/module.html#c.PyModule_Create)), invoke [`PyUnstable_Module_SetGIL()`](https://docs.python.org/3.14/c-api/module.html#c.PyUnstable_Module_SetGIL) to signal that GIL-free operation is supported. Since that function exists only within the free-threaded build, wrap the call in `#ifdef Py_GIL_DISABLED` so the ordinary build still compiles without error.

```c
static struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT,
    ...
};

PyMODINIT_FUNC
PyInit_mymodule(void)
{
    PyObject *m = PyModule_Create(&moduledef);
    if (m == NULL) {
        return NULL;
    }
#ifdef Py_GIL_DISABLED
    PyUnstable_Module_SetGIL(m, Py_MOD_GIL_NOT_USED);
#endif
    return m;
}

```

[Subject index](INDEX.md) · [Previous source context](multi-phase-initialization.md) · [Following source context](general-api-guidelines.md)
