# Python 3.11.0 alpha 2 / library / xmlrpc client

[bpo-45386](https://bugs.python.org/issue?@action=redirect&bpo=45386): Harden [`xmlrpc.client`](https://docs.python.org/3.14/library/xmlrpc.client.html#module-xmlrpc.client) against C runtimes whose underlying C `strftime` function yields a `ValueError` while probing year formatting options.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
