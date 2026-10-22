# email.errors: Email parse errors and header-separator defects

## email.errors: Exception and Defect classes

### `email.errors`: Exception and Defect classes

**Source code:** [Lib/email/errors.py](https://github.com/python/cpython/tree/3.14/Lib/email/errors.py)

---

These exception classes are declared within the `email.errors` module:

 *exception *email.errors.MessageError

This serves as the root class for every exception the [`email`](https://docs.python.org/3.14/library/email.html#module-email) package may raise. It descends from the standard [`Exception`](https://docs.python.org/3.14/library/exceptions.html#Exception) class and adds no methods of its own.

 *exception *email.errors.MessageParseError

This is the parent class for exceptions thrown by the [`Parser`](https://docs.python.org/3.14/library/email.parser.html#email.parser.Parser) class. It descends from `MessageError`. The parser that [`headerregistry`](https://docs.python.org/3.14/library/email.headerregistry.html#module-email.headerregistry) relies on also uses this class internally.

 *exception *email.errors.HeaderParseError

Thrown under certain error conditions while parsing the [**RFC 5322**](https://datatracker.ietf.org/doc/html/rfc5322.html) headers of a message, this class descends from `MessageParseError`. The [`set_boundary()`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage.set_boundary) method raises this error when the content type is unknown at the point the method runs. [`Header`](https://docs.python.org/3.14/library/email.header.html#email.header.Header) may throw it for some base64 decoding failures, and whenever something tries to build a header that looks like it embeds another header (meaning what should be a continuation line carries no leading whitespace and resembles a header).

 *exception *email.errors.BoundaryError

Deprecated and no longer used.

 *exception *email.errors.MultipartConversionError

Thrown when the [`attach()`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message.attach) method runs against an instance of a class that descends from [`MIMENonMultipart`](https://docs.python.org/3.14/library/email.mime.html#email.mime.nonmultipart.MIMENonMultipart) (for instance [`MIMEImage`](https://docs.python.org/3.14/library/email.mime.html#email.mime.image.MIMEImage)). `MultipartConversionError` inherits from both `MessageError` and the built-in [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

 *exception *email.errors.HeaderWriteError

Thrown when something goes wrong as the [`generator`](https://docs.python.org/3.14/library/email.generator.html#module-email.generator) emits headers.

 *exception *email.errors.MessageDefect

This is the root class for every defect uncovered while parsing email messages. It descends from [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError).

 *exception *email.errors.HeaderDefect

This is the root class for every defect uncovered while parsing email headers. It descends from `MessageDefect`.

Below is the catalog of defects the [`FeedParser`](https://docs.python.org/3.14/library/email.parser.html#email.parser.FeedParser) may detect during message parsing. Keep in mind that a defect is attached to the message where the trouble was spotted; thus, for instance, if a message nested within a *multipart/alternative* carried a malformed header, that nested message object would hold a defect while the messages enclosing it would not.

Every defect class is a subclass of `email.errors.MessageDefect`.

 *exception *email.errors.NoBoundaryInMultipartDefect

A message asserted that it was a multipart yet supplied no *boundary* parameter.

 *exception *email.errors.StartBoundaryNotFoundDefect

The start boundary announced in the *Content-Type* header turned up nowhere.

 *exception *email.errors.CloseBoundaryNotFoundDefect

A start boundary turned up, but its matching close boundary never did.

Added in version 3.3.

 *exception *email.errors.FirstHeaderLineIsContinuationDefect

The message began its header block with a continuation line.

 *exception *email.errors.MisplacedEnvelopeHeaderDefect

A “Unix From” header appeared partway through a header block.

 *exception *email.errors.MissingHeaderBodySeparatorDefect

While parsing headers, a line surfaced that lacked any leading white space yet held no ‘:’. Parsing proceeds on the assumption that this line is the body’s first line.

Added in version 3.3.

[Subject index](INDEX.md) · [Continue](malformed-email-header-defects.md)
