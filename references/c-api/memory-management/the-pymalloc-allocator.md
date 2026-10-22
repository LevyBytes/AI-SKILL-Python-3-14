# The pymalloc allocator

### The pymalloc allocator

Python ships a *pymalloc* allocator tuned for short-lived small objects, those of 512 bytes or under. It draws on memory mappings termed “arenas”, each a fixed 256 KiB on 32-bit platforms or 1 MiB on 64-bit platforms. For any request above 512 bytes it defers to `PyMem_RawMalloc()` and `PyMem_RawRealloc()`.

For the `PYMEM_DOMAIN_MEM` domain (say, `PyMem_Malloc()`) and the `PYMEM_DOMAIN_OBJ` domain (say, `PyObject_Malloc()`), *pymalloc* serves as the allocator chosen by default.

For its work, the arena allocator turns to these functions:

- `VirtualAlloc()` and `VirtualFree()` on Windows,

- `mmap()` and `munmap()` if available,

- `malloc()` and `free()` otherwise.

Configuring Python with the [`--without-pymalloc`](https://docs.python.org/3.14/using/configure.html#cmdoption-without-pymalloc) option switches this allocator off. You can also turn it off while the program runs by way of the [`PYTHONMALLOC`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONMALLOC) environment variable (for instance, `PYTHONMALLOC=malloc`).

As a rule, turning the pymalloc allocator off is the sensible move when you build Python alongside AddressSanitizer ([`--with-address-sanitizer`](https://docs.python.org/3.14/using/configure.html#cmdoption-with-address-sanitizer)), since that tool surfaces low-level defects hiding in the C code.

[Subject index](INDEX.md) · [Previous source contract](debug-hooks-on-the-python-memory-allocators.md) · [Following source contract](pyobjectarenaallocator-to-pyobject-setarenaallocator.md)
