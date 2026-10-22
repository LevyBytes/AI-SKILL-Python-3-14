# Character classification and conversion

### Character classification and conversion

These macros classify and convert characters in a locale-independent way, which sets them apart from the C standard library `ctype.h`. Whatever you hand them has to be a signed or unsigned char.

 Py_ISALNUM(c)

Return true if the character *c* is an alphanumeric character.

 Py_ISALPHA(c)

Return true if the character *c* is an alphabetic character (`a-z` and `A-Z`).

 Py_ISDIGIT(c)

Return true if the character *c* is a decimal digit (`0-9`).

 Py_ISLOWER(c)

Return true if the character *c* is a lowercase ASCII letter (`a-z`).

 Py_ISUPPER(c)

Return true if the character *c* is an uppercase ASCII letter (`A-Z`).

 Py_ISSPACE(c)

Report true when *c* counts as whitespace, namely a space, tab, carriage return, newline, vertical tab, or form feed.

 Py_ISXDIGIT(c)

Return true if the character *c* is a hexadecimal digit (`0-9`, `a-f`, and `A-F`).

 Py_TOLOWER(c)

Return the lowercase equivalent of the character *c*.

 Py_TOUPPER(c)

Return the uppercase equivalent of the character *c*.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyos-snprintf-to-pyos-strtol.md) · [Previous source contract](pyos-string-to-double-to-pyos-strnicmp.md) · [Following source contract](../coroutine-objects/coroutine-objects.md)
