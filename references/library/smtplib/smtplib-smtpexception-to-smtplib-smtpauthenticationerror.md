# smtplib: SMTP connection, response and authentication exceptions

*exception *smtplib.SMTPException

A subclass of [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) acting as the base exception class behind every other exception this module supplies.

Changed in version 3.4: SMTPException became subclass of [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError)

 *exception *smtplib.SMTPServerDisconnected

This exception fires when the server drops the connection unexpectedly, or when code tries to use the `SMTP` instance before it has connected to a server.

 *exception *smtplib.SMTPResponseException

The base class behind every exception that carries an SMTP error code. Such exceptions arise in certain cases where the SMTP server hands back an error code.

 smtp_code

The error code.

 smtp_error

The error message.

 *exception *smtplib.SMTPSenderRefused

Sender address refused. Beyond the attributes that all `SMTPResponseException` exceptions set, this one also assigns ‘sender’ to the string the SMTP server rejected.

 *exception *smtplib.SMTPRecipientsRefused

All recipient addresses refused.

 recipients

A dictionary of precisely the same form that `SMTP.sendmail()` returns, holding the errors for every recipient.

 *exception *smtplib.SMTPDataError

The SMTP server declined to accept the message data.

 *exception *smtplib.SMTPConnectError

An error arose while a connection with the server was being established.

 *exception *smtplib.SMTPHeloError

The server rejected our `HELO` message.

 *exception *smtplib.SMTPNotSupportedError

The attempted command or option is not supported by the server.

Added in version 3.5.

 *exception *smtplib.SMTPAuthenticationError

SMTP authentication failed. The likeliest cause is that the server rejected the username/password combination supplied.

See also

[**RFC 821**](https://datatracker.ietf.org/doc/html/rfc821.html) - Simple Mail Transfer Protocol

The protocol specification for SMTP. This document lays out the model, operating procedure, and protocol particulars for SMTP.

[**RFC 1869**](https://datatracker.ietf.org/doc/html/rfc1869.html) - SMTP Service Extensions

The specification of the ESMTP extensions to SMTP. It sets out a framework for adding new commands to SMTP, enables dynamic discovery of which commands the server offers, and defines a handful of extra commands.

[Subject index](INDEX.md) · [Previous](smtplib-lmtp-class.md) · [Continue](smtp-set-debuglevel-to-smtp-login.md) · [Owning module, declaration or section: smtplib](smtplib-smtp-class.md)
