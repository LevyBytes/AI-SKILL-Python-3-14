# ctypes._CFuncPtr: Foreign-function restype, argtypes and errcheck contracts

restype

Set a ctypes type here to declare what result type the foreign function yields. Supply `None` for void, that is, a function that returns nothing.

You may instead assign a callable Python object that is not a ctypes type; the function is then presumed to return a C int, and the callable receives that integer, which permits extra processing or error checking. This usage is deprecated; for more flexible post processing or error checking, assign a ctypes data type to `restype` and put a callable on the `errcheck` attribute.

 argtypes

Assign a tuple of ctypes types to declare the argument types the function takes. Functions on the `stdcall` calling convention may be called only with as many arguments as this tuple is long; functions on the C calling convention also tolerate extra, unspecified arguments.

When a foreign function is called, every actual argument is handed to the `from_param()` class method of the corresponding items in the `argtypes` tuple, a method that adapts the actual argument into an object the foreign function will accept. For instance, a `c_char_p` item in the `argtypes` tuple converts a string supplied as an argument into a bytes object following ctypes conversion rules.

New: You can now place items in argtypes that are not ctypes types, provided each item carries a `from_param()` method returning a value usable as an argument (integer, string, ctypes instance). This makes it possible to define adapters that turn custom objects into function parameters.

 errcheck

Set a Python function or another callable on this attribute. That callable gets called with three or more arguments:

 callable(*result*, *func*, *arguments*)

*result* is the foreign function's return value, as the `restype` attribute specifies.

*func* is the foreign function object as such; this lets one callable object be reused to check or post process several functions' results.

*arguments* is a tuple holding the parameters first passed to the function call; this lets the behavior be tailored to the arguments in use.

Whatever this function returns becomes the return value of the foreign function call, yet it may also examine the result and raise an exception should the foreign function call have failed.

On Windows, if a foreign function call triggers a system exception (for instance, from an access violation), it is intercepted and swapped for an appropriate Python exception. Additionally, an auditing event `ctypes.set_exception` with argument `code` is raised, letting an audit hook substitute its own exception.

Certain approaches to invoking foreign function calls, along with some of this module's functions, may raise an auditing event `ctypes.call_function` with arguments `function pointer` and `arguments`.

[Subject index](INDEX.md) · [Previous](ctypes-cfuncptr-class.md) · [Continue](ctypes-cfunctype-to-prototype.md) · [Owning module, declaration or section: ctypes](ctypes-a-foreign-function-library-for-python.md) · [Owning module, declaration or section: ctypes._CFuncPtr](ctypes-cfuncptr-class.md) · [Owning module, declaration or section: Foreign functions](ctypes-cfuncptr-class.md)
