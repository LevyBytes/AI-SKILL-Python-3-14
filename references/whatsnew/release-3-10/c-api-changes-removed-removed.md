# Python 3.10 changes: Removed symbol-table APIs

### Removed

- Removed `Py_UNICODE_str*` functions manipulating `Py_UNICODE*` strings. (Contributed by Inada Naoki in [bpo-41123](https://bugs.python.org/issue?@action=redirect&bpo=41123).)

  - `Py_UNICODE_strlen`: use [`PyUnicode_GetLength()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_GetLength) or [`PyUnicode_GET_LENGTH`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_GET_LENGTH)

  - `Py_UNICODE_strcat`: use [`PyUnicode_CopyCharacters()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_CopyCharacters) or [`PyUnicode_FromFormat()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_FromFormat)

  - `Py_UNICODE_strcpy`, `Py_UNICODE_strncpy`: use [`PyUnicode_CopyCharacters()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_CopyCharacters) or [`PyUnicode_Substring()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_Substring)

  - `Py_UNICODE_strcmp`: use [`PyUnicode_Compare()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_Compare)

  - `Py_UNICODE_strncmp`: use [`PyUnicode_Tailmatch()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_Tailmatch)

  - `Py_UNICODE_strchr`, `Py_UNICODE_strrchr`: use [`PyUnicode_FindChar()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_FindChar)

- Removed `PyUnicode_GetMax()`. Please migrate to new ([**PEP 393**](https://peps.python.org/pep-0393/)) APIs. (Contributed by Inada Naoki in [bpo-41103](https://bugs.python.org/issue?@action=redirect&bpo=41103).)

- Removed `PyLong_FromUnicode()`. Please migrate to [`PyLong_FromUnicodeObject()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_FromUnicodeObject). (Contributed by Inada Naoki in [bpo-41103](https://bugs.python.org/issue?@action=redirect&bpo=41103).)

- Removed `PyUnicode_AsUnicodeCopy()`. Please use [`PyUnicode_AsUCS4Copy()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_AsUCS4Copy) or [`PyUnicode_AsWideCharString()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_AsWideCharString) (Contributed by Inada Naoki in [bpo-41103](https://bugs.python.org/issue?@action=redirect&bpo=41103).)

- Removed `_Py_CheckRecursionLimit` variable: its role is now filled by `ceval.recursion_limit` belonging to the [`PyInterpreterState`](https://docs.python.org/3.14/c-api/subinterpreters.html#c.PyInterpreterState) structure. (Contributed by Victor Stinner in [bpo-41834](https://bugs.python.org/issue?@action=redirect&bpo=41834).)

- Removed undocumented macros `Py_ALLOW_RECURSION` and `Py_END_ALLOW_RECURSION` together with the `recursion_critical` field of the [`PyInterpreterState`](https://docs.python.org/3.14/c-api/subinterpreters.html#c.PyInterpreterState) structure. (Contributed by Serhiy Storchaka in [bpo-41936](https://bugs.python.org/issue?@action=redirect&bpo=41936).)

- Removed the undocumented `PyOS_InitInterrupts()` function. Starting up Python already quietly puts signal handlers in place: refer to [`PyConfig.install_signal_handlers`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.install_signal_handlers). (Contributed by Victor Stinner in [bpo-41713](https://bugs.python.org/issue?@action=redirect&bpo=41713).)

- Remove the `PyAST_Validate()` function. Building an AST object (`mod_ty` type) through the public C API is no longer achievable. That function had already been kept out of the limited C API ([**PEP 384**](https://peps.python.org/pep-0384/)). (Contributed by Victor Stinner in [bpo-43244](https://bugs.python.org/issue?@action=redirect&bpo=43244).)

- Remove the `symtable.h` header file together with the undocumented functions:

  - `PyST_GetScope()`

  - `PySymtable_Build()`

  - `PySymtable_BuildObject()`

  - `PySymtable_Free()`

  - `Py_SymtableString()`

  -

[Subject index](INDEX.md) · [Previous source section](c-api-changes-deprecated.md) · [Next source section](c-api-changes-removed-py-symtablestringobject.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](c-api-changes-pep-652-maintaining-the-stable-abi.md)
