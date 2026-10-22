# ctypes: `ctypes.cdll`, `ctypes.windll`, `ctypes.oledll`, `ctypes.pydll`, `ctypes.pythonapi`

ctypes.cdll

Produces `CDLL` instances.

 ctypes.windll

Produces `WinDLL` instances.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows

 ctypes.oledll

Produces `OleDLL` instances.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows

 ctypes.pydll

Produces `PyDLL` instances.

For working with the C Python api directly, there is a prebuilt Python shared library object on hand:

 ctypes.pythonapi

An instance of `PyDLL` that surfaces Python C API functions as attributes. Keep in mind that every one of these functions is presumed to return C int, which naturally is not always so, meaning you must set the right `restype` attribute before using them.

Whenever a library is loaded by way of one of these objects, an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `ctypes.dlopen` fires, carrying the string argument `name` — the name with which the library was loaded.

Reaching a function on an already-loaded library fires an auditing event `ctypes.dlsym` whose arguments are `library` (that library's object) and `name` (a string or integer giving the symbol’s name).

Where you hold only the library handle and not the object, reaching a function fires an auditing event `ctypes.dlsym/handle` whose arguments are `handle` (the raw library handle) and `name`.

[Subject index](INDEX.md) · [Previous](shared-library-loader.md) · [Continue](ctypes-cfuncptr-class.md) · [Owning module, declaration or section: ctypes](ctypes-a-foreign-function-library-for-python.md) · [Owning module, declaration or section: Loading shared libraries](ctypes-cdll-class.md)
