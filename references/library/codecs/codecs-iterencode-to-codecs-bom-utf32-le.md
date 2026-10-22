# codecs: Incremental codec iteration and byte-order marks

codecs.iterencode(*iterator*, *encoding*, *errors='strict'*, ***kwargs*)

Drives an incremental encoder to encode, step by step, the input coming from *iterator*. *iterator* has to yield [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) objects. This function is a [generator](https://docs.python.org/3.14/glossary.html#term-generator). The *errors* argument (along with any other keyword argument) is handed straight to the incremental encoder.

For this to work, the codec has to accept text [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) objects for encoding. As a result, bytes-to-bytes encoders such as `base64_codec` are not supported.

 codecs.iterdecode(*iterator*, *encoding*, *errors='strict'*, ***kwargs*)

Drives an incremental decoder to decode, step by step, the input coming from *iterator*. *iterator* has to yield [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) objects. This function is a [generator](https://docs.python.org/3.14/glossary.html#term-generator). The *errors* argument (along with any other keyword argument) is handed straight to the incremental decoder.

For this to work, the codec has to accept [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) objects for decoding. As a result, text-to-text encoders such as `rot_13` are not supported, though `rot_13` can be applied the same way through `iterencode()`.

 codecs.readbuffer_encode(*buffer*, *errors=None*, */*)

Yield a [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple) that carries the unprocessed bytes drawn from *buffer* — which may be a [buffer-compatible object](https://docs.python.org/3.14/c-api/buffer.html#bufferobjects) or a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) (run through UTF-8 encoding first) — paired with how many bytes those occupy.

The *errors* argument is ignored.

```pycon
>>> codecs.readbuffer_encode(b"Zito")
(b'Zito', 4)

```

The module further defines the constants below, handy when reading from and writing to platform dependent files:

 codecs.BOM

 codecs.BOM_BE

 codecs.BOM_LE

 codecs.BOM_UTF8

 codecs.BOM_UTF16

 codecs.BOM_UTF16_BE

 codecs.BOM_UTF16_LE

 codecs.BOM_UTF32

 codecs.BOM_UTF32_BE

 codecs.BOM_UTF32_LE

Each of these constants stands for a particular byte sequence — the Unicode byte order marks (BOMs) belonging to assorted encodings. Within UTF-16 and UTF-32 data streams they signal which byte order is in effect, and within UTF-8 they act as a Unicode signature. Depending on the platform’s native byte order, `BOM_UTF16` equals either `BOM_UTF16_BE` or `BOM_UTF16_LE`; `BOM` is an alias for `BOM_UTF16`, `BOM_LE` for `BOM_UTF16_LE` and `BOM_BE` for `BOM_UTF16_BE`. The remaining constants give the BOM for the UTF-8 and UTF-32 encodings.

[Subject index](INDEX.md) · [Previous](codecs-getencoder-to-codecs-encodedfile.md) · [Continue](codec-base-classes.md) · [Owning module, declaration or section: codecs](codecs-encode-to-codecs-lookup.md)
