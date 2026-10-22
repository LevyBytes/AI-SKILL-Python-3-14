# ctypes: `ctypes._CFuncPtr`

### Foreign functions

As the prior section described, foreign functions are reachable as attributes of loaded shared libraries. By default the function objects produced this way take any quantity of arguments, accept any ctypes data instances as those arguments, and yield the default result type that the library loader declares.

Each one is an instance of the private local class `_FuncPtr` (which `ctypes` does not expose), a subclass of the private `_CFuncPtr` class:

```pycon
>>> import ctypes
>>> lib = ctypes.CDLL(None)
>>> issubclass(lib._FuncPtr, ctypes._CFuncPtr)
True
>>> lib._FuncPtr is ctypes._CFuncPtr
False

```

 *class *ctypes._CFuncPtr

The base class for foreign functions that C can call.

Foreign function instances are themselves C compatible data types; they stand for C function pointers.

You can tailor this behavior by setting special attributes on the foreign function object.

[Subject index](INDEX.md) · [Previous](ctypes-cdll-to-ctypes-pythonapi.md) · [Continue](ctypes-cfuncptr-callable.md) · [Owning module, declaration or section: ctypes](ctypes-a-foreign-function-library-for-python.md)
