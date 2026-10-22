# Python 3.14.0 alpha 4 / library / ctypes

[gh-128182](https://github.com/python/cpython/issues/128182): Resolved a crash that arose from using [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes) pointers concurrently under the [free threaded](https://docs.python.org/3.14/glossary.html#term-free-threading) build.

[gh-127946](https://github.com/python/cpython/issues/127946): Resolved a crash from altering [`ctypes._CFuncPtr`](https://docs.python.org/3.14/library/ctypes.html#ctypes._CFuncPtr) objects concurrently under the [free threaded](https://docs.python.org/3.14/glossary.html#term-free-threading) build.

[gh-112015](https://github.com/python/cpython/issues/112015): [`ctypes.memoryview_at()`](https://docs.python.org/3.14/library/ctypes.html#ctypes.memoryview_at) now exists for building a [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview) object pointing at the given pointer and length. It behaves like [`ctypes.string_at()`](https://docs.python.org/3.14/library/ctypes.html#ctypes.string_at) yet sidesteps a buffer copy, which tends to help when writing pure Python callback functions that receive dynamically-sized buffers.

[gh-126742](https://github.com/python/cpython/issues/126742): Restored handling of localized error text coming from *[dlerror(3)](https://manpages.debian.org/dlerror(3))* and *[gdbm_strerror](https://manpages.debian.org/gdbm(3))* within [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes) and [`dbm.gnu`](https://docs.python.org/3.14/library/dbm.html#module-dbm.gnu) functions respectively. Bénédikt Tran wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
