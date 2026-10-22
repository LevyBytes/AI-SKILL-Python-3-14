# email.parser — `email.parser`: Parsing email messages

# Email.Parser

### `email.parser`: Parsing email messages

**Source code:** [Lib/email/parser.py](https://github.com/python/cpython/tree/3.14/Lib/email/parser.py)

---

You have two paths to building a message object tree. One path assembles it directly: instantiate an [`EmailMessage`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage), populate its headers through the mapping-style interface, and attach body content with [`set_content()`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage.set_content) plus its companion methods. The alternative path reads a serialized form of the message and parses it back into objects.

Bundled with the [`email`](https://docs.python.org/3.14/library/email.html#module-email) package is a general-purpose parser that copes with the bulk of email layouts, MIME among them. Hand it bytes, a string, or a file object, and back comes the top-level [`EmailMessage`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage) at the head of the resulting tree. When the message is plain and non-MIME, that top node usually carries the message body as a single string payload. With MIME content, the root answers `True` to [`is_multipart()`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage.is_multipart), and you reach the nested parts through the payload helpers — for instance [`get_body()`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage.get_body), [`iter_parts()`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage.iter_parts), and [`walk()`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage.walk).

In practice the package exposes a pair of parsing interfaces: the `Parser` API and the step-by-step `FeedParser` API. Reach for `Parser` when the whole message text already sits in memory or resides as a file on disk. Prefer `FeedParser` when the data arrives over a stream that may stall while it awaits more bytes — pulling a message off a socket, say. `FeedParser` digests the input piece by piece and hands back the root object only once you close it.

Bear in mind that the supplied parser admits only modest customization, though nothing stops you from writing a replacement entirely on your own. The glue binding the package's built-in parser to the [`email`](https://docs.python.org/3.14/library/email.html#module-email) [`EmailMessage`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage) class lives inside the [`Policy`](https://docs.python.org/3.14/library/email.policy.html#email.policy.Policy) class; by supplying your own overrides of the relevant `Policy` methods, a bespoke parser may assemble object trees however it likes.

[Subject index](INDEX.md) · [Continue](email-parser-bytesfeedparser-class.md)
