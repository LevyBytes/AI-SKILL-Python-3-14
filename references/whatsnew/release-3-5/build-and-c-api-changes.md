# What’s New In Python 3.5 / Build and C API Changes

### Build and C API Changes

The following `calloc` functions were introduced:

- [`PyMem_RawCalloc()`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_RawCalloc),

- [`PyMem_Calloc()`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_Calloc),

- [`PyObject_Calloc()`](https://docs.python.org/3.14/c-api/memory.html#c.PyObject_Calloc).

(Contributed by Victor Stinner in [bpo-21233](https://bugs.python.org/issue?@action=redirect&bpo=21233).)

Helper functions for encoding and decoding were added:

- [`Py_DecodeLocale()`](https://docs.python.org/3.14/c-api/sys.html#c.Py_DecodeLocale) (replaced `_Py_char2wchar()`),

- [`Py_EncodeLocale()`](https://docs.python.org/3.14/c-api/sys.html#c.Py_EncodeLocale) (replaced `_Py_wchar2char()`).

(Contributed by Victor Stinner in [bpo-18395](https://bugs.python.org/issue?@action=redirect&bpo=18395).)

The added [`PyCodec_NameReplaceErrors()`](https://docs.python.org/3.14/c-api/codec.html#c.PyCodec_NameReplaceErrors) function swaps a unicode encode error out for `\N{...}` escapes. (Contributed by Serhiy Storchaka in [bpo-19676](https://bugs.python.org/issue?@action=redirect&bpo=19676).)

There is now a [`PyErr_FormatV()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_FormatV) function that mirrors [`PyErr_Format()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Format) yet takes a `va_list` argument. (Contributed by Antoine Pitrou in [bpo-18711](https://bugs.python.org/issue?@action=redirect&bpo=18711).)

An added [`PyExc_RecursionError`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyExc_RecursionError) exception. (Contributed by Georg Brandl in [bpo-19235](https://bugs.python.org/issue?@action=redirect&bpo=19235).)

The added [`PyModule_FromDefAndSpec()`](https://docs.python.org/3.14/c-api/module.html#c.PyModule_FromDefAndSpec), [`PyModule_FromDefAndSpec2()`](https://docs.python.org/3.14/c-api/module.html#c.PyModule_FromDefAndSpec2), and [`PyModule_ExecDef()`](https://docs.python.org/3.14/c-api/module.html#c.PyModule_ExecDef) functions came from [**PEP 489**](https://peps.python.org/pep-0489/) — multi-phase extension module initialization. (Contributed by Petr Viktorin in [bpo-24268](https://bugs.python.org/issue?@action=redirect&bpo=24268).)

The added [`PyNumber_MatrixMultiply()`](https://docs.python.org/3.14/c-api/number.html#c.PyNumber_MatrixMultiply) and [`PyNumber_InPlaceMatrixMultiply()`](https://docs.python.org/3.14/c-api/number.html#c.PyNumber_InPlaceMatrixMultiply) functions carry out matrix multiplication. (Contributed by Benjamin Peterson in [bpo-21176](https://bugs.python.org/issue?@action=redirect&bpo=21176). See also [**PEP 465**](https://peps.python.org/pep-0465/) for details.)

The stable ABI now contains the [`PyTypeObject.tp_finalize`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_finalize) slot.

Building on Windows now demands Microsoft Visual C++ 14.0, shipped within [Visual Studio 2015](https://visualstudio.microsoft.com/en/vs/older-downloads/#visual-studio-2015-and-other-products).

On certain platforms, the filenames of extension modules now carry a platform information tag (this tag is optional, and CPython will load extensions lacking it, though when the tag is present yet mismatched the extension won't be loaded):

- Under Linux, the filenames of extension modules close with `.cpython-<major><minor>m-<architecture>-<os>.pyd`:

  - `<major>` holds the Python release's major number; under Python 3.5 that value is `3`.

  - `<minor>` holds the Python release's minor number; under Python 3.5 that value is `5`.

  - `<architecture>` denotes the hardware architecture the extension module was compiled to run on. Usually that's `i386` for 32-bit Intel machines or `x86_64` for 64-bit Intel (and AMD) machines.

  - `<os>` always reads `linux-gnu`, save for extensions compiled against the 32-bit ABI atop 64-bit hosts, where it instead reads `linux-gnu32` (with `<architecture>` reading `x86_64`).

- Under Windows, the filenames of extension modules close with `<debug>.cp<major><minor>-<platform>.pyd`:

  - `<major>` holds the Python release's major number; under Python 3.5 that value is `3`.

  - `<minor>` holds the Python release's minor number; under Python 3.5 that value is `5`.

  - `<platform>` names the platform the extension module targeted: `win32` covers Win32, `win_amd64` covers Win64, `win_ia64` covers Windows Itanium 64, while `win_arm` covers Windows running on ARM.

  -

When compiled under debug mode, `<debug>` becomes `_d`, and is otherwise empty.

- Under OS X platforms, the filenames of extension modules now close with `-darwin.so`.

- Across every remaining platform, the filenames of extension modules match what Python 3.4 produced.

[Subject index](INDEX.md) · [Previous source section](optimizations.md) · [Release/subject declaration](summary-release-highlights.md) · [Next source section](new-keywords.md)
