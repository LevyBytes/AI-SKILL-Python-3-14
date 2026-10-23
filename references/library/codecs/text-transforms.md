# codecs - Text Transforms

### Text Transforms

A text transform — a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) to `str` mapping — is what the codec below supplies. You cannot reach it through [`str.encode()`](https://docs.python.org/3.14/library/stdtypes.html#str.encode), since that yields nothing but [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) output.

| Codec | Aliases | Meaning |
| --- | --- | --- |
| rot_13 | rot13 | Hand back the operand run through Caesar-cypher encryption. |

Added in version 3.2: The `rot_13` text transform was brought back.

Changed in version 3.4: The `rot13` alias was brought back.

[Subject index](INDEX.md) · [Previous](codecs-escape-encode-to-codecs-escape-decode.md) · [Continue](../encodings/encodings-normalize-encoding-to-encodings-codecregistryerror.md) · [Owning module, declaration or section: codecs](codecs-encode-to-codecs-lookup.md)
