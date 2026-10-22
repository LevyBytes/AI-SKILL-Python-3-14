# Python 3.11 changes: Limited API header dependencies and frame accessors

Once the `Py_LIMITED_API` macro is fixed at `0x030b0000` (Python 3.11) or above, `<Python.h>` stops pulling in the `<stdlib.h>`, `<stdio.h>`, `<errno.h>` and `<string.h>` header files. A C extension ought to bring those header files in itself, placing them after `#include <Python.h>`. (Contributed by Victor Stinner in [bpo-45434](https://bugs.python.org/issue?@action=redirect&bpo=45434).)

- A set of non-limited API files — `cellobject.h`, `classobject.h`, `code.h`, `context.h`, `funcobject.h`, `genobject.h` and `longintrepr.h` — has relocated into the `Include/cpython` directory, and on top of that the `eval.h` header file is gone. You shouldn't include any of these on their own, because `Python.h` already brings them in: [Include Files](https://docs.python.org/3.14/c-api/intro.html#api-includes). Where they were being included directly, switch to including `Python.h` instead. (Contributed by Victor Stinner in [bpo-35134](https://bugs.python.org/issue?@action=redirect&bpo=35134).)

- The limited C API no longer carries the `PyUnicode_CHECK_INTERNED()` macro. It could never actually be used there to begin with, since it leaned on internal structures that the limited C API doesn't expose. (Contributed by Victor Stinner in [bpo-46007](https://bugs.python.org/issue?@action=redirect&bpo=46007).)

- These frame functions and the type below now come straight from `#include <Python.h>`, so adding `#include <frameobject.h>` is no longer required:

  - [`PyFrame_Check()`](https://docs.python.org/3.14/c-api/frame.html#c.PyFrame_Check)

  - [`PyFrame_GetBack()`](https://docs.python.org/3.14/c-api/frame.html#c.PyFrame_GetBack)

  - [`PyFrame_GetBuiltins()`](https://docs.python.org/3.14/c-api/frame.html#c.PyFrame_GetBuiltins)

  - [`PyFrame_GetGenerator()`](https://docs.python.org/3.14/c-api/frame.html#c.PyFrame_GetGenerator)

  - [`PyFrame_GetGlobals()`](https://docs.python.org/3.14/c-api/frame.html#c.PyFrame_GetGlobals)

  - [`PyFrame_GetLasti()`](https://docs.python.org/3.14/c-api/frame.html#c.PyFrame_GetLasti)

  - [`PyFrame_GetLocals()`](https://docs.python.org/3.14/c-api/frame.html#c.PyFrame_GetLocals)

  - [`PyFrame_Type`](https://docs.python.org/3.14/c-api/frame.html#c.PyFrame_Type)

(Contributed by Victor Stinner in [gh-93937](https://github.com/python/cpython/issues/93937).)

- The structure members of [`PyFrameObject`](https://docs.python.org/3.14/c-api/frame.html#c.PyFrameObject) are now gone from the public C API.

Even though the docs warn that [`PyFrameObject`](https://docs.python.org/3.14/c-api/frame.html#c.PyFrameObject) fields may shift at any moment, in fact they had held steady for ages and saw use in a number of widely-used extensions.

Python 3.11 restructured the frame struct in order to make room for performance optimizations. A few fields disappeared outright, being artifacts of how the old implementation worked.

[`PyFrameObject`](https://docs.python.org/3.14/c-api/frame.html#c.PyFrameObject) fields:

  - `f_back`: use [`PyFrame_GetBack()`](https://docs.python.org/3.14/c-api/frame.html#c.PyFrame_GetBack).

  - `f_blockstack`: removed.

  - `f_builtins`: use [`PyFrame_GetBuiltins()`](https://docs.python.org/3.14/c-api/frame.html#c.PyFrame_GetBuiltins).

  - `f_code`: use [`PyFrame_GetCode()`](https://docs.python.org/3.14/c-api/frame.html#c.PyFrame_GetCode).

  - `f_gen`: use [`PyFrame_GetGenerator()`](https://docs.python.org/3.14/c-api/frame.html#c.PyFrame_GetGenerator).

  -

[Subject index](INDEX.md) · [Next source section](c-api-frame-accessor-migration.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](c-api-changes-new-features.md) · [Release/subject declaration](c-api-trashcan-lifecycle-migration.md) · [Preceding release/subject continuation](immutable-heap-types-and-vectorcall.md)
