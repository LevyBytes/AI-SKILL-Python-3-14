# `printf`-style String Formatting — Complete Conversion , Meaning , Notes table

| Conversion | Meaning | Notes |
| --- | --- | --- |
| `'d'` | Signed decimal integer. |  |
| `'i'` | Signed decimal integer. |  |
| `'o'` | Signed octal value. | (1) |
| `'u'` | Obsolete type — behaves the same as `'d'`. | (6) |
| `'x'` | Signed hexadecimal (lowercase). | (2) |
| `'X'` | Signed hexadecimal (uppercase). | (2) |
| `'e'` | Lowercase floating-point exponential format. | (3) |
| `'E'` | Uppercase floating-point exponential format. | (3) |
| `'f'` | Floating-point decimal format. | (3) |
| `'F'` | Floating-point decimal format. | (3) |
| `'g'` | Floating-point format. Switches to lowercase exponential format when the exponent drops below -4 or reaches the precision; otherwise uses decimal format. | (4) |
| `'G'` | Floating-point format. Switches to uppercase exponential format when the exponent drops below -4 or reaches the precision; otherwise uses decimal format. | (4) |
| `'c'` | Single character (takes an integer or a one-character string). |  |
| `'r'` | String (converts any Python object using `repr()`). | (5) |
| `'s'` | String (converts any Python object using `str()`). | (5) |
| `'a'` | String (converts any Python object using `ascii()`). | (5) |
| `'%'` | Nothing is converted; a `'%'` character ends up in the result. |  |

With the floating-point formats, the outcome ought to be rounded accurately to a stated precision `p` of digits following the decimal point. That rounding follows the same scheme as the [`round()`](https://docs.python.org/3.14/library/functions.html#round) builtin.

Notes:

1.

Under the alternate form, a leading octal specifier (`'0o'`) is placed ahead of the first digit.

2.

Under the alternate form, a leading `'0x'` or `'0X'` (the choice tracking whether you used the `'x'` or `'X'` format) is placed ahead of the first digit.

3.

Under the alternate form, the outcome always carries a decimal point, even when no digits come after it.

The precision sets how many digits appear after the decimal point, with a default of 6.

4.

Under the alternate form, the outcome always carries a decimal point, and any trailing zeroes that would normally be stripped are kept.

The precision sets how many significant digits appear before and after the decimal point, with a default of 6.

5.

When precision equals `N`, the result is cut down to `N` characters.

6.

See [**PEP 237**](https://peps.python.org/pep-0237/).

Because Python strings carry an explicit length, `%s` conversions never treat `'\0'` as marking where the string ends.

Changed in version 3.1: a `%f` conversion is no longer swapped for a `%g` conversion when the number's absolute value exceeds 1e50.

[Subject index](INDEX.md) · [Previous](printf-string-formatting-overview.md) · [Continue](binary-sequence-types-bytes-bytearray-memoryview.md) · [Owning module, declaration or section: `printf`-style String Formatting](printf-string-formatting-overview.md)
