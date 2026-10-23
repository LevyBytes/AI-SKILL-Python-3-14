# What’s New In Python 3.5 / xmlrpc - ssl, xmlrpc.client

### xmlrpc

You can now drive the [`client.ServerProxy`](https://docs.python.org/3.14/library/xmlrpc.client.html#xmlrpc.client.ServerProxy) class with the [context manager](https://docs.python.org/3.14/glossary.html#term-context-manager) protocol. (Contributed by Claudiu Popa in [bpo-20627](https://bugs.python.org/issue?@action=redirect&bpo=20627).)

An optional [`ssl.SSLContext`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext) instance may now be supplied to the [`client.ServerProxy`](https://docs.python.org/3.14/library/xmlrpc.client.html#xmlrpc.client.ServerProxy) constructor. (Contributed by Alex Gaynor in [bpo-22960](https://bugs.python.org/issue?@action=redirect&bpo=22960).)

[Subject index](INDEX.md) · [Previous source section](wsgiref.md) · [Next source section](xml-sax.md) · [Release/subject declaration](summary-release-highlights.md)
