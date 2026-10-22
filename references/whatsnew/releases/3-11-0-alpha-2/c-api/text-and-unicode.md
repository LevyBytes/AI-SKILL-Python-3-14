# Python 3.11.0 alpha 2 / c api / text and unicode

[bpo-45434](https://bugs.python.org/issue?@action=redirect&bpo=45434): Once the `Py_LIMITED_API` macro is set to `0x030b0000` (Python 3.11) or above, `<Python.h>` stops pulling in the `<stdlib.h>`, `<stdio.h>`, `<errno.h>` and `<string.h>` headers. A C extension should pull those headers in explicitly following its `#include <Python.h>`. Victor Stinner contributed the patch.

[bpo-41123](https://bugs.python.org/issue?@action=redirect&bpo=41123): Delete the `Py_UNICODE_COPY()` and `Py_UNICODE_FILL()` macros, which had been deprecated since Python 3.3. Reach instead for `PyUnicode_CopyCharacters()` or `memcpy()` (`wchar_t*` string), plus the `PyUnicode_Fill()` function. Victor Stinner contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
