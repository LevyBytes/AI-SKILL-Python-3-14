# poplib: `poplib.POP3_SSL`

`class poplib.POP3_SSL(*host*, *port=POP3_SSL_PORT*, ***, *timeout=None*, *context=None*)`

A derivative of `POP3`, this one reaches the server through an SSL-encrypted socket. Omit *port* and 995, the conventional POP3-over-SSL port, takes effect. The *timeout* behaves exactly as it does in the `POP3` constructor. The *context* slot accepts an optional [`ssl.SSLContext`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext) object, by which SSL settings, certificates and private keys can be gathered into one (potentially long-lived) structure. For recommended practice, see [Security considerations](https://docs.python.org/3.14/library/ssl.html#ssl-security).

Fires an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `poplib.connect` with the arguments `self`, `host`, `port`.

All issued commands raise an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `poplib.putline` with `self` plus `line`, where `line` denotes the bytes queued for delivery to the remote host.

Changed in version 3.2: *context* parameter added.

Changed in version 3.4: Hostname verification via [`ssl.SSLContext.check_hostname`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext.check_hostname), together with *Server Name Indication* ([`ssl.HAS_SNI`](https://docs.python.org/3.14/library/ssl.html#ssl.HAS_SNI)), is handled by the class from this release on.

Changed in version 3.9: Supplying zero as the *timeout* argument now raises a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError), preventing a non-blocking socket from being created.

Changed in version 3.12: The *keyfile* plus *certfile* arguments, long deprecated, are gone as of this version.

A lone exception sits as an attribute on the `poplib` module:

[Subject index](INDEX.md) · [Previous](poplib-pop3-class.md) · [Continue](poplib-error-proto.md) · [Owning module, declaration or section: poplib](poplib-pop3-class.md)
