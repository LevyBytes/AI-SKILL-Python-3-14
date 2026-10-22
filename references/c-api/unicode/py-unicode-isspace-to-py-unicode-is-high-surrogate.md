# unicode C API: Unicode character classification and case conversion

### Unicode Character Properties

Unicode exposes a great many character properties. The ones you reach for most are surfaced through these macros, which map onto C functions according to how Python was configured.

 int Py_UNICODE_ISSPACE(Py_UCS4 ch)

Gives back `1` or `0` according to whether *ch* is a whitespace character.

 int Py_UNICODE_ISLOWER(Py_UCS4 ch)

Gives back `1` or `0` according to whether *ch* is a lowercase character.

 int Py_UNICODE_ISUPPER(Py_UCS4 ch)

Gives back `1` or `0` according to whether *ch* is an uppercase character.

 int Py_UNICODE_ISTITLE(Py_UCS4 ch)

Gives back `1` or `0` according to whether *ch* is a titlecase character.

 int Py_UNICODE_ISLINEBREAK(Py_UCS4 ch)

Gives back `1` or `0` according to whether *ch* is a linebreak character.

 int Py_UNICODE_ISDECIMAL(Py_UCS4 ch)

Gives back `1` or `0` according to whether *ch* is a decimal character.

 int Py_UNICODE_ISDIGIT(Py_UCS4 ch)

Gives back `1` or `0` according to whether *ch* is a digit character.

 int Py_UNICODE_ISNUMERIC(Py_UCS4 ch)

Gives back `1` or `0` according to whether *ch* is a numeric character.

 int Py_UNICODE_ISALPHA(Py_UCS4 ch)

Gives back `1` or `0` according to whether *ch* is an alphabetic character.

 int Py_UNICODE_ISALNUM(Py_UCS4 ch)

Gives back `1` or `0` according to whether *ch* is an alphanumeric character.

 int Py_UNICODE_ISPRINTABLE(Py_UCS4 ch)

Gives back `1` or `0` according to whether *ch* is a printable character, in the sense of [`str.isprintable()`](https://docs.python.org/3.14/library/stdtypes.html#str.isprintable).

The following APIs handle quick direct character conversions:

 Py_UCS4 Py_UNICODE_TOLOWER(Py_UCS4 ch)

Gives the character *ch* turned into lower case.

 Py_UCS4 Py_UNICODE_TOUPPER(Py_UCS4 ch)

Gives the character *ch* turned into upper case.

 Py_UCS4 Py_UNICODE_TOTITLE(Py_UCS4 ch)

Gives the character *ch* turned into title case.

 int Py_UNICODE_TODECIMAL(Py_UCS4 ch)

Gives the character *ch* turned into a decimal positive integer. Gives `-1` when that cannot be done. No exceptions are raised by this function.

 int Py_UNICODE_TODIGIT(Py_UCS4 ch)

Gives the character *ch* turned into a single digit integer. Gives `-1` when that cannot be done. No exceptions are raised by this function.

 double Py_UNICODE_TONUMERIC(Py_UCS4 ch)

Gives the character *ch* turned into a double. Gives `-1.0` when that cannot be done. No exceptions are raised by this function.

The following APIs let you operate on surrogates:

 int Py_UNICODE_IS_SURROGATE(Py_UCS4 ch)

Test whether *ch* is a surrogate (`0xD800 <= ch <= 0xDFFF`).

 int Py_UNICODE_IS_HIGH_SURROGATE(Py_UCS4 ch)

Test whether *ch* is a high surrogate (`0xD800 <= ch <= 0xDBFF`).

[Subject index](INDEX.md) · [Previous source contract](pyunicode-read-to-pyunicode-is-ascii.md) · [Following source contract](py-unicode-is-low-surrogate-to-py-unicode-join-surrogates.md)
