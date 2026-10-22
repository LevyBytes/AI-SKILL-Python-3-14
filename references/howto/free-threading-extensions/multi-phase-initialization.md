# Multi-Phase Initialization

### Multi-Phase Initialization

Where an extension relies on multi-phase initialization (that is, [`PyModuleDef_Init()`](https://docs.python.org/3.14/c-api/extension-modules.html#c.PyModuleDef_Init)), include a [`Py_mod_gil`](https://docs.python.org/3.14/c-api/module.html#c.Py_mod_gil) slot within its module definition. Should the extension also target earlier CPython releases, wrap that slot behind a [`PY_VERSION_HEX`](https://docs.python.org/3.14/c-api/apiabiversion.html#c.PY_VERSION_HEX) guard.

```c
static struct PyModuleDef_Slot module_slots[] = {
    ...
#if PY_VERSION_HEX >= 0x030D0000
    {Py_mod_gil, Py_MOD_GIL_NOT_USED},
#endif
    {0, NULL}
};

static struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT,
    .m_slots = module_slots,
    ...
};

```

[Subject index](INDEX.md) · [Previous source context](module-initialization.md) · [Following source context](single-phase-initialization.md)
