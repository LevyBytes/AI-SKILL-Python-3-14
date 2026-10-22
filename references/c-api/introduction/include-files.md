# Include Files

### Include Files

Every function, type, and macro declaration you need in order to work with the Python/C API gets pulled into your source by this single line:

```c
#define PY_SSIZE_T_CLEAN
#include <Python.h>

```

Doing so brings in these standard headers along with it: `<stdio.h>`, `<string.h>`, `<errno.h>`, `<limits.h>`, `<assert.h>` and `<stdlib.h>` (if available).

Note

Because Python can set certain pre-processor definitions that alter the standard headers on some platforms, you *must* pull in `Python.h` ahead of any standard headers.

Defining `PY_SSIZE_T_CLEAN` ahead of the `Python.h` include is the recommended practice in every case. Consult [Parsing arguments and building values](https://docs.python.org/3.14/c-api/arg.html#arg-parsing) for an explanation of this macro.

Every externally visible name that Python.h declares (apart from the ones coming from the included standard headers) carries either the `Py` or the `_Py` prefix. The `_Py`-prefixed names are reserved for the internal workings of the Python implementation and ought not to be touched by extension writers. There's no reserved prefix on structure member names.

Note

Never let user code declare names that start with `Py` or `_Py`. Doing so muddles things for the reader and threatens the portability of that user code to later Python releases, which might introduce more names carrying one of those prefixes.

The header files normally ship alongside Python. Under Unix, you'll find them in the `*prefix*/include/pythonversion/` and `*exec_prefix*/include/pythonversion/` directories, with [`prefix`](https://docs.python.org/3.14/using/configure.html#cmdoption-prefix) and [`exec_prefix`](https://docs.python.org/3.14/using/configure.html#cmdoption-exec-prefix) set by the matching arguments handed to Python's **configure** script, while *version* equals `'%d.%d' % sys.version_info[:2]`. Under Windows, the headers land in `*prefix*/include`, where `prefix` denotes the install location you gave the installer.

When pulling in the headers, add both directories (where they differ) to your compiler's include search path. Don't *instead* add the parent directories to the search path and then write `#include <pythonX.Y/Python.h>`; that approach falls apart on multi-platform builds, because the platform independent headers beneath [`prefix`](https://docs.python.org/3.14/using/configure.html#cmdoption-prefix) pull in the platform specific headers out of [`exec_prefix`](https://docs.python.org/3.14/using/configure.html#cmdoption-exec-prefix).

For C++ programmers: even though the entire API is written in C, the header files correctly mark the entry points as `extern "C"`. Consequently, nothing extra is required to call the API from C++.

[Subject index](INDEX.md) · [Previous source contract](coding-standards.md) · [Following source contract](py-can-start-threads-to-py-getenv.md)
