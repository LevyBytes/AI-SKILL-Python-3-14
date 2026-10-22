# What’s New In Python 3.5 / ssl / Memory BIO Support — ssl

### ssl

#### Memory BIO Support

Geert Jansen contributed this (see [bpo-21965](https://bugs.python.org/issue?@action=redirect&bpo=21965)).

To cover situations where the network I/O features of [`SSLSocket`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLSocket) are either unwanted or a poor fit, the new [`SSLObject`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLObject) class now supplies SSL protocol support. Although `SSLObject` models an SSL protocol instance, it offers no network I/O methods at all, exposing a memory buffer interface in their place. To shuttle data between Python and an SSL protocol instance, you can rely on the new [`MemoryBIO`](https://docs.python.org/3.14/library/ssl.html#ssl.MemoryBIO) class.

This memory BIO SSL capability mainly targets frameworks that build asynchronous I/O, where the readiness model (“select/poll”) of [`SSLSocket`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLSocket) performs poorly.

To spin up a fresh `SSLObject` instance, you can call the new [`SSLContext.wrap_bio()`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext.wrap_bio) method.

[Subject index](INDEX.md) · [Previous source section](socket.md) · [Next source section](ssl-application-layer-protocol-negotiation-support.md) · [Release/subject declaration](summary-release-highlights.md)
