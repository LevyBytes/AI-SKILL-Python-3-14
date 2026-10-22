# binascii: `binascii.b2a_hex()`, `binascii.hexlify()`, `binascii.a2b_hex()`, `binascii.unhexlify()`, `binascii.Error`, `binascii.Incomplete`

binascii.b2a_hex(*data*[, *sep*[, *bytes_per_sep=1*]])

 binascii.hexlify(*data*[, *sep*[, *bytes_per_sep=1*]])

Gives back the hexadecimal rendering of the binary *data*. Each byte of *data* becomes its matching 2-digit hex form, so the bytes object that comes back runs twice the length of *data*.

A comparable capability — though it yields a text string — is readily within reach through the [`bytes.hex()`](https://docs.python.org/3.14/library/stdtypes.html#bytes.hex) method.

When *sep* is given, it has to be a single-character str or bytes object. It gets slipped into the output following each group of *bytes_per_sep* input bytes. By default the separator's placement is tallied from the output's right end; to tally from the left instead, pass a negative *bytes_per_sep* value.

```python
>>> import binascii
>>> binascii.b2a_hex(b'\xb9\x01\xef')
b'b901ef'
>>> binascii.hexlify(b'\xb9\x01\xef', '-')
b'b9-01-ef'
>>> binascii.b2a_hex(b'\xb9\x01\xef', b'_', 2)
b'b9_01ef'
>>> binascii.b2a_hex(b'\xb9\x01\xef', b' ', -2)
b'b901 ef'

```

Changed in version 3.8: The *sep* and *bytes_per_sep* parameters were added.

 binascii.a2b_hex(*hexstr*)

 binascii.unhexlify(*hexstr*)

Gives back the binary data that the hexadecimal string *hexstr* stands for. This function undoes what `b2a_hex()` does. The *hexstr* argument has to hold an even count of hexadecimal digits (in either upper or lower case); failing that, an `Error` exception is raised.

A like capability — one more forgiving of whitespace — is likewise within reach through the [`bytes.fromhex()`](https://docs.python.org/3.14/library/stdtypes.html#bytes.fromhex) class method.

 *exception *binascii.Error

The exception that gets raised on errors, which tend to be programming mistakes.

 *exception *binascii.Incomplete

The exception that gets raised on incomplete data. As a rule these aren't programming mistakes; you can deal with them by pulling in a bit more data and having another go.

See also

Module [`base64`](https://docs.python.org/3.14/library/base64.html#module-base64)

Offers RFC-compliant base64-style encoding across base 16, 32, 64, and 85.

Module [`quopri`](https://docs.python.org/3.14/library/quopri.html#module-quopri)

Offers quoted-printable encoding of the sort found in MIME email messages.

[Subject index](INDEX.md) · [Previous](binascii-a2b-uu-to-binascii-crc32.md) · [Continue](../bisect/bisect-bisect-left-to-bisect-insort.md) · [Owning module, declaration or section: binascii](binascii-a2b-uu-to-binascii-crc32.md)
