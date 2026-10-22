# What’s New in Python 2.6 / ctypes Enhancements — ctypes

### ctypes Enhancements

Thomas Heller kept up his maintenance and refinement of the [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes) module.

A `c_bool` datatype, mirroring the C99 `bool` type, is now available in [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes). (Contributed by David Remahl; [bpo-1649190](https://bugs.python.org/issue?@action=redirect&bpo=1649190).)

The string, buffer and array types in [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes) handle extended slicing syntax better now, accepting assorted mixes of `(start, stop, step)`. (Implemented by Thomas Wouters.)

Every [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes) data type now offers `from_buffer()` and `from_buffer_copy()` methods, which build a ctypes instance out of a buffer object you pass in. Where `from_buffer_copy()` duplicates the object's contents, `from_buffer()` shares the very same block of memory.

There is a new calling convention that instructs [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes) to reset the `errno` or Win32 LastError variables before each wrapped call begins. (Implemented by Thomas Heller; [bpo-1798](https://bugs.python.org/issue?@action=redirect&bpo=1798).)

The Unix `errno` variable can now be read back after a function call. While building a wrapped function, pass `use_errno=True` as a keyword parameter to the `DLL()` function, then reach for the module-level methods `set_errno()` and `get_errno()` to write and read the error value.

A parallel arrangement covers the Win32 LastError variable through the `DLL()`, `OleDLL()`, and `WinDLL()` functions. Pass `use_last_error=True` as a keyword parameter, then call the module-level methods `set_last_error()` and `get_last_error()`.

The `byref()` function, which obtains a pointer to a ctypes instance, has picked up an optional *offset* parameter — a byte count tacked onto the pointer that comes back.

[Subject index](INDEX.md) · [Previous source section](the-plistlib-module-a-property-list-parser.md) · [Next source section](improved-ssl-support.md) · [Release/subject declaration](python-3-0.md)
