# codecs - Binary Transforms

### Binary Transforms

The codecs below supply binary transforms: [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) to [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) mappings. They aren't handled by [`bytes.decode()`](https://docs.python.org/3.14/library/stdtypes.html#bytes.decode) (which yields only [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) output).

| Codec | Aliases | Meaning | Encoder / decoder |
| --- | --- | --- | --- |
| base64_codec [1] | base64, base_64 | Turn the operand into multiline MIME base64 (a trailing `'\n'` is always present in the result). Changed in version 3.4: any bytes-like object is now accepted as input when encoding and decoding | `base64.encodebytes()` / `base64.decodebytes()` |
| bz2_codec | bz2 | Squeeze the operand down with bz2. | `bz2.compress()` / `bz2.decompress()` |
| hex_codec | hex | Render the operand in hexadecimal, using two digits for each byte. | `binascii.b2a_hex()` / `binascii.a2b_hex()` |
| quopri_codec | quopri, quotedprintable, quoted_printable | Turn the operand into MIME quoted printable. | `quopri.encode()` with `quotetabs=True` / `quopri.decode()` |
| uu_codec | uu | Transform the operand by way of uuencode. |  |
| zlib_codec | zip, zlib | Squeeze the operand down with gzip. | `zlib.compress()` / `zlib.decompress()` |

Added in version 3.2: The binary transforms were brought back.

Changed in version 3.4: The aliases tied to the binary transforms were brought back.

[Subject index](INDEX.md) · [Previous](text-encodings.md) · [Owning module, declaration or section: codecs](codecs-encode-to-codecs-lookup.md) · [Continue](codecs-escape-encode-to-codecs-escape-decode.md)
