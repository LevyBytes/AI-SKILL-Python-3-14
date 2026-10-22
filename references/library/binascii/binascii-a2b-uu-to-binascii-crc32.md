# binascii: `binascii.a2b_uu()`, `binascii.b2a_uu()`, `binascii.a2b_base64()`, `binascii.b2a_base64()`, `binascii.a2b_qp()`, `binascii.b2a_qp()`, `binascii.crc_hqx()`, `binascii.crc32()`

### `binascii` — Convert between binary and ASCII

---

A handful of methods in the `binascii` module move data back and forth between binary and assorted ASCII-encoded binary forms. As a rule you won't reach for these functions yourself, instead going through wrapper modules such as [`base64`](https://docs.python.org/3.14/library/base64.html#module-base64). Underneath, the `binascii` module holds low-level functions coded in C for extra speed, which the higher-level modules draw upon.

Note

The `a2b_*` functions take Unicode strings made up only of ASCII characters, whereas the rest take just [bytes-like objects](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) — among them [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes), [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray), and any other object honoring the buffer protocol.

Changed in version 3.3: The `a2b_*` functions now take unicode strings restricted to ASCII.

The `binascii` module defines the following functions:

 binascii.a2b_uu(*string*)

Turns one line of uuencoded data back into binary and gives back that binary data. A line typically holds 45 (binary) bytes, the final line aside. Whitespace is permitted to trail the line's data.

 binascii.b2a_uu(*data*, ***, *backtick=False*)

Turns binary data into a line of ASCII characters; what comes back is that converted line, the trailing newline char included. The length of *data* ought to be no greater than 45. With *backtick* set to true, zeros show up as `'`'` rather than as spaces.

Changed in version 3.7: Added the *backtick* parameter.

 binascii.a2b_base64(*string*, */*, ***, *strict_mode=False*)

Turns a block of base64 data back into binary and gives back the binary data. You may hand it several lines in a single call.

When *strict_mode* is true, only base64 data that is valid gets converted; anything invalid prompts a `binascii.Error`.

Valid base64:

- Conforms to [**RFC 3548**](https://datatracker.ietf.org/doc/html/rfc3548.html).

- Contains only characters from the base64 alphabet.

- Contains no excess data after padding (including excess padding, newlines, etc.).

- Does not start with a padding.

Changed in version 3.11: Added the *strict_mode* parameter.

 binascii.b2a_base64(*data*, ***, *newline=True*)

Turns binary data into a line of ASCII characters using base64 coding. The value returned is that converted line, carrying a newline char whenever *newline* is true. This function's output abides by [**RFC 3548**](https://datatracker.ietf.org/doc/html/rfc3548.html).

Changed in version 3.6: Added the *newline* parameter.

 binascii.a2b_qp(*data*, *header=False*)

Turns a block of quoted-printable data back into binary and gives back the binary data. Several lines may go in at once. Should the optional argument *header* be present and true, underscores get decoded into spaces.

 binascii.b2a_qp(*data*, *quotetabs=False*, *istext=True*, *header=False*)

Turns binary data into one or more lines of ASCII characters under quoted-printable encoding. What comes back is the converted line(s). With the optional argument *quotetabs* present and true, every tab and space gets encoded. With the optional argument *istext* present and true, newlines stay unencoded but any trailing whitespace is encoded. With the optional argument *header* present and true, spaces are encoded as underscores in line with [**RFC 1522**](https://datatracker.ietf.org/doc/html/rfc1522.html). With the optional argument *header* present and false, newline characters get encoded too; were that not so, linefeed conversion could spoil the binary data stream.

 binascii.crc_hqx(*data*, *value*)

Works out a 16-bit CRC value over *data*, taking *value* as the starting CRC, and hands back the outcome. The polynomial it employs is the CRC-CCITT one, *x*16 + *x*12 + *x*5 + 1, which is commonly written as 0x1021. This particular CRC figures in the binhex4 format.

 binascii.crc32(*data*[, *value*])

Works out CRC-32, the unsigned 32-bit checksum over *data*, beginning from an initial CRC of *value*. By default that starting CRC is zero. The algorithm lines up with the checksum used for ZIP files. Because it was built to serve as a checksum algorithm, it makes a poor fit as a general-purpose hash algorithm. Employ it like so:

```python
print(binascii.crc32(b"hello world"))
# Or, in two pieces:
crc = binascii.crc32(b"hello")
crc = binascii.crc32(b" world", crc)
print('crc32 = {:#010x}'.format(crc))

```

Changed in version 3.0: The result is always unsigned.

[Subject index](INDEX.md) · [Previous](convert-between-binary-and-ascii.md) · [Continue](binascii-b2a-hex-to-binascii-incomplete.md)
