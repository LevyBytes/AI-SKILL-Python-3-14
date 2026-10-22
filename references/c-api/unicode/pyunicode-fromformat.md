# PyObject *PyUnicode_FromFormat(const char *format, ...)

[PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicode_FromFormat(const char *format, ...)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Accepts a C `printf()`-style *format* string together with a variable count of arguments, works out the size of the resulting Python Unicode string, and gives back a string with those values formatted in. The variable arguments have to be C types and have to line up exactly with the format characters in the ASCII-encoded *format* string.

Every conversion specifier holds two or more characters and is built from the following components, which have to appear in this sequence:

1.

The `'%'` character, marking where the specifier begins.

2.

Conversion flags (optional), which influence the outcome of certain conversion types.

3.

Minimum field width (optional). When written as `'*'` (asterisk), the real width arrives in the next argument, which has to be of type int, and the object to convert follows the minimum field width and any optional precision.

4.

Precision (optional), written as a `'.'` (dot) trailed by the precision. When written as `'*'` (an asterisk), the real precision arrives in the next argument, which has to be of type int, and the value to convert follows the precision.

5.

Length modifier (optional).

6.

Conversion type.

These are the conversion flag characters:

| Flag | Meaning |
| --- | --- |
| `0` | The conversion will be zero padded for numeric values. |
| `-` | Left-adjusts the converted value (takes precedence over the `0` flag when you supply both). |

For the integer conversions that follow (`d`, `i`, `o`, `u`, `x`, or `X`), the length modifiers state the argument's type (int by default):

| Modifier | Types |
| --- | --- |
| `l` | long or unsigned long |
| `ll` | long long or unsigned long long |
| `j` | `intmax_t` or `uintmax_t` |
| `z` | `size_t` or `ssize_t` |
| `t` | `ptrdiff_t` |

For the conversions `s` or `V` that follow, the length modifier `l` declares the argument's type to be const wchar_t*.

These are the conversion specifiers:

| Conversion Specifier | Type | Comment |
| --- | --- | --- |
| `%` | *n/a* | The literal `%` character. |
| `d`, `i` | Specified by the length modifier | The decimal representation of a signed C integer. |
| `u` | Specified by the length modifier | The decimal representation of an unsigned C integer. |
| `o` | Specified by the length modifier | The octal representation of an unsigned C integer. |
| `x` | Specified by the length modifier | The hexadecimal representation of an unsigned C integer (lowercase). |
| `X` | Specified by the length modifier | The hexadecimal representation of an unsigned C integer (uppercase). |
| `c` | int | A single character. |
| `s` | const char* or const wchar_t* | A null-terminated C character array. |
| `p` | const void* | A C pointer rendered in hex. Largely the same as `printf("%p")`, save that it always begins with the literal `0x` no matter what the platform’s `printf` produces. |
| `A` | PyObject* | The result of calling `ascii()`. |
| `U` | PyObject* | A Unicode object. |
| `V` | PyObject*, const char* or const wchar_t* | A Unicode object (possibly `NULL`) plus, as a second parameter, a null-terminated C character array (employed whenever that first parameter comes in as `NULL`). |
| `S` | PyObject* | The result of calling `PyObject_Str()`. |
| `R` | PyObject* | The result of calling `PyObject_Repr()`. |
| `T` | PyObject* | Get the fully qualified name of an object type; call `PyType_GetFullyQualifiedName()`. |
| `#T` | PyObject* | Like the `T` format, except a colon (`:`) divides the module name from the qualified name. |
| `N` | PyTypeObject* | Get the fully qualified name of a type; call `PyType_GetFullyQualifiedName()`. |
| `#N` | PyTypeObject* | Like the `N` format, except a colon (`:`) divides the module name from the qualified name. |

Note

Width is measured in characters, not in bytes. Precision is counted in bytes or in `wchar_t` items (where the length modifier `l` applies) for `"%s"` and `"%V"` (when the `PyObject*` argument equals `NULL`), and counted in characters for `"%A"`, `"%U"`, `"%S"`, `"%R"` and `"%V"` (when the `PyObject*` argument is non-`NULL`).

Note

In contrast to C `printf()`, the `0` flag still takes effect for integer conversions (`d`, `i`, `u`, `o`, `x`, or `X`) even where a precision has been supplied.

Changed in version 3.2: Support for `"%lld"` and `"%llu"` added.

Changed in version 3.3: Support for `"%li"`, `"%lli"` and `"%zi"` added.

Changed in version 3.4: Support width and precision formatter for `"%s"`, `"%A"`, `"%U"`, `"%V"`, `"%S"`, `"%R"` added.

Changed in version 3.12: Added the conversion specifiers `o` and `X`, plus the length modifiers `j` and `t`. Every integer conversion now honors length modifiers. The length modifier `l` now extends to the conversion specifiers `s` and `V`. Variable width and precision `*` are now handled, as is the flag `-`.

A format character that is not recognized now triggers a [`SystemError`](https://docs.python.org/3.14/library/exceptions.html#SystemError). Earlier releases instead copied the entire remainder of the format string verbatim into the result string and threw away any leftover arguments.

Changed in version 3.13: Support for `%T`, `%#T`, `%N` and `%#N` formats added.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyunicode-new-to-pyunicode-fromstring.md) · [Following source contract](pyunicode-fromformatv-to-pyunicode-getdefaultencoding.md)
