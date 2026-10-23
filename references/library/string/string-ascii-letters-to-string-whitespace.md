# string - String constants

### String constants

This module defines the following constants:

 string.ascii_letters

Joins together the `ascii_lowercase` and `ascii_uppercase` constants documented further down. The value does not depend on locale.

 string.ascii_lowercase

The lowercase letters `'abcdefghijklmnopqrstuvwxyz'`. Locale has no bearing on this value, and it stays fixed.

 string.ascii_uppercase

The uppercase letters `'ABCDEFGHIJKLMNOPQRSTUVWXYZ'`. Locale has no bearing on this value, and it stays fixed.

 string.digits

The string `'0123456789'`.

 string.hexdigits

The string `'0123456789abcdefABCDEF'`.

 string.octdigits

The string `'01234567'`.

 string.punctuation

String of ASCII characters which are considered punctuation characters in the `C` locale: `!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~`.

 string.printable

String of ASCII characters that Python treats as printable. It combines `digits`, `ascii_letters`, `punctuation`, and `whitespace`.

Note

By design, [`string.printable.isprintable()`](https://docs.python.org/3.14/library/stdtypes.html#str.isprintable) returns [`False`](https://docs.python.org/3.14/library/constants.html#False). In particular, `string.printable` is not printable in the POSIX sense (see *[LC_CTYPE](https://manpages.debian.org/locale(5))*).

 string.whitespace

A string holding every ASCII character treated as whitespace. The set covers space, tab, linefeed, return, formfeed, and vertical tab.

[Subject index](INDEX.md) · [Previous](string-common-string-operations.md) · [Continue](string-formatter-class.md) · [Owning module, declaration or section: string](string-common-string-operations.md)
