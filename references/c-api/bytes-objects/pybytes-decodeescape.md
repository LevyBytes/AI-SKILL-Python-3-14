# PyObject *PyBytes_DecodeEscape(const char *s, Py_ssize_t len, const char *errors, Py_ssize_t unicode, const char *recode_encoding)

[PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyBytes_DecodeEscape(const char *s, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) len, const char *errors, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) unicode, const char *recode_encoding)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).** Thread safety: [Atomic](https://docs.python.org/3.14/library/threadsafety.html#threadsafety-level-atomic).*

Decode the backslash escapes in the string *s*. Here *s* cannot be `NULL`, and *len* has to give the length of *s*.

Pass *errors* as one of `"strict"`, `"replace"`, or `"ignore"`. When *errors* comes in as `NULL`, the default of `"strict"` applies.

On success, what comes back is a [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) to a Python [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object carrying the decoded string. Failing that, the routine yields `NULL` with an exception set.

Changed in version 3.9: The *unicode* and *recode_encoding* arguments no longer have any effect.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](bytes-objects.md) · [Owning structure and shared ABI conditions](pybytesobject-to-pybytes-get-size.md) · [Previous source contract](pybytes-asstring-to-pybytes-repr.md)
