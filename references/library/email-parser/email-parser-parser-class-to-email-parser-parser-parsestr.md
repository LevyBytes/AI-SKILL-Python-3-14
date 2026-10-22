# email.parser / Parser API: `email.parser.Parser`, `parse()`, `parsestr()`

`*class *email.parser.Parser(*_class=None*, ***, *policy=policy.compat32*)`

A counterpart to `BytesParser` that deals in string input rather than bytes.

Changed in version 3.3: Dropped the *strict* argument; introduced the *policy* keyword.

Changed in version 3.6: *_class* defaults to the policy `message_factory`.

`parse(*fp*, *headersonly=False*)`

Consume all the content of the text-mode file-like object *fp*, parse the text you obtain, and return the root message object. The *fp* you give it must provide both the [`readline()`](https://docs.python.org/3.14/library/io.html#io.TextIOBase.readline) and the [`read()`](https://docs.python.org/3.14/library/io.html#io.TextIOBase.read) methods that file-like objects offer.

Setting aside the demand for text mode, this method behaves the way `BytesParser.parse()` does.

`parsestr(*text*, *headersonly=False*)`

Akin to the `parse()` method, but it accepts a string rather than a file-like object. Invoking it on a string is the same as wrapping *text* inside a [`StringIO`](https://docs.python.org/3.14/library/io.html#io.StringIO) first and then calling `parse()`.

The optional *headersonly* behaves just as it does for the `parse()` method.

[Subject index](INDEX.md) · [Previous](email-parser-bytesheaderparser-class.md) · [Continue](email-parser-headerparser-class-to-email-message-from-file.md) · [Owning module, declaration or section: email.parser](email-parser-parsing-email-messages.md) · [Owning module, declaration or section: Parser API](email-parser-bytesparser-class.md)
