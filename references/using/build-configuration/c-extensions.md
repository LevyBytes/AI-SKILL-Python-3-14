# 3.4.4. C extensions

### 3.4.4. C extensions

A number of C extensions, the `sys` module among them, are compiled as built-in modules. They get built with the `Py_BUILD_CORE_BUILTIN` macro defined. Built-in modules carry no `__file__` attribute:

```pycon
>>> import sys
>>> sys
<module 'sys' (built-in)>
>>> sys.__file__
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'sys' has no attribute '__file__'

```

Other C extensions, such as the `_asyncio` module, are compiled as dynamic libraries instead. They get built with the `Py_BUILD_CORE_MODULE` macro defined. Here is an example on Linux x86-64:

```pycon
>>> import _asyncio
>>> _asyncio
<module '_asyncio' from '/usr/lib64/python3.9/lib-dynload/_asyncio.cpython-39-x86_64-linux-gnu.so'>
>>> _asyncio.__file__
'/usr/lib64/python3.9/lib-dynload/_asyncio.cpython-39-x86_64-linux-gnu.so'

```

`Modules/Setup` drives the generation of Makefile targets that build C extensions. Toward the top of the file, C extensions are compiled as built-in modules. Any extension listed past the `*shared*` marker is compiled as a dynamic library.

How the `PyAPI_FUNC()`, `PyAPI_DATA()` and [`PyMODINIT_FUNC`](https://docs.python.org/3.14/c-api/extension-modules.html#c.PyMODINIT_FUNC) macros in `Include/exports.h` are defined turns on whether the `Py_BUILD_CORE_MODULE` macro is defined:

- Use `Py_EXPORTED_SYMBOL` whenever `Py_BUILD_CORE_MODULE` is defined

- Otherwise use `Py_IMPORTED_SYMBOL`.

Should the `Py_BUILD_CORE_BUILTIN` macro be applied by accident to a C extension compiled as a shared library, that extension's `PyInit_*xxx*()` function goes unexported, which raises an [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError) at import time.

[Subject index](INDEX.md) · [Previous source section](make-regen-all.md) · [Following source section](compiler-and-linker-flags.md)
