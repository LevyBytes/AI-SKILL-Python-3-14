# email.parser.BytesParser: `parse()`, `parsebytes()`

`parse(*fp*, *headersonly=False*)`

Pull every byte out of the binary file-like object *fp*, parse what you read, and hand back the message object. Your *fp* has to offer both the [`readline()`](https://docs.python.org/3.14/library/io.html#io.IOBase.readline) and the [`read()`](https://docs.python.org/3.14/library/io.html#io.BufferedIOBase.read) methods.

What *fp* holds has to take the shape of a [**RFC 5322**](https://datatracker.ietf.org/doc/html/rfc5322.html) block of headers (or, when [`utf8`](https://docs.python.org/3.14/library/email.policy.html#email.policy.EmailPolicy.utf8) is `True`, [**RFC 6532**](https://datatracker.ietf.org/doc/html/rfc6532.html)) together with their continuation lines, and an envelope header may precede them. Either the end of the input or an empty line marks where the header block stops. Past that block lies the message body — which can hold MIME-encoded subparts, some perhaps bearing a *Content-Transfer-Encoding* of `8bit`.

The optional *headersonly* flag decides whether parsing halts once the headers are read. Its default, `False`, means the whole file gets parsed through.

`parsebytes(*bytes*, *headersonly=False*)`

Much like the `parse()` method, only it accepts a [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) rather than a file-like one. Running it against a bytes-like object amounts to first wrapping *bytes* in a [`BytesIO`](https://docs.python.org/3.14/library/io.html#io.BytesIO) and then calling `parse()`.

The optional *headersonly* works the same here as it does for the `parse()` method.

Added in version 3.2.

[Subject index](INDEX.md) · [Previous](email-parser-bytesparser-class.md) · [Continue](email-parser-bytesheaderparser-class.md) · [Owning module, declaration or section: email.parser](email-parser-parsing-email-messages.md) · [Owning module, declaration or section: email.parser.BytesParser](email-parser-bytesparser-class.md) · [Owning module, declaration or section: Parser API](email-parser-bytesparser-class.md)
