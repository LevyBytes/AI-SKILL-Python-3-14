# What's New In Python 3.11 / C API Changes / Removed

### Removed

- Both `PyFrame_BlockSetup()` and `PyFrame_BlockPop()` are gone. (Contributed by Mark Shannon in [bpo-40222](https://bugs.python.org/issue?@action=redirect&bpo=40222).)

- Drop these math macros that relied on the `errno` variable:

  - `Py_ADJUST_ERANGE1()`

  - `Py_ADJUST_ERANGE2()`

  - `Py_OVERFLOWED()`

  - `Py_SET_ERANGE_IF_OVERFLOW()`

  - `Py_SET_ERRNO_ON_MATH_ERROR()`

(Contributed by Victor Stinner in [bpo-45412](https://bugs.python.org/issue?@action=redirect&bpo=45412).)

- Drop the `Py_UNICODE_COPY()` and `Py_UNICODE_FILL()` macros, which had been deprecated all the way back in Python 3.3. Lean on `PyUnicode_CopyCharacters()` or `memcpy()` (for a `wchar_t*` string), plus the `PyUnicode_Fill()` functions, in their stead. (Contributed by Victor Stinner in [bpo-41123](https://bugs.python.org/issue?@action=redirect&bpo=41123).)

- Drop the `pystrhex.h` header file, which holds nothing but private functions. A C extension should include only the principal `<Python.h>` header file. (Contributed by Victor Stinner in [bpo-45434](https://bugs.python.org/issue?@action=redirect&bpo=45434).)

- Drop the `Py_FORCE_DOUBLE()` macro, which the `Py_IS_INFINITY()` macro had relied on. (Contributed by Victor Stinner in [bpo-45440](https://bugs.python.org/issue?@action=redirect&bpo=45440).)

- With [`Py_LIMITED_API`](https://docs.python.org/3.14/c-api/stable.html#c.Py_LIMITED_API) defined, the items below can no longer be reached:

  - [`PyMarshal_WriteLongToFile()`](https://docs.python.org/3.14/c-api/marshal.html#c.PyMarshal_WriteLongToFile)

  - [`PyMarshal_WriteObjectToFile()`](https://docs.python.org/3.14/c-api/marshal.html#c.PyMarshal_WriteObjectToFile)

  - [`PyMarshal_ReadObjectFromString()`](https://docs.python.org/3.14/c-api/marshal.html#c.PyMarshal_ReadObjectFromString)

  - [`PyMarshal_WriteObjectToString()`](https://docs.python.org/3.14/c-api/marshal.html#c.PyMarshal_WriteObjectToString)

  - the `Py_MARSHAL_VERSION` macro

None of these belong to the [limited API](https://docs.python.org/3.14/c-api/stable.html#limited-api-list).

(Contributed by Victor Stinner in [bpo-45474](https://bugs.python.org/issue?@action=redirect&bpo=45474).)

- Keep [`PyWeakref_GET_OBJECT()`](https://docs.python.org/3.14/c-api/weakref.html#c.PyWeakref_GET_OBJECT) out of the limited C API. It had never functioned there anyway, the `PyWeakReference` structure being opaque under the limited C API. (Contributed by Victor Stinner in [bpo-35134](https://bugs.python.org/issue?@action=redirect&bpo=35134).)

- Drop the `PyHeapType_GET_MEMBERS()` macro. Surfacing it in the public C API was an error; it is meant strictly for Python's own internal use. Turn to the `PyTypeObject.tp_members` member in its place. (Contributed by Victor Stinner in [bpo-40170](https://bugs.python.org/issue?@action=redirect&bpo=40170).)

- Drop the `HAVE_PY_SET_53BIT_PRECISION` macro, now shifted into the internal C API. (Contributed by Victor Stinner in [bpo-45412](https://bugs.python.org/issue?@action=redirect&bpo=45412).)

- Drop the [`Py_UNICODE`](https://docs.python.org/3.14/c-api/unicode.html#c.Py_UNICODE) encoder APIs, given that they've sat deprecated since Python 3.3, see scant use, and run inefficiently next to the recommended alternatives.

Here are the functions that were removed:

  - `PyUnicode_Encode()`

  - `PyUnicode_EncodeASCII()`

  - `PyUnicode_EncodeLatin1()`

  - `PyUnicode_EncodeUTF7()`

  - `PyUnicode_EncodeUTF8()`

  - `PyUnicode_EncodeUTF16()`

  - `PyUnicode_EncodeUTF32()`

  - `PyUnicode_EncodeUnicodeEscape()`

  - `PyUnicode_EncodeRawUnicodeEscape()`

  - `PyUnicode_EncodeCharmap()`

  - `PyUnicode_TranslateCharmap()`

  - `PyUnicode_EncodeDecimal()`

  - `PyUnicode_TransformDecimalToASCII()`

See [**PEP 624**](https://peps.python.org/pep-0624/) for details and [**migration guidance**](https://peps.python.org/pep-0624/#alternative-apis). (Contributed by Inada Naoki in [bpo-44029](https://bugs.python.org/issue?@action=redirect&bpo=44029).)

[Subject index](INDEX.md) · [Previous source section](c-api-changes-pending-removal-in-python-3-12.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](c-api-changes-new-features.md) · [Next source section](tarfile.md)
