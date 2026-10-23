# email.mime`email.mime`: Creating email and MIME objects from scratch

# Email.Mime

### `email.mime`: Creating email and MIME objects from scratch

**Source code:** [Lib/email/mime/](https://github.com/python/cpython/tree/3.14/Lib/email/mime/)

---

This module belongs to the legacy (`Compat32`) email API. In the newer API its role is taken over in part by the [`contentmanager`](https://docs.python.org/3.14/library/email.contentmanager.html#module-email.contentmanager), yet for some applications these classes can still earn their keep, even outside legacy code.

Typically you obtain a message object structure by feeding a file or some text into a parser, which works through the text and returns the root message object. That said, you are equally free to assemble a full message structure yourself, or even to hand-craft individual [`Message`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message) objects. You may likewise take a structure that already exists and tack on new `Message` objects, shuffle them about, and so on. The upshot is a rather handy interface for slicing-and-dicing MIME messages.

To build a new object structure, you instantiate [`Message`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message) objects and attach the payloads plus every fitting header by hand. For MIME messages specifically, though, the [`email`](https://docs.python.org/3.14/library/email.html#module-email) package supplies a few convenient subclasses that lighten the work.

The classes are these:

 *class *email.mime.base.MIMEBase(*_maintype*, *_subtype*, ***, *policy=compat32*, ***_params*)

Module: `email.mime.base`

This serves as the base class underlying all of the MIME-specific subclasses of [`Message`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message). As a rule you would not directly instantiate `MIMEBase` itself, even though it is permitted. `MIMEBase` exists mainly to act as a convenient base class for the more targeted MIME-aware subclasses.

*_maintype* gives the *Content-Type* major type (for instance *text* or *image*), while *_subtype* gives the *Content-Type* minor type (for instance *plain* or *gif*). *_params* is a dictionary of parameter keys and values that gets forwarded as-is to [`Message.add_header`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message.add_header).

When *policy* is given (its default being the [`compat32`](https://docs.python.org/3.14/library/email.policy.html#email.policy.Compat32) policy), it is forwarded on to [`Message`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message).

The `MIMEBase` class invariably attaches a *Content-Type* header (derived from *_maintype*, *_subtype*, and *_params*) along with a *MIME-Version* header (forever fixed at `1.0`).

Changed in version 3.6: Added *policy* keyword-only parameter.

[Subject index](INDEX.md) · [Continue](email-mime-nonmultipart-mimenonmultipart-class.md)
