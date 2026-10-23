# email.encoders`email.encoders`: Encoders

## email.encoders: Encoders

### `email.encoders`: Encoders

**Source code:** [Lib/email/encoders.py](https://github.com/python/cpython/tree/3.14/Lib/email/encoders.py)

---

This module belongs to the legacy (`Compat32`) email API. Within the new API the same capability comes from the *cte* parameter on the [`set_content()`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage.set_content) method.

Within Python 3 this module is deprecated. You should not call the functions here directly, because the [`MIMEText`](https://docs.python.org/3.14/library/email.mime.html#email.mime.text.MIMEText) class already establishes the content type and CTE header from the *_subtype* and *_charset* values handed in when an instance of that class is created.

What follows below in this section is the module’s original documentation.

While building [`Message`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message) objects from the ground up, you frequently must encode the payloads so they travel safely through standards-conforming mail servers. That holds in particular for *image/** and *text/** style messages that carry binary data.

The [`email`](https://docs.python.org/3.14/library/email.html#module-email) package ships several handy encoders within its `encoders` module. Those encoders are in fact what the [`MIMEAudio`](https://docs.python.org/3.14/library/email.mime.html#email.mime.audio.MIMEAudio) and [`MIMEImage`](https://docs.python.org/3.14/library/email.mime.html#email.mime.image.MIMEImage) class constructors call to supply their default encodings. Every encoder function accepts precisely one argument: the message object to be encoded. They typically read out the payload, encode it, and write the freshly encoded value back as the payload. They are also expected to set the *Content-Transfer-Encoding* header to a fitting value.

Be aware that these functions carry no meaning for a multipart message. You have to apply them to the individual subparts instead; handing one a message whose type is multipart raises a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

The encoding functions on offer are:

 email.encoders.encode_quopri(*msg*)

Converts the payload to quoted-printable form and assigns `quoted-printable` to the *Content-Transfer-Encoding* header [1]. This encoding works well when the bulk of your payload is ordinary printable data but holds a handful of unprintable characters.

 email.encoders.encode_base64(*msg*)

Converts the payload to base64 form and assigns `base64` to the *Content-Transfer-Encoding* header. This encoding suits payloads that are mostly unprintable data, as it is more compact than quoted-printable. Its downside is that base64 makes the text unreadable to humans.

 email.encoders.encode_7or8bit(*msg*)

This leaves the message’s payload untouched, yet it does set the *Content-Transfer-Encoding* header to whichever of `7bit` or `8bit` fits, judging from the payload data.

 email.encoders.encode_noop(*msg*)

This performs no action whatsoever; it does not even set the *Content-Transfer-Encoding* header.

Footnotes

[Subject index](INDEX.md) · [Continue](../email-errors/email-parse-errors-and-header-separator-defects.md)
