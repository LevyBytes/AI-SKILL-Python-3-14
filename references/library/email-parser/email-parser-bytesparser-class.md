# email.parser: `email.parser.BytesParser`

### Parser API

Pulled in from the `email.parser` module, the `BytesParser` class gives you an interface for parsing a message whose entire contents already sit in a [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) or a file. That same `email.parser` module supplies `Parser` for string input, along with the headers-only variants `BytesHeaderParser` and `HeaderParser` for when nothing but the message headers matters to you. Because `BytesHeaderParser` and `HeaderParser` skip the body entirely — leaving the payload as the raw body — they run considerably quicker in those cases.

`*class *email.parser.BytesParser(*_class=None*, ***, *policy=policy.compat32*)`

Build a `BytesParser`. Its *_class* and *policy* parameters carry exactly the same meaning and behaviour as the *_factory* and *policy* parameters over on `BytesFeedParser`.

Note: **The policy keyword should always be specified**; a coming Python release will switch the default over to [`email.policy.default`](https://docs.python.org/3.14/library/email.policy.html#email.policy.default).

Changed in version 3.3: The *strict* argument, deprecated back in 2.4, is gone; the *policy* keyword arrived.

Changed in version 3.6: *_class* defaults to the policy `message_factory`.

[Subject index](INDEX.md) · [Previous](email-parser-feedparser-class.md) · [Continue](byte-parser-stream-and-buffer-input.md) · [Owning module, declaration or section: email.parser](email-parser-parsing-email-messages.md)
