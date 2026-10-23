# email.mime`email.mime`: Creating email and MIME objects from scratch

*class *email.mime.image.MIMEImage(*_imagedata*, *_subtype=None*, *_encoder=email.encoders.encode_base64*, ***, *policy=compat32*, ***_params*)

Module: `email.mime.image`

Derived from `MIMENonMultipart`, the `MIMEImage` class builds MIME message objects whose major type is *image*. *_imagedata* holds the bytes of the raw image data. Should that data type be recognizable (each of `jpeg`, `png`, `gif`, `tiff`, `rgb`, `pbm`, `pgm`, `ppm`, `rast`, `xbm`, `bmp`, `webp`, and `exr` is tried), the subtype is folded into the *Content-Type* header on its own. Otherwise you may state the image subtype outright via the *_subtype* argument. When the minor type cannot be inferred and *_subtype* was left out, a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) is raised.

The optional *_encoder* is a callable (that is, a function) tasked with carrying out the image data's actual encoding for transport. That callable receives a single argument, the `MIMEImage` instance. It is expected to call [`get_payload()`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message.get_payload) and [`set_payload()`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message.set_payload) to swap the payload over to its encoded form. It should as well attach whatever *Content-Transfer-Encoding* or other headers the message object needs. base64 is the default encoding. Consult the [`email.encoders`](https://docs.python.org/3.14/library/email.encoders.html#module-email.encoders) module for the roster of built-in encoders.

The optional *policy* argument defaults to [`compat32`](https://docs.python.org/3.14/library/email.policy.html#email.policy.Compat32).

*_params* travel directly into the `MIMEBase` constructor.

Changed in version 3.6: Added *policy* keyword-only parameter.

[Subject index](INDEX.md) · [Previous](email-mime-audio-mimeaudio-class.md) · [Continue](email-mime-message-mimemessage-class.md) · [Owning module, declaration or section: email.mime](email-mime-base-mimebase-class.md)
