# ctypes: `ctypes.pointer()`, `ctypes.resize()`, `ctypes.set_errno()`, `ctypes.set_last_error()`, `ctypes.sizeof()`, `ctypes.string_at()`, `ctypes.WinError()`, `ctypes.wstring_at()`, `ctypes.memoryview_at()`

**CPython implementation detail:** Once built, the pointer type is stored under the `__pointer_type__` attribute on *type*. You may assign this attribute ahead of the first `POINTER` invocation to register a custom pointer type. That practice, though, is not recommended: building a proper pointer type by hand is tricky unless you lean on internals that future Python releases might alter.

 ctypes.pointer(*obj*, */*)

Build a fresh pointer instance that refers to *obj*. What comes back has the type `POINTER(type(obj))`.

Note: When all you need is to hand a pointer for an object into a foreign function call, reach for `byref(obj)` instead, since it runs considerably faster.

 ctypes.resize(*obj*, *size*)

This routine changes the size of the internal memory buffer belonging to *obj*, which has to be an instance of a ctypes type. You cannot shrink the buffer below the native size of that object's type, reported by `sizeof(type(obj))`, though growing it larger is allowed.

 ctypes.set_errno(*value*)

Assign *value* to the ctypes-private copy of the system [`errno`](https://docs.python.org/3.14/library/errno.html#module-errno) variable for the calling thread, and hand back whatever the prior value was.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `ctypes.set_errno` with argument `errno`.

 ctypes.set_last_error(*value*)

Assigns *value* to the ctypes-private copy of the system `LastError` variable for the calling thread, and hands back whatever the prior value was.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `ctypes.set_last_error` with argument `error`.

 ctypes.sizeof(*obj_or_type*)

Gives back the byte size of a ctypes type or of an instance's memory buffer. Behaves just like the C `sizeof` operator.

 ctypes.string_at(*ptr*, *size=-1*)

Hand back the byte string located at *void *ptr*. When *size* is provided, that value serves as the size; otherwise the string is treated as zero-terminated.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `ctypes.string_at` with arguments `ptr`, `size`.

 ctypes.WinError(*code=None*, *descr=None*)

Builds an instance of [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError). When *code* is omitted, `GetLastError()` is invoked to obtain the error code. When *descr* is omitted, `FormatError()` is invoked to fetch a text description of the error.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows

Changed in version 3.3: Formerly an instance of [`WindowsError`](https://docs.python.org/3.14/library/exceptions.html#WindowsError) was produced; that is now an alias of [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError).

 ctypes.wstring_at(*ptr*, *size=-1*)

Hand back the wide-character string located at *void *ptr*. When *size* is provided, it serves as the character count of the string; otherwise the string is treated as zero-terminated.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `ctypes.wstring_at` with arguments `ptr`, `size`.

 ctypes.memoryview_at(*ptr*, *size*, *readonly=False*)

Hand back a [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview) object whose length is *size* and which refers to memory beginning at *void *ptr*.

When *readonly* is true, the resulting `memoryview` object cannot serve to alter the underlying memory. (Alterations performed through other channels will still appear in the returned object.)

This routine resembles `string_at()`, the major distinction being that it avoids copying the indicated memory. It offers a semantically equivalent (yet faster) substitute for `memoryview((c_byte * size).from_address(ptr))`. (Although `from_address()` accepts only integers, *ptr* may additionally be supplied as a `ctypes.POINTER` or a `byref()` object.)

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `ctypes.memoryview_at` with arguments `address`, `size`, `readonly`.

Added in version 3.14.

[Subject index](INDEX.md) · [Continue](ctypes-cdata-class.md) · [Owning module, declaration or section: ctypes](ctypes-a-foreign-function-library-for-python.md) · [Owning module, declaration or section: Utility functions](ctypes-addressof-to-ctypes-create-string-buffer.md) · [Owning module, declaration or section: ctypes.POINTER](ctypes-pointer.md) · [Preceding source contract and version conditions](ctypes-pointer.md)
