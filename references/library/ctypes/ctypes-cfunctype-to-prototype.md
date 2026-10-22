# ctypes — Function prototypes

### Function prototypes

Another way to create foreign functions is by instantiating function prototypes. Function prototypes resemble function prototypes in C; they characterize a function (return type, argument types, calling convention) without supplying an implementation. You call the factory functions with the wanted result type and the function's argument types, and you can employ them as decorator factories, applying them to functions via the `@wrapper` syntax. Consult Callback functions for examples.

 ctypes.CFUNCTYPE(*restype*, **argtypes*, *use_errno=False*, *use_last_error=False*)

The function prototype returned builds functions using the standard C calling convention. During the call the function releases the GIL. With *use_errno* set to true, the ctypes private copy of the system [`errno`](https://docs.python.org/3.14/library/errno.html#module-errno) variable is swapped with the real `errno` value both before and after the call; *use_last_error* performs the same swap for the Windows error code.

 ctypes.WINFUNCTYPE(*restype*, **argtypes*, *use_errno=False*, *use_last_error=False*)

The function prototype returned builds functions using the `stdcall` calling convention. During the call the function releases the GIL. *use_errno* and *use_last_error* carry the same meaning as above.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows

 ctypes.PYFUNCTYPE(*restype*, **argtypes*)

The function prototype returned builds functions using the Python calling convention. The function does *not* release the GIL during the call.

Function prototypes produced by these factory functions can be instantiated in several ways, governed by the type and count of the parameters supplied in the call:

 prototype(*address*)

Hands back a foreign function located at the given address, which has to be an integer.

 prototype(*callable*)

Builds a C callable function (a callback function) out of a Python *callable*.

 prototype(*func_spec*[, *paramflags*])

Hands back a foreign function that a shared library exports. *func_spec* must be a 2-tuple `(name_or_ordinal, library)`. Its first item is the exported function's name as a string, or that function's ordinal as a small integer. Its second item is the shared library instance.

[Subject index](INDEX.md) · [Previous](ctypes-cfuncptr-callable.md) · [Continue](prototype.md) · [Owning module, declaration or section: ctypes](ctypes-a-foreign-function-library-for-python.md)
