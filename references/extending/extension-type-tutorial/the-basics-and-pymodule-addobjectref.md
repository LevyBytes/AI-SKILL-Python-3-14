# The Basics - tp_flags, Py_TPFLAGS_DEFAULT, tp_doc, PyTypeObject, PyDoc_STR, tp_new, PyType_GenericNew, PyType_Ready, PyObject, PyModule_AddObjectRef

```c
.tp_flags = Py_TPFLAGS_DEFAULT,

```

Every type ought to carry this constant among its flags. Doing so switches on all of the members introduced through at least Python 3.3. Should you require more members beyond those, you’ll have to OR in the matching flags.

The type’s doc string is supplied via [`tp_doc`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_doc).

```c
.tp_doc = PyDoc_STR("Custom objects"),

```

So that objects can actually be created, we need to supply a [`tp_new`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_new) handler. That’s the counterpart to Python’s [`__new__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__new__) method, only it must be stated outright. Here we can simply fall back on the stock implementation that the API function [`PyType_GenericNew()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_GenericNew) hands us.

```c
.tp_new = PyType_GenericNew,

```

The rest of the file ought to look familiar, apart from a little code sitting inside `custom_module_exec()`:

```c
if (PyType_Ready(&CustomType) < 0) {
    return -1;
}

```

This readies the `Custom` type, populating several members with their proper defaults, [`ob_type`](https://docs.python.org/3.14/c-api/structures.html#c.PyObject.ob_type) among them, which we had originally left as `NULL`.

```c
if (PyModule_AddObjectRef(m, "Custom", (PyObject *) &CustomType) < 0) {
    return -1;
}

```

That registers the type in the module dictionary. With it in place we can produce `Custom` instances by invoking the `Custom` class:

```pycon
>>> import custom
>>> mycustom = custom.Custom()

```

And we’re done! The only thing left is to compile it; drop the code above into a file named `custom.c`,

```c
[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"

[project]
name = "custom"
version = "1"

```

into a file named `pyproject.toml`, and

```python
from setuptools import Extension, setup
setup(ext_modules=[Extension("custom", ["custom.c"])])

```

into a file named `setup.py`; after that, running

```shell
$ python -m pip install .

```

inside a shell ought to generate a `custom.so` file in a subdirectory and install it; then start up Python — at that point you should be free to `import custom` and experiment with `Custom` objects.

Not too painful, right?

Granted, the `Custom` type as it stands is rather dull. It carries no data and performs no work. You can’t even subclass it.

[Subject index](INDEX.md) · [Previous source section](the-basics-and-pytype-genericnew.md) · [Next source section](adding-data-and-methods-to-the-basic-example.md) · [Owning section and setup](the-basics-and-pymoduledef-init.md)
