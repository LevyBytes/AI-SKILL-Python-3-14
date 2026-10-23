# ctypes - Accessing values exported from dlls

### Accessing values exported from dlls

Certain shared libraries export not just functions but variables as well. One such case inside the Python library itself is [`Py_Version`](https://docs.python.org/3.14/c-api/apiabiversion.html#c.Py_Version), the Python runtime version number packed into a single constant integer.

To reach values of this kind, `ctypes` offers the `in_dll()` class methods on the type. *pythonapi* is a built-in symbol that exposes the Python C api:

```python
>>> version = ctypes.c_int.in_dll(ctypes.pythonapi, "Py_Version")
>>> print(hex(version.value))
0x30c00a0

```

A fuller example, one that also shows pointers in action, reaches the [`PyImport_FrozenModules`](https://docs.python.org/3.14/c-api/import.html#c.PyImport_FrozenModules) pointer that Python exports.

From the documentation for that value:

>

At startup this pointer references an array of [`_frozen`](https://docs.python.org/3.14/c-api/import.html#c._frozen) records; the array’s final entry acts as a terminator, with every member set to `NULL` or zero. Importing a frozen module triggers a lookup in this table. Outside code might exploit that mechanism to supply a collection of frozen modules built on the fly.

That makes the pointer potentially handy to tinker with. To keep the example small, we only demonstrate how `ctypes` can read this table:

```python
>>> from ctypes import *
>>>
>>> class struct_frozen(Structure):
...     _fields_ = [("name", c_char_p),
...                 ("code", POINTER(c_ubyte)),
...                 ("size", c_int),
...                 ("get_code", POINTER(c_ubyte)),  # Function pointer
...                ]
...
>>>

```

Having defined the [`_frozen`](https://docs.python.org/3.14/c-api/import.html#c._frozen) data type, we can now fetch the pointer to the table:

```python
>>> FrozenTable = POINTER(struct_frozen)
>>> table = FrozenTable.in_dll(pythonapi, "_PyImport_FrozenBootstrap")
>>>

```

Given that `table` is a `pointer` into the array of `struct_frozen` records, we can walk over it — but we have to guarantee the loop ends, because pointers carry no length. Eventually it would likely blow up with an access violation or similar, so the safer move is to break out the moment we reach the `NULL` entry:

```python
>>> for item in table:
...     if item.name is None:
...         break
...     print(item.name.decode("ascii"), item.size)
...
_frozen_importlib 31764
_frozen_importlib_external 41499
zipimport 12345
>>>

```

It isn’t widely known that the stock Python ships with a frozen module and a frozen package (flagged by the negative `size` member); they exist purely for testing. Give it a spin with `import __hello__`, for instance.

[Subject index](INDEX.md) · [Previous](ctypes-and-we-could-equally-have-written.md) · [Continue](surprises.md) · [Owning module, declaration or section: ctypes](ctypes-a-foreign-function-library-for-python.md)
