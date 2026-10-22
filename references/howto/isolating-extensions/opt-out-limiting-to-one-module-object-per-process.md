# Opt-Out: Limiting to One Module Object per Process

### Opt-Out: Limiting to One Module Object per Process

A non-negative `PyModuleDef.m_size` declares that a module copes with multiple interpreters properly. Where that is not yet true of your module, you may deliberately allow your module to load just once per process. For instance:

```c
// A process-wide flag
static int loaded = 0;

// Mutex to provide thread safety (only needed for free-threaded Python)
static PyMutex modinit_mutex = {0};

static int
exec_module(PyObject* module)
{
    PyMutex_Lock(&modinit_mutex);
    if (loaded) {
        PyMutex_Unlock(&modinit_mutex);
        PyErr_SetString(PyExc_ImportError,
                        "cannot load module more than once per process");
        return -1;
    }
    loaded = 1;
    PyMutex_Unlock(&modinit_mutex);
    // ... rest of initialization
}

```

Where your module's [`PyModuleDef.m_clear`](https://docs.python.org/3.14/c-api/module.html#c.PyModuleDef.m_clear) function can ready things for a later re-initialization, it ought to reset the `loaded` flag. Then your module will not back multiple instances living *concurrently*, yet it will, for instance, back being loaded after the Python runtime shuts down ([`Py_FinalizeEx()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_FinalizeEx)) and is re-initialized ([`Py_Initialize()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_Initialize)).

[Subject index](INDEX.md) · [Previous source context](managing-per-module-state.md) · [Following source context](module-state-access-from-functions.md)
