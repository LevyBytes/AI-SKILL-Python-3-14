# What’s New in Python 2.0 / Extending/Embedding Changes

### Extending/Embedding Changes

A number of the changes happen beneath the surface and will matter only to those authoring C extension modules or embedding a Python interpreter inside a bigger program. If Python’s C API isn’t part of your work, feel free to skip past this section.

The Python C API’s version number went up, so any C extensions built against 1.5.2 have to be rebuilt before they’ll function with 2.0. On Windows, because of the way Windows DLLs operate, Python 2.0 simply can’t import a third-party extension that was built for Python 1.5.x, so Python throws an exception and the import fails.

Anyone using Jim Fulton’s ExtensionClass module will be glad that hooks now exist so that ExtensionClasses work with [`isinstance()`](https://docs.python.org/3.14/library/functions.html#isinstance) and [`issubclass()`](https://docs.python.org/3.14/library/functions.html#issubclass). That means there’s no longer any need to write code like `if type(obj) == myExtensionClass`; you can instead use the more natural `if isinstance(obj, myExtensionClass)`.

The `Python/importdl.c` file, once a thicket of #ifdefs covering dynamic loading across many platforms, was tidied and restructured by Greg Stein. `importdl.c` is now fairly compact, with the platform-specific portions relocated into a set of `Python/dynload_*.c` files. Another tidy-up: the Include/ directory previously held several `my*.h` files carrying various portability hacks; these have been combined into one file, `Include/pyport.h`.

Vladimir Marangozov’s long-awaited overhaul of malloc finished, making it straightforward to let the Python interpreter run a custom allocator in place of C’s standard `malloc()`. For documentation, read the comments inside `Include/pymem.h` and `Include/objimpl.h`. To follow the extended discussions in which the interface was worked out, browse, over at python.org, the web archives belonging to the ‘patches’ and ‘python-dev’ lists.

Newer releases of the GUSI development environment for MacOS include POSIX threads. As a result Python’s POSIX threading support now functions on the Macintosh. Someone also contributed threading support built on the user-space GNU `pth` library.

Threading on Windows got better too. Windows offers thread locks that fall back on kernel objects only when there’s contention; in the usual no-contention case they rely on lighter-weight functions roughly ten times faster. A threaded build of Python 1.5.2 on NT runs at half the speed of an unthreaded one; after the 2.0 changes that gap shrinks to just 10%. Yakov Markovitch contributed these gains.

Python 2.0’s source has been switched to use only ANSI C prototypes, so building Python now demands an ANSI C compiler and can no longer be carried out with a compiler limited to K&R C.

The Python virtual machine formerly stored 16-bit numbers in its bytecode, which capped how large source files could be. This particularly constrained how big literal lists and dictionaries could grow in Python source; now and then people who generate Python code bumped into the ceiling. A patch from Charles G. Waldman lifts the cap from `2**16` to `2**32`.

Three new convenience functions, meant for inserting constants into a module’s dictionary while the module initializes, were added: [`PyModule_AddObject()`](https://docs.python.org/3.14/c-api/module.html#c.PyModule_AddObject), [`PyModule_AddIntConstant()`](https://docs.python.org/3.14/c-api/module.html#c.PyModule_AddIntConstant), and [`PyModule_AddStringConstant()`](https://docs.python.org/3.14/c-api/module.html#c.PyModule_AddStringConstant). Each takes a module object, a null-terminated C string holding the name to add, and a third argument carrying the value to bind to that name. That third argument is, in order, a Python object, a C long, or a C string.

A wrapper API for Unix-style signal handlers was added. [`PyOS_getsig()`](https://docs.python.org/3.14/c-api/sys.html#c.PyOS_getsig) fetches a signal handler and [`PyOS_setsig()`](https://docs.python.org/3.14/c-api/sys.html#c.PyOS_setsig) installs a fresh one.

[Subject index](INDEX.md) · [Previous source section](porting-to-2-0.md) · [Next source section](distutils-making-modules-easy-to-install.md) · [Release/subject declaration](introduction.md)
