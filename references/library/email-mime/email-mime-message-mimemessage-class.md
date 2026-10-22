# email.mime — `email.mime`: Creating email and MIME objects from scratch

*class *email.mime.message.MIMEMessage(*_msg*, *_subtype='rfc822'*, ***, *policy=compat32*)

Module: `email.mime.message`

Derived from `MIMENonMultipart`, the `MIMEMessage` class builds MIME objects whose main type is *message*. *_msg* acts as the payload and is required to be an instance of the [`Message`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message) class (or one of its subclasses); if it is not, a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) is raised.

The optional *_subtype* establishes the message's subtype and defaults to *rfc822*.

The optional *policy* argument defaults to [`compat32`](https://docs.python.org/3.14/library/email.policy.html#email.policy.Compat32).

Changed in version 3.6: Added *policy* keyword-only parameter.

[Subject index](INDEX.md) · [Previous](email-mime-image-mimeimage-class.md) · [Continue](email-mime-text-mimetext-class.md) · [Owning module, declaration or section: email.mime](email-mime-base-mimebase-class.md)
