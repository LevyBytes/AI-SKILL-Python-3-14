# codecs — Text Encodings

### Text Encodings

The codecs below furnish [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) to [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) encoding plus [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) to `str` decoding, akin to the Unicode text encodings.

| Codec | Aliases | Meaning |
| --- | --- | --- |
| idna |  | Implement **RFC 3490**, see also `encodings.idna`. Only `errors='strict'` is supported. |
| mbcs | ansi, dbcs | Windows only: Encode the operand according to the ANSI codepage (CP_ACP). |
| oem |  | Windows only: Encodes the operand using the OEM codepage (CP_OEMCP). Added in version 3.6. |
| palmos |  | Encoding of PalmOS 3.5. |
| punycode |  | Implement **RFC 3492**. Stateful codecs are not supported. |
| raw_unicode_escape |  | Latin-1 encoding that uses `\u*XXXX*` and `\U*XXXXXXXX*` to cover the remaining code points. Backslashes already present get no escaping whatsoever. The Python pickle protocol relies on it. |
| undefined |  | Reserve this Codec for testing alone. Every conversion, the empty string included, raises an exception. Whatever error handler is set gets disregarded. |
| unicode_escape |  | An encoding fit to serve as the body of a Unicode literal within ASCII-encoded Python source code, save that quotes go unescaped. Decoding treats the input as Latin-1 source code. Take care: by default, Python source code in fact uses UTF-8. |

Changed in version 3.8: “unicode_internal” codec is removed.

[Subject index](INDEX.md) · [Previous](python-specific-encodings.md) · [Continue](binary-transforms.md) · [Owning module, declaration or section: codecs](codecs-encode-to-codecs-lookup.md)
