# email.mime — `email.mime`: Creating email and MIME objects from scratch

*class *email.mime.multipart.MIMEMultipart(*_subtype='mixed'*, *boundary=None*, *_subparts=None*, ***, *policy=compat32*, ***_params*)

Module: `email.mime.multipart`

Derived from `MIMEBase`, this stands as an intermediate base class covering MIME messages that are *multipart*. The optional *_subtype* defaults to *mixed* but may be set to declare the message's subtype. A *Content-Type* header reading *multipart/_subtype* gets appended to the message object, and a *MIME-Version* header is appended as well.

The optional *boundary* is the multipart boundary string. With `None` (its default), the boundary is worked out as needed (for example, at the point the message is serialized).

*_subparts* is a sequence of starting subparts for the payload. It has to be convertible into a list. At any time you can append fresh subparts to the message through the [`Message.attach`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message.attach) method.

The optional *policy* argument defaults to [`compat32`](https://docs.python.org/3.14/library/email.policy.html#email.policy.Compat32).

Further parameters for the *Content-Type* header are drawn from the keyword arguments, or handed in through the *_params* argument, which is a keyword dictionary.

Changed in version 3.6: Added *policy* keyword-only parameter.

[Subject index](INDEX.md) · [Previous](email-mime-nonmultipart-mimenonmultipart-class.md) · [Continue](email-mime-application-mimeapplication-class.md) · [Owning module, declaration or section: email.mime](email-mime-base-mimebase-class.md)
