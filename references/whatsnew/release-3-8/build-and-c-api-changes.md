# What’s New In Python 3.8 / Build and C API Changes - decimal, fractions, sys

### Build and C API Changes

- The default value of [`sys.abiflags`](https://docs.python.org/3.14/library/sys.html#sys.abiflags) is now an empty string: with builds using or omitting pymalloc being ABI compatible, the `m` flag for pymalloc no longer served any purpose and was dropped. (Contributed by Victor Stinner in [bpo-36707](https://bugs.python.org/issue?@action=redirect&bpo=36707).)

Example of changes:

  - Only the `python3.8` program gets installed; `python3.8m` is no longer present.

  - Only the `python3.8-config` script gets installed; `python3.8m-config` is no longer present.

  - From the suffix of dynamic library filenames, the `m` flag is gone: this affects extension modules shipped in the standard library plus those that third-party packages build and install, such as anything pulled from PyPI. To illustrate on Linux, the Python 3.7 suffix `.cpython-37m-x86_64-linux-gnu.so` turned into `.cpython-38-x86_64-linux-gnu.so` under Python 3.8.

- To draw clearer lines between the different categories of APIs, the header files were reorganized:

  - `Include/*.h` should be the portable public stable C API.

  - `Include/cpython/*.h` is meant to hold the unstable, CPython-specific C API: a public API alongside a bit of private API carrying the `_Py` or `_PY` prefix.

  - `Include/internal/*.h` holds the private internal C API that is highly particular to CPython. No backward compatibility guarantee accompanies this API, and it should stay unused beyond CPython. Its exposure serves narrow purposes only, such as debuggers and profiles that must reach CPython internals without going through function calls. From now on `make install` installs this API.

(Authored by Victor Stinner under [bpo-35134](https://bugs.python.org/issue?@action=redirect&bpo=35134) plus [bpo-35081](https://bugs.python.org/issue?@action=redirect&bpo=35081); the effort was begun by Eric Snow back in Python 3.7.)

- A number of macros were turned into static inline functions: their parameter types and return type are now well defined, the issues that are particular to macros disappear, and their variables hold local scopes. Examples:

  - [`Py_INCREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_INCREF), [`Py_DECREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_DECREF)

  - [`Py_XINCREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_XINCREF), [`Py_XDECREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_XDECREF)

  - `PyObject_INIT`, `PyObject_INIT_VAR`

  - Private functions: `_PyObject_GC_TRACK()`, `_PyObject_GC_UNTRACK()`, `_Py_Dealloc()`

(Contributed by Victor Stinner in [bpo-35059](https://bugs.python.org/issue?@action=redirect&bpo=35059).)

- The `PyByteArray_Init()` and `PyByteArray_Fini()` functions have been removed. Doing nothing since Python 2.7.4 and Python 3.2.0, left out of the limited API (stable ABI), and never documented, they were dropped. (Contributed by Victor Stinner in [bpo-35713](https://bugs.python.org/issue?@action=redirect&bpo=35713).)

- What [`PyExceptionClass_Name()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyExceptionClass_Name) returns now carries the type `const char *` instead of `char *`. (Contributed by Serhiy Storchaka in [bpo-33818](https://bugs.python.org/issue?@action=redirect&bpo=33818).)

- The pairing of `Modules/Setup.dist` and `Modules/Setup` has been removed. Formerly, while updating the CPython source tree, you had to copy `Modules/Setup.dist` (inside the source tree) over to `Modules/Setup` (inside the build tree) by hand so that upstream changes would be picked up. That arrangement gave packagers a slight advantage but was a recurring nuisance for developers tracking CPython work, since neglecting to copy the file could trigger build failures.

The build system now reads exclusively from `Modules/Setup` inside the source tree. Anyone wanting to customize that file is encouraged to keep their edits in a git fork of CPython or as patch files, just as they would for any other modification to the source tree.

(Contributed by Antoine Pitrou in [bpo-32430](https://bugs.python.org/issue?@action=redirect&bpo=32430).)

- Functions that convert a Python number into a C integer, such as [`PyLong_AsLong()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_AsLong), along with argument parsing helpers such as [`PyArg_ParseTuple()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_ParseTuple) that use integer-converting format units like `'i'`, will now favor the [`__index__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__) special method over [`__int__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__int__) when it exists. A deprecation warning is raised for objects offering the `__int__()` method yet lacking the `__index__()` method (such as [`Decimal`](https://docs.python.org/3.14/library/decimal.html#decimal.Decimal) and [`Fraction`](https://docs.python.org/3.14/library/fractions.html#fractions.Fraction)). For objects that implement `__index__()`, [`PyNumber_Check()`](https://docs.python.org/3.14/c-api/number.html#c.PyNumber_Check) now returns `1`. [`PyNumber_Long()`](https://docs.python.org/3.14/c-api/number.html#c.PyNumber_Long), [`PyNumber_Float()`](https://docs.python.org/3.14/c-api/number.html#c.PyNumber_Float) and [`PyFloat_AsDouble()`](https://docs.python.org/3.14/c-api/float.html#c.PyFloat_AsDouble) likewise consult the `__index__()` method when present. (Contributed by Serhiy Storchaka in [bpo-36048](https://bugs.python.org/issue?@action=redirect&bpo=36048) and [bpo-20092](https://bugs.python.org/issue?@action=redirect&bpo=20092).)

- A heap-allocated type object will now bump its reference count inside [`PyObject_Init()`](https://docs.python.org/3.14/c-api/allocation.html#c.PyObject_Init) (and its companion macro `PyObject_INIT`) rather than within [`PyType_GenericAlloc()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_GenericAlloc). Any type that customizes instance allocation or deallocation might require adjustment. (Contributed by Eddie Elizondo in [bpo-35810](https://bugs.python.org/issue?@action=redirect&bpo=35810).)

- A new function, `PyCode_NewWithPosOnlyArgs()`, lets you build code objects much like `PyCode_New()` does, except it adds a *posonlyargcount* parameter that records how many positional-only arguments there are. (Contributed by Pablo Galindo in [bpo-37221](https://bugs.python.org/issue?@action=redirect&bpo=37221).)

- `Py_SetPath()` now assigns [`sys.executable`](https://docs.python.org/3.14/library/sys.html#sys.executable) the full program path ([`Py_GetProgramFullPath()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_GetProgramFullPath)) instead of the program name ([`Py_GetProgramName()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_GetProgramName)). (Contributed by Victor Stinner in [bpo-38234](https://bugs.python.org/issue?@action=redirect&bpo=38234).)

[Subject index](INDEX.md) · [Previous source section](optimizations.md) · [Release/subject declaration](assignment-expressions.md) · [Next source section](deprecated.md)
