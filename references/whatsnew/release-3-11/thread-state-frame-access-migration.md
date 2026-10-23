# What's New In Python 3.11 / C API Changes / Porting to Python 3.11 - sys

`frame`: gone — turn to [`PyThreadState_GetFrame()`](https://docs.python.org/3.14/c-api/threads.html#c.PyThreadState_GetFrame), a function that [bpo-40429](https://bugs.python.org/issue?@action=redirect&bpo=40429) added back in Python 3.9. Take care: it hands you a [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference), so a [`Py_XDECREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_XDECREF) call is needed.

  - `tracing`: altered — turn to [`PyThreadState_EnterTracing()`](https://docs.python.org/3.14/c-api/threads.html#c.PyThreadState_EnterTracing) and [`PyThreadState_LeaveTracing()`](https://docs.python.org/3.14/c-api/threads.html#c.PyThreadState_LeaveTracing), functions that [bpo-43760](https://bugs.python.org/issue?@action=redirect&bpo=43760) brought into Python 3.11.

  - `recursion_depth`: removed, use `(tstate->recursion_limit - tstate->recursion_remaining)` instead.

  - `stackcheck_counter`: removed.

A definition of `PyThreadState_GetFrame()` for Python 3.8 and earlier:

```python
#if PY_VERSION_HEX < 0x030900B1
static inline PyFrameObject* PyThreadState_GetFrame(PyThreadState *tstate)
{
    Py_XINCREF(tstate->frame);
    return tstate->frame;
}
#endif

```

A definition of `PyThreadState_EnterTracing()` and `PyThreadState_LeaveTracing()` for Python 3.10 and earlier:

```python
#if PY_VERSION_HEX < 0x030B00A2
static inline void PyThreadState_EnterTracing(PyThreadState *tstate)
{
    tstate->tracing++;
#if PY_VERSION_HEX >= 0x030A00A1
    tstate->cframe->use_tracing = 0;
#else
    tstate->use_tracing = 0;
#endif
}

static inline void PyThreadState_LeaveTracing(PyThreadState *tstate)
{
    int use_tracing = (tstate->c_tracefunc != NULL || tstate->c_profilefunc != NULL);
    tstate->tracing--;
#if PY_VERSION_HEX >= 0x030A00A1
    tstate->cframe->use_tracing = use_tracing;
#else
    tstate->use_tracing = use_tracing;
#endif
}
#endif

```

Failing that, draw on [the pythoncapi-compat project](https://github.com/python/pythoncapi-compat) to obtain these functions on old Python functions.

- Anyone distributing Python is urged to build it against the optimized Blake2 library [libb2](https://www.blake2.net/).

- For initialization to draw on [`PyConfig.module_search_paths`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.module_search_paths) when setting up [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path), the [`PyConfig.module_search_paths_set`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.module_search_paths_set) field has to be 1 from now on. Leave it unset and initialization recomputes the path, discarding anything you placed in `module_search_paths`.

- [`PyConfig_Read()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Read) has stopped working out the initial search path and will leave [`PyConfig.module_search_paths`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.module_search_paths) empty. If your aim is to derive the default paths and then tweak them, let initialization run to completion, pull [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) back as a Python list via [`PySys_GetObject()`](https://docs.python.org/3.14/c-api/sys.html#c.PySys_GetObject), and edit that list in place.

[Subject index](INDEX.md) · [Previous source section](c-api-frame-accessor-migration.md) · [Next source section](c-api-changes-deprecated.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](c-api-changes-new-features.md) · [Release/subject declaration](c-api-trashcan-lifecycle-migration.md) · [Preceding release/subject continuation](immutable-heap-types-and-vectorcall.md)
