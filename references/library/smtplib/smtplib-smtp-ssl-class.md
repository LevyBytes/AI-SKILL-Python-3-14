# smtplib: `smtplib.SMTP_SSL`

*class *smtplib.SMTP_SSL(*host=''*, *port=0*, *local_hostname=None*, ***, [*timeout*, ]*context=None*, *source_address=None*)

An `SMTP_SSL` instance acts in precisely the same way as instances of `SMTP`. Reach for `SMTP_SSL` when SSL must be active from the very start of the connection and applying `starttls()` would not fit. When *host* is omitted, the local host is used. When *port* is zero, the conventional SMTP-over-SSL port (465) applies. The optional arguments *local_hostname*, *timeout* and *source_address* carry the same significance they hold in the `SMTP` class. *context*, likewise optional, may hold an [`SSLContext`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext) and lets you configure assorted facets of the secure connection. Please review [Security considerations](https://docs.python.org/3.14/library/ssl.html#ssl-security) for best practices.

Changed in version 3.3: *context* was added.

Changed in version 3.3: The *source_address* argument was added.

Changed in version 3.4: Hostname checking via [`ssl.SSLContext.check_hostname`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext.check_hostname) plus *Server Name Indication* (see [`ssl.HAS_SNI`](https://docs.python.org/3.14/library/ssl.html#ssl.HAS_SNI)) is now handled by the class.

Changed in version 3.9: When the *timeout* parameter is given the value zero, a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised so that a non-blocking socket cannot be created

Changed in version 3.12: The *keyfile* and *certfile* parameters, long deprecated, are now gone.

[Subject index](INDEX.md) · [Previous](smtplib-smtp-class.md) · [Continue](smtplib-lmtp-class.md) · [Owning module, declaration or section: smtplib](smtplib-smtp-class.md)
