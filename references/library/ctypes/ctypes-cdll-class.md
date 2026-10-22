# ctypes: `ctypes.CDLL`

### Loading shared libraries

You have a handful of options for pulling shared libraries into the Python process. One option is to create an instance of `CDLL` or one of its subclasses:

 *class *ctypes.CDLL(*name*, *mode=DEFAULT_MODE*, *handle=None*, *use_errno=False*, *use_last_error=False*, *winmode=None*)

Represents a loaded shared library.

The functions in such a library follow the standard C calling convention and are presumed to return int. Python’s [global interpreter lock](https://docs.python.org/3.14/glossary.html#term-global-interpreter-lock) is dropped before any function these libraries export is called, then taken back up afterward. When you need different function behavior, turn to a subclass: `OleDLL`, `WinDLL`, or `PyDLL`.

When you already hold a `handle` to a shared library that’s been loaded, you can pass it as the *handle* argument so the open library gets wrapped inside a new `CDLL` object. There, *name* serves only to populate the `_name` attribute, though it may be tweaked and/or validated.

When *handle* is `None`, the platform’s own *[dlopen(3)](https://manpages.debian.org/dlopen(3))* or `LoadLibrary()` function does the work of loading the library into the process and obtaining a handle for it.

*name* is the pathname of the shared library you want to open. If *name* carries no path separator, the library gets located in a platform-specific manner.

On systems that aren’t Windows, *name* may be `None`. Then `dlopen()` runs with `NULL`, which opens the main program as a “library”. (A few systems behave the same way when *name* is empty; passing `None`/`NULL` is the more portable choice.)

CPython implementation detail

Because CPython is linked against `libc`, passing a `None` *name* is a common trick for reaching the C standard library:

```python
>>> printf = ctypes.CDLL(None).printf
>>> printf.argtypes = [ctypes.c_char_p]
>>> printf(b"hello\n")
hello
6

```

When you want the Python C API, favor `ctypes.pythonapi`, which behaves consistently across platforms.

The *mode* parameter lets you dictate how the library gets loaded; the *[dlopen(3)](https://manpages.debian.org/dlopen(3))* manpage spells out the specifics. On Windows, *mode* has no effect. On posix systems, RTLD_NOW is always tacked on and cannot be configured.

Setting the *use_errno* parameter to true switches on a ctypes facility that lets you reach the system [`errno`](https://docs.python.org/3.14/library/errno.html#module-errno) error number safely. `ctypes` keeps a thread-local copy of the system’s `errno` variable; whenever you call foreign functions built with `use_errno=True`, the `errno` value present before the call is exchanged with the private ctypes copy, and the same swap happens again right after the call returns.

The `ctypes.get_errno()` function reports the value held in the private ctypes copy, while the `ctypes.set_errno()` function sets that private ctypes copy to a fresh value and gives back the previous one.

[Subject index](INDEX.md) · [Previous](listing-loaded-shared-libraries.md) · [Owning module, declaration or section: ctypes](ctypes-a-foreign-function-library-for-python.md) · [Required continuation of the source contract](loading-shared-libraries.md)
