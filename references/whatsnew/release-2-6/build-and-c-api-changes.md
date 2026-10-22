# What’s New in Python 2.6 / Build and C API Changes — cmath

### Build and C API Changes

Revisions to Python's build process and to the C API take in:

- A C89 compiler is now required to build Python (after 19 years!). As a result the Python source tree no longer carries its own `memmove()` and `strerror()` implementations, since both belong to the C89 standard library.

- Microsoft Visual Studio 2008 (version 9.0) can now build Python 2.6, and it serves as the new default compiler. The build files sit in the `PCbuild` directory. (Implemented by Christian Heimes.)

- Under Mac OS X, Python 2.6 can be put together as a 4-way universal build. A `--with-universal-archs=[32-bit|64-bit|all]` switch can be handed to the **configure** script, which governs whether the binaries target 32-bit architectures (x86, PowerPC), 64-bit (x86-64 and PPC-64), or both. (Contributed by Ronald Oussoren.)

- Python 2.6.6 introduced a new function, `PySys_SetArgvEx()`, which assigns the value of `sys.argv` and, governed by an *updatepath* parameter, can also extend `sys.path` so that it covers the directory holding the script named in `sys.argv[0]`.

This function arrived to seal a security hole affecting applications that embed Python. The earlier function, `PySys_SetArgv()`, always updated `sys.path`, and on occasion it would tack on the current directory. The upshot: if you launched a Python-embedding application from a directory under someone else's control, an attacker could plant a Trojan-horse module there (say, a file called `os.py`) that your application would then import and execute.

If you look after a C/C++ application that embeds Python, see whether you call `PySys_SetArgv()` and weigh carefully whether the application ought to switch to `PySys_SetArgvEx()` with *updatepath* set to false. Keep in mind that adopting this function breaks compatibility with Python releases 2.6.5 and older; should you need to keep supporting those older releases, you can leave the `PySys_SetArgv()` call as it is and run `PyRun_SimpleString("sys.path.pop(0)\n")` afterward to drop the first `sys.path` entry.

