# email.mime`email.mime`: Creating email and MIME objects from scratch

*class *email.mime.application.MIMEApplication(*_data*, *_subtype='octet-stream'*, *_encoder=email.encoders.encode_base64*, ***, *policy=compat32*, ***_params*)

Module: `email.mime.application`

Derived from `MIMENonMultipart`, the `MIMEApplication` class stands in for MIME message objects whose major type is *application*. *_data* holds the bytes of the raw application data. The optional *_subtype* names the MIME subtype and defaults to *octet-stream*.

The optional *_encoder* is a callable (that is, a function) tasked with carrying out the data's actual encoding for transport. That callable receives a single argument, the `MIMEApplication` instance. It is expected to call [`get_payload()`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message.get_payload) and [`set_payload()`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message.set_payload) to swap the payload over to its encoded form. It should as well attach whatever *Content-Transfer-Encoding* or other headers the message object needs. base64 is the default encoding. Consult the [`email.encoders`](https://docs.python.org/3.14/library/email.encoders.html#module-email.encoders) module for the roster of built-in encoders.

The optional *policy* argument defaults to [`compat32`](https://docs.python.org/3.14/library/email.policy.html#email.policy.Compat32).

*_params* travel directly into the base class constructor.

Changed in version 3.6: Added *policy* keyword-only parameter.

[Subject index](INDEX.md) · [Previous](email-mime-multipart-mimemultipart-class.md) · [Continue](email-mime-audio-mimeaudio-class.md) · [Owning module, declaration or section: email.mime](email-mime-base-mimebase-class.md)
