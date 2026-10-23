# `printf`-style Bytes Formatting - Complete Conversion , Meaning , Notes table

| Conversion | Meaning | Notes |
| --- | --- | --- |
| `'d'` | Signed integer decimal. |  |
| `'i'` | Signed integer decimal. |  |
| `'o'` | Signed octal value. | (1) |
| `'u'` | Obsolete type — it is identical to `'d'`. | (8) |
| `'x'` | Signed hexadecimal (lowercase). | (2) |
| `'X'` | Signed hexadecimal (uppercase). | (2) |
| `'e'` | Floating-point exponential format (lowercase). | (3) |
| `'E'` | Floating-point exponential format (uppercase). | (3) |
| `'f'` | Floating-point decimal format. | (3) |
| `'F'` | Floating-point decimal format. | (3) |
| `'g'` | Floating-point format. Picks lowercase exponential format when the exponent is below -4 or at least the precision; otherwise decimal format. | (4) |
| `'G'` | Floating-point format. Picks uppercase exponential format when the exponent is below -4 or at least the precision; otherwise decimal format. | (4) |
| `'c'` | Single byte (accepts integer or single byte objects). |  |
| `'b'` | Bytes (any object that follows the buffer protocol or has `__bytes__()`). | (5) |
| `'s'` | `'s'` serves as an alias for `'b'`, to be reserved for Python2/3 code bases only. | (6) |
| `'a'` | Bytes (converts any Python object using `repr(obj).encode('ascii', 'backslashreplace')`). | (5) |
| `'r'` | `'r'` serves as an alias for `'a'`, to be reserved for Python2/3 code bases only. | (7) |
| `'%'` | Nothing is converted; the result simply gets a `'%'` character. |  |

Notes:

1.

The alternate form prepends a leading octal specifier (`'0o'`) ahead of the first digit.

2.

The alternate form prepends a leading `'0x'` or `'0X'` (whichever matches the `'x'` or `'X'` format that was used) ahead of the first digit.

3.

The alternate form makes the result always carry a decimal point, even when no digits come after it.

The precision sets how many digits follow the decimal point and defaults to 6.

4.

The alternate form makes the result always carry a decimal point, and trailing zeroes are kept rather than stripped as they otherwise would be.

The precision sets how many significant digits sit before and after the decimal point and defaults to 6.

5.

When precision is `N`, the output is cut down to `N` characters.

6.

`b'%s'` is deprecated, yet it will stay throughout the 3.x series.

7.

`b'%r'` is deprecated, yet it will stay throughout the 3.x series.

8.

See [**PEP 237**](https://peps.python.org/pep-0237/).

Note

The bytearray flavour of this method does *not* operate in place - it always yields a fresh object, even when nothing was altered.

See also

[**PEP 461**](https://peps.python.org/pep-0461/) - Adding % formatting to bytes and bytearray

Added in version 3.5.

[Subject index](INDEX.md) · [Previous](printf-bytes-formatting-overview.md) · [Continue](memory-views-and-memoryview-construction.md) · [Owning module, declaration or section: `printf`-style Bytes Formatting](printf-bytes-formatting-overview.md)
