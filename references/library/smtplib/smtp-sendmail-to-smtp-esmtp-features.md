# smtplib: `SMTP.sendmail()`, `SMTP.send_message()`, `SMTP.quit()`, `SMTP.helo_resp`, `SMTP.ehlo_resp`, `SMTP.does_esmtp`, `SMTP.esmtp_features`

SMTP.sendmail(*from_addr*, *to_addrs*, *msg*, *mail_options=()*, *rcpt_options=()*)

Send mail. What you must pass in is an [**RFC 822**](https://datatracker.ietf.org/doc/html/rfc822.html) from-address string, then a list of [**RFC 822**](https://datatracker.ietf.org/doc/html/rfc822.html) to-address strings (a plain string is handled as a list with 1 address), and finally a message string. As *mail_options*, the caller may supply a list of ESMTP options (for example `"8bitmime"`) for use in `MAIL FROM` commands. ESMTP options (for example `DSN` commands) meant to apply to every `RCPT` command can be supplied as *rcpt_options*. Each option must be given as a string holding the option's full text, including any potential key (for example, `"NOTIFY=SUCCESS,FAILURE"`). (When you need distinct ESMTP options for distinct recipients you must fall back on the low-level methods such as `mail()`, `rcpt()` and `data()` to send the message.)

Note

The *from_addr* and *to_addrs* parameters serve to build the message envelope that the transport agents use. `sendmail` leaves the message headers entirely unchanged.

*msg* may be a string holding characters within the ASCII range, or it may be a byte string. A string is encoded into bytes with the ascii codec, and stray `\r` and `\n` characters become `\r\n` characters. A byte string stays untouched.

When no `EHLO` or `HELO` command has yet been sent during this session, the method attempts ESMTP `EHLO` first. When the server does ESMTP, the message size and each named option are forwarded to it (provided the option is among the features the server advertises). Should `EHLO` fail, `HELO` is attempted and ESMTP options are suppressed.

The method returns normally when the mail is accepted for at least one recipient. Failing that, it raises an exception. In other words, if the method does not raise an exception, somebody ought to receive your mail. When the method does not raise an exception, it returns a dictionary holding one entry per recipient that was refused. Each entry holds a tuple of the SMTP error code and the matching error message the server sent.

When `SMTPUTF8` appears in *mail_options* and the server supports it, *from_addr* and *to_addrs* may hold non-ASCII characters.

The method may raise the following exceptions:

`SMTPRecipientsRefused`

Every recipient was refused. No one received the mail.

`SMTPHeloError`

The server failed to respond correctly to the `HELO` greeting.

`SMTPSenderRefused`

The server declined the *from_addr*.

`SMTPDataError`

The server answered with an unexpected error code (something other than a recipient refusal).

`SMTPNotSupportedError`

`SMTPUTF8` was supplied in *mail_options* but the server does not support it.

Unless stated otherwise, the connection stays open even after an exception is raised.

Changed in version 3.2: *msg* may be a byte string.

Changed in version 3.5: `SMTPUTF8` support added, and `SMTPNotSupportedError` may be raised when `SMTPUTF8` is specified but the server does not support it.

 SMTP.send_message(*msg*, *from_addr=None*, *to_addrs=None*, *mail_options=()*, *rcpt_options=()*)

This convenience method calls `sendmail()` with the message held in an [`email.message.Message`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message) object. The arguments mean the same thing as for `sendmail()`, except that *msg* is a `Message` object.

When *from_addr* is `None` or *to_addrs* is `None`, `send_message` populates those arguments with addresses pulled from the headers of *msg* per [**RFC 5322**](https://datatracker.ietf.org/doc/html/rfc5322.html): *from_addr* is taken from the *Sender* field when present, and otherwise from the *From* field. *to_addrs* combines whatever values are present across the *msg* fields *To*, *Cc*, and *Bcc*. When precisely one set of *Resent-** headers occurs in the message, the ordinary headers are disregarded and the *Resent-** headers stand in for them. Should the message carry several sets of *Resent-** headers, a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) results, because nothing reliably identifies which group of *Resent-* headers came last.

`send_message` serializes *msg* with [`BytesGenerator`](https://docs.python.org/3.14/library/email.generator.html#email.generator.BytesGenerator) using `\r\n` as the *linesep*, then calls `sendmail()` to transmit the resulting message. No matter what *from_addr* and *to_addrs* hold, `send_message` does not transmit any *Bcc* or *Resent-Bcc* headers that may occur in *msg*. Should any address among *from_addr* and *to_addrs* carry non-ASCII characters while the server advertises no `SMTPUTF8` support, an `SMTPNotSupportedError` results. Failing that, the `Message` gets serialized using a clone of its [`policy`](https://docs.python.org/3.14/library/email.policy.html#module-email.policy) in which the [`utf8`](https://docs.python.org/3.14/library/email.policy.html#email.policy.EmailPolicy.utf8) attribute is set to `True`, and both `SMTPUTF8` and `BODY=8BITMIME` get added to *mail_options*.

Added in version 3.2.

Added in version 3.5: Support for internationalized addresses (`SMTPUTF8`).

 SMTP.quit()

Wrap up the SMTP session and shut the connection. Hand back whatever the SMTP `QUIT` command yields.

Low-level methods matching the standard SMTP/ESMTP commands `HELP`, `RSET`, `NOOP`, `MAIL`, `RCPT`, and `DATA` are supported too. Ordinarily there is no need to call these directly, so they are left undocumented here. For particulars, see the module code.

An SMTP instance additionally carries the following attributes:

 SMTP.helo_resp

The response to the `HELO` command, see `helo()`.

 SMTP.ehlo_resp

The response to the `EHLO` command, see `ehlo()`.

 SMTP.does_esmtp

A boolean value reflecting whether the server supports ESMTP, see `ehlo()`.

 SMTP.esmtp_features

A dictionary of the names of SMTP service extensions the server supports, see `ehlo()`.

[Subject index](INDEX.md) · [Previous](smtp-auth-to-smtp-starttls.md) · [Continue](smtp-example.md) · [Owning module, declaration or section: smtplib](smtplib-smtp-class.md) · [Owning module, declaration or section: SMTP Objects](smtp-set-debuglevel-to-smtp-login.md)
