# Python 3.7.0 beta 2 / library / constructing sslsocket sslobject objects directly disallowed

[bpo-32951](https://bugs.python.org/issue?@action=redirect&bpo=32951): Constructing SSLSocket and SSLObject objects directly is now disallowed. Those constructors were never documented, tested, or meant to serve as public constructors. The expectation was that users would rely on ssl.wrap_socket() or SSLContext.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
