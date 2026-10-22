# ctypes: `ctypes.PyDLL`

*class *ctypes.PyDLL

Refer to the superclass `CDLL` for shared details.

Calling a function from this library leaves the Python GIL held throughout the call, and once the function finishes the Python error flag gets inspected. When that flag is set, a Python exception is raised.

For that reason, this is handy only for invoking Python C API functions directly.

[Subject index](INDEX.md) · [Previous](ctypes-windll-class.md) · [Continue](ctypes-rtld-global-to-ctypes-default-mode.md) · [Owning module, declaration or section: ctypes](ctypes-a-foreign-function-library-for-python.md) · [Owning module, declaration or section: Loading shared libraries](ctypes-cdll-class.md)
