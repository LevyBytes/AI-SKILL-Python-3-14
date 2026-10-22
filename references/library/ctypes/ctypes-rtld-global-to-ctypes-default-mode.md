# ctypes: `ctypes.RTLD_GLOBAL`, `ctypes.RTLD_LOCAL`, `ctypes.DEFAULT_MODE`

ctypes.RTLD_GLOBAL

A flag intended for the *mode* parameter. Where a platform lacks this flag, it takes the integer zero as its definition.

 ctypes.RTLD_LOCAL

A flag intended for the *mode* parameter. Where a platform lacks it, the flag matches *RTLD_GLOBAL*.

 ctypes.DEFAULT_MODE

The mode applied by default when loading shared libraries. Under OSX 10.3 it equals *RTLD_GLOBAL*; elsewhere it matches *RTLD_LOCAL*.

You can also load shared libraries via one of the ready-made objects, which are instances of the `LibraryLoader` class, whether by invoking the `LoadLibrary()` method or by reading the library as an attribute of the loader instance.

[Subject index](INDEX.md) · [Previous](ctypes-pydll-class.md) · [Continue](shared-library-loader.md) · [Owning module, declaration or section: ctypes](ctypes-a-foreign-function-library-for-python.md) · [Owning module, declaration or section: Loading shared libraries](ctypes-cdll-class.md)
