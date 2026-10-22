# ctypes / Loading shared libraries: `ctypes.LibraryLoader`, `LoadLibrary()`

*class *ctypes.LibraryLoader(*dlltype*)

A class that loads shared libraries. *dlltype* ought to be one of the `CDLL`, `PyDLL`, `WinDLL`, or `OleDLL` types.

`__getattr__()` behaves specially: accessing it as an attribute of a library loader instance loads the corresponding shared library. That outcome is cached, so each later attribute access hands back the identical library.

 LoadLibrary(*name*)

Bring a shared library into the process and return it. A brand-new instance of the library is returned by this method every time.

The following ready-made library loaders exist:

[Subject index](INDEX.md) · [Previous](ctypes-rtld-global-to-ctypes-default-mode.md) · [Continue](ctypes-cdll-to-ctypes-pythonapi.md) · [Owning module, declaration or section: ctypes](ctypes-a-foreign-function-library-for-python.md) · [Owning module, declaration or section: Loading shared libraries](ctypes-cdll-class.md)