Security issue reported as [**CVE 2008-5983**](https://www.cve.org/CVERecord?id=CVE-2008-5983); discussed in [gh-50003](https://github.com/python/cpython/issues/50003), and fixed by Antoine Pitrou.

- The BerkeleyDB module now exposes a C API object as `bsddb.db.api`. Other C extensions that want to draw on the `bsddb` module for their own ends can make use of this object. (Contributed by Duncan Grisby.)

- The new buffer interface, covered earlier in the PEP 3118 section, brings in [`PyObject_GetBuffer()`](https://docs.python.org/3.14/c-api/buffer.html#c.PyObject_GetBuffer) and [`PyBuffer_Release()`](https://docs.python.org/3.14/c-api/buffer.html#c.PyBuffer_Release), along with a handful of other functions.

- Python's reliance on the C stdio library is now thread-safe — at least to the degree that the underlying library is. There used to be a lurking bug if one thread closed a file object while a second thread was still reading from or writing to it. As of 2.6, file objects carry a reference count, managed through the `PyFile_IncUseCount()` and `PyFile_DecUseCount()` functions. A file object cannot be closed while its reference count stays above zero. Call `PyFile_IncUseCount()` with the GIL still held, ahead of any I/O work that uses the `FILE *` pointer, and call `PyFile_DecUseCount()` immediately once the GIL has been taken back. (Contributed by Antoine Pitrou and Gregory P. Smith.)

- Importing modules at the same time from two separate threads no longer deadlocks; instead it now raises an [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError). A new API function, [`PyImport_ImportModuleNoBlock()`](https://docs.python.org/3.14/c-api/import.html#c.PyImport_ImportModuleNoBlock), first checks `sys.modules` for a module, then tries to import it once it has taken an import lock. Should another thread already hold the import lock, an `ImportError` results. (Contributed by Christian Heimes.)

- A handful of functions report on the platform's floating-point capabilities. [`PyFloat_GetMax()`](https://docs.python.org/3.14/c-api/float.html#c.PyFloat_GetMax) gives the largest representable floating-point value, and [`PyFloat_GetMin()`](https://docs.python.org/3.14/c-api/float.html#c.PyFloat_GetMin) gives the smallest positive one. [`PyFloat_GetInfo()`](https://docs.python.org/3.14/c-api/float.html#c.PyFloat_GetInfo) returns an object holding further details drawn from the `float.h` file, among them `"mant_dig"` (count of digits in the mantissa), `"epsilon"` (the smallest gap between 1.0 and the next-larger representable value), and a number of others. (Contributed by Christian Heimes; [bpo-1534](https://bugs.python.org/issue?@action=redirect&bpo=1534).)

- C functions and methods relying on [`PyComplex_AsCComplex()`](https://docs.python.org/3.14/c-api/complex.html#c.PyComplex_AsCComplex) will now take arguments that supply a `__complex__()` method. Notably, the functions inside the [`cmath`](https://docs.python.org/3.14/library/cmath.html#module-cmath) module will now take objects carrying that method. This backports a Python 3.0 change. (Contributed by Mark Dickinson; [bpo-1675423](https://bugs.python.org/issue?@action=redirect&bpo=1675423).)

- Python's C API now carries two functions for comparing strings case-insensitively, `PyOS_stricmp(char*, char*)` and `PyOS_strnicmp(char*, char*, Py_ssize_t)`. (Contributed by Christian Heimes; [bpo-1635](https://bugs.python.org/issue?@action=redirect&bpo=1635).)

- Plenty of C extensions roll their own small macro for stuffing integers and strings into the module's dictionary within the `init*` function. With Python 2.6 the language finally ships, for the job of putting values into a module, the standard macros [`PyModule_AddStringMacro`](https://docs.python.org/3.14/c-api/module.html#c.PyModule_AddStringMacro) and [`PyModule_AddIntMacro()`](https://docs.python.org/3.14/c-api/module.html#c.PyModule_AddIntMacro). (Contributed by Christian Heimes.)

- A few macros got renamed in both 3.0 and 2.6 to signal more plainly that they are macros and not functions. `Py_Size()` turned into [`Py_SIZE()`](https://docs.python.org/3.14/c-api/structures.html#c.Py_SIZE), `Py_Type()` turned into [`Py_TYPE()`](https://docs.python.org/3.14/c-api/structures.html#c.Py_TYPE), and `Py_Refcnt()` turned into [`Py_REFCNT()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_REFCNT). For backward compatibility the mixed-case spellings remain present in Python 2.6. ([bpo-1629](https://bugs.python.org/issue?@action=redirect&bpo=1629))

- When it runs against a debug build of Python, Distutils now drops the C extensions it compiles into a separate directory. (Contributed by Collin Winter; [bpo-1530959](https://bugs.python.org/issue?@action=redirect&bpo=1530959).)

- A number of basic data types, integers and strings among them, keep internal free lists of objects available for reuse. The data structures backing these free lists now share a naming convention: the variable is always called `free_list`, the counter is always called `numfree`, and a macro `Py<typename>_MAXFREELIST` is always defined.

- A fresh Makefile target, "make patchcheck", readies the Python source tree for producing a patch: it strips trailing whitespace from every modified `.py` file, checks whether the documentation has changed, and reports on whether the `Misc/ACKS` and `Misc/NEWS` files have been brought up to date. (Contributed by Brett Cannon.)

A second new target, "make profile-opt", builds a Python binary with GCC's profile-guided optimization. It first builds Python with profiling switched on, runs the test suite to gather a body of profiling data, and then rebuilds using that data for optimization. (Contributed by Gregory P. Smith.)

[Subject index](INDEX.md) · [Previous source section](deprecations-and-removals.md) · [Next source section](port-specific-changes-windows.md) · [Release/subject declaration](python-3-0.md)
