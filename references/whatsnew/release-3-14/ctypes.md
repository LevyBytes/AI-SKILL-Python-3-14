# What's new in Python 3.14 / ctypes — ctypes

### ctypes

- How [bit fields](https://docs.python.org/3.14/library/ctypes.html#ctypes-bit-fields-in-structures-unions) get laid out inside [`Structure`](https://docs.python.org/3.14/library/ctypes.html#ctypes.Structure) and [`Union`](https://docs.python.org/3.14/library/ctypes.html#ctypes.Union) objects now lines up more tightly with what each platform defaults to (GCC/Clang or MSVC). Notably, fields stop overlapping. (Contributed by Matthias Görgens in [gh-97702](https://github.com/python/cpython/issues/97702).)

- You may now assign the [`Structure._layout_`](https://docs.python.org/3.14/library/ctypes.html#ctypes.Structure._layout_) class attribute to assist with matching a non-default ABI. (Contributed by Petr Viktorin in [gh-97702](https://github.com/python/cpython/issues/97702).)

- The class behind [`Structure`](https://docs.python.org/3.14/library/ctypes.html#ctypes.Structure)/[`Union`](https://docs.python.org/3.14/library/ctypes.html#ctypes.Union) field descriptors is now reachable as [`CField`](https://docs.python.org/3.14/library/ctypes.html#ctypes.CField), carrying fresh attributes that help with debugging and introspection. (Contributed by Petr Viktorin in [gh-128715](https://github.com/python/cpython/issues/128715).)

- Under Windows, the [`COMError`](https://docs.python.org/3.14/library/ctypes.html#ctypes.COMError) exception has become public. (Contributed by Jun Komoda in [gh-126686](https://github.com/python/cpython/issues/126686).)

- Under Windows, the [`CopyComPointer()`](https://docs.python.org/3.14/library/ctypes.html#ctypes.CopyComPointer) function has become public. (Contributed by Jun Komoda in [gh-127275](https://github.com/python/cpython/issues/127275).)

- The new [`memoryview_at()`](https://docs.python.org/3.14/library/ctypes.html#ctypes.memoryview_at) builds a [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview) object pointing at the pointer and length you supply. Behaving much like [`ctypes.string_at()`](https://docs.python.org/3.14/library/ctypes.html#ctypes.string_at), it skips a buffer copy, which tends to help when you write pure Python callback functions handed dynamically-sized buffers. (Contributed by Rian Hunter in [gh-112018](https://github.com/python/cpython/issues/112018).)

- The complex types [`c_float_complex`](https://docs.python.org/3.14/library/ctypes.html#ctypes.c_float_complex), [`c_double_complex`](https://docs.python.org/3.14/library/ctypes.html#ctypes.c_double_complex), and [`c_longdouble_complex`](https://docs.python.org/3.14/library/ctypes.html#ctypes.c_longdouble_complex) become available provided that the compiler together with the `libffi` library support complex C types. (Contributed by Sergey B Kirpichev in [gh-61103](https://github.com/python/cpython/issues/61103).)

- The new [`ctypes.util.dllist()`](https://docs.python.org/3.14/library/ctypes.html#ctypes.util.dllist) enumerates the shared libraries that the present process has loaded. (Contributed by Brian Ward in [gh-119349](https://github.com/python/cpython/issues/119349).)

- Relocate the [`ctypes.POINTER()`](https://docs.python.org/3.14/library/ctypes.html#ctypes.POINTER) types cache away from one global internal cache (`_pointer_type_cache`) onto the [`_CData.__pointer_type__`](https://docs.python.org/3.14/library/ctypes.html#ctypes._CData.__pointer_type__) attribute belonging to each matching `ctypes` type. Doing so keeps the cache from expanding without bound under certain conditions. (Contributed by Sergey Miryanov in [gh-100926](https://github.com/python/cpython/issues/100926).)

- Subscription now works on the [`py_object`](https://docs.python.org/3.14/library/ctypes.html#ctypes.py_object) type, turning it into a [generic type](https://docs.python.org/3.14/glossary.html#term-generic-type). (Contributed by Brian Schubert in [gh-132168](https://github.com/python/cpython/issues/132168).)

- The `ctypes` module now works with [free-threading builds](https://docs.python.org/3.14/glossary.html#term-free-threading). (Contributed by Kumar Aditya and Peter Bierma in [gh-127945](https://github.com/python/cpython/issues/127945).)

[Subject index](INDEX.md) · [Previous source section](contextvars.md) · [Next source section](curses.md) · [Release/subject declaration](summary-release-highlights.md)
