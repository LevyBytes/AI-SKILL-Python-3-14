# email.parser: `email.parser.FeedParser`

`*class *email.parser.FeedParser(*_factory=None*, ***, *policy=policy.compat32*)`

Behaves just like `BytesFeedParser`, save that what you pass to its `feed()` method has to be a string. That restricts its usefulness, because for the resulting message to be valid it must hold ASCII only — or, when [`utf8`](https://docs.python.org/3.14/library/email.policy.html#email.policy.EmailPolicy.utf8) is `True`, carry no binary attachments.

Changed in version 3.3: Added the *policy* keyword.

[Subject index](INDEX.md) · [Previous](incremental-byte-parser-feed-and-close.md) · [Continue](email-parser-bytesparser-class.md) · [Owning module, declaration or section: email.parser](email-parser-parsing-email-messages.md) · [Owning module, declaration or section: FeedParser API](email-parser-bytesfeedparser-class.md)
