# Python 3.9.0 alpha 1 / library / ctypes

[bpo-19865](https://bugs.python.org/issue?@action=redirect&bpo=19865): On platforms whose `wchar_t` is 16-bit (Windows and AIX, for instance), [`ctypes.create_unicode_buffer()`](https://docs.python.org/3.14/library/ctypes.html#ctypes.create_unicode_buffer) now copes with non-BMP characters as well.

[bpo-37140](https://bugs.python.org/issue?@action=redirect&bpo=37140): Fixed a ctypes regression in Python 3.8. Whenever a ctypes.Structure was handed by copy to a function, the internals of ctypes built a temporary object, with the side effect of running the structure finalizer (__del__) twice. Python semantics demand that a finalizer run precisely once. The ctypes internals were fixed so the finalizer is no longer run twice.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
