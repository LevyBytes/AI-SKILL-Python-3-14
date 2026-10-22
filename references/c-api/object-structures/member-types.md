# Member types

### Member types

`PyMemberDef.type` accepts any of the macros below, each standing for a particular C type. Reading the member from Python turns it into the matching Python type; writing it from Python turns the value back into the C type. Where that conversion can't happen, you get an exception like [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) or [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError).

Attributes set up in this manner resist deletion through, say, [`del`](https://docs.python.org/3.14/reference/simple_stmts.html#del) or [`delattr()`](https://docs.python.org/3.14/library/functions.html#delattr), except where they carry the (D) marking.

| Macro name | C type | Python type |
| --- | --- | --- |
| Py_T_BYTE * Included in the Stable ABI from version 3.12 onward.* | char | `int` |
| Py_T_SHORT * Included in the Stable ABI from version 3.12 onward.* | short | `int` |
| Py_T_INT * Included in the Stable ABI from version 3.12 onward.* | int | `int` |
| Py_T_LONG * Included in the Stable ABI from version 3.12 onward.* | long | `int` |
| Py_T_LONGLONG * Included in the Stable ABI from version 3.12 onward.* | long long | `int` |
| Py_T_UBYTE * Included in the Stable ABI from version 3.12 onward.* | unsigned char | `int` |
| Py_T_UINT * Included in the Stable ABI from version 3.12 onward.* | unsigned int | `int` |
| Py_T_USHORT * Included in the Stable ABI from version 3.12 onward.* | unsigned short | `int` |
| Py_T_ULONG * Included in the Stable ABI from version 3.12 onward.* | unsigned long | `int` |
| Py_T_ULONGLONG * Included in the Stable ABI from version 3.12 onward.* | unsigned long long | `int` |
| Py_T_PYSSIZET * Included in the Stable ABI from version 3.12 onward.* | Py_ssize_t | `int` |
| Py_T_FLOAT * Included in the Stable ABI from version 3.12 onward.* | float | `float` |
| Py_T_DOUBLE * Included in the Stable ABI from version 3.12 onward.* | double | `float` |
| Py_T_BOOL * Included in the Stable ABI from version 3.12 onward.* | char (written as 0 or 1) | `bool` |
| Py_T_STRING * Included in the Stable ABI from version 3.12 onward.* | const char* (*) | `str` (RO) |
| Py_T_STRING_INPLACE * Included in the Stable ABI from version 3.12 onward.* | const char[] (*) | `str` (RO) |
| Py_T_CHAR * Included in the Stable ABI from version 3.12 onward.* | char (0-127) | `str` (**) |
| Py_T_OBJECT_EX * Included in the Stable ABI from version 3.12 onward.* | PyObject* | `object` (D) |

>

(*): A C string that ends in a null byte and is UTF8-encoded. Under `Py_T_STRING` the C side holds a pointer, while under `Py_T_STRING_INPLACE` the characters sit right inside the structure.

(**): String of length 1. Only ASCII is accepted.

(RO): Implies `Py_READONLY`.

(D): May be removed, and doing so leaves the pointer at `NULL`. Trying to read a `NULL` pointer brings up [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError).

Added in version 3.12: Earlier releases exposed the macros solely through `#include "structmember.h"`, and they went without the `Py_` prefix back then (for instance, `T_INT`). That header remains in place and keeps the former names, plus the deprecated types shown here:

 T_OBJECT

Behaves as `Py_T_OBJECT_EX` does, save that a `NULL` becomes `None`. The Python-side consequence is unexpected: removing the attribute really just leaves it holding `None`.

 T_NONE

Always `None`. Must be used with `Py_READONLY`.

[Subject index](INDEX.md) · [Previous source contract](py-readonly-to-py-relative-offset.md) · [Following source contract](pygetsetdef-to-pyobject.md)
