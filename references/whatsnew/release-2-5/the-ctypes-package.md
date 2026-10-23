# What's New in Python 2.5 / The ctypes package - ctypes

### The ctypes package

The [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes) package, the work of Thomas Heller, is now part of the standard library. With `ctypes` you can invoke arbitrary functions living in shared libraries or DLLs. Veteran users might recall the `dl` module, which supplied functions for loading shared libraries and calling into them. By comparison, the `ctypes` package is considerably more capable.

Loading a shared library or DLL means constructing an instance of the `CDLL` class and handing it the name or path of that shared library or DLL. After that, you reach arbitrary functions by treating them as attributes on the `CDLL` object.

```python
import ctypes

libc = ctypes.CDLL('libc.so.6')
result = libc.printf("Line of output\n")

```

The various C types come with their own type constructors: `c_int()`, `c_float()`, `c_double()`, `c_char_p()` (the equivalent of char*), and others. In contrast to Python's own types, every C counterpart is mutable; you change the wrapped value by assigning to its `value` attribute. Python integers and strings are converted to the matching C types for you, yet for the remaining types you have to invoke the appropriate type constructor. (And I do mean *must*; a mistake here will frequently crash the interpreter with a segmentation fault.)

Avoid passing a Python string to `c_char_p()` whenever the C function intends to alter that memory region, since Python strings are meant to stay immutable; ignoring this will produce baffling bugs. Whenever you require a writable memory region, reach for `create_string_buffer()`:

```python
s = "this is a string"
buf = ctypes.create_string_buffer(s)
libc.strfry(buf)

```

By default C functions are taken to return integers, but you can override that by setting the function object's `restype` attribute:

```python
>>> libc.atof('2.71828')
-1783957616
>>> libc.atof.restype = ctypes.c_double
>>> libc.atof('2.71828')
2.71828

```

[`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes) additionally exposes a wrapper around Python's C API via the `ctypes.pythonapi` object. That object does *not* drop the global interpreter lock before a call, since the lock has to remain held whenever interpreter code is entered. A [`py_object`](https://docs.python.org/3.14/library/ctypes.html#ctypes.py_object) type constructor is available for building a [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)* pointer. A minimal example:

```python
import ctypes

d = {}
ctypes.pythonapi.PyObject_SetItem(ctypes.py_object(d),
          ctypes.py_object("abc"),  ctypes.py_object(1))
# d is now {'abc', 1}.

```

Remember to apply [`py_object()`](https://docs.python.org/3.14/library/ctypes.html#ctypes.py_object); leave it out and a segmentation fault is what you'll get.

[`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes) has existed for some time, yet people kept authoring and shipping hand-coded extension modules because there was no guarantee `ctypes` would be available. Maybe now that `ctypes` ships with core Python, developers will start writing Python wrappers over a library reached through `ctypes` rather than building extension modules.

See also

[https://web.archive.org/web/20180410025338/http://starship.python.net/crew/theller/ctypes/](https://web.archive.org/web/20180410025338/http://starship.python.net/crew/theller/ctypes/)

The pre-stdlib ctypes web page, with a tutorial, reference, and FAQ.

The documentation for the [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes) module.

[Subject index](INDEX.md) · [Previous source section](weakref-and-archive-module-changes.md) · [Next source section](the-elementtree-package.md) · [Release/subject declaration](pep-308-conditional-expressions.md)
