# email.parser - Additional notes

### Additional notes

A few observations about how the parsing behaves follow:

- The bulk of messages whose type is not *multipart* parse into one message object carrying a string payload. Such objects answer `False` to [`is_multipart()`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage.is_multipart), and their [`iter_parts()`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage.iter_parts) produces nothing but an empty list.

- Every message of *multipart* type parses into a container message object whose payload is a list of nested sub-message objects. That outer container answers `True` to [`is_multipart()`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage.is_multipart), while [`iter_parts()`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage.iter_parts) produces a list of the subparts.

- Messages whose content type begins with *message/** — *message/delivery-status* and *message/rfc822* are typical — likewise parse into a container object, but one whose list payload holds just a single entry. For these the [`is_multipart()`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage.is_multipart) method answers `True`, and the lone item that [`iter_parts()`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage.iter_parts) yields is a sub-message object.

- Certain messages that flout the standards turn out internally inconsistent about whether they are *multipart*. One might carry a *Content-Type* header announcing *multipart*, yet have its [`is_multipart()`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage.is_multipart) method answer `False`. Should the `FeedParser` handle such a message, it lodges a [`MultipartInvariantViolationDefect`](https://docs.python.org/3.14/library/email.errors.html#email.errors.MultipartInvariantViolationDefect) instance in the message's *defects* list. Turn to [`email.errors`](https://docs.python.org/3.14/library/email.errors.html#module-email.errors) for the particulars.

[Subject index](INDEX.md) · [Previous](email-parser-headerparser-class-to-email-message-from-file.md) · [Owning module, declaration or section: email.parser](email-parser-parsing-email-messages.md)
