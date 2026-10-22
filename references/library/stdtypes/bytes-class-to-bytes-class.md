# stdtypes: `bytes`

### Bytes Objects

Bytes objects are immutable sequences holding single bytes. Because a great many widely used binary protocols build on the ASCII text encoding, bytes objects expose a handful of methods that apply only to ASCII compatible data, and in numerous other respects they parallel string objects closely.

 *class *bytes(*source=b''*)

 *class *bytes(*source*, *encoding*, *errors='strict'*)

To begin with, writing bytes literals follows mostly the same rules as writing string literals, save for the extra `b` prefix:

- Single quotes: `b'still allows embedded "double" quotes'`

- Double quotes: `b"still allows embedded 'single' quotes"`

- Triple quoted: `b'''3 single quotes'''`, `b"""3 double quotes"""`

Bytes literals may hold only ASCII characters (no matter what source code encoding has been declared). Whenever a binary value exceeds 127 it has to be written into a bytes literal through the right escape sequence.

Just like string literals, bytes literals can carry an `r` prefix that turns off interpretation of escape sequences. Consult [String and Bytes literals](https://docs.python.org/3.14/reference/lexical_analysis.html#strings) for further detail on the assorted shapes a bytes literal can take, including the escape sequences it supports.

Although bytes literals and their displayed forms rest on ASCII text, a bytes object really acts as an immutable sequence of integers, where every entry is confined so that `0 <= x < 256` (trying to break this bound raises [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError)). The intent here is to stress that, even though plenty of binary formats embed ASCII based pieces and respond well to certain text-oriented algorithms, the same does not hold for arbitrary binary data in general (carelessly running text processing algorithms over binary data formats that aren't ASCII compatible tends to corrupt the data).

Beyond the literal notations, there are several further ways to build bytes objects:

- A zero-filled bytes object of a specified length: `bytes(10)`

- From an iterable of integers: `bytes(range(20))`

- Copying existing binary data via the buffer protocol: `bytes(obj)`

Also see the [bytes](https://docs.python.org/3.14/library/functions.html#func-bytes) built-in.

Given that 2 hexadecimal digits line up exactly with one byte, hexadecimal numbers see frequent use as a way to spell out binary data. For that reason, the bytes type carries an extra class method for reading data in that notation:

[Subject index](INDEX.md) · [Previous](binary-sequence-types-bytes-bytearray-memoryview.md) · [Continue](bytes-bytes-hex-to-bytes-bytes-hex.md)
