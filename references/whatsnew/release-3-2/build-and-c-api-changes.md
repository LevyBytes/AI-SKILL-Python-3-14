# What's New In Python 3.2 / Build and C API Changes - sys, unicodedata

### Build and C API Changes

Changes to Python’s build process and to the C API include:

- Running `make altinstall` now installs the *idle*, *pydoc* and *2to3* scripts carrying a version-specific suffix ([bpo-10679](https://bugs.python.org/issue?@action=redirect&bpo=10679)).

- The C functions reaching into the Unicode Database now take in and give back characters spanning the whole Unicode range, narrow unicode builds included (Py_UNICODE_TOLOWER, Py_UNICODE_ISDECIMAL, plus more). At the Python level, you can see this in [`unicodedata.numeric()`](https://docs.python.org/3.14/library/unicodedata.html#unicodedata.numeric) yielding the right answer for large code points, and in [`repr()`](https://docs.python.org/3.14/library/functions.html#repr) potentially treating additional characters as printable.

(Reported by Bupjoe Lee and fixed by Amaury Forgeot D’Arc; [bpo-5127](https://bugs.python.org/issue?@action=redirect&bpo=5127).)

- On compilers that support them (the configure script works out which do), computed gotos are switched on by default now. You can still turn them off on a case-by-case basis by passing `--without-computed-gotos`.

(Contributed by Antoine Pitrou; [bpo-9203](https://bugs.python.org/issue?@action=redirect&bpo=9203).)

- The `--with-wctype-functions` option is gone. Every function now relies on the bundled unicode database.

(Contributed by Amaury Forgeot D’Arc; [bpo-9210](https://bugs.python.org/issue?@action=redirect&bpo=9210).)

- A fresh type, [`Py_hash_t`](https://docs.python.org/3.14/c-api/hash.html#c.Py_hash_t), sized to match a pointer, now carries hash values. They used to be long, a type that on certain 64-bit operating systems remains just 32 bits wide. Thanks to this fix, on builds with 64-bit pointers a [`set`](https://docs.python.org/3.14/library/stdtypes.html#set) or [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) can carry beyond `2**32` entries (before, reaching that many was possible but came with a disastrous performance collapse).

(Suggested by Raymond Hettinger and implemented by Benjamin Peterson; [bpo-9778](https://bugs.python.org/issue?@action=redirect&bpo=9778).)

- A freshly added macro `Py_VA_COPY` duplicates the state held in a variable argument list. It matches C99 *va_copy* yet works across every Python platform ([bpo-2443](https://bugs.python.org/issue?@action=redirect&bpo=2443)).

- A newly added C API function `PySys_SetArgvEx()` lets an embedded interpreter assign [`sys.argv`](https://docs.python.org/3.14/library/sys.html#sys.argv) while leaving [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) untouched ([bpo-5753](https://bugs.python.org/issue?@action=redirect&bpo=5753)).

- These days `PyEval_CallObject()` exists solely as a macro. Its function declaration, retained all this while for backwards compatibility, has been dropped — the macro itself goes back to 1997 ([bpo-8276](https://bugs.python.org/issue?@action=redirect&bpo=8276)).

- A fresh function [`PyLong_AsLongLongAndOverflow()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_AsLongLongAndOverflow) parallels [`PyLong_AsLongAndOverflow()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_AsLongAndOverflow). Each turns a Python [`int`](https://docs.python.org/3.14/library/functions.html#int) into a native fixed-width type and flags any situation where the value cannot fit ([bpo-7767](https://bugs.python.org/issue?@action=redirect&bpo=7767)).

- When the Python string ends in a *NUL*, the [`PyUnicode_CompareWithASCIIString()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_CompareWithASCIIString) function now reports *not equal*.

- A fresh function [`PyErr_NewExceptionWithDoc()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_NewExceptionWithDoc) resembles [`PyErr_NewException()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_NewException) except that you can attach a docstring. That gives C exceptions the same self-documenting reach their all-Python equivalents enjoy ([bpo-7033](https://bugs.python.org/issue?@action=redirect&bpo=7033)).

- Build with the `--with-valgrind` option and the pymalloc allocator shuts itself off whenever execution happens under Valgrind. The payoff is sharper memory leak detection inside Valgrind while pymalloc still kicks in everywhere else ([bpo-2422](https://bugs.python.org/issue?@action=redirect&bpo=2422)).

- The `O?` format is dropped from the *PyArg_Parse* functions. Nothing relied on it any longer, and it had never been written up in the docs ([bpo-8837](https://bugs.python.org/issue?@action=redirect&bpo=8837)).

Several further minor adjustments landed in the C-API. The [Misc/NEWS](https://github.com/python/cpython/blob/v3.2.6/Misc/NEWS) file holds the full rundown.

The Mac OS X build likewise picked up a handful of revisions; [Mac/BuildScript/README.txt](https://github.com/python/cpython/blob/v3.2.6/Mac/BuildScript/README.txt) spells them out. Anyone on a 32/64-bit build faces a documented snag with the stock Tcl/Tk shipped on Mac OS X 10.6. We therefore advise putting in a newer substitute, [ActiveState Tcl/Tk 8.5.9](https://web.archive.org/web/20101208191259/https://www.activestate.com/activetcl/downloads) for instance. Further particulars sit at [https://www.python.org/download/mac/tcltk/](https://www.python.org/download/mac/tcltk/).

[Subject index](INDEX.md) · [Previous source section](code-repository.md) · [Next source section](porting-to-python-3-2.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md)
