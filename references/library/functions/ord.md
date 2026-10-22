# ord

ord(*character*, */*)

Yield the ordinal value belonging to a character.

When the argument is a one-character string, hand back the Unicode code point of that character. As an example, `ord('a')` yields the integer `97` and `ord('€')` (Euro sign) yields `8364`. This is the inverse of `chr()`.

When the argument is a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) or [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) object of length 1, hand back its single byte value. As an example, `ord(b'a')` yields the integer `97`.

[Builtin task index](INDEX.md).
