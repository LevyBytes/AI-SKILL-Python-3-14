# Initialization function

### Initialization function

An extension module's initialization function carries this signature:

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyInit_modulename(void)

The name it bears should be `PyInit_*<name>*`, where `<name>` stands in for the module's own name.

When a module has a name made up only of ASCII characters, the function instead has to be called `PyInit_*<name>*`, again swapping `<name>` for the module's name. With Multi-phase initialization, module names outside ASCII become permissible; in that situation the initialization function goes by `PyInitU_*<name>*`, where `<name>` is run through Python's *punycode* encoding and any hyphens become underscores. Expressed in Python:

```python
def initfunc_name(name):
    try:
        suffix = b'_' + name.encode('ascii')
    except UnicodeEncodeError:
        suffix = b'U_' + name.encode('punycode').replace(b'-', b'_')
    return b'PyInit' + suffix

```

The advised practice is to declare the initialization function through a helper macro:

 PyMODINIT_FUNC

Declares an initialization function for an extension module. What this macro does:

- declares the return type as [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*,

- tacks on whatever special linkage declarations the platform calls for, and

- for C++, declares the function as `extern "C"`.

As an illustration, here is how a module named `spam` would be set up:

```c
static struct PyModuleDef spam_module = {
    .m_base = PyModuleDef_HEAD_INIT,
    .m_name = "spam",
    ...
};

PyMODINIT_FUNC
PyInit_spam(void)
{
    return PyModuleDef_Init(&spam_module);
}

```

You can ship several modules out of one shared library by writing a separate initialization function for each. Importing them, though, calls for symbolic links or a custom importer, since out of the box only the function whose name matches the filename gets located. The [Multiple modules in one library](https://peps.python.org/pep-0489/#multiple-modules-in-one-library) section of [**PEP 489**](https://peps.python.org/pep-0489/) covers the specifics.

As a rule, the initialization function is the lone non-`static` entity declared in the module's C source.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](defining-extension-modules.md) · [Previous source contract](multiple-module-instances.md) · [Following source contract](pymoduledef-init.md)
