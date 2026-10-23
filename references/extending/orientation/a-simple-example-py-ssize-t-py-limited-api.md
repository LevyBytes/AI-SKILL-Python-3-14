# A Simple Example - Py_ssize_t, Py_LIMITED_API

### 1.1. A Simple Example

Suppose we build an extension module named `spam` (beloved by Monty Python fans…) and suppose we aim to expose a Python wrapper around the C library function `system()` [1]. That function accepts a null-terminated character string and hands back an integer. Our intention is to make the function usable from Python like this:

```pycon
>>> import spam
>>> status = spam.system("ls -l")

```

Start off by writing a file `spammodule.c`. (As a matter of tradition, a module named `spam` keeps its implementation in a C file named `spammodule.c`; should the module name run long, say `spammify`, the file may simply be `spammify.c`.)

Our file can open with these first two lines:

```c
#define PY_SSIZE_T_CLEAN
#include <Python.h>

```

which brings in the Python API (feel free to tack on a comment explaining what the module does plus a copyright notice).

Note

Because Python can introduce certain pre-processor definitions that influence the standard headers on a few systems, you *must* place `Python.h` ahead of any standard headers in your include order.

The purpose of `#define PY_SSIZE_T_CLEAN` was to signal that `Py_ssize_t` ought to replace `int` within some APIs. Since Python 3.13 it is no longer required, though we retain it for backward compatibility. Consult [Strings and buffers](https://docs.python.org/3.14/c-api/arg.html#arg-parsing-string-and-buffers) for an explanation of this macro.

Every user-visible symbol that `Python.h` declares carries a `Py` or `PY` prefix, the lone exceptions being those originating in standard header files.

Tip

To preserve backward compatibility, `Python.h` brings in a handful of standard header files. A C extension ought to include for itself whatever standard headers it relies on rather than leaning on these implicit includes. When you target the limited C API at version 3.13 or later, the implicit includes are:

- `<assert.h>`

- `<intrin.h>` (on Windows)

- `<inttypes.h>`

- `<limits.h>`

- `<math.h>`

- `<stdarg.h>`

- `<wchar.h>`

- `<sys/types.h>` (if present)

When [`Py_LIMITED_API`](https://docs.python.org/3.14/c-api/stable.html#c.Py_LIMITED_API) goes undefined, or is pinned to version 3.12 or earlier, these headers come along too:

- `<ctype.h>`

- `<unistd.h>` (on POSIX)

When [`Py_LIMITED_API`](https://docs.python.org/3.14/c-api/stable.html#c.Py_LIMITED_API) goes undefined, or is pinned to version 3.10 or earlier, these headers come along too:

- `<errno.h>`

-

[Subject index](INDEX.md) · [Previous source section](extending-python-with-c-or-c.md) · [Next source section](a-simple-example-pyobject-pyarg-parsetuple-pylong-fromlong.md)
