# string conversion and formatting C API: `PyOS_string_to_double()`, `PyOS_double_to_string()`, `Py_DTSF_SIGN`, `Py_DTSF_ADD_DOT_0`, `Py_DTSF_ALT`, `Py_DTSF_NO_NEG_0`, `PyOS_mystricmp()`, `PyOS_mystrnicmp()`, `PyOS_stricmp()`, `PyOS_strnicmp()`

double PyOS_string_to_double(const char *s, char **endptr, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *overflow_exception)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Turn the `s` string into a double, throwing a Python exception if it cannot. Which strings count as valid mirrors what Python’s [`float()`](https://docs.python.org/3.14/library/functions.html#float) constructor takes, with the one caveat that `s` may carry no surrounding whitespace. None of this depends on the locale in effect.

Passing `NULL` for `endptr` makes it parse the entire string. When the text is not a legitimate floating-point form, it throws [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) and hands back `-1.0`.

When endptr is something other than `NULL`, parse the longest prefix you can and aim `*endptr` at the earliest character left unparsed. If not even the opening segment forms a valid floating-point number, leave `*endptr` aimed at the string’s start, throw ValueError, and hand back `-1.0`.

When `s` denotes a magnitude beyond what a float can hold (`"1e500"`, say, behaves this way on numerous platforms), the behavior splits: a `NULL` `overflow_exception` yields `Py_INFINITY` carrying the right sign while leaving no exception set; otherwise `overflow_exception` has to reference a Python exception object, which gets thrown as the call returns `-1.0`. Either way, `*endptr` is aimed at the character immediately following the value that was parsed.

Should some different problem arise mid-conversion (an out-of-memory condition, for instance), set the matching Python exception and hand back `-1.0`.

Added in version 3.1.

 char *PyOS_double_to_string(double val, char format_code, int precision, int flags, int *ptype)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Render the double *val* as text, driven by the *format_code*, *precision*, and *flags* you pass in.

Allowed values for *format_code* are `'e'`, `'E'`, `'f'`, `'F'`, `'g'`, `'G'` or `'r'`. Choosing `'r'` forces *precision* to 0 and disregards whatever you passed. That `'r'` code requests the conventional [`repr()`](https://docs.python.org/3.14/library/functions.html#repr) rendering.

You may combine none, one, or several of these *flags* by or-ing them:

 Py_DTSF_SIGN

Prefix the produced text with a sign every time, including the case where *val* is zero or positive.

 Py_DTSF_ADD_DOT_0

Ensure that the returned string will not look like an integer.

 Py_DTSF_ALT

Apply “alternate” formatting rules. See the documentation for the `PyOS_snprintf()` `'#'` specifier for details.

 Py_DTSF_NO_NEG_0

Negative zero is converted to positive zero.

Added in version 3.11.

When *ptype* is not `NULL`, whatever it references gets assigned one of the constants below, picked according to *val*’s kind:

| **ptype* | type of *val* |
| --- | --- |
| Py_DTST_FINITE | finite number |
| Py_DTST_INFINITE | infinite number |
| Py_DTST_NAN | not a number |

What comes back is a pointer into *buffer* holding the converted text, or `NULL` when the conversion did not succeed. Releasing that returned string is the caller’s job, done through [`PyMem_Free()`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_Free).

Added in version 3.1.

 int PyOS_mystricmp(const char *str1, const char *str2)

 int PyOS_mystrnicmp(const char *str1, const char *str2, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) size)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Compare two strings while disregarding case. Their behavior tracks `strcmp()` and `strncmp()` (in that order) very closely, the difference being that ASCII letter case plays no role.

Yield `0` when the two match, something negative when *str1* orders ahead of *str2* lexicographically, and something positive when it orders behind.

Within the *str1* and *str2* arguments, a NUL byte signals where the string terminates. With `PyOS_mystrnicmp()`, the *size* argument caps the string length, behaving as though a NUL sat at the position *size* names.

These functions do not use the locale.

 int PyOS_stricmp(const char *str1, const char *str2)

 int PyOS_strnicmp(const char *str1, const char *str2, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) size)

Case insensitive comparison of strings.

On Windows, these are aliases of `stricmp()` and `strnicmp()`, respectively.

On other platforms, they are aliases of `PyOS_mystricmp()` and `PyOS_mystrnicmp()`, respectively.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyos-snprintf-to-pyos-strtol.md) · [Following source contract](py-isalnum-to-py-toupper.md)
