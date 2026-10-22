# email.parser.BytesFeedParser: `feed()`, `close()`

`feed(*data*)`

Hand the parser additional input. The *data* you supply ought to be a [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) holding one line or several. Fragments are fine — the parser knits broken lines back together correctly. Whatever line terminators you use are accepted: a bare carriage return, a bare newline, or the carriage-return-plus-newline pair, and you may even intermix them.

`close()`

Finish parsing everything fed so far and hand back the root message object. Behaviour is unspecified should `feed()` be invoked once this call has run.

[Subject index](INDEX.md) · [Previous](email-parser-bytesfeedparser-class.md) · [Continue](email-parser-feedparser-class.md) · [Owning module, declaration or section: email.parser](email-parser-parsing-email-messages.md) · [Owning module, declaration or section: email.parser.BytesFeedParser](email-parser-bytesfeedparser-class.md) · [Owning module, declaration or section: FeedParser API](email-parser-bytesfeedparser-class.md)
