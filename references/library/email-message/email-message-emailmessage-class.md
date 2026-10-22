# email.message: `email.message.EmailMessage`

### `email.message`: Representing an email message

**Source code:** [Lib/email/message.py](https://github.com/python/cpython/tree/3.14/Lib/email/message.py)

---

Added in version 3.6: [1]

Within the [`email`](https://docs.python.org/3.14/library/email.html#module-email) package, the principal class is `EmailMessage`, which you import from the `email.message` module. This class serves as the foundation for the `email` object model. The core capabilities offered by `EmailMessage` cover assigning and querying header fields, reaching message bodies, and building or altering structured messages.

Every email message is made up of *headers* together with a *payload* (which also goes by the name *content*). Headers follow [**RFC 5322**](https://datatracker.ietf.org/doc/html/rfc5322.html) or [**RFC 6532**](https://datatracker.ietf.org/doc/html/rfc6532.html) conventions for field names and values, with a colon separating the name from the value. That colon belongs to neither the field name nor the field value. A payload can take the form of plain text, a binary object, or an organized series of sub-messages, each carrying its own headers and its own payload. A message whose MIME type is something like *multipart/** or *message/rfc822* signals this last kind of payload.

You can think of an `EmailMessage` object as an ordered dictionary of headers paired with a *payload* standing for the [**RFC 5322**](https://datatracker.ietf.org/doc/html/rfc5322.html) body of the message, which itself may be a list of sub-`EmailMessage` objects. Beyond the usual dictionary operations for reading header names and values, the class supplies methods for pulling specialized data out of the headers (the MIME content type, say), for working on the payload, for producing a serialized form of the message, and for traversing the object tree recursively.

Header names index the dictionary-like interface of `EmailMessage`, and those names are required to be ASCII values. What the dictionary returns are strings that carry a few additional methods. Although headers keep their original case when stored and retrieved, field names compare case-insensitively. While the keys keep an order, duplicates are allowed here, in contrast to a genuine dict. Extra methods exist to help you deal with headers whose keys repeat.

For simple message objects the *payload* is a string or bytes object, whereas for MIME container documents like *multipart/** and *message/rfc822* message objects it is a list of `EmailMessage` objects.

 *class *email.message.EmailMessage(*policy=default*)

When *policy* is supplied, its rules govern how the representation of the message is updated and serialized. When no *policy* is given, the [`default`](https://docs.python.org/3.14/library/email.policy.html#email.policy.default) policy applies; it honors the email RFCs apart from line endings (rather than the `\r\n` the RFC requires, it employs the standard Python `\n` line endings). Consult the [`policy`](https://docs.python.org/3.14/library/email.policy.html#module-email.policy) documentation for further detail. [2]

[Subject index](INDEX.md) · [Continue](email-message-serialization-and-header-assignment.md)
