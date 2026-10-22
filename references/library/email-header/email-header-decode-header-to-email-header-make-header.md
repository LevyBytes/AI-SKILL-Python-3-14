# email.header: `email.header.decode_header()`, `email.header.make_header()`

email.header.decode_header(*header*)

Decode a message header value while leaving the character set unconverted. That header value is carried in *header*.

Owing to history, this function can give back one of two things:

1.

A list of pairs, one per decoded portion of the header, shaped as `(decoded_bytes, charset)`, in which *decoded_bytes* is invariably a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) instance and *charset* is one of:

>
  - A lower-case string holding the name of whichever character set was specified.

  - `None` wherever the header part was not encoded.

2.

A one-element list holding a single pair `(string, None)`, in which *string* is invariably a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) instance.

Certain decoding failures — a base64 decoding exception, say — can prompt an [`email.errors.HeaderParseError`](https://docs.python.org/3.14/library/email.errors.html#email.errors.HeaderParseError).

A few examples follow:

```python
>>> from email.header import decode_header
>>> decode_header('=?iso-8859-1?q?p=F6stal?=')
[(b'p\xf6stal', 'iso-8859-1')]
>>> decode_header('unencoded_string')
[('unencoded_string', None)]
>>> decode_header('bar =?utf-8?B?ZsOzbw==?=')
[(b'bar ', None), (b'f\xc3\xb3o', 'utf-8')]

```

Note

This function is kept around purely for backwards compatibility. In fresh code, lean on [`email.headerregistry.HeaderRegistry`](https://docs.python.org/3.14/library/email.headerregistry.html#email.headerregistry.HeaderRegistry) instead.

 email.header.make_header(*decoded_seq*, *maxlinelen=None*, *header_name=None*, *continuation_ws=' '*)

Build a `Header` instance out of a sequence of pairs of the kind `decode_header()` produces.

Given a header value string, `decode_header()` yields a sequence of pairs shaped as `(decoded_string, charset)`, with *charset* being the character set's name.

Hand one such sequence of pairs to this function and it gives back a `Header` instance. The optional *maxlinelen*, *header_name*, and *continuation_ws* match those of the `Header` constructor.

Note

This function lives on solely for backwards compatibility, and reaching for it in new code is discouraged.

[Subject index](INDEX.md) · [Previous](email-header-header-append-to-email-header-header-ne.md) · [Owning module, declaration or section: email.header](email-header-header-class.md)
