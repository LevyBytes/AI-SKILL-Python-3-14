# imaplib: `imaplib.IMAP4_SSL`

*class *imaplib.IMAP4_SSL(*host=''*, *port=IMAP4_SSL_PORT*, ***, *ssl_context=None*, *timeout=None*)

A subclass of `IMAP4` that establishes its link over an SSL encrypted socket (using this class requires a socket module built with SSL support). When *host* is not provided, `''` (the local host) applies. Leaving *port* out selects the standard IMAP4-over-SSL port (993). The *ssl_context* argument is a [`ssl.SSLContext`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext) object that gathers SSL configuration options, certificates and private keys into one (potentially long-lived) structure. Please read [Security considerations](https://docs.python.org/3.14/library/ssl.html#ssl-security) for best practices.

The optional *timeout* parameter gives a timeout in seconds for the connection attempt. When timeout is absent or set to `None`, the global default socket timeout governs.

Changed in version 3.3: *ssl_context* parameter was added.

Changed in version 3.4: Hostname checking via [`ssl.SSLContext.check_hostname`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext.check_hostname) and *Server Name Indication* (see [`ssl.HAS_SNI`](https://docs.python.org/3.14/library/ssl.html#ssl.HAS_SNI)) is now handled by the class.

Changed in version 3.9: The optional *timeout* parameter was added.

Changed in version 3.12: The *keyfile* and *certfile* parameters, long deprecated, are gone.

The other subclass handles connections set up by a child process:

[Subject index](INDEX.md) · [Previous](imaplib-imap4-class-to-imap4-readonly.md) · [Continue](imaplib-imap4-stream-class.md) · [Owning module, declaration or section: imaplib](imaplib-imap4-class-to-imap4-readonly.md)
