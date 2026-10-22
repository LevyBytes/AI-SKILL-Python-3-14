# email.parser: `email.parser.HeaderParser`, `email.message_from_bytes()`, `email.message_from_binary_file()`, `email.message_from_string()`, `email.message_from_file()`

`*class *email.parser.HeaderParser(*_class=None*, ***, *policy=policy.compat32*)`

Identical to `Parser`, save that its *headersonly* defaults to `True`.

Building a message object tree out of a string or a file object comes up so often that four helper functions ship for convenience, all reachable from the top-level [`email`](https://docs.python.org/3.14/library/email.html#module-email) package namespace.

`email.message_from_bytes(*s*, *_class=None*, ***, *policy=policy.compat32*)`

Produce a message object tree out of a [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object). It comes to the same thing as `BytesParser().parsebytes(s)`. Any *_class* and *policy* you pass mean what they do for the `BytesParser` constructor.

Added in version 3.2.

Changed in version 3.3: Took out the *strict* argument and brought in the *policy* keyword.

`email.message_from_binary_file(*fp*, *_class=None*, ***, *policy=policy.compat32*)`

Produce a message object tree out of an open binary [file object](https://docs.python.org/3.14/glossary.html#term-file-object). It comes to the same thing as `BytesParser().parse(fp)`. The *_class* and *policy* mean what they do for the `BytesParser` constructor.

Added in version 3.2.

Changed in version 3.3: The *strict* argument was withdrawn and the *policy* keyword put in.

`email.message_from_string(*s*, *_class=None*, ***, *policy=policy.compat32*)`

Produce a message object tree out of a string. It comes to the same thing as `Parser().parsestr(s)`. The *_class* and *policy* mean what they do for the `Parser` constructor.

Changed in version 3.3: Eliminated the *strict* argument; the *policy* keyword was added in.

`email.message_from_file(*fp*, *_class=None*, ***, *policy=policy.compat32*)`

Produce a message object tree out of an open [file object](https://docs.python.org/3.14/glossary.html#term-file-object). It comes to the same thing as `Parser().parse(fp)`. The *_class* and *policy* mean what they do for the `Parser` constructor.

Changed in version 3.3: Did away with the *strict* argument while adding the *policy* keyword.

Changed in version 3.6: *_class* defaults to the policy `message_factory`.

Below is a short demonstration of calling `message_from_bytes()` from an interactive Python session:

```python
>>> import email
>>> msg = email.message_from_bytes(myBytes)

```

[Subject index](INDEX.md) · [Previous](email-parser-parser-class-to-email-parser-parser-parsestr.md) · [Continue](additional-notes.md) · [Owning module, declaration or section: email.parser](email-parser-parsing-email-messages.md) · [Owning module, declaration or section: Parser API](email-parser-bytesparser-class.md)
