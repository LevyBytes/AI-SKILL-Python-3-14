# email.mime — `email.mime`: Creating email and MIME objects from scratch

*class *email.mime.text.MIMEText(*_text*, *_subtype='plain'*, *_charset=None*, ***, *policy=compat32*)

Module: `email.mime.text`

Derived from `MIMENonMultipart`, the `MIMEText` class builds MIME objects whose major type is *text*. *_text* is the string serving as the payload. *_subtype* is the minor type and defaults to *plain*. *_charset* is the text's character set and gets handed to the `MIMENonMultipart` constructor as an argument; it falls back to `us-ascii` when the string holds only `ascii` code points and to `utf-8` in every other case. The *_charset* parameter takes either a string or a [`Charset`](https://docs.python.org/3.14/library/email.charset.html#email.charset.Charset) instance.

So long as the *_charset* argument is not deliberately set to `None`, the resulting MIMEText object carries both a *Content-Type* header bearing a `charset` parameter and a *Content-Transfer-Encoding* header. Consequently a later `set_payload` call will not yield an encoded payload, even with a charset passed into the `set_payload` command. To “reset” this behavior, remove the `Content-Transfer-Encoding` header; thereafter a `set_payload` call encodes the new payload by itself (and tacks on a fresh *Content-Transfer-Encoding* header).

The optional *policy* argument defaults to [`compat32`](https://docs.python.org/3.14/library/email.policy.html#email.policy.Compat32).

Changed in version 3.5: *_charset* also accepts [`Charset`](https://docs.python.org/3.14/library/email.charset.html#email.charset.Charset) instances.

Changed in version 3.6: Added *policy* keyword-only parameter.

[Subject index](INDEX.md) · [Previous](email-mime-message-mimemessage-class.md) · [Owning module, declaration or section: email.mime](email-mime-base-mimebase-class.md)
