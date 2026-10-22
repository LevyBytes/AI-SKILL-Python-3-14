# ctypes: Fundamental ctypes instance values

value

This attribute holds the instance's actual value. With integer and pointer types it is an integer; with character types it is a single-character bytes object or string; with character pointer types it is a Python bytes object or string.

Fetching the `value` attribute from a ctypes instance usually yields a freshly built object each time. `ctypes` does *not* perform original object return; a new object is always created. This holds for every other ctypes object instance as well.

Every subclass carries a class attribute:

 _type_

Class attribute holding an internal type code as a single-character string. Refer to Fundamental data types for a summary.

Types flagged * in the summary can be (or always are) aliases of some other `_SimpleCData` subclass, and may not use the type code shown. As an example, when the platform's long, long long and time_t C types coincide, then `c_long`, `c_longlong` and `c_time_t` all point at one class, `c_long`, whose `_type_` code is `'l'`. The `'L'` code then goes unused.

See also

The [`array`](https://docs.python.org/3.14/library/array.html#module-array) and [struct](https://docs.python.org/3.14/library/struct.html#format-characters) modules, plus third-party modules such as [numpy](https://numpy.org/doc/stable/reference/arrays.interface.html#object.__array_interface__), employ comparable – though slightly different – type codes.

Fundamental data types are quietly converted into native Python types when they come back as foreign function call results or, for instance, when you fetch structure field members or array items. Put differently, when a foreign function's `restype` is `c_char_p`, you always get a Python bytes object, *not* a `c_char_p` instance.

Subclasses of fundamental data types do *not* pick up this behavior. Thus, when a foreign function's `restype` is a subclass of `c_void_p`, the call gives you an instance of that subclass. You can, naturally, retrieve the pointer's value through the `value` attribute.

These are the fundamental ctypes data types:

[Subject index](INDEX.md) · [Previous](ctypes-simplecdata-class.md) · [Continue](ctypes-c-byte-class.md) · [Owning module, declaration or section: ctypes](ctypes-a-foreign-function-library-for-python.md) · [Owning module, declaration or section: ctypes._SimpleCData](ctypes-simplecdata-class.md) · [Owning module, declaration or section: Fundamental data types](ctypes-simplecdata-class.md)
