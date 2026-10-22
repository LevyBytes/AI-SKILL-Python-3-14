# codecs: `codecs.backslashreplace_errors()`, `codecs.xmlcharrefreplace_errors()`, `codecs.namereplace_errors()`

codecs.backslashreplace_errors(*exception*)

Implements the `'backslashreplace'` error handling.

The malformed data gives way to a backslashed escape sequence. When encoding, render the Unicode code point in hexadecimal via the formats `\x*hh*` `\u*xxxx*` `\U*xxxxxxxx*`; when decoding, render the byte value in hexadecimal via the format `\x*hh*`.

Changed in version 3.5: Works with decoding and translating.

 codecs.xmlcharrefreplace_errors(*exception*)

Implements the `'xmlcharrefreplace'` error handling (for encoding within [text encoding](https://docs.python.org/3.14/glossary.html#term-text-encoding) only).

A fitting XML/HTML numeric character reference stands in for the unencodable character; it is a decimal form of Unicode code point with format `&#*num*;` .

 codecs.namereplace_errors(*exception*)

Implements the `'namereplace'` error handling (for encoding within [text encoding](https://docs.python.org/3.14/glossary.html#term-text-encoding) only).

A `\N{...}` escape sequence stands in for the unencodable character. Whatever sits inside the braces is the Name property drawn from the Unicode Character Database. As an example, the German lowercase letter `'ß'` becomes the byte sequence `\N{LATIN SMALL LETTER SHARP S}` .

Added in version 3.5.

[Subject index](INDEX.md) · [Previous](codecs-register-error-to-codecs-replace-errors.md) · [Continue](codecs-codec-class-to-encode.md) · [Owning module, declaration or section: codecs](codecs-encode-to-codecs-lookup.md) · [Owning module, declaration or section: Error Handlers](codecs-register-error-to-codecs-replace-errors.md)
