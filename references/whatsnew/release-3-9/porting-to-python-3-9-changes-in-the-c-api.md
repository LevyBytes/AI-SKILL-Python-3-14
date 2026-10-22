# What's New In Python 3.9 / Porting to Python 3.9 / Changes in the C API

### Changes in the C API

- Since Python 3.8, instances of [heap-allocated types](https://docs.python.org/3.14/c-api/typeobj.html#heap-types) (for instance those built with [`PyType_FromSpec()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_FromSpec) and comparable APIs) keep a reference to their type object. As the ?Changes in the C API? section of Python 3.8 noted, the overwhelming majority of cases see no side effect, but for any type carrying a custom [`tp_traverse`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_traverse) function, make sure every custom `tp_traverse` function on heap-allocated types visits the type of the object.

>

Example:

```c
int
foo_traverse(PyObject *self, visitproc visit, void *arg)
{
// Rest of the traverse function
#if PY_VERSION_HEX >= 0x03090000
    // This was not needed before Python 3.9 (Python issue 35810 and 40217)
    Py_VISIT(Py_TYPE(self));
#endif
}

```

When your traverse function defers to `tp_traverse` of its base class (or some other type), be sure `Py_TYPE(self)` gets visited a single time only. Bear in mind that only a [heap type](https://docs.python.org/3.14/c-api/typeobj.html#heap-types) is expected to visit the type within `tp_traverse`.

>

For example, if your `tp_traverse` function includes:

```c
base->tp_traverse(self, visit, arg)

```

then add:

```c
#if PY_VERSION_HEX >= 0x03090000
    // This was not needed before Python 3.9 (bpo-35810 and bpo-40217)
    if (base->tp_flags & Py_TPFLAGS_HEAPTYPE) {
        // a heap type's tp_traverse already visited Py_TYPE(self)
    } else {
        Py_VISIT(Py_TYPE(self));
    }
#else

```

(Refer to [bpo-35810](https://bugs.python.org/issue?@action=redirect&bpo=35810) and [bpo-40217](https://bugs.python.org/issue?@action=redirect&bpo=40217) for further detail.)

- The functions `PyEval_CallObject`, `PyEval_CallFunction`, `PyEval_CallMethod` and `PyEval_CallObjectWithKeywords` are deprecated. Switch to [`PyObject_Call()`](https://docs.python.org/3.14/c-api/call.html#c.PyObject_Call) and its variants. (Further detail appears in [bpo-29548](https://bugs.python.org/issue?@action=redirect&bpo=29548).)

[Subject index](INDEX.md) · [Previous source section](changes-in-the-python-api.md) · [Next source section](bytecode-migration-changes.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](porting-to-python-3-9.md)
