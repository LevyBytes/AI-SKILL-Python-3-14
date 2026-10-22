# ctypes: Unicode buffers, library lookup, errors and raw memory operations

ctypes.create_unicode_buffer(*init*, *size=None*)

 ctypes.create_unicode_buffer(*size*)

This function builds a mutable unicode character buffer. What it returns is a ctypes array of `c_wchar`.

It accepts the same arguments as `create_string_buffer()`, save that *init* has to be a string and *size* is measured in `c_wchar`.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `ctypes.create_unicode_buffer` with arguments `init`, `size`.

 ctypes.DllCanUnloadNow()

This function is a hook that makes it possible to build in-process COM servers with ctypes. The `_ctypes` extension dll exports a DllCanUnloadNow function from which it is invoked.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows

 ctypes.DllGetClassObject()

This function is a hook that makes it possible to build in-process COM servers with ctypes. The `_ctypes` extension dll exports a DllGetClassObject function from which it is invoked.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows

 ctypes.util.find_library(*name*)

Attempt to locate a library and give back a pathname. *name* is the library name stripped of any prefix such as `lib`, suffix such as `.so`, `.dylib`, or version number (the form taken by the posix linker option `-l`). When no library turns up, `None` comes back.

What it actually does varies by system.

Consult Finding shared libraries for the full documentation.

 ctypes.util.find_msvcrt()

Gives back the filename of the VC runtime library that Python and the extension modules rely on. Should that library's name be undeterminable, `None` comes back.

When you must free memory, say, memory allocated by an extension module through a call to `free(void *)`, it matters that you call the function from the same library that allocated that memory.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows

 ctypes.util.dllist()

Attempt to supply a list of the paths of shared libraries loaded into the present process. Those paths get no normalization or processing of any kind. Should the underlying platform APIs fail, the function may raise [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError). What it actually does varies by system.

Across most platforms, the list's first element stands for the current executable file. That element may be an empty string.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows, macOS, iOS, glibc, BSD libc, musl

Added in version 3.14.

 ctypes.FormatError([*code*])

Hands back a text description for the error code *code*. When no error code is given, the last error code is obtained via a call to the Windows API function `GetLastError()`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows

 ctypes.GetLastError()

Hands back the most recent error code that Windows set within the calling thread. The function invokes the Windows `GetLastError()` function directly; it does not give back the ctypes-private copy of the error code.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows

 ctypes.get_errno()

Hands back the present value held by the ctypes-private copy of the system [`errno`](https://docs.python.org/3.14/library/errno.html#module-errno) variable within the calling thread.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `ctypes.get_errno` with no arguments.

 ctypes.get_last_error()

Hands back the present value held by the ctypes-private copy of the system `LastError` variable within the calling thread.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `ctypes.get_last_error` with no arguments.

 ctypes.memmove(*dst*, *src*, *count*)

Behaves like the standard C memmove library function: it copies *count* bytes out of *src* into *dst*. Both *dst* and *src* have to be integers or ctypes instances convertible to pointers.

 ctypes.memset(*dst*, *c*, *count*)

Behaves like the standard C memset library function: it fills the memory block at address *dst* with *count* bytes whose value is *c*. *dst* has to be either an integer naming an address or a ctypes instance.

[Subject index](INDEX.md) · [Previous](ctypes-addressof-to-ctypes-create-string-buffer.md) · [Continue](ctypes-pointer.md) · [Owning module, declaration or section: ctypes](ctypes-a-foreign-function-library-for-python.md) · [Owning module, declaration or section: Utility functions](ctypes-addressof-to-ctypes-create-string-buffer.md)
