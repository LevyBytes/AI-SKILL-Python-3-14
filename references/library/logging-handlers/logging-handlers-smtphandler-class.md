# logging.handlers: `logging.handlers.SMTPHandler`

### SMTPHandler

Living in the `logging.handlers` module, the `SMTPHandler` class lets you deliver logging messages to an email address over SMTP.

 *class *logging.handlers.SMTPHandler(*mailhost*, *fromaddr*, *toaddrs*, *subject*, *credentials=None*, *secure=None*, *timeout=1.0*)

Hands back a fresh instance of the `SMTPHandler` class. Its setup takes the email's from and to addresses along with the subject line. The *toaddrs* should be a list of strings. For a non-standard SMTP port, give the *mailhost* argument as a (host, port) tuple; pass a plain string and the standard SMTP port applies. Where your SMTP server demands authentication, you may give a (username, password) tuple as the *credentials* argument.

To call for a secure protocol (TLS), hand a tuple to the *secure* argument. It comes into play only when authentication credentials have been supplied. That tuple should be one of: an empty tuple; a one-value tuple naming a keyfile; or a two-value tuple naming the keyfile and the certificate file. (The tuple is forwarded to the [`smtplib.SMTP.starttls()`](https://docs.python.org/3.14/library/smtplib.html#smtplib.SMTP.starttls) method.)

By way of the *timeout* argument you can set a timeout for talking to the SMTP server.

Changed in version 3.3: Added the *timeout* parameter.

[Subject index](INDEX.md) · [Previous](windows-event-log-handler-lifecycle-and-message-id.md) · [Continue](smtp-handler-emission-and-subject.md) · [Owning module, declaration or section: logging.handlers](handler-types-overview.md)
