# Module State Access from Functions

### Module State Access from Functions

Reaching the state from module-level functions is easy. Each function receives the module object as its first argument; to pull out the state, you can apply `PyModule_GetState`:

```c
static PyObject *
func(PyObject *module, PyObject *args)
{
    my_struct *state = (my_struct*)PyModule_GetState(module);
    if (state == NULL) {
        return NULL;
    }
    // ... rest of logic
}

```

Note

`PyModule_GetState` can hand back `NULL` without raising an exception whenever there is no module state, that is, when `PyModuleDef.m_size` was zero. Within your own module you decide `m_size`, so guarding against this is simple.

[Subject index](INDEX.md) · [Previous source context](opt-out-limiting-to-one-module-object-per-process.md) · [Following source context](heap-types.md)
