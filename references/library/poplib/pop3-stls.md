# poplib: `POP3.stls()`

`POP3.stls(*context=None*)`

Begin a TLS session over the live connection, following [**RFC 2595**](https://datatracker.ietf.org/doc/html/rfc2595.html). It may only be done prior to user authentication

The *context* argument is a [`ssl.SSLContext`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext) object that lets you fold SSL settings, certificates and private keys into one (potentially long-lived) structure. For recommended practice, consult [Security considerations](https://docs.python.org/3.14/library/ssl.html#ssl-security).

Hostname verification through [`ssl.SSLContext.check_hostname`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext.check_hostname) and *Server Name Indication* (see [`ssl.HAS_SNI`](https://docs.python.org/3.14/library/ssl.html#ssl.HAS_SNI)) is supported by this method.

Added in version 3.4.

A `POP3_SSL` instance brings no extra methods of its own; this subclass presents the very same interface as its parent.

[Subject index](INDEX.md) · [Previous](pop3-set-debuglevel-to-pop3-utf8.md) · [Continue](pop3-example.md) · [Owning module, declaration or section: poplib](poplib-pop3-class.md) · [Owning module, declaration or section: POP3 Objects](pop3-set-debuglevel-to-pop3-utf8.md)
