# Python 3.8.0 alpha 1 / library / directly instantiating sslsocket sslobject objects disallowed

[bpo-32951](https://bugs.python.org/issue?@action=redirect&bpo=32951): Directly instantiating SSLSocket and SSLObject objects is now disallowed. Those constructors were never documented, tested, or intended as public constructors. Users were meant to rely on ssl.wrap_socket() or SSLContext.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
