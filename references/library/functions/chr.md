# chr

chr(*codepoint*, */*)

Give back the string for the character at the given Unicode code point. As an illustration, `chr(97)` yields the string `'a'`, whereas `chr(8364)` yields the string `'€'`. It is the reverse of `ord()`.

The argument’s permitted range runs from 0 through 1,114,111 (0x10FFFF in base 16). A value beyond that range raises [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError).

[Builtin task index](INDEX.md).
